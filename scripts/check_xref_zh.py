#!/usr/bin/env python3
"""跨章引用核对（AGENTS 规则 7b/7c 的机械化回查动作）。

**为什么要有这个脚本**：`check_crossref.py` 只认 `chNN "引语"` 这一个英文模式，
中文写法（「上一章」「第 15 章」「序章」）完全不在它的口径内 ⇒ 它报「0 对 0 报警」
是**真空绿**。Pictures of You 批次实测 60 处章号错引全部落在这个盲区。

本脚本做两件事，都以 `text/` 为真值：
  ① 把 md 里每个 `chNN` + 紧随其后的反引号短语抽出来，逐条回 `text/chNN` 核该短语是否真在该章
  ② 把中文相对引用（上一章/下一章/前一章/后一章/序章/尾声/结尾/开头）所在行的
     引语块号抽出来，人工判（机械判不了「相对表述折算到第几章」）

用法: python3 scripts/check_xref_zh.py "<书目录>" [--full]
"""
import glob
import os
import re
import sys

# 收口：提取件定位统一走 chapter_text_path 唯一实现（分隔符 _ . 空格 + 章号 1/2/3/4 位）。
# ⚠️ 2026-10-02：此文件是**收口时漏掉的第 9 处**——它从没被跑过，所以从不报错，
#    也就没进「同一缺陷共 8 处」的统计。Beach Read 终验补跑时立刻 IndexError 崩掉。
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chapter_text_path import find_chapter_text

book = sys.argv[1]
full = "--full" in sys.argv
REL = re.compile(r"上一章|下一章|前一章|后一章|上章|下章|序章|开篇|尾声|结尾|本章前|几章前|"
                 r"数章前|前面几章|后面几章|早前|很久以前|前几页")
# 明确带章号的引用。**章号后面可能是中文**（「ch03 冬日市集」）也可能是英文引语，
#   原实现只认英文 ⇒ 把本库最常见的写法整个漏掉（2026-09-29 实测：明明有 3 处
#   chNN 引用却报「命中 0 / 错 0」——正是 8.4「报 0 时先怀疑工具」那一类）。
NUMREF = re.compile(r"ch(\d{2})\s*[，,、]?\s*(?:[「\"'`（(]?\s*)?"
                    r"([A-Za-z][A-Za-z ,.’'\-]{6,60}|[一-鿿]{2,20})")
# POV 断言：「ch21，Viv 视角」「（ch22，Althea 视角）」
POVREF = re.compile(r"ch(\d{2})[，,]\s*([A-Za-z]+)\s*视角")
CHREF = re.compile(r"第\s*(\d+)\s*章")

miss, ok, pov_bad, rel_hits = 0, 0, 0, []
for f in sorted(glob.glob(f"{book}/ch*.md"),
                key=lambda x: int(re.search(r"ch(\d\d)", x).group(1))):
    n = int(re.search(r"ch(\d\d)", f).group(1))
    txt = open(f, encoding="utf-8").read()
    # 本章 text/ 也 flat 化，用于区分「他章才有」与「全书都没有」
    _own_t = find_chapter_text(book, n)
    if not _own_t:
        print(f"❌ {os.path.basename(f)}  找不到本章 text/ 提取件（ch{n}）")
        continue
    own = re.sub(r"[^a-z0-9]", "", open(_own_t, encoding="utf-8").read().lower())
    for i, line in enumerate(txt.split("\n"), 1):
        # ① POV 断言核对：说「chNN，XXX 视角」就得那章真是这个 POV
        for m in POVREF.finditer(line):
            tgt, who = int(m.group(1)), m.group(2)
            if tgt == n or not (1 <= tgt <= 99):
                continue
            tp = find_chapter_text(book, tgt)
            if not tp:
                continue
            src = open(tp, encoding="utf-8").read()
            counts = {w: len(re.findall(rf"\b{w}\b", src)) for w in ("Althea", "Hannah", "Viv")}
            real = max(counts, key=counts.get)
            if who.capitalize() != real:
                print(f"❌ {os.path.basename(f)}:{i}  称 ch{tgt:02d} 是「{who} 视角」，"
                      f"实测该章主导 POV = {real}（{counts}）")
                pov_bad += 1
            else:
                ok += 1
        for m in NUMREF.finditer(line):
            tgt, phrase = int(m.group(1)), m.group(2).strip()
            if tgt == n or not (1 <= tgt <= 99):
                continue
            tp = find_chapter_text(book, tgt)
            if not tp:
                print(f"❌ {os.path.basename(f)}:{i}  指向 ch{tgt:02d}（该章 text/ 不存在）")
                miss += 1
                continue
            tflat = re.sub(r"[^a-z0-9]", "", open(tp, encoding="utf-8").read().lower())
            p = re.sub(r"[^a-z0-9]", "", phrase.lower())
            if p in tflat:
                ok += 1
            elif p in own:
                print(f"⚠️  {os.path.basename(f)}:{i}  「{phrase[:44]}」标 ch{tgt:02d}，"
                      f"实际在本章 ch{n:02d} ⇒ 章号错")
                miss += 1
            else:
                print(f"❌ {os.path.basename(f)}:{i}  「{phrase[:44]}」全书查无（ch{tgt:02d} 亦无）")
                miss += 1
        if REL.search(line) and full:
            q = re.search(r"^> \*\*原句 (\d+):\*\*", line.strip())
            rel_hits.append(f"  {os.path.basename(f)}:{i} 块{q.group(1) if q else '—'}  {line.strip()[:70]}")

print(f"=== 跨章引用：章号+短语/POV 命中 {ok} / 错 {miss} / POV 错 {pov_bad} ===")
if rel_hits:
    print(f"⚠️ 中文相对引用 {len(rel_hits)} 处（机械判不了，须人工折算）：")
    print("\n".join(rel_hits))
sys.exit(2 if (miss or pov_bad) else 0)
