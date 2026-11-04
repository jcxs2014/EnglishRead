# ch27 · T3 判定表

- 章：ch27 chapter twenty seven meg.md
- R1 素读：`1-suread.json`（审查会话独立只读 `text/`，未参考 md；8 条事实带字符区间）
- R2 机器层：`2-machine.json`（第二实现；verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 5 块，逐块 R4 + R5；**无「只有机器层」的章**

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 50 | wide-ass paisley ties / mint green / oversized fit | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 24 | from the bathroom / a card / if it’s legit | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 33 | guilt in the driver’s seat / coming out was a journey / still on it | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 26 | ambush / for no reason / being extra | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 28 | know where that is / on your way / introduce you to everyone | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 全章 5 块引语逐字 + 分析层对应 + 施事三问 | text/ch27_chapter_twenty_seven_meg.txt（8 条 R1 事实锚点全部命中） | 四层（逐字/对应/形态/断言）均通过 | 通过 |

## 分组计数（只报四组）

- **逐字**：5/5 块整串命中（`2-machine.json` verdict=ok；末引号形态差异见「已核实为正确」）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 5 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 0

## 已核实为正确

以下写法看似可疑，回原文核对后成立——**后续任何人不得以「读着不对」为由改动，除非能给出反证**：

- ch27 全部 5 块引语在 `text/` 内逐字命中（`2-machine.json` verdict=ok；verify_fragments_indep 352 个受检片段 MISS 0）——引语逐字层已核实成立。

## 覆盖声明

- 本章 5 块全部经 R4 逐块对应 + R5 判定，无「只有机器层」的章。
- 未审项：无。
