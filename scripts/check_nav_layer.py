#!/usr/bin/env python3
"""核对 md 的 `## 本章导航` 与 `## 一句话总结` 两层里的英文片段是否逐字见于 text/。

为什么需要（六道门禁的结构性盲区）:
  `verify_quotes` / `check_chapter_quotes` / `sweep_full` **只解析 `## 精读` 的引语行**，
  `sweep_analysis_inline` 只扫**引语块之外**的正文行——而导航层与总结层既不在引语口径内，
  也不在它的扫描范围里。实测这两层是本库最大的共同盲区
  （Jane Eyre 98 条缺陷约六成在导航/总结/读者视角内）。
  ⇒ 写作侧「只能从 text/ 或已写好的引语块复制」这条规则，事后只能靠本脚本兜。

用法:
  python3 scripts/check_nav_layer.py "<书目录>" [<单个 md> ...]
  python3 scripts/check_nav_layer.py "<书目录>" --per-chapter   # 逐章核（严）

判定:
  ❌ 全书查无 = 阻断型（多半是手打造词）→ 退出码 2
  ⚠️ 本章查无 = 提示型（可能引的是别章，需人工判）→ 只报
  跳过: 单个词（≤4 字母，可能是专名缩写）、非字母开头、纯中文括号内容
"""
import re
import sys
from pathlib import Path

book = Path(sys.argv[1])
per_chapter = "--per-chapter" in sys.argv
targets = [Path(x) for x in sys.argv[2:] if not x.startswith("--")] or sorted(book.glob("ch*.md"))

flat = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())

corpus = {}
for f in sorted((book / "text").glob("ch*.txt")):
    corpus[f.name] = flat(f.read_text(encoding="utf-8"))
all_flat = "".join(corpus.values())
if not all_flat:
    print("❓ text/ 为空或无 ch*.txt")
    sys.exit(2)

fail, warn = [], 0
for md in targets:
    text = md.read_text(encoding="utf-8")
    chunks = []
    if "## 本章导航" in text:
        chunks.append(text.split("## 本章导航", 1)[1].split("\n## ", 1)[0])
    if "## 一句话总结" in text:
        chunks.append(text.split("## 一句话总结", 1)[1])
    for chunk in chunks:
        for m in re.finditer(r"[\"“”'`]([A-Za-z][^\"“”'`]{1,})[\"“”'`]", chunk):
            seg = m.group(1).strip()
            if len(seg) <= 4 or not re.search(r"[A-Za-z]{3}", seg):
                continue
            fs = flat(seg)
            if not fs:
                continue
            if fs in all_flat:
                continue
            own = any(fs in v for k, v in corpus.items() if per_chapter and k.startswith(md.name[:4]))
            if own:
                continue
            if per_chapter:
                fail.append(f"{md.name}: 「{seg}」本章查无（全书亦无）")
            else:
                warn += 1
                fail.append(f"{md.name}: 「{seg}」全书查无 ⇒ 阻断型")

for f in fail:
    print(("❌ " if "全书查无" in f or "本章查无" in f else "⚠️ ") + f)
print(f"\n=== 导航/总结层英文核对：❌ {len([f for f in fail if '查无' in f])} ｜ ⚠️ {warn} ===")
sys.exit(2 if any("全书查无" in f or "本章查无" in f for f in fail) else 0)
