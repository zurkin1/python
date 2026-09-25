# -*- coding: utf-8 -*-
"""
Fix a PDF whose two-page ("spread"/"facing pages") viewer mode shows pages
in the wrong order for a right-to-left (Hebrew/Arabic) book — i.e. the
LEFT-hand page is shown first, then the right, when it should be the
reverse for an RTL book (page 1 on the right, like a physical Hebrew/Arabic
book opened from its right-bound spine).

Root cause (confirmed by diffing a correctly-behaving book against a broken
one): PDF viewers decide left/right spread order from exactly one catalog
setting, `ViewerPreferences/Direction`. `/R2L` -> right-to-left spreads
(page 1 on the right). Missing entirely, or `/L2R` -> left-to-right spreads
(the default every viewer falls back to). This has NOTHING to do with the
page content, text direction, or font — a Hebrew book with Hebrew text can
still be missing this flag if it was produced by a generic/naive PDF
tool (seen in the wild: Online2PDF.com and similar web converters) rather
than a real layout tool (Adobe InDesign etc, which sets this automatically
when the document's binding direction is configured as RTL).

This is a single, tiny, non-destructive catalog edit — it does not touch
page content, images, or text in any way, so it's always safe to apply to
a Hebrew/Arabic book if you're unsure whether it's already set (the fix is
idempotent: running it on an already-correct PDF is a harmless no-op).

Usage:
    python fix_pdf_rtl_direction.py input.pdf [output.pdf] [--direction R2L|L2R] [--in-place]

    - With no output path and no --in-place: writes "<input> (RTL).pdf"
      next to the input (or "(LTR)" if --direction L2R).
    - --in-place overwrites the input file directly (still safe: PyMuPDF
      writes to a temp file and replaces atomically).
    - --direction defaults to R2L (the overwhelmingly common real request
      — "my Hebrew/Arabic book's two-page view is backwards"). Pass L2R
      only if you specifically need to *remove* RTL spread order.

For non-ASCII (e.g. Hebrew-named) file paths on Windows, prefer calling
`fix_pdf_direction()` directly from a small driver script over relying on
shell CLI argv, which can mangle non-ASCII arguments:
    import sys
    sys.path.insert(0, r"<path to this scripts/ dir>")
    from fix_pdf_rtl_direction import fix_pdf_direction
    fix_pdf_direction(r"C:\path\to\<hebrew name>.pdf", r"C:\path\to\<hebrew name> (RTL).pdf")
"""
import argparse
import os
import re
import shutil
import tempfile

import fitz  # PyMuPDF


def diagnose(path: str) -> dict:
    """Report the PDF's current ViewerPreferences/Direction state without
    changing anything. Useful to explain *why* a book is misbehaving before
    fixing it, and to confirm a fix actually took effect afterward."""
    doc = fitz.open(path)
    try:
        cat_xref = doc.pdf_catalog()
        cat_obj = doc.xref_object(cat_xref)
        vp_match = re.search(r'/ViewerPreferences\s*<<(.*?)>>', cat_obj, re.DOTALL)
        direction = None
        if vp_match:
            dmatch = re.search(r'/Direction\s*/(\w+)', vp_match.group(1))
            if dmatch:
                direction = dmatch.group(1)
        return {
            'path': path,
            'page_count': len(doc),
            'producer': doc.metadata.get('producer', ''),
            'creator': doc.metadata.get('creator', ''),
            'page_layout': doc.xref_get_key(cat_xref, 'PageLayout')[1] if doc.xref_get_key(cat_xref, 'PageLayout')[0] != 'null' else None,
            'has_viewer_preferences': vp_match is not None,
            'direction': direction,  # None | 'R2L' | 'L2R'
            'encrypted': doc.is_encrypted,
        }
    finally:
        doc.close()


def fix_pdf_direction(src: str, dst: str, direction: str = 'R2L'):
    """Set ViewerPreferences/Direction on the PDF at `src`, writing the
    result to `dst` (which may equal `src` for an in-place edit — this
    writes to a temp file first and replaces atomically, so that's safe).

    Preserves any OTHER existing keys already inside ViewerPreferences
    (e.g. a book might already have /FitWindow or /HideToolbar set) —
    only the /Direction entry is added or overwritten, everything else in
    that dict is left alone. Idempotent: running this twice, or against a
    PDF that already has the requested direction, is a harmless no-op that
    still produces a valid rewritten file.
    """
    assert direction in ('R2L', 'L2R'), "direction must be 'R2L' or 'L2R'"

    doc = fitz.open(src)
    if doc.is_encrypted:
        doc.close()
        raise RuntimeError(
            f"{src} is password-protected/encrypted — decrypt it first, "
            "PyMuPDF can't safely rewrite the catalog of an encrypted PDF."
        )

    cat_xref = doc.pdf_catalog()
    cat_obj = doc.xref_object(cat_xref)

    vp_match = re.search(r'/ViewerPreferences\s*<<(.*?)>>', cat_obj, re.DOTALL)
    if vp_match:
        inner = vp_match.group(1)
        if '/Direction' in inner:
            inner = re.sub(r'/Direction\s*/\w+', f'/Direction /{direction}', inner)
        else:
            inner = inner.rstrip() + f' /Direction /{direction} '
        new_vp = f'<<{inner}>>'
    else:
        new_vp = f'<< /Direction /{direction} >>'

    doc.xref_set_key(cat_xref, 'ViewerPreferences', new_vp)

    fd, tmp = tempfile.mkstemp(suffix='.pdf', dir=os.path.dirname(os.path.abspath(dst)) or '.')
    os.close(fd)
    try:
        doc.save(tmp, garbage=0, deflate=False, incremental=False)
        doc.close()
        shutil.move(tmp, dst)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    print(f'fixed ({direction}) -> {dst}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('input')
    ap.add_argument('output', nargs='?', default=None)
    ap.add_argument('--direction', choices=['R2L', 'L2R'], default='R2L')
    ap.add_argument('--in-place', action='store_true')
    args = ap.parse_args()

    info = diagnose(args.input)
    print(f"page count: {info['page_count']}")
    print(f"producer/creator: {info['producer']} / {info['creator']}")
    print(f"current ViewerPreferences/Direction: {info['direction'] or '(not set — defaults to L2R in every viewer)'}")

    if args.in_place:
        out = args.input
    elif args.output:
        out = args.output
    else:
        base, ext = os.path.splitext(args.input)
        suffix = ' (RTL)' if args.direction == 'R2L' else ' (LTR)'
        out = f'{base}{suffix}{ext}'

    fix_pdf_direction(args.input, out, args.direction)
