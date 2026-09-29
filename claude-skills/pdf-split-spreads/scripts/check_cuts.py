"""Render zoomed strips around each cut line so they can be eyeballed for cut text.

Usage:
  python check_cuts.py cuts.json outdir [--pages 3,17,40] [--all]
Default: fallback pages + the 6 cuts farthest from centre. Writes check_*.png (13 strips each).
"""
import argparse, json, os
import fitz
from PIL import Image, ImageDraw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cuts')
    ap.add_argument('outdir')
    ap.add_argument('--pages')
    ap.add_argument('--all', action='store_true')
    args = ap.parse_args()
    data = json.load(open(args.cuts))
    d = fitz.open(data['input'])
    cuts = {c['page']: c for c in data['cuts'] if c['frac'] is not None}
    if args.pages:
        sel = [int(x) for x in args.pages.split(',')]
    elif args.all:
        sel = sorted(cuts)
    else:
        sel = [p for p, c in cuts.items() if c['fallback']]
        sel += [p for p in sorted(cuts, key=lambda p: -abs(cuts[p]['frac'] - 0.5))[:6] if p not in sel]
    os.makedirs(args.outdir, exist_ok=True)
    ims = []
    for i in sel:
        pix = d[i].get_pixmap(dpi=70)
        im = Image.frombytes('RGB', (pix.w, pix.h), pix.samples)
        x = int(cuts[i]['frac'] * pix.w)
        im = im.crop((x - 45, 0, x + 45, pix.h))
        dr = ImageDraw.Draw(im)
        dr.line([(45, 0), (45, pix.h)], fill='red', width=1)
        dr.text((2, 2), str(i), fill='blue')
        ims.append(im)
    per = 13
    for k in range(0, len(ims), per):
        row = ims[k:k + per]
        s = Image.new('RGB', (95 * len(row), max(im.height for im in row)), 'white')
        for n, im in enumerate(row):
            s.paste(im, (n * 95, 0))
        p = os.path.join(args.outdir, f'check_{k // per:02d}.png')
        s.save(p)
        print(p)


if __name__ == '__main__':
    main()
