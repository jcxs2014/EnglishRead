# ch41（Chapter Forty）深审 R5 判定

> 机器层：`2-machine.json` rc=0，9 块精读，segment_miss 0。
> R1 素读：`1-suread.json` 20 facts，全部回源命中（MISS 0）。

## R3 三张单子

- **词表**：v41 探针 25 行，例句逐字命中 25／25。
- **撇号**：ap41 直撇号 token 1 → 阻断 C-41-1；backtick span 0。
- **块内嵌英文**：in41 未命中 5，模板 2，其余 2 项均判假红（见下）。

## 判定汇总

- **阻断：1**
  - **C-41-1**（引原文用 ASCII 直撇号，先例 C-34-2／C-35-1／C-38-1 同型）：md L10「Greer line was tainted by Ida's blood」——原文 text/ch41_chapter_forty.txt:180 为 `Ida’s`（弯撇号）。
- **提示：0**
- **假红：2**
  - **F-41-1**：in41 标 `feet too hot` 查无——叙事手法层把 L111 "My feet felt too hot all of a sudden" 压缩成引理；stomach turned（L87）逐字在。引理形态非引语，不构成缺陷。
  - **F-41-2**：in41 标 `Gazzie-Caroline` 查无——原句5「为什么这样写」层分析者自造连字标签，两要素均在 L96/L126 原文，非引语形态。

## R4 逐块对应（9 块）

| 块 | 取证 | 结论 |
|---|---|---|
| 原1 figure/blinds/negligence/forgive | L9 逐字 | ✓ |
| 原2 mudroom/curious glance/caged snake | L18 逐字 | ✓ |
| 原3 great-aunt/celebration/four hours | L30＋L36 逐字 | ✓ |
| 原4 boot/grinding | L84（suread）＋L90 legacy/to a T | ✓ |
| 原5 taught her children/college tuition/punishment | L96＋L102（引语逐字） | ✓ |
| 原6 intentional/pulse/rolled/prod | L136 附近（suread L138）逐字 | ✓ |
| 原7 Greer line/tainted/fighting chance | L180 逐字 | ✓ |
| 原8 I killed Mama, too/like stones | L216 逐字 | ✓ |
| 原9 relishing/sabotage | L273 逐字 | ✓ |

## 导航层断言

17 项断言（breath in short bursts L9、less incriminating L117、"Am I?" L201、推倒/facture 词表 L249、water bottle/Should you drink L51、my inheritance/peacemaker L108、"Uncle Leon," firmly L93、"What?" L99、"Or what?" L150、stomach turned L87、feet too hot L111（引理）、Tainted 单独成句 L183、Cat Two/four hours L30/L36、hurtling through Ocala L288、报纸袋掉包 L285、seawall L306、My mother didn't marry L168、devil inside L189、heart attack L222、final key L270）——全部回源命中。

## 已核实为正确

- 引语 9 块逐字（s41 20 facts MISS 0；机器层 segment_miss 0）。
- 词表 25 行例句逐字；wickedness 例句 Michelle 前史与 L186 一致；dead三死法（Michelle/Leon/Mama）本章仅按原文转述，未裁决。
- 时序（雨夜→火边口供→Caroline 线→自首→揭 Harrison→报纸袋→海堤）与原文一致。
