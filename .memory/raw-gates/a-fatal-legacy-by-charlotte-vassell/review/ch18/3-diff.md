# 3-diff.md · 第 18 章《A Fatal Legacy》对账（漏 / 编 / 错）

- 被审：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch18 mel tests the death scent samples.md`（HEAD `6f4fa513`，14560 字节，103 行）
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch18_18.txt`（4,029 字符）
- 区间记法：`ch18:[起,止]`＝源文字符区间（换行计 1 字符）
- 素读底稿：同目录 `1-suread.json`（**先素读、后开 md**，顺序合规）
- 机器层：`2-machine.json`（派工书给的文件名，退出码 0 但 `chapters: 0`——沉默假绿）、`2-machine-chapter.json`（**真实路径**，退出码 0，`verdict: ok`，6 块 / 7 片段 / 0 MISS）、`2-machine-book.json`（整书跑，退出码 0：54 章 / 块数中位 7 / 区间 [5,10] / nav 全为 5 / H1 形全为 `N.`）
- 编号说明：本版按**最终分档**重排编号（旧 D-2 的 Venetia 半条已拆出为 D-2b，D-4 由阻断降为提示）。

> **文件名对账（影响复现）**：派工书给的 `ch18 mel packages callie for the label` **在盘上不存在**（`grep -rn "packages callie" .memory/ docs/` 只命中我自己的 2-machine.json）。盘上实际的 ch18 精读是 `ch18 mel tests the death scent samples.md`（H1 `# 18. Eulalia’s House`，6 块，与派工书的「Eulalia's House｜6 块」一致），**本次以此为审查对象**。
> 另：同目录还有一个**无扩展名**孪生文件 `ch18 mel tests the death scent samples`（git 已跟踪，提交 `aa5ea4156`），内容是 `e38b6ec1b` 之前的旧稿（md5 `a834ef02…`），**不是本次审查对象**；**全书 54 章都有这种无扩展名孪生件**，属仓库卫生问题，另案处理。
> **被审文件在审查途中被改写**：mtime 10:09 → 14:42，提交链 `e38b6ec1b`(10:10 延长引语) → `b720cbeb5`(14:41 分部名改 TUESDAY) → `aa3227fe0`(14:42 改「周二」) → `4e91ac82c`(14:59 全大写分部名收入 check_entities STOP)。**本报告一律以当前 HEAD `6f4fa513` 为准。**

---

## 一、漏（素读有、md 无）

### D-1 ｜提示｜`[1641,2282]` 一整段未被任何引语块覆盖，而导航断言与本章反讽核心都在这一段

**源文 ch18:[1641,2282]**（md 六块引语全部避开此段）
```
Eulalia swatched every lipstick shade down her arm like a plump, semimatte ladder climbing
up her flesh. Globs of lip oil ran down the back of her hand. She tried a sheer purple one on.
It tasted like Palma Violets. Anyone she kissed while wearing it would succumb. Eulalia smeared
every high-pigmented glitter eyeshadow from a palette inspired by poisonous jellyfish down her
other forearm, followed by every cream blush that looked like bruising and every mercurial
highlighter. She was utterly delighted by everything, but she was most of all delighted that
she’d been understood by the mega luxury goods conglomerate. Mel made notes.
```

**md 现状**：六块引语区间为 `[129,640] [721,1010] [1327,1641] [2282,2623] [2626,3414] [3732,4028]`——`[1641,2282]` **整段落在块与块之间，无一块覆盖**。
而 md 导航 L11／L14 的两条断言：「Eulalia 负责…**涂满两条手臂**，Mel 负责**记笔记**」，其唯一出处正是这段（`down her other forearm`；`[2264,2279] Mel made notes.`）；本章最锋利的一句反讽「she was most of all delighted that she’d been **understood** by the mega luxury goods conglomerate」也在这段。
同理被跳过的还有 `[1234,1285]` `‘I thought we should start with the perfumes first.’ Mel gestured at the bottles lined up.`——**梅尔主导这次试样的唯一直接证据**（本章专项「姐妹分工」），以及 `[1011,1047]` `‘It won’t look like that in the end. They’re really open to our input.’`。

