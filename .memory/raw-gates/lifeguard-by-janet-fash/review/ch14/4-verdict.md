# ch14 · T3 判定表

- 章：Chapter Fourteen: 2012（md：`ch14 chapter fourteen 2012.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 9 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 53 | Hurricane Sandy / refuge / grid | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 60 | 126 homes / hellish dominoes / Ocean Avenue | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 54 | storm surge / full moon / destroyed boardwalk | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 49 | nineteen lifeguards / inspector general / unde | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 55 | Terrence / screaming / boogie board | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 48 | detailed lifeguards / The Public Rescues Thems | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 34 | diabetes / leukemia / fixated | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 54 | San Diego / Santa Monica / bacteria | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 49 | pod of dolphins / arch out of the water / peac | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「2012 年 10 月 29 日，飓风 Sandy 冲垮了罗克韦」 | text/ch14_chapter_fourteen_2012.txt:13：原文逐字：On October 29, 2012, Rockaway washed away. Hurricane Sandy hit the city’s shore | 回原文核对后成立 | 假红 |
| 「126 栋房子像地狱里的多米诺骨牌」 | text/ch14_chapter_fourteen_2012.txt:19：原文逐字：burning down 126 homes like a set of hellish dominoes | 回原文核对后成立 | 假红 |
| 「临终前对 Janet 说『你是我最好的朋友』」 | text/ch14_chapter_fourteen_2012.txt:63：原文逐字：Toward the end she told me, “Janet, you’re my best friend.” | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：9/9 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 9 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- （无）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「2012 年 10 月 29 日，飓风 Sandy 冲垮了罗克韦」 | 回原文逐字核对一致 | 原文逐字：On October 29, 2012, Rockaway washed away. Hurricane Sandy hit the city’s shore | text/ch14_chapter_fourteen_2012.txt:13 |
| 「126 栋房子像地狱里的多米诺骨牌」 | 回原文逐字核对一致 | 原文逐字：burning down 126 homes like a set of hellish dominoes | text/ch14_chapter_fourteen_2012.txt:19 |
| 「临终前对 Janet 说『你是我最好的朋友』」 | 回原文逐字核对一致 | 原文逐字：Toward the end she told me, “Janet, you’re my best friend.” | text/ch14_chapter_fourteen_2012.txt:63 |
