# ch23 深审 R3 三张单子（漏 / 编 / 错）

> 章：`text/ch23_chapter_23.txt` ↔ `ch23 the devils bath.md`
> 流程：R1 素读（`1-suread.json`，132 条证据片段全部为原文子串，`BAD=0`）→ R2 机器 → R3 本文件 → R4 逐块对应（§四）→ R5 判定（见 `4-verdict.md`）

---

## 〇、结构底账

| # | 事实 | 证据（`text/ch23_chapter_23.txt`） |
|---|---|---|
| 1 | 正文体范围 `:35`–`:207`（`:207` `…stole every last drop.` 为最后一句；`:208` 为空行） | `:35` `Helena couldn’t stop thinking about Cynthia.` |
| 2 | **单一视角＝海伦娜**全章到底，换场只换地点不换 POV | 通读 `:35`–`:207`；`:186` 起场景二仍贴海伦娜内感知（“她先感到热”） |
| 3 | 换场空白带 `:171`–`:185`（15 行空白），场一 `:35`–`:170`、场二 `:186`–`:207` | 逐行核：`:170` 末句 `The world went dark.` → `:186` `Helena felt the heat first.` |
| 4 | 推广／版权残留行 0 条 | `/usr/bin/grep -ci lokepub` → `0`，rc=1（§六 A） |
| 5 | 场一地点＝**药草店 All Things Bright and Beautiful**（“我们打烊了”，她盘点、忘锁前门） | `:53` `inventory`；`:122` `We’re closed for the day.`；`:131` 店名；`:146` `We are closed.` |
| 6 | 场二地点＝**干热的雪松木房间**（后由 ch24–ch25 揭示为五钟街土耳其浴场的最后一道桑拿房） | `:198` `Cedar and eucalyptus…no larger than her own bedroom. Wooden benches lined the cedar-planked walls.`；ch25 `:92` `The final sauna…Tiled on the outside to maintain utmost heat, a furnace blasted hot air through vents into the cedar-planked interior.` |
| 7 | 舅舅＝**母系**（拉克兰是罗温的丈夫），故 md 用「拉克兰舅舅」正确 | ch21 `:326` `Aunt Rowan and Uncle Lachlan realised they couldn’t save her.`；ch22 `:156` `your uncle and my brother` |
| 8 | 死者全名＝**Hubert Burrows** | `:44` `Hubert Burrows’ murderer` |
| 9 | 辛克莱**首次被提名在 ch08**（ch01–ch07 全部 0 命中） | §六 B：`ch08:41` `The Devil of Seven Dials. Damien Sinclair.`；ch01–ch07 计数全 0 |
| 10 | 海伦娜**在 ch10 已与辛克莱当面对话**（并非本章第一次） | ch10 `:161` `‘I am here to ensure Lady Burrows’ safety.’`（海伦娜）／`:170` `‘With relish, Mr Sinclair.’` | 
| 11 | 辛克莱的口音＝**吞掉词首 h 的伦敦土腔**（非口吃） | `:125` `’oping`／`:131` `’eard`／`:149` `’ere`；ch10 `:156` `tinged with the accent of the rookery` |
| 12 | 魔法失灵的规则条目：平时可屏蔽，例外＝对方情绪强烈／她主动探查；近来一出门就被侵入 | `:65` |
| 13 | 无引号心声 2 处：`:92` 与 `:110`–`:113` | `:92` `But Cynthia would never hurt me.`；`:110` `Oh. Dear. Goddess.`／`:113` `I’m wrong.` |
| 14 | 哈姆雷特本章**不说话**，只以吼／吠／贴腿／搭手／舔脸表态 | `:71` `whined`／`:77` `growled…hackles rose`／`:80` `barked`／`:98` `bumped his head into her knee`／`:101` `paws on her arm`／`:107` `licked her cheek` |
| 15 | 辛克莱当面说出他要找的东西：**一个女巫** | `:164` `‘I seek a witch, Miss Blair.’` |
| 16 | 击倒只有一句叙述，未写出手者／方位／工具 | `:170` `…something heavy slammed into the back of her head. The world went dark.` |
| 17 | 房间触感：干热、空气吸走水分、呼吸灼肺、雪松＋尤加利香 | `:186`／`:198` |
| 18 | md：9 块（`md:18/28/38/48/58/68/78/88/98`）、词表 24 行 9/9/6、导航 5 项 | `2-machine.json`：`blocks=9`、`block_target=[3,5]`、`words=1660`、**`block_hint`＝「块数 9 偏离本章篇幅建议 3–5（本章 1660 词）」**、`segments=9`、`segment_miss=0`、`issues` 全空 |

