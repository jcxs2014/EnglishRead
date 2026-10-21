# 第 16 章 R3–R4 差异单（人工审查）

- **审查对象**：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch16 chapter 16.md`（161 行，8 个引语块，modified 2026-10-21）
- **唯一真值**：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch16_chapter_16.txt`（66 行 / 20160 字符）
- **机器层**：`review/ch16/2-machine.json`（已存在，未改动）——`verdict: ok`；8 块全 `ok=true`；`counts`：blocks 8 / quote_long 0 / segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0 / template 0 / keyword_long 5 / hole 0；`issues` 仅 `keyword_long` 5 条（块 2/4/5/6/7），非阻断。
- **流程**：先素读原文并落 `review/ch16/1-suread.json`（R1），再开成品 md 对照（R3–R4）；本轮只出指令，**未改动任何 md 文件，git 未执行任何操作**。
- **行号约定**：`text/ch16_chapter_16.txt:NNN`＝原文行号；`ch16 chapter 16.md:NNN`＝成品 md 行号。字符区间为原文解码后的 `[start,end)`。
- **本轮口径**：本章 md 已经过一轮修复。父代理已代修并要求记为**已修复**的四条，本单**不再列为待改**：① md:21「圣诞老人会在树里接待客人」（原为「坐在树里」）；② md:27「……（原文说那并不是门，只是一个门框，人从外面就能看见里面）」（原为「只留一扇门」）；③ md:39「……原文没有点破」（原为「这些挪动的污渍其实是别的女人——本章后面才说破」）；④ md:99「……原文没有交代是谁、又用什么手段处理的」（原为「一直有人在替这些女人做手术」）。以上四条经本轮回原文复核**均已成立**（另见 `4-verdict.md` §4 防误修清单）。

---

## 一、漏（L）

### L1【提示】女人们要推倒商场那扇沉重铁门、迎接「圣诞正式开始」——本章的动机高潮，md 全文未出现

- **原文侧**（`text/ch16_chapter_16.txt:48`，字符区间 [14237,16089)）：`"…they were walking to the mall door to knock it over, to leave that place, and to mark the official start of Christmas. One of the few times of the year when the void didn't feel so close by, when they felt full because they had a million things to do, and they knew how to do them better than anyone. There was no way a horde of women could fail to bring down the heavy metal Splau door while their friends and family watched the kids and held their purses."`
- **md 侧**（`ch16 chapter 16.md`）：全文检索 `铁门` / `推倒` / `圣诞开始` / `official start` 均命中 **0**；md:11 只写到「几百个和她一样的女人从各个店铺涌出来合声尖叫」，md:15 提到「用一连串并置的意象推进」，均未触及这一动机。
- **影响**：这一段是「回家过节」这条线在整章里的最高点——几百个女人一起奔向门口，要把商场推倒，好让圣诞正式开始。md 缺它，本章的结局就只剩「涌出来 + 尖叫」，读者看不到她们**要做什么**，因而看不懂 :51 为什么全体转身堵住出口（她们不是要逃，是要**留下来**）。
- **修法**：在 md:14（人物弧线）或 md:109 末段补一句原文事实，例如「她们是奔着商场那扇沉重铁门去的——要推倒它，好让『圣诞正式开始』；可最后她们堆在门口转过身来，陪着的人全散了，只剩她们和她」。

### L2【提示】女人们的动机是 Alba 的「投射」，md 没写——读者会把「她们都想回家」当成客观事实

