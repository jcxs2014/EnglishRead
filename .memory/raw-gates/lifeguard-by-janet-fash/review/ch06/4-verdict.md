# ch06 · T3 判定表

- 章：Chapter Six: 1985（md：`ch06 chapter six 1985.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 10 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 38 | exceptional day / multiple rescues / take a br | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 53 | official protocol / no direction / not at work | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 64 | split the chairs / no one was on the chair / m | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 49 | bodysurfed in / strong rip current / sucked ou | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 31 | Whitey / started screaming / too late | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 48 | confirmed submersion / stay behind / helplessn | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 50 | Long Island beaches / more than ten miles / go | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 38 | pull everyone out of the water / It worked / n | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 42 | ten dollars / politicians’ campaigns / swim te | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 48 | citywide lifeguard coordinator / managing what | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「此后十九年她这片海滩才再出一次溺亡」 | text/ch06_chapter_six_1985.txt:31：原文逐字：After that first summer, it took nineteen more years before another drowning happened on my beach. | 回原文核对后成立 | 假红 |
| 「她把两把椅子拆开守」 | text/ch06_chapter_six_1985.txt:19：原文逐字：Because we didn’t have enough people that day, I decided to split the chairs… | 回原文核对后成立 | 假红 |
| 「遗体在十英里外的海滩寻获」 | text/ch06_chapter_six_1985.txt:25：原文逐字：He was eventually found on one of the Long Island beaches east of Rockaway, more than ten miles away. | 回原文核对后成立 | 假红 |

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
| 「此后十九年她这片海滩才再出一次溺亡」 | 回原文逐字核对一致 | 原文逐字：After that first summer, it took nineteen more years before another drowning happened on my beach. | text/ch06_chapter_six_1985.txt:31 |
| 「她把两把椅子拆开守」 | 回原文逐字核对一致 | 原文逐字：Because we didn’t have enough people that day, I decided to split the chairs… | text/ch06_chapter_six_1985.txt:19 |
| 「遗体在十英里外的海滩寻获」 | 回原文逐字核对一致 | 原文逐字：He was eventually found on one of the Long Island beaches east of Rockaway, more than ten miles away. | text/ch06_chapter_six_1985.txt:25 |
