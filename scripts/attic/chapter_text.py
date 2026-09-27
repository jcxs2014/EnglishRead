#!/usr/bin/env python3
"""Extract one chapter of 100 Great Short Stories epub to text/chNN.txt (gitignored).

Usage:
  python3 scripts/chapter_text.py <NN>
Prints the flattened text to stdout AND writes notes/.../text/chNN.txt
so downstream grep/verify can read it.

Dropcap fix: the epub uses <span class="smallcaps"> or similar for the
first-letter dropcap; we strip all tags so no spurious spaces are inserted.
"""
import re, sys, zipfile, html, os

EPUB = 'notes/books/short-story-anthologies/100 Great Short Stories by James Daley/library/100 Great Short Stories - James Daley.epub'
OUTDIR = 'notes/books/short-story-anthologies/100 Great Short Stories by James Daley/text'

def clean(b: bytes) -> str:
    t = b.decode('utf-8', errors='ignore')
    t = re.sub(r'<style[^>]*>.*?</style>', '', t, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t).replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', t).strip()

def main(nn: int):
    name = f'OEBPS/ch{nn}.html'
    with zipfile.ZipFile(EPUB) as z:
        if name not in z.namelist():
            # try ch0 padded
            name = f'OEBPS/ch{nn:03d}.html'
            if name not in z.namelist():
                raise SystemExit(f'no {name} in epub')
        text = clean(z.read(name))
    os.makedirs(OUTDIR, exist_ok=True)
    outp = os.path.join(OUTDIR, f'ch{nn:02d}.txt')
    with open(outp, 'w') as f:
        f.write(text)
    print(text)
    print(f'\n\n[written {outp} | {len(text)} chars]', file=sys.stderr)

if __name__ == '__main__':
    nn = int(sys.argv[1])
    main(nn)
