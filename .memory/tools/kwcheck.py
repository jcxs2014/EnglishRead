#!/usr/bin/env python3
"""检查每条引语块的「关键词」是否都出现在该块的引语里（gate ⑱ 的阻断项）。

⚠️ 口径必须与官方一致（2026-10-20 实测教训）：
   本脚本最初用朴素子串判定，比官方 `scripts/check_block_keywords.py` 严得多，
   一次跑出 14 条「问题」，官方只判 2 条阻断 + 12 条提示型；
   后来自己补「语境延伸词豁免」仍与官方不一致（11 条 vs 官方 0 条阻断），
   **根因是关键词匹配口径本身**（官方的 `_kw_in_quote` 允许 flat 匹配、
   括号剥离、按序分词、含 `…` 的句型框架；豁免还要看「为什么这样写」/「读者视角提示」两处）。
   ⇒ **不再自己实现一套**：直接 import 官方模块复用 `_kw_in_quote` / `_echoed`，
      口径漂移在结构上不可能发生。

用法: python3 kwcheck.py <书目录>
退出: 0 无阻断型 ｜ 1 有阻断型
"""
import sys, os, glob, importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # .memory/tools → 仓库根
SPEC = importlib.util.spec_from_file_location(
    "cbk", os.path.join(REPO, "scripts", "check_block_keywords.py"))
cbk = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cbk)

book = sys.argv[1] if len(sys.argv) > 1 else "."
blocking = 0
hinting = 0
for md_path in sorted(glob.glob(os.path.join(book, "ch*.md"))):
    from pathlib import Path
    for line in cbk.check(Path(md_path), Path(book)):
        if "⚠️ 提示" in line:
            print("⚠️  " + line)
            hinting += 1
        else:
            print("❌ " + line)
            blocking += 1
print(f"=== 阻断型 {blocking} 条 ／ 提示型 {hinting} 条 ===")
sys.exit(1 if blocking else 0)
