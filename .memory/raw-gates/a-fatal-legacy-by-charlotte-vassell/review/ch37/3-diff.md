# ch37 · R3 对账（漏 / 编 / 错）

- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch37_37.txt`（全文 8539 字符，142 行）
- 被审：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch37 robbie takes over the case.md`
- 字符区间写法：`text/ch37_37.txt:<行号>`，括号内为字符区间 `[起, 止)`（与 `1-suread.json` 同口径）

---

## 一、漏（原文有、md 无）

### 漏-1【阻断】Matt 的下一步报告：35 号黄房子、Fenella 同意拆门 —— 全章高潮的「因由」在 md 里完全没有

**原文（text/ch37_37.txt:101，区间 [5438, 6080]）**

> ‘I went round to number 35, the yellow house on the map, last night. They’ve got really good security. State of the art. They’ve not been broken into but we could always ask to access it just in case anyone attempted to and aborted when they realised they’d be visible. It seems highly likely that they would try to get access to their basement too,’ Matt said, wrinkling his nose. ‘Caius requested permission for us to take the door down to the basement off in the Horatio Combe Institute. Digby’s mother Fenella is the only other surviving trustee and she agreed this morning. I’m going to go over there now and will liaise with forensics.’

**md 侧：查无**

- 7 个引语块无一覆盖该段（引语区间见 `2-machine.json`：123–432 / 1442–2116 / 2691–2913 / 3429–4280 / 4381–5350 / 6734–7553 / 8410–8538，**无 5438–6080**）；
- 导航五项（`ch37 …md:11-15`）无一提及 35 号、Fenella、拆门许可；
- 结尾「一句话总结」（`:116`）写「法证队凿开百年油漆、拆下那扇封了几十年的地下室门」，但**拆门的授权来源（Fenella 今早同意）从未出现**，因果链断在这里；
- 唯一残留痕迹在词汇表：`security cameras` 一条的例句取自同一场景（`He thought there was an off-chance that their security cameras may have caught the burglar.`），说明作者知道这段内容，只是分析层没写。

**后果**：读者读完 md 不知道 (a) 下一条现场线是 35 号（黄房子）的地下室；(b) 研究所那扇门是被谁批准拆的；(c) 本章结尾法证队拆门这一动作的授权来源。

### 漏-2【提示】白板颜色图例与「黄房子＝35 号」的对应

**原文（text/ch37_37.txt:53，区间 [2389, 2461]）**

> Amy began. ‘Red means a death, orange means a break-in, the yellow one—’

**原文（text/ch37_37.txt:56–62，区间 [2464, 2598]）** —— 该解说**被 Robbie 打断且未讲完**：

> ‘They’re evenly spaced,’ Robbie said. … ‘Is there any significance to that?’ Robbie asked.

**md 侧**：导航「线索结构」写「Amy 再补上白板地图」（`:13`），但分析层从未给出颜色图例，也从未说明「黄色 = 35 号」；同时 md 把这次被打断的解说写成了「补上」（完成态），而原文里 Amy 的话停在「the yellow one—」。

### 漏-3【提示】Robbie 主动要求同去现场 + Amy 如释重负

**原文（text/ch37_37.txt:104–107，区间 [6083, 6332]）**

> ‘Sure,’ Robbie said, sitting down at Caius’s desk. He’d been told. Amy scowled at him from across the desk. ‘I tell you what, Matt, I’ll come with you. Get a feel for the crime scene.’ / ‘That’s not a bad idea,’ Amy said, failing to hide her relief.

**md 侧**：「人物弧线」（`:14`）只写到抢话—僵持—道歉，**没有记录 Robbie 主动要求同去现场、Amy 松口气**这一转折（这也是本章「Robbie 接手」的实际动作）。另同段 `He'd been told.`（Robbie 已从上级处听说 Matt 的去向）亦无对应。

---

## 二、编（md 有、原文无）

### 编-1【提示】导航称 Robbie 对「这家博物馆」带着旧账 —— 原文无此依据

**md（`:11`）**

> ……他们知道的比他多、缺的比他清楚，而他本人对凯厄斯、连带对这家博物馆，还带着一笔旧账与成见。

