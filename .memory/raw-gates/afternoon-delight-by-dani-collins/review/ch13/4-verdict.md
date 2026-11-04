# ch13 · T3 判定表

- 章：ch13 chapter thirteen meg.md
- R1 素读：`1-suread.json`（审查会话独立只读 `text/`，未参考 md；5 条事实带字符区间）
- R2 机器层：`2-machine.json`（第二实现；verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 5 块，逐块 R4 + R5；**无「只有机器层」的章**

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 43 | collecting for the mob / carting the kids around / drifting apart | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 30 | trained Joel / run triage / once the crisis had passed | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 36 | breezy casualness / sexual health store / diverse customer base | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 25 | the point is to get excited / smirking mouth / I’m just a kid | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 28 | comes out as a dungeon master / tell your friends / don’t have any | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 全章 5 块引语逐字 + 分析层对应 + 施事三问 | text/ch13_chapter_thirteen_meg.txt（5 条 R1 事实锚点全部命中） | 四层（逐字/对应/形态/断言）均通过 | 通过 |

## 分组计数（只报四组）

- **逐字**：5/5 块整串命中（`2-machine.json` verdict=ok；末引号形态差异见「已核实为正确」）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 5 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 0

## 已核实为正确

以下写法看似可疑，回原文核对后成立——**后续任何人不得以「读着不对」为由改动，除非能给出反证**：

- ch13 原句 5「When your mom comes out as a dungeon master…」：md 用直引号包裹、原文为弯引号，属引号形态差异（verify_quotes 判过），不改。

## 覆盖声明

- 本章 5 块全部经 R4 逐块对应 + R5 判定，无「只有机器层」的章。
- 未审项：无。
