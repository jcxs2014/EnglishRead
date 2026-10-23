# ch18 深审 R3/R4 差异单（审查方只出指令，不改稿）

- 审查对象：`notes/books/novels/the-house-built-on-alligator-bones-by-sophia-huneycutt/ch18 skinning 101.md`
- 语料：`text/ch18_chapter_seventeen.txt`（3,048 词，本书最长章之一；R1 素读 242 条事实、anchor 0 MISS）
- 机器层：`bash scripts/chapter.sh` 退出码 0；引语块 10／片段 11／查无 0；空引号 0；子项缺 0；关键词不成立 0；H1 ✅「18. Chapter Seventeen」；导航 5 项 ✅
- 词表：15 行（5＋6＋4）例句逐行展平核对 **0 MISS**
- ⚠️ 本轮踩到一次门禁假绿：首次跑 `chapter.sh` 时把文件名拼成 `ch18 ch18 skinning 101.md`（ls 输出已含 `ch18` 前缀，又补了一次），退出码 0 却只吐出「本书形态基线」8 行（已有章 md：0／text 0）。**已用真实路径重跑**，本单结论基于重跑件。教训同「第 29 条：`check_chapter_quotes --book-dir` 假绿」——`chapter.sh` 对不存在的 md 不给非零码。
- 人判覆盖：本章 R1–R4 全走（导航 5 项＋10 块四子项＋词表 15 行＋一句话总结）
- **口径缺口（本轮新登记，属门禁而非稿件）**：`scripts/bookform.py` 的 `QUOTE_RE` 只匹配 `> **原句 N:**` 行 ⇒ **导航与「一句话总结」里内嵌的英文引语完全不在逐字 lane 内**。本章因此有 2 处撇号假绿（C-18-13）；全书扫描：15/49 章的分析层含 ASCII 撇号英文词，合计 51 处。

## 阻断（C-18-1 … C-18-13）

### C-18-1｜md:20「摔门出门」＝凭空动作
- 原文：:9 `Gazzie stalked out the front door before I could say a word`——只有「怒气冲冲地出门」。
- 取证：全章查无摔门用词。
  ```
  /usr/bin/grep -n 'slam\|bang' text/ch18_chapter_seventeen.txt   → 无输出，rc=1
  ```
- 风险：本书「摔门」是有归属的母题，只在 ch17 出现两次（ch17:45 `the cracked door to the other room slammed shut`、ch17:105 `she slammed the door behind us`）。把摔门挪到本章开头，等于给 ch17 的证据链添一件赝品。
- 改前：`周一早上，Gazzie 抢在我开口之前摔门出门。`
- 改后：`周一早上，Gazzie 抢在我开口之前出了前门。`（怒气交给 md:24 已有的 `stalked` 词义分析去说）

### C-18-2｜md:34「前一晚的文件不是疏忽而是第一波攻势」＝凭空时点
- 原文：:51 `Given her attempt to bore me to death with files` 无任何时间锚；文件工作从 ch12 起持续数日（ch12:51 `Dart has volunteered to digitize our files`、ch12:63、ch12:111、ch12:141、ch16:~90 `Digitizing files`）。
- 取证：本章 `last night`／`previous night` 只有三处，都不是文件：
  ```
  /usr/bin/grep -n 'last night\|previous night' text/ch18_chapter_seventeen.txt
  :9（昨晚找速写本的决心）  :48（Gazzie 给 Harrison 发短信）  :66（昨夜衬衫上的红溅）
  ```
- 改前：`我的推理因此有据可循：前一晚的文件不是疏忽而是第一波攻势。`
- 改后：`我的推理因此有据可循：连日把她按在文件里的安排不是疏忽，而是第一波攻势。`

### C-18-3｜md:54「读者比叙述者更早怀疑这句保证」被同块之后两行反证
- 原文：:171 `Another drop fell on his shoulder.` 紧接 :174 `“Sure seems like it,” I replied, unable to suppress a cheerful tone.`——叙述者当场用反讽拆台，不存在读者抢在她前面。
- 改前：`与"under control"的静态自信形成对照，读者比叙述者更早怀疑这句保证。`
- 改后：`与"under control"的静态自信形成对照；原文随即用一滴水（:171）和她压不住的欢快反讽（:174）替读者把这句保证拆掉。`

