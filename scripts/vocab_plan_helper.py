#!/usr/bin/env python3
"""导出「已有可用词头+释义」与「候选池」并排清单，供人工挑词填 plan。

用法: python3 scripts/vocab_plan_helper.py <书目录> <ch1> [ch2 ...]
输出: 每章一节，含
  - 已有行（词头在本章命中）按档位列出：词头 | 现释义 | 现有例句是否命中本章
  - 候选池（vocab_candidates 产出，例句天然逐字）按档位列出
"""
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_vocab import word_hits_corpus, FUNC_STOP
from build_vocab_table import load_chapter
from chapter_text_path import find_chapter_text

TIER_PAT = re.compile(r'^###\s*(⭐{1,3})')
book = sys.argv[1]
chs = sys.argv[2:]

files = {}
for f in os.listdir(book):
    m = re.match(r'ch(\d+)', f)
    if m and f.endswith('.md'):
        files.setdefault(int(m.group(1)), os.path.join(book, f))

for ch in chs:
    cn = int(ch)
    p = files.get(cn)
    if not p:
        print(f"### ch{cn}: 找不到 md"); continue
    src = load_chapter(book, ch)
    corpus = unicodedata.normalize('NFKD', src).lower()
    text = open(p, encoding='utf-8').read()
    i = text.index('## 词汇')
    m = re.search(r'^## ', text[i+3:], re.M)
    j = (i+3+m.start()) if m else len(text)
    section = text[i:j]
    print(f"\n{'='*70}\n### ch{cn}  {os.path.basename(p)}")
    print("\n-- 已有行（✓=词头在本章 / ✗=编造）--")
    cur = None
    for line in section.split('\n'):
        s = line.strip()
        tm = TIER_PAT.match(s)
        if tm:
            cur = tm.group(1); print(f"\n[{cur}]"); continue
        if not s.startswith('|') or '|---' in s or s.startswith('| 词'):
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        if len(cells) < 3 or not re.search(r'[A-Za-z]{2,}', cells[0]):
            continue
        head, gloss, ex = cells[0], cells[1], cells[2]
        ws = [w.lower() for w in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", head)
              if w.lower() not in FUNC_STOP]
        ok = all(word_hits_corpus(w, corpus) for w in ws) if ws else True
        mark = "✓" if ok else "✗"
        print(f"  {mark} {head} | {gloss} | 例句:{ex[:60]}")
    # 候选池
    try:
        out = subprocess.run(["python3", "scripts/vocab_candidates.py", book, "--ch", ch,
                              "--tiers", "--limit", "300", "--max-sent", "400"],
                             capture_output=True, text=True, check=True).stdout
    except Exception as e:
        print("候选抽取失败:", e); continue
    print("\n-- 候选池 --")
    cur = None
    for line in out.split("\n"):
        if line.startswith("###"):
            cur = "⭐⭐⭐" if "⭐⭐⭐" in line else ("⭐⭐" if "进阶" in line else "⭐")
            print(f"\n[{cur}] 候选")
        elif line.startswith("| "):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) >= 3 and c[0] not in ("词/短语", "词条") and not set(c[0]) <= set("-: "):
                print(f"    {c[0]} :: {c[2][:70]}")
