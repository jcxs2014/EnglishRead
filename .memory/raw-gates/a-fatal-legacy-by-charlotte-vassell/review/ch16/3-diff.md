# 3-diff · ch16 对账（漏 / 编 / 错）

> 审章：notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch16 isolde burrell denies the letters.md
> 唯一权威源：text/ch16_16.txt（13,453 字符）
> 区间＝原文**字符区间**（`start-end`，闭区间，半开取尾）。
> md 行号＝md 文件行号（L11 导航一句话概括 / L12 视角 / L13 线索结构 / L14 人物弧线 / L15 叙事手法 / L19-80 九个引语块 / L82-125 词汇表 / L129 一句话总结）。

**机器层先行结论**：`bash scripts/chapter.sh … --json` → 退出码 0，`verdict=ok`；9 引语 / 9 块；`segment_miss=0`、`struct_bad=0`、`empty_quote=0`、`keyword_bad=0`、`cjk_low=0`。
`check_vocab.py`（全书跑，筛 ch16）：FAIL 0、WARN 0（本书 26 条 WARN 全在其他章）。
`corruption_scan.py`（书目录跑，筛 ch16）：无命中。
**⇒ 下面每一条都是机器结构上查不了的：漏 / 编 / 错 / 对应 / 说话人。**

---

## 一、漏（素读有、md 无）

### 漏-1　Matt 那条同名者线索整条缺失　【阻断】
- 原文①　`ch16:661-707`：「‘Isolde Wallis, resident of Marlow,’ Matt said, getting his phone out and searching for the postcode. ‘You all right?’」
- 原文②　`ch16:10599-10871`：「‘My Isolde was a mum of three under three who laughed in my face when I asked if she had been sending love letters to Digby Combe-Watson. She was at a family wedding all weekend. Her mum was there trying to wrangle a toddler onto a potty and alibied her there and then.’」
- md 侧：全文 **无任何一处**引用这两段。全书检索：`Wallis` 命中 1 次——只在 L125 词汇表「postcode」的例句里；`mum of three` 0 次、`wedding` 0 次、`Issy`（Matt 的妈妈）/ 母亲作证 0 次。
- 判定：本章是**两个同名 Isolde 并行**的结构（原文 `ch16:208-213` 蔡厄斯自己说「That leaves one each for me and you」＝Burrell 与 Wallis 各一）。md 的 9 个引语只落在「Caius–Isolde 家对话」与「事故室 Caius 发言」两处，**Matt 那一半从未进入正文**。这不是取舍（md 未写任何取舍理由），是整条线掉了。
- 附带影响：见 **错-1**（md 反而宣称这条线存在）。

### 漏-2　本章三处关键推论/数字未进任何引语块　【提示】
- 原文①　`ch16:12302-12367`：「‘Both female, under thirty-five and living in London. That’s it.’」——本章唯一的**凶手画像判据**，且含全书唯一一处数字 `under thirty-five`（md 全文 0 次 `thirty-five`）。
- 原文②　`ch16:12401-12499`：「The killer, “fake Isolde”, planned this out. She’s chucked two red herrings at us to slow us down.」——md 把 `red herrings` 只做成 L96 的一个**词汇表词条**，分析层一次都没用。
- 原文③　`ch16:12666-12694`：「Copying Willow is practical. It’s a costume in case any of the neighbours see her.」——全章**唯一**解释「凶手为什么长成 Willow 那副样子」的句子，md 正文 0 次 `costume`。
- 判定：三条都是「本章为什么这样写」层面可用的硬料，且①是唯一的量化判据。md 的 9 个引语未覆盖。

