# ch09 · T3 判定表

- 章：Chapter Nine: 1991（md：`ch09 chapter nine 1991.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 12 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 37 | lifeguard’s lifeguard / infectious / easy conf | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 51 | irked / permission / standard piece of equipme | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 33 | drowning / report / standard piece of equipmen | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 37 | negotiating / off the ground / fifty-five wome | ✓ 命中 | ✓ | ✓ 与原文一致 | 提示 |
| 5 | 52 | rigging the competition / cinder blocks / wher | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 49 | Ram’s Horn / job action / challenge Stein’s me | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 46 | there was a rat / told Stein about Joe’s plan  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 65 | passenger vans / sixty-three pools / organizat | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 43 | create them on the spot / anonymous / 100 to 8 | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 32 | contested the disciplinary charges / four year | ✓ 命中 | ✓ | ✓ 与原文一致 | 已修·阻断 |
| 11 | 66 | union contract / eligible bargaining unit posi | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 12 | 45 | Saint Patrick’s Day parade / part of the solut | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| R1 转折点「Joe 背四十多项不实指控被解雇、仲裁四年才讨回清白」只出现在导航层，引语层无对应块——块序/原文顺序上这块位于工会合同块之前 | text/ch09_chapter_nine_1991.txt:  原文逐字：Joe contested the disciplinary charges. He went through four years of arbitration with the  | R3 漏＝阻断（关键转折未在引语层出现） | 阻断 |
| 原句 4 读者视角提示写「后来 Joe 带这只队伍时」——Joe 不在本块引语内 | （见左）提示型（前向引用）：Joe 在本章原句 1 即出现，事实成立 | 表面成立，措辞正当 | 提示 |
| 「1984 年从 Riis Park 转入市队」 | text/ch09_chapter_nine_1991.txt:19：原文逐字：Joe moved over from Riis Park to the city’s lifeguard corps in 1984 | 回原文核对后成立 | 假红 |
| 「四十多项不实指控」 | text/ch09_chapter_nine_1991.txt:100：原文逐字：Joe got brought up on trumped-up disciplinary charges—over forty in total | 回原文核对后成立 | 假红 |
| 「最后离开纽约去了佛罗里达」 | text/ch09_chapter_nine_1991.txt:109：原文逐字：Joe left New York City altogether and went to Florida | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：12/12 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 1
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 12 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- **[漏]** R1 转折点「Joe 背四十多项不实指控被解雇、仲裁四年才讨回清白」只出现在导航层，引语层无对应块——块序/原文顺序上这块位于工会合同块之前
  - 判据：R3 漏＝阻断（关键转折未在引语层出现）
  - 证据：text/ch09_chapter_nine_1991.txt:  原文逐字：Joe contested the disciplinary charges. He went through four years of arbitration with the city and Stein. During those years, every charge eventually got dismissed because the city couldn’t provide any proof.
  - 处理：已修：新增第 10 块（40 词，含 Stein），后续块号顺移为 11–12

## 提示（只记不改）

- **[对应]** 原句 4 读者视角提示写「后来 Joe 带这只队伍时」——Joe 不在本块引语内
  - 判定：提示型（前向引用）：Joe 在本章原句 1 即出现，事实成立

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「1984 年从 Riis Park 转入市队」 | 回原文逐字核对一致 | 原文逐字：Joe moved over from Riis Park to the city’s lifeguard corps in 1984 | text/ch09_chapter_nine_1991.txt:19 |
| 「四十多项不实指控」 | 回原文逐字核对一致 | 原文逐字：Joe got brought up on trumped-up disciplinary charges—over forty in total | text/ch09_chapter_nine_1991.txt:100 |
| 「最后离开纽约去了佛罗里达」 | 回原文逐字核对一致 | 原文逐字：Joe left New York City altogether and went to Florida | text/ch09_chapter_nine_1991.txt:109 |
