#!/usr/bin/env python3
"""overview.py — 总览三篇的**唯一入口**（2026-10-20 把 3 个脚本收成 1 个命令）。

总览三篇（`00_概述` / `00_金句精选` / `00_情感节点`）原先有三个各管一段的脚本：

    verify_overview_quotes.py  —— 总览引语是否逐字（对 epub）
    check_overview_full.py     —— 总览整串核查 + 章节标签对账 + H1 语义
    check_overview_labels.py   —— `（chNN）` 标注层：逐字 + 章号归属

现在统一为：

    python3 scripts/overview.py quotes "<书>" ["<epub>"]   # 逐字（无 epub 则退出码 2）
    python3 scripts/overview.py full   "<书>" ["<epub>"]   # 整串 + 标签对账
    python3 scripts/overview.py labels "<书>" ["<epub>"]   # （chNN）标注层

三者的判据互不替代（quotes 只看独立成行的 `> "`，labels 只收带 `（chNN）` 的行，
full 做整串与标签对账）——合并的是入口，不是判据。

退出码沿用各自原语义：0 通过 / 1 有问题 / 2 无法判定。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

MODES = {"quotes": "总览引语逐字", "full": "总览整串 + 章节标签对账", "labels": "（chNN）标注层"}


def _argv_call(mod, argv):
    old = sys.argv
    sys.argv = [f"overview.py {mod.__name__}", *argv]
    try:
        rc = mod.main()
        return 0 if rc is None else rc
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    finally:
        sys.argv = old


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(sys.argv) > 1 else 2
    mode, rest = sys.argv[1], sys.argv[2:]
    if mode not in MODES:
        print(f"未知模式：{mode}\n{__doc__}", file=sys.stderr)
        return 2
    if not rest:
        print(f'用法: overview.py {mode} "<书>" ["<epub>"]', file=sys.stderr)
        return 2

    if mode == "quotes":
        from overviewcheck.verbatim import main as quotes_main
        try:
            quotes_main(rest[0], rest[1] if len(rest) > 1 else "")
        except SystemExit as e:
            return e.code if isinstance(e.code, int) else 1
        return 0

    mod = __import__(f"overviewcheck.{mode}", fromlist=["main"])
    return _argv_call(mod, rest)


if __name__ == "__main__":
    sys.exit(main())
