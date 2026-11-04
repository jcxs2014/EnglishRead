# ch02 · T3 判定表

- 章：ch02 chapter two zak.md
- R1 素读：`1-suread.json`（审查会话独立只读 `text/`，未参考 md；8 条事实带字符区间）
- R2 机器层：`2-machine.json`（第二实现；verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 5 块，逐块 R4 + R5；**无「只有机器层」的章**

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 51 | cry of pain / workroom / clutching his own hand | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 43 | my Google / heat gun / hair dryer | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 22 | fucked with them / Literally / vibrator | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 36 | good to have you home / company / catching a ball | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过（md 引语起点省去同话轮首句 “Let’s do that.”——提示级（分析层未涉及被省内容），不作阻断） |
| 5 | 32 | bandage / puzzlement / He was not okay | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 4 施事：中文理解写「Dale 说：有你回家真好」 | text/ch02_chapter_two_zak.txt 原文逐字：`“Let’s do that. It’s good to have you home, Zak. I like the company.” He gave my shoulder a pat...` | 说话人是 Dale（「It’s good to have you home, Zak」中的 Zak 是被称呼者） | 通过 |
| 原句 5 的「他不是他父亲」判断：中文理解写「Zak 心沉，判定『He was not okay』」 | text/ch02_chapter_two_zak.txt 原文逐字：`But then he noticed the bandage on his hand and began to pick at it with puzzlement... My heart sank. He was not okay.` | 与原文一致 | 通过 |

## 分组计数（只报四组）

- **逐字**：5/5 块整串命中（`2-machine.json` verdict=ok；末引号形态差异见「已核实为正确」）
- **对应**：阻断 0，提示 1
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 5 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 1

## 已核实为正确

以下写法看似可疑，回原文核对后成立——**后续任何人不得以「读着不对」为由改动，除非能给出反证**：

- ch02 原句 4 的引语起点：`“It’s good to have you home, Zak. I like the company.”` 与原文完全一致（同一话轮内）；`“Let’s do that.”` 是同话轮的前置回应句，未被分析层引用。

## 覆盖声明

- 本章 5 块全部经 R4 逐块对应 + R5 判定，无「只有机器层」的章。
- 未审项：无。
