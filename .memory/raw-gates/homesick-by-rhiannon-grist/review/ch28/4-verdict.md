# ch28 判定（R4）：`ch28 the tartan scarf.md`

## 结论

**不通过（1 阻断 / 6 提示）。** 五条原句字面全部逐字对得上、词汇表 26 条例句也无错引，问题只在两处：**围巾归属写反了**（本章因果的支点），以及四处边界/计数/表格结构的小毛病。改掉阻断那一条即可放行，其余随便修不修。

## 阻断

1. **md:12 一句话概括｜「她昨晚把一条格子围巾落在 The Curtyard」——归属错，且与本句后半自相矛盾。**
   围巾不是 Tamsin 的：她当场否认（`“That isn’t mine,” I said.`，text:53），随后认出是邻居的（text:62），后文也把它安置在邻居卧室（`It was the same tartan scarf I’d tied onto her door handle yesterday.`，ch46:23），村民后来还问她「did you get your scarf back?」而她答 `“Not my scarf.”`（ch34:26/32）。「Viv 说这是你昨晚落在酒馆的」只是 **Viv 的误认转述**。
   - 建议改为：「Maggie 和 Rowan 找上门来——Viv 说这条格子围巾是塔姆辛昨晚落在 The Curtyard 的，可它不是她的，而是那天蒙在邻居眼睛上、看她投环的那条」。

## 提示

1. **md:54 原句4 跨段拼接**：`…all by myself.` 是 text:122，`“I’m perfectly alright,”…` 是 text:125，中间隔着空段。词都逐字对，但引用应断开或加 `…`。
2. **md:112 `scarf` 例句跨段拼接**：text:32 + text:35 两个自然段粘成一条，同上处理。
3. **md:104 `sparkling` 例句引号未闭合**：`“And miss out on your sparkling company?` 缺收尾；text:167 原句是 `“And miss out on your sparkling company? Never.”`。建议补全或截到 `company?` 并把开引号去掉。
4. **md:52 把两个晚上并成一个**：「昨晚在酒馆里扔圈的人是谁？」——投环（`The hoop flew`）发生在 ch24:59/71 那一晚；ch28 只证明 **昨晚** 围巾落在酒馆（text:32）。建议改为「那昨晚把围巾落在酒馆的人是谁？」或「那个蒙着眼投环的人，昨晚又去了酒馆？」
5. **md:60「嘴上四个字」计数不准**：中文「我完全没事」五字，原文 `“I’m perfectly alright,”` 三词。建议改成「嘴上只有一句'我完全没事'」。
6. **词汇表结构被打断**：md:82-85（`silhouette` 前无表头）、91-92、97、100、105、108-110、114-116 等处夹空行或裸行，Markdown 渲染时表格会断成几截。建议整表连排。

（附记）md:126「那天早上她第一次觉得」——text:209 是 `For the first time in a long while`，「很久以来第一次」比「第一次」稳。

## R4 三问

1. **谁做的**：送围巾的是 **Maggie**（Maggie's Café 老板娘，text:8；名字本身是 Tamsin 的推定 `who I assumed was called Maggie`）；开车送她来的是 **Rowan**（text:47 `Ro offered to drive me over on my way home`，text:20 那辆 `muddy, navy flatbed truck`）；围巾的**原主是邻居**（1a），失物线索由 **Viv**（The Curtyard 老板，`Loves a zebra`，text:41）提供。md 除阻断那条外，人物分工都写对了。
2. **关系与谁欠谁**：本章是一组**双向小人情**——Maggie 欠 Rowan 一趟顺风车（`I was going to make Maggie chum me up in return for driving her over`，text:158），Rowan 欠 Tamsin 一次副驾（`I just need someone who can sit with me while I drive the van`，text:149），Tamsin 想欠/被欠以进入关系（`I wanted to be someone people could ask for a favour`，text:188）。她答应得快，是因为这笔人情后面可能换成 `a bit of paid website work`（text:188）。md:18 抓住的正是这一层，没写错。
3. **数字与死因**：本章无死亡。数字类：从她门口到邻居门口 `the four steps`（text:113）；Rowan 车上贴着 learner 的 `‘L’`（text:20）；车牌/保险细节 `I’m not on your insurance`（text:173）——Rowan 的回答是 `it’s only a problem if we knock into someone`（text:176），这句是后文风险的伏笔，md 未提，不算漏。md 唯一的数字错是提示 5 的「四个字」。

## 已核实为正确（下一轮不要改坏）

- 五条原句的**字面**：text:62 / 113 / 119 / 122+125 / 188；弯引号 `“ ” ’` 与破折号 `—` 全部照原文。
- md:30 说「把 **ch24** 的场景调回来」——**章号是对的**（ch24:59 蒙眼投环、ch24:71 `The hoop flew`），不要被 ch26 那场隔壁聚会带偏改成 26。
- md:18「缝皮针」有据：ch17:92 `It could probably be used to sew leather.`、ch40:131 `Lucky you used a leatherworking needle.`
- md:16「鬼不会把围巾落在酒馆」直接对应 text:68 `Unless ghosts go to the pub.`
- 词汇表 26 条例句均可 grep 命中，`papery`（text:209）、`vicious`（text:206）、`assessing`（text:128）、`lifesaver`（text:194）都对。
- 「1a 不是空的」这句是 Tamsin 自己第一次说出口（text:110），Maggie 反倒说以为它是空的（text:119）——这个对照写对了，别改反。
