# ch02 · T3 判定表

- 章：Chapter Two: 1980（md：`ch02 chapter two 1980.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 13 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 45 | subway / strike / bicycle | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 40 | full-time / recruited / opposite | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 37 | rugby / assignment / Rockaway | ✓ 命中 | ✓ | ✓ 与原文一致 | 已修·阻断 |
| 4 | 42 | horns / locals / isolating | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 67 | punishment / partner / dangerous | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 57 | fluster / determined / showing that off | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 7 | 66 | volunteer / porpoising / wave | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 33 | panicked / drown / barnacles | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 62 | buoy / Styrofoam / no-no | ✓ 命中 | ✓ | ✓ 与原文一致 | 已修·阻断 |
| 10 | 55 | blamed / save face / consolation prize | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 11 | 42 | beer / street sign / yelled | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 12 | 41 | deserved / angelic / punch | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 13 | 36 | favorite / vacationers / quiet | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 3 中文理解写「她想 Helen 既然爱游泳」，本块引语只说 “she”，人名不在本块引语内 | text/ch02_chapter_two_1980.txt:  引语「It wasn’t until we started playing rugby…Just like Barbara taught me, I told her to choose Roc | §0.2 阻断 | 阻断 |
| 原句 9 中文理解写「Freddie 站在回岗亭的路上」，本块引语从 “He noticed neither of us…” 起，Fredd | text/ch02_chapter_two_1980.txt:  原文「As we were walking back to the shack, Freddie, the borough coordinator, was standing there.」紧邻 | §0.2 阻断 | 阻断 |
| 「小她四岁的妹妹」 | text/ch02_chapter_two_1980.txt：原文逐字：Helen is four years younger than me, and the opposite of me in many ways. | 回原文核对后成立 | 假红 |
| 「Timlin 是她的娘家姓」 | text/ch02_chapter_two_1980.txt：原文逐字：(Timlin is my maiden name.) | 回原文核对后成立 | 假红 |
| 「打中尉的根本不是她，是 Helen」 | text/ch02_chapter_two_1980.txt：原文逐字：The bartender who saw the whole thing didn’t throw me out because he said the guy had deserved it. But wi | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：13/13 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 2，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 13 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- **[对应]** 原句 3 中文理解写「她想 Helen 既然爱游泳」，本块引语只说 “she”，人名不在本块引语内
  - 判据：§0.2 阻断
  - 证据：text/ch02_chapter_two_1980.txt:  引语「It wasn’t until we started playing rugby…Just like Barbara taught me, I told her to choose Rockaway as her assignment.」
  - 处理：已修：中文理解「Helen」→「对方」；为什么这样写「我教妹妹」→「我让她去选」
- **[对应]** 原句 9 中文理解写「Freddie 站在回岗亭的路上」，本块引语从 “He noticed neither of us…” 起，Freddie 不在块内
  - 判据：§0.2 阻断
  - 证据：text/ch02_chapter_two_1980.txt:  原文「As we were walking back to the shack, Freddie, the borough coordinator, was standing there.」紧邻本块引语之前
  - 处理：已修：引语向前扩一句（47→64 词，仍在 30–70 词内，且仍是原文连续一段）

## 提示（只记不改）

- （无）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「小她四岁的妹妹」 | 回原文逐字核对一致 | 原文逐字：Helen is four years younger than me, and the opposite of me in many ways. | text/ch02_chapter_two_1980.txt |
| 「Timlin 是她的娘家姓」 | 回原文逐字核对一致 | 原文逐字：(Timlin is my maiden name.) | text/ch02_chapter_two_1980.txt |
| 「打中尉的根本不是她，是 Helen」 | 回原文逐字核对一致 | 原文逐字：The bartender who saw the whole thing didn’t throw me out because he said the guy had deserved it. But with our… | text/ch02_chapter_two_1980.txt |
