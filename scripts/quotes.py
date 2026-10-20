#!/usr/bin/env python3
"""quotes.py — 引语层的**唯一入口**（2026-10-20 把 6 个脚本收成 1 个命令）。

原先是六个独立脚本，名字相近、参数各不相同，谁在什么时候该跑哪个全靠记：
    verify_quotes.py / sweep_full.py / check_short_quotes.py /
    check_chapter_quotes.py / check_block_coverage.py / check_quote_blocks.py

现在统一为：

    python3 scripts/quotes.py verbatim "<书>" "<epub>" [--full]   # 逐字（对 epub）
    python3 scripts/quotes.py full     "<书>" [--quiet]           # 整串 flat（拼接克星）
    python3 scripts/quotes.py short    "<书>"                     # <20 字符短引语兜底
    python3 scripts/quotes.py chapter  <NN> "<章 md>" [--out-dir <text目录>]   # 逐章归属
    python3 scripts/quotes.py coverage "<书>" [md ...]            # 块是否都进了校验
    python3 scripts/quotes.py blocks   "<书>"                     # 块结构（前缀/编号/孤儿/泄漏）

**为什么 `verbatim` 没有并进包**：`verify_quotes.py` 是 9 个脚本 import 的公共库
（`extract_quotes` / `flat_alpha` / `epub_flat_text`），搬它会连带动 9 个 importer；
本文件只把它挂成子命令，实现留在原处。

退出码沿用各子命令原语义：0 通过 / 1 有阻断 / 2 无法判定。gate.sh 的 lane 编号不变。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

USAGE = __doc__

MODES = {
    "full": "整串 flat 比对（拼接克星）",
    "short": "短引语（<20 字符）兜底",
    "chapter": "逐章归属",
    "coverage": "块覆盖对账",
    "blocks": "引语块结构对账",
}


def _argv_call(mod, argv):
    """按旧脚本的方式调用（它们读 sys.argv），把 SystemExit 折成返回码。"""
    old = sys.argv
    sys.argv = [f"quotes.py {mod.__name__}", *argv]
    try:
        rc = mod.main()
        return 0 if rc is None else rc
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    finally:
        sys.argv = old


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(USAGE)
        return 0 if len(sys.argv) > 1 else 2

    mode, rest = sys.argv[1], sys.argv[2:]

    if mode == "verbatim":
        if len(rest) < 2:
            print('用法: quotes.py verbatim "<书>" "<epub>" [--full]', file=sys.stderr)
            return 2
        from verify_quotes import main as verbatim_main
        try:
            verbatim_main(rest[0], rest[1], "--full" in rest[2:])
        except SystemExit as e:
            return e.code if isinstance(e.code, int) else 1
        return 0

    if mode not in MODES:
        print(f"未知模式：{mode}\n{USAGE}", file=sys.stderr)
        return 2

    mod = __import__(f"quotecheck.{mode}", fromlist=["main"])
    return _argv_call(mod, rest)


if __name__ == "__main__":
    sys.exit(main())
