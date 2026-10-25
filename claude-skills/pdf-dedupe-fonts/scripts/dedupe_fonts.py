"""Shrink a PDF by sharing byte-identical font data across pages.

Targets PDFs where every page carries its own copy of the same fonts, typically
Type3 fonts (each letter stored as a small drawing, re-embedded per page).
Only exact duplicates (same decoded bytes + same stream dictionary) are merged,
so rendering cannot change. Everything else is left as it is.

Optional --jpx re-encodes page images (e.g. scans) as JPEG2000. That is lossy, so
verification then checks a per-page pixel difference limit instead of exact equality.

Usage:
    python dedupe_fonts.py "<in.pdf>" [-o "<out.pdf>"] [--no-verify] [--dpi 72]
                           [--jpx] [--jpx-rate 150] [--max-diff 6]
Output defaults to "<name> - small.pdf" next to the input. The input is never modified.
"""
import argparse, hashlib, io, os, sys
import fitz
import numpy as np
import pikepdf
from PIL import Image

FONT_FILE_KEYS = ("/FontFile", "/FontFile2", "/FontFile3")


def stream_key(stream):
    d = {k: str(v) for k, v in stream.items() if k not in ("/Length", "/Filter", "/DecodeParms")}
    return hashlib.sha256(repr(sorted(d.items())).encode() + stream.read_bytes()).hexdigest()


def dedupe(pdf):
    canon = {}
    stats = {"type3_fonts": 0, "other_fonts": 0, "glyphs": 0, "glyphs_shared": 0,
             "tounicode": 0, "tounicode_shared": 0, "fontfiles": 0, "fontfiles_shared": 0}

    def share(stream, kind):
        k = (kind, stream_key(stream))
        if k in canon:
            return canon[k], canon[k].objgen != stream.objgen
        canon[k] = stream
        return stream, False

    for obj in pdf.objects:
        if not isinstance(obj, pikepdf.Dictionary) or obj.get("/Type") != "/Font":
            continue
        if obj.get("/Subtype") == "/Type3" and "/CharProcs" in obj:
            stats["type3_fonts"] += 1
            procs = obj.CharProcs
            for g in list(procs.keys()):
                stats["glyphs"] += 1
                new, dup = share(procs[g], "glyph")
                if dup:
                    procs[g] = new
                    stats["glyphs_shared"] += 1
        else:
            stats["other_fonts"] += 1
            descs = [obj.get("/FontDescriptor")]
            for desc_font in obj.get("/DescendantFonts", []):
                descs.append(desc_font.get("/FontDescriptor"))
            for desc in descs:
                if not isinstance(desc, pikepdf.Dictionary):
                    continue
                for fk in FONT_FILE_KEYS:
                    if fk in desc:
                        stats["fontfiles"] += 1
                        new, dup = share(desc[fk], "fontfile")
                        if dup:
                            desc[fk] = new
                            stats["fontfiles_shared"] += 1
        tu = obj.get("/ToUnicode")
        if isinstance(tu, pikepdf.Stream):
            stats["tounicode"] += 1
            new, dup = share(tu, "tounicode")
            if dup:
                obj.ToUnicode = new
                stats["tounicode_shared"] += 1
    return stats


def recompress_images(pdf, rate):
    """Re-encode raster images as JPEG2000 where that is smaller. rate = compression ratio vs raw 8-bit."""
    stats = {"images": 0, "images_jpx": 0, "image_mb_before": 0, "image_mb_after": 0}
    for obj in pdf.objects:
        if not isinstance(obj, pikepdf.Stream) or obj.get("/Subtype") != "/Image":
            continue
        if obj.get("/ImageMask", False) or isinstance(obj.get("/Mask"), pikepdf.Array):
            continue # Stencil masks and color-key masks depend on exact sample values.
        filters = obj.get("/Filter")
        filters = list(filters) if isinstance(filters, pikepdf.Array) else [filters]
        if "/JPXDecode" in filters:
            continue
        stats["images"] += 1
        before = len(obj.read_raw_bytes())
        try:
            im = pikepdf.PdfImage(obj).as_pil_image()
        except Exception:
            continue
        if im.mode in ("1", "L"):
            im, cs = im.convert("L"), pikepdf.Name.DeviceGray
        elif im.mode in ("RGB", "P"):
            im, cs = im.convert("RGB"), pikepdf.Name.DeviceRGB
        else:
            continue # CMYK/Lab etc.: converting would shift colors.
        buf = io.BytesIO()
        im.save(buf, "JPEG2000", quality_mode="rates", quality_layers=[rate], irreversible=True)
        data = buf.getvalue()
        stats["image_mb_before"] += before / 1e6
        if len(data) >= before:
            stats["image_mb_after"] += before / 1e6
            continue
        obj.write(data, filter=pikepdf.Name.JPXDecode)
        obj.ColorSpace = cs
        obj.BitsPerComponent = 8
        for k in ("/Decode", "/DecodeParms"):
            if k in obj:
                del obj[k]
        stats["images_jpx"] += 1
        stats["image_mb_after"] += len(data) / 1e6
    stats["image_mb_before"] = round(stats["image_mb_before"], 2)
    stats["image_mb_after"] = round(stats["image_mb_after"], 2)
    return stats