### C-18-4｜md:70「许可不是用嘴要的，是用眼神要的」被上一自然段反证
- 原文：:306 `Snorting for the second time that morning, he reached over the table, hovering his hands above mine. “Do you mind?” he asked.`——许可先用嘴要过；:309 `His eyes flicked back and forth between mine, asking for permission.` 是第二次、非语言的确认。
- 连带问题：块 6 的引文起于 :309 的第二句，把 :306 的发问整句关在门外，才使这句分析得以成立（见 C-18-11）。
- 改前：`许可不是用嘴要的，是用眼神要的，于是这幕教学在字面上没有发生任何越界。`
- 改后：`许可他先开口要过一次（:306 “Do you mind?”），手悬上去后又用眼神二次确认（:309）；两道请求之间，这幕教学在字面上没有发生任何越界。`

### C-18-5｜md:76「她把每个身体接触都要翻译成权力问题」全称被同块反证
- 反证（同章、同一次接触）：:312 `His hand engulfed mine. His palms were callused, rough. I hadn’t noticed his lips before. Dry but not cracked. Soft, probably.`——这一次被登记的是对他唇的观察（欲望），不是权力。
- 其他反证：:159 `trying not to feel appreciation for the solidarity`（同盟感）、:189 `I flashed him a bright smile`、:174 `unable to suppress a cheerful tone`。
- 改前：`注意她把每个身体接触都要翻译成权力问题（"unnerve""bullied"），这是她衡量所有近距离互动的默认标尺。`
- 改后：`注意她能把一次接触立刻翻译成权力问题（"unnerve""bullied"），但同章 :312 这一次读出来的却是他的唇——两套读数在同一个人体上打架，值得跟踪哪一套什么时候占上风。`

### C-18-6｜md:96「"被看穿恐惧"从这里开始升级」章内时序写反
- 原文顺序：:114 `I didn’t like that he’d clocked it.` → :327 `Had he noticed?`（Michelle 闪回之后）→ :330 `he credited my motionlessness to disgust—not pleasure` → 块 8 的 :345 → :348 `Had I slipped again?`。:345 之前已有两轮，不是起点。
- 改前：`注意她需要向自己确认"这不算邪恶"——章内反复出现的"被看穿恐惧"从这里开始升级。`
- 改后：`注意她需要向自己确认"这不算邪恶"——这股"被看穿恐惧"在本章已非第一次（:114 的 he’d clocked it、:327 的 Had he noticed?），到这里（:348 Had I slipped again?）它开始在她动手的瞬间发作。`

### C-18-7｜md:106「"Mama"每次作为禁令或标尺出现、而从不作为被叙述的人出现」全称被 :9 反证
- 反证：:9 `I was too tired to ask her about Uncle Leon or Mama or the unfamiliar voice`——Mama 在此是她咽回去的一个**提问对象**，既非禁令也非标尺。
- 同段 :354 `Mama would have been furious to see a knife in my hand` 才是禁令那一次。
- 改前：`留意"Mama"每次作为禁令或标尺出现、而从不作为被叙述的人出现——关于她，这章只给了态度，没给往事。`
- 改后：`留意本章两处提到 Mama：:9 是被她咽回去的提问对象之一，:354 是一条禁令；两处都没有给往事。`

### C-18-8｜md:116「罕见地主动出击的一问」＝言语行为误称＋「此前被动」被 :240 反证
- 误称：:381 `“Gazzie mentioned things going missing last week,” I said casually` 是**陈述**，不是问句（她随后 :387 `“How many?”` 才是问）。
- 「此前都是被动接招」不成立——本章她主动发问的行号（`/usr/bin/grep -n 'I asked\|I wondered\|I guessed\|Let me guess'` 汇总）：:33、:54、:102、:165、:201、:213、:219、:225、:231、:255、:273、:297、:357、:387 共 14 处；其中 :231 还写成 `Let me guess.`（先猜再问）。
- 最强反证：:240 `Harrison raised his eyebrows. “Interrogation over?”`——叙述者的连问已被对手当场命名为「审问」，与「被动接招」正相反。
- 改前：`注意这是我在一整章里罕见地主动出击的一问；此前的闲聊、教学、打闹都是被动接招，直到这里我才把话头拿去赌。`
- 改后：`注意这是我罕见地把话头拿去赌的一次：本章我问过十几次（:33 到 :357），Harrison 甚至用 “Interrogation over?”（:240）给我的连问定过性——但只有 :381 这一句是明知自己在诈（:381 hoping the statement was vague enough to fool him）。`