- **原文侧**（`text/ch16_chapter_16.txt:48`，区间 [14237,16089)）：`"She was projecting her desire to leave on the women—to be home shortly, to wrap up the Switch controllers while the kids slept, to nestle them under the tree. She had no doubt those women yearned for the same, that they were walking to the mall door to knock it over…"`
- **md 侧**（`ch16 chapter 16.md`）：全文检索 `投射` / `projecting` 命中 **0**；md:11、md:14、md:15 均把「几百个女人涌出店铺」写成客观场面，没有点明这是 Alba 单方面把自己的离意投射到她们身上、且只是「她毫不怀疑」她们也这么想。
- **影响**：原文把「几百人都想回家」写成**主观的确信**，是本章最刻意的反讽之一（她们其实要留下）。md 不点破，读者会把投射当事实，正好丢掉这一层。
- **修法**：在 md:109 或 md:14 补一句，例如「这一切其实来自她的投射——是 Alba 把自己想回家的念头投到那些女人身上，并且毫不怀疑她们也想回家」。

### L3【提示】陪同者集体消失、女人们转身堵住出口（本章唯一一次「局势彻底反转」），md 全文未出现

- **原文侧**（`text/ch16_chapter_16.txt:51`，区间 [16092,16883)）：`"The tentacles fell to either side of Alba's body, as if they'd been suspended with threads someone had suddenly cut… She heard the collective scream once more, more intense than ever. More furious, and more desperate. Alba looked back toward the mall entrance and saw all those women, hundreds and hundreds, heaped against the door but turned toward her and staring. Their companions were gone. They were alone. Jaws unlatched, tongues pale, eyes wide open. They seemed to have no intention of leaving, or allowing Alba to."`
- **md 侧**（`ch16 chapter 16.md`）：全文检索 `陪同者` / `陪同` 命中 **0**；md:85 只把块 6 当作「深情」来解读，没有写 :51 的反转——陪伴者不见了、几百个女人堆在门口却转身盯着 Alba、明显不打算放她走。
- **影响**：这是本章从「被围观」到「被围困」的转折点，也是块 6「深爱」的对照面（:36 的陪伴者 vs :51 的消失）。md 缺它，块 6 的「被爱」就没有反面，读者也读不出 :63 她们成群走向 Alba 的可怕。
- **修法**：在 md:85 或 md:109 补一句，例如「可等触手落地，她们身边的陪同者全不见了——几百个女人堆在门口，却转过身来盯着她；她们哪儿也不打算去」。

### L4【提示】「没有人拍手 → 灯不亮 → Alba 模仿孩子自己拍手 → 灯亮」这条因果链，md 只剩半句

- **原文侧**（`text/ch16_chapter_16.txt:39`，区间 [11707,12714)）：`"The mall lights shut off again, as did the lights outside and the ones on the Christmas tree… No one clapped to turn the lights back on."`；`:57`（区间 [16934,18218)）：`"She thought of her kids clapping and dancing in restrooms, the incredible choreography they invented to wake up the sensor. She wanted that again. So she clapped. And the lights turned on."`
- **md 侧**（`ch16 chapter 16.md`）：md:75 只写「光源之后会变成刑具，而灯还会再灭一次」；全文检索 `拍手` 命中 **0**（仅 :128 词表例句出现 `clapping`）。
- **影响**：这一组呼应是本章最漂亮的一处结构（Alba 用自己孩子唤醒商场洗手间感应器的那套动作，替全场点亮了灯——`ch16:57` 的 `choreography…to wake up the sensor` 接 `ch11:9`）。md 缺了它，:39/:57 的因果就断了，读者也看不出 Alba 最后那一下拍手是她唯一还能做的、也是最像人的动作。
- **修法**：在 md:75 或 md:109 补一句，例如「灯灭后没人拍手，灯就再也亮不起来——直到她想起孩子们在商场洗手间里为唤醒感应器自创的那套拍手动作，自己拍了起来，灯才重新亮」。

### L5【提示】卡门在黎明前叫车送 Alba 去急诊的回忆（本章唯一的母亲线），md 全文未出现

