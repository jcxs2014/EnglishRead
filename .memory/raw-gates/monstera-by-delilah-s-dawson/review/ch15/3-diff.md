# ch15 a garden ripe and soft —— R3 差异单

对照物：`review/ch15/1-suread.json`（R1 独立素读，8 条）＋ `review/ch15/2-machine.json`（R2）。

## 单子一：漏（素读有、md 未体现）
**2 条，均已补**：
1. R1 第 5 条「领她进厨房、取下一只粉色 Caboodle 急救盒」（`text/ch15_chapter_15.txt:85` `Saskia leads her to the kitchen and pulls a pink Caboodle down from a cabinet, before turning to Lucy. “Let’s see it.”`）——md 里 `Caboodle`／`急救` 零命中，而它接住上一章刚立的反差：ch14 里 Lucy 连一只急救箱都没有（`text/ch14_chapter_14.txt:206`），这一章柜门一拉就有盒子。处置：补写为**原句 3**（22 词 2 句）。
2. R1 第 7 条里的「抬起她的下巴、多年以来最深的一次对视」（`:163` `Saskia reaches down, lifts Lucy’s chin so that they are making the deepest eye contact Saskia has had with another person in years, Zoom calls notwithstanding.`）——md 只写了「抱住、骂回去」，`下巴`／`chin` 零命中；这是 Saskia 独居多年这条线的落点。处置：补写为**原句 6**（26 词 1 句，整段原文）。
- 其余 6 条有落点：三处种子数与花园→原句 1；装病三周计划→导航＋一句话总结；醒来握刀→原句 2；血纸巾与胡萝卜说法→原句 4；「找到母亲遗体」→原句 5；你不蠢／混蛋→原句 7；解口罩踮脚吻→原句 8。
- 原块号顺延：旧 3→4、旧 4→5、旧 5→7、旧 6→8；块数 6→8（⑱ 上限 8，合规）。

## 单子二：编（md 有、素读无）
- 0 条。

## 单子三：错（md 与素读不一致）
- 0 条。三处易错点回源核实：
  1. 「第 13 章末行写的正是她醒来时手里握着一把刀」（导航情感弧线）——正确，ch13 章末即 `Wakes up holding a knife.`。
  2. 导航写「原文写的是 I'm constantly lying to you」——正确，`:202` `I’m constantly lying to you, and I hate it.`（是她没说出口的内心话，导航也写明「该说而没说出口」）。
  3. 导航「怪物在屋里，不在门外」的依据——握刀的是她自己的身体、刀出自 Lucy 家厨房（`:28` 一句三样可核），属收窄过的合理读法。

## 派工人处置（2 条）
- 新增**原句 3**（Caboodle 急救盒）与**原句 6**（抬下巴），块数 6→8；改后复跑 `chapter.sh` rc=0、`structure.py order` 29 md / 177 块 · 0 缺陷。
