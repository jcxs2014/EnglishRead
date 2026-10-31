抽样章（先定后读）：ch00, ch05, ch10, ch15, ch20, ch25, ch30, ch35, ch40, ch45, ch50, ch57 —— 全书 58 章，>40 章规则取 1/5（12 章），首章与末章必含，其余等距（每 5 章取 1）。

## 一、机器层（先跑完再人判）

- `bash scripts/gate.sh` → 正门 0 条阻断型，退出码 0；总览三篇 ⑭ verify_overview_quotes：概述 24/24 ✅、金句 25/25 ✅、情感节点 22/22 ✅；⑯ 跨章指认 0 伪造；⑲ 分析密度 100%。
- `python3 scripts/assertion_scan.py` → 1077 行候选 / 61 个文件，原始输出见同目录 `t1-candidates.txt`。

## 二、人判（改前 → 改后）

| 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|
| 00_金句精选.md ⑰ | 引语截到 `‘Once root, now nest,’ I said.` 并补了原文没有的收引号 | 整句 `‘Once root, now nest. He has no love of the Synod; he and Isen were raised Cynghal, not like their brothers in Galen.’` | ch42：该句在本段内连续，句末无提前收引号 |
| 00_概述.md 第六部 | 引语按「（ch49）（ch50）（ch51）」行内连写，标签被前一条吃掉（⑮ 报 ch49 标引语实属 ch50） | 改为叙述段 + 三条独立 `> "…"（chNN）` 引用块 | 各条引语分别在 ch49 / ch50 / ch51 正文 |
| 00_概述.md 第七部 | 同上（ch56 标签下压着 ch57 的引语） | 同上，两段拆开 | ch56 / ch57 各自正文 |
| 00_情感节点.md 节点四 | 「同一天，Elise 在房里织挂毯」——把相邻两章并成一天 | 「紧接着的一章里」 | ch32 与 ch33 是相邻两章，原文未说同日 |

## 三、抽读的断言（回原文查证，未改）

- ch00「Marolyn 十五岁、长她一岁」→ `a year my senior` 命中。
- ch41「Ziyan 报出五天」→ `‘Five days,’ he said at last.` 命中。
- ch34「salt 是辛格人毁林的手段」→ `Salt had been buried where the old roots had been` 命中。
- ch30「天鹅肝配血与金、在无光月下蒸馏」→ `Distilled from a swan’s liver, mixed with blood and gold under a shaded moon` 命中。
- ch57「分别不到六个月」→ `Not six moons` 命中。
- ch52「tangle of hurt and fear…」→ 本章原文命中（总览引用处）。

## 四、候选行读了多少

①相对章号 25 行全读；②绝对断言 266 行全读；⑥场景方位 27 行全读；③年龄数字 466 行按抽样章过滤后读 68 行；④亲属身份 232 行抽 20 行；⑤方向施受 61 行抽 20 行。合计读 406 行（原始 1077 行）。

## 五、结论

缺陷密度 = 阻断 1 ÷ 12 章 ≈ 0.08 < 0.2，不触发加倍抽样；「≥3 条阻断」与「同一成因类跨 ≥2 章」均未出现，**不自动进 T2**。
未修 0 条：上表四条已全部就地修复并复跑 gate（退出码 0）。
遗留提示（不修）：00_金句精选.md 25 条仍为行内引语，工具建议迁为引用块——格式建议，非事实问题。
本 T1 为**同会话自检**（写作方与审查方同一会话），非异会话验收。