- **原文侧**（`text/ch16_chapter_16.txt:33`，区间 [9162,10561)）：`"It was exactly what Carmen must have seen each time Alba had a panic attack. She didn't want to think about what her mother must have felt last time, a few months ago, when she'd called a cab before dawn to take Alba to urgent care. She imagined herself, at age seventy, waking up to the landline ringing at three in the morning… crossing the Ronda traffic circle alone in the middle of the night so she could go to the clinic with Alba. Juan couldn't have gone with her because someone had to stay with the kids. She'd thought that was just how it had to be. No one had even suggested that it'd be better if he had gone with her, since he could have driven them, and Carmen could have stayed at their place with the children. Not even Carmen thought of it. Of course she was going to go."`
- **md 侧**（`ch16 chapter 16.md`）：全文检索 `卡门` / `Carmen` / `急诊` / `urgent care` / `母亲` 命中 **0**（md 全文没有出现「卡门」这两个字）。
- **影响**：这是「陪着＝爱」的**原始样板**——母亲半夜独自送女儿去急诊，连「换个人陪」都没人想到，于是她成了那个「从不缺席的人」。md:87 已经把块 6 判成「全书的题解」，却没有这块样板撑着，题解就成了空转。
- **修法**：在 md:87（块 6 读者视角提示）或 md:85 补一句，例如「这个样板在更早的夜里已经出现过一次：阿尔巴恐慌发作，卡门三更半被座机叫醒，独自穿过 Ronda 交通环岛送她去急诊——连『让 Juan 陪、卡门留下看孩子』都没人想到过」。

### L6【提示】陪同者里连孩子和婴儿都骨瘦如柴、成年人不超过九十磅——「陪伴者也是受害者」的量化依据，md 只做了解读没有事实

- **原文侧**（`text/ch16_chapter_16.txt:36`，区间 [10563,11705)）：`"Like the Diana inside the tree, all of them looked frail. They were skinny, hollow, haggard. Even the children. Even the babies. They were swimming in their clothes, their bones sticking out… None of the adults could have weighed more than ninety pounds."`
- **md 侧**（`ch16 chapter 16.md`）：md:81／md:85 只把块 6 的引语译成「出于惯性…当成理所当然」的解读；全文检索 `婴儿` / `九十磅` / `骨瘦如柴` 命中 **0**（`:155` 词表里有 `babies` 的例句 `Even the babies.`，但正文没有）。
- **影响**：原文先给恐怖事实（婴儿也骨瘦如柴）再给深情（他们从不抱怨）；md 只留深情那一半，读者会以为陪同者只是「习惯性陪伴」的普通人，少了「陪着她的人同样是受害者」这层。
- **修法**：在 md:81（块 6 中文理解）补一句事实层，例如「而这些陪同者自己也已经被消耗殆尽：连婴儿都瘦得只剩骨头，成年人没有一个超过九十磅——他们能这样陪着，是拿自己的身子在陪」。

---

## 二、编（C）

### C1【提示】md:97 残留「术后痕迹」「被处理过的残根」——原文只写「被切掉」，全书没有任何手术或处理的描写

- **原文侧**（`text/ch16_chapter_16.txt:42`，区间 [12716,14164)）：`"From where she was lying, she could see some of the women's uncovered bellies. Where she thought there should have been tentacles, there were scars. Or in some cases, tiny stumps: small, fleshy appendages that had been cut and hadn't yet healed. That's why they scream, she thought."`——原文只交代**痕迹**（scars / tiny stumps / `had been cut`），既没说**谁**切的，也没说用什么手段切的。同句 `That's why they scream, she thought` 是 Alba 的**猜想**（`she thought`），不是叙述者给的因果定论。
- **md 侧**（`ch16 chapter 16.md:97`）：`……反转不在「多」，而在「少」：满地都是被处理过的残根，等于宣告这些女人全都曾经和阿尔巴一样。触手在这里从超自然之物变成术后痕迹，因果关系被一下子摆平。`
- **影响**：三处越界：①「术后痕迹」给「被切掉」安上手术（surgery）这个原文没有的施动者；②「被处理过的残根」同义重复同一个推断；③「满地都是」「这些女人全都」与原文的 `some of the women's uncovered bellies`、`Some of them showed the stumps on their abdomens`（:63）冲突——原文明说是「一部分」。另外「因果关系被一下子摆平」把 Alba 的猜想说成了作者的定论。**注**：父代理已把 md:99 的「一直有人在替这些女人做手术」删掉（已修复），但同一推断仍留在 md:97，本条要修的正是这一处残留。
- **修法**：把 md:97 改成 `……反转不在「多」，而在「少」：她躺着看见的那些裸露的肚皮上，长着触手的本该是触手的地方只剩疤痕，有些则是被切掉、还没长好的肉芽——残根说明这些女人全都曾经和阿尔巴一样；触手在这里从超自然之物变成了一处伤口，原文只写「被切掉」，没有交代是谁、也没有交代用什么手段。而「That's why they scream」是她的猜想，不是作者的定论。`（保留「全都曾经和阿尔巴一样」这层判断可以，但把主语限定回「她看见的那些女人」，并删掉「术后」「被处理过」两个词。）

