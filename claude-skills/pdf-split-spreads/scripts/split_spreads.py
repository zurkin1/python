"""Split a PDF whose pages are two-page spreads (scanned book) into single pages.

The cut is placed per page in the text-free gutter, not at the fixed middle:
  - render each page at low DPI, grayscale, binarize
  - per column, count vertical black/white transitions (text = many; blank or
    solid gutter shadow = few)
  - "safe" columns = transitions <= max(2, min+2) in the central 30-70% band
  - cut at the safe column (with +-3 safe neighbours) CLOSEST to the page centre
    (NOT the widest blank run: half-empty chapter-opener pages would win that)
  - if no such column exists (tight/skewed gutter), fall back to the least-ink column
Each half extends OVERLAP pt past the cut so labels sitting in the gutter stay whole.
Portrait pages (width < height) are treated as single pages and copied unchanged.

Usage:
  python split_spreads.py input.pdf [-o out.pdf] [--ltr] [--overlap 6] [--cuts cuts.json]
Default order is RTL (right half first) for Hebrew/Arabic; --ltr for left half first.
"""
import argparse, json, os
import fitz
import numpy as np


def find_cut(page, dpi=60, band=(0.3, 0.7), margin=3):
    pix = page.get_pixmap(dpi=dpi, colorspace=fitz.csGRAY)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.h, pix.stride)[:, :pix.w]
    h, w = a.shape
    b = (a[int(h * .03):int(h * .97)] < 128).astype(np.int8)
    trans = np.abs(np.diff(b, axis=0)).sum(0).astype(float)
    lo, hi = int(w * band[0]), int(w * band[1])
    seg = trans[lo:hi]
    safe = seg <= max(2, seg.min() + 2)
    ok = np.array([safe[max(0, j - margin):j + margin + 1].all() for j in range(len(seg))])
    if ok.any():
        idx = np.where(ok)[0]
        j = int(idx[np.argmin(abs(idx - (w * 0.5 - lo)))])
        fallback = False
    else:
        j = int(np.argmin(np.convolve(seg, np.ones(2 * margin + 1), 'same')))
        fallback = True
    return (lo + j) / w, fallback


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('-o', '--output')
    ap.add_argument('--ltr', action='store_true', help='left half first (default: right half first)')
    ap.add_argument('--overlap', type=float, default=6, help='pt each half extends past the cut')
    ap.add_argument('--cuts', help='write per-page cut positions to this json (for check_cuts.py)')
    args = ap.parse_args()
    out_path = args.output or os.path.splitext(args.input)[0] + ' - split.pdf'

    src = fitz.open(args.input)
    out = fitz.open()
    cuts = []
    for i, p in enumerate(src):
        cb = p.cropbox
        if cb.width < cb.height:  # already a single page
            out.insert_pdf(src, from_page=i, to_page=i)
            cuts.append({'page': i, 'frac': None, 'fallback': False})
            continue
        frac, fb = find_cut(p)
        cuts.append({'page': i, 'frac': round(frac, 4), 'fallback': fb})
        x = cb.x0 + frac * cb.width
        right = fitz.Rect(x - args.overlap, cb.y0, cb.x1, cb.y1)
        left = fitz.Rect(cb.x0, cb.y0, x + args.overlap, cb.y1)
        for r in ((left, right) if args.ltr else (right, left)):
            out.insert_pdf(src, from_page=i, to_page=i)
            out[-1].set_cropbox(r)
    out.set_metadata(src.metadata)
    out.save(out_path, garbage=3, deflate=True)

    if args.cuts:
        json.dump({'input': os.path.abspath(args.input), 'cuts': cuts}, open(args.cuts, 'w'), indent=0)
    fbs = [c['page'] for c in cuts if c['fallback']]
    print(f'{len(src)} pages -> {len(out)} pages: {out_path}')
    print(f'fallback (narrow/skewed gutter, check these): {fbs}')


if __name__ == '__main__':
    main()