### 漏-3　Andy 问询段与关系细节整段无引语块；Andy 在人物弧线里缺席　【提示】
- 原文①　`ch16:7410-9014`（Andy 在警局的口供）：「‘I walked to Issy’s about 9 p.m., I guess.’…  Uber → Whipps Cross（`ch16:8529-8542`）…『We were together for thirteen years. We first met in Freshers. … We outgrew each other in many senses, but we’ll always be connected.’』（`ch16:8968-9014`）
- 原文②　`ch16:6680-6711`（Keisha 证词 + 冻豌豆）：「another solicitor from his firm had accompanied her」/「Keisha stated that she was out running with Isolde who had landed funny on a dodgy paving stone… a bag of frozen peas」（`ch16:6844-6882`、`ch16:6986-7011`、`ch16:7093-7113`）
- md 侧：9 个引语无一落在这一段；`thirteen years` 0 次、`Freshers` 0 次、`Whipps Cross` 0 次、`6.30` 0 次、`9 p.m.` 0 次。L14 人物弧线只写 Isolde 与 Caius，**Andy 与 Keisha 无位置**。
- 判定：不算「关键转折」缺失（其功能已由原句 7 概括），但本章唯一的**人物关系实证**（十三年、互留备用钥匙、仍是好朋友）没被写下。

---

## 二、编（md 有、原文无）

### 编-1　「周二这一天的开头」——凭空出现的日期　【阻断】
- md 侧　L15 导航·叙事手法：「…也**把这一章钉在周二这一天的开头**。」
- 原文侧：`ch16_16.txt` 全文**没有任何 weekday**；本章唯一 weekday 是 **过去时**的伤夜 `ch16:3241-3266`「Friday evening after work」（即 Isolde 断足那一晚，不是本章时点）。**全书 `text/` 30+ 章逐章检索 Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday，Tuesday 出现 0 次**（相邻章 ch13 只有笑谈「Monday Funday」，ch15、ch17 也没有）。
- 判定：凭空断言 + 全书无据 ⇒ 阻断。（本章时点在原文中根本不可考。）

### 编-2　「我真不觉得他很特别」——引号内的句子原文没有，且语义相反　【阻断】
- md 侧　L14 导航·人物弧线：「…走到**「我真不觉得他很特别」**的那句否认…」
- 原文侧　`ch16:5340-5370`：「‘I really don’t think I have.’」（= 我真不觉得自己**见过他**）；`ch16:5398-5459`：「‘I’d remember a moustache like that. **He’s very characterful.**’」（= 他**很有辨识度**）。
- 判定：md 用引号把一句**不存在的台词**归给 Isolde，且把原文的正向判断（他很有辨识度）反转成「不觉得他很特别」。本块正文（原句 5，L47-52）自己译得是对的（「他很有辨识度」），与导航自相矛盾 ⇒ 阻断（改一处即可解）。

### 编-3　「三份证词（…哥哥 Richard 的同事…）」——第三位根本没有作证　【提示】
- md 侧　L12 导航·视角：「到警局问询室里**三份证词**（朋友 Keisha、**哥哥 Richard 的同事**、前男友 Andy）」
- 原文侧　`ch16:6680-6711`：「As it turned out her brother Richard was a solicitor, and **another solicitor from his firm had accompanied her.**」（只是**陪同**，全文无其证词）；作证的只有 Keisha（`ch16:6844-6882`）与 Andy（`ch16:7410-9014`）。
- 判定：把「陪同人」算成第三份证词 ⇒ 多出一份原文没有的证词。提示级（导航计数措辞，改正为「两位作证者 + 一位陪同的同行」即可）。

---

## 三、错（两边都有但不一致）

### 错-1　「两条同名者的线索在这间客厅里正面相撞」——地点与结构都不符　【阻断】
- md 侧　L11 导航·一句话概括：「…**两条同名者的线索因此正面撞上**。」／L129 一句话总结：「…**两条同名者的线索在这间客厅里正面相撞**，最后把全案压到一个尚未查清的邮政信箱上。」
- 原文侧：客厅（`ch16:967-6508`）里**只有 Caius 与 Isolde Burrell 两人**，没有第二条线；两份说法真正撞车的地方是**事故室**——`ch16:11221-11285` Matt：「‘Those are the facts that Amy listed out from Isolde’s letters.’」＋ `ch16:11288-11601` Caius：「‘Exactly, but it couldn’t have been her…’」；另一条同名者线（Matt 的 Wallis）则在 `ch16:661-707`＋`ch16:10599-10871`。
- 判定：无论把「两条同名者」读成（Burrell vs Wallis）还是（信里 Isolde vs Burrell），「在这间客厅里」都不成立；而前者那一条在 md 正文里根本不存在（= **漏-1**）。md 自己的 L15 又说「章末用…邮政信箱收束」，与 L129「收在这间客厅里」自相矛盾 ⇒ 阻断。