**为什么算提示**：md 的引语覆盖率 62.9%（2,536/4,029 字符），远高于本书中位 18.7%，块数 6 也在本书众数区间内，**不构成"引语选短"或覆盖不足**；但 nav 用未引证的字句做断言，属可补可不必补的取舍。
**修法**：把 原句3 的引语从 `[1327,1641]` 延到 `[1327,2282]`（试用过程与「Mel made notes.」一并纳入），并在 原句2 之后补进 `[1011,1047]` 与 `[1234,1285]` 两句；或在 原句3 与 原句4 之间加一块专讲这一段。

---

## 二、编（md 有、原文无）

### D-2 ｜阻断｜导航／总结把「谁在替谁打掩护」的方向写反了：**梅尔是把 Calliope 雇进流程，不是挡在流程外**

**md L11（导航·一句话概括）**
```
…Mel 负责记笔记并独自应付厂方来电，在电话里**把外人 Calliope 挡在流程之外**。
```
**md L103（一句话总结）**
```
…她**把外人 Calliope 挡在流程之外**，又**把 Venetia 拉进姐妹俩共同隐瞒的那一边**…
```

**源文 ch18:[884,1010]**（同一段里，Callie 是被**雇进来**的）
```
that this was the whole point of hiring Callie, but Eulalia refused to ever see the big
picture and preferred griping instead.
```
**源文 ch18:[3189,3251]**
```
She’s working with Eulalia on concepts. They’ve really gelled.
```
**源文 ch18:[3304,3414]**
```
She wasn’t comfortable with an outsider being so close to the process, so close to their
mutually held deceit.
```

**为什么算阻断**：本章原文的方向与 md 写的**相反**——
① 梅尔不是把 Calliope 挡在流程外，而是**主动把外人雇进来、送进流程**（"the whole point of hiring **Callie**"；"She’s **working with Eulalia on concepts**"）。"挡在流程之外"在原文里找不到任何依据。
② 原文里被梅尔"挡"的是**离姐妹俩的隐瞒太近的局外人**（"an outsider being so close to… their mutually held deceit"），而 "their" ＝**梅尔与埃乌拉莉亚这对姐妹**；md 却把"共同隐瞒"的一边扩成维内提亚（见 D-2b）。

这是本章专项「**谁在替谁打掩护的方向有没有写反**」的**正中靶心**，且落在导航与总结两个主断言上。
**修法**：L11／L103 的「把外人 Calliope 挡在流程之外」改为「**雇下外人 Calliope 让她进流程**，却在电话里独自兜住姐妹俩的隐瞒」。

### D-2b ｜提示｜「把 Venetia 拉进姐妹俩共同隐瞒的那一边」：拉进伙对，归属错

**md L13（导航·线索结构）**
```
…以及 **Mel 与 Venetia 在电话里结成的一小圈共同隐瞒**。
```
**md L51（原句 5·为什么这样写）**
```
…再用『共同隐瞒』**把 Venetia 拉进同一个阵营**。
```
**源文 ch18:[3304,3414]**
```
She wasn’t comfortable with an outsider being so close to the process, so close to their
mutually held deceit.
```
**源文 ch18:[3732,3768]**
```
Between you and me, we all just need to listen to the presentation and nod along, telling
```

**结论**："拉人入伙/一起做戏"这层**原文支持**（梅尔确实让维内提亚在演示时"listen… and nod along"，`we all` 含维内提亚）；错的是把**姐妹俩的"mutually held deceit"** 说成维内提亚也站进去的一边——原文的语态是梅尔**不自在**"一个外人离这套流程（和姐妹俩共同的隐瞒）这么近"。
**修法**：保留"拉进伙（照做）"，删去"共同隐瞒/同一个阵营"这类归属语，改为「**姐妹俩**共同隐瞒，局外只被安排照做」。

---

