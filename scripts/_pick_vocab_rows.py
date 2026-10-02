#!/usr/bin/env python3
"""Pick rows verbatim from vocab_candidates.py output — never hand-type an example sentence."""
import sys, re, unicodedata

def flat(s):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())

def main():
    cand_file, text_file = sys.argv[1], sys.argv[2]
    words = sys.argv[3:]
    rows = []
    for line in open(cand_file, encoding='utf-8'):
        if not line.startswith('| ') or line.startswith('| 词') or set(line) <= set('| -'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 3:
            continue
        head, gloss, ex = cells[0], cells[1], cells[2]
        if head in ('词/短语',):
            continue
        rows.append((head, gloss, ex))

    src = flat(open(text_file, encoding='utf-8').read())
    picked = []
    for w in words:
        fw = flat(w)
        # match headword: candidate headword is a prefix/equal of the requested word
        hits = [(h, g, e) for (h, g, e) in rows if flat(h) == fw or flat(h) and fw.startswith(flat(h)) and len(flat(h)) >= 4]
        if not hits:
            print(f"### ✗ NOT-IN-CANDIDATES: {w}")
            continue
        # prefer longest headword
        h, g, e = sorted(hits, key=lambda t: -len(flat(t[0])))[0]
        fe = flat(e)
        ok = fe in src
        flag = "OK " if ok else "EX-MISS"
        print(f"| {h} | （释义待填） | {e} |   <<{flag}>>")
        picked.append((h, ok))
    miss = [h for h, ok in picked if not ok]
    if miss:
        print("### example not verbatim in chapter text:", miss)

main()
