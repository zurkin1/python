---
name: pdf-dedupe-fonts
description: Shrink a text-based (not scanned) PDF that is unexpectedly large because every page re-embeds its own copy of the same fonts — typically Type3 fonts, where each letter is stored as a small drawing and repeated on every page. Merges only byte-identical glyphs, ToUnicode maps and font files into one shared copy, then verifies every page renders pixel-identical. Use when the user asks why a regular (non-scanned) PDF book is so big, wants to shrink/compress/reduce a PDF whose size comes from fonts, or says the fonts are duplicated per page.
---

# Shrink a PDF by sharing duplicate font data

## 1. Diagnose first

Confirm the size really comes from fonts before running anything. With PyMuPDF (`fitz`):

- `page.get_fonts()` over all pages: count distinct font xrefs. Hundreds or thousands of
  fonts in a book = per-page copies. A `Type3` subtype with name `n/a` is the classic case.
- Sum raw stream sizes by kind: images (`/Subtype /Image`), Type3 `CharProcs` glyph
  streams, page content streams, font files. If images dominate, this skill won't help.
- Hash the decoded glyph streams: number unique vs total shows the possible saving.

Real case: a 400-page Hebrew textbook (Cormen), 19.4 MB. It had 2,727 Type3 fonts and
38,556 glyph drawings, but only 565 unique glyphs. Glyphs were ~55% of the file.
Result: 5.8 MB, all pages pixel-identical.

## 2. Run

```
python ~/.claude/skills/pdf-dedupe-fonts/scripts/dedupe_fonts.py "<in.pdf>"
```

- Writes `<name> - small.pdf` next to the input (`-o` to choose). Never modifies the input.
- What it merges (exact byte match only, so rendering cannot change):
  - Type3 glyph procedures (`CharProcs`) across all Type3 fonts
  - `ToUnicode` CMaps
  - Embedded font files (`FontFile`/`FontFile2`/`FontFile3`) for normal fonts
- Then it drops unreferenced objects and saves with object streams.
- It verifies automatically: renders every page of both files (72 dpi; `--dpi` to change)
  and compares pixels, plus text per page, bookmarks and link count. It exits 1 on any
  difference. Don't report success unless it prints `VERIFY OK`.

Requires `pikepdf` and `pymupdf`. Run with plain `python` (not `-I`), or the user
site-packages are hidden.

## 3. Report

Before/after size, how many glyphs/fonts were shared, and the verify result.

## Limits

- Font *dictionaries* stay per page, since each page's encoding/widths can differ. Only
  the heavy streams are shared. That is what makes it safe.
- Near-identical glyphs (tiny float differences) are deliberately not merged.
- Scanned PDFs (size from images) need image recompression instead. That is a different job.