---

## 一、漏

| # | 原文事实 | md 现状 | 判定 |
|---|---|---|---|
| L1 | `:50` 拉克兰的旧身份：`Uncle Lachlan’s lethal glare reminded Helena the man had once been a deadly and fearsome soldier in her majesty’s army.` | md:13 只写他「从可依靠的执法者变成确信而无法证明的人」，未记军人底账 | 提示 |
| L2 | `:116` `Her coven knew it. Aunt Rowan knew it. The fox knew it. And he was trying to break it to her gently.` —— 不是狐狸独自说服，**整个女巫团早已知情** | md:13 只写「哈姆雷特从沉默的反对者变成用身体说话的人」 | 提示 |
| L3 | `:152` `Damien Sinclair only came out of Seven Dials for one purpose: to start a war.` —— 她聚水的判断依据（不是被动挨打） | md:10 只写「她从空气里抽水分…威胁他」，未记这句动机 | 提示 |
| L4 | `:167` `The Devil of Seven Dials might be hunting witches, but she refused to be anyone’s prey.` | 无 | 提示 |
| L5 | `:198` 她的复仇幻想：`send Sinclair into the depths of the English Channel on a geyser of witchwater powered by her rage` | 无（`geyser` 只进了词表） | 提示 |
| L6 | `:134` 海伦娜的回嘴 `I hardly think you converse with our clientele, Sinclair.` ＋ `:137` 辛克莱的 `You would be surprised at the quality of company I keep` —— 进店后的双向试探 | md:10 直接跳到「离开的最后机会」 | 提示 |

---

## 二、编

**本节无新增凭空事实。**（md 与原文冲突的三处——「第一次当面对话」「口吃」「摸鼻子」——按「与原文相反／新增动作」记在 §三，不重复计数。）

**成立取证表（md 事实主张逐条回原文）**

