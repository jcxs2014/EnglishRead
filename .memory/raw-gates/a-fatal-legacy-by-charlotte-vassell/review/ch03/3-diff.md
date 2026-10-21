# R3 三张单子 · ch03《The Police Station》

- 原文（唯一权威源）：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch03_3.txt`（8225 字符 / 173 行）
- md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch03 willow bell is questioned.md`
- 素读底稿：`1-suread.json`（先落盘，后开 md）
- 机器层：`2-machine.json`（`bash scripts/chapter.sh … --json` → 退出码 0，verdict ok）
- 引用口径：原文侧一律给 `text/ch03_3.txt:<行>` + 该行逐字；md 侧给行号 + 逐字片段
- 判据：`docs/rules/审查表.md` R3（漏 / 编 / 错）+ `docs/rules/创建卡.md` §0.2、§2 ①

---

## 单子 A · 漏（素读有、md 无）

### A1 —【阻断】发现尸体当天早上她到的时刻「8.45 a.m.」全 md 缺失

- **原文逐字**（`text/ch03_3.txt:26`）：
  > ‘Sure,’ she said, placing the partially nibbled biscuit down. ‘**I turned up at the Institute at 8.45 a.m.** like I normally do. The door was left open, which was a bit odd, and I just walked in.’
- **md 侧**：全文件检索不到 `8.45`（取证命令与输出见下方「取证」节）；md 唯一给出的「到场时间」是 3.15 p.m.（`ch03 …md:13` 导航「到场时间（手机基站打卡反推出 3.15 p.m.）」），而 3.15 p.m. 在原文里是**前一天下午**的探访时间（见 C1）。
- **为什么算漏**：本章专属判据是「一个目击者的记忆与盲区——**她能提供什么**」。「她几点到、推门进去、发现尸体」是这份证词里最基本的一项事实，也是读者能据以重建时间线的那一项。md 用 3.15 p.m. 顶替了这一项，等于时间线上「发现现场」这一格是空的，而读者会误以为 3.15 p.m. 就是发现时间。
- **建议**：md 导航「线索结构」与「一句话总结」里补上 8.45 a.m.（或直接引用 `text/ch03_3.txt:26` 整句），并把 3.15/3.24 p.m. 明确标成**前一天下午**。

### A2 —【提示】她对死者专业身份的了解「He was a historian」未出现

- **原文逐字**（`text/ch03_3.txt:80`）：
  > ‘No, sorry. He wasn’t chatty like that anyway, but that just doesn’t chime with what I knew about his personality. Mr Combe-Watson was a very studious man. **He was a historian.** Quite a serious “chap”. He didn’t have dramatic fallings out with anyone.’
- **md 侧**：7 个引语块无一处涉及；导航亦无。
- **为什么算提示（不判阻断）**：不是关键事件或转折，属可选补充。但它与 md 自己写下的另一处形成对照：md 在原句 5 之外没有收录 `text/ch03_3.txt:98` 的「I’m not supposed to call it a museum, it’s an institute for the further study of something or another」——「她知道死者是历史学家、却拒绝说研究所研究什么」本可以构成一组很好的反讽（这正是"她能提供什么/不知道什么"）。
- **建议**：可选。若要补，宜与 A5 合并成一块。

### A3 —【提示】她誊日记的理由「Because I was asked to.」未出现

- **原文逐字**（`text/ch03_3.txt:128`–`131`）：
  > ‘Why were you typing it up?’ Caius thought the journals sounded like a liability to the Institute’s reputation.
  > ‘**Because I was asked to.**’ She shrugged.
- **md 侧**：原句 6 的引语从 "Horatio Combe would be in prison…" 起，到 "…Neapolitan brothel." 止；问答的收尾（她说只是被吩咐）落在引语之外，md 未收。
- **为什么算提示**：不判阻断（不构成关键转折），但它决定了第 6 块的读法——她对藏品的了解是**被派下来的活儿**带来的，不是好奇；这条对"她与藏品的距离"有实质作用，而 md 第 6 块的读者视角提示说「她是真的逐字读过那些手稿的」却补不出她为什么读。
- **建议**：把原句 6 的引语向后延一句到 "Because I was asked to."（引语需保持连续，见 B5），或在第 6 块的分析里点明。