## 三、错（两边都有但不一致）

### D-3 ｜提示｜原句 1／原句 4 把两姐妹的分工写成"各看各的"，与本章机制及 md 自身 L30 相抵

**md L23（原句 1·为什么这样写）**
```
同一批样品**在两人眼里是两件东西：Eulalia 看见的是审美，Mel 手里是货物**，
而它们此刻并排躺在同一张餐桌上。
```
**md L44（原句 4·为什么这样写）**
```
同一套化妆品，在这两个人手里**分别是作品和生意**。
```
**md L30（原句 2·为什么这样写，md 自己）**
```
两个人一个在闹、一个在扛，**谁也不点破**。
```

**源文 ch18:[38,126]**
```
Mel laid out a selection of goodies on the dining room table for Eulalia to choose from.
```
**源文 ch18:[721,1010]**
```
…Mel had to stop herself from rolling her eyes at **her sister’s predictability**. She’d told
her that before, that this was the whole point of hiring Callie…
```
**源文 ch18:[2910,2985]**
```
…she picked everything I said, sorry, I mean everything I thought she would.
```

**结论**：原文里"挑"的是梅尔——**摆上桌的是梅尔筛过的那一批**（"laid out a selection … for Eulalia to choose from"），妹妹"挑"的每一样都在梅尔预判之内（"her sister’s predictability"、"everything I thought she would"）。md 却写成"妹妹＝审美、姐姐＝货物／生意"两套不相干的东西，等于把本章的**一个套路的两个角色**写成各看各的；并且与 md 自己 原句2 的"谁也不点破"**直接矛盾**（L30 说心照不宣，L23/L44 说两人看的是两件东西）。
**为什么算提示**：这属分析层的取舍，不是与原文逐字冲突的硬伤（两半各自的依据都找得到），但方向偏了，且内部自相矛盾。
**修法**：L23／L44 改为「同一批样品是**同一盘棋**：梅尔摆盘、记笔记，早知妹妹会挑什么；妹妹以为是自己挑的」。

### D-4 ｜提示｜原句 2 给「雇 Callie」安的动机偏窄（原文只说"这才是全部用意"，未说是为消抱怨）

**md L28（原句 2·中文理解）**
```
她早就跟妹妹讲过：**请 Callie 来做这件事正是为了消掉这些抱怨**；可 Eulalia 始终不肯看全局…
```
**md L31（原句 2·读者视角提示）**
```
Calliope 在这一句里以『**被雇来收拾残局**』的身份出现…
```
**源文 ch18:[884,1010]**
```
that this was the whole point of hiring Callie, but Eulalia refused to ever see the big
picture and preferred griping instead.
```
**源文 ch18:[1011,1047]**（同一拍里的补充）
```
‘It won’t look like that in the end. They’re really open to our input.’
```

**结论**：原文的逻辑是——「雇 Callie 才是全部用意」是**梅尔早先告诉过妹妹、而妹妹始终没看懂的那个大局**；「抱怨包装」是妹妹**看不懂大局时的替代动作**（"preferred griping instead"）。md 把"用意"定成"为了消掉抱怨"，于是原文的 "refused to ever see the big picture" 在 md 里失去着力点（若用意只是止住抱怨，看不看大局就无从谈起）。
**为什么算提示而非阻断**：md 的读法有本地支撑——同一段里 Mel 确实说过 "It won’t look like that in the end"（最终的样子会不同，暗示由 Callie/厂方接手），"叫人来收拾包装"是一条**可成立的本地推断**；但它把"大局"读窄了，且抹掉了"被雇来收拾残局"这层定位的真正问题（见 D-2：Callie 是**被雇进流程的人**，不是擦屁股的人）。
**修法**：改为「梅尔早先说过：雇 Callie 才是这盘棋的关键；埃乌拉莉亚看不懂这个大局，只顾抱怨包装」，删「收拾残局」。

### D-5 ｜提示｜原句 2：这一拍里"兜"的方向与场面时点

