---
name: pdf-rtl-page-direction
description: Fix a PDF whose two-page/facing-page/spread view shows pages in the wrong order for a right-to-left book (Hebrew, Arabic, etc) — e.g. the left-hand page displays before the right-hand page, or a user says a PDF "opens backwards", "two-page view is wrong/reversed", "shows left page then right page", "pages are swapped in spread view", or "doesn't flip like a Hebrew/Arabic book". Also use when comparing two RTL PDFs where one behaves correctly and one doesn't, to diagnose the difference. Does NOT apply to single-page scrolling/reading order (that's just the page stream order) or to EPUB scroll/paging direction (see the pdf-to-epub skill for EPUB RTL issues) — this is specifically about PDF two-up/spread viewer layout.
---

# PDF two-page (spread) view — RTL direction fix

## What's actually wrong

PDF viewers decide which page appears on the left vs. right in a two-page/facing-page
spread from exactly one document-level setting: `ViewerPreferences/Direction` in the
PDF's catalog dictionary.

- `/R2L` → spreads lay out right-to-left (page 1 on the right — correct for a
  physical Hebrew/Arabic book opened from its right-bound spine).
- Missing entirely, or `/L2R` → spreads lay out left-to-right (the default every
  viewer falls back to, regardless of whether the page content itself is Hebrew/Arabic).

This is **not** about the text direction, fonts, or page content in any way — a PDF
full of Hebrew text can still be missing this flag. In practice this flag is present
when a book was produced by a real layout tool (Adobe InDesign, etc. — these set it
automatically when the document's binding direction is configured as RTL) and is
usually missing when a book went through a generic/naive PDF tool (seen in the wild:
Online2PDF.com and similar web converters, which have no concept of RTL books and
never write this flag).

## Diagnosing (do this first, especially when comparing two files)

```python
import sys
sys.path.insert(0, r"C:\Users\user\.claude\skills\pdf-rtl-page-direction\scripts")
from fix_pdf_rtl_direction import diagnose

info = diagnose(r"path\to\book.pdf")
# info['direction'] is None (not set), 'R2L', or 'L2R'
# info['producer'] / info['creator'] often explains *why* (InDesign vs. a generic converter)
```

If comparing a "broken" book against a "working" one, run `diagnose()` on both and
show the user the `direction` and `producer`/`creator` fields side by side — that's
usually enough to both explain the cause and confirm the fix target.

## Fixing

```python
import sys
sys.path.insert(0, r"C:\Users\user\.claude\skills\pdf-rtl-page-direction\scripts")
from fix_pdf_rtl_direction import fix_pdf_direction

fix_pdf_direction(r"path\to\book.pdf", r"path\to\book (RTL).pdf")  # direction='R2L' by default
```

This is a single, tiny, non-destructive catalog edit — it does not touch page content,
images, or text in any way. It's idempotent (safe to run on an already-correct PDF,
or to run twice) and preserves any other existing `ViewerPreferences` keys the book
might already have.

- Pass `direction='L2R'` only if a user specifically wants to *remove* RTL spread
  order (rare — confirm this is really what they want, since almost every real
  request is "make my Hebrew/Arabic book page correctly," i.e. R2L).
- Write to a new file (e.g. `"<name> (RTL).pdf"`) by default, matching how other
  fixes in this environment are delivered — don't overwrite the user's original
  unless they've asked for in-place editing.
- The script raises a clear error on encrypted/password-protected PDFs rather than
  silently failing — decrypt first if that happens.

## Non-ASCII (Hebrew/Arabic) filenames — read this before running anything

Windows + Git Bash (MSYS) can inconsistently mangle non-ASCII characters when
spawning a Python subprocess with a Hebrew/Arabic path embedded in the command —
sometimes it works, sometimes the same path comes back corrupted with `�`
replacement characters and a resulting `FileNotFoundError`, even though the file is
genuinely present. This is environment fragility, not a bug in the fix logic itself.

- **Prefer the PowerShell tool over Bash** for any command that embeds a
  Hebrew/Arabic path directly (it handles Unicode natively and doesn't go through
  the MSYS argv-translation layer that causes the mangling).
- If a `FileNotFoundError` comes back with visibly garbled/mangled characters in the
  path (question marks, `�`, boxes) — that's the encoding bug; retry the exact same
  call via PowerShell instead of debugging the Python code.
- If a `FileNotFoundError` comes back with the path rendering *correctly* (readable
  Hebrew/Arabic) — that's very likely a **real** missing file, not an encoding
  artifact. Verify with `Test-Path` / `Get-ChildItem` in PowerShell before assuming
  it's a code bug; don't waste time re-debugging the script itself in that case.
- Either way, write a small driver `.py` file (via the Write tool, which writes
  correct UTF-8) and run *that* rather than passing the Hebrew path as an inline
  CLI argument or deep inside a Bash heredoc — this sidesteps most of the mangling
  regardless of which shell tool you use.

## Reference

- `scripts/fix_pdf_rtl_direction.py` — `diagnose(path)` (read-only report) and
  `fix_pdf_direction(src, dst, direction='R2L')` (the fix). Also runnable directly:
  `python fix_pdf_rtl_direction.py input.pdf [output.pdf] [--direction R2L|L2R] [--in-place]`
  — but for Hebrew/Arabic-named files, call the functions from a driver script
  instead of relying on shell CLI argv (see above).