| md 主张 | 原文 |
|---|---|
| 她多接班、仍被门铃牵着心起心落 | `:35` |
| 陪埃莉送货、尖酸与白眼引来三次抱怨、埃莉建议找拉克兰 | `:38` |
| 命案僵局＋辛克莱对七铃区控制密不透风＋贿赂／威胁／赦免旧罪都换不来证词 | `:41` |
| 拉克兰将被派往巴斯，协查针对贵族的连环盗窃 | `:41` |
| 「我们已经找到凶手…我只是没法证明」（人物口述，非法律事实） | `:47` |
| 「他迟早失手」 | `:47` `He’ll slip up.` |
| 盘点＝全员最讨厌的活、她自愿、做到深夜 | `:53`／`:56` |
| 魔法失灵四条：凝水、湿衣、闪银多于灰、念头压不住 | `:65` |
| 「爱不是我的选项，她值得一份爱」 | `:74` |
| 「我不会被爱遮眼」＋两个 `I won’t` | `:86` |
| 母亲的爱＝吞噬一切的漩涡；铁匠的欲望 `twisted, warped, and destroyed` 威洛 | `:89` |
| 三个动词连打（twisted／warped／destroyed） | `:89` ✔ |
| 心语「可辛西娅绝不会伤害我」 | `:92` |
| 狐狸舔脸＋`never lowered himself to such canine behaviour` | `:107` |
| 「我错了」排在嘴硬之后 | `:104` `I’m not wrong.` → `:113` `I’m wrong.` |
| 忘锁门、门铃响、辛克莱进店 | `:119`／`:122`／`:125` |
| 「店里的药水如同巫术」 | `:131` `akin to witchcraft` |
| 「我要找一个女巫」 | `:164` |
| 从空气抽湿、掌心聚起海蓝女巫之水 | `:152`／`:158` |
| 「这是你完好离开的最后机会」 | `:161` `This is your last chance to leave unscathed` |
| 后脑被重物击中、世界变黑 | `:170` |
| 「The world went dark」＝四个词 | `:170` `The world went dark.` ✔（4 词） |
| 醒来先热、呼吸灼肺 | `:186` `She was breathing in flames.`／`:198` `every inhalation singed her lungs` |
| 手腕被皮带与铁链吊在低梁上 | `:192` |
| 衣裙被脱走只剩睡裙 | `:195` `She wore only her shift` |
| 房间不比卧室大、雪松与尤加利香「不协调地愉悦」 | `:198` `incongruently pleasant` |
| 探向体内只剩雾和记忆 | `:201` |
| `stole` 而非 `blocked` | `:207` `stole every last drop` ✔ |
| 「somehow」是原文留白 | `:207` `had somehow constructed` ✔ |
| ch21「我的水变成了雾」的回收 | ch21 `:344` `my water turned to mist`（第一人称原话）✔ |
| 罗温在 ch20 讲过「平衡」（md:46） | ch20 `:126` `The goddess believes in balance. That includes balance between fated pairs.` ✔ |
| ch20 里罗温解释魔宠／灵魂交织（md:76） | ch20 `:53`／`:126` ✔ |
| 「全书对能力规则最清楚的一次说明」（md:44） | 全书 grep：`thoughts unless`／`read minds` 仅 `:65` 给出两条例外 ✔（其余 `ch06:95`／`ch20:68` 是提问或单句，未给规则） |
| 「打她后脑的那一下原文始终没交代出手者」（md:12） | 全书 `slammed/struck/knocked/hit her` 仅 `:170` 一处，ch24–ch27 无归属 ✔（§六 D） |
| 「全章唯一一次暴力发生」（md:84） | 全章只有 `:170` 一次物理暴力 ✔ |

---

## 三、错

