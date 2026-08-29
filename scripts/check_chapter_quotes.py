#!/usr/bin/env python3
"""Strict per-chapter quote checker.

Unlike verify_quotes.py (which searches the WHOLE epub and could pass a quote
lifted from a DIFFERENT chapter), this checks each ①-⑩ quote against THAT
chapter's own extracted text/chNN.txt only. This prevents cross-chapter
misattribution.

Usage:
  python3 scripts/check_chapter_quotes.py <NN> "<md_file_path>" [--out-dir <text_dir>]

Exits 0 only if every extracted quote (>=20 alphanum chars) is found in
text/chNN.txt.
"""
import re, sys, os
OUTDIR = 'notes/books/short-story-anthologies/100 Great Short Stories by James Daley/text'
CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩'
QUOTE_RE = re.compile(
    # ① "..." / **①** "..."（MHW / Venus Fly Trap 格式）
    r'^(?:\*{1,2}[' + CIRCLED + r']\*?|[' + CIRCLED + r'])\s*["\'](.*)["\']'
    # > **原句 N:** "..."（The Giver / Golden Boy 等长篇精读格式）
    + r'|^>\s*\*{0,2}原句\s*\d+[:：]?\*{0,2}\s+["\'](.*)["\']'
    # ① **"..."**（100 Great 格式：引语带粗体包裹，靠 strip 剥离）
    + r'|^[' + CIRCLED + r']\s+(.+)'
)
def flat(s): return re.sub(r'[^a-z0-9]', '', s.lower())

def extract(txt):
    qs = []; seen = set()
    for raw in txt.splitlines():
        s = raw.strip()
        m = QUOTE_RE.match(s)
        if not m:
            continue
        body = next(g for g in m.groups() if g is not None)
        b = body.strip().strip('*').strip('\'"\u201c\u201d\u2018\u2019 ').strip()
        if len(flat(b)) >= 20 and b not in seen:
            seen.add(b); qs.append(b)
    return qs

def main(nn, md, outdir=None):
    od = outdir or OUTDIR
    # try both bare chNN.txt and chNN_<slug>.txt (extract_chapters.py output)
    cands = [os.path.join(od, f'ch{nn:02d}.txt'),
             os.path.join(od, f'ch{nn:02d}_')]
    tp = None
    if os.path.exists(cands[0]):
        tp = cands[0]
    else:
        matches = [f for f in os.listdir(od)
                   if re.match(rf'^ch{nn:02d}_.*\.txt$', f)]
        if matches:
            tp = os.path.join(od, matches[0])
    if not tp:
        raise SystemExit(f'missing ch{nn:02d}*.txt in {od}; run scripts/extract_chapters.py first')
    chap = flat(open(tp, encoding='utf-8').read())
    qs = extract(open(md, encoding='utf-8').read())
    if not qs:
        print('NO QUOTES EXTRACTED'); sys.exit(1)
    ok = 0; bad = []
    for i, q in enumerate(qs, 1):
        f = flat(q)[:60]
        if f in chap:
            ok += 1
        else:
            bad.append((i, q[:70]))
    print(f'{os.path.basename(md)}: {ok}/{len(qs)} in ch{nn:02d} text ({od})')
    for i, q in bad:
        print(f'  MISS #{i}: {q}')
    sys.exit(0 if ok == len(qs) else 1)

if __name__ == '__main__':
    args = sys.argv[1:]
    outdir = None
    if '--out-dir' in args:
        i = args.index('--out-dir')
        outdir = args[i + 1]
        del args[i:i + 2]
    main(int(args[0]), args[1], outdir)