### A4 —【提示】导航承诺的「死者的性格、孤独」在 7 个块里没有对应内容

- **md 侧逐字**（`ch03 …md:14` 导航「人物弧线」）：
  > …再把**死者的性格、孤独**与藏品一件件评过来…
  同一承诺在 `ch03 …md:12`「视角」重复：「也看得出她既喜欢又烦躁迪吉」。
- **原文逐字**（性格，`text/ch03_3.txt:137`）：
  > ‘Mr Combe-Watson treated me fine. He was tight though. Very tight. He’d only pay my travel expenses. I’d seen him eat yoghurt that had been expired for a month.’ … ‘Oddly, though, he was fussy. … He was very pernickety. … He was antiquated, if you know what I mean. Being surrounded by all that stuff all the time had seeped into him and made him part of the past. That moustache for starters. Digby wasn’t even that old. Yeah, he was born in the 1980s…’ … ‘He was the only one who bit. He wrote to offer me the position. The whole thing was arranged by letter.’
  （孤独，`text/ch03_3.txt:155`）：
  > ‘**I guess he was lonely. Lonely and trapped.** I won’t miss that place. It has a funny energy.’ She touched her tarot card necklace again. ‘Sad though. Poor Digby.’
- **md 侧**：7 块中，**性格 0 处、孤独 0 处**（藏品 2 处，见原句 6、7）。导航向读者承诺了一段内容，精读没有交付。
- **为什么算提示（不判阻断）**：原文里这些评价确实存在，导航对**章节**的概括不算编；缺陷在于「导航承诺 ↔ 精读实有」不对齐，且按本章判据「留意她提起博物馆藏品时的语气」的语气研究已经做了（两块），性格/孤独是另外的质地，属可选覆盖。
- **建议**：要么补一块（如原句 3 之后接 `text/ch03_3.txt:155` 的孤独句），要么把导航「性格、孤独」改成与实有块一致的措辞。

### A5 —【提示】研究所的自我描述与她的日常工作未出现

- **原文逐字**（`text/ch03_3.txt:98`）：
  > ‘I was supposed to do tours of the museum. Sorry, Institute. I’m not supposed to call it a museum, it’s an institute for the further study of something or another. Not that they get many visitors, just the odd weirdo.’
  （工作内容，`text/ch03_3.txt:119`）：
  > ‘The filing. He did everything on paper. I was updating the little booklet that would be handed out to visitors. I did the odd thing on the website while at home for him too. Pretty boring.’
- **md 侧**：无（`ch03 …md:14` 导航只说「再把…藏品一件件评过来」）。
- **为什么算提示**：非关键事件；「Institute 而非 museum」这一自我否认对"藏品"话题有铺垫价值，但不补不伤。

---

## 单子 B · 编（md 有、原文无）

### B1 —【提示】「手机基站打卡」／「刷进了 Chalk Farm 的基站范围」——机制名与原文不符

- **md 侧逐字**：
  - `ch03 …md:13`（导航 线索结构）：「到场时间（**手机基站打卡**反推出 3.15 p.m.）」
  - `ch03 …md:51`（原句 4 中文理解）：「记录显示她 3.24 p.m. **刷进了 Chalk Farm 的基站范围**」
- **原文逐字**（`text/ch03_3.txt:62`）：
  > ‘About 3 p.m., I guess. Hang on.’ Willow took out her phone and scrolled for a moment before showing Caius what she’d found. ‘My phone says I **tapped back into Chalk Farm** at 3.24 p.m. It’s ten minutes’ walk so 3.15 p.m., I guess.’