| # | md 位置 | md 说法 | 反证 | 判据 | 判定 |
|---|---|---|---|---|---|
| E1 | `md:13` | 「辛克莱从 ch08 起就悬在背景里的名字**第一次当面对话**」 | ch10 `:146` `‘Mr Sinclair. I believe you were expecting me.’`（辛西娅）→ `:161` `‘I am here to ensure Lady Burrows’ safety.’`（海伦娜）→ `:170` `‘With relish, Mr Sinclair.’`（海伦娜）：海伦娜在辛克莱办公室已当面对他说话，且本章并非首次交锋 | (j) 跨章「第一次」已全书取证并被证伪 | **阻断（轻）** |
| E2 | `md:10` | 「辛克莱进店，用**口吃不清的腔调**夸店里的药水」 | 原文是吞词首 h 的伦敦土腔：`:125` `’oping`／`:131` `’eard`／`:149` `’ere`；ch10 `:156` `tinged with the accent of the rookery`。md:14 自己也写「用前置撇号标出口音」——两处口径不一 | 人物语言特征写错（口吃≠口音） | **阻断（轻）** |
| E3 | `md:34` | 「又用一个**摸鼻子的具体比喻**把‘确定’变成身体感觉」 | `:47` 是 `as clearly as this is the nose on my face`（“像我鼻子长在脸上”），**没有摸鼻子的动作** | (g) 引语外新增动作 | 提示 |
| E4 | `md:44` | 「能力的失控比她**承认的爱情**更早说出口」 | 本章她没有承认爱情：`:104` 是 `I’m not wrong.`、`:113` 是 `I’m wrong.`（承认“辛西娅不会伤害我”），全章无“爱”的自认 | 章级内容与原文不符（无据） | 提示 |
| E5 | `md:66` | 「**书中没有给出铁匠的动机细节**」 | ch21 `:266` `He knew of her powers. He knew, and he craved the riches they could bring.`——动机已给（贪图她力量带来的财富） | (j) 跨章否定断言须全书取证；已证伪 | 提示 |
| E6 | `md:84` | 「作者让魔宠先发声、**再挨击**」 | `:170` 被砸的是**海伦娜的后脑**：`something heavy slammed into the back of her head`；狐狸只是叫 | (h) 受事归属易读反 | 提示 |
| E7 | `md:104` | 「把**辛克莱的房子里**写成一次盗窃」 | 病句（“把…房子里写成”），且 `:207` 的主语是 `the Devil of Seven Dials` 与 `a room`，不是“房子里” | 表述不成句 | 提示 |
| E8 | `md:104` | 「读者至此才明白他**早就备好了对付她的东西**」 | `:164` 他只说 `I seek a witch`，未说针对她；`:207` 的 `somehow constructed` 是海伦娜的推断；ch25 `:92` 揭示那间是浴场对外营业的桑拿房（`a furnace blasted hot air through vents`），非为她专造 | (g) 引语外新增预谋事实 | 提示 |
| E9 | `md:104` | 「也为后面**罗温一线的解释**留口」 | ch24–ch27 的罗温只做救治与劝止（ch26 `:98`/`:113`/`:149`），**全书没有罗温解释这间屋子的段落**（§六 E） | 跨章预告无据 | 提示 |
| E10 | `md:11` | 「力量被剥夺直接推到**全书最低点**」 | ch26 `:38` 辛西娅中弹、`:98` 取弹、`:203` `And you got shot instead.`——危机量级更深 | 可核最高级（跨章）须 hedge | 提示 |
| E11 | `md:13` | 「并因巴斯之调离开（这一条在 ch24 **直接导致无人可求**）」 | ch24 `:71` 只说 `She went to Bath with Uncle Lachlan.`（去的是罗温）；同一章 Cynthia／Ellie／Thomas／Clio 都在行动，并非“无人可求” | 因果与范围放大 | 提示 |
| E12 | `md:13` | 「他的**来意仍未说明**」 | 他当面说了 `:164` `I seek a witch.`；真正未说明的是“要女巫做什么”——与 md:12 的自述（“说的是‘找一个女巫’”）口径不一 | 表述自相抵牾（可窄化） | 提示 |
| E13 | `md:14` | 「章末**三行**以触觉—嗅觉—内在感受的顺序收在悬念上」 | 顺序对（`:186` 热→`:198` 香→`:201`/`:204` 内在），但“三行”对不上物理行：`:186`–`:204` 是 5 个自然段、19 个物理行 | (f) 行数断言无据 | 提示 |

---

### 问答链底账（R4 归属核对用）

`:38` 叙述 → `:44` 海伦娜 → `:47` 拉克兰 → `:50` 叙述 → `:68` 海伦娜 → `:74` 海伦娜 → `:80` 海伦娜 → `:86` 海伦娜 → `:92` 海伦娜（心声）→ `:104` 海伦娜 → `:110` 海伦娜（心声）→ `:113` 海伦娜（心声）→ `:119` 叙述 → `:122` 海伦娜 → `:125` 辛克莱 → `:128` 海伦娜 → `:131` 辛克莱 → `:134` 海伦娜 → `:137` 辛克莱 → `:146` 海伦娜 → `:149` 辛克莱 → `:161` 海伦娜 → `:164` 辛克莱 → `:167` 叙述 → `:170` 叙述 → `:186` 起海伦娜独白／内感知。

⇒ md 的 9 块说话人**零错**：`md:34` 明确标“他说”（拉克兰），`md:76` 明确标“狐狸并没有说话”。

### 块序单调性

`35 < 47 < 65 < 86 < 89 < 107 < 170 < 201 < 207` ⇒ **9 块 0 调转**。

---

## 四、R4 逐块对应表

