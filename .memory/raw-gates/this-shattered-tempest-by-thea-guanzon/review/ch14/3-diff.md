# ch14 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch14 the whirlwind dream of childhood.md`
- 原文：`text/ch14_chapter_fourteen.txt`（`char_total` = 18806）
- 素读底稿：`review/ch14/1-suread.json`（events 8 / relations 5 / numbers 5，18/18 命中）
- 机器层：`review/ch14/2-machine.json`（verdict ok，修前块数 10、本章 3318 词、建议 6–10）

## R3 三张单子

### 漏

| # | 素读事件 | 处置 |
|---|---|---|
| L1 | event 7：抵达城塞后他把「夜皇后寝宫」指给她，而这间屋子原属他母亲、已被清空得没有一丝私物 | 修前 10 块只写到「进屋」，**没有这间屋子的来历** → 新增 **原句 10**（`text/ch14_chapter_fourteen.txt:197`，35 词、单段：`These chambers had once belonged…personal touches she’d left behind?`）；他那句「最近翻新过」在上一段（`:191`，15 词、低于硬线），提示里标注 |

### 编 / 错

无。块 5 `We’ll see` 的处置对应 `:170` 附近（修前 3 处提及）；块 8 的 `No.` 单句独立成段对应 `:154`；块 9 的「不让你独自见他」对应 `:189`。

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 素读 `seven`（七个月亮只出现一个）未进 md | 记一行不改（氛围细节，不承载情节） |
| T2 | `quarter past midnight` 未进 md | 记一行不改（时刻细节；本章无跨日事件） |

## 修复后复跑

`chapter.sh` rc=0、0 ⚠️（块数 11）；`check_para_span.py` OK；`gate.sh` rc=0。