### C-18-9｜md:14「关键信息几乎全经 Harrison 之口二手传来」被自己举的例子推翻
- 举的反例：:60 `Gazzie had said our farm slaughtered fourteen thousand alligators each year.`——这个数出自**叙述者回忆 Gazzie 的原话**，不经 Harrison；而且不是本章新信息，ch08:153 已出现同一数字（`That did make me feel a little better about the fourteen thousand they’d slaughter this year.`）。
- 真正经 Harrison 之口的是：:210 Joe 的来历、:216 秘密内容、:252–:276 皮与头的去向、:168 漏水年限、:384 盗皮。
- 改前：`关键信息几乎全经 Harrison 之口二手传来（每年一万四千头的数字注明是"Gazzie had said"，Joe 的来历是转述）`
- 改后：`本章多数新信息经 Harrison 之口（Joe 的来历 :210、皮的生意 :252–:276、盗皮 :384），叙述者特意标明每年一万四千头是回忆 Gazzie 曾说过的（:60 Gazzie had said；该数 ch08:153 已出现过）——同一章里两种来源被这样区分开。`

### C-18-10｜md:13 把叙述者的判读算成「Harrison 交底」
- :69 `The unease that had crept into his expression when we watched Gazzie’s slaughtering session had returned. He didn’t like the messy parts of the business.`——后一句是叙述者由表情推的判断，Harrison 全章没有说过这句话。
- 他真正说出口的交底只有 :156 `She gives me the heebie-jeebies, too.` 与 :168（五年漏水）、:177（Ironheart 的玩笑）。
- 改前：`转到交底：他也怕 Ida 的画像、不喜欢生意里"messy parts"、在这栋漏水的楼里干了五年。`
- 改后：`转到交底：他承认 Ida 的画像也让他发毛（:156）、说这楼从他五年前入职起就一直漏（:168）；至于"不喜欢生意里 messy parts"（:69），那是叙述者从他表情里读出来的，不是他讲的。`

### C-18-11｜漏 :309 第一句 dryer sheets（跨章回指＋本章气味—接触链条的起点）
- 原文：:309 `The fragrance of dryer sheets drifted toward me, ten times stronger than the shirt in his room at Greer House.`
- 跨章：气味母题先在 ch13:48 落地，ch17:33 她埋进他 T 衫闻（`dryer sheets and something musky. Cedar, maybe`），本章由**同一件气味**给接触开场，并且是她自己量化「浓十倍」。
- 判定依据：块 6 的引文与四子项完全没有这一句，整幕因此只剩「权力」一条读数（放大 C-18-5）；这条回指也未被导航或读者视角提示登记。
- 改法（二选一）：① 把块 6 的引文扩到 :309 首句（注意机器层的引语块数会由 10 变 10、片段数会 +1，须重跑 `chapter.sh`）；② 不改引文，在块 6 的「读者视角提示」里补一行：`注意 Harrison 的手还没落到她手上，先落下来的是 dryer sheets 的气味——比他 Greer House 房里那件衬衫浓十倍（:309），这条气味线从 ch13:48 起就在替他到场。`

### C-18-12｜md:152 一句话总结把收束写成「打回原形」，漏掉 :369–:372 的确证
- 原文：:369 `I imagined myself showing up to skin alligators every day. Could I do it?` → :372 `Certainty shot through me. Yes, I could. More than that—I wanted to.`——愧疚（:354）之后渴望又长回来，本章内部落点是「她想干这活」，之后才转 :381 的试探。
- 连带：md:11 情感弧线「结尾停在怀疑（盗皮）上」只覆盖了最后九行，同样没给 :372 落位。
- 改前：`把这快感打回原形的不是鳄鱼尸体，而是我认出了自己对血色的着迷，和 Mama 那条缺席的禁令。`
- 改后：`让我住手的不是鳄鱼尸体，而是我认出了自己对血色的着迷和 Mama 那条缺席的禁令——可收工前我又确认了一次：我能干，而且我想（:372 More than that—I wanted to）。`
- 并建议 md:11 弧线补一格：`… Michelle 的记忆和"Mama would have been furious"把快感拽回愧疚与自警，:372 的确证又把渴望立回来，结尾停在怀疑（盗皮）上`。

