#!/usr/bin/env python3
"""fit_vocab_glosses.py — 把 glosses JSON 与该章候选集求交，可就地裁剪。

为什么需要（2026-10-01 The Death of Us 实测连踩七次）
-----------------------------------------------------
`build_vocab_section.py` 对**候选集外**的词头会报「词头不在本章候选集内（自造？）」并
**整体拒绝产出**。而词头不是我定的——它是 `vocab_candidates.py` 从原文抽出来的结果
（大小写、单复数、是否成短语都随该章的用词走）。凭印象写释义是允许的，**凭印象写
词头必然被拒**。

实测 ch02/ch03/ch04/ch05/ch06/ch07/ch08/ch10 各踩一次：写 30–57 条释义，被拒 1–27 条，
每章多花一轮「改词头 → 重跑 → 再被拒」。

用法:
  python3 scripts/fit_vocab_glosses.py <书目录> <NN> <glosses.json> [--write]
    --write  就地只保留候选内的词头（供 build_vocab_section 直接用）
"""
import json
import subprocess
import sys
from pathlib import Path

book, nn, gj = sys.argv[1], sys.argv[2], Path(sys.argv[3])
write = "--write" in sys.argv

out = subprocess.run(
    ["python3", "scripts/vocab_candidates.py", book, "--ch", nn,
     "--tiers", "--limit", "300", "--max-sent", "400"],
    capture_output=True, text=True, check=True).stdout
cand = set()
for line in out.split("\n"):
    if line.startswith("| ") and "词/短语" not in line and not line.startswith("|---"):
        cand.add(line.strip().strip("|").split("|")[0].strip())

g = json.loads(gj.read_text(encoding="utf-8"))
inside = {k: v for k, v in g.items() if k in cand}
outside = sorted(set(g) - cand)
print(f"候选 {len(cand)} 条｜glosses {len(g)} 条｜候选内 {len(inside)}｜候选外 {len(outside)}")
if outside:
    print("候选外（会被 build_vocab_section 拒绝）:", ", ".join(outside))
if write:
    gj.write_text(json.dumps(inside, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已就地裁剪 {gj} → {len(inside)} 条")
else:
    sys.exit(2 if outside else 0)