**md L30（原句 2·为什么这样写）**
```
Mel 一边『忍不住翻白眼』，一边**替妹妹在厂方面前兜着**；
```
**源文 ch18:[643,718]／[721,775]**
```
‘I hate the packaging.’ Eulalia wrinkled her nose at how ‘clean’ it looked.
…
‘That’s just what the sample comes in from the factory.’ …
```

**结论**：这一拍在**餐桌前**，梅尔是**替厂方（PCQV）向妹妹解释**（"样品就是这么从工厂来的"）；"厂方面前"的场面要到 原句5／6 的电话才发生。把"替妹妹在厂方面前兜着"放进这一拍，是把后文话题提前，且把兜的方向对调。**提示级**。
**修法**：改为「妹妹抱怨，梅尔**替厂方解释**；『厂方面前』那一遍在后面的电话里」。

### D-6 ｜提示｜原句 6：把同一通电话里的两句拆成"电话上／私下"

**md L56（原句 6·中文理解）**
```
…**她私下把结果说破**——真落进彩妆线的，多半不过是一个字体或一套配色。
```
**md L58（原句 6·为什么这样写）**
```
**对着电话她许的是姿态，私下认定的是结果**；
```
**源文 ch18:[3732,3961]**
```
Between you and me, we all just need to listen to the presentation and nod along, telling
Eulalia she’s a genius. I think realistically what you’ll end up incorporating is a font or
a colourway, you know. Artists huh. Great chat.
```

**结论**：两句**同在一通电话里说出**。"Between you and me"是对维内提亚的**交底**，不是电话之后的私下心里话；原文里她**恰恰对维内提亚讲明了**（这正是要维内提亚配合点头的原因）。md 的 L58 把"打折扣的实话"搬到"私下"一侧，等于说梅尔没对维内提亚讲真话。
**为什么算提示**：L56 的"私下"单看可读成"私下对维内提亚交底"，尚可容忍；**L58 的"对着电话／私下"二分才是可核对的不符**。
**修法**：L56 删「私下」二字，L58 改为「同一通电话里，她**一边教对方点头、一边交底**」。

### D-7 ｜提示｜原句 3：叙述句"始终是干的"过强

**md L37（原句 3·为什么这样写）**
```
…而**叙述者的句子始终是干的**：她一瓶瓶试过去，同样高兴，仅此而已。
```
**源文 ch18:[1606,1640]**
```
…equally delighted with their sickly sweet, heady smell of decay.
```

**结论**：引号内那句叙述并非"干"的——"sickly sweet, heady smell of decay" 本身带修辞。且"始终"由**一句**推及全章叙述语调，过强。**提示级**。

### D-8 ｜提示｜导航把"腐烂"安在了桃子上

**md L13（导航·线索结构）**
```
…（**腐桃**、毒水母、血月）
```
**源文 ch18:[246,320]／[1483,1508]**
```
There were death-scented perfumes, over-ripe peach-flavoured lip oils, …
…
‘Love it. Smells like rotting plums.’
```

**结论**：原文里**腐烂的是 plum（香水的气味）**，桃子只是 **over-ripe（熟过头）**；md 的"腐桃"把两样水果合成了一样。**提示级**（nav 措辞）。

### D-9 ｜提示｜原句 5：把给 Calliope 背书的履历说成"不相干"

**md L49（原句 5·中文理解）**
```
Mel 用一串**不相干的履历**（旧日做过时装编辑、你们是旧相识）把人接住…
```
**源文 ch18:[3020,3251]**
```
You know Calliope Foster? Yeah, yeah, so lovely. Milliner, but did a lot of fashion editorial
a decade ago. Oh you know her personally. You’re old friends. Small world. She’s working with
Eulalia on concepts. They’ve really gelled.
```

**结论**：这串履历在原文里**正是在派用场**——"Milliner + 十年前做过时装编辑"给 Calliope 背书，"you know her personally. You're old friends. Small world"把这次合作说成顺理成章的旧识往来，替姐妹俩的安排做了掩护。md 称其"不相干"并说梅尔只是"接住"话头，削掉了这层掩护功能。**提示级**。