- **判据**：原文是**车站闸机刷卡**（tapped back into Chalk Farm＝在回程的 Chalk Farm 站刷卡进站），不是蜂窝基站定位打卡。本书他章对同类证据一律用「刷卡／Oyster」（取证：`/usr/bin/grep -rniE "刷卡|闸机|Oyster|tapped (in|back|out)" --include="*.md" .` → 命中 `ch15 …md:15`、`ch15 …md:113`、`ch12 …md:68`，**全书 md 中「基站」仅出现在 ch03 这两处**）。
- **为什么判提示而非阻断**：时间、地点、倒推方向三项事实全对（3.24 p.m. 在 Chalk Farm、步行十分钟、倒推 3.15 p.m.），错的只是记录**机制名**；且它以「刷进…范围」的形式出现时，刷卡动作本身写对了（`刷进了`）。审查表的「错」限定在主语/因果/数字/时序，机制用词不在其列。
- **口径声明（如需严判）**：若把「机制名与原文不符」按「与原文不符 = 阻断」处理，本条可升为阻断——两处（导航 + 第 4 块）需一并改。**本次按「三项事实全对、仅机制用词不符」判提示**，把升格判断权交回执行方。
- **建议**：改为「手机进站记录（闸机刷卡）」。

### B2 —【提示】「她……背着『我本不该进去』的自责」——原文没有自责

- **md 侧逐字**（`ch03 …md:35`，原句 2 为什么这样写）：
  > 目击者于是从一进门起就背着「**我本不该进去**」的**自责**，发现尸体也就不再只是一次偶然，而是越界之后的结果。
- **原文逐字**（`text/ch03_3.txt:26` 与 `:32`）：
  > ‘I turned up at the Institute at 8.45 a.m. like I normally do. The door was left open, which was a bit odd, and I just walked in.’
  > ‘No. I usually had to ring the bell and wait to be let in. Mr Combe-Watson was very particular about that. I rang and I rang but Mr Combe-Watson didn’t come to the door.’ … ‘Then I noticed it was slightly ajar anyway so I walked in. I turned into the first room and there he was on the floor.’
- **判据**：她对「门开着」的说法是中性的（"a bit odd"），对走进去也没有任何愧色；原文没有「自责」「本不该」这类意思。这是一处**读者可能当真的心理断言**（分析层的解读），与"断言"不同性质，故判提示。
- **建议**：改为「她是在例行开门无果之后自己决定走进去的」之类不预设内疚的写法，或明写这是推测。

### B3 —【提示】「连细节都不自觉地补齐」——歧义：那些细节来自日记，不是她的记忆补白

- **md 侧逐字**（`ch03 …md:75`，原句 6 为什么这样写）：
  > 她一边嫌那些手稿是 the damn things、一边讲得又快又具体，**连细节都不自觉地补齐**。
- **原文逐字**（`text/ch03_3.txt:125`）：
  > ‘Well, I urgh, I was typing up Horatio Combe’s journals,’ Willow volunteered, but then looked like she regretted it. She started talking quickly. ‘There are all these volumes of the damn things. They’re all handwritten. Spidery writing. It takes forever because it’s so hard to read. Horatio Combe would be in prison for vandalism if he was alive today. He was a womaniser too. **I transcribed a diary entry last month** where he blithely described chiselling a bit of a Roman villa off in Pompei, pocketing it and then visiting his favourite Neapolitan brothel. …’
- **判据**：她讲出的凿取、私吞、妓院三件细节，出处是**她上月誊抄的那条日记**（原文写明 "I transcribed a diary entry last month"），不是她凭记忆替空白补上的细节。本章的母题是「哪些记忆是后来补上的」，所以这句在上下文里容易被读成「她在无意识中补齐证词」——那是原文不支持的读法。
- **建议**：把「补齐」的主语点明（补的是日记里的细节），或改写为「她讲得又快又具体，具体到把日记里那一段几乎背了出来」。

### B4 —【提示】「死者把藏品当作全部生命的立场」——本章无此依据

- **md 侧逐字**（`ch03 …md:85`，原句 7 为什么这样写）：
  > 她为归还而骄傲，与**死者把藏品当作全部生命的立场**正面冲突；…