### 错-2　「冰箱里的冷冻豌豆」　【提示】
- md 侧　L15 导航·叙事手法：「被唱片机、拐杖、侧柜、**冰箱里的冷冻豌豆**这类小市民细节包住」
- 原文侧　`ch16:7093-7113`：「…had sat her down on her sofa with **a bag of frozen peas**.」（一袋冻豌豆；**原文没有冰箱**；且这是 Keisha 证词里的转述，不在客厅场景内）
- 判定：细节被加码（冰箱）／场景被挪进客厅。提示级。

### 错-3　「三个字就把问题挡了回去」——计数与引语、与 md 自己的译文都不符　【提示】
- md 侧　L37（原句 3·为什么这样写）：「全章最短的一次否认，**三个字**就把问题挡了回去」
- 原文侧　`ch16:3683-3693`：「‘No, why?’」——英文 2 词 8 字母；md 自己的 L35 中文理解把它译成「**没有，怎么了？**」（六字）。
- 判定：数字与引语、与本块自译都不吻合。属修辞性计数、不涉情节事实，故记提示；建议改「三个字」→「一句」（或「两个字」）。

### 错-4　「他低头看了看衬衫有没有沾上墨水」　【提示】
- md 侧　L77（原句 9·中文理解）：「他低头看了看衬衫**有没有沾上墨水**」
- 原文侧　`ch16:13242-13277`：「Caius checked his shirt for **a stain**.」（只说「污渍」，未说是墨水；墨水在嘴唇上是咬笔造成的，`ch16:12880-12903`「Caius chewed on the pen. It leaked and he got ink on his lip」）
- 判定：md 自己在 L79 的「为什么这样写」写对了（「咬笔尖时墨水沾到嘴唇那一幕的回声」），前后不一致。提示级。

### 错-5　「她盯着照片看了很久」　【提示】
- md 侧　L49（原句 5·中文理解）：「她盯着照片**看了很久**」
- 原文侧　`ch16:5371-5397`：「She **peered** at the picture.」（只有「端详」，无时长）
- 判定：加了个原文没有的时长。提示级。

### 错-6　「对草莓严重过敏」　【提示】
- md 侧　L56（原句 6·中文理解）：「…**严重**过敏」
- 原文侧　`ch16:11182-11216`：「is allergic to **bloody** strawberries」（bloody 是语气词，不是「严重」）
- 判定：程度词加码。提示级。

### 错-7　「最后收在事故室的白板前」　【提示】
- md 侧　L12 导航·视角：「…**最后收在事故室的白板前**。」
- 原文侧：白板出现在 `ch16:12368-12399`（「Caius stared at the whiteboard.」，在「共同点」那段之后、并非章末）；本章真正收尾是 `ch16:13230-13452`（Caius 叫 Matt 去追邮局／PO Box）。
- 判定：章末锚点错；且与 md 自己 L15「章末用…邮政信箱收束」矛盾。提示级。

### 错-8　「确认她就是那几封信的原型」——把两位警探的推断写成既定事实　【提示】
- md 侧　L129 一句话总结：「…**确认**她就是那几封信的原型、却不是写信的人」；L63（原句 7·中文理解）：「**事实完全对得上，但不可能是她**」
- 原文侧：这是两位警探的推断链，不是章内定论——`ch16:11221-11285`（Matt：「Those are the facts that Amy listed out from Isolde’s letters.」）→ `ch16:11288-11601`（Caius：「Exactly, but it couldn’t have been her…」）→ `ch16:11605-11646`（Matt：「So someone used her life as the backstory for this “fake Isolde”.」）→ `ch16:11675-11707`（Caius：「That’s what it looks like to me.」）。
- 判定：结论本身正确，但按「同名者两份陈述只是双方各自说法」的要求，md 应写成**两位警探的推断**而非「确认／事实完全对得上」。提示级。

