# ch13 4-verdict

- 文件：`ch13 a postage stamp of a rug.md`
- 结论：**1 阻断 / 2 提示**

## 阻断

### 阻断 1｜导航把「同一天买、同一天抱回」的地毯写成「昨天赌气买下的」——时间线错标

- 位置：md 第 11 行（`## 本章导航` → **一句话概括**）：「Tamsin 抱着昨天赌气买下的地毯走回小屋」
- 原文证据：ch12 结尾就是「为了当晚的酒吧聚会，先把地毯抱回家放下」，ch13 开头紧接着是这段回家的路、同一天傍晚再去村子：

```
$ /usr/bin/grep -n -F "Tonight was the meet-up at the pub" text/ch12_chapter_12.txt
188:I then realised I hadn’t asked about delivery. Tonight was the meet-up at the pub. I could hardly walk around town with a rug under my arm all day, let alone take it out for drinks with me. I looked at Bodach’s Brig and the road back out of town. My shoulders drooped. I would have to walk all the way home to drop off the rug and then walk all the way back.
$ echo $?
0

$ /usr/bin/grep -n -F "started the long walk home" text/ch12_chapter_12.txt
194:I shifted the rug under my arm and started the long walk home.
$ echo $?
0

$ /usr/bin/grep -n -F "The walk back took longer than the walk in" text/ch13_chapter_13.txt
5:The walk back took longer than the walk in. I had to keep stopping every few feet to readjust my grip on the rug. …
$ echo $?
0
```

  ch13 里的「昨天」指的是**邻居那次尴尬照面**，不是买地毯：

```
$ /usr/bin/grep -n -F "the awkwardness of yesterday" text/ch13_chapter_13.txt
59:Maybe I should invite her out tonight, I thought. Learn her name. Make up for the awkwardness of yesterday.
$ echo $?
0
```

  且本章结尾她「换上毛衣就出门去村里」，正是 ch12 说的当晚聚会，中间没有过夜。
- 建议改为：「Tamsin 抱着当天赌气买下的地毯走回小屋（她得先放下地毯，才好赶当晚村里的聚会）」。

## 提示

1. **`the single watery eye` 的「单只」在导航里丢了**（md:11「那只水汪汪的眼睛」）。原文 `the barely seen face, the lank hair, the single watery eye`（text/ch13_chapter_13.txt:74）强调的是**只有一只眼**能看见，这是哥特线的关键一笔。建议导航改为「那只水汪汪的独眼」。
2. **原句3 中文理解把 `barely seen` 译成「只看清一半」**（md:41）。`barely seen` 是「几乎看不清」，不是「看清了一半」；「一半」会与 ch04 的「半张脸」混淆。建议改为「那张几乎看不清的脸」。

## R4 三问

1. **谁做的**：Tamsin 一个人完成全章动作——自己把地毯抱回家（text/ch13_chapter_13.txt:5）、自己找工具、自己用斧头割扎带（:32）、自己坐地认输（:44）、自己幻想、自己换衣（:71）、自己走到 1a 门口又自己收手（:80、:83）。邻居全程没有出场、没有台词，只以「安静／可能昼伏夜出」被谈论（:14、:17）。
2. **什么关系／谁欠谁**：本章没有任何实际发生的施受关系，只有**她单方面替邻居安排**的关系想象：她要当「把对方拉出壳」的恩人，坐对方婚礼主桌（text/ch13_chapter_13.txt:62 `I imagined myself sat at the top table on her wedding day`）。她自己随后意识到这个念头是「self-congratulating」（:74），于是收手——即她判断自己**不欠**邻居一场社交，也不确定自己会不会造成打扰（:77 `What if she was left alone out here for a reason?`）。地毯交易上她「欠」自己一张收据（:44），对方（店主）不欠她什么。
3. **数字与死因**：本章**无死亡、无年龄、无金额、无日期**。唯一数字是地毯尺寸 `Barely a metre long.`（text/ch13_chapter_13.txt:38），md 写的「不到一米」有据。没有需要核的死因断言；md 未编造数字。✔ 不阻断。

## 已核实为正确（下一轮不要改坏）

① 原句1–3 三段引语逐字无误（含 `simultaneously too big and too small`、`top table on her wedding day`、`the single watery eye`）；
② 「用斧头割塑料扎带」正确（text/ch13_chapter_13.txt:32 `nicked the plastic ties with its shining, still-new edge`）；
③ 「门垫／杯垫／邮票」三连比喻逐字对应（:38 `A doormat. A coaster. A postage stamp.`）；
④ 「后悔没拿收据」正确（:44）；
⑤ 「奶油色阿兰毛衣、吊牌还在、咬掉吊牌」正确（:71 `cream woollen jumper` / `It even still had its tags. Not anymore. I bit the tags off`）；
⑥ 「门边忽然多出的吊花篮」正确（:74 `were those hanging baskets trailing pretty little flowers?`）；
⑦ 「她想起黑屋/憔悴脸/塌发/独眼后收拳退开、独自去村」正确（:74、:80、:83）；
⑧ 「邻居昼伏夜出、怕日光」确系她的脑补、原文无证据（:17），md 的判断正确。