### 其余断言已核，无编造

- 已核断言（回原文逐条比对，全部成立）：md:21「圣诞老人会在树里接待客人，问他们乖不乖、想要什么礼物」→ :6「Santa Claus would welcome visitors there, asking if they'd been good and what gifts they wanted」（`there` 指树内，同段「customers could enter the tree freely」）——成立；md:27「那并不是门，只是一个门框，人从外面就能看见里面」→ :6「It wasn't really a door; it was just the frame.」＋「You could see the heart of the tree from the outside」——成立；md:39「原文没有点破」→ :9「She didn't know who they were, but she didn't intend to look and find out.」——成立；md:99「原文没有交代是谁、又用什么手段处理的」→ :42（全书 grep `surg|scalpel|operat|incision` 仅命中 `ch02:177` 的 `surgical tape`，无任何手术描写）——成立；md:45「被抽干之后的戴安娜」→ :15「Diana, or a gloomy version of Diana… colorless, soulless」——成立；md:49「想抱这个版本的姐姐，脚却不听指挥」→ :15「Alba wanted to hug this emaciated version of her sister, but her feet wouldn't respond to her command.」——成立；md:51「大学第二年绝食」→ :15「when Diana quit eating her second year of university」——成立；md:57「拇指和食指掐住身旁那个女人的腿」→ :18「she stretched out her thumb and index finger and pinched her thigh」（被掐者是 `the woman beside her`）——成立；md:69「斯普劳变成一张狼嘴」→ :24「Splau became the mouth of a wolf」——成立；md:93「一截被切掉、还没长好的肉芽」→ :42——成立；md:105「五个词」「那两只手柄」→ :66「I just wanted the controllers.」（5 词）＋ `ch11:99`「one red and the other blue」——成立；md:109「那只装着手柄的盒子」→ :60「the box would remain intact」——成立；md:15「商场保洁」→ :60「When the cleaning staff found her」——成立；md:11「两个和她一模一样的人」→ :24「her own face, twice duplicated, broken in two different ways」——成立；md:81「出于惯性…当成理所当然」→ :36——成立。
- 词汇表 29 条例句已逐条比对（规范化引号/破折号/省略号后做本章 text 子串匹配）：`rows checked=29 not_verbatim=0`——无编造例句。

---

## 三、错（W）

### W1【提示】md:11「合声尖叫」与 md:61「全体同步的尖叫」——原文里明确同步的是掌声，不是尖叫

