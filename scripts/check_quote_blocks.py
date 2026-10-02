#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""引语块结构对账：分析子项组数 == `> **原句 N:**` 行数，且每条原句行都带 `> ` 前缀。

**为什么要有这一项**（Beach Read 第八轮，验证器指出）：
ch21 出现**引语行丢失 `> ` 前缀**（`**原句 10:**` 不带 `>`）＋**原句 9/10 倒序且编号撞车**
＋**写作期自查记录泄漏到成品**；ch18 出现**孤儿分析组**（有四个子项、没有对应引语行）。
**这类损坏对六道引语门禁全部不可见**——它们只解析带 `> ` 的引语行，
丢了前缀的行在它们眼里根本不是引语；而「孤儿分析」是少了一行，多出来的东西没人查。

**五种判据**（逐条报，退出码 2 = 有阻断型）：
  A 缺前缀   `**原句 N:**` 行不以 `> ` 开头
  B 编号倒序 本条 N 小于上一条 N
  C 编号撞车 同一 N 出现两次
  D 孤儿分析 出现分析子项（中文理解/关键词/为什么这样写/读者视角提示）但其上方无引语行
  E 自查泄漏 正文里出现「写作期自查记录」「不作为独立引语块计」等**面向作者而非读者**的字样
用法: python3 scripts/check_quote_blocks.py "<书目录>"
"""
import glob
import os
import re
import sys

SUBS = ("**中文理解：**", "**关键词：**", "**为什么这样写：**", "**读者视角提示：**")
LEAK = ("写作期自查记录", "不作为独立引语块计", "自查记录", "写作期备注")
QUOTE = re.compile(r"^\s*>\s*\*\*原句\s*(\d+)\s*[:：]")
ANY = re.compile(r"^\s*(\*\*原句\s*(\d+)\s*[:：])")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        raise SystemExit('用法: check_quote_blocks.py "<书目录>"')
    book = args[0]
    bad = []
    tot_q = tot_g = 0
    for md in sorted(glob.glob(os.path.join(book, "ch*.md"))):
        name = os.path.basename(md)
        lines = io_lines = open(md, encoding="utf-8", errors="ignore").read().split("\n")
        seen, last, groups, in_group = {}, 0, 0, False
        for i, line in enumerate(lines, 1):
            for w in LEAK:
                if w in line:
                    bad.append(("E 自查泄漏", name, i, line.strip()[:60]))
                    break
            mq = QUOTE.match(line)
            ma = ANY.match(line)
            # ⚠️ A 判据必须放在 `if mq:` **之外**：QUOTE 本身就要求 `>` 前缀，
            #    丢前缀的行 mq 恒为 None ⇒ 整个块被跳过 ⇒ 第一版 0 报警（工具自己漏报）。
            if ma and not mq:
                bad.append(("A 缺前缀", name, i, line.strip()[:60]))
                continue
            if mq:
                tot_q += 1
                n = int(mq.group(1))
                groups += 1
                if n < last:
                    bad.append(("B 编号倒序", name, i,
                                "N=%d < 上一条 %d" % (n, last)))
                if n in seen:
                    bad.append(("C 编号撞车", name, i,
                                "N=%d 已在第 %d 行出现" % (n, seen[n])))
                seen[n] = i
                last = max(last, n)
                in_group = True
                continue
            if not any(line.strip().startswith(s) for s in SUBS):
                continue
            # 只判「一段连续子项的第一行」；排版是「引语行 → 空行 → 四个子项」，
            # 所以向上**跳过空行**后必须紧邻一条引语行，否则这组子项是孤儿。
            if i >= 2 and any(lines[i - 2].strip().startswith(x) for x in SUBS):
                continue                  # 本行不是子项段的第一行
            k = i - 2
            while k >= 0 and not lines[k].strip():
                k -= 1
            if k < 0 or not QUOTE.match(lines[k]):
                bad.append(("D 孤儿分析", name, i,
                            "子项段向上跳过空行后无 `> **原句 N:**` 行"))
        tot_g += groups
    print("=== 引语块结构对账（%s）===" % os.path.basename(book.rstrip("/")))
    print("  带前缀的 `> **原句 N:**` 行：%d 个文件共 %d 行"
          % (len(glob.glob(os.path.join(book, "ch*.md"))), tot_q))
    if not bad:
        print("  ✅ 前缀完整 · 编号连续无撞车 · 无孤儿分析 · 无自查泄漏")
        return 0
    from collections import Counter
    print("  ❌ %d 处：" % len(bad))
    for k, v in sorted(Counter(x[0] for x in bad).items()):
        print("     %s %d 处" % (k, v))
    print()
    for kind, name, ln, detail in bad:
        print("  %s | %s:%d | %s" % (kind, name[:30], ln, detail))
    return 2


if __name__ == "__main__":
    sys.exit(main())
