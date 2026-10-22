#!/usr/bin/env python3
"""总览三篇的**文件名识别**——唯一实现（2026-10-22 立）。

为什么要有这个模块
------------------
2026-10-17 把「按 `00` 前缀收总览」改成「按语义关键词收」，修掉了空格型 /
无编号 / `00概述.md` 那一批（22 本书目录）。但关键词只有中文三个词
（`概述|金句|情感节点`），于是**英文命名的总览整批漏收**：

    a-sea-of-unspoken-things  00_overview.md / 01_quotes.md / 02_emotional_nodes.md
    forest-of-scars           同上
    the-last-thing            00_overview.md / 00_quotes.md / 00_emotional_moments.md
    lost                      00 overview.md / 00 quotes.md / 00 emotional moments.md
    the-girl-from-the-war-room 00 overview.md / 00 golden quotes.md / 00 emotional moments.md
    wolf-hour                 00 overview.md / 00 golden quotes.md / 00 emotional nodes.md
    books-that-saved-my-life  总结.md

实测 7 本（2026-10-22）。这些书在 `gate.sh` 的 ⑭⑮ 两 lane 里打印的是
「（无总览三篇，本项不适用）」——**总览引语与章节标签从未进任何门禁**，
属第四档「跳过型假绿」，而不是「查过没查到」。

口径（三处工具 + gate 必须一致，否则同一段文字在 A 段被核、B 段看不见）
--------------------------------------------------------------------
收：中文语义词（概述 / 金句 / 情感节点 / 总结 / 论证节点）、
    英文语义词（overview / quote(s) / golden quotes / emotional nodes|moments /
    summary / highlights）。
不收：章级文件（`chNN` 开头）——全库章级文件含上述词的 0 个，但显式排除可防将来误收。
"""
from __future__ import annotations

import glob
import os
import re

_ZH = re.compile(r"概述|金句|情感节点|总结|论证节点")
_EN = re.compile(
    r"(?i)overview|quotes?|golden[\s_-]*quotes?|emotional[\s_-]*(?:nodes?|moments?)|summar|highlights?"
)
_CHAP = re.compile(r"(?i)^ch\d")


def is_overview(path_or_name: str) -> bool:
    """判断一个路径/文件名是不是总览件。"""
    base = os.path.basename(path_or_name)
    if _CHAP.match(base):
        return False
    return bool(_ZH.search(base) or _EN.search(base))


def find_overviews(book_dir: str) -> list[str]:
    """返回书目录下的总览件（排序）。"""
    return sorted(p for p in glob.glob(os.path.join(book_dir, "*.md")) if is_overview(p))


def required_count(book_dir: str) -> int | None:
    """按体裁 profile 给出该书应有的总览篇数；判不出体裁返回 None。

    体裁取路径里的分类目录名（`notes/books/<genre>/<slug>`），
    与 `docs/rules/genre-profiles.json` 的 `overview` 字段对应。
    """
    import json

    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    prof_path = os.path.join(root, "docs", "rules", "genre-profiles.json")
    try:
        prof = json.load(open(prof_path, encoding="utf-8"))
    except Exception:
        return None
    parts = os.path.abspath(book_dir).split(os.sep)
    for part in reversed(parts):
        if part in prof and isinstance(prof[part], dict):
            return int(prof[part].get("overview", prof.get("_default", 3)))
    return None


def main(argv: list[str] | None = None) -> int:
    argv = list(sys_argv() if argv is None else argv)
    if not argv:
        print("用法: names.py <书目录>", file=sys.stderr)
        return 2
    book = argv[0]
    for p in find_overviews(book):
        print(p)
    return 0


def sys_argv():
    import sys

    return sys.argv[1:]


if __name__ == "__main__":
    import sys

    sys.exit(main())
