# ch43（Chapter Forty-Two）深审 R5 判定

> 机器层：`2-machine.json` rc=0，8 块精读，segment_miss 0。
> R1 素读：`1-suread.json` 20 facts，全部回源命中（MISS 0）。

## R3 三张单子

- **词表**：v43 探针 14 行，例句逐字命中 14／14。
- **撇号**：ap43 直撇号 token 0，backtick span 0。
- **块内嵌英文**：in43 未命中 2，均为模板（首跑 61 条系派生脚本 text 文件名写错所致工具误用，修正后复跑确认）。

## 判定汇总

- **阻断：1**
  - **C-43-1**：原句5 中文理解「沉默了五年半」——原文 L210 "half a decade"＝五年；时间错译（先例 C-34-1 同型）。
- **提示：0**
- **假红：0**

## R4 逐块对应（8 块）

| 块 | 取证 | 结论 |
|---|---|---|
| 原1 flashlight／portrait／goosebumps | L9 逐字 | ✓ |
| 原2 impassive／forgiveness／regret | L66 逐字 | ✓ |
| 原3 bolt gun／turn me in／survived | L174 逐字 | ✓ |
| 原4 headlines／bastard／spare heir | L180 逐字 | ✓ |
| 原5 half a decade／woodwork／blackmail／croaked／trusted him | L210 逐字（中文时间错译见 C-43-1） | ✓（引语） |
| 原6 legacy／rotting／following orders／done | L255 后段逐字（机器层核） | ✓ |
| 原7 processing／closed the distance／slaughtering／calculated | L278 逐字 | ✓ |
| 原8 tunneled／dimming／black frame／surprised | L285 逐字 | ✓ |

## 导航层断言

14 项断言全部回源命中（详见 3-diff.md）；时序（办公室→走廊→后门→池边→砸额→推倒→视野收暗）与原文一致。

## 已核实为正确

- 引语 8 块逐字（s43 20 facts MISS 0；机器层 segment_miss 0）。
- 词表 14 行例句逐字；Greg＝Harrison 父亲（L207 "Harrison's father, presumably"）与人物弧线一致；Dartrine 真名 L234 原文出现。
- 三种死法（Michelle/Leon/Mama）本章按原文转述（heart attack 记录 L255），未裁决。
