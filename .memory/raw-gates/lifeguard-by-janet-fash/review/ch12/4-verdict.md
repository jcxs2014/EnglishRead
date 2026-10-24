# ch12 · T3 判定表

- 章：Chapter Twelve: 2004（md：`ch12 chapter twelve 2004.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 9 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 53 | twenty-five years / butted heads / chief | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 56 | boardwalk / call the lifeguards off / furious | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 59 | acting lieutenant / fallen out / seniority | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 34 | worrying about / next season / dismiss | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 55 | chest-deep / could barely swim / ripped them a | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 59 | preventable / beyond the job / teaching kids h | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 39 | distributed to thirty-eight schools / 112,000  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 66 | first batch of kids / a pretest / thirty-five  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 47 | took their test separately / didn’t make the c | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「水安全片分送到三十八所学校、放给 112,000 名学生看」 | text/ch12_chapter_twelve_2004.txt:92：原文逐字：The video was distributed to thirty-eight schools and was screened for 112,000 students. | 回原文核对后成立 | 假红 |
| 「二十个学生里有十九个被判不及格」 | text/ch12_chapter_twelve_2004.txt:117：原文逐字：nineteen out of twenty of our students were failed. | 回原文核对后成立 | 假红 |
| 「先做一次摸底测试（pretest）」 | text/ch12_chapter_twelve_2004.txt:111：原文逐字：high schoolers ranging from sixteen to eighteen years old, and gave them a pretest…which was the fifty-ya | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：9/9 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 9 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- （无）

## 提示（只记不改）

- （无）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「水安全片分送到三十八所学校、放给 112,000 名学生看」 | 回原文逐字核对一致 | 原文逐字：The video was distributed to thirty-eight schools and was screened for 112,000 students. | text/ch12_chapter_twelve_2004.txt:92 |
| 「二十个学生里有十九个被判不及格」 | 回原文逐字核对一致 | 原文逐字：nineteen out of twenty of our students were failed. | text/ch12_chapter_twelve_2004.txt:117 |
| 「先做一次摸底测试（pretest）」 | 回原文逐字核对一致 | 原文逐字：high schoolers ranging from sixteen to eighteen years old, and gave them a pretest…which was the fifty-yard entry time to get into the New York City lifeguard school. | text/ch12_chapter_twelve_2004.txt:111 |