### 错-9　「可他们想从他身上得到什么？」——Matt 的话被放进 Caius 的话里　【提示】
- md 侧　L77（原句 9·中文理解）：「**「可他们想从他身上得到什么？」**他低头看了看衬衫…」
- 原文侧　`ch16:13173-13227`：「‘**They must have wanted something from him,’ Matt said.**」（这是 **Matt** 说的）＋ `ch16:13230-13255`：「‘**But what?**’ Caius checked his shirt for a stain.」（Caius 说的只是「那……要什么？」）
- 判定：md 用引号把**Matt 的台词**写进 Caius 那一轮。上下文可推知，语义不误，但引号＝逐字归属的场合会被误引。提示级（建议写成「他追问：他们想从他身上得到什么？」，把引号去掉）。

---

## 四、本章专项三问的自查结果（对应 md 侧）

| 专项 | 结论 | 依据 |
|---|---|---|
| ① 引语是否跨话轮拼接 | **无**。9 条引语全部是原文**连续区间**（`292-628`/`2783-2967`/`3683-3727`/`4943-5231`/`5340-5459`/`10969-11218`/`11288-11601`/`11787-12245`/`13230-13452`），**无 `…`**，无「隔行缝两段」。原句 4、原句 5、原句 9 把同一说话人的两段话连同中间的叙述一起收进来（同一人、不跨话轮）。 | 逐条 `find()` 全等命中 |
| ② 说话人是否写对 | **引语层无错**（原句 1/2/6/7/8/9＝Caius 或 Isolde，均与原文一致；原句 2/3/4/5＝Isolde）。**分析层 1 处越界**：错-9（Matt 的台词被引号归给 Caius）。 | 见错-9 |
| ③ 「同名者两份陈述」是否被写成事实 | **是，两处**：md 写成既定事实（错-8），并把 Matt 那一方的陈述**整条丢掉**（漏-1），只留下 Caius 一方，再由 L11/L129 宣称「两条同名者的线索…正面相撞」（错-1）。 | 见漏-1 / 错-1 / 错-8 |

---

## 五、机器层未覆盖、本次人工补做的检查

- 词汇表 27 条例句：`check_vocab.py` 全书跑 ch16 FAIL 0 / WARN 0；另逐条 `grep -F` 本章 `text/` 均命中 1 次（`geo-social`/`metatarsal`/`orthopaedic`/`intelligentsia`/`comedown`/`watertight alibi`/`catfishing`/`nefarious`/`red herrings`/`crutches`/`sideboard`/`substitute`/`moustache`/`ballerina`/`gallantly`/`amicable`/`backstory`/`solicitor`/`ex-boyfriend`/`sofa`/`school teacher`/`sprain`/`X-ray`/`CCTV`/`marking`/`civil smile`/`playlist`/`postcode`）。分档无注水信号。
- 视角声明核对：L12 声明「第三人称限知，紧贴 Caius」。多数段落确实挂在 Caius 的感官上（`ch16:1967-2015` 行走靴与拐杖、`ch16:2096-2121` 长金发与录像里短鲍勃头的对照、`ch16:2161-2196` 侧柜与唱片机）。但存在**两处非 Caius 限知的内心叙述**：`ch16:5936-6013`（Isolde 心里觉得自己「不够热」到配得上当受害者）与 `ch16:6064-6120`（「Isolde was then in turn duly appalled at her own vanity」——她为自己的虚荣而骇然，Caius 无从知晓）。另有 `ch16:8030-8084`（Andy 的「warm brown eyes appeared bemused」是 Caius 的观察，属可接受的外显描写）。⇒ 视角声明**基本成立但不完全**，记提示（见 4-verdict.md）。
