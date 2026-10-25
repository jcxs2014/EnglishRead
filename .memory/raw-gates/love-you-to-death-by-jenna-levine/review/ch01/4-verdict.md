# ch01 · T3 判定表

- 章：Prologue（md：`ch01 the white room.md`；原文 `text/ch01_prologue.txt`）
- R1 素读：`1-suread.json`（**独立代理**，只读 `text/`，禁开任何 md；8 条事实 + 转折点，锚点逐条唯一核过）
- R2 机器层：`2-machine.json`（第二实现，verdict=ok；10 块 / 18 片段查无 0）
- R3 对账：`3-diff.md`
- 覆盖：**全章 10 块逐块 R4 + R5**；无「只有机器层」的块

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 44 | featureless / eternal damnation | ✓ 命中 | ✓ | ✓ 他的抱怨 | 通过 |
| 2 | 72 | bowler hat / vaguely recognize | ✓ 命中 | ✓ | ✓ 政客踱步 | 通过（读者指引另见 R5 阻断 1） |
| 3 | 44 | formless time / Heaven and Hell | ✓ 命中 | ✓ | ✓ 他答政客 | 通过 |
| 4 | 67 | whose name I know from the papers | ✓ 命中 | ✓ | ✓ 杀人犯的话 | 通过 |
| 5 | 73 | None taken / refused to introduce herself | ✓ 命中 | ✓ | ✓ 女人「无所谓」 | 通过 |
| 6 | 48 | appears out of nowhere | ✓ 命中 | ✓ | ✓ 灰袍人现身 | 通过 |
| 7 | 54 | the Powers That Be | ✓ 命中 | ✓ | ✓ 「你们被邀请」 | 通过 |
| 8 | 78 | short-staffed / skip all that Hell nastiness | ✓ 命中 | ✓ | ✓ 「雇佣」条款 | 通过 |
| 9 | 50 | do what, exactly? / impertinent | ✓ 命中 | ✓ | ✓ 他问「我」 | 通过（断言另见提示 1） |
| 10 | 44 | immediately sign / a moment's hesitation | ✓ 命中 | ✓ | ✓ 三人立刻签、他犹豫一瞬 | 通过（读者指引另见 R5 阻断 2） |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 2 读者视角提示：政客「第一句话只说『我们』」，稍后改口「the four of us」 | `text/ch01_prologue.txt:31`："Why keep the three of us waiting?"；`:37`："Why keep the four of us waiting?" the politician amends. | 与原文不符：改口的前一态是「the **three** of us」；「three」＝把不报姓名的女人排除在外，随后的「No offense, ma’am」正是为此 | **阻断** |
| 原句 10 读者视角提示引「他后来那句『我几乎为自己做的事感到庆幸』」 | `/usr/bin/grep -rn "grateful" text/ch*.txt` → 8 处命中，**无此句**（退出码 0）；`/usr/bin/grep -rniE "for what i'?ve? done" text/ch*.txt` → **零命中（退出码 1）**；语义最近处 `text/ch24_chapter_twenty_three.txt:127`："I was almost glad to do what I do." | 引语指认不实：原句是「几乎为自己**正在做的差事**感到高兴」，且未给章号 | **阻断** |
| 原句 9「为什么这样写」称本段是「**全书第一个**真正尖锐的问题」 | 本章是全书首章（`text/ch01_prologue.txt:13` 时间标记「135 Years Ago」）；此前只有政客「Why keep the three of us waiting?」这类抱怨与假设句，限定语「真正尖锐」承担了区分 | 成立（自指表述，限定语承担区分） | 提示（已核实为正确） |
| 原句 3「为什么这样写」：后来的 Agency 空间「没有窗户没有钟」 | `text/ch08_chapter_seven.txt:13` 逐字："There's no way to mark the passage of time here. There's no window I can look out of and no clock." | 成立 | 提示（已核实为正确） |
| 原句 5 读者视角提示：「她的身份原文从头到尾没有交代」 | `text/ch33_chapter_thirty_two.txt:16` 逐字："…the bedraggled woman whose former name I never managed to learn…"（全书最后仍不知其名） | 成立 | 提示（已核实为正确） |
| 导航「时间标记『135 Years Ago』直接前置」 | `text/ch01_prologue.txt:13` 逐字："135 Years Ago" | 成立 | 提示（已核实为正确） |
| 原句 10 读者视角提示：「读到后面 Executive Suite、Inhuman Resources 这些地方时」 | 两处地名分别在 `text/ch26/ch29`（Executive Suite）与 `text/ch18/ch19`（Inhuman Resources） | 成立（前向指引，读者可定位） | 提示 |

