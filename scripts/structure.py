#!/usr/bin/env python3
"""structure.py — 结构层检查的**唯一入口**（2026-10-20 把 4 个脚本收成 1 个命令）。

    python3 scripts/structure.py audit    "<书>" [--quiet]   # 子项齐备/编号/孤儿/重复/配额
    python3 scripts/structure.py keywords "<书>"             # 引语块覆盖度/关键词锚定/拼接红线
    python3 scripts/structure.py anchor   "<书>"             # 关键词锚定（凭空造词/松散）
    python3 scripts/structure.py order    "<书>"             # 章内块序 vs 原文顺序（抽查级）

四者判据互不替代：audit 看"块长得对不对"，keywords 看"块与它的分析配不配"，
anchor 看"关键词能不能在原文里落地"，order 看"块排得是不是原文顺序"。
order **不进 gate**（全库 354 本有倒置，进正门会一次性红一片），只在抽查/验收时手动跑。

退出码沿用各自原语义：0 通过 / 1 有问题 / 2 无法判定。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

MODES = {"audit": "结构扫描", "keywords": "块覆盖度/关键词/拼接", "anchor": "关键词锚定", "order": "章内块序"}
POSITIONAL = {"order"}  # main(book_dir) 而不是读 sys.argv


def _argv_call(mod, argv):
    old = sys.argv
    sys.argv = [f"structure.py {mod.__name__}", *argv]
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
        print(f'用法: structure.py {mode} "<书>"', file=sys.stderr)
        return 2
    mod = __import__(f"structurecheck.{mode}", fromlist=["main"])
    if mode in POSITIONAL:
        try:
            rc = mod.main(rest[0])
            return 0 if rc is None else rc
        except SystemExit as e:
            return e.code if isinstance(e.code, int) else 1
    return _argv_call(mod, rest)


if __name__ == "__main__":
    sys.exit(main())
