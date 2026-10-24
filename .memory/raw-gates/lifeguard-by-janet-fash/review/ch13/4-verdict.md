# ch13 · T3 判定表

- 章：Chapter Thirteen: 2007（md：`ch13 chapter thirteen 2007.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 13 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 40 | mismanagement / sent those kids packing / brea | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 49 | Broad Channel / granddaughter had been failed  | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 45 | former chief lifeguard / change the system / C | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 34 | ten steps ahead / public enemy number one / ta | ✓ 命中 | ✓ | ✓ 与原文一致 | 已修·阻断 |
| 5 | 55 | around thirty-five people / cut it down to six | ✓ 命中 | ✓ | ✓ 与原文一致 | 已修·阻断 |
| 6 | 48 | crosshairs / official channels / documenting e | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 54 | broke down crying / bullied her / rip currents | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 36 | my shack / gave my lifeguards a choice / a maf | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 37 | didn’t give me new lifeguards / twelve lifegua | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 38 | community meeting / do a better job / my big m | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 11 | 45 | New York Daily News / Stein’s fiefdom / Lifegu | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 12 | 60 | gold teeth / Stein and Sher’s bodyguard / stuc | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 13 | 46 | As Rockaway chiefs / borough coordinators / ev | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 4 中文理解写「那年夏天，Stein 用抽走她手下救生员的方式惩罚她」，本块引语只说 “he”，施事未在块内点名 | text/ch13_chapter_thirteen_2007.txt:  原文紧邻前句逐字：But while I was starting the battle, Stein was already ten steps ahead of me in the | §0.2 阻断（人名不在本块引语） | 阻断 |
| 「十二名救生员守十个街区」 | text/ch13_chapter_thirteen_2007.txt:40：原文逐字：Now I had twelve lifeguards covering ten blocks of beach, which was the lowest amount I’d ever had. | 回原文核对后成立 | 假红 |
| 「原句 5：他们面对的是一伙黑手党」 | text/ch13_chapter_thirteen_2007.txt：原文逐字：I wanted to be realistic about the situation… we were dealing with a mafia | 回原文核对后成立 | 假红 |
| 「《纽约每日新闻》专栏作者 Denis Hamill——两人从小就住同一栋楼」 | text/ch13_chapter_thirteen_2007.txt：原文逐字：Denis Hamill, a columnist at the New York Daily News, who I knew because he lived in the same building | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：13/13 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 1，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 13 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- **[对应]** 原句 4 中文理解写「那年夏天，Stein 用抽走她手下救生员的方式惩罚她」，本块引语只说 “he”，施事未在块内点名
  - 判据：§0.2 阻断（人名不在本块引语）
  - 证据：text/ch13_chapter_thirteen_2007.txt:  原文紧邻前句逐字：But while I was starting the battle, Stein was already ten steps ahead of me in the war.；后句：After the lifeguard development program, I was now his public enemy number one.
  - 处理：已修：拆成两块（原句 4 = “Stein was already ten steps ahead…taking away my lifeguards.” 39 词含 Stein；新增原句 5 = “I normally had around thirty-five people…incredibly difficult.” 36 词），块号顺移至 1–13

## 提示（只记不改）

- （无）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「十二名救生员守十个街区」 | 回原文逐字核对一致 | 原文逐字：Now I had twelve lifeguards covering ten blocks of beach, which was the lowest amount I’d ever had. | text/ch13_chapter_thirteen_2007.txt:40 |
| 「原句 5：他们面对的是一伙黑手党」 | 回原文逐字核对一致 | 原文逐字：I wanted to be realistic about the situation… we were dealing with a mafia | text/ch13_chapter_thirteen_2007.txt |
| 「《纽约每日新闻》专栏作者 Denis Hamill——两人从小就住同一栋楼」 | 回原文逐字核对一致 | 原文逐字：Denis Hamill, a columnist at the New York Daily News, who I knew because he lived in the same building | text/ch13_chapter_thirteen_2007.txt |
