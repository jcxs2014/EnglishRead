# ch04 · T3 判定表

- 章：Chapter Four: 1983（md：`ch04 chapter four 1983.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 9 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 58 | senior guard / 106th Street shack / naked phot | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 62 | horn / scan the water / senior guard | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 49 | high school friend / firefighter / bouncer | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 55 | women being strong or athletic / supportive /  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 43 | backpacking / commodity trading job / My mothe | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 31 | Enough is enough / Come home and start your li | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 54 | waved me off / inevitably return / not allowed | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 37 | Mercedes-Benz / hit on me / repulsive | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 54 | out of a job / make more money / signed up for | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「Bob 是 Brian 的高中同学，既当消防员，也在酒吧做保镖」 | text/ch04_chapter_four_1983.txt:25：原文逐字：Bob was a high school friend of Brian’s who worked as a firefighter and as a bouncer at Fitzgerald’s. | 回原文核对后成立 | 假红 |
| 「后来她成了酒吧的『Brass Balls Club』铜牌会员」（原文用词） | text/ch04_chapter_four_1983.txt：原文逐字：the Brass Balls Club | 回原文核对后成立 | 假红 |
| 「母亲的信末：够了，回来做你的救生员工作」 | text/ch04_chapter_four_1983.txt：原文逐字：“Enough is enough,” she wrote. “Come home and start your lifeguarding job.” | 回原文核对后成立 | 假红 |

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
| 「Bob 是 Brian 的高中同学，既当消防员，也在酒吧做保镖」 | 回原文逐字核对一致 | 原文逐字：Bob was a high school friend of Brian’s who worked as a firefighter and as a bouncer at Fitzgerald’s. | text/ch04_chapter_four_1983.txt:25 |
| 「后来她成了酒吧的『Brass Balls Club』铜牌会员」（原文用词） | 回原文逐字核对一致 | 原文逐字：the Brass Balls Club | text/ch04_chapter_four_1983.txt |
| 「母亲的信末：够了，回来做你的救生员工作」 | 回原文逐字核对一致 | 原文逐字：“Enough is enough,” she wrote. “Come home and start your lifeguarding job.” | text/ch04_chapter_four_1983.txt |