- **原文侧**（`text/ch16_chapter_16.txt:18`、`:21`、`:24`、`:48`）：尖叫的描写是 `The cries grew louder, multiplied, surged through the mall`（:18）、「all with identical grimaces, jaws unhinged, the scream passing through their bodies」（:21）——**放大、倍增、表情一致**；真正写了同步的是掌声：`"All the women had raised their arms in the air at once, and they clapped in perfect synchrony."`（:24）。`Hundreds and hundreds`（:48）只写人数，没写整齐。
- **md 侧**（`ch16 chapter 16.md:11`）：`……几百个和她一样的女人从各个店铺涌出来合声尖叫……`；`ch16 chapter 16.md:61`：`……触发机制只是「掐一下」这样的小动作，得到的却是全体同步的尖叫：个体动作被放大成集体噪音。`
- **影响**：md 自己也知道这一点——md:13 的导航写的是「尖叫也反转成几百人同步的掌声」，与 md:11/md:61 的「合声／同步的尖叫」自相矛盾；读者会记错本章最关键的那个反转（同步的是掌声）。
- **修法**：md:11 把「合声尖叫」改成「涌出来尖叫」；md:61 把「全体同步的尖叫」改成「被放大的集体噪音」，并把「同步」留给 :24 的掌声。

### W2【提示】md:39「全章她都在回避被认出」——后半个场景她正是全场焦点

- **原文侧**（`text/ch16_chapter_16.txt:9`、`:51`、`:63`）：`:9` 她想的是「只要自己不看她们，她们就不会发现她」（`staring up at the star`）；但 `:51` 几百个女人「heaped against the door but turned toward her and staring」；`:63` 她们「were now resolute and walking toward her en masse」，她随后穿过人群。
- **md 侧**（`ch16 chapter 16.md:39`）：`……记住这份不肯看：全章她都在回避被认出。`
- **影响**：把「开篇的自我隐蔽」说成「全章状态」，与她成为全场目标、被围观被围堵的收束冲突。
- **修法**：把末句改成 `记住这份不肯看——开篇她靠不看别人来躲避被认出；而这一夜最后，是所有人在盯着她。`

### W3【提示】md:63「本章之后它还会再出现」——第 17 章没有同一声音的回扣

- **原文侧**（`text/ch16_chapter_16.txt:18`）：`an awful moaning emerged from their mouths, the same sound Alba had heard before, which had brought her here in the first place`。全书检索 `moan/moaning` 仅命中 **ch16:18** 与 **ch16:39**；**ch17** 里与声音相关的只有 `sound`（:24、:318、:348）、`howling`（:63）、`crying`（:321），没有同一声闷哼的回扣。
- **md 侧**（`ch16 chapter 16.md:63`）：`作者明说这是阿尔巴「以前听过、并且因此被引来」的声音——记住它的出处，本章之后它还会再出现。`
- **影响**：这是一个关于后文的预测，全书文本不支持——第 17 章没有再出现这声闷哼。读者按提示去找会落空。
- **修法**：把后半句改成 `记住它的出处：那不是本章才有的声音，是她早就听过、并且因为它才走到这里。`（若确实要预告，得另找依据，例如 ch17 里「圣诞树下」的场景；本轮 grep 未找到对应回扣。）

### W4【提示】md:51「原文紧接着让阿尔巴想起姐姐大学第二年绝食的事」——原文里回忆在拥抱**之前**

- **原文侧**（`text/ch16_chapter_16.txt:15`，区间 [1811,3951)）句序：`She thought back to when Diana quit eating her second year of university, how her naked body looked when Alba walked into the bathroom without knocking…` → `Alba wanted to hug this emaciated version of her sister, but her feet wouldn't respond to her command.`（**先回忆，后拥抱**）
- **md 侧**（`ch16 chapter 16.md:49` → `ch16 chapter 16.md:51`）：md:49 说「作者还特意让阿尔巴『想抱这个版本的姐姐，脚却不听指挥』」；md:51 紧接一句「原文**紧接着**让阿尔巴想起姐姐大学第二年绝食的事」。
- **影响**：读者按 md 的顺序读，会以为原文是「拥抱 → 想起绝食」；实际是「想起绝食 → 拥抱」。这一处的因果方向（是旧伤让她认出这是姐姐）被倒过来了。
- **修法**：md:51 改成 `原文其实先写她想起姐姐大学第二年绝食的样子，再写她想拥抱这个版本的姐姐——旧伤和今夜的消瘦被并排放着，因果由读者自己完成。`（或把 md:51 这句删掉，保留「大学第二年绝食」的事实即可。）