| 块 | md | 原文 | 动词主语 | 受事 | 归属方向 | 结论 |
|---|---|---|---|---|---|---|
| 1 | :18 | `:35` | Helena（couldn’t stop／took on）／her heart（jumped／plummeted） | Cynthia／班次／心 | 「她的」思念 ✔ | 对应 ✔ |
| 2 | :28 | `:47` | We（’ve found）／It（’s Sinclair）／I（canna prove） | 凶手 | 说话人＝拉克兰 ✔；md:34「摸鼻子」⇒ **E3** | 对应 ✔ |
| 3 | :38 | `:65` | Her magic（had been malfunctioning）／she（could ignore／delved） | 别人的念头／秘密 | 能力主体＝海伦娜 ✔；md:44「承认的爱情」⇒ **E4** | 对应 ✔ |
| 4 | :48 | `:86` | I（won’t risk／won’t be blinded） | 变成母亲那样／真相 | 自誓主体＝海伦娜 ✔ | 对应 ✔ |
| 5 | :58 | `:89` | Her mother’s love（had been）／the blacksmith’s desire（had twisted） | 一切／Willow | 施事＝铁匠、受事＝威洛 ✔；md:66「动机」⇒ **E5** | 对应 ✔ |
| 6 | :68 | `:107` | He（stretched／licked）／he（had never lowered） | 脖子／她的脸／他自己 | 施事＝哈姆雷特 ✔ | 对应 ✔ |
| 7 | :78 | `:170` | Hamlet’s snarl（sharpened）／something heavy（slammed）／The world（went dark） | 她的后脑 | 受事＝海伦娜 ✔；md:84「魔宠…挨击」⇒ **E6** | 对应 ✔ |
| 8 | :88 | `:201` | she（reached）／The cool rush（was gone） | 核心／力量 | 「她的」力量 ✔ | 对应 ✔ |
| 9 | :98 | `:207` | Her element（was）／It（was）／the Devil（had constructed） | 水／房间 | 「七铃区的魔鬼」＝辛克莱 ✔；md:104 三处⇒ **E7/E8/E9** | 对应 ✔ |

---

## 五、形态层

| # | 检查项 | 结果 |
|---|---|---|
| 1 | 导航 5 项齐全 | ✔ |
| 2 | 9 块格式 `> **原句 N:**` 连续、外层 `"…"` 首尾闭合 | ✔ 9/9 |
| 3 | 四子项齐全（含「读者视角提示」） | ✔ 9/9 |
| 4 | 词表标准 Markdown 表格、9/9/6＝24 行、词头全部在正文命中 | ✔（24/24：`impenetrable` `:41`、`infuriating` `:41`、`malfunctioning` `:65`、`delved` `:65`、`lethal` `:50`、`incongruently` `:198`、`suffocating` `:186`、`geyser` `:198`、`aquamarine` `:158`、`acerbic` `:38`、`baleful` `:38`、`standstill` `:41`、`hackles` `:77`、`whirlpool` `:89`、`singed` `:198`、`unscathed` `:161`、`rasp` `:198`、`tinkled` `:119`、`ledger` `:71`、`aisle` `:98`、`cuffs` `:192`、`beam` `:192`、`benches` `:198`、`mop` `:62`） |
| 5 | 块数档位：9 vs `block_target=[3,5]` ⇒ **超限** | 提示型（rc 仍 0）⇒ **禁止增第 10 块**，补漏只进导航或现有块 |
| 6 | `aquamarine` 词性 | 词表给「海蓝色的」（形容词），但 `:158` `a swirl of aquamarine` 是**名词**（海蓝色／蓝绿色）⇒ 提示，建议释义补「（此处作名词）海蓝色」 |
| 7 | `unscathed` 例句 | `‘This is your last chance to leave unscathed, Sinclair.` **缺收尾 `’`**（全书同类体例待统一）⇒ 提示 |
| 8 | H1 | `# 23. Chapter Twenty-Three` ✔（与 ch22 同形） |

---

## 六、实跑取证

**A. 本章推广残留**
```
$ /usr/bin/grep -ci lokepub notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/text/ch23_chapter_23.txt
0
rc=1
```

