#!/usr/bin/env python3
"""章号对账：书里写了几章 vs text/ 提取了几章（按**章题 slug** 配对，不按纯章号）。

用法：python3 scripts/check_chapters.py "<书目录>"

为什么要有这一条（2026-11-20）：
  盘点近期 18 本书时发现 `paradise` 书里 27 章、`text/` 28 章，**少写一章**，
  而 gate EXIT=0、总览三篇齐、T1/T2 自检照跑 ⇒ **少写一章零信号**。

判据：
  ❌ 阻断型：text/ 里有某章（≥500 词）而书里没有对应章 → 少写。
  ⚠️ 提示型：
     - 该章原文 < 500 词 → 按非正文件（致谢/前言/人物表）放过；
     - 书里有章、text/ 没有 → 旧书未留语料或提取漏件；
     - md 与 text/ 章号整体偏移（text 按 epub 顺序含扉页编号）→ 按章题配对后判定。

不判红的例外：本书没有任何 `ch*.md`（旧格式命名）→ 退出码 2「无法判定」。

退出码：0 通过 / 1 有阻断 / 2 无法判定
"""
import os, re, sys
from collections import Counter

MIN_WORDS = 500

def slug(prefixless):
    x = prefixless.lower().replace(".md", "").replace(".txt", "")
    return re.sub(r"[^a-z0-9]+", "", x)

def collect(book):
    md, tx = {}, {}
    for p in os.listdir(book):
        m = re.match(r"^ch(\d+)\s+(.*)\.md$", p)
        if m:
            md[slug(m.group(2))] = (int(m.group(1)), p)
    tdir = os.path.join(book, "text")
    if os.path.isdir(tdir):
        for p in os.listdir(tdir):
            m = re.match(r"^ch(\d+)_(.*)\.txt$", p)
            if m:
                tx[slug(m.group(2))] = (int(m.group(1)), p)
    return md, tx, tdir

def words(tdir, fname):
    body = open(os.path.join(tdir, fname), encoding="utf-8", errors="ignore").read()
    return len(re.findall(r"[A-Za-z']+", body))

def main():
    if len(sys.argv) != 2:
        print(__doc__); return 2
    book = sys.argv[1].rstrip("/")
    if not os.path.isdir(book):
        print(f"❌ 目录不存在：{book}"); return 1
    md, tx, tdir = collect(book)
    if not md:
        print("❓ 本书没有 ch*.md（旧格式命名）——无法判定")
        return 2

    # 配对策略：优先「章题 slug」（能同时对齐编号与标题）；slug 命中率低时退回「章号 + 偏移」
    common = [k for k in md if k in tx]
    overlap = len(common) / max(1, min(len(md), len(tx)))
    offset = 0
    if overlap >= 0.5:
        offset = Counter(tx[k][0] - md[k][0] for k in common).most_common(1)[0][0]
        md_nums = {n + offset for n, _ in md.values()}
    else:
        md_nums = {n for n, _ in md.values()}
        best = None
        for k in range(-6, 7):
            shifted = {n + k for n in md_nums}
            hit = len(shifted & {n for n, _ in tx.values()})
            if best is None or hit > best[0] or (hit == best[0] and abs(k) < abs(best[1])):
                best = (hit, k)
        offset = best[1]
        md_nums = {n + offset for n in md_nums}
    if offset:
        print(f"  ⚠️ md 与 text/ 章号整体偏移 {offset:+d}"
              f"（text 按 epub 顺序含扉页/目录编号），对齐后判定")

    tx_nums = {n: (n, f) for n, f in tx.values()}
    md_by_num = {n + offset: (n, f) for n, f in md.values()}
    missing, short, no_text = [], [], []
    for n, (orig, f) in tx_nums.items():
        if n in md_nums:
            continue
        w = words(tdir, f)
        (missing if w >= MIN_WORDS else short).append((n, w, f))
    for n, (orig, f) in md_by_num.items():
        if n not in tx_nums:
            no_text.append((orig, f))

    if missing:
        print("❌ 少写的章：" + "、".join(f"ch{n:02d}（{w} 词）" for n, w, _ in sorted(missing)))
    for n, w, _ in sorted(short):
        print(f"  ⚠️ text/ ch{n:02d} 无对应 md，但原文仅 {w} 词——按非正文件（致谢/前言）放过")
    for n, f in sorted(no_text):
        print(f"  ⚠️ 书里 ch{n:02d} 无对应原文（旧书未留语料或提取漏件，不判红）")

    print(f"=== 章号对账：md {len(md)} 章 ｜ text/ {len(tx)} 章 ｜ 偏移 {offset:+d} ｜ "
          f"少写 {len(missing)} ｜ 短件放过 {len(short)} ｜ 无原文 {len(no_text)} ===")
    if missing:
        print("结论：❌ 有阻断（少写章节）"); return 1
    print("结论：✅ 章号齐全"); return 0

if __name__ == "__main__":
    sys.exit(main())
