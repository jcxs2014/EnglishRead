# ch05 · T3 判定表

- 章：Chapter Five: 1985（md：`ch05 chapter five 1985.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 15 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 46 | citywide lifeguard coordinator / gym teacher / | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 41 | wherewithal / token female / appearances | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 50 | somewhat as a fluke / strong women / right pla | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 58 | barge / rip current / collapsing a sandbar | ✓ 命中 | ✓ | ✓ 与原文一致 | 提示 |
| 5 | 57 | out-of-control / clean up the beach’s image /  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 55 | manage three dozen guards / miffed / rogue lif | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 50 | player coach / social club / didn’t train | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 40 | a woman was in charge / female lieutenants / a | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 41 | average lifeguard / twenty to forty seconds /  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 48 | fell to the ground / dehydration / logbook | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 11 | 40 | save people on land / bandage / dislocated sho | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 12 | 37 | chest puffed up / antagonistic / erupted | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 13 | 35 | HIV positive / AIDS crisis / confided in us | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 14 | 42 | off-duty cop / precinct / walk miles | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 15 | 34 | oil paint / toxic / smothered her overnight | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 4 读者视角提示写「等后面 Stein 把他们调走时」——Stein 不在本块引语内 | （见左）提示型（前向引用）：该层职能即预告后文，且 Stein 在本章原句 5 就出现，事实成立 | 表面成立，措辞正当 | 提示 |
| 「Stein 更在乎这帮人『看起来』如何，而不是他们『做了什么』」 | text/ch05_chapter_five_1985.txt:44：原文逐字：he was trying to clean up the beach’s image. He cared more about how the guys looked than what they did. | 回原文核对后成立 | 假红 |
| 「罗克韦仅有的两名女性中尉之一」 | text/ch05_chapter_five_1985.txt:56：原文逐字：I was one of only two female lieutenants on the whole beach | 回原文核对后成立 | 假红 |
| 「三十六名救生员」 | text/ch05_chapter_five_1985.txt：原文逐字：I basically had to figure out how to manage three dozen guards alone. | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：15/15 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 1
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 15 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- **[对应]** 原句 4 读者视角提示写「等后面 Stein 把他们调走时」——Stein 不在本块引语内
  - 判定：提示型（前向引用）：该层职能即预告后文，且 Stein 在本章原句 5 就出现，事实成立

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「Stein 更在乎这帮人『看起来』如何，而不是他们『做了什么』」 | 回原文逐字核对一致 | 原文逐字：he was trying to clean up the beach’s image. He cared more about how the guys looked than what they did. | text/ch05_chapter_five_1985.txt:44 |
| 「罗克韦仅有的两名女性中尉之一」 | 回原文逐字核对一致 | 原文逐字：I was one of only two female lieutenants on the whole beach | text/ch05_chapter_five_1985.txt:56 |
| 「三十六名救生员」 | 回原文逐字核对一致 | 原文逐字：I basically had to figure out how to manage three dozen guards alone. | text/ch05_chapter_five_1985.txt |
