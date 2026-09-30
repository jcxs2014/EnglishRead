#!/usr/bin/env python3
"""check_struct_indep.py — 结构扫描的**独立实现**（第 10 条 c 步用）

为什么需要它（2026-09-29 实测）：`audit_structure.py` 的子项检查是**假阴性高发点**
（两块各缺一项仍报 0 —— 它按块内子项集推断，不核「块数与子项数是否一一对应」），
且对「分析块被整段复制」这类损坏报 0。AGENTS 第 10 条 c 步明确：
**不得把它的 0 当作「子项齐全」的证明**。本脚本换实现、换口径，不复用它的判定。

四项（逐文件，逐块）：
  ① 硬性四子项齐全且**各只一次**（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）
  ② 四子项**顺序**固定（中文理解 → 关键词 → 为什么这样写 → 读者视角提示）
  ③ 编号连续（1..N，无跳号/重号）
  ④ 必备 H2 恰一次：## 本章导航 / ## 精读 / ## 本章词汇 / ## 一句话总结；
     词汇三档标题 `### ⭐⭐⭐ 高级` / `### ⭐⭐ 进阶` / `### ⭐ 基础` 齐备
  ⑤ 每章引语块数落在 3–8；全文引语（`> ` 行）只出现在 ## 精读 内

用法: python3 scripts/check_struct_indep.py "<书目录>" [md ...]
退出: 0 全过 ｜ 1 有结构缺陷 ｜ 2 参数错误
"""
import re, sys
from pathlib import Path

SUB = ["中文理解", "关键词", "为什么这样写", "读者视角提示"]
TIER = ["### ⭐⭐⭐ 高级", "### ⭐⭐ 进阶", "### ⭐ 基础"]
H2 = ["## 本章导航", "## 精读", "## 本章词汇", "## 一句话总结"]
QRE = re.compile(r'^> \*\*原句 (\d+):\*\* (.+)$', re.M)


def check(md: Path):
    out = []
    s = md.read_text(encoding="utf-8")
    lines = s.split("\n")
    # --- ④ 必备 H2 / 三档标题 ---
    for h in H2:
        n = s.count("\n" + h + "\n") + (1 if s.startswith(h + "\n") else 0)
        if n != 1:
            out.append(f"必备节「{h}」出现 {n} 次（须恰 1）")
    for t in TIER:
        if t not in s:
            out.append(f"词汇档位标题缺「{t}」")
    # --- ③ 编号连续 ---
    nums = [int(m.group(1)) for m in re.finditer(r'^> \*\*原句 (\d+):\*\*', s, re.M)]
    if nums and nums != list(range(1, len(nums) + 1)):
        out.append(f"引语编号不连续：{nums}")
    # --- ⑤ 块数配额 ---
    if not 3 <= len(nums) <= 8:
        out.append(f"引语块 {len(nums)} 个，超出 3–8 配额")
    # --- ① ② 逐块四子项（硬性、不推断、查重、查序）---
    marks = list(re.finditer(r'^> \*\*原句 (\d+):\*\*', s, re.M))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else s.find("\n## 本章词汇")
        if end < 0:
            end = len(s)
        blk = s[m.end():end]
        pos = []
        for name in SUB:
            # ⚠️ 2026-09-30 修正（The Secret Wife 实测 1680 处假红）：子项行以
            # `- **中文理解**：` 起首（列表项），而原正则 `^\*\*` + re.M 要求
            # `**` 出现在**行首** ⇒ 全书 420 块 × 4 子项全部「出现 0 次」。
            # 本库两种形态并存（A：`**中文理解**：` 行首；B：`- **中文理解**：`
            # 列表项行首），且**冒号可在粗体内或粗体外**。
            # 教训同 audit_structure 的 RE_ANY_LABEL：**正则不加前导容错就是静默空跑**。
            hits = [mm.start() for mm in
                    re.finditer(r'^[ \t]*(?:[-*+]\s+)?\*\*' + name + r'\*\*[：:]',
                               blk, re.M)]
            if len(hits) != 1:
                out.append(f"原句 {m.group(1)}: 子项「{name}」出现 {len(hits)} 次（须恰 1）")
            else:
                pos.append((name, hits[0]))
        if len(pos) == len(SUB):
            order = [p[0] for p in sorted(pos, key=lambda x: x[1])]
            if order != SUB:
                out.append(f"原句 {m.group(1)}: 子项顺序错 {order}")
    # --- ⑤ > 行只出现在 ## 精读 内 ---
    in_read = False
    for i, l in enumerate(lines, 1):
        if l.startswith("## "):
            in_read = (l.strip() == "## 精读")
        if l.startswith("> ") and not in_read:
            out.append(f"第 {i} 行：`> ` 出现在 ## 精读 之外（> 只用于引语）")
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    book = Path(sys.argv[1])
    mds = [Path(x) for x in sys.argv[2:]] or sorted(book.glob("ch*.md"))
    if not mds:
        print(f"❌ {book} 下没有 ch*.md"); return 2
    bad = []
    for md in mds:
        for msg in check(md):
            bad.append(f"{md.name}: {msg}")
    for b in bad:
        print("  ❌ " + b)
    print(f"=== 独立结构扫描：{len(mds)} 个 md，缺陷 {len(bad)} 处 ===")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
