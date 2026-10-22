# ch33 4-verdict

- 文件：`ch33 the not my mum story.md`（124 行）
- 结论：**1 阻断 / 4 提示**

## 阻断

### B1 人物弧线编出原文没有的动作：她“把手伸向订书机”
- 位置：`ch33 the not my mum story.md:18`（导航·人物弧线）
- 现状：「她的弧线是往回缩——听完故事没有走近真相，**只是把手伸向一台订书机**。」
- 问题：原文只写**目光**锁住订书机，她的手没有伸出去；同桌还有 Fergus 的手。md 自己在 `:64`（原句 5）与 `:72`（读者视角提示）都写对了——“我的**眼睛**盯住……”“这台订书机在本章没有用上”，人物弧线与本文件内的引语/分析自相矛盾。原文证据：
  - `text/ch33_chapter_33.txt:182`「My eyes locked onto the loaded, industrial stapler on the desk, his hand laid close by.」
  - `:176`「He kept laughing, mouth wide, wide enough that I could see all of his teeth at once.」（她在看他的牙，不是伸手）
- 建议改后：「她的弧线是往回缩——听完故事没有走近真相，**只是把目光落在柜台那台工业订书机上**。」

## 提示

1. `:12`（导航·一句话概括）｜「**楼上**叫我的不是我妈」——传说原名是 `my-not-mum-called-me-from-downstairs`（`text/ch33_chapter_33.txt:203`），声音来自**楼下**；本文件 `:124` 一句话总结已写“楼下”，两处自相矛盾。建议统一为「楼下叫我的不是我妈」。
2. `:64`（原句 5）｜引语跨**三段**合并：`text/ch33_chapter_33.txt:176`「He kept laughing…」、`:179`「The high ringing in my ears grew.」、`:182`「My eyes locked onto…」原文各有空行。建议在引语中加 `…` 或拆成三条。
3. 漏掉全章最冷的一笔：男孩几周后回校，**胎记消失**，说「I changed it, so Mum could be safe.」（`text/ch33_chapter_33.txt:149`「He was back. But as I got close, I saw he was missing that birthmark.」／`:152`）。这是故事与 1a 复制体线的接口，md 导航只留“胎记男孩”，原句 4 又止于“moved on again”。建议在导航补半句或加一条原句。
4. `:32`（读者视角提示）｜「她认得出这种笑，因为**她家里**就有一个」——原文 `:71` 的「A bit like her smile.」指代留白；最可能指隔壁 1a 的女人（与 `text/ch27_chapter_27.txt:38` 蚀刻像的「a too-wide smile」呼应），不是“她家里”。建议改「因为她见过那种笑」。

## R4 三问

1. **谁做的**：**Fergus 讲**（并设局），故事里的行动者是**男孩**——顶门、翻窗、爬屋顶、跑去学校（`text/ch33_chapter_33.txt:128`/`:134`）；“叫他下楼”的声音与浴室门后的母亲是故事中的两个“妈妈”（`:119`）。Tamsin 在本章**只听**：攥白柜台边缘（`:122`）、目光锁订书机（`:182`）、最后走出店门（`:212`）。Rowan 推门进来（`:188`），没有参与叙述。
2. **什么关系／谁欠谁**：Fergus—Rowan＝熟人／朋友（Fergus 叫他“your new pal”，`:197`），Fergus 替 Rowan 代班（`:8`）；Fergus—Tamsin＝店主与顾客，他**故意捉弄**她（`:203`「I just told her the old … urban legend and she believed me.」／`:209`「You know what these tourists are like.」），欠她一个道歉，她欠他什么也没有。故事里的男孩—母亲＝被“两个妈妈”拆散的亲子；**她与 1a 邻居**：她一度以为“his house was my house”（`:161`），Fergus 用“Got you”否认——镜像关系是**被暗示又撤回**的，不能当成事实。复制体—本体：故事里的“两个妈妈”是母题，但本章明确降级为都市传说，**不构成书内事实**。
3. **数字与死因**：男孩当时「about nine, ten?」（`:86`）＝约九到十岁；夜里「about two in the morning」（`:110`）＝凌晨两点；「A few weeks went by… just before school closed for Christmas break」（`:149`）＝几周后、圣诞假前；**无人死亡**——男孩没死、母亲没死、也没有人受伤（他落地只是「Winded himself」，`:134`）。无金额、无日期。md 未编数字。

## 已核实为正确（下一轮不要改坏）

- 原句 1–4、6 逐字命中 `text/ch33_chapter_33.txt:71 / 119 / 134 / 149 / 188`；原句 6 是单段连续，不是拼贴。
- 都市传说原名 `my-not-mum-called-me-from-downstairs`（`:203`）拼写与归属（Fergus 说的）正确。
- “Got you”之后她**没有**真的用订书机——md `:72` 已写明“本章没有用上”，不要改成“她抓起订书机”。
- “他一定是追着我跑下来的”是她的推断（`:188`「He must have chased down after me.」），md 未写成叙述者事实。
- Fergus 是替 Rowan 代班（`:8`「Rowan had said Fergus was busy at the store.」），不是碰巧在店。
- 词汇表 20 条例句全部逐字落在 `text/ch33_chapter_33.txt`（disdain `:8`、flinch `:77`、inevitably `:155`、thundering/vengeful/gaping `:188`、creaky `:167`、urban legend `:203`、distracted `:98`、miffed `:149`、forgetful `:104`、mouthed `:119`、sleepover `:92`、birthmark `:86`、shrugged `:29`、football `:95`、chore `:5`、stapler `:8`、garden `:134`、keys `:11`），表格无破损行。
