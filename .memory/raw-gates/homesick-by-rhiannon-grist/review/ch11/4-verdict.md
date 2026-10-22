# ch11 4-verdict

- 文件：`ch11 the fox and the door ajar.md`
- 结论：**1 阻断 / 4 提示**

## 阻断

### 阻断 1｜导航「Tropes 兑现/反转」把 ch01 写成「恐惧的是……陌生男人」——原文无此男性，且性别错位

- 位置：md 第 13 行（`## 本章导航` → **Tropes 兑现/反转**）：
  「反转在于第一章她恐惧的是人（撬痕、陌生男人），这一章威胁是无声的、没有入侵痕迹的」
- 原文证据：ch01 全章没有任何「男人／陌生人」作为威胁出场。ch01 的「stranger」指的是**隔壁那位未见其面的邻居**，性别未定：

```
$ /usr/bin/grep -n -i -E "\bman\b|\bmen\b|stranger|male|bloke" text/ch01_chapter_1.txt
29:No, I’d bought 1b Sgàthan Sìth. A semi-detached. The right half of a stone cottage in the middle of nowhere. To intimately share my rural dreams with a complete stranger.
$ echo $?
0
```

  「撬痕」倒是有据（是门锁四周的深划痕，且她怕的是**前任住户**从门后看她，不是陌生男人）：

```
$ /usr/bin/grep -n -F "deep scratches" text/ch01_chapter_1.txt
125:I ran my hand over the surface of the door. They’d been careless placing the lock. Didn’t matter how much gloss paint they’d used; they’d failed to hide the deep scratches in the woodwork all around the edge. Maybe they’d had to pry it open after the last inhabitant. I peered through the small, mottled window in the door, slightly worried I might see said inhabitant staring back out.
$ echo $?
0
```

  （ch01 唯一的男性是闪回里房产中介前台 `The receptionist had shifted uncomfortably in his seat`，text/ch01_chapter_1.txt:104，与「恐惧」无关。）
- 建议改为：「反转在于第一章她恐惧的是人（门锁四周被撬开的深划痕、门后可能盯着她的前任住户、窗帘后不肯露面的邻居），这一章威胁没有面孔、也不留入侵痕迹，唯一能确认的异常是『门开了』」。

## 提示

1. **「前四章累积的安全感」指代不明且与原文相反**（md:12）。若指 ch01–ch04，那四章并不安全：ch02 标题即 `first blood`、ch04 是 `the mown lawn and half a face`（隔窗半张脸）。建议改成「前几章（ch07–ch10）累积的安全感」。
2. **「这一章威胁是无声的」与本章声音描写矛盾**（md:13）。本章正是被 `Thud-thud-thud-thud-thud`（text/ch11_chapter_11.txt:104、119）与「家具在木头上刮擦的闷响」（text/ch11_chapter_11.txt:122 `The dull screech of furniture on wood`）推动的。建议改为「威胁是没有面孔、没有来源的」。
3. **梦里桥上的老头被整章漏掉**（text/ch11_chapter_11.txt:80 `The old man was watching me from the bridge. Him and his dog.` … `He clutched the handles of the wheelchair carrying the sleeping old woman, and grinned.`）。这是全书反复出现的桥头老者，且在本章梦里「咧嘴笑」是预兆性的一笔，导航与「一句话总结」的梦境复述里都没有他。建议在导航梦段补一句：「梦里桥头那个灰白发像犄角的老头推着轮椅上的熟睡老妇，冲她咧嘴笑。」
4. **`flinch as` 被译成因果**（md:41，原句3 中文理解「随即又缩了一下——因为她努力想挥手回应」）。原文 `then flinched as I struggled to wave back` 的 `as` 是「当……时」，不是「因为」；她的爪子乱抓是同时发生的动作，不是对方退缩的原因。建议改为「她努力想挥手回应时，他们又都缩了一下——她的黑爪子在人家脸前乱抓」。
5. **`tinned chilli` 译作「罐头辣豆」**（md:11 导航）。英国语境里 chilli 通常指 chilli con carne（辣肉酱），「辣豆」易读成素豆子。建议「一罐辣肉酱」。

## R4 三问

1. **谁做的**：Tamsin 一人在 1b 过夜。她自己翻箱找睡袍当被子（text/ch11_chapter_11.txt:8）、自己开卧室门查看楼梯口并确认门链（:62）、自己做梦（:77）、自己被脚步声惊醒后拿斧头下楼巡查（:113）、自己把第二次响声归因于邻居（:122）。全程无第二人在场，邻居只以声音存在。
2. **什么关系／谁欠谁**：本章只有一条现实的相邻关系与一条梦里的施受关系。邻居（1a）与她是「只闻其声」的共墙关系，她不欠邻居、邻居也不欠她；梦里 **Rowan 是施惠者、她是施害者**——`Rowan, the man from the hardware store, he was the only one who tried to help me. But the moment he got close, I clamped my jaw around his wrist, so he couldn’t leave.`（text/ch11_chapter_11.txt:77），她明确知道自己在伤他（`I could see the skin tearing around my teeth`），欠下的是「他善意、她伤害」这笔债。与母亲的关系是受惠：睡袍是母亲送的圣诞礼物，她此前从不穿（:8）。
3. **数字与死因**：本章**无死亡、无年龄、无金额、无日期**。唯一数字是门牌 `1b`／`1a`，有逐字依据：`I eyed the joining wall between 1b and 1a.`（text/ch11_chapter_11.txt:14）。因此不存在需要核的死因或年龄断言；md 也未编造任何数字。✔ 不阻断。

## 已核实为正确（下一轮不要改坏）

① 原句1–5 五段引语逐字无误（含 `terrycloth`、`indispensable to older generations`、`clamped my jaw around his wrist`、末句 `hadn’t I?`）；
② 「狐狸尖叫 → 不是人」的判断链正确（text/ch11_chapter_11.txt:26 `A fox. A fucking fox.`）；
③ 「门链还在」的细节正确（:62 `And there was the chain, just where I knew it would be.`）；
④ 「斧头本来就在地下室门边、她只是捡起来」正确（:113 `My axe lay on the floor by the basement door.`）；
⑤ 「前门仍锁、无撬痕、地下室封口完好」三查俱全（:113）；
⑥ 「第二次响声来自隔壁、是她半睡误听」的归因正确（:122）；
⑦ 末句「睡前明明关过门」的悬置判断正确（:140）；
⑧ 词汇例句均能在原文逐字命中（`ingenuity`／`spectre`／`juddered`／`skittered`／`clutched` 等）。