## 分组计数（只报四组）

- **逐字**：10/10 块整串命中，查无 0（`2-machine.json` verdict=ok；18 片段逐条回查，segment_miss=0）
- **对应**：阻断 0，提示 0（10 块的中文均在讲本块引语；施事/受事逐块核过，无反转）
- **形态**：阻断 0（H1 `01. Prologue` 合本书形态 · 导航 5 项 · 4 子项齐备 · 10 块在本书众数区间 3–12 内 · 编号连续无撞车）
- **断言**：阻断 2，提示 5，未核 0

## 阻断

- **[断言]** 原句 2 读者视角提示：改口的前一态写成裸「我们」
  - 判据：读者指引必须与原文一致；此处漏掉的「the three of us」正是作者埋的 tell
  - 证据：`text/ch01_prologue.txt:31`："Why keep the three of us waiting?"；`:37`："Why keep the four of us waiting?"
  - 处理：已改为「留意房间里是四个人，但政客先说的是「the three of us」；等他改口成「the four of us」……」
- **[断言]** 原句 10 读者视角提示：引用的「我几乎为自己做的事感到庆幸」全书无此句，且无章号
  - 判据：R5 硬约束（无原文逐字不得作跨章引用）；R5-补（零命中须贴命令与退出码）
  - 证据：`grep -rn "grateful" text/ch*.txt` → 8 处命中无此义（退出码 0）；`grep -rniE "for what i'?ve? done" text/ch*.txt` → 零命中（退出码 1）；最近处 `text/ch24_chapter_twenty_three.txt:127`："I was almost glad to do what I do."
  - 处理：已改为「他后来（ch24）那句「我几乎为自己这份差事感到高兴」」

## 提示（只记不改）

- **[断言]** 原句 9「全书第一个真正尖锐的问题」——自指表述且限定语承担区分，成立
- **[断言]** 原句 3「Agency 那种没有窗户没有钟的空间」——`text/ch08:13` 逐字一致
- **[断言]** 原句 5「她的身份从头到尾没有交代」——`text/ch33:16` 明说没学到她的原名
- **[断言]** 导航「时间标记『135 Years Ago』」——`text/ch01:13` 逐字一致
- **[断言]** 原句 10「读到后面 Executive Suite、Inhuman Resources 这些地方」——两地名后文均在场

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 原句 5 读者视角提示：「她的身份原文从头到尾没有交代」 | 序章那位不报姓名的女人，到全书最后一章仍不知原名 | "…the bedraggled woman whose former name I never managed to learn…" | `text/ch33_chapter_twenty_two.txt`（实为 `text/ch33_chapter_thirty_two.txt`）:16 |
| 原句 3「Agency 那种没有窗户没有钟的空间」 | ch08 的 HR 候诊区逐字就是「没有窗户、没有钟」 | "There's no window I can look out of and no clock." | `text/ch08_chapter_seven.txt`:13 |
| 原句 1 读者视角提示：「叙述者对『永劫』一词的熟稔」 | 原句本身用 "eternal damnation" 这个书面词 | "…it more than makes up for in lack of obvious eternal damnation." | `text/ch01_prologue.txt` |
| 原句 2「为什么这样写」：「vaguely recognize 暗示他曾是个有头脸的人物」 | 原文是 "a politician I vaguely recognize by name"——认得**名字**才成立 | "he introduced himself as a politician I vaguely recognize by name" | `text/ch01_prologue.txt` |
