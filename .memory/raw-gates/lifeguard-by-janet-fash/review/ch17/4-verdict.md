# ch17 · T3 判定表

- 章：Chapter Seventeen: 2020（md：`ch17 chapter seventeen 2020.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 5 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 38 | hindsight / impunity / rampant | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 50 | Miguel / Coney Island / orgies | ✓ 命中 | ✓ | ✓ 与原文一致 | 提示 |
| 3 | 58 | Ruben Brand / Jenny Pereira / locker room | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 67 | Boris Braverman / first-year horn / hazing | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 35 | locker door / sexual harassment / doing this t | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 2 读者视角提示写「往后凡是再提到 Stein 与 Sher」——Stein 不在本块引语内 | （见左）提示型（前向引用）：Stein 在本章紧邻后文出现，事实成立 | 表面成立，措辞正当 | 提示 |
| 「2006 年被轮奸的少年救生员 Boris Braverman」 | text/ch17_chapter_seventeen_2020.txt:34：原文逐字：Several older lifeguards took turns sodomizing Braverman, Herbert wrote. | 回原文核对后成立 | 假红 |
| 「1998 年，十七岁的救生员 Jenny Pereira 告诉《纽约杂志》」 | text/ch17_chapter_seventeen_2020.txt:31：原文逐字：Jenny Pereira told New York Magazine that in 1998, when she was a seventeen-year-old lifeguard | 回原文核对后成立 | 假红 |
| 「Sher 会在救生员棚屋里办群交」 | text/ch17_chapter_seventeen_2020.txt：原文逐字：He said that back in the day, Sher would host orgies in the lifeguard shack. | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：5/5 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 1
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 5 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- **[对应]** 原句 2 读者视角提示写「往后凡是再提到 Stein 与 Sher」——Stein 不在本块引语内
  - 判定：提示型（前向引用）：Stein 在本章紧邻后文出现，事实成立

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「2006 年被轮奸的少年救生员 Boris Braverman」 | 回原文逐字核对一致 | 原文逐字：Several older lifeguards took turns sodomizing Braverman, Herbert wrote. | text/ch17_chapter_seventeen_2020.txt:34 |
| 「1998 年，十七岁的救生员 Jenny Pereira 告诉《纽约杂志》」 | 回原文逐字核对一致 | 原文逐字：Jenny Pereira told New York Magazine that in 1998, when she was a seventeen-year-old lifeguard | text/ch17_chapter_seventeen_2020.txt:31 |
| 「Sher 会在救生员棚屋里办群交」 | 回原文逐字核对一致 | 原文逐字：He said that back in the day, Sher would host orgies in the lifeguard shack. | text/ch17_chapter_seventeen_2020.txt |
