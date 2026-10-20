#!/usr/bin/env python3
"""analysis.py — 分析层的**唯一入口**（2026-10-20 把 6 个脚本收成 1 个命令）。

    python3 scripts/analysis.py inline   "<书>"   # 分析层行内英文逐字（七档）
    python3 scripts/analysis.py quotes   "<书>"   # 分析层英文取证（是否真在原文）
    python3 scripts/analysis.py keywords "<书>"   # 关键词/导航层逐字
    python3 scripts/analysis.py nav      "<书>" [--per-chapter]   # 导航/总结层英文核对
    python3 scripts/analysis.py xref     "<书>"   # 分析层跨章指认（chNN 指的是不是那一章）
    python3 scripts/analysis.py misattr  "<书>"   # 跨章误标（导航/总结/词表层的英文属于别的章）

**只合入口，不动判据**：这六个工具的口径互相重叠但**归一化与豁免规则不同**
（`keywords` 故意不调 `flat_alpha` 以抓撇号换词；`inline` 有七档优先级）。
合并它们的判据会重演「93.5% 假红」那类事故，所以这里只做 façade。

退出码沿用各自原语义：0 通过 / 1 有问题 / 2 无法判定。
"""
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.join(HERE, "analysischeck")
sys.path.insert(0, HERE)
sys.path.insert(0, PKG)

MODES = {
    "inline": "分析层行内英文（七档）",
    "quotes": "分析层英文取证",
    "keywords": "关键词/导航层逐字",
    "nav": "导航/总结层英文核对",
    "xref": "分析层跨章指认",
    "misattr": "跨章误标",
}
# nav.py 是模块级脚本（没有 main，靠顶层代码 + sys.exit），用 runpy 按脚本执行最稳，
# 它不 import 任何仓库内模块。其余五个都有 main()。
RUNPY = {"nav": "nav.py"}
FILES = {
    "inline": "sweep_analysis_inline.py",
    "quotes": "analysis_quotes.py",
    "keywords": "keywords_verbatim.py",
    "xref": "xref.py",
    "misattr": "misattr.py",
}


def _argv_call(mod, argv):
    old = sys.argv
    sys.argv = [f"analysis.py {mod.__name__}", *argv]
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
        print(f'用法: analysis.py {mode} "<书>"', file=sys.stderr)
        return 2

    if mode in RUNPY:
        old = sys.argv
        sys.argv = [FILES.get(mode, f"{mode}.py"), *rest] if mode not in RUNPY else [RUNPY[mode], *rest]
        try:
            runpy.run_path(os.path.join(PKG, RUNPY[mode]), run_name="__main__")
            return 0
        except SystemExit as e:
            return e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
        finally:
            sys.argv = old

    mod = __import__(f"analysischeck.{FILES[mode][:-3]}", fromlist=["main"])
    return _argv_call(mod, rest)


if __name__ == "__main__":
    sys.exit(main())
