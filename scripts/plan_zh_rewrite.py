#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成「中文层重写」派活清单：每批一批 JSON，含每块的现状与原文路径

用途
----
派子代理改写分析层时，代理最贵的是**翻找**——「本章哪些块要改、改的是哪一行、
引语是什么、原文在哪」。本脚本把这些一次性备好，代理只做**判断与写作**。

产出 JSON 结构::

    {
      "batch": "B03",
      "chapters": [
        {
          "file": "ch19 five years.md",
          "chapter": "ch19",
          "text_path": "text/ch19_chapter_19.txt",
          "note": "本批专属判据（由调用方 --note 传入）",
          "blocks": [
            {
              "n": 1,            # 原句编号
              "line": 17,        # md 中该块引语行号
              "quote": "…",      # 引语原文
              "zh": "…",         # 现有中文理解（可能为空 = 缺）
              "why": "…",        # 现有关于这样写
              "tip": "…",        # 现有读者视角提示
              "flags": ["EN_ZH", "EN_WHY", "NO_TIP"]   # 需处理的项
            }
          ],
          "tail_lines": 8,    # 文件级 ## 读者视角提示 小节行数
          "tail_english": true
        }
      ]
    }

用法
----
    python3 scripts/plan_zh_rewrite.py "<书目录>" "ch19,ch20" --batch B03 --note "…" -o /tmp/b03.json
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_chinese_layer as ccl  # noqa: E402

BLOCK_RE = re.compile(r'^> \*\*原句 (\d+):\*\*')
TAIL_HEADING = "## 读者视角提示"


def chapter_text_path(book_dir, ch):
    for p in sorted(glob.glob(os.path.join(book_dir, "text", f"{ch}_chapter_*.txt"))):
        return os.path.relpath(p, book_dir)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_dir")
    ap.add_argument("chapters", help="逗号分隔章号，如 ch19,ch20")
    ap.add_argument("--batch", default="B00")
    ap.add_argument("--note", default="")
    ap.add_argument("-o", "--out", required=True)
    args = ap.parse_args()

    blocks = ccl.scan_chapters(args.book_dir)
    by_file = {}
    for b in blocks:
        by_file.setdefault(b["file"], []).append(b)

    chs = [c.strip() for c in args.chapters.split(",") if c.strip()]
    out = {"batch": args.batch, "note": args.note, "chapters": []}

    for ch in chs:
        fname = next((f for f in by_file if f.startswith(ch + " ")), None)
        if not fname:
            print(f"❓ 找不到 {ch} 的 md")
            continue
        path = os.path.join(args.book_dir, fname)
        lines = open(path, encoding="utf-8").read().split("\n")
        h = next((i for i, l in enumerate(lines) if l.strip() == TAIL_HEADING), None)
        tail = lines[h + 1:] if h is not None else []
        tail_zh = "".join(tail)
        tail_en = (ccl.mix_ratio(tail_zh) if tail_zh.strip() else 0) > 0.5

        chap = {
            "file": fname,
            "chapter": ch,
            "text_path": chapter_text_path(args.book_dir, ch),
            "note": args.note,
            "tail_lines": len(tail),
            "tail_english": tail_en,
            "blocks": [],
        }
        for b in by_file[fname]:
            sec = b["sec"]
            zh = (sec.get("中文理解") or sec.get("理解") or "").strip()
            why = (sec.get("为什么这样写") or "").strip()
            tip = (sec.get("读者视角提示") or "").strip()
            flags = []
            if not zh:
                flags.append("NO_ZH")
            elif not ccl.HAN.search(zh):
                flags.append("EN_ZH")
            elif ccl.mix_ratio(zh) > 0.35:
                flags.append("MIX_ZH")
            if not why:
                flags.append("NO_WHY")
            elif not ccl.HAN.search(why):
                flags.append("EN_WHY")
            elif ccl.mix_ratio(why) > 0.35:
                flags.append("MIX_WHY")
            if not tip:
                flags.append("NO_TIP")
            elif not ccl.HAN.search(tip):
                flags.append("EN_TIP")
            elif ccl.mix_ratio(tip) > 0.35:
                flags.append("MIX_TIP")
            if not flags:
                continue
            chap["blocks"].append({
                "n": int(BLOCK_RE.match(
                    next(l for l in lines if l.startswith(f'> **原句 ') and
                        abs(lines.index(l) - b["line"]) < 3)
                ).group(1)) if False else None,
                "line": b["line"],
                "quote": b["quote"],
                "zh": zh,
                "why": why,
                "tip": tip,
                "flags": flags,
            })
        # 补原句编号
        cur = 0
        for i, l in enumerate(lines):
            m = BLOCK_RE.match(l)
            if not m:
                continue
            cur = int(m.group(1))
            for blk in chap["blocks"]:
                if blk["line"] == i + 1:
                    blk["n"] = cur
        out["chapters"].append(chap)

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    nb = sum(len(c["blocks"]) for c in out["chapters"])
    print(f"=== {args.batch}: {len(out['chapters'])} 章 / {nb} 个待改块 → {args.out}")


if __name__ == "__main__":
    main()
