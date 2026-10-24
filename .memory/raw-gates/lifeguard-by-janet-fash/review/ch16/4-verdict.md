# ch16 · T3 判定表

- 章：Chapter Sixteen: 2018（md：`ch16 chapter sixteen 2018.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 6 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 48 | physical toll / adds up / hot sun | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 40 | bursitis / inflammation / act up | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 40 | dermatologist / routine visit / skin cancer | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 71 | union / dermatological services / full-time | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 56 | slowed down / chased after / as fast as I used | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 64 | constant / ageless / porpoise | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 4 为 71 词，超 30–70 词软上限 1 词 | （见左）提示型，不改：chapter.sh 只在 >100 词判 ⚠️；库内既成书 40 本 7375 块中 >70 词者占 6.0%（P99=112），本书 1/193=0.5%，不属离群 | 表面成立，措辞正当 | 提示 |
| 「一千名救生员里只有约九十名全职的才有覆盖」 | text/ch16_chapter_sixteen_2018.txt:31：原文逐字：Only full-time lifeguards—around ninety out of a thousand—are covered. | 回原文核对后成立 | 假红 |
| 「2018 年做例行皮肤科检查，查出皮肤癌」 | text/ch16_chapter_sixteen_2018.txt：原文逐字：In 2018 I went to the dermatologist for a routine visit. | 回原文核对后成立 | 假红 |
| 「大学时因游泳落下的肩部滑囊炎——关节发炎」 | text/ch16_chapter_sixteen_2018.txt：原文逐字：In college I got bursitis—an inflammation of the shoulder joint | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：6/6 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 6 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- **[形态]** 原句 4 为 71 词，超 30–70 词软上限 1 词
  - 判定：提示型，不改：chapter.sh 只在 >100 词判 ⚠️；库内既成书 40 本 7375 块中 >70 词者占 6.0%（P99=112），本书 1/193=0.5%，不属离群

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「一千名救生员里只有约九十名全职的才有覆盖」 | 回原文逐字核对一致 | 原文逐字：Only full-time lifeguards—around ninety out of a thousand—are covered. | text/ch16_chapter_sixteen_2018.txt:31 |
| 「2018 年做例行皮肤科检查，查出皮肤癌」 | 回原文逐字核对一致 | 原文逐字：In 2018 I went to the dermatologist for a routine visit. | text/ch16_chapter_sixteen_2018.txt |
| 「大学时因游泳落下的肩部滑囊炎——关节发炎」 | 回原文逐字核对一致 | 原文逐字：In college I got bursitis—an inflammation of the shoulder joint | text/ch16_chapter_sixteen_2018.txt |