### C-18-13｜md:13／md:14 导航内嵌英文引语的撇号字形（逐字层，机器不覆盖）
- md:13 写 `"You're good at saying the opposite of what you feel"`——原文 :111 是 `You’re good at saying the opposite of what you feel`（弯撇号 U+2019）。
- md:14 写 `"he'd clocked it"`——原文 :114 是 `he’d clocked it`。
- 取证：`chapter.sh` 的查无 0 只覆盖 `> **原句 N:**` 块，导航层的引语**不在口径内**；本章正文块 10 块 11 片段仍全对。
- 书级规模：15/49 章的分析层有 ASCII 撇号英文词，合计 51 处（`re.findall(r"[A-Za-z]+'[A-Za-z]+")`）。**禁止无差别全局替换**——其中一部分是她自撰的英文（关键词行、术语），须逐条回 text/ 判形：能在 text/ 以 ’ 命中的才改。
- 改前：`Harrison 从讽刺（"You're good at saying the opposite of what you feel"）`
- 改后：`Harrison 从讽刺（"You’re good at saying the opposite of what you feel"）`
- 改前：`叙述者随即自查"he'd clocked it"式的被看穿恐惧`
- 改后：`叙述者随即自查"he’d clocked it"式的被看穿恐惧`（若采纳 T-18-11 换例引，则连带把新例引按 text/ 字形写）

