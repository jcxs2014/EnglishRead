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

# 行首「粗体标签 + 冒号」——**同时吃两种冒号位置**（`**中文理解：**` 与 `**中文理解**：`）。
# 2026-10-02 取代原先写死的 SUBS 四元组（全库 383 种标签，见 main() 内注释）。
SUB_LABEL = re.compile(r"^\*\*([^*\n]{1,14}?)(?:\*\*)?[：:]")
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
        # ⚠️ 2026-10-02 第二次修正：子项标签**不能写死**。原 `SUBS` 硬编码
        #   beach-read 的四个标签且只认「冒号在加粗内」这一种形态，于是：
        #     · the-wrong-sister（五子项：中文理解/句子结构/关键词/表达方式/为什么这样写）
        #       → 它的 句子结构/表达方式 不在名单里，上扫落在兄弟子项上 ⇒ 假红；
        #     · carmen-and-grace（`**中文理解**：` 冒号在加粗**外**）→ 同样落空。
        #   全库实测 12140 个章节文件里有 **383 种**行首粗体标签，其中还混着
        #   导航层（`一句话概括`/`叙事手法`…）与非虚构层（`核心论点`/`论证脉络`…），
        #   所以也不能「见粗体就算子项」——那会把它们全判成孤儿。
        #   ⇒ **按文件自校准**（与 `audit_structure` 的「按书内多数派子项集自校准」同法）：
        #     本文件的子项标签集 = **实际出现在某条引语行下方**的那些标签。
        #   这样标签名与冒号位置都从文件自身取，与任何一本书的格式解耦；
        #   没有引语行的文件直接跳过 D 判据（无从自校准就不判）。
        # 含引语行的小节集合——D 判据**只在小节范围内**生效（见下面 ms 处的注释）
        quote_sections, sec = set(), None
        for ql in lines:
            if ql.startswith("## "):
                sec = ql.strip()
            elif QUOTE.match(ql) and sec:
                quote_sections.add(sec)
        subs_here = set()
        for qi, ql in enumerate(lines):
            if not QUOTE.match(ql):
                continue
            for k in range(qi + 1, len(lines)):
                # ⚠️ 必须同时被「下一条引语行」和「下一个 `## ` 小节」截断：
                #   只按引语行截断时，**末条**引语行的组会一路扫到文件尾，
                #   把 `## 本章词汇` / `## 一句话总结` 里的粗体标签
                #   （`**这一章的技艺在于：**` 等）也吸进子项集 ⇒ 那些行被判成孤儿。
                if QUOTE.match(lines[k]) or lines[k].startswith("## "):
                    break
                m = SUB_LABEL.match(lines[k].strip())
                if m:
                    subs_here.add(m.group(1).strip())
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
            ms = SUB_LABEL.match(line.strip())
            if not ms or ms.group(1).strip() not in subs_here:
                continue
            # ⚠️ 只在「本文件里含有引语行的小节」内判孤儿。否则专项节/词汇节/总结节里
            #   **同名**的字段行会被误判（实测：the-passing-of-the-dragon 的
            #   `## 长难句专项` 里有 `**句子结构**：`、a-history-of-burning 的词汇表后
            #   跟着 `**读者视角提示**：`——都不是引语块的子项）。
            _sec = next((l.strip() for l in reversed(lines[:i - 1])
                         if l.startswith("## ")), None)
            # 文件开头（无前置小节）不属任何小节 ⇒ 不能被范围约束一并放过，
            # 否则「整组子项浮在文件最前面」这种最硬的孤儿会漏报（负控实测）。
            if _sec is not None and _sec not in quote_sections:
                continue
            # 只判「一段子项的第一行」（上一条非空行不是子项），保证每组只报一次。
            k = i - 2
            while k >= 0 and not lines[k].strip():
                k -= 1
            if k >= 0 and SUB_LABEL.match(lines[k].strip()):
                continue
            # ⚠️ 2026-10-02 第三次修正（89 本书同时报 D 才暴露出来）：「组首行上方必须
            #   **紧邻**一条引语行」是**过严**的——本库相当一部分书的 **中文理解是无标签的
            #   裸段落**（如 save-whats-left ch01：引语行 → 「别买海滨房。连想都别想要。…」
            #   → 关键词），组其实**有主**，只是第一个子项没标签。首版判据把这 89 本
            #   全判成孤儿。
            #   ⇒ 改为：**向上越过空行、无标签段落与其它子项行**，直到
            #       ① 命中引语行 ⇒ 有主，放行；② 撞到 `## ` 小节或文件开头 ⇒ 真的没主。
            #   这个「撞到小节就停」是必要的边界：否则紧跟在 `## 精读` 之后的
            #   注入孤儿会被一路扫回上一个章节的文件尾而**漏报**。
            k = i - 2
            while k >= 0:
                u = lines[k].strip()
                if u.startswith("## "):
                    break                     # 出了本节 ⇒ 本组没有引语行管着
                if QUOTE.match(lines[k]):
                    break                     # 命中引语行 ⇒ 有主
                k -= 1
            if k < 0 or not QUOTE.match(lines[k]):
                bad.append(("D 孤儿分析", name, i,
                            "本组子项向上直到 `## ` 小节都没有 `> **原句 N:**` 行"
                            "（要么上方缺引语行，要么它被未标注的正文劈开——"
                            "前者补引语行，后者把正文并回上一条子项）"))
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
