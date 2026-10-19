# -*- coding: utf-8 -*-
"""⑱ check_block_keywords 修复：块内「关键词」必须能在该块引语里找到（AGENTS 第 9 条 b）。

逐条按「文件 + 原句号 + 旧关键词行 → 新关键词行」精确替换，不动引语行。
"""

# (文件名, 原句号, 新关键词行内容)
KW = [
    ("ch02 passengers.md", 4, "I killed / I think I killed him"),
    ("ch02 passengers.md", 6, "going forever / He chased us out / He was there"),
    ("ch03 memeto sangro.md", 7, "raft of misery / a raft of human animals"),
    ("ch04 blind monkey.md", 4, "learning from each other / The monkeys"),
    ("ch04 blind monkey.md", 5, "all through the feed / You must have seen them too"),
    ("ch04 blind monkey.md", 6, "screamed / Carol"),
    ("ch10 life goes on.md", 4, "very patient / they do that / the walker slouches away"),
    ("ch10 life goes on.md", 5, "Like falling asleep / then you wake up"),
    ("ch11 wait.md", 1, "bloodline / unburdened with blessings"),
    ("ch11 wait.md", 4, "lack of choice / What frightened Antigone"),
    ("ch13 sinking all the while.md", 1, "didn't kill him / He fell / accustomed to blame"),
    ("ch15 seven bells.md", 2, "necromancer's bells / The warning bell in the village tower tolled / lend extra emphasis"),
    ("ch23 the leaving season.md", 2, "crown of horns / crown of thorns"),
]

import os
import re
import sys
import tempfile

BOOK = sys.argv[1]
byfile = {}
for f, n, kw in KW:
    byfile.setdefault(f, []).append((n, kw))

for fname, items in byfile.items():
    path = os.path.join(BOOK, fname)
    lines = open(path, encoding="utf-8").read().split("\n")
    idxs = [i for i, l in enumerate(lines) if re.match(r"^> \*\*原句 \d+:\*\*", l)]
    changed = 0
    for k, i in enumerate(idxs):
        end = idxs[k + 1] if k + 1 < len(idxs) else len(lines)
        num = int(re.match(r"^> \*\*原句 (\d+):", lines[i]).group(1))
        for n, kw in items:
            if n != num:
                continue
            for j in range(i + 1, end):
                if lines[j].startswith("- **关键词**"):
                    new = "- **关键词**：" + kw
                    if lines[j] != new:
                        lines[j] = new
                        changed += 1
    if changed:
        out = "\n".join(lines)
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(out)
        os.replace(tmp, path)
        print(f"✓ {fname}: 改了 {changed} 条关键词")
    else:
        print(f"· {fname}: 无变化")