## 提示（T-18-1 … T-18-18）- **T-18-1**｜md:10「Gazzie 一整天不跟我说话」是归纳（全章确无 Gazzie 一句台词），但 Gazzie 只在 :9–:18 在场，之后文本对全天互动是选择性叙述（:363 `We skinned six alligators that afternoon` 一笔压缩）。宜收窄为「当天她没跟我说话，只把话交给 Harrison 与一条短信转达」。
- **T-18-2**｜md:12「Ida Greer 的肖像复制品在剥皮间**值班墙上**」会被读成一处「值班墙」；原文只说挂在墙钟下（:150 `hanging underneath a wall clock`）。宜作「在剥皮间的墙上值着班」。
- **T-18-3**｜md:34「"but skinning?"…从句式里抽掉了宾语」——它是「部门」的省略、光杆动名词；缺的是谓语（she would assign me to skinning），不是宾语。
- **T-18-4**｜md:66「这一眼是本章给他的**全部**性格底色」——:210–:234 还经 Harrison 之口给了他完整的来历与立场（第三代、被买断、老派、不愿为女人干活、她喜欢有能力的人）。宜收窄为「唯一一次直接落在他身上的举止」。
- **T-18-5**｜md:74「"I inclined my head"…是她少见的毫不迟疑的应答」——同句之前是 `I assumed… but I refused to be bullied` 的权衡；「毫不迟疑」应改为「压住权衡之后的一动」，「少见的」属跨章稀有度判断、无出处。
- **T-18-6**｜md:84「让她着迷的不是惨剧而是那层颜色」——:321 只给 `I’d never seen anything like it`，紧随 :327 把这次走神定性为 `dangerous territory`。写「着迷」要挂到 :330 的 `not pleasure`（叙述者自己主张那是快感）上才有据。
- **T-18-7**｜md:94「用背影写权力感」——原文是身体知觉（:345 `I sensed Harrison moving out of my way`），没有背影画面。
- **T-18-8**｜md:104「与前面快感的"轻盈"形成身体对仗」——前文的动感来自 :318 `Excitement rippled through me`、:354 `Satisfaction swept through me`；「轻盈」宜落回 rippled／swept 这两个水面动词，对仗才成立（sweep/ripple vs settle）。
- **T-18-9**｜md:104「她真正的考官始终不在场」——Gazzie 在 :9–:18 同章在场（一起坐车、同到办公室）。若指「剥皮现场无人监督」，请写明。
- **T-18-10**｜md:56 把 :21（前办公室 `newly drywalled, leak-free ceiling`）与 :162（剥皮间 `a new, all-too-familiar crack`）并成「这栋楼」的对照——两处是不同房间（:117 侧廊通往加工区，同一建筑群）。可并提，但需点明房间不同；另 ch12:39 已有「屋顶漏水是常态」的判读，:168 的五年年限是第二次坐实，可作跨章登记。
- **T-18-11**｜md:14 例引 `he'd clocked it` 是 :114 的话；Michelle 闪回（:321）之后她的自查是 :327 `Had he noticed?`、:348 `Had I slipped again?`。写「随即自查」应换例引。
- **T-18-12**｜md:10「只通过 Harrison 的转述把我扔进剥皮间受训」——指派另有 :48 `She texted me last night`（Gazzie 的短信），转述只是末端。宜写「只经 Harrison 之口与一条发给他的短信」。
- **T-18-13**｜**书级形态**：本章用 ASCII 直引号包住中文词 48 处、「」仅 4 处；ch17 为 0／21，最重的 ch34 达 76 处，全书 39/49 章用「」、10 章为零。不宜逐章返工，请在总指令里一次性定档（建议：中文语境用「」、英文短语用 `"..."`，并把「引号形态」加进 chapter.sh 的提示型统计）。
- **T-18-14**｜漏 :21–:24 Nova 一幕（:21 `making her white peasant top billow cinematically`、`which were carnation pink`、`using the ends to tickle her glossy lips`）与 :24 `I wished, for no discernible reason, that I’d worn lip balm`／`I’d stopped wearing foundation, too`——这是本章第一次「对镜自察」，与 :312 观察 Harrison 的唇同一条线；目前只进了词表（miniature／discernible），未进块层或导航（「进了词表≠已登记」）。
- **T-18-15**｜漏 :129 `Does Gazzie still think it’s your great-great-grandmother’s ghost?`——本章鬼话题由 Harrison 口中续上，并暴露「Gazzie 跟他谈过叙述者」；配套 :132 `She told you that?`、:135 `I know she’s superstitious`、:138 `I wasn’t about to shit talk Gazzie in front of my rival`（她第一次在心里称他 rival）。曾曾祖母＝Ida 的等式在 ch04:279/:282 已被她自己提出，属可回指的既有坐标。
- **T-18-16**｜漏 :339 `imagining plaster pouring over my face, rendering it expressionless`——她「先把自己刷成无表情再动手」的方法句，紧接 :345 `But I was already pushing the knife in`；:309/:312 的许可—接触—走神链条要有这句才闭合。
- **T-18-17**｜漏 :366 `The leak’s size had doubled with each alligator I skinned, almost like the water was protesting my involvement`——她把漏水读成对她工作的抗议（泛灵读数），与 ch17 的穿堂风／骤冷同一手法；注意原文用 `almost like`（对冲）而叙述者自己把它当玩笑。
- **T-18-18**｜漏 :375–:378（:375 `slung a chain around the two handles, connecting them with a padlock`、`another padlock`、`Glancing at the security camera above the door`；:378 `I remembered Nova’s hushed exchange with Gazzie, Gazzie’s insistence that they stop their discussion in front of me`）——两把挂锁＋摄像头是 :384 盗皮的结构前提。**另 :378 的回指在 ch01–ch17 的 text/ 里查无对应场景**（`/usr/bin/grep -rn 'hushed'` 只命中 ch10:93 的 `Gazzie shushed me`，非同一事），属书中未叙的回忆，不许裁决为「ch10 那一幕」。

## 假红（已判定为不是错，防止下一轮改坏）

