#!/usr/bin/env python3
"""Pick vocab example sentences for ch12 by slicing the source text.

Rules enforced:
  - the example must be a verbatim contiguous sentence of this chapter's text
  - no footnote digits inside the sentence
  - sentence must start with a capital letter and end with terminal punctuation
  - the sentence must contain the headword (word-boundary match)
  - the headword must exist in this chapter
  - flat(example)[:60] must be inside the flat chapter corpus (check_vocab's example_ok)
  - no Chinese in the cell (the cell holds English only)
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch12_10_monstrous_bitches_bite_back.txt"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch12-vocab.json"

text = TXT.read_text(encoding="utf-8")


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s).lower())


flattext = flat(text)
paras = re.split(r"\n\s*\n", text)


def split_sentences(p: str) -> list[str]:
    out, start, i, n = [], 0, 0, len(p)
    while i < n:
        c = p[i]
        if c in ".!?":
            j = i + 1
            while j < n and p[j] in "\u201d\u2019\"')]":
                j += 1
            if j < n and p[j].isdigit():
                out.append(p[start:i].strip())
                i = j
                while i < n and p[i].isdigit():
                    i += 1
                start = i
                continue
            if j >= n or p[j].isspace():
                out.append(p[start:j].strip())
                i = j
                start = i
                continue
        i += 1
    tail = p[start:].strip()
    if tail:
        out.append(tail)
    return [s for s in out if s]


SENTS: list[str] = []
for pi, para in enumerate(paras):
    if para.strip().startswith("10") and "Monstrous Bitches Bite Back" in para:
        continue                      # chapter title line, not prose
    for s in split_sentences(para.strip()):
        SENTS.append(s)


def usable(s: str) -> bool:
    if len(re.findall(r"[A-Za-z0-9]", s)) < 25:
        return False
    if re.search(r"[.!?]\d", s):
        return False
    if not s[:1].isupper():
        return False
    if not s.endswith((".", "!", "?", ".”", "!”", "?”")):
        return False
    if s.count('"') % 2 or s.count("\u201c") != s.count("\u201d"):
        return False
    if flat(s)[:60] not in flattext:
        return False
    if flat(s) not in flattext:
        return False
    return True


CAND = [s for s in SENTS if usable(s)]


def pick(head: str) -> str | None:
    pat = re.compile(r"\b" + re.escape(head).replace(r"\ ", r"\s+") + r"(s|es|ed|ing)?\b", re.I)
    hits = [s for s in CAND if pat.search(s)]
    if not hits:
        return None
    hits.sort(key=lambda s: (len(s.split()), len(s)))
    return hits[0]


TIERS = {
    "高级": ["mormolyke", "lycanthropy", "succubus", "matrilinear", "autosomal-dominant",
             "Erichtho", "Bacchanalian", "indomitability", "Alecto", "transmissible"],
    "进阶": ["patriarchal", "monstrosity", "sapphic", "forcible", "allegory",
             "dehumanizing", "seductive", "monstrous contagion", "possession ritual",
             "bloodborne"],
    "基础": ["vampire", "cannibal", "monster", "sisters", "girl", "bite", "witch", "blood"],
}

vocab: dict[str, list] = {}
for tier, heads in TIERS.items():
    rows = []
    for h in heads:
        ex = pick(h)
        if ex is None:
            print("MISS:", tier, h)
            continue
        rows.append({"head": h, "example": ex})
    vocab[tier] = rows

OUT.write_text(json.dumps(vocab, ensure_ascii=False, indent=1), encoding="utf-8")
for tier, rows in vocab.items():
    print(f"\n### {tier}  ({len(rows)} rows)")
    for r in rows:
        print(f"| {r['head']} | … | {r['example']} |")
