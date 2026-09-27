#!/usr/bin/env python3
"""逐条核验某章 md 的三档词表：词头须在本章 text/ 逐字出现（带词边界），例句须命中本章。

用法: python3 scripts/vocab_heads_check.py <md> <NN>
"""
import re
import sys
from pathlib import Path

md = Path(sys.argv[1])
ch = sys.argv[2]
text = Path(md).parent / "text" / f"ch{ch}_chapter_{int(ch)}.txt"
corpus = text.read_text(encoding="utf-8")
flat = re.sub(r"[^a-z0-9]", "", corpus.lower())


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


bad_head, bad_ex = [], []
for line in md.read_text(encoding="utf-8").split("\n"):
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 3 or cells[0] in ("词/短语", "---") or set(cells[0]) <= set("-: "):
        continue
    head, ex = cells[0], cells[-1]
    if not ex or ex in ("（释义待填）", "-", "—") or not norm(head):
        continue
    # 词头：带词边界逐字命中
    if not re.search(r"(?<![a-z0-9])" + re.escape(head.lower()) + r"(?![a-z0-9])", corpus.lower()):
        bad_head.append(head)
    # 例句：flat 命中
    if len(norm(ex)) >= 20 and norm(ex) not in flat:
        bad_ex.append((head, ex[:70]))

print(f"[{md.name}] ch{ch} 词头未命中本章: {len(bad_head)}｜例句未命中本章: {len(bad_ex)}")
for h in bad_head:
    print(f"  ❌ 词头本章查无: {h}")
for h, e in bad_ex:
    print(f"  ❌ 例句未命中: {h} → {e}")
sys.exit(1 if (bad_head or bad_ex) else 0)
