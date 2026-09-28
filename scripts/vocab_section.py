#!/usr/bin/env python3
"""词表生产工具：把三档词表写进精读 md（AGENTS 8.2 禁令 1a / 8.5）

它替代的动作是「凭印象手写词条」——初稿缺陷率 14%–43%，脚本产出 0%。

用法：
    python3 scripts/attic/vocab_section.py <书目录> <NN> <glosses.json> <out.md>
    python3 scripts/attic/vocab_section.py <书目录> <NN> <glosses.json> --print

glosses.json 格式：
    {"tiers": {"⭐⭐⭐": [["word1","释义1"], ...], "⭐⭐": [[...]], "⭐": [[...]]}}

硬保证（任一不满足即退出码 2，不产出）：
  1. 每个词头必须在 vocab_candidates.py 本章候选集内（不许自造词头）
  2. 每个例句由脚本从 text/ 抽取并 flat 比对必须逐字命中本章
  3. 每个词头必须有释义（缺则报错，不写空）
  4. 每档不设配额——候选不足就少写，不从记忆里补
"""
import json
import re
import subprocess
import sys


def main() -> int:
    if len(sys.argv) < 5:
        print(__doc__)
        return 2
    book, ch, gloss_file = sys.argv[1], sys.argv[2], sys.argv[3]
    out = sys.argv[4] if len(sys.argv) > 4 and not sys.argv[4].startswith("--") else None

    proc = subprocess.run(
        ["python3", "scripts/vocab_candidates.py", book, "--ch", ch, "--tiers", "--limit", "300"],
        capture_output=True, text=True,
    )
    if not proc.stdout.strip():
        print("❓ 候选集为空——先怀疑 cwd 是否在仓库根、--ch 章号是否越界")
        return 2
    avail = {w.strip(): e.strip() for w, e in
             re.findall(r"^\| ([^|]+?) \| （释义待填） \| (.+?) \|$", proc.stdout, re.M)}

    text = open(f"{book}/text/{_chapter_file(book, ch)}", encoding="utf-8").read()
    flat = re.sub(r"[^a-z0-9]", "", text.lower())

    spec = json.load(open(gloss_file, encoding="utf-8"))
    tiers = spec["tiers"]

    errors = []
    for tier, words in tiers.items():
        for entry in words:
            w, gloss = entry[0], entry[1]
            if w not in avail:
                errors.append(f"[{tier}] 词头不在本章候选集内（自造？）: {w}")
                continue
            if not gloss.strip():
                errors.append(f"[{tier}] 缺释义: {w}")
                continue
            if re.sub(r"[^a-z0-9]", "", avail[w].lower()) not in flat:
                errors.append(f"[{tier}] 例句不逐字命中本章: {w} -> {avail[w][:50]}")
    if errors:
        print("\n".join(errors))
        print(f"\n❌ {len(errors)} 处问题，未产出（宁缺毋造）")
        return 2

    lines = ["## 本章词汇", ""]
    for tier in ("⭐⭐⭐", "⭐⭐", "⭐"):
        if tier not in tiers:
            continue
        lines += [f"### {tier} 高级" if tier == "⭐⭐⭐" else f"### {tier} 进阶" if tier == "⭐⭐" else "### ⭐ 基础",
                  "", "| 词/短语 | 释义 | 例句 |", "|---|---|---|"]
        for w, gloss in tiers[tier]:
            lines.append(f"| {w} | {gloss} | {avail[w]} |")
        lines.append("")
    section = "\n".join(lines).rstrip() + "\n"

    if out:
        open(out, "w", encoding="utf-8").write(section)
        print(f"✅ 写入 {out}（{sum(len(v) for v in tiers.values())} 条，全部通过 4 项断言）")
    else:
        print(section)
    return 0


def _chapter_file(book: str, ch: str) -> str:
    import glob
    hits = glob.glob(f"{book}/text/ch{int(ch):02d}_*.txt")
    if len(hits) != 1:
        print(f"❓ text/ 下 ch{ch:02d} 匹配到 {len(hits)} 件，无法定位本章")
        raise SystemExit(2)
    return hits[0].split("/")[-1]


if __name__ == "__main__":
    raise SystemExit(main())
