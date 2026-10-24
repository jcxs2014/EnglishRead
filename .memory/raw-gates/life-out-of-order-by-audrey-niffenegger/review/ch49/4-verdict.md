# ch49 First Kiss — R5 判定

- 机器层：`bash scripts/chapter.sh "ch49 first kiss.md" --json` → rc=0，verdict `ok`
- 块数：3（原文 430 词 < 800 ⇒ 短章下限 3，**恰达下限**；本书 71 章中位 6）
- 原文 430 词 / 精读 81 行（六章中唯一 Oliver 第一人称现在时）

## 一、判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 三块引语逐字 | 与 `text/ch49_first_kiss.txt` L23/L66/L93 逐字对齐，3/3 命中 | 真 | 跳过 |
| 抬头与年龄 | `text/ch49_first_kiss.txt:18` `Sunday, November 22, 1998 (Alba is 40, Oliver is 17)` | md 写「她的四十岁生日」，与原文一致 | 跳过 |
| 「丈夫扎克正瞒着她筹办惊喜派对」 | `:23` `Her husband Zach is preparing a surprise party for her because she is turning forty.` | 一致 | 跳过 |
| 「她早已从奥利弗口中得知」 | `:48` `“You told me about it.”` | 一致（派对泄底） | 跳过 |
| 「中国男人会在三十九岁停两年」 | `:36` `“For men, no. We stay thirty-nine for two years. Then we are forty-one.”` | 一致 | 跳过 |
| 「时间只报了一次——下午四点半」 | 命令：`/usr/bin/grep -nE "half past\|o.clock\|a\.m\.\|p\.m\." ch49_first_kiss.txt`；输出仅 `61:“Don't you like birthdays?” I ask. We are washing the dishes. It's half past four in the afternoon…`；exit=0 | 全章确为 1 次报时，md 说法成立 | 跳过 |
| 「连那顿算午饭还是晚饭都说不准」 | `:61` `and I am not sure whether we ate lunch late, or dinner early` | 一致 | 跳过 |
| 「他用湿的、带肥皂的手碰他的脸」 | `:88` `she touches my face with her wet, soapy hand, and kisses me` | md 主语承前为「她」，与原文一致（未误作「他」） | 跳过 |
| 「她叫他呼吸，他才知道自己屏着气」 | `:93` `She pulls back and says, “Breathe, Oliver,” and I realize that I haven't been.` | 一致 | 跳过 |
| 「他把手放到自己腰上…一个吻从笨拙走向安稳」 | `:93` `She takes my hands and puts them around her waist…` | 置手者是「她」不是他；md 摘要写「又把他的手放到自己腰上」主语正确 | 跳过 |
| 黑发夹银丝一笔未收 | `:71` `Her black hair is interspersed with silver.` | 未进块；导航仅提岁数 | 提示 |
| 第二次吻（歪头—再贴—这次他呼吸）未收 | `:93` `She presses her lips to mine, and this time, I breathe, and we kiss.` | 摘要止于「手放到腰上」 | 提示 |
| md 全章未出现奥利弗 17 岁 | `:18` `(Alba is 40, Oliver is 17)` | 数字层缺一侧年龄；导航用「年纪差」含糊带过 | 提示 |

## 二、报数

- **逐字**：3/3 块引语逐字命中；0 偏差。
- **对应**：3/3 块中文在讲该块引语。b1「日期—更正—缘由」的三层结构讲对；b3 的「提问→模仿→呼吸」次序讲对。
- **形态**：H1 `# 49. First Kiss`；导航 5 项；子项 4 项齐；块数 3＝短章下限（430 词）。
- **断言**：md 内可核断言 8 条全对（四十岁、丈夫是扎克、三十九停两年、四点半唯一报时、午饭晚饭说不准、肥皂手、Breathe、手放腰上）；0 条错，2 条漏段为提示。

## 三、已核实为正确（下一轮勿误改）

1. 「这一章是奥利弗的第一人称现在时」——首句即以 `Oliver:` 起头，全章叙述用 `I`（`:23`、`:61`、`:93`）；**不要改成阿尔芭视角**（同为 First Kiss 的 ch50 才是 Alba 视角）。
2. 「时间只报了一次——下午四点半」——grep 全章仅 `:61` 一处（命令与输出见上表）。
3. 「他说中国男人会在三十九岁停两年」——`:36`，说话人为 Oliver 转述中国习俗，不是阿尔芭。
4. 「她用沾着肥皂的手碰他的脸」——`:88`，施动者为阿尔芭；一句话概括的「她」没有写错。
5. 「他把他的手放到自己腰上」——`:93` `She takes my hands and puts them around her waist`，置手者是阿尔芭，奥利弗是被摆放的一方；summary 的主语正确。
6. 「两人在厨房洗碗」——本章原文未写 kitchen，但跨章可证：`text/ch50_first_kiss.txt:157` `“It was in the kitchen. We were washing dishes, and then you kissed me.”` ⇒ 不是虚构。
7. 「派对还没开就已泄底，她也不显得期待」——`:48` `You told me about it.` ＋下文的道歉，成立。
8. 导航「反转『年长的一方被动』：她替两个人定下节奏」——`:88`–`:93` 三个动作（摸脸、叫他呼吸、摆他的手）全由她发起，成立。
