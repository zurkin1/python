"""Switch an EPUB from horizontal paging to vertical (continuous) scrolling.

Usage: python epub_vertical_scroll.py "c:\\github\\book.epub" [output.epub]
If no output is given, writes "<name>-vertical.epub" next to the input.
"""
import re
import sys
import zipfile
from pathlib import Path

FLOW_META = '<meta property="rendition:flow">scrolled-continuous</meta>'
APPLE_OPTIONS = 'META-INF/com.apple.ibooks.display-options.xml'
APPLE_XML = ('<?xml version="1.0" encoding="UTF-8"?>\n<display_options>\n'
             '  <platform name="*">\n'
             '    <option name="scroll-axis">vertical</option>\n'
             '  </platform>\n</display_options>\n')


def find_opf(z):
    container = z.read('META-INF/container.xml').decode('utf-8')
    return re.search(r'full-path="([^"]+)"', container).group(1)


def fix_opf(opf):
    # Drop any existing rendition:flow / rendition:layout overrides that force paging.
    opf = re.sub(r'\s*<meta[^>]*property="rendition:flow"[^>]*>.*?</meta>', '', opf, flags=re.S)
    opf = re.sub(r'\s*<meta[^>]*property="rendition:flow"[^>]*/>', '', opf)
    # Per-itemref overrides (e.g. rendition:flow-paginated) in the spine.
    opf = re.sub(r'\s*rendition:flow-[a-z-]+', '', opf)
    opf = re.sub(r'\sproperties="\s*"', '', opf)
    # The rendition prefix is required for EPUB3 readers to honor the property.
    package_tag = re.search(r'<package[^>]*>', opf).group(0)
    if 'rendition:' not in package_tag:
        if 'prefix="' in package_tag:
            opf = re.sub(r'(<package[^>]*prefix=")', r'\1rendition: http://www.idpf.org/vocab/rendition/# ', opf, count=1)
        else:
            opf = re.sub(r'<package', '<package prefix="rendition: http://www.idpf.org/vocab/rendition/#"', opf, count=1)
    return re.sub(r'</metadata>', f'  {FLOW_META}\n  </metadata>', opf, count=1)


def fix_apple(xml):
    if 'scroll-axis' in xml:
        return re.sub(r'(<option name="scroll-axis">)[^<]*', r'\1vertical', xml)
    return re.sub(r'(<platform[^>]*>)', r'\1\n    <option name="scroll-axis">vertical</option>', xml, count=1)


def main(src, dst=None):
    src = Path(src)
    dst = Path(dst) if dst else src.with_name(src.stem + '-vertical.epub')
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, 'w') as zout:
        opf_path = find_opf(zin)
        names = zin.namelist()
        # mimetype must be first and stored uncompressed.
        zout.writestr('mimetype', zin.read('mimetype'), compress_type=zipfile.ZIP_STORED)
        for name in names:
            if name == 'mimetype':
                continue
            data = zin.read(name)
            if name == opf_path:
                data = fix_opf(data.decode('utf-8')).encode('utf-8')
            elif name == APPLE_OPTIONS:
                data = fix_apple(data.decode('utf-8')).encode('utf-8')
            zout.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)
        if APPLE_OPTIONS not in names:
            zout.writestr(APPLE_OPTIONS, APPLE_XML, compress_type=zipfile.ZIP_DEFLATED)
    print(f'Written: {dst}')


if __name__ == '__main__':
    main(*sys.argv[1:3])
