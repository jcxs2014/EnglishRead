#!/usr/bin/env python3
"""T1 抽样计划生成器（2026-10-25）。

用法：
    python3 scripts/t1_plan.py "<书目录>"          # 打印该书的抽样章清单 + 停手判据
    python3 scripts/t1_plan.py "<书目录>" --json   # 机器可读

为什么要有它：「先定抽样章、再读」是 T1 最容易作弊的一步（读完再挑章）。
把抽样变成一条确定性命令，章号就不再是回忆出来的。

规则来源：docs/rules/审查表.md §0.3（2026-10-25 改，取代固定 1/8）
    ≤16 章  → 1/3，至少 3 章
    17–40 章 → 1/4
    >40 章  → 1/5，且至少 10 章
    首章与末章必含，其余等距取。
"""
import glob
import json
import math
import os
import re
import sys


def chapters(book):
    """按章号排序返回 [(n, path)]；只收 `chNN` 命名的 md，排除总览与 xx_ 前缀件。"""
    out = []
    for p in glob.glob(os.path.join(book, "ch*.md")):
        m = re.match(r"ch(\d+)", os.path.basename(p))
        if m:
            out.append((int(m.group(1)), p))
    return sorted(out)


def plan(n):
    """返回 (抽几章, 依据说明)。"""
    if n <= 16:
        k, why = max(3, math.ceil(n / 3)), "≤16 章 → 1/3（至少 3 章）"
    elif n <= 40:
        k, why = max(4, math.ceil(n / 4)), "17–40 章 → 1/4"
    else:
        k, why = max(10, math.ceil(n / 5)), ">40 章 → 1/5（至少 10 章）"
    return min(k, n), why


def pick(nums, k):
    """首末必含 + 等距取。"""
    if k >= len(nums):
        return nums
    if k == 1:
        return [nums[0]]
    idx = [round(i * (len(nums) - 1) / (k - 1)) for i in range(k)]
    seen, out = set(), []
    for i in idx:
        if i not in seen:
            seen.add(i)
            out.append(nums[i])
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    book = sys.argv[1].rstrip("/")
    if not os.path.isdir(book):
        print(f"❌ 不是目录：{book}")
        return 2
    chs = chapters(book)
    if not chs:
        print(f"❌ {book} 下没有 `chNN*.md`（旧格式书？见 docs/实测档案/AD_…旧格式清单）")
        return 2
    nums = [n for n, _ in chs]
    k, why = plan(len(nums))
    picked = pick(nums, k)
    res = {
        "book": book,
        "chapters": len(nums),
        "ratio_rule": why,
        "sample_count": len(picked),
        "sample": [f"ch{n:02d}" for n in picked],
        "density_rule": "密度 = 已读章阻断总数 ÷ 已读章数；<0.2 停 / 0.2–0.5 按规定比例 / ≥0.5 加抽一倍",
    }
    if "--json" in sys.argv:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"书：{res['book']}")
        print(f"章数：{res['chapters']}　抽样规则：{res['ratio_rule']}")
        print(f"抽样章（{res['sample_count']} 章）：{' '.join(res['sample'])}")
        print(f"停手判据：{res['density_rule']}")
        print("\n把上面这行章号**先写进 `t1-verdict.md` 第一行**，再开始读。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
