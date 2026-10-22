# ch01 判定（首章 · 快审）

- 机器层：`chapter.sh --json` rc=0；8 块 / 9 片段全部逐字命中；gate.sh 该书 0 条阻断。
- 人判：1 提示（整段动作高潮未取块）+ 1 提示（原句 2 外推）。
- 阻断：0。档位：**无阻断**。

## 已核实为正确
- 引语 8 块逐字对应 `text/ch01_chapter_one.txt`，含跨段 `…` 块（账单块）两段各自可独立取证。
- 人物归属正确：摇铃立尸、贴符、斩首、开单均归 Por Por；拔符吻尸归醉军官；Kiamling 只做递符与收尸。
- 「Too late…」两句归 Kiamling 内心叙述，非人物台词。
- 数字/物件无错：四具尸体、八卦镜、糯米、铜钱剑、账单三项。

## 修复复验（2026-10-22 21:45）
- 已补第 6 块（`text/ch01_chapter_one.txt:100`）：「A dull thud sounded as Por Por’s staff smacked into the side of the geongsi’s head. The monster swayed for a moment before toppling. For good measure she reattached a talisman to its forehead.」（3 句 / 37 词 / 单段），原句 6–8 顺延为 7–9。
- 首版插错位置（先插成原句 6），`structure.py order` 立刻报「原句 7（md:57）在原文里位于原句 6 之前」——因为 "Too late to consider…" 在第 76 行、祖母杖击在第 100 行；已交换两块次序并顺序重编号。
- `chapter.sh` → CHAPTER_EXIT=0（9 块 / 10 片段 / 查无 0 / 关键词 0 / 中文过薄 0）；`structure.py order` 对 ch01 无报错；`gate.sh` rc=0；分片 581-0。
- 结论：**提示级「动作高潮未取块」已闭合**；块数 9 对建议 5–8 为 ⚠️ 提示（硬限 15 内）。
