# 4-correspondence · ch39 逐块对应（一行一块）

> 判据：这段中文是不是在讲这句引语？引语是谁说的（施事/受事/归属有没有写反）？分析有没有讲到引语之外的东西？
> 依据文件：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch39_39.txt`（区间为字符偏移）

| 块号 | 引语区间 | 结论 | 一句依据 |
|---|---|---|---|
| 原句 1 | 310–812 | 对应成立（1 提示） | 中文逐项对上 text:26 的 candlesticks／markings／time capsule／ancestor worship／Grave robbing／Highgate Cemetery，说话人 Matt ✓；仅「读者视角提示」提前搬来 text:93 的「家族墓穴」。 |
| 原句 2 | 2556–2708 | 对应成立，**内容阻断 1** | 施事受事都对（text:75 遗嘱卡住 Digby 归还 mokomokai、询法律意见、送回新西兰），但 md:28 把 mokomokai 释成「毛利战鼓」，原文 text:129 同物为 `the shrunken heads`、text/ch11_11.txt:102 `seven toi moko or mokomokai`。 |
| 原句 3 | 3256–3519 | 对应成立，**内容阻断 1** | 说话人是 Matt 的内心（`Matt wondered`）✓、手的归属（Horatio 之妻＝Fenella 的曾曾祖母＝`hers`）✓；但 md:38「降神会数量」把 text:90 `the sheer number of orgies`（群交次数）写成降神会次数。 |
| 原句 4 | 3789–4235 | 对应成立，**内容阻断 2** | 说话人 Fenella ✓；但 md:42「博物馆一直坚持塑造他」写反——text:99 是 `despite how he insisted we portray him`（坚持者是 Horatio 本人），且 md:42「她祖父小时候」把 `My great-grandfather`（曾祖父）写成祖父，与同段的「曾祖父阿洛伊修斯」自相矛盾。 |
| 原句 5 | 5144–5536 | 对应成立（3 提示） | 引语是 Fenella 的话、「他」= Digby ✓，回收箱／因果报应逐项对上 text:123；提示：「她此前的许多封信」归属含混（原文 `so many of his letters`）、「顺手／销毁证据」为分析添加、「karma」原文作 `karmic`。 |
| 原句 6 | 5597–6030 | 对应成立（2 提示） | 逐项对上 text:129 的报价并附信／lowballing／piss off／缩头／millstone／the money／`It was glorious. He was going to really live.`；**原文无任何金额，md 也未编造金额** ✓；提示：「约她吃午饭」未指明对象（原文 `go for lunch to discuss an offer`）。 |

## 跨块（导航／总结层）

| # | 位置 | 结论 | 一句依据 |
|---|---|---|---|
| X1 | md:11 导航「一句话概括」 | **阻断** | 「他（Matt）去研究所找那本失踪的日记」写反——text:41 是 Amy 说 `I’m going to go back to the Institute and see if I can find it first`，Matt 只说 text:44 `Try Digby’s house too.` |
| X2 | md:11 导航「一句话概括」 | **阻断** | 「Amy 继续挖『假 Isolde』」受事写反——text:32 Matt 交代的是 `look into real Isolde again`，「假 Isolde」是要解释的对象。 |
| X3 | md:110 一句话总结 | **阻断** | 「Matt 一边在警局接着查那本失踪的日记和『假 Isolde』」施事＋受事双错（依据同 X1／X2）。 |
| X4 | md:11 导航「一句话概括」 | **阻断** | 「归还缩头与 mokomokai 的打算」把一物当两物——text:129 `returning the shrunken heads here too` 即 mokomokai（text/ch11_11.txt:102 `toi moko or mokomokai`）。 |
| X5 | md:15 导航「叙事手法」 | **阻断** | 「缩头、战鼓」并列为两物；mokomokai 是风干人头骨（text/ch02_2.txt:285 `preserved … showcasing their tattoos`），非战鼓。 |
| X6 | md:67 词汇表 mokomokai 条 | **阻断** | 释义「毛利战鼓；此处指霍雷肖带回的毛利编年史木刻」两处皆错；本书 ch02:125、ch11:82 已写对（「风干缩头」「人头骨」）。 |
| X7 | md:11 导航「分部「FRIDAY」」 | 成立 ✓ | epub `OPS/toc.ncx` 第八分部标题逐字为 `FRIDAY`（`s050-Part-008.xhtml`），ch39 在其中，未误用 `A FRIDAY IN MAY`。 |
| X8 | md:110「迪吉死后的第一个星期五」 | 成立 ✓ | Digby 死于第一部 `A FRIDAY IN MAY`（epub spine：Part-001 → Chapter-001），ch39 属再下一个 `FRIDAY`（+7 天）。 |
| X9 | md:11「信里那笔被嫌压价的收购报价」 | 成立 ✓ | 本章原文无金额（grep 见 3-diff.md 取证），md 未虚构数字。 |
