#!/usr/bin/env python3
"""Extract candidate quote spans for ch09 from text/ with hard constraints:
- 1-3 consecutive sentences within ONE natural paragraph (paragraphs separated by blank lines)
- 30-70 words
- no ellipsis character
- unique match in the whole text after flattening punctuation + lowercasing
- no footnote-number-bearing sentences (digit glued to word/punct)
Outputs JSON candidates with positions so we can pick 15 strictly increasing.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

TXT = Path("/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch09_7_crazy_bitches_of_the_1940s_and_1950s.txt")
OUT = Path("/Users/jcxs2014/Documents/Works/EnglishRead/.memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch09-candidates.json")

text = TXT.read_text(encoding="utf-8")

# strip the leading heading block (line 1 title + blank lines) but keep offsets
paras = []
pos = 0
for m in re.finditer(r"[^\n]+(?:\n(?!\s*\n)[^\n]+)*", text):
    pass

# simpler: split keeping offsets
parts = re.split(r"\n\s*\n", text)
offsets = []
o = 0
for p in parts:
    idx = text.find(p, o)
    if idx < 0:
        idx = o
    offsets.append((idx, idx + len(p)))
    o = idx + len(p)

ABBREV = {"Dr.", "Mr.", "Mrs.", "Ms.", "No.", "St.", "Jr.", "Sr.", "etc.", "vs.", "U.S."}
SENT_END = re.compile(r'(?<=[.!?…])["”\')\]]*\s+(?=[A-Z“"\'(])')


def split_sentences(para: str):
    raw = []
    last = 0
    for m in SENT_END.finditer(para):
        head = para[last:m.end()]
        # abbreviation guard: don't split if the token before the period is a known abbrev
        tok = head.rstrip()[-6:]
        if any(tok.endswith(a) for a in ABBREV):
            continue
        raw.append(para[last:m.end()])
        last = m.end()
    if last < len(para):
        raw.append(para[last:])
    return [s for s in raw if s.strip()]


def sentences_of(para: str):
    return split_sentences(para)


def flat(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[^\w\s]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


flattext = flat(text)
# count occurrences of each candidate in whole text
words_total = len(text.split())

cands = []
for pi, (ps, pe) in enumerate(offsets):
    para = text[ps:pe]
    sents = sentences_of(para)
    if len(sents) < 1:
        continue
    for i in range(len(sents)):
        for j in range(i, min(i + 3, len(sents))):
            span = " ".join(s.strip() for s in sents[i:j + 1]).strip()
            n = len(span.split())
            if n < 30 or n > 70:
                continue
            if "…" in span or "..." in span:
                continue
            # footnote markers: digit glued to a word or to punctuation
            if re.search(r"[A-Za-z)\"”]\d+", span) or re.search(r"\d+\s*[a-z]", span):
                continue
            if re.search(r"\d", span):
                # digits only allowed if standalone like a year? avoid entirely for safety
                continue
            fs = flat(span)
            if len(fs) < 40:
                continue
            cnt = flattext.count(fs)
            if cnt != 1:
                continue
            cands.append({
                "pi": pi,
                "i": i,
                "j": j,
                "pos": ps + para.find(sents[i]),
                "nwords": n,
                "text": span,
            })

cands.sort(key=lambda c: c["pos"])
OUT.write_text(json.dumps(cands, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"total words in text: {words_total}; candidates: {len(cands)}")
for c in cands:
    print(f'--[{c["pos"]:6d} pi{c["pi"]:3d} s{c["i"]}-{c["j"]} {c["nwords"]:3d}w] {c["text"][:110]}')
