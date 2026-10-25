#!/usr/bin/env python3
"""Extract candidate quote spans for ch13 (paragraph-local, 30-70 words, no digits, unique flat hit)."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch13_11_back_to_babylon.txt"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch13-candidates.json"

text = TXT.read_text(encoding="utf-8")


def flat(s: str) -> str:
    """Same normalization as scripts/chapter_contiguity.flat (ruler used by structurecheck/order.py)."""
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFC", s).lower())


flattext = flat(text)

# Paragraphs: split on blank lines, keep absolute offsets in `text`.
paras = []
pos = 0
for chunk in re.split(r"\n\s*\n", text):
    idx = text.find(chunk, pos)
    if idx < 0:
        idx = pos
    paras.append((idx, chunk))
    pos = idx + len(chunk)

# Sentence split that respects quotes and abbreviations.
SENT = re.compile(r"[^.!?]*[.!?]+[”’\"')\]]*(?:\s+|$)|[^.!?]+$")
ABBR = ("Dr.", "Mr.", "Mrs.", "Ms.", "No.", "St.", "Jr.", "Sr.", "etc.", "vs.", "U.S.")

cands = []
for pidx, (off, chunk) in enumerate(paras):
    if not chunk.strip():
        continue
    sents = [s.strip() for s in SENT.findall(chunk) if s.strip()]
    spos = []
    cursor = 0
    for s in sents:
        i = chunk.find(s, cursor)
        if i < 0:
            i = cursor
        spos.append(i)
        cursor = i + len(s)
    for i in range(len(sents)):
        for j in range(i, min(i + 3, len(sents))):
            span = " ".join(sents[i: j + 1])
            span = re.sub(r"\s+", " ", span).strip()
            n = len(span.split())
            if not (30 <= n <= 70):
                continue
            if "…" in span or "..." in span:
                continue
            if re.search(r"\d", span):
                continue
            if any(sents[k].rstrip().endswith(a) for k in range(i, j + 1) for a in ABBR):
                continue
            cnt = flattext.count(flat(span))
            abs_pos = off + spos[i]
            cands.append({"para": pidx, "pos": abs_pos, "nwords": n, "count": cnt, "text": span})

OUT.write_text(json.dumps(cands, ensure_ascii=False, indent=1), encoding="utf-8")
uniq = [c for c in cands if c["count"] == 1]
print("candidates:", len(cands))
print("unique-hit candidates:", len(uniq))
by_para = {}
for c in uniq:
    by_para.setdefault(c["para"], []).append(c)
for p in sorted(by_para):
    ps = [c["pos"] for c in by_para[p]]
    print(f"  para {p}: {len(by_para[p])} uniq, pos {min(ps)}..{max(ps)}")