### D-10 ｜提示｜原句 6·读者视角提示：把被恭维的对象写成了"姐姐"

**md L59（原句 6·读者视角提示）**
```
…Mel 让对方点头、**夸姐姐是天才**，心里清楚这一整套姿态只有自己在经营。
```
**源文 ch18:[3814,3844]**
```
telling Eulalia she’s a genius
```
**md 自己的称呼约定**：L11「姐姐 Mel … 妹妹 Eulalia」、L42「她要给**姐姐**已经写好旋律的那首新歌填词」（旋律出自梅尔，=姐姐）⇒ md 里 **姐姐＝Mel，Eulalia＝妹妹**。

**为什么算阻断**：原文的受事是 **Eulalia（妹妹）**：被恭维为 genius 的是埃乌拉莉亚，梅尔教维内提亚去这么说。md 写成"夸**姐姐**是天才"，按 md 自己的称呼即"夸 Mel 是天才"——**对象错置**，且与**同一块**的中文理解 L56「再告诉 Eulalia 她是天才就行」**自相矛盾**。这属《生产-审查对照》S3 的④说话人错配／⑥受事归属反转（引语逐字、关键词、密度、形态四道机器探针全绿，只有 R4 的"受事是谁"这一问能抓）。
**修法**：L59 改为「Mel 让对方点头、**夸 Eulalia 是天才**」。

### D-11 ｜提示｜原句 5：自我更正只抄了字面，没点破"实情"

**md L49（原句 5·中文理解）**
```
…紧接着她顺手把『她挑的全是我说的』改成『她挑的全是我以为她会挑的』，**一句自我更正把漏洞圆了过去**。
```
**源文 ch18:[2910,2985]**
```
…she picked everything I said, sorry, I mean everything I thought she would.
```
**源文 ch18:[38,126]**
```
Mel laid out a selection of goodies on the dining room table for Eulalia to choose from.
```

**结论（本章专项②：梅尔报给对方的说法与实情差在哪里）**：md 抄准了改口的两端，也判断对「更正版是圆过去的说法」；但**没有点破实情**——梅尔摆上桌的就是她早知妹妹会挑的那一批（"laid out a selection … for Eulalia to choose from" ＋ "her sister’s predictability"），所以更正后的那句"她挑的全是我以为她会挑的"**本身仍是包装**：它把**梅尔排好的局**说成妹妹的自由品味。漏掉这一层，本章最锋利的反讽就没被读出来（R4「只复述字面、没有为什么」的密度不足）。
**修法**：在 L49 或 L52 补一句「更正后的说法仍是包装——桌上那一批本就是梅尔按妹妹的喜好挑好的」。

### D-12 ｜提示｜导航：把楼下的房间说成"客厅"

**md L12（导航·视角）**
```
…她的注意力在餐桌上的样品、妹妹上楼后空下来的**客厅**和电话那头的 Venetia 之间来回移动。
```
**源文 ch18:[38,126]／[2282,2623]**
```
Mel laid out a selection of goodies on the dining room table for Eulalia to choose from.
…
Eulalia flitted back upstairs to her room … as Mel was left downstairs to manage everything else.
```

**结论**：原文只给出 **dining room table**（餐桌）、**upstairs / her room / downstairs**；"客厅"是原文没有的房间名（楼下摊样品的地方按原文是**餐厅**）。**提示级**（nav 措辞）。
**修法**：「妹妹上楼后空下来的楼下」或「摊样品的餐厅」。

---

## 四、假红（工具判错，不改 md）

### D-13 ｜假红｜`check_vocab.py` 报 ch18 基础档「packaging」超纲

**取证命令与输出**
```
$ python3 scripts/check_vocab.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell" | grep ch18
  ch18 mel tests the death scent samples.md [基础] 基础档疑含超纲词「packaging」
$ echo $?
0
```
**工具口径**：`scripts/check_vocab.py:255` 的判据是 `len(p) >= 9 and p not in BASIC_WORDS and p not in COMMON`——**纯长度启发式**；"packaging" 恰好 9 个字母。它是本章原文用词（ch18:[643,664] `‘I hate the packaging.’`），属**工具误报**。md 不改。