**原文**：本章只给出 Robbie 对 **Caius** 的态度（`'He wasn't looking forward to the next few weeks with these two. At least Caius wasn’t there. He found him intimidating at the best of times.'`，text/ch37_37.txt:29，区间 [565, 760]）与对 Billy 的袒护（`:126`，区间 [6612, 6731]）。**博物馆/研究所的旧账（降神会、异教神庙、遗失的第二十二号日记、封了几十年的地下室）全部是 Amy 转述给 Robbie 的**，不是他自带的。

**取证（Robbie 是本书新人物，ch37 之前全书无他）**

```
/usr/bin/grep -c "Robbie" text/ch0*.txt text/ch1*.txt text/ch2*.txt text/ch3[0-6]*.txt | /usr/bin/grep -v ":0$"
→ 无输出；cmd_exit=1（ch01–ch36 全部 0 命中）
```

### 编-2【提示】「跟他僵持」的对象指代含混，按字面读会读成 Robbie 与 Matt

**md（`:14`）**

> ……在 Matt 点破之后**跟他**僵持几秒

**原文（text/ch37_37.txt:74，区间 [2916, 3063]）** —— 僵持发生在 Robbie 与 **Amy** 之间：

> Robbie stared at Amy. She stared back. They reached a stalemate. Robbie broke the silence. ‘Sorry, Amy. Do continue.’

前一句「把 Amy 的讲述掐断」已把代词锚在 Amy，故“他”按最近的先行词应指 Amy；但字面上离 “Matt 点破” 最近的是 Matt，属指代歧义（非事实错误，故列提示）。

### 编-3【提示】「连声道歉」与原文的一次道歉不符

**md（`:14`）**

> ……才低声连声道歉

**原文（text/ch37_37.txt:74 与 :86）**：该处只有一次道歉（`'Sorry, Amy. Do continue.'`）；另一次 `'Sorry, um.'` 在**之后**、Amy 说完 Benedict 醉酒的另一轮对话里（区间 [3338, 3390]），两次并不连声。

---

## 三、错（两边都有但不一致）

### 错-1【阻断】「作者不写安米的情绪」—— 与本章原文直接矛盾，且与本文件词汇表自相矛盾

**md（`:37`，原句 3 的「为什么这样写」）**

> 作者不写安米的情绪，而让 Matt 用一句“翻译”把它讲出来——这既是同事间的护短，也是一份诊断……

**原文（text/ch37_37.txt:65，区间 [2601, 2652]）** —— 作者**恰恰写了**安米的情绪：

> ‘I’m …’ Amy let out an exasperated, guttural groan.

**自相矛盾**：本 md 自己的词汇表 `guttural` 一条（`:92`）的例句正是这一行：

> ‘I’m …’ Amy let out an exasperated, guttural groan.

即 md 同时主张「作者不写安米的情绪」，并在词汇表里引用了作者写安米情绪的原句。

### 错-2【阻断·逐字】原句 6 的引语不是原文的逐字串：漏掉收尾的右单引号

**md（`:54`）**

> "Three things. … Not because she’s good at her job, but because she’s a person. Matt got in the car."

**原文（text/ch37_37.txt:129，区间 [6734, 7553]）**

> …Not because she’s good at her job, but because she’s a person.’ Matt got in the car.

**核验（独立实现，非门禁路径）**

```
最长逐字前缀 = 796 / 817 字符；其后 md 为 " Matt got in the car."，原文为 "’ Matt got in the car."
```

即 md 在 `a person` 之后**吞掉了 `’`**（右单引号），使该引语块不再是原文的一段连续逐字串。

**范围核验（全书）**：对本书 54 章全部 391 个引语块做同样的逐字子串比对，**非逐字者仅此一处** ⇒ 不是本书体例，是本章孤例。

> ⚠️ 门禁未捕获：`2-machine.json` 对原句 6 判 `"ok": true`（其 `segments[0].text` 只展示前 100 字符，属前缀窗口口径）——本条即「机器绿 ≠ 逐字对」的实例。

### 错-3【提示】原句 2 把 `former comedy enfant terrible Jimmy Jones` 译成「前喜剧红星」

**md（`:28`）**

> ……其中一起导致前喜剧红星 Jimmy Jones 意外身亡。

**原文（text/ch37_37.txt:44，区间 [1442, 2116]）**

> …the accidental death of former comedy enfant terrible Jimmy Jones.

