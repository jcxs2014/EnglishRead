# ch20 · T3 判定表

- 章：Photographs（md：`ch20 photographs.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 3 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 25 | Empire State Games / sponsor / Miller Lite | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 19 | off-duty rescue / watching the water / always | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 47 | urban agglomerations / city surfer / ethnicity | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 1/原句 2 分别为 25/19 词，低于 30–70 词软下限 | （见左）提示型，不改：本章是照片说明体，单条说明在原文即是一两句短文；扩引语必须缝进相邻两条说明或叙述句，反而破坏「一条说明一块」的体裁对应（chapter.sh 亦不判下限） | 表面成立，措辞正当 | 提示 |
| 「救生员 Jennifer Tubridy 和她的姐妹俩在 97 街下班后实施了一次救援」 | text/ch20_photographs.txt:54：原文逐字：Lifeguard Jennifer Tubridy and her sisters performed an off-duty rescue at 97th Street. | 回原文核对后成立 | 假红 |
| 「从四岁在水里」 | text/ch20_photographs.txt：原文逐字：Swimming in the bay at four years old with my sister Mary, my cousin Maureen, and my brother Pat. Highlan | 回原文核对后成立 | 假红 |
| 「末条借摄影师的话说：这座城市的冲浪者是所有人」 | text/ch20_photographs.txt:76：原文逐字：the city surfer is everyone: men, women, pro surfers, incredible artists, firefighters, and people of eve | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：3/3 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 3 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- **[形态]** 原句 1/原句 2 分别为 25/19 词，低于 30–70 词软下限
  - 判定：提示型，不改：本章是照片说明体，单条说明在原文即是一两句短文；扩引语必须缝进相邻两条说明或叙述句，反而破坏「一条说明一块」的体裁对应（chapter.sh 亦不判下限）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「救生员 Jennifer Tubridy 和她的姐妹俩在 97 街下班后实施了一次救援」 | 回原文逐字核对一致 | 原文逐字：Lifeguard Jennifer Tubridy and her sisters performed an off-duty rescue at 97th Street. | text/ch20_photographs.txt:54 |
| 「从四岁在水里」 | 回原文逐字核对一致 | 原文逐字：Swimming in the bay at four years old with my sister Mary, my cousin Maureen, and my brother Pat. Highlands, NJ. | text/ch20_photographs.txt |
| 「末条借摄影师的话说：这座城市的冲浪者是所有人」 | 回原文逐字核对一致 | 原文逐字：the city surfer is everyone: men, women, pro surfers, incredible artists, firefighters, and people of every ethnicity. | text/ch20_photographs.txt:76 |
