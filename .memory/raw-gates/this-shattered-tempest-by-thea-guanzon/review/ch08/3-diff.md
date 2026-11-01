# ch08 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch08 the roof of heaven on high alert.md`
- 原文：`text/ch08_chapter_eight.txt`（`char_total` = 16116）
- 素读底稿：`review/ch08/1-suread.json`（events 7 / relations 4 / numbers 4，15/15 命中）
- 机器层：`review/ch08/2-machine.json`（verdict ok，修前块数 8、本章 2709 词、建议 5–8）

## R2 对账

修前 8 块（逐字查无 0）；修后 **11 块**（新增 3 块），落在本书分布区间 5–13 内，0 ⚠️。

## R3 三张单子

### 漏

| # | 素读事件 | 取证与处置 |
|---|---|---|
| L1 | 两名长矛手交叉长矛拦住走廊，只放两位陛下入内 | `text/ch08_chapter_eight.txt:60`（40 词、单段）→ 新增 **原句 5** |
| L2 | 阿拉里克拒绝解下佩剑（`Hang your protocols`） | `:99`（66 词、单段）→ 新增 **原句 6** |
| L3 | 她提出回伊安塔斯主持追查、最迟明晚回话，乌尔杜佳挥手令卫兵放下火枪 | `:204`（49 词、单段）→ 新增 **原句 10**；「放下火枪」在紧随的下一段，已在提示里标注 |

### 编 / 错

无。块 7（修前 5）「铁镣反绑、双臂像台钳」对应 `pinned her arms like a vise, her hands manacled behind her back`；块 9（修前 7）「没有达雅·维卡尔谁都熬不过噬世者之夜」对应 `Without Daya Vaikar, none of us would have made it through the Night of the World-Eater`。

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 修前块数 8 已到「建议 5–8」上沿，三处事件因此无处安放 | 已补 3 块；11 块仍在硬限 2–15 与本书区间 5–13 内 |
| T2 | 关键词行长度 | 已全局收紧（`26e3efd2b`） |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️（块数 11）；`check_para_span.py` OK；`gate.sh` rc=0。
