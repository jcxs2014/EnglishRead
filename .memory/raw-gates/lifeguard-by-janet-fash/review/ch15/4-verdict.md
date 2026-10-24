# ch15 · T3 判定表

- 章：Chapter Fifteen: 2016（md：`ch15 chapter fifteen 2016.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 11 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 43 | Freddie Bomhoff / closest allies / dying of ol | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 42 | Trump / just like you / won’t vote for him | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 64 | out of the blue / swim team / targeting | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 60 | promoted / open-water test / high-top sneakers | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 51 | ransom note / retaliation / Meet the Godfather | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 61 | installed / ineligible / $230,000 | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 30 | March 31, 2020 / COVID hit / shut down | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 39 | two sessions / over Zoom / never held a union  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 31 | AFSCME panel / violated the constitution / bar | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 37 | house in the Bronx / aboveground pool / lifegu | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 11 | 30 | in February / twenty-two full-time lifeguards  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「Stein 七十多岁」 | text/ch15_chapter_fifteen_2016.txt:13：原文逐字：he had been working as a lifeguard for almost six decades and he was already in his seventies. | 回原文核对后成立 | 假红 |
| 「亲自跑到她的棚屋坐了两小时」 | text/ch15_chapter_fifteen_2016.txt:34：原文逐字：And for two hours he did. | 回原文核对后成立 | 假红 |
| 「Stein 本人年入一度高到 23 万美元」 | text/ch15_chapter_fifteen_2016.txt：原文逐字：Stein himself was making as much as $230,000 | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：11/11 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 11 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- （无）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「Stein 七十多岁」 | 回原文逐字核对一致 | 原文逐字：he had been working as a lifeguard for almost six decades and he was already in his seventies. | text/ch15_chapter_fifteen_2016.txt:13 |
| 「亲自跑到她的棚屋坐了两小时」 | 回原文逐字核对一致 | 原文逐字：And for two hours he did. | text/ch15_chapter_fifteen_2016.txt:34 |
| 「Stein 本人年入一度高到 23 万美元」 | 回原文逐字核对一致 | 原文逐字：Stein himself was making as much as $230,000 | text/ch15_chapter_fifteen_2016.txt |