`enfant terrible` ＝「被宠坏的麻烦人物／难缠角色」，不是「红星（star）」；md 自己的词汇表（`:80`）释义也写着「（法语）被宠坏的麻烦人物；难缠角色」——同一文件里两种口径。

### 错-4【提示】原句 6 把种族辱称降级成「骂了一句」

**md（`:56`）**

> ……其三，Matt 上班第一周就看见 Billy 在警局停车场里从车钥匙上吸古柯碱，**被发现后还骂了他一句**、威胁说会毁掉他

**原文（text/ch37_37.txt:129，区间 [6734, 7553]）**

> He called me a “chink” when he realised I saw and said he’d ruin me if I told.

原文是种族辱称（“chink”）。md 在同块第一条里把同类用词译作「贬称」（`用一个贬称说他祖父`）、关键词也列了 `slur`，唯独第三条写成「骂了他一句」，把「辱称」降级为一般斥骂，并丢掉本章「血统/来源」这条与第一条（Caius 的 background）呼应的线索。

### 错-5【提示】原句 6「为什么这样写」把「并非因为她工作做得好」的逻辑反写成「你工作不行」

**md（`:58`）**

> 末了还把“你工作不行但你是个人”这句刺人的公平摆出来。

**原文（text/ch37_37.txt:129）**

> treat Amy with respect. Not because she’s good at her job, but because she’s a person.

**同块中文理解（`:56`）口径正确**：「不是因为她工作做得好，而是因为她是一个人」。「你工作不行」是「因为她做得不好」的断言，与原文的「并非因为她做得好」不是同一命题。

### 错-6【提示】原句 4「为什么这样写」把「传说/取证路线」说成「作案动机」，与同块读者视角提示自相矛盾

**md（`:44`）**

> 作者让地貌本身变成作案动机：不是“谁恨谁”，而是“哪几个点必须同时在场”。

**md 同块读者视角提示（`:45`）**

> 记住“四个正方位点围成一个中心”这个结构：它同时是传说，也是**往后取证要走的那条路线**。

**原文（text/ch37_37.txt:89，区间 [3393, 4280]）**：本块只交代降神会、罗盘四方位点、修道院与异教神庙、160 年前发现废墟的传闻；「凶手为拿到日记」这一**作案动机在原句 5**（区间 [4355, 5350]）。本块引语里没有「必须同时在场」这一说。

### 错-7【提示】同一警衔两种译名

**md（`:21`）** 作「总警监」；**md（`:24`）** 作「警长」：

> 也解释了**警长**离开办公室时为什么忽然想去算那块地值多少钱。

原文为 `the Chief Superintendent`（text/ch37_37.txt:32，区间 [763, 1032]）；md 词汇表 `Superintendent` 一条（`:75`）释义为「（英国警衔）总警监」。

### 错-8【提示】原句 1「他父亲」指代有歧义（本条牵涉本章专属判据，须防走样）

**md（`:21`）**

> Caius 已经向他报告，这些案子发生在他父亲持有租赁权的地皮上

**原文（text/ch37_37.txt:23，区间 [123, 432]）**

> …as Caius has flagged with me that these crimes happened on property that **his father** owns the leasehold on.

原文的先行词是 Caius（`Caius has flagged … his father`）；md 的中文里「他」紧跟在「Robbie Eastley」「Caius 已经向他报告」之后，读者有可能读成 Robbie 的父亲。**交接理由不得走样**，建议写成「凯厄斯的父亲」。

### 错-9【提示·低】结尾把「封了几十年」与「百年油漆」并到门上

**md（`:116`）**

> 法证队凿开百年油漆、拆下那扇封了几十年的地下室门

**原文**：门上的是 `the century’s thick layer of paint`（text/ch37_37.txt:139，区间 [7568, 8407]），「sealed up for decades」说的是 `the door to the basement which has been sealed up for decades`（text/ch37_37.txt:95，区间 [4355, 5350]）。原文该从句的先行词本身有歧义（门 or 地下室），md 的并写属可接受压缩，故列提示不列阻断。

---

## 四、R3 小结

| 单子 | 阻断 | 提示 |
|---|---|---|
| 漏 | 1（漏-1） | 2（漏-2、漏-3） |
| 编 | 0 | 3（编-1～编-3） |
| 错 | 2（错-1、错-2） | 7（错-3～错-9） |

**阻断型合计 3 条**：漏-1、错-1、错-2。
