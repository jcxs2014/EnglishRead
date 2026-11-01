# ch01 三单对账（R3）

素读基准：`1-suread.json`（facts 7 / relations 3 / numbers 4）；晶体：`ch01 business or pleasure.md`（4 块）。

## 漏（素读有、md 未写）
- **F5/F6/F7 未成块**：素读记「她把手放到共用扶手上（L49）」「邻座嘟囔着让出扶手（L52）」「她转回电脑藏起笑容（L54-55）」。md 只写到「她用假求助挡开邻座」这一层，没有单独立块。
  - 两侧原文：`text/ch01_chapter_1.txt:49` `“You—you wouldn't want to help me, would you?” I laid a hand on our shared armrest`；`text/ch01_chapter_1.txt:52` `“Nah, nah, just gonna watch a movie,” he mumbled, relinquishing the armrest`
  - 判定：**漏**，但属选材取舍（本章 761 词、块数 4 为本章篇幅下限），不构成事实错误 ⇒ 提示。
- **F2 未单独立块**：邻座自称在纽约做金融、与大学同学去 Jackson Hole 打高尔夫（L19）。md 原句 2 用「And he was a golfer too」承接，未展开 Jackon Hole。⇒ 提示（选材）。

## 编（md 有、原文无）
- 无。四块引语逐字命中（`2-machine.json` verdict=ok，4/4 segments ok）。

## 错（md 与原文冲突）
- **「假邀请」用词不准**：导航与一句话总结原写「她用一个『优化策略』的假邀请挡开了邻座」。
  - md 侧：`ch01 business or pleasure.md:10`、`:89`
  - 原文侧：`text/ch01_chapter_1.txt:43` 她说的是「I'm on my way to workshop some optimization strategies with a colleague…Unless—」，`:46` 明写 `This was a bluff`，`:49` 落地成请求对方帮忙 `you wouldn't want to help me, would you?`
  - 判定：**错（措辞）**——那是**假求助**（假装需要人帮忙整理笔记），不是邀请同行。已改。
