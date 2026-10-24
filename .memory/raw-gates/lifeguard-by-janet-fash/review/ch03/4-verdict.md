# ch03 · T3 判定表

- 章：Chapter Three: 1981（md：`ch03 chapter three 1981.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 10 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 48 | bungalow / respected / belonged | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 68 | Artie / shared the chair / good partner | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 57 | New York’s Finest / New York’s Wettest / publi | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 44 | only once / come back and thank / photograph | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 62 | bathing cap / porpoise / panicked | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 48 | diving in the right direction / against the cu | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 47 | oxygen tank / Kevin / CPR | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 44 | on your watch / considered a murderer / buy a  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 55 | the chiefs / weren’t even there / the paperwor | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 50 | switch from accounting to communications / SUN | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「New York’s Wettest」 | text/ch03_chapter_three_1981.txt：原文逐字：The police called themselves New York’s Finest, the firemen were New York’s Bravest, and the sanitation w | 回原文核对后成立 | 假红 |
| 「被调到底区的 17 街岗亭」（导航层） | text/ch03_chapter_three_1981.txt:13：原文逐字：they sent us to the boondocks, all the way downtown to 17th Street | 回原文核对后成立 | 假红 |
| 「Barbara 逆着水流朝那条线游过去」 | text/ch03_chapter_three_1981.txt：原文逐字：She said that once she was in the water, she immediately knew the lifeguards weren’t diving in the right  | 回原文核对后成立 | 假红 |

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
| 「New York’s Wettest」 | 回原文逐字核对一致 | 原文逐字：The police called themselves New York’s Finest, the firemen were New York’s Bravest, and the sanitation workers were New York’s Strongest. We called ourselves New York’s Wettest. | text/ch03_chapter_three_1981.txt |
| 「被调到底区的 17 街岗亭」（导航层） | 回原文逐字核对一致 | 原文逐字：they sent us to the boondocks, all the way downtown to 17th Street | text/ch03_chapter_three_1981.txt:13 |
| 「Barbara 逆着水流朝那条线游过去」 | 回原文逐字核对一致 | 原文逐字：She said that once she was in the water, she immediately knew the lifeguards weren’t diving in the right direction…the current was pulling the submerged guy away from the line. Barbara swam toward the line against the current. | text/ch03_chapter_three_1981.txt |
