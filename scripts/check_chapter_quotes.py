#!/usr/bin/env python3
"""Strict per-chapter quote checker for 100 Great Short Stories rework.

Unlike verify_quotes.py (which searches the WHOLE epub and could pass a quote
lifted from a DIFFERENT story), this checks each ①-⑩ quote against THAT
chapter's own extracted text/chNN.txt only. This prevents cross-chapter
misattribution.

Usage:
  python3 scripts/check_chapter_quotes.py <NN> "<md_file_path>"

Exits 0 only if every extracted quote (>=20 alphanum chars) is found in
text/chNN.txt.
"""
import re, sys, os
OUTDIR = 'notes/books/short-story-anthologies/100 Great Short Stories by James Daley/text'
CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩'
def flat(s): return re.sub(r'[^a-z0-9]', '', s.lower())

def extract(txt):
    qs=[]; seen=set()
    for raw in txt.splitlines():
        s=raw.strip()
        m=(re.match(r'^['+CIRCLED+r']\s+(.+)$', s)
           or re.match(r'^\*{1,2}['+CIRCLED+r']\*{1,2}\s+[\"\'](.*)[\"\']', s)
           or re.match(r'^['+CIRCLED+r']\s+[\"\'](.*)[\"\']', s))
        if not m: continue
        b=m.group(1).strip().strip('*').strip('\'"“”‘’ ')
        if len(flat(b))>=20 and b not in seen:
            seen.add(b); qs.append(b)
    return qs

def main(nn, md):
    tp = os.path.join(OUTDIR, f'ch{nn:02d}.txt')
    if not os.path.exists(tp):
        raise SystemExit(f'missing {tp}; run scripts/chapter_text.py {nn} first')
    chap = flat(open(tp).read())
    qs = extract(open(md, encoding='utf-8').read())
    if not qs:
        print('NO QUOTES EXTRACTED'); sys.exit(1)
    ok=0; bad=[]
    for i,q in enumerate(qs,1):
        f=flat(q)[:60]
        if f in chap: ok+=1
        else: bad.append((i,q[:70]))
    print(f'{os.path.basename(md)}: {ok}/{len(qs)} in ch{nn:02d} text')
    for i,q in bad:
        print(f'  MISS #{i}: {q}')
    sys.exit(0 if ok==len(qs) else 1)

if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
