#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""总览三篇注入器（fail-closed）。

用途：把 `.overview_templates/*.tpl` 里的 `{Q:章号:块号}` 锚点替换成**章节 md 里逐字取出的英文引语**，
模板零手打英文。本脚本是 `scripts/gen_overview.py` 的等价替代（该工具在本书上于 ch23#1 误判「不在 text/」，
详见 docs/实测档案/AB_2026-10-25_gen_overview池构建中断.md）。

与 gen_overview 的差别：本作���在注入**之前**对每条引语做三重核验，任何一条不过即中止、不写盘：
  ① 锚点指向的章 md 里确实有该「原句 K」块，且块只占一行；
  ② 该块的每个「 … 」分段都在本章 `text/chNN_*.txt` 里逐字命中（空白归一后）；
  ③ 各分段在原文中的出现位置严格递增（拼接红线：不得逆序）。

用法：
  python3 .memory/tools/overview_inject.py "<书目录>" [--dry-run]
"""
import argparse
import glob
import os
import re
import sys

ANCHOR = re.compile(r"\{Q:(\d+):(\d+)\}")
BLOCK_LINE = re.compile(r'^> \*\*原句 (\d+):\*\*\s*"(.*)"\s*$')
TPL_TO_OUT = {
    "ov_00_概述.md.tpl": "00_概述.md",
    "ov_00_金句精选.md.tpl": "00_金句精选.md",
    "ov_00_情感节点.md.tpl": "00_情感节点.md",
}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def load_chapter_quotes(book: str) -> dict:
    """{章号: {原句号: 引语原文}}"""
    out = {}
    for path in sorted(glob.glob(os.path.join(book, "ch*.md"))):
        m = re.match(r"ch(\d+)", os.path.basename(path))
        if not m:
            continue
        nn = int(m.group(1))
        blocks = {}
        for line in open(path, encoding="utf-8"):
            b = BLOCK_LINE.match(line.rstrip("\n"))
            if b:
                blocks[int(b.group(1))] = b.group(2)
        out[nn] = blocks
    return out


def load_text(book: str) -> dict:
    out = {}
    for path in sorted(glob.glob(os.path.join(book, "text", "ch*.txt"))):
        m = re.match(r"ch(\d+)", os.path.basename(path))
        if not m:
            continue
        out[int(m.group(1))] = norm(open(path, encoding="utf-8").read())
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    book = args.book
    tpl_dir = os.path.join(book, ".overview_templates")
    if not os.path.isdir(tpl_dir):
        print(f"❌ 找不到模板目录：{tpl_dir}")
        return 2

    chapters = load_chapter_quotes(book)
    texts = load_text(book)
    if len(chapters) != 35 or len(texts) != 35:
        print(f"❌ 章数不符：md {len(chapters)} 章 / text {len(texts)} 件（须 35 / 35）")
        return 2

    pool = {}          # (章, 块) -> 引语原文
    covered = set()   # 被锚点覆盖的章号
    total = 0
    problems = []

    for tpl_name in sorted(TPL_TO_OUT):
        tpl_path = os.path.join(tpl_dir, tpl_name)
        if not os.path.exists(tpl_path):
            problems.append(f"缺模板 {tpl_name}")
            continue
        text = open(tpl_path, encoding="utf-8").read()
        for nn, kk in ANCHOR.findall(text):
            nn, kk = int(nn), int(kk)
            total += 1
            covered.add(nn)
            blocks = chapters.get(nn)
            if blocks is None:
                problems.append(f"{tpl_name}: ch{nn:02d} 无章 md")
                continue
            if kk not in blocks:
                problems.append(f"{tpl_name}: ch{nn:02d} 无「原句 {kk}」块")
                continue
            quote = blocks[kk]
            if nn not in texts:
                problems.append(f"{tpl_name}: ch{nn:02d} 无语料件")
                continue
            body = texts[nn]
            pos = -1
            for seg in quote.split(" … "):
                seg = norm(seg)
                if not seg:
                    problems.append(f"{tpl_name}: ch{nn:02d}#{kk} 存在空分段")
                    break
                at = body.find(seg)
                if at < 0:
                    problems.append(f"{tpl_name}: ch{nn:02d}#{kk} 分段不在 text/：{seg[:60]!r}")
                    break
                if at <= pos:
                    problems.append(f"{tpl_name}: ch{nn:02d}#{kk} 拼接逆序：{seg[:60]!r}")
                    break
                pos = at
            pool[(nn, kk)] = quote

    if problems:
        print("❌ 池构建中止，未写盘：")
        for p in problems:
            print("   -", p)
        return 1

    missing = sorted(set(range(1, 36)) - covered)
    print(f"✅ 池构建通过：锚点 {total} 个，覆盖章 {len(covered)}/35")
    if missing:
        print(f"⚠️ 未被任何锚点覆盖的章：{missing}")
    else:
        print("✅ 35 章全部被锚点覆盖")

    if args.dry_run:
        return 0

    for tpl_name, out_name in sorted(TPL_TO_OUT.items()):
        tpl_path = os.path.join(tpl_dir, tpl_name)
        if not os.path.exists(tpl_path):
            continue
        text = open(tpl_path, encoding="utf-8").read()

        def repl(m):
            nn, kk = int(m.group(1)), int(m.group(2))
            return '"' + pool[(nn, kk)] + '"'

        out_text = ANCHOR.sub(repl, text)
        if ANCHOR.search(out_text):
            print(f"❌ {out_name} 仍有未替换锚点")
            return 1
        out_path = os.path.join(book, out_name)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(out_text)
        n_q = out_text.count('"')
        print(f"✅ 写入 {out_path}（引语行 {out_text.count('（ch')} 处）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
