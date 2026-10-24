# ch01 · T3 判定表

- 章：Chapter One: 1974（md：`ch01 chapter one 1974.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 15 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 41 | ultimatum / Park Slope / rule | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 52 | Peter / Barbara / stripping | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 44 | greenhorn / horns / senior lifeguards | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 39 | Catholic / lifeguard / beach | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 51 | sponsored / immigration / mentally | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 6 | 31 | shore breaker / slammed / shoulder | ✓ 命中 | ✓ | ✓ 与原文一致 | 提示 |
| 7 | 43 | brownstone / police officer / Detective Sweene | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 8 | 42 | camaraderie / intoxicating / craziest parties | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 9 | 44 | tube top / sandal / phone booth | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 10 | 38 | stood your ground / backed off / sandals | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 11 | 39 | Barbara / teamwork / agreed | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 12 | 42 | Barbara / porpoising / technique | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 13 | 53 | case / whistle / bumping the chairs | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 14 | 47 | lunged / buoy / experienced lifeguard | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 15 | 46 | the public / mundane / extraordinary | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 3 中文理解把「Helen」写进分析层，而该块引语只说 “she”，人名不在本块引语内 | text/ch01_chapter_one_1974.txt:  引语「It wasn’t until we started playing rugby…Just like Barbara taught me, I told her to choose Roc | §0.2 阻断：分析里出现的每个人名/动作/关系，都必须在这段引语里 | 阻断 |
| 中文理解写「在 Sandy Hook，表姐 Patricia…」——Sandy Hook 不在本块引语内 | text/ch01_chapter_one_1974.txt:  「…there were two beaches there: the bay…; and Sandy Hook, just over the bridge, where the waves w | 提示型（地点类，非人名/动作/关系；本章原文确有该地点） | 阻断 |
| 原句 3/原句 5 等块的「读者视角提示」写「后面那些……」「前面那些」等章内相对指认 | （见左）提示层职能即引导读者章内前后对照；R4 第二层扫描全书 20 条相对指认，逐条核过，全部指向同章相邻块，无一条讲引语之外的上下文 | 表面成立，措辞正当 | 提示 |
| 「表姐 Patricia 斜着冲进浪里……冲击力把她的肩膀撞断了」 | text/ch01_chapter_one_1974.txt：原文逐字：My cousin Patricia rode a shore breaker in and I could tell she was on it wrong. She slammed into the san | 回原文核对后成立 | 假红 |
| 「母亲那天也在沙滩上……凭你这样，永远别想当救生员」 | text/ch01_chapter_one_1974.txt:28：原文逐字：“Jesus, Mary, and Joseph,” she said. “You’ll never be a lifeguard.” | 回原文核对后成立 | 假红 |
| 「四年后 Barbara 问她要不要一起当救生员」 | text/ch01_chapter_one_1974.txt:86,89：原文逐字：Four years after the summer we spent together, I ran into her…It was Barbara, again, who pulled me in. /  | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：15/15 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 2，提示 1
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 15 在本书众数区间、编号连续无撞车）
- **断言**：阻断 1，提示 0，假红 3

## 阻断

- **[对应]** 原句 3 中文理解把「Helen」写进分析层，而该块引语只说 “she”，人名不在本块引语内
  - 判据：§0.2 阻断：分析里出现的每个人名/动作/关系，都必须在这段引语里
  - 证据：text/ch01_chapter_one_1974.txt:  引语「It wasn’t until we started playing rugby…Just like Barbara taught me, I told her to choose Rockaway as her assignment.」内无 Helen
  - 处理：已修：中文理解改用「对方」，「我教妹妹」改「我让她去选」
- **[断言]** 中文理解写「在 Sandy Hook，表姐 Patricia…」——Sandy Hook 不在本块引语内
  - 判据：提示型（地点类，非人名/动作/关系；本章原文确有该地点）
  - 证据：text/ch01_chapter_one_1974.txt:  「…there were two beaches there: the bay…; and Sandy Hook, just over the bridge, where the waves were.」（距本块引语约 400 字符）
  - 处理：只记不改

## 提示（只记不改）

- **[对应]** 原句 3/原句 5 等块的「读者视角提示」写「后面那些……」「前面那些」等章内相对指认
  - 判定：提示层职能即引导读者章内前后对照；R4 第二层扫描全书 20 条相对指认，逐条核过，全部指向同章相邻块，无一条讲引语之外的上下文

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「表姐 Patricia 斜着冲进浪里……冲击力把她的肩膀撞断了」 | 回原文逐字核对一致 | 原文逐字：My cousin Patricia rode a shore breaker in and I could tell she was on it wrong. She slammed into the sand under the water, and the force broke her shoulder. | text/ch01_chapter_one_1974.txt |
| 「母亲那天也在沙滩上……凭你这样，永远别想当救生员」 | 回原文逐字核对一致 | 原文逐字：“Jesus, Mary, and Joseph,” she said. “You’ll never be a lifeguard.” | text/ch01_chapter_one_1974.txt:28 |
| 「四年后 Barbara 问她要不要一起当救生员」 | 回原文逐字核对一致 | 原文逐字：Four years after the summer we spent together, I ran into her…It was Barbara, again, who pulled me in. / I was the ripe old age of nineteen when I first signed up | text/ch01_chapter_one_1974.txt:86,89 |
