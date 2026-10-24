# ch11 · T3 判定表

- 章：Chapter Eleven: 1994（md：`ch11 chapter eleven 1994.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 6 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 52 | tipped off / public advocate / mismanagement | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 62 | the test / another assignment / couldn’t even  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 58 | prerequisite / thirty-five seconds / top eight | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 57 | Nine drownings / mandated by law / wading pool | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 53 | 65th Street / a dictator / document that said  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 42 | union grievance / capitulated / dashed right t | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「泳池里五十码对海里的上千码」 | text/ch11_chapter_eleven_1994.txt:22：原文逐字：swim fifty yards in a pool in thirty-five seconds or less. Meanwhile, in Los Angeles, you had to do a tho | 回原文核对后成立 | 假红 |
| 「自 1988 年以来共发生九起溺亡，其中五起缺员」 | text/ch11_chapter_eleven_1994.txt：原文逐字：Nine drownings had occurred since 1988, and in five of them, there weren’t enough lifeguards on the beach | 回原文核对后成立 | 假红 |
| 「两年后一切又回到原点」 | text/ch11_chapter_eleven_1994.txt:78：原文逐字：Just two years after the Green report came out, the union boys were back in charge, and we were right bac | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：6/6 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 6 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- （无）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「泳池里五十码对海里的上千码」 | 回原文逐字核对一致 | 原文逐字：swim fifty yards in a pool in thirty-five seconds or less. Meanwhile, in Los Angeles, you had to do a thousand-yard swim in the ocean | text/ch11_chapter_eleven_1994.txt:22 |
| 「自 1988 年以来共发生九起溺亡，其中五起缺员」 | 回原文逐字核对一致 | 原文逐字：Nine drownings had occurred since 1988, and in five of them, there weren’t enough lifeguards on the beach as mandated by law | text/ch11_chapter_eleven_1994.txt |
| 「两年后一切又回到原点」 | 回原文逐字核对一致 | 原文逐字：Just two years after the Green report came out, the union boys were back in charge, and we were right back where we began. | text/ch11_chapter_eleven_1994.txt:78 |
