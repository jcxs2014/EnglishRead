# ch19 Two Little Albas — 判定表

机器层：`bash scripts/chapter.sh ".../ch19 two little albas.md" --json` → **rc=0**，verdict=ok，
块数 4、引语段 4（0 查无）、空引号 0、关键词坏 0、子项缺 0、CJK 低 0、1271 词。
**机器 rc=0 但人判有 1 处阻断**（见下），即"机器全绿 ≠ 内容无误"。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字 | `2-machine.json` quotes 4 段全 `ok:true`（pos 72/1456/2174/6011）；人工复核 md:19/29/39/49 与 text 一致 | 通过 | 假红（无问题） |
| 日期与年龄 | `text/ch19_two_little_albas.txt:18` "Friday, May 1, 2065 (Alba is 7 and 9)" / md:11 | 一致 | 通过 |
| 独自留下的是妹妹，不是姐姐 | `text/ch19_two_little_albas.txt:57-65` "Before it gets light, you’ll be home." … "Um, you’ll be here by yourself for a little while." | md:11「自己还有独自待一会儿」把"你"读成"姐姐" | **阻断** |
| md 内部自相矛盾 | md:11 说姐姐独自留下；md:14 说 Other Alba"把『你会一个人待一会儿』说得很轻" | 同一份 md 两种归属 | 阻断（随上条一并修） |
| 孩子"答不出，只能哭" | `text/ch19_two_little_albas.txt:101` "and I cry, I was scared, Mama, there were rats" | 她哭着说出了原因 | 提示 |
| 水泡穿楼梯 | `text/ch19_two_little_albas.txt:24` "there’s water in the basement"；`:42` "the stairs are gone" | 因果是推断 | 提示 |
| Other Alba = 姐姐 | `text/ch19_two_little_albas.txt:18` "Alba is 7 and 9"；`:42` "because she’s older" | 同一人两个年龄，"姐姐"是译法 | 提示 |
| 乐谱/壁炉一条线未进块 | `text/ch19_two_little_albas.txt:70、76、85` "Look, it’s music" / "how can you write music if you already know how it goes?" / "Maybe we don’t need it anymore." | 未进任何块与导航，只在 md:89 一句带过 | 提示 |
| 形态：H1、导航 5、四子项、块中位 6 | `2-machine.json` form 全绿 | 通过 | 假红（无问题） |

## 报数（四组）

- **逐字**：4/4 通过，0 失败。
- **对应**：4 块，2 通过、2 提示（原句 2 有推断越界；原句 4 有"答不出"过强）。
- **形态**：全绿（4 块，1271 词，block_target 2–4）。
- **断言**：13 条断言，7 通过、**1 阻断**、5 提示。

**本章 rc=0，但有 1 处阻断：md:11 导航把"你会一个人待一会儿"的"你"误作姐姐。**

**改法（一句话）**：md:11「姐姐说天亮前送她回家，自己还要独自待一会儿」→「姐姐说天亮前她就会回家，之后她还要独自在这屋里待一会儿」；或直接引原文"you’ll be here by yourself for a little while"，删掉"自己"这个歧义代词。

## 已核实为正确（防下一轮误修）

1. `text/ch19_two_little_albas.txt:42` "She gets to decide because she’s older." —— 年长的是 Other Alba，md:14「她年长，所以由她决定」正确；**不要**因为"七岁与九岁"就把叙述者当九岁。
2. `text/ch19_two_little_albas.txt:18` "Friday, May 1, 2065" —— 日期是 2065 年 5 月 1 日**星期五**，md:11 的"2065 年 5 月"正确。
3. `text/ch19_two_little_albas.txt:42` "we look funny in the too-big clothes" —— 是"衣服太大"，不是"衣服太小"；md:31 译法正确。
4. `text/ch19_two_little_albas.txt:46` "The thing I saw turns out to be a can of SpaghettiOs." —— 先前看见的是"罐头"，不是"盒子"；md:41 正确。
5. `text/ch19_two_little_albas.txt:89` "Something scratches inside the piano. 'Rats,' Other Alba says." —— 琴里先有响动，后文才见老鼠；md 没有把它写成"老鼠在琴里"（md:57 只说老鼠与蜡烛），未犯误。
6. `text/ch19_two_little_albas.txt:65` "I am afraid of the dark." —— 怕黑的是叙述者（妹妹），md:14「她怕黑」若指妹妹则正确（此处 md 未误置）。