### W5【提示】md:45「树里的第三个人不是别人，是戴安娜」——「第三个人」易被读成「三个人里的第三个」

- **原文侧**（`text/ch16_chapter_16.txt:15`）：`There were three of them. Two sitting on the same bench, and one on the other. … The one sitting alone had raw skin around her eyes … The woman across from her, who was identical, was suffering through a nosebleed. … That duplicated woman was Alba herself. And the one sitting next to her was Diana, or a gloomy version of Diana.`
- **md 侧**（`ch16 chapter 16.md:45`）：`树里的第三个人不是别人，是戴安娜，或者说，是被抽干之后的戴安娜：苍白、骨瘦如柴……`
- **影响**：原文给 Diana 的定位是「**坐在她旁边的那一个**」（`the one sitting next to her`）；md 用「第三个人」描述她，读者很可能理解成「三个里的第三个」，而原文的顺序是：独坐那个（眼周皮肤红肿）→ 对面那个（流鼻血的复制体＝Alba 自己）→ 旁边那个（Diana）。位置关系（谁在对面、谁在旁边）是本章最易错的信息之一。
- **修法**：md:45 首句改成 `树里那个坐在她旁边的女人不是别人，是戴安娜，或者说，是被抽干之后的戴安娜：……`（并保留「对面那个才是 Alba 的复制体」这一对照，见 §4）。

### W6【提示】md:73「全书的核心母题」与 md:87「全书的题解」、md:111「全书的题眼」三处互相冲突

- **原文侧**：`text/ch16_chapter_16.txt:24`（同一张脸裂成两种样子）、`:36`（被爱却看不见）、`:66`（我想要的不过是那两只手柄）——原文并没有「给全书定一个母题」的动作，这是成品 md 的解读层。
- **md 侧**：`ch16 chapter 16.md:73`：`紧接着作者又把全书的核心母题摆上台面——同一张脸可以裂成两种样子，她和她的复制品并不相同。`；`ch16 chapter 16.md:87`：`这句话可以当成全书的题解：不要让身边的人独自待着…`；`ch16 chapter 16.md:111`：`这是全书的题眼：……`
- **影响**：一章之内三次把不同内容说成「全书的核心／题解／题眼」，读者无法判断哪一处才是作者要认领的那一个；其中 md:73 把「同一张脸裂成两种样子」抬成核心母题，与书名本身（`Don't Leave Her Alone`）指向的「不要让人独自待着」直接抵触。
- **修法**：把 md:73 的「全书的核心母题」降级为「本章的第二条母题」或「作者又一次把同一张脸劈成两种样子」，把「全书的」这三个字留给 md:87（题解）与 md:111（题眼）；若要保留「核心」二字，建议改挂到 :36 那段（陪伴与被看见），并在 md:87 注明二者同源。

### W7【提示】md:87「「她总在我身边」正是你以为的证据」——措辞退让，容易读成「陪伴只是你的错觉」

- **原文侧**（`text/ch16_chapter_16.txt:36`）：`They did it out of a deep affection she hadn't recognized, and since she hadn't recognized it, she had taken it for granted.`——**深情是实在的**，问题出在 Alba「没认出来」，所以「当成理所当然」。
- **md 侧**（`ch16 chapter 16.md:87`）：`这句话可以当成全书的题解：不要让身边的人独自待着，因为「她总在我身边」正是你以为的证据。`
- **影响**：「正是你以为的证据」这句话的宾语含混——既可读成「你以为的证据（＝你当作理所当然的那份在场）」，也可读成「你以为的证据其实是假的（＝陪伴是幻觉）」。后者与原文 `a deep affection` 冲突，会把本章的情感核心读反。
- **修法**：改成 `这句话可以当成全书的题解：不要让身边的人独自待着——「她总在我身边」只是你以为的证据，那份深情其实一直在，你只是从来没认出来。`

