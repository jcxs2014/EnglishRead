#!/usr/bin/env python3
"""Extract candidate quote spans for ch11 (paragraph-local, 30-70 words, no digits)."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch11_9_sexy_vampire_bitches_of_the_1970s_and_.txt"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch11-candidates.json"

text = TXT.read_text(encoding="utf-8")


def flat(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[^\w\s]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


flattext = flat(text)

# Paragraphs: split on blank lines. Keep their absolute offsets in `text`.
paras = []
pos = 0
for chunk in re.split(r"\n\s*\n", text):
    idx = text.find(chunk, pos)
    if idx < 0:
        idx = pos
    paras.append((idx, chunk))
    pos = idx + len(chunk)

cands = []
for pidx, (off, chunk) in enumerate(paras):
    if not chunk.strip():
        continue
    # sentences: split after . ! ? followed by space+capital, keeping terminator
    sents = re.findall(r"[^.!?]*[.!?]+(?:[”’\"']?)(?:\s+|$)|[^.!?]+$", chunk)
    sents = [s.strip() for s in sents if s.strip()]
    for i in range(len(sents)):
        for j in range(i, min(i + 3, len(sents))):
            span = " ".join(sents[i : j + 1])
            span = re.sub(r"\s+", " ", span).strip()
            n = len(span.split())
            if not (30 <= n <= 70):
                continue
            if "…" in span or "..." in span:
                continue
            if re.search(r"\d", span):
                continue
            if "“" in span or "”" in span or '"' in span:
                # quotes inside would complicate md quoting; allow but flag
                pass
            cnt = flattext.count(flat(span))
            abs_pos = off + chunk.find(sents[i])
            cands.append(
                {
                    "para": pidx,
                    "pos": abs_pos,
                    "nwords": n,
                    "count": cnt,
                    "text": span,
                }
            )

OUT.write_text(json.dumps(cands, ensure_ascii=False, indent=1), encoding="utf-8")
print("candidates:", len(cands))
uniq = [c for c in cands if c["count"] == 1]
print("unique-hit candidates:", len(uniq))
print("first 5 positions:", [c["pos"] for c in uniq[:5]])
print("last 5 positions:", [c["pos"] for c in uniq[-5:]])
