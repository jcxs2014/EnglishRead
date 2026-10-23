# ch44（Chapter Forty-Three）深审 R5 判定

> 机器层：`2-machine.json` rc=0，7 块精读，segment_miss 0。
> R1 素读：`1-suread.json` 20 facts，全部回源命中（MISS 0）。

## R3 三张单子

- **词表**：v44 探针 14 行，例句逐字命中 14／14。
- **撇号**：ap44 直撇号 token 0，backtick span 0。
- **块内嵌英文**：in44 未命中 2，均为模板。

## 判定汇总

- **阻断：0**
- **提示：0**
- **假红：0**

## R4 逐块对应（7 块）

| 块 | 取证（text/ch44_chapter_forty_three.txt） | 结论 |
|---|---|---|
| 原1 revealed/infiltrated/sway/legacy | L27 逐字 | ✓ |
| 原2 barbed wire/ten-foot/padlock/wound | L60 逐字 | ✓ |
| 原3 melon-sized/calculated/Eight/snips | L92–96 逐字 | ✓ |
| 原4 slammed/snout/packed dirt/resistance | L105 段逐字（引语） | ✓ |
| 原5 determined/convince/great-great-grandmother/on their side | L132 段逐字 | ✓ |
| 原6 bend/reasoning/irredeemable/damned | L198 逐字 | ✓ |
| 原7 loose/promise/make things right | L201 逐字 | ✓ |

## 导航层断言

12 项断言全部回源命中（详见 3-diff.md）；「对满池逼近的黄色眼睛」＝Countless yellow eyes（L105），与快审护栏「无『数十』口径」一致；「gate 挂锁、无『门上挂着锁』」护栏未被违反（md 只写 padlock wound around it）。

## 已核实为正确

- 引语 7 块逐字（s44 20 facts MISS 0；机器层 segment_miss 0）。
- 词表 14 行例句逐字；快审护栏两条（鳄鱼数口径、锁的写法）复核未违反。
- 时序（梦→醒→剪网→被咬→扎鳄→喊话→包扎→飓风眼→判词→驶向 Greer House）与原文一致。