- **F-18-1**｜「祖孙冲突」（md:24）成立：ch02:53 `This Gazzie person called me her granddaughter, which meant she was my grandmother`。
- **F-18-2**｜md:64「他看"我的祖母"时早就有的那一种」与 :198 一致；因祖母＝Gazzie（他的雇主），md 由此推出的「对女性雇主的立场」有 :231–:234 接应。
- **F-18-3**｜md:84「Michelle 是谁、发生了什么，**这一句**一概不给」＝对单句范围的准确陈述，不是「全书未写」（Michelle 事件在 ch30:156、ch32:315 才展开）。
- **F-18-4**｜「第一次让我感到"能干、尽在掌控"」（md:10／md:152）站得住：`/usr/bin/grep -rni -w 'competent|capable|in control|a natural'` 全书 ch01–ch17 无「她自觉胜任工作」的先例（ch11:117 是 Virginia 的期许、ch10:105 的 `a natural` 说的是 Gazzie 口中正在学打枪的 Ida（见 ch10:100 那问 So Ida just…bought a gun）、ch19:174 在下一章）。
- **F-18-5**｜md:44「copy（复制品）…主肖像在别处」由 :150 `the copy of Ida Greer’s main portrait` 蕴含。
- **F-18-6**｜md:33「proverbial…自嘲式地点明"火坑"是套话」贴合 :51 的用词位置。
- **F-18-7**｜块 3 的 `…` 拼接两段（:150 首两句＋末句）由机器层独立取证通过；整串 flat 比对不适用，勿因「查无 0」就认定该块可直接合并。
- **F-18-8**｜词表 15 行例句全部逐字在 text/ 中（0 MISS）；`scutes`／`bathwater`／`baseball bat` 三行的释义与原文用法相符。
- **F-18-9**｜md:64 关于 `already smeared` 的时态读法成立（:198 `like alligator guts were already smeared across my shirt`——厌恶先于污迹）。
- **F-18-10**｜md:24「怒气在开场前就已成立」由 :9 `before I could say a word` 支撑，不依赖被 C-18-1 撤掉的「摔门」。
- **F-18-11**｜md:116 后半「直到这里我才把话头拿去赌」的**判断**本身与 :381 的 `hoping the statement was vague enough to fool him` 相符；C-18-8 只打「一问」与「此前被动」两处口径，不要把这句删掉。
- **F-18-12**｜md:46「连 Harrison 之后也承认她让人发毛」的「之后」时序正确（:156 > :150）。
- **F-18-13**｜导航内嵌引语的**短语本身**逐字正确：md:11 的 `I just wanted to get through the day`（:9）、`Mama would have been furious`（:354）、md:13 的 `With the knife in my hand, I felt competent, in control`（:345）三处无误；md:13 的 `You’re good at saying the opposite of what you feel` 短语同样正确，**只差撇号字形**（已列 C-18-13，修字形时不要动词序或标点）。

## 不许裁决（本章留白，任何一轮都不许替原文作答）

1. 走廊上「陌生的声音」是谁（:9 只写她归因于焦虑；回指 ch17 末 `soft, feminine`）。
2. 死去的鳄鱼头上那道 `gash`（:243）具体由谁、以何造成——本章只让她想象棒球棒（:243）。
3. Joe 那句 `Brought his family secrets along, too`（:210）之外还有没有别的秘密；Harrison 自己把它限定为 `Feed mixtures, egg vendors`（:216）。
4. Joe 对她祖母的厌恶是否即性别歧视——:231 是她自己的猜测（`Let me guess.`），:234 Harrison 只补了一句。
5. 盗皮者身份与数量：:390 `“Mmm,” he said evasively. “Nothing to worry about.”`——数目本章不给。
6. 偷皮是否与 grow-out barn 那次（:192 `After my illicit trip to the grow-out barn`）或 ch12:141 的孤立待遇有关——原文无连接。
7. Harrison 半句 `You don’t really think—`（:141）想说什么；以及他是否知道昨夜她闯过 Leon 的房间（:126 她自陈 invaded，原文未写他知情）。
8. Michelle 事件的经过与责任——本章只给颜色与操场。
9. `probably Joe` 腌皮（:360）是 Harrison 的推测，不是排班事实。
10. 天花板病害与 Greer House 的嗡鸣／裂缝是否同源——全书一律不裁决。
11. :378 那次 Nova 与 Gazzie 的悄声交谈内容（且本章之前的 text/ 查无该场景）。

## 跨章取证（本轮实际用到的外部锚点）

- ch02:53 祖母＝Gazzie（F-18-1）
- ch04:279／:282 曾曾祖母＝Ida 的等式由叙述者自己提出（T-18-15）
- ch08:153 一万四千头已在场（C-18-9）
- ch11:117 `she sees you’re capable`（F-18-4）
- ch12:39 屋顶漏水＝常态的首次判读；ch12:51／:63／:111／:141 文件工作自 ch12 起（C-18-2／T-18-10）
- ch13:48 dryer sheets 首次落地（C-18-11）
- ch17:33 闻他 T 衫、:45／:105 摔门、:90 衬衫上的血、:105 锁箱、:120 女声（C-18-1／:66 行对应 :18 的 :66 `red splash across her shirt last night`）
- ch30:156／ch32:315 Michelle 事件后文才展开（F-18-3）