**B. 辛克莱首次出现的章（md:13「从 ch08 起」）**
```
$ for f in text/ch0[1-7]*.txt; do n=$(/usr/bin/grep -ic "sinclair" "$f"); echo "$f $n"; done
text/ch01_chapter_1.txt 0
text/ch02_chapter_2.txt 0
text/ch03_chapter_3.txt 0
text/ch04_chapter_4.txt 0
text/ch05_chapter_5.txt 0
text/ch06_chapter_6.txt 0
text/ch07_chapter_7.txt 0
（rc=0）
$ /usr/bin/grep -n "Sinclair" text/ch08*.txt | head -1
41:‘The Devil of Seven Dials. Damien Sinclair.’ He spat the words like poison.…
```

**C. 「第一次当面对话」（E1）**
```
$ /usr/bin/grep -n "Mr Sinclair\|Sinclair\." text/ch10*.txt
59:…‘Mr Sinclair has strict rules of confidentiality…
62:…‘And what happens when Mr Sinclair is displeased?’…
146:‘Mr Sinclair. I believe you were expecting me.’…（辛西娅）
170:‘With relish, Mr Sinclair.’ Helena’s voice was cool water rushing over granite stones.
（rc=0）
$ /usr/bin/sed -n '161p' text/ch10*.txt
‘I am here to ensure Lady Burrows’ safety.’ Helena’s footsteps echoed loudly…
```

**D. 击倒的出手者（md:12 成立 ＋ E6）**
```
$ for f in text/ch2*.txt; do /usr/bin/grep -in "slammed\|struck\|knocked\|hit her\|blow to\|back of her head" "$f"; done
text/ch23_chapter_23.txt:170:Hamlet’s snarl abruptly sharpened into a yelp of fear as something heavy slammed into the back of her head. The world went dark.
（ch21/ch22 的命中是无关句；ch24–ch27 无命中；rc=1）
```

**E. 巴斯与「罗温的解释」（E11／E9）**
```
$ /usr/bin/sed -n '68,72p' text/ch24*.txt
‘Does Aunt Rowan know?’
‘She went to Bath with Uncle Lachlan. Something about a friend there who needed her help.’…
$ for f in text/ch2[4-7]*.txt; do echo "--- $f"; /usr/bin/grep -in "Rowan" "$f"; done
--- ch24：:68 :213（:213 是童年故事，非解释）
--- ch25：（无命中）
--- ch26：:62 :65 :68 :92 :98 :101 :113 :119 :122 :125 :146 :149 :161 :276 :279 :354 :369 :399 :414 :417 :432 :435（全为救治／劝止／回巴斯）
--- ch27：（无命中）
（rc=1）
$ /usr/bin/sed -n '92p' text/ch25*.txt
The final sauna was separated from the rest of the rooms. Tiled on the outside to maintain utmost heat, a furnace blasted hot air through vents into the cedar-planked interior.…
```

**F. 逐字（R2 ＋ 两把独立尺子）**
`chapter.sh --json`：`verdict ok`、9 块全 `ok`、`segment_miss=0`、`issues` 全空；`/tmp/hx_md_frag.py` → `checked=9 BAD=0`；R1 底稿 `/tmp/hx_frag_check2.py` → `checked=132 BAD=0`。

---

## 七、悬置

| # | 悬置点 | 取证 |
|---|---|---|
| U1 | 打她后脑的人是谁（是否是辛克莱本人） | 全书只有 `:170` 一句；ch24–ch27 未追认；不裁决 |
| U2 | 那间屋子如何抽走她的水 | 本章只写 `somehow constructed`；ch25 `:92` 只交代它是 60°C 干热桑拿房；机制未解释 |
| U3 | 辛克莱要女巫做什么 | `:164` 只到 `I seek a witch` 为止；全书后文未由他本人补述 |
| U4 | 他进店前是否已知她是女巫 | `:131` 用“药水如同巫术”试探、`:164` 才点明；本章不明说他是冲她而来 |
| U5 | 「quality of company I keep」（`:137`）所指为谁 | 无下文；不据此推人脉 |
| U6 | 盘点打翻的三瓶具体是哪三款 | `:62` 只说 `three of the anti-inflammatory potions`，款式未列 |