- **原文逐字**（本章唯一相关的两处，`text/ch03_3.txt:173` 与 `:137`）：
  > ‘I did.’ Willow nodded proudly. ‘I don’t get why Digby, Mr Combe-Watson, still kept them. …’
  > … Being surrounded by all that stuff all the time had seeped into him and made him part of the past. That moustache for starters. …
- **判据**：本章只写到他**留着** mokomokai、「被那些东西泡透」；「把藏品当作全部生命」是跨章解读（ch01 有相近的描述，但那不是本章原文）。分析层作跨章解读本属正常，但这里它被写成了与她的立场"正面冲突"的既成事实，措辞强度超出本章证据。
- **建议**：弱化为「与他一辈子守着这些东西的立场正面冲突」之类本章可支撑的说法。

### B5 —【提示】两处分析引了引语外的英文原词（引语选短，创建卡 §0.2）

- **md 侧**：
  - `ch03 …md:65`（原句 5 为什么这样写）：「**Caius 紧接着的观察**（现在没人能核实她那份 LinkedIn 档案了）也提醒读者…」
  - `ch03 …md:75`（原句 6 为什么这样写）：「她一边嫌那些手稿是 **the damn things**、一边**讲得又快**又具体…」
- **原文逐字**：
  - `text/ch03_3.txt:107`（原句 5 引语**之外**）：
    > ‘Right.’ Caius could see her changing her LinkedIn profile in her head now there was no one to verify that with.
  - `text/ch03_3.txt:125`（原句 6 引语**之外**，在引语起点之前）：
    > … She started talking quickly. ‘There are all these volumes of **the damn things**. …
- **判据**：`docs/rules/创建卡.md` §0.2「分析里出现的每个人名/动作/关系，都必须在这段引语里；不在，就是引语选短了」。两处分析都用了引语外的材料（原句 5 引文外出现人名「Caius」与「LinkedIn」；原句 6 引文外出现 "the damn things" 与 "She started talking quickly"）。
- **为什么判提示而非阻断**：两块的**主旨仍在引语之内**（第 5 块＝自我更正，第 6 块＝她对藏品/祖辈的轻蔑），外引只是佐证句，且外引内容本身逐字属实。按「分析覆盖的原文比引语长 ⇒ 引语选短」的口径，这是 S2 ① 的轻微形态，不是错引。
- **建议**：要么扩引语（第 5 块向后延到含 "Caius could see her changing her LinkedIn profile…"；第 6 块向前延到含 "There are all these volumes of the damn things…"，注意保持连续、不要用 `…` 缝合叙述），要么在分析里改成不直接引英文外词。

### B6 —【提示】「这是全章第一次出现关于这批藏品的分歧」——与本章导航自相矛盾

- **md 侧逐字**（`ch03 …md:85`）：
  > …这是**全章第一次出现关于这批藏品的分歧**，而说出分歧的人是个每天进那间屋子做事的人。
  对照同文件 `ch03 …md:13`（导航 线索结构）：
  > …以及她**两次提起馆藏时的语气**——日记里的凿取，与她要求归还 mokomokai 的请愿。
- **原文逐字**（第一次，第 6 块自己的引语范围内，`text/ch03_3.txt:125`）：
  > Horatio Combe would be in prison for vandalism if he was alive today. He was a womaniser too. I transcribed a diary entry last month where he blithely described chiselling a bit of a Roman villa off in Pompei, pocketing it and then visiting his favourite Neapolitan brothel. … He wasn’t a good person by any stretch and a very poor storyteller, for that matter.
- **判据**：第 6 块已是她对**这批藏品**（及其掠夺来历）的第一次批判性表述，md 自己的导航也写成「两次提起馆藏时的语气」。若「分歧」专指两人之间的对立，则成立；但与同一文件里「两次提起馆藏时的语气」并读，读者会读成矛盾。
- **建议**：改成「这是全章第一次出现**针对死者本人立场**的分歧」。

---

## 单子 C · 错（两边都有但不一致）

