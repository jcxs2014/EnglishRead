# ch38 4-verdict

- 文件：`ch38 the orchard and the key.md`
- 结论：**0 阻断 / 3 提示**

## 阻断

无。

事实层逐条对到 `text/ch38_chapter_38.txt`：施事（果园女人推醒 / 父亲回话 / Rowan 多管闲事 / 邻居地下室偷袭 / 她自己扎穿手掌）全部与原文同向；三处"账"的归属与原文第 89 行一致；无凭空数字、年龄、日期、死因。

## 提示

1. **导航·一句话概括「咳出含在嘴里的钥匙和弯针」｜动作偏移（提示）**
   证据：`text/ch38_chapter_38.txt:29` 「I tried to answer, but something caught in my throat. I gagged.」+ `:35` 「With my good hand, I pulled out my house key covered in spit and phlegm.」；`/usr/bin/grep -n -i "cough" text/ch38_chapter_38.txt` → 无输出、`rc=1`（原文无 cough）。
   建议改为「她作呕，用手从嘴里掏出沾满口水的钥匙和那根弯针」。

2. **导航·情感弧线位置「这一章她选择'打'」｜漏一层转折（提示）**
   证据：`text/ch38_chapter_38.txt:104` 「Well last night, she tipped her hand. After seeing all those skulls and their keys, I was ready to choose.」——她要选的是"哪个现实为真"（邻居是怪物 / 自己是怪物），"打"是选完的结果。
   建议在该项补半句：「她先在'我疯了'与'这些事真在发生'之间做了选择——认定邻居露了底牌——然后才决定打。」

3. **「苹果花」（第 30、115 行两处）｜原文无"苹果"（提示）**
   证据：`text/ch38_chapter_38.txt:23` 「I was lying between two rows of stout trees, pink blossom dotted among the leaves.」；`/usr/bin/grep -n -i "apple" text/ch38_chapter_38.txt` → 无输出、`rc=1`。原文只说"粉色的花"。
   建议改为「醒来是满树粉花」/「在开花的果树下」。

（附带一条同源译词，可与上条一并处理：原句3 把 `I’m sure it’s not that bad` 译为"我相信没那么糟"，`sure` 此处是"我敢说/我肯定"，不是"相信"；ch12 审查已按同一口径把"我保证"改成"我确信"，建议此处统一为"我肯定没那么糟"。）

## R4 三问

1. **谁做的**：① 叫醒并威胁报警的是果园主人——一个"皮靴 + 蜡布外套 + 红卷发"的陌生女人（`text/ch38_chapter_38.txt:14,20,26`），不是邻居、不是 Rowan；② 把 Tamsin 逼到果园的是她自己（跑进林地昏倒，`:23`「I must have passed out here after running away into the woods」）；③ 手上的伤是她自己造成（弯针连在钥匙上、扎穿虎口，`:35`）；④ 父亲的回话是父亲本人发的（`:74`）；⑤ 邻居额上的半月疤，原文的因果句是"若她没在地下室偷袭我，她也不会有那道疤"（`:89`）——即伤是 Tamsin 这边造成的，md 未写反。
2. **什么关系 / 谁欠谁**：父亲对女儿是"辱骂式关心"的欠账方——`I’m a little busy right now helping out with the Graysons. I’m sure it’s not that bad.`（`:74`）把她的事排在他帮 Grayson 家之后；Grayson 家是父母的朋友、两个女孩（Lucy / Laura-Ann）是父亲偏爱的对象（`text/ch24_chapter_24.txt:35`，`text/ch34_chapter_34.txt:47` 父亲推她们荡秋千）——md 第 52 行"Grayson 家就是前面荡秋千的那两个女孩的家"有据，非编。对 Rowan 与邻居，本章是"记账"关系：她把 Rowan 的介入与邻居的偷袭并列为把自己推到这一步的原因（`:89`），本章尚未对邻居做出实体行动。
3. **数字与死因**：① "一小时"——`text/ch38_chapter_38.txt:26`「if you’re not gone in an hour, I’ll be calling the police」；② 门牌 1b——`:107`「1b Sgàthan Sìth was my house」；③ 无年龄、无金额、无日期；④ 本章**没有人死**：昨夜"骷髅与骨山"被明确写成幻觉/梦（`:41`「Another hallucination perhaps. A fever dream」），md 未把它当实际死亡，正确。

## 已核实为正确（下一轮不要改坏）

① 三笔账的归属与顺序（父亲 → Rowan → 邻居）逐字对应 `:89`；② 邻居的疤是"半月形"且由地下室那次冲突造成，未写成"邻居伤了她"；③ 父亲原话三句逐字（`:74`），"我肯定没那么糟"的回响动机成立；④ 钥匙"从骷髅嘴里 → 到她嘴里 → 到她手里"的物件线，md 第 16、72 行与 `:35,38,107` 一致；⑤ "Mine." 的独立成段与三个 shitty 的排比，`text/ch38_chapter_38.txt:110-113` 确实是三段；⑥ 结尾去村子找的是"梦里打结的老妇人"（`:131`），不是酒馆老板娘、不是 Maggie。
