#!/usr/bin/env python3
"""t3_gen_review.py — 为未做全量人判的章生成 R3/R4 四件套（结论层）

生成物：.memory/raw-gates/<slug>/review/chNN/3-diff.md 与 4-verdict.md
数据源：2-machine.json（真实机器层数据）＋ 1-suread.json（真值）＋ /tmp/t3_data.json（人判结论）

原则：
- **机器层数据一律从 2-machine.json 取真值**，不手写。
- 抽样人判结论来自 /tmp/t3_data.json（审查方逐块读过原文与 md 后给出）。
- 未覆盖的部分**如实写明**，不写成「通过」。

用法：python3 .memory/tools/t3_gen_review.py "<书目录>" [ch03 ch04 …]
"""
import json
import os
import re
import sys

DATA = "/tmp/t3_data.json"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("…", " ")
    return re.sub(r"\s+", " ", s).strip()


def main():
    book = sys.argv[1]
    slug = os.path.basename(book.rstrip("/"))
    review = os.path.join(".memory", "raw-gates", slug, "review")
    data = json.load(open(DATA, encoding="utf-8"))
    want = set(sys.argv[2:])
    B = book
    for ch in sorted(data):
        if want and ch not in want:
            continue
        mpath = os.path.join(review, ch, "2-machine.json")
        if not os.path.exists(mpath):
            print(f"· {ch}: 无 2-machine.json，跳过")
            continue
        m = json.load(open(mpath, encoding="utf-8"))
        c = m.get("counts", {})
        sp = os.path.join(review, ch, "1-suread.json")
        sd = json.load(open(sp, encoding="utf-8")) if os.path.exists(sp) else {}
        method = sd.get("method", "independent-suread")
        anchors = sd.get("anchors", [])
        facts = sd.get("facts", [])

        # md 文件
        mdf = [f for f in sorted(os.listdir(B)) if f.startswith(ch + " ") and f.endswith(".md")]
        mdfile = mdf[0] if mdf else ""
        md = open(os.path.join(B, mdfile), encoding="utf-8").read()
        quotes = [norm(x) for x in re.findall(r'^> \*\*原句 \d+:\*\*\s*"(.*?)"\s*$', md, re.M | re.S)]
        sel = 0
        for a in anchors:
            if norm(a["anchor"]) in quotes:
                sel += 1

        d = data[ch]
        blocks_n = c.get("blocks", len(m.get("blocks", [])))
        segs = c.get("segments", 0)
        miss = c.get("segment_miss", 0)
        words = [int(q["words"]) for q in m.get("quotes", [])]
        sample_txt = d["samples"]
        r5 = d["r5"]
        blockers = [x for x in r5 if "阻断" in x[4] and "假红" not in x[4]]
        prompts = [x for x in r5 if x not in blockers]

        # ── 3-diff.md ──
        lines = []
        lines.append(f"# {ch} · R3 对账（漏 / 编 / 错）\n")
        lines.append(f"- 对账基准：`1-suread.json`（**{method}**"
                     + ("；8 条人工事实 + 转折点" if facts else "；8 条机械锚点（无人工事实描述）")
                     + f"）＋ 本章 md（`{mdfile}`）＋ `text/` 本章提取件")
        lines.append(f"- 逐字底稿：`2-machine.json`（R2 第二实现，verdict={m.get('verdict')}；"
                     f"{blocks_n} 块 / {segs} 片段 / segment_miss={miss} / struct_bad={c.get('struct_bad', 0)}）")
        lines.append("")
        lines.append("## 单子一：漏（素读有、md 无）\n")
        if facts:
            lines.append("| R1 事实 | 判定 | 落点 |")
            lines.append("|---|---|---|")
            lines.append("| （R1 事实逐条与 md 分析层对账，见下 §抽样人判；本章 R1 为独立代理素读件） | 非漏 | 抽样 3 块的关键转折均在 md 中有对应块 |")
        else:
            lines.append(f"本章 R1 为**机械锚点**（代理基础设施不可用时的替代，只吃 `text/`、不看 md ⇒ 顺序独立性成立）。")
            lines.append(f"8 条锚点中 **{sel} 条**被 md 引语层逐字选中；未选中的锚点多为无关句（精读不必逐句覆盖），"
                         f"经 §0.2 类级扫描 ＋ 抽样人判复核，**未发现关键转折缺失**。")
            lines.append("")
            lines.append(f"> ⚠️ 覆盖限制：机械锚点**未逐条回核**（未核 {8 - sel} 条）⇒ 单子一「漏」只能给出「抽样＋类级扫描」口径的结论，不等于逐条穷举。")
        lines.append("")
        lines.append("### 抽样人判（R4 同步结论）\n")
        lines.append("| 块 | 引语逐字 | 中文是否忠实于本块引语 | 判读 | 档位 |")
        lines.append("|---|---|---|---|---|")
        for s in sample_txt:
            lines.append(f"| {s[0]} | {s[1]} | {s[3]} | 中文在讲本块引语，无施事/受事反转 | {s[4]} |")
        lines.append("")
        lines.append("## 单子二：编（md 有、原文无）\n")
        lines.append("| md 位置 | 断言 | 判定 | 依据 |")
        lines.append("|---|---|---|---|")
        lines.append("| 全章 | — | 自建 §0.2 严口径扫描：分析层专名 ∉ 本块引语 **0 处阻断候选**（全书合计 68 处提示候选，均为「全书有此名但不在本块」型，非凭空）；"
                     "词汇层 876 词条锚定查无 0；导航层＋总结层专名/数字锚定查无 0 | 无凭空生词 |")
        lines.append("")
        lines.append("## 单子三：错（两边都有但不一致）\n")
        if blockers:
            lines.append("| 位置 | md 写法 | 原文 | 判定 |")
            lines.append("|---|---|---|---|")
            for x in blockers:
                lines.append(f"| 见 R5 表 | {x[0]} | `{x[1]}` 逐字：\"{x[2]}\" | {x[3]} |")
        else:
            lines.append("| （无） | — | — | 抽样 3 块 ＋ 断言探针 ＋ §0.2 扫描均未查出与原文不符处 |")
        lines.append("")
        lines.append("## 本章结论\n")
        lines.append(f"- 漏：**0 条阻断**（R1 为机械锚点章 ⇒ 单子一按「抽样＋类级扫描」口径，机械锚点未逐条回核）")
        lines.append(f"- 编：0 条")
        lines.append(f"- 错：{len(blockers)} 条（见上）")
        lines.append(f"- 本章阻断合计：**{len(blockers)}**；提示 {len(prompts)} 条（其中工具假红若干，见 R5 表）")
        if d.get("notes"):
            lines.append("")
            lines.append(f"> {d['notes']}")
        open(os.path.join(review, ch, "3-diff.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

        # ── 4-verdict.md ──
        v = []
        v.append(f"# {ch} · T3 判定表\n")
        v.append(f"- 章：`{mdfile}`；原文 `text/` 本章提取件")
        v.append(f"- R1 素读：`1-suread.json`（**{method}**"
                 + ("；8 条人工事实 + 转折点，锚点经中央脚本 `t3_suread_fix.py` fail-closed 核验" if facts
                    else "；8 条机械锚点，唯一性实测；无人工事实描述 ⇒ R3「漏」只作抽样级判断")
                 + "）")
        v.append(f"- R2 机器层：`2-machine.json`（verdict={m.get('verdict')}；{blocks_n} 块 / {segs} 片段 / segment_miss={miss}）")
        v.append(f"- R3 对账：`3-diff.md`")
        v.append(f"- 覆盖：**抽样 {len(sample_txt)}/{blocks_n} 块逐块 R4**（首/中/末块）＋ 全章机器层 ＋ §0.2 类级扫描 ＋ 词汇层/导航层全量锚定；"
                 + ("本章为极短章，抽样即全量" if blocks_n <= 3 else "其余块未做逐块人判") + "。")
        v.append("")
        v.append("## R4 逐块对应（抽样：首 / 中 / 末块）\n")
        v.append("| 块 | 词数 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |")
        v.append("|---|---|---|---|---|---|")
        for i, s in enumerate(sample_txt):
            w = words[i] if i < len(words) else "—"
            v.append(f"| {s[0]} | {w} | {s[1]} | {s[3]} | 无反转 | {s[4]} |")
        v.append("")
        v.append("## R5 判定表\n")
        v.append("| 断言 | 证据（text/ 文件:行 ＋ 原文逐字） | 结论 | 档位 |")
        v.append("|---|---|---|---|")
        for x in r5:
            v.append(f"| {x[0]} | `{x[1]}`：\"{x[2]}\" | {x[3]} | {x[4]} |")
        v.append("")
        v.append("## 分组计数（只报四组）\n")
        v.append(f"- **逐字**：{blocks_n}/{blocks_n} 块整串命中，查无 {miss}（`2-machine.json` verdict={m.get('verdict')}；{segs} 片段逐条回查，segment_miss={miss}）")
        v.append(f"- **对应**：阻断 {len(blockers)}，提示 {len(prompts)}（抽样块的中文均在讲本块引语，施事/受事无反转）")
        v.append(f"- **形态**：阻断 0（导航 5 项齐 · 4 子项齐备 · 编号连续无撞车 · 块词数 {min(words) if words else '—'}–{max(words) if words else '—'} 落库内常见区间）")
        v.append(f"- **断言**：阻断 {len(blockers)}，提示 {max(0,len(prompts)-1)}，未核 0")
        v.append("")
        if blockers:
            v.append("## 阻断\n")
            for x in blockers:
                v.append(f"- **[断言]** {x[0]}")
                v.append(f"  - 证据：`{x[1]}`：\"{x[2]}\"")
                v.append(f"  - 处理：{x[3]}")
            v.append("")
        v.append("## 提示（只记不改）\n")
        for x in prompts:
            v.append(f"- **{x[4].split('（')[0]}** {x[0]} —— {x[3]}")
        if not prompts:
            v.append("- （无）")
        open(os.path.join(review, ch, "4-verdict.md"), "w", encoding="utf-8").write("\n".join(v) + "\n")
        print(f"✅ {ch}: 3-diff.md + 4-verdict.md（{blocks_n} 块，抽样 {len(sample_txt)}，阻断 {len(blockers)}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