### C1 —【阻断】3.15 p.m. 被写成发现尸体那个早晨的「到场时间」——实为前一天下午

- **md 侧逐字**：
  - `ch03 …md:13`（导航 线索结构）：「**到场时间**（手机基站打卡反推出 **3.15 p.m.**）」
  - `ch03 …md:138`（一句话总结）：「侦探 Caius 听实习生 Willow Bell **复述那个早晨**：虚掩的门、**手机倒推出的三点一刻**、一句“至少我没看见任何人”的双重退让，…」
- **原文逐字**：
  - `text/ch03_3.txt:47`（Caius 问的是哪一次）：「‘When was the last time you saw Digby alive?’」
  - `text/ch03_3.txt:50`：**‘Yesterday, actually.** I popped in in the early afternoon. I’d accidentally left a book I needed to complete an essay there last week.’
  - `text/ch03_3.txt:59`（问的仍是那一次）：「‘**What time was this?**’」
  - `text/ch03_3.txt:62`：「‘About 3 p.m., I guess. Hang on.’ … ‘My phone says I tapped back into Chalk Farm at 3.24 p.m. It’s ten minutes’ walk so 3.15 p.m., I guess.’」
  - 对照发现现场那天的时刻 `text/ch03_3.txt:26`：「‘I turned up at the Institute at **8.45 a.m.** like I normally do. The door was left open, which was a bit odd, and I just walked in.’」
- **判据（时序错）**：3.15 p.m. / 3.24 p.m. 这一组时间属于**前一天下午那次探访**（Q&A 明确：最后一次见活着的 Digby 是「Yesterday」，随后问「What time was this?」），与「发现尸体的那个早晨」无关。md 把它写进「复述那个早晨」的清单、并在导航里当成「到场时间」，等于把**前一天下午的时间**说成**发现当天的时间**。这是本章唯一的时间线断言，也是读者复盘「她什么时候到现场」的唯一依据。
- **与 A1 的关系**：A1（漏 8.45 a.m.）与 C1（错 3.15 p.m. 的归属）是同一个根因的两面：md 里「发现当天早上」这一格被**前一天下午的时间顶替**。修一处必须同时修另一处，只改 A1 不改 C1，读者仍会读到「到场时间 3.15 p.m.」。
- **建议**：导航「到场时间」改写为「发现当天早上 8.45 a.m.（`text/ch03_3.txt:26`）」，3.15/3.24 p.m. 明确标为「前一天下午那次探访的时间，由手机进站记录倒推」；一句话总结里「手机倒推出的三点一刻」前面补「前一天下午」。

### C2 —【提示】「等主人来开门」——原文是被动，施事是补写的

- **md 侧逐字**（`ch03 …md:31`，原句 2 中文理解）：
  > 她说平时必须先按门铃、**等主人来开门**，Combe-Watson 先生对此非常讲究；…
- **原文逐字**（`text/ch03_3.txt:32`）：
  > ‘No. I usually had to ring the bell and **wait to be let in**. Mr Combe-Watson was very particular about that. I rang and I rang but Mr Combe-Watson didn’t come to the door.’
- **判据（R4 固定追问 ①：每个动词的主语是谁）**：原文是**被动**（"wait to be let in"，由谁放她进去没有明说），md 补出施事「主人」，并暗示由 Combe-Watson 开门；本章也未称他为「主人」（他是研究所的主事者，ch39 才出现 he can sell the Institute 这层）。
- **建议**：改为「等有人来放她进去」或「等 Combe-Watson 来开门」（后者仍是对 "Mr Combe-Watson was very particular about that" 的合理还原，读者可接受）。

### C3 —【提示】「归还本来能换来好名声」——主语从「他」滑成「归还」

- **md 侧逐字**（`ch03 …md:81`，原句 7 中文理解）：
  > …理直气壮地说她不明白为什么他还要留着那些东西——**归还本来能换来好名声**，也许真会有人来看展，他还能卖上几张明信片；…
