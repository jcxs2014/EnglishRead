#!/usr/bin/env python3
"""查 md 引语块是否被 verify_quotes 的抽取口径漏掉／截断（块数对账）。

**发现的缺陷类（2026-09-29 实测）**：`verify_quotes.extract_quotes` 对
「以内层引号开头」的 `> **原句 N:** …` 行会做一次**按引号切分**，于是：
  - `“Look,” Harrison sighed, dropping the theatrics.`  → **整块被丢**（块数 10 → 抽到 9）
  - `“Because I can’t pull a happy ending out of thin air just because I want it enough,” Viv said…`
    → **只留到第一个内层闭引号**（后半段「It almost hurt to talk about this」整段不进校验）
后果：verify_quotes 报 9/9 ✅，但**实际有两块没被校验**——「报了 9/9」≠「10 块都对」。

本脚本口径 = **直接复用 verify_quotes 的 extract_quotes**（不自造正则），
比对「md 里的 `> **原句 N:**` 行数」与「工具抽到的条数」，并对每条做首 40 flat 字符
前缀比对，定位「被丢」和「被截断」两种形态。

处置（写作侧根治，不是改工具）：
  被丢  → 把块首的内层开引号去掉，从引号之后的第一个词起（`Harrison sighed, …`），
           该段仍与原文逐字连续；
  被截断 → 让块以「引号前」起（如 `Viv said, “The language is too broad.”`），
           或把引语本身缩到工具看得见的范围内。
  ⚠️ 不要用 `…` 去「凑」——那会造出跨标签拼接。

用法: python3 scripts/check_block_coverage.py "<书目录>" [md ...]
"""
import importlib.util
import re
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("vq", "scripts/verify_quotes.py")
vq = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vq)

book = Path(sys.argv[1])
targets = [Path(x) for x in sys.argv[2:]] or sorted(book.glob("ch*.md"))
flat = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())

bad_total = 0
for md in targets:
    text = md.read_text(encoding="utf-8")
    blocks = re.findall(r"^>\s*\*{0,2}原句\s*\d+[:：]?\*{0,2}\s+(.+)$", text, re.M)
    # ⚠️ 2026-09-29 修正：`extract_quotes` 默认 include_short=False ⇒ <20 flat 字符的
    # 短引语**不在** extracted 里 ⇒ 本脚本把它们判成「被丢（整块未进任何校验）」。
    # 但短引语由 `check_short_quotes.py` 逐条兜底（复用同一 extract_quotes 口径），
    # 投毒已证明该脚本真会报 MISS ⇒ 原行为是**假红**（it says the tool doesn't know
    # about the fallback）。改为带 include_short=True，让本脚本只报真正的孤儿块。
    groups = vq.extract_quotes(text, include_short=True)
    extracted = [q for g in groups if isinstance(g, list) for q in g]
    problems, notes = [], []
    used = set()
    for b in blocks:
        fb = flat(b)
        e = next((x for x in extracted if id(x) not in used and flat(x) == fb), None)
        if e is None:
            e = next((x for x in extracted if id(x) not in used and fb.startswith(flat(x))), None)
            if e is not None:
                used.add(id(e))
                notes.append(("尾部叙述标签未进 verify_quotes（由 sweep_full 整串兜）",
                              f"{b[:56]} …→ 校验到 {e[:44]!r}"))
                continue
            problems.append(("被丢（整块未进任何校验）", b))
        else:
            used.add(id(e))
    if problems or notes:
        print(f"{'❌' if problems else '⚠️'} {md.name}: md 块 {len(blocks)} / 工具抽到 {len(extracted)}")
        for kind, detail in problems + notes:
            print(f"   [{kind}] {detail[:120]}")
        bad_total += 1 if problems else 0
if not bad_total:
    print(f"✅ 块覆盖对账：{len(targets)} 个文件，每块都进了 verify_quotes 校验")
sys.exit(2 if bad_total else 0)
