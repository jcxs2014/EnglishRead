# ch08 · T3 判定表

- 章：Chapter Eight: 1988（md：`ch08 chapter eight 1988.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 10 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 50 | Kim Lonergan / women lieutenants / first femal | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 53 | Stein’s school / both of my jobs / more contro | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 55 | Bert Kis / Mike Doda / over three hundred resc | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 44 | different personalities / gravity of our job / | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 52 | Sher / swim test / get back at you | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 66 | deferring to my superiors / wait for central o | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 62 | June 1990 / 44th Street / Edgemere | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 54 | Joe McManus / 32nd Street / dive lines | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 44 | Regina / falsify the reports / bathing suit | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 48 | preventable / negligence / $2 million | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「罗克韦只有两名女性副队长——她和 Kim Lonergan」 | text/ch08_chapter_eight_1988.txt:16：原文逐字：there were two women lieutenants in Rockaway—me and Kim Lonergan—so I told him that either one of us coul | 回原文核对后成立 | 假红 |
| 「被当作『摆设』的象征头衔」 | text/ch08_chapter_eight_1988.txt:19：原文逐字：they made me the symbolic “first female chief” lifeguard of New York City | 回原文核对后成立 | 假红 |
| 「纽约市赔了两百万美元」 | text/ch08_chapter_eight_1988.txt：原文逐字：the city agreed to pay the families two million dollars | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：10/10 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 10 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- （无）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「罗克韦只有两名女性副队长——她和 Kim Lonergan」 | 回原文逐字核对一致 | 原文逐字：there were two women lieutenants in Rockaway—me and Kim Lonergan—so I told him that either one of us could become the first female chief. | text/ch08_chapter_eight_1988.txt:16 |
| 「被当作『摆设』的象征头衔」 | 回原文逐字核对一致 | 原文逐字：they made me the symbolic “first female chief” lifeguard of New York City | text/ch08_chapter_eight_1988.txt:19 |
| 「纽约市赔了两百万美元」 | 回原文逐字核对一致 | 原文逐字：the city agreed to pay the families two million dollars | text/ch08_chapter_eight_1988.txt |