- **原文逐字**（`text/ch03_3.txt:173`）：
  > ‘I don’t get why Digby, Mr Combe-Watson, still kept them. **He could’ve got some good PR by returning them** and maybe someone would actually come and visit and he’d sell a postcard here and there. Culturally sensitive artefacts like that shouldn’t be in museums. It’s really disrespectful.’
- **判据（R4 固定追问 ①）**：原文的施事是 **He（Digby）**——好名声是**他**通过归还能拿到的东西；md 写成「归还本身换来好名声」，主语脱落。同句后半 md 又回到「他还能卖上几张明信片」，前后主语不统一。
- **建议**：改为「归还能替他换来好名声」。

### C4 —【提示】「侦探 Caius」——本章未写其职务

- **md 侧逐字**：`ch03 …md:12`「视角」：「第三人称限知，贴着**侦探** Caius 的观察与判断」；`ch03 …md:45`（原句 3 为什么这样写）：「而**侦探**此前刚把‘在场’从鬼魂气氛拉回到活人身上」；`ch03 …md:138`：「**侦探** Caius 听实习生…」
- **原文逐字**（本章只写他在录口供）：`text/ch03_3.txt:20`「Caius stated their names for the recording.」；章节小标题 `text/ch03_3.txt:17`「The Police Station」
- **取证（本条**成立**、不是缺陷，列此只为「已核实为正确」留护栏）**：
  - `text/xx_characters.txt:20`：「An Irish-Jamaican **detective** in the Met, CAIUS is a foodie…」
  - `text/ch06_6.txt:152`：「‘You should be a detective. I’m sure Caius could get you on a fast track scheme or something.’」
  - `text/ch24_24.txt:41`：「‘Oh, a DI.’ …」
  - ⇒ 「侦探 Caius」在全书口径下成立，**不判缺陷**。

---

## 取证（零命中类断言必须自证）

```
$ /usr/bin/grep -n "8.45\|8：45\|8点45\|8 时 45" \
    "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch03 willow bell is questioned.md"
(无输出)
退出码 1
```
⇒ md 全文确无 8.45 a.m.（A1 成立）。**未用 git grep / rg**（`text/` 被 `.gitignore` 排除，见审查表 R5-补）。

```
$ /usr/bin/grep -rniE "saturday in may" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/
(无输出)
退出码 1
```
⇒ 本书提取件里**没有任何分部标题行**，"A SATURDAY IN MAY" 不是语料里的字样（见 4-verdict 形态组）。

```
$ /usr/bin/grep -rn "基站" --include="*.md" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/
ch03 willow bell is questioned.md:13:…手机基站打卡…
ch03 willow bell is questioned.md:51:…刷进了 Chalk Farm 的基站范围…
退出码 0
```
⇒ 「基站」是 ch03 独有说法，全书他章无先例（B1）。

```
$ /usr/bin/grep -rnoE "分部「?[A-Z ]+ IN MAY" --include="*.md" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/
ch13:15 分部 A MONDAY IN MAY ／ ch21:11 A WEDNESDAY IN MAY ／ ch25:11 A WEDNESDAY IN MAY ／
ch27:11 A WEDNESDAY IN MAY ／ ch28:11 A THURSDAY IN MAY ／ ch29:11 A THURSDAY IN MAY ／
ch30:11 A THURSDAY IN MAY ／ ch31:11 A THURSDAY IN MAY ／ ch33:11 A THURSDAY IN MAY ／
ch34:11 A THURSDAY IN MAY ／ ch36:11 A FRIDAY IN MAY ／ ch38:11 A FRIDAY IN MAY ／
ch39:11 A FRIDAY IN MAY ／ ch42:10,123 A SATURDAY IN MAY ／ ch44:12 A SATURDAY IN MAY ／
ch47:15 A SATURDAY IN MAY ／ ch49:15 A MONDAY IN MAY ／ ch50:15 A MONDAY IN MAY ／ ch51:11 A MONDAY IN MAY
退出码 0
```
⇒ 17/54 章在导航散文里带分部名（ch03 不带），分部按「几月的星期几」递进。
