# ch01 · T3 判定表

- 章：ch01 chapter one meg.md
- R1 素读：`1-suread.json`（审查会话独立只读 `text/`，未参考 md；8 条事实带字符区间）
- R2 机器层：`2-machine.json`（第二实现；verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 12 块，逐块 R4 + R5；**无「只有机器层」的章**

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 40 | gut-crunching anxiety / loin-tingling thrill / graduation night | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 36 | twenty-one years ago / virginity / rebellion | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 55 | cells / stepping stones / Where did my life go | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 30 | shoulder season / metaphor | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 49 | I’m scared / wrong choice / what I settled for | ✓ 命中 | ✓ | ✓ 与原文一致 | 假红（末引号形态差异（md 补 `.”`、原文为 `. `）——全库通行做法（the-scarlet-ball 同类 61 处）） |
| 6 | 32 | high as a kite / wouldn’t ask for help / lose my store | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 39 | awnings / gloomy and dark / golden light | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 34 | elephantine penis / Nothing, Mother / buzzing | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 22 | bemusement / Dale is my dad / I’m Zak | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 32 | firm grip / callus / zing of electricity | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 11 | 40 | We own the building / lease / what kind of toys | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 12 | 27 | condom tree / textures and patterns / flavoured | ✓ 命中 | ✓ | ✓ 与原文一致 | 假红（短信正文被 md 加 `“…”` 包裹（原文为无引号的短信体）——全库通行（本书同类 23 处）） |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 9 的施事：中文理解写「她把三十多岁的房东儿子当成了失智老人」 | text/ch01_chapter_one_meg.txt 原文逐字：`His face moved through a comical series of expressions, landing on bemusement. “Dale is my dad. I’m Zak. Are you not Georgia?”` | 「她误认」与原文一致（Meg 先喊 Dale，Zak 纠正） | 通过 |

## 分组计数（只报四组）

- **逐字**：12/12 块整串命中（`2-machine.json` verdict=ok；末引号形态差异见「已核实为正确」）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 12 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 2

## 已核实为正确

以下写法看似可疑，回原文核对后成立——**后续任何人不得以「读着不对」为由改动，除非能给出反证**：

- ch01 原句 5「I'm scared…」的收尾引号：md 写 `settled for.”`，原文为 `settled for. `——引语在 text/ 内逐字命中，末尾引号为 md 侧的呈现差异，不改。
- ch01 原句 12「It's a condom tree…」：原文是 Georgia 的短信正文（无引号），md 用 `“…”` 包裹以符合引语块格式——内容逐字，不改。

## 覆盖声明

- 本章 12 块全部经 R4 逐块对应 + R5 判定，无「只有机器层」的章。
- 未审项：无。