---

## 四、交叉说明

1. **树里三个女人的身份链（本章最易错的一处，md:45 需改）**（`text/ch16:15`）：三人 ＝ ①**独坐另一条长椅**的、眼周皮肤红肿得睁不开眼的那个（`:15`）；②**坐在 Alba 对面**、流鼻血的「identical」女人＝**Alba 自己的复制体**（`That duplicated woman was Alba herself.`）；③**坐在 Alba 旁边**、苍白骨瘦、戴 Alba 婚礼上送的戒指的那个＝**Diana，或阴郁版的 Diana**（`And the one sitting next to her was Diana, or a gloomy version of Diana.`）。到 `:24`，这两张「她自己的脸」被并置成 `her own face, twice duplicated, broken in two different ways`——一张眼周皮肤被剥掉、一张流鼻血。成品 md:11「两个和她一模一样的人」与 :24 吻合，成立；但 md:45 的「第三个人」说法要改（见 W5）。
2. **称呼链**：`:18`「the woman beside her」（被 Diana 掐腿的那个女人）≠ `:15`「the one sitting next to her」（坐在 Alba 旁边的 Diana）——两处 `next to`／`beside` 指向不同人；`:60`「When the cleaning staff found her, she'd be unrecognizable」中的 `her`＝**Alba**；`:51`「Their companions were gone. They were alone.」的 `they`＝**那群女人**（不是 Alba）；`:42`「That's why they scream, she thought」的 `she`＝**Alba**、`they`＝**那群女人**。
3. **时间轴链**：本章＝**平安夜当晚、Splau 关门之后的深夜**，与第 15 章同一夜（`ch15:93`「It's Christmas Eve」、`ch15:96`「There are people who work on Christmas Eve」）。本章内部的相对时间：`:24`「Minutes passed and then, all at once, they stopped」→ `:27` 灯亮 → `:30` 恢复日常 → `:39` 灯再灭、触手剖腹 → `:42` 灯亮 → `:45` 触手停 → `:48` 女人们奔向门口 → `:51` 触手落地、陪同者消失、她们转身 → `:54` 尖叫停止、灯灭 → `:57` Alba 拍手、灯亮 → `:60` 她掏出手柄盒 → `:63` 触手重新发光、她穿过人群 → `:66` 最后一句。**另有一个回忆时间点**：`:33`「a few months ago… called a cab before dawn… three in the morning」（卡门送 Alba 去急诊的那夜），本章两处「当下」与这一处「几个月前」不可混。
4. **跨章事实（跨章引用必须标章号）**：
   - `text/ch16:57`「the incredible choreography they invented to wake up the sensor」接 **ch11:9**（商场洗手间感应器：灯灭时孩子们跳一段、拍手），并被 ch15:138 Diana 的「I'd still be crying in the bathroom」反向呼应。
   - `text/ch16:42`「an oversized version of what Alba and Diana put on their kids' bedside tables」接 **ch14** 送手柄那条线（本章不点孩子名，只用 kids）。
   - `text/ch16:66`「the controllers」接 **ch10:93–96**（Alba 为 Switch 手柄折回 MediaMarkt）、**ch11:99**（`one red and the other blue`，两只手柄）、**ch15:81**（Diana「she did get the controllers in the end」），并在 **ch17:48** 收尾（Alba 把手柄扔进大垃圾袋）。
   - `text/ch16:42` 的 `tiny stumps…had been cut` 与 **ch17:282–285**（Alba「It was a tentacle, Mom. I had two.」／Diana「an octopus tentacle」）互为另一侧的证据；**ch17 同样没有手术描写** ⇒ C1 的「术后」写法在全书口径上也是孤例。
   - `text/ch16:33` 的卡门线接 **ch15:42**（卡门承认当年胃里的章鱼）、**ch15:117**（营地的夏天）与 **ch17** 的母亲自白；**ch15** 的「陪着你却不被看见」在本章由 :36 升级成 :51 的失去。
   - `text/ch16:24`「Splau became the mouth of a wolf」的商场名写法与全书一致（`Splau` 是正文英文原名，中文叙述层全书用「斯普劳」：`00_概述.md`、`00_金句精选.md`、`00_情感节点.md`、ch16、ch17）⇒ md:69 的「斯普劳」**成立，不要**改成 Splau，也不要把 md 里的英文引文 `Splau` 改成中文。
