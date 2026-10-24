# ch18 · T3 判定表

- 章：Chapter Eighteen: 2023（md：`ch18 chapter eighteen 2023.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 12 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 37 | Bubba / Stein / AFSCME | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 61 | Stein / dual roles / any recourse | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 55 | came to a head / mismanagement / five hundred | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 64 | medical leave / skin cancer / five-day class | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 51 | retention / part-time / unions | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 63 | technically closed / Helen / 911 | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 61 | the New York Daily News / rip current / no ava | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 51 | Rodriguez-Rosa / The Rockaway Times / It can o | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 47 | Stein / Justin / punished | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 33 | pulled one last move / retired / eighty years  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 11 | 56 | found guilty / a slap on his wrist / on his ow | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 12 | 40 | democratic union / brush us off / no longer un | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「Stein 以八十岁高龄退休」 | text/ch18_chapter_eighteen_2023.txt:82：原文逐字：After more than six decades…he retired…He was eighty years old. | 回原文核对后成立 | 假红 |
| 「AFSCME 判他与两名副手违反工会章程，却只给正式谴责」 | text/ch18_chapter_eighteen_2023.txt:103：原文逐字：They ruled that Stein and two of his deputies, Rodriguez and Neil Veloz, had violated the union constitut | 回原文核对后成立 | 假红 |
| 「Helen 在 108 街看到一群女孩有危险，拨了 911」（2022 年） | text/ch18_chapter_eighteen_2023.txt:41：原文逐字：In 2022, my sister Helen was walking along the beach…she called 911…It was 5:50 p.m., ten minutes before  | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：12/12 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 12 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- （无）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「Stein 以八十岁高龄退休」 | 回原文逐字核对一致 | 原文逐字：After more than six decades…he retired…He was eighty years old. | text/ch18_chapter_eighteen_2023.txt:82 |
| 「AFSCME 判他与两名副手违反工会章程，却只给正式谴责」 | 回原文逐字核对一致 | 原文逐字：They ruled that Stein and two of his deputies, Rodriguez and Neil Veloz, had violated the union constitution…they just issued a formal reprimand | text/ch18_chapter_eighteen_2023.txt:103 |
| 「Helen 在 108 街看到一群女孩有危险，拨了 911」（2022 年） | 回原文逐字核对一致 | 原文逐字：In 2022, my sister Helen was walking along the beach…she called 911…It was 5:50 p.m., ten minutes before they were off duty. | text/ch18_chapter_eighteen_2023.txt:41 |