---

## 五、已核实为正确（护栏，后续不得据"读着不对"改动）

| # | md 写法 | 原文依据 |
|---|---|---|
| G-1 | 原句 4「她要给**姐姐**已经写好旋律的那首新歌填词」 | ch18:[2481,2538] `a new song **her sister** had already bashed out a melody for` —— 旋律出自梅尔（=姐姐），妹妹写词；md 未把作词人也写反 |
| G-2 | 原句 3「闻起来像**烂掉的李子**」 | ch18:[1483,1508] `Smells like rotting plums.` —— plum 可作李子/梅子，未误作"烂桃子" |
| G-3 | 原句 1「五种怪色号的纤长睫毛膏」「像血月一样发亮的高光」 | ch18:[246,640] `a tubing mascara in five wacky shades`、`powder highlighters that shone like the blood moon` |
| G-4 | 原句 5「电话那头是 Venetia——样品正是从她那边送来的」 | ch18:[2782,2830] `‘From Eulalia’s team. She was thrilled with everything you sent over.’` —— "you sent over" 指维内提亚一方，无误 |
| G-5 | 原句 6「Mel 把电话那头的同事拉进伙」中的"拉进伙" | ch18:[3732,3768] `Between you and me, **we all** just need to listen to the presentation and nod along` —— 梅尔确实把维内提亚拉进表演；错的只是"同事"这一称谓与"共同隐瞒"的归属（见 D-2b） |
| G-6 | 原句 6「告诉 Eulalia 她是天才就行」（中文理解 L56） | ch18:[3814,3844] `telling Eulalia she’s a genius` —— **这句 md 是对的**，错在同一块的读者视角提示（见 D-10） |
| G-7 | 原句 5「电话那头是 Venetia」（本章专项①） | ch18:[2626,2680] `‘Hey, Venetia, it’s Mel.’` —— 说话人识别正确 |
| G-8 | 原句 5「样品正是从她那边送来的」 | ch18:[2837,2850] `She was thrilled with **everything you sent over**` —— PCQV 一方送出，无误 |
| G-9 | 词汇表 23 条例句 | 全部逐字命中本章原文（含 `she’d been understood by the mega luxury goods conglomerate` 落在未引证的 `[1641,2282]`，仍是本章原句） |

---

## 六、附：覆盖与形态实测

| 项 | 实测 | 本书众数/基线 | 判定 |
|---|---|---|---|
| 引语逐字 | 6 块 / 7 片段 **全部逐字命中**，0 MISS | — | ✅ |
| 引语字符覆盖率 | **62.9%**（2536/4029） | 中位 18.7%（54 章实测） | ✅ 远高于众数 |
| 块数 | 6 | 中位 7，区间 5–10 | ✅ 在区间内 |
| H1 形态 | `# 18. Eulalia’s House` | 全书 54/54 为 `N.` 形 | ✅ |
| 导航项名与项数 | 5 项：`一句话概括/视角/线索结构/人物弧线/叙事手法` | 全书 54/54 同名同序 | ✅ |
| 子项集 | `中文理解/关键词/为什么这样写/读者视角提示` | profile 子项集（同 4 项），`句子结构` 为可选项、本章未用 | ✅ |
| 词汇表例句 | 23 条例句**全部逐字命中本章原文** | — | ✅ |
| 引语顺序 | 6 块区间单调递增 | — | ✅ |
| **分部名写法（偏离项）** | 本章用中文「周二」 | 全书 **16 章**用英文全大写原名（`分部「WEDNESDAY」`…`分部「SIX WEEKS LATER」`）；**仅 ch16**（同属 TUESDAY 分部、第一部）也用中文「周二」 | ⚠️ 提示，见 `4-verdict.md` 形态组 |
