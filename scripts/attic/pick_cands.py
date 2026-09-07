#!/usr/bin/env python3
"""Print evenly-spread candidate sentences from a chapter text file.

Usage: python3 scripts/pick_cands.py <NN> [count]
Reads text/chNN.txt (produced by chapter_text.py) and prints `count`
sentences spread across the chapter, each on its own line, numbered.
Helps choose 10 real quote spans for the ①-⑩ blocks.
"""
import re, sys, os

OUTDIR = 'notes/books/short-story-anthologies/100 Great Short Stories by James Daley/text'

def sents(text):
    # split on sentence boundaries but keep reasonable
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z"\u201c\u2018])', text)
    out = []
    for p in parts:
        p = p.strip()
        if len(re.sub(r'[^a-z0-9]', '', p.lower())) >= 20:
            out.append(p)
    return out

def main(nn, count=16):
    p = os.path.join(OUTDIR, f'ch{nn:02d}.txt')
    text = open(p).read()
    ss = sents(text)
    n = len(ss)
    print(f'# ch{nn:02d}: {n} sentences total, showing {count}')
    idxs = [int(i * (n - 1) / (count - 1)) for i in range(count)]
    for i, si in enumerate(idxs, 1):
        print(f'\n[{i}] (sent#{si}) {ss[si][:400]}')

if __name__ == '__main__':
    nn = int(sys.argv[1])
    c = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    main(nn, c)
