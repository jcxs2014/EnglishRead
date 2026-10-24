# ch10 · T3 判定表

- 章：Chapter Ten: 1993（md：`ch10 chapter ten 1993.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 10 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 42 | quit working / swim test / the beach | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 53 | concession guy / walkie-talkie / 94th Street | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 46 | Chief / give birth / administer care | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 49 | Tony / headphones on / curse Paul out | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 61 | the rip / whistled / his job | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 50 | Rockaway Action Committee / Mary Leahy / elect | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 41 | Olympic-size pool / Riis Park / Schumer | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 66 | District 27 / media center / media literacy | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 40 | run for office / thorn in the politicians / do | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 53 | Lynbrook / sold our house / our home | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「那根刺」 | text/ch10_chapter_ten_1993.txt:78：原文逐字：I wanted to be a thorn in the politicians’ asses, but I didn’t want their jobs. | 回原文核对后成立 | 假红 |
| 「搬到一小时车程外的长岛 Lynbrook」 | text/ch10_chapter_ten_1993.txt：原文逐字：Bob and I sold our house and moved an hour away to Lynbrook | 回原文核对后成立 | 假红 |
| 「Schumer 答应过会建，却始终没有下文」 | text/ch10_chapter_ten_1993.txt：原文逐字：Schumer had promised us a pool… and then nothing happened | 回原文核对后成立 | 假红 |

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
| 「那根刺」 | 回原文逐字核对一致 | 原文逐字：I wanted to be a thorn in the politicians’ asses, but I didn’t want their jobs. | text/ch10_chapter_ten_1993.txt:78 |
| 「搬到一小时车程外的长岛 Lynbrook」 | 回原文逐字核对一致 | 原文逐字：Bob and I sold our house and moved an hour away to Lynbrook | text/ch10_chapter_ten_1993.txt |
| 「Schumer 答应过会建，却始终没有下文」 | 回原文逐字核对一致 | 原文逐字：Schumer had promised us a pool… and then nothing happened | text/ch10_chapter_ten_1993.txt |
