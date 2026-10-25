#!/usr/bin/env python3
"""Candidate quote spans for ch11 — allow digits but exclude footnote markers (`.N`)."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch11_9_sexy_vampire_bitches_of_the_1970s_and_.txt"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch11-candidates2.json"

text = TXT.read_text(encoding="utf-8")


def flat(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[^\w\s]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


flattext = flat(text)

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
            if re.search(r"[a-zA-Z]\.\d", span):  # footnote marker
                continue
            if re.search(r"\d", span):
                continue  # keep digits out for now; relaxed pass below
            cnt = flattext.count(flat(span))
            abs_pos = off + chunk.find(sents[i])
            cands.append({"para": pidx, "pos": abs_pos, "nwords": n, "count": cnt, "text": span})

OUT.write_text(json.dumps(cands, ensure_ascii=False, indent=1), encoding="utf-8")
u = [c for c in cands if c["count"] == 1]
u.sort(key=lambda x: x["pos"])
print("total", len(cands), "unique", len(u))
for x in u:
    if 400 <= x["pos"] <= 6000 or 9500 <= x["pos"] <= 11000 or 19000 <= x["pos"] <= 21000 \
       or 23000 <= x["pos"] <= 24500 or 27000 <= x["pos"] <= 29500 or 33000 <= x["pos"] <= 40500 \
       or 43500 <= x["pos"] <= 47000:
        print("---", x["pos"], x["nwords"])
        print(x["text"])
