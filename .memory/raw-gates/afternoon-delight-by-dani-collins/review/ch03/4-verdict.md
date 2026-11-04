# ch03 · T3 判定表

- 章：ch03 chapter three meg.md
- R1 素读：`1-suread.json`（审查会话独立只读 `text/`，未参考 md；8 条事实带字符区间）
- R2 机器层：`2-machine.json`（第二实现；verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 10 块，逐块 R4 + R5；**无「只有机器层」的章**

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 41 | behemoths / desperate need of TLC / Like me | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 42 | handyman / every small job / warped panel | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 72 | stonewalling / obstinate belief / distressing ability | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 71 | Maybe next time / no silver lining to sexism / passed over | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 33 | happiest day / certified paperwork / unpaid personal assistant | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 37 | on her own terms / live my life / only for a few weeks | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 36 | announcements / tore that bandage right off / quitting my job | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 36 | froze / tightened on the edge / looked down her nose | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 60 | scared to do anything else / pushing me into marrying / whole heart | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 29 | open-minded / pathologically responsible / so I will help her | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 全章 10 块引语逐字 + 分析层对应 + 施事三问 | text/ch03_chapter_three_meg.txt（8 条 R1 事实锚点全部命中） | 四层（逐字/对应/形态/断言）均通过 | 通过 |

## 分组计数（只报四组）

- **逐字**：10/10 块整串命中（`2-machine.json` verdict=ok；末引号形态差异见「已核实为正确」）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 10 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 0

## 已核实为正确

以下写法看似可疑，回原文核对后成立——**后续任何人不得以「读着不对」为由改动，除非能给出反证**：

- ch03 原句 9 的 md 用直引号 `I'm` 而原文为弯引号 `I’m`——verify_quotes 按弯直不算差异判过，属词形级假红，不改。

## 覆盖声明

- 本章 10 块全部经 R4 逐块对应 + R5 判定，无「只有机器层」的章。
- 未审项：无。
