# ch07 · T3 判定表

- 章：Chapter Seven: 1987（md：`ch07 chapter seven 1987.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 9 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 45 | six years younger / second-youngest child / ha | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 55 | midnight shift / seat belt / guardrail | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 68 | grouchy / nice morning / seat belt | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 66 | instinctive drowning response / breathing must | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 49 | felt like I was drowning / four days off / ran | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 47 | family bungalow / not laying in this bed / thi | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 60 | passed away / neighbor Grace / St. Saviour Chu | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 41 | best man / walked down the aisle / wishing she | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 50 | volleyball league / pieces of my life / beginn | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「Pia 写下这句话……本能性溺水反应」 | text/ch07_chapter_seven_1987.txt：原文逐字：“In times of extreme peril in the water, breathing must take precedence over speech,” Pia wrote. He coine | 回原文核对后成立 | 假红 |
| 「John 去世两年后，母亲在公园坡地的公寓里过世」 | text/ch07_chapter_seven_1987.txt:60：原文逐字：Just two years after John died, my mother passed away at our apartment in Park Slope. | 回原文核对后成立 | 假红 |
| 「救生员搭档 Brian 做了 Bob 的伴郎」 | text/ch07_chapter_seven_1987.txt：原文逐字：Brian, my partner in the lifeguard chair, was Bob’s best man. | 回原文核对后成立 | 假红 |

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
| 「Pia 写下这句话……本能性溺水反应」 | 回原文逐字核对一致 | 原文逐字：“In times of extreme peril in the water, breathing must take precedence over speech,” Pia wrote. He coined the term “instinctive drowning response” | text/ch07_chapter_seven_1987.txt |
| 「John 去世两年后，母亲在公园坡地的公寓里过世」 | 回原文逐字核对一致 | 原文逐字：Just two years after John died, my mother passed away at our apartment in Park Slope. | text/ch07_chapter_seven_1987.txt:60 |
| 「救生员搭档 Brian 做了 Bob 的伴郎」 | 回原文逐字核对一致 | 原文逐字：Brian, my partner in the lifeguard chair, was Bob’s best man. | text/ch07_chapter_seven_1987.txt |