def verify(src, dst, dpi, max_diff=None):
    """Exact pixel match when max_diff is None, else per-page mean abs difference (0-255) <= max_diff."""
    a, b = fitz.open(src), fitz.open(dst)
    if a.page_count != b.page_count:
        return False, f"page count differs: {a.page_count} vs {b.page_count}"
    pix_bad, txt_bad, worst = [], [], 0.0
    for i in range(a.page_count):
        pa, pb = a[i].get_pixmap(dpi=dpi).samples, b[i].get_pixmap(dpi=dpi).samples
        if max_diff is None:
            if pa != pb:
                pix_bad.append(i + 1)
        else:
            diff = 0.0 if len(pa) != len(pb) else float(np.abs(
                np.frombuffer(pa, np.uint8).astype(np.int16) - np.frombuffer(pb, np.uint8)).mean())
            worst = max(worst, diff)
            if len(pa) != len(pb) or diff > max_diff:
                pix_bad.append(i + 1)
        if a[i].get_text() != b[i].get_text():
            txt_bad.append(i + 1)
    links_a = sum(len(p.get_links()) for p in a)
    links_b = sum(len(p.get_links()) for p in b)
    problems = []
    if pix_bad: problems.append(f"pixel diffs on pages {pix_bad[:20]}")
    if txt_bad: problems.append(f"text diffs on pages {txt_bad[:20]}")
    if a.get_toc() != b.get_toc(): problems.append("bookmarks differ")
    if links_a != links_b: problems.append(f"link count {links_a} vs {links_b}")
    if max_diff is None:
        ok_msg = f"all {a.page_count} pages identical (pixels, text, bookmarks, links)"
    else:
        ok_msg = f"all {a.page_count} pages within pixel diff {max_diff} (worst {worst:.2f}); text, bookmarks, links identical"
    return not problems, "; ".join(problems) or ok_msg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output")
    ap.add_argument("--no-verify", action="store_true")
    ap.add_argument("--dpi", type=int, default=72)
    ap.add_argument("--jpx", action="store_true", help="re-encode images as JPEG2000 (lossy)")
    ap.add_argument("--jpx-rate", type=float, default=150, help="JPEG2000 compression ratio; higher = smaller/blurrier")
    ap.add_argument("--max-diff", type=float, default=6, help="with --jpx: allowed mean pixel diff per page (0-255)")
    args = ap.parse_args()

    out = args.output or os.path.splitext(args.input)[0] + " - small.pdf"
    if os.path.abspath(out) == os.path.abspath(args.input):
        sys.exit("output must differ from input")

    pdf = pikepdf.open(args.input)
    stats = dedupe(pdf)
    if args.jpx:
        stats.update(recompress_images(pdf, args.jpx_rate))
    pdf.remove_unreferenced_resources()
    pdf.save(out, object_stream_mode=pikepdf.ObjectStreamMode.generate, compress_streams=True)
    pdf.close()

    before, after = os.path.getsize(args.input), os.path.getsize(out)
    print(stats)
    print(f"{before/1e6:.2f} MB -> {after/1e6:.2f} MB ({100*(1-after/before):.0f}% smaller)")
    print("output:", out)
    if not args.no_verify:
        ok, msg = verify(args.input, out, args.dpi, args.max_diff if args.jpx else None)
        print("VERIFY", "OK:" if ok else "FAILED:", msg)
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    main()
