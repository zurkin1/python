---
name: pdf-split-spreads
description: Split a PDF where each page holds two book pages side by side (scanned book spreads, "two pages per sheet", "2-up") into single pages, cutting in the blank gutter of each page rather than the fixed middle, in right-to-left order for Hebrew/Arabic books (or left-to-right). Use when the user asks to "split this pdf" and the pages are spreads, says "each pdf page contains two pages", or complains that a split cut through text.
---

# Split two-page spreads into single pages

## Workflow

1. **Inspect first.** With PyMuPDF (`fitz`), print page count and cropbox sizes, and render
   2–3 pages (first, a middle one, last) at ~40 dpi to see that they really are spreads.
   Landscape = spread, portrait = single page (the script copies portrait pages unchanged).
2. **Order.** Hebrew/Arabic → right half first (default). Latin books → `--ltr`.
3. **Split:**
   ```
   python ~/.claude/skills/pdf-split-spreads/scripts/split_spreads.py "<in.pdf>" --cuts <scratch>/cuts.json
   ```
   The output goes next to the input as `<name> - split.pdf`. The original is left untouched.
4. **Verify before reporting done:**
   ```
   python ~/.claude/skills/pdf-split-spreads/scripts/check_cuts.py <scratch>/cuts.json <scratch>/check
   ```
   Read the `check_*.png` images. Each strip is a zoom on one cut: the red line must run
   through blank gutter, not through letters. Check any page the user complained about with
   `--pages`. Also render 3–4 consecutive output pages to confirm the reading order.
5. **Report** the page counts and the order used. If you used the overlap, mention that
   some pages show a thin sliver of the facing page at the inner edge.

## Lessons (from a real failure)

- **Never cut at the fixed middle.** On scans the gutter drifts from page to page, and a
  middle cut chopped the ends of text lines.
- **Don't pick the widest blank area.** On chapter openers and half-empty pages the widest
  blank run is inside a page, far from the gutter. Pick the safe column **closest to
  centre**.
- **Measure ink by vertical black/white transitions, not darkness.** A dark gutter shadow
  is solid (few transitions), so it counts as safe; text has many transitions.
- **Tight or skewed gutters** have no fully clean column, so the script falls back to the
  least-ink column and lists those pages. Margin labels (e.g. "לוח 2.1") often sit in the
  gutter. The default 6 pt overlap keeps them whole. Raise `--overlap` if letters still
  get clipped, or set `--overlap 0` if the user wants no sliver of the facing page.
- Splitting only sets the cropbox. The image is not re-rendered, so there is no quality loss.
- For a PDF whose two-page *viewer* layout is reversed, use `pdf-rtl-page-direction`
  instead. That is a different problem.
