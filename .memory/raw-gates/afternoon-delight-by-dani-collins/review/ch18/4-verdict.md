# ch18 · T3 判定表

- 章：ch18 chapter eighteen meg.md
- R1 素读：`1-suread.json`（审查会话独立只读 `text/`，未参考 md；8 条事实带字符区间）
- R2 机器层：`2-machine.json`（第二实现；verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 6 块，逐块 R4 + R5；**无「只有机器层」的章**

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 24 | slow down / stay home to play / forget about the shop | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 22 | freaking the fuck out / don’t care anymore / can’t stay like this | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 29 | stroking the top edge / top-of-the-line / 1971 Zenith Allegro | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 33 | talk me down / $15 / double my money | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 29 | the hustler / elbow in / someone coming back for it | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 6 | No / said together | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 全章 6 块引语逐字 + 分析层对应 + 施事三问 | text/ch18_chapter_eighteen_meg.txt（8 条 R1 事实锚点全部命中） | 四层（逐字/对应/形态/断言）均通过 | 通过 |

## 分组计数（只报四组）

- **逐字**：6/6 块整串命中（`2-machine.json` verdict=ok；末引号形态差异见「已核实为正确」）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 6 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 0

## 已核实为正确

以下写法看似可疑，回原文核对后成立——**后续任何人不得以「读着不对」为由改动，除非能给出反证**：

- ch18 原句 3「Nice,” Zak said…”：md 直引号 / 原文弯引号，属形态假红。

## 覆盖声明

- 本章 6 块全部经 R4 逐块对应 + R5 判定，无「只有机器层」的章。
- 未审项：无。