5. **体例说明**：本章 md 块间有 `---` 分隔（9 行），与 ch00–ch11、ch17 一致；ch12–ch15 没有。两种写法都在本书内并存，**不算形态偏离**，此处只作记录。

---

## 五、修后复核

改完 `ch16 chapter 16.md` 后，按顺序跑下面这组命令。

```bash
MD="notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch16 chapter 16.md"

# 1) C1：手术/处理过的推断必须消失（期望 exit=1）
/usr/bin/grep -n "术后痕迹" "$MD"   # 期望 exit=1
/usr/bin/grep -n "被处理过的残根" "$MD"   # 期望 exit=1
/usr/bin/grep -n "因果关系被一下子摆平" "$MD"   # 期望 exit=1

# 2) W1–W7：旧措辞必须消失（期望 exit=1）
/usr/bin/grep -n "合声尖叫" "$MD"   # 期望 exit=1
/usr/bin/grep -n "全体同步的尖叫" "$MD"   # 期望 exit=1
/usr/bin/grep -n "全章她都在回避被认出" "$MD"   # 期望 exit=1
/usr/bin/grep -n "本章之后它还会再出现" "$MD"   # 期望 exit=1
/usr/bin/grep -n "原文紧接着让阿尔巴想起姐姐大学第二年绝食的事" "$MD"   # 期望 exit=1
/usr/bin/grep -n "树里的第三个人不是别人" "$MD"   # 期望 exit=1
/usr/bin/grep -n "全书的核心母题" "$MD"   # 期望 exit=1
/usr/bin/grep -n "正是你以为的证据" "$MD"   # 期望 exit=1

# 3) L1–L6：补充句落地（期望 exit=0 且命中 ≥1）
/usr/bin/grep -n "铁门" "$MD"   # 期望 exit=0（:48 推门/迎接圣诞开始）
/usr/bin/grep -n "投射" "$MD"   # 期望 exit=0（:48 Alba 的投射）
/usr/bin/grep -n "陪同者" "$MD"   # 期望 exit=0（:51 陪同者消失 / :36 陪同者）
/usr/bin/grep -n "九十磅" "$MD"   # 期望 exit=0（:36）
/usr/bin/grep -n "急诊" "$MD"   # 期望 exit=0（:33 卡门回忆）
/usr/bin/grep -n "拍手" "$MD"   # 期望 exit=0（:39/:57）

# 4) 父代理已修复的四条不得被改坏（期望 exit=0）
/usr/bin/grep -n "会在树里" "$MD"   # 期望 exit=0
/usr/bin/grep -n "并不是门，只是一个门框" "$MD"   # 期望 exit=0
/usr/bin/grep -n "原文没有点破" "$MD"   # 期望 exit=0
/usr/bin/grep -n "原文没有交代是谁" "$MD"   # 期望 exit=0

# 5) 门禁
bash scripts/chapter.sh "$MD" --json   # 期望退出码 0
```

补充说明：

- 补写 L1–L6 时挂在**已有的四个子项行**（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）上，**不要新开子项、不要改块数**（块数 8，落在 3–10 内）。
- W5 改 md:45 时，注意不要破坏块 3 的引语行（md:43）与关键词行（md:47）。
- 补写后建议重跑词表逐字校验（`## 本章词汇` 29 条例句必须仍是本章 text 的逐字子串）；若顺手改了词表，务必重新核。
- 本单只出指令，未改动任何 md 文件；git 未执行任何操作（未 add / 未 commit / 未 push）。
