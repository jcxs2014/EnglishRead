# 3-diff.md · 《Victorious》第 46 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch46_chapter_i.txt`
- 受审 md：`ch46 eli wakes and meets gabriel.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（claims not to be Eli’s enemy and says he will have Eli’s coo）
- **原文**：原文 L270：“I’m not your enemy, Eli,” he said. “You’ll see that soon enough. In the meantime, it would be better for us both if you accept that you can’t hurt me.” This time, there was force behind the words. Eli felt the order cinch around him. “I would prefer to have your consent. But I will have your cooper
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L270：原文 L270 的事实「claims not to be Eli’s enemy and says he will 」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（37 词 3 句）：He had the vague sense that he’d been dreaming—though of what, he couldn’t say. Slowly, he sat up, scraping a hand over his face. His limbs and mind felt leaden, sluggish, as if still disentangling from sleep.
- 中文理解：他隐约觉得自己做了梦，可梦见了什么说不出来。他慢慢坐起来，一只手在脸上抹过。四肢和脑子都沉、都钝，像还没从睡眠里挣出来。
- 关键词：vague sense · scraping a hand
- 为什么这样写：这一段先给身体。sat up、scraping a hand over his face、leaden、sluggish 一路都是慢动作，读者跟着他一节一节醒过来。破折号后的 though of what, he couldn’t say 把记忆的空缺直接摊在开头，不解释、不追问。末句把「沉」与「像还没从睡眠里挣出来」放在一起：感觉上他只是刚睡醒，可这一觉本该有来处。
- 读者视角提示：这里只写了「像刚睡醒」，没写他睡了多久，也没写他身在何处。读者拿到的是一具发沉的身体，位置与时间都还空着。
- **原文**：原文 L27-L27
- **结论**：引语 3 句 37 词（原文 L27）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（35 词 2 句）：Eli closed his eyes, trying to remember where he’d been before, what he’d been doing, and was unnerved when his mind supplied only a flat expanse of black. As if the memories had been excised.
- 中文理解：伊莱闭上眼，想记起自己之前在哪儿、在做什么；脑子里只递出一片平的黑，这让他心里发毛。像那些记忆被人剜掉了。
- 关键词：unnerved · flat expanse of black
- 为什么这样写：句子用一个动作串起结果：closed his eyes → trying to remember → was unnerved。中间两个并列成分都不是问句，而是他要翻找的内容，读起来像他在自己脑子里摸索。supplied 这个词把脑子写成供货的一方，它只肯交出 black，还是 flat 的一片。末句用被动语态 had been excised，空缺因此像是有人动过手，而不是他自己忘了。
- 读者视角提示：他先问自己是怎么失去意识的、又失去意识了多久，然后才闭眼去翻记忆——翻到的是一片空。读者和他同时撞上这块空缺，此刻还没有人替他解释。
- **原文**：原文 L42-L42
- **结论**：引语 2 句 35 词（原文 L42）：中文理解逐句对得上，主语=伊莱、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（48 词 2 句）：The sound seemed to come from everywhere, but a moment later, the wall to his left turned from green to glass, revealing a man he’d never seen before. Calm, but confident, salt-and-pepper hair swept back, sleeves rolled to his elbows, eyes dark behind a pair of wire-frame glasses.
- 中文理解：声音像从四面八方来；过了一会儿，他左边的墙由绿变成玻璃，露出一个他从未见过的男人。那人神色平静而带把握，花白的头发往后梳，袖子卷到手肘，深色的眼睛架在一副细框眼镜后面。
- 关键词：green to glass · sleeves rolled
- 为什么这样写：先写声音、后写来源，把「先听见、再看见」的次序留着，读者和他一起转头。墙从 green 变 glass，一个颜色的替换就完成了隔断的打开，不必另写机关。后半句用四个短并列写这个人：Calm, but confident、hair swept back、sleeves rolled、eyes dark behind glasses，每个短语各管一处，凑成的是一张不动的像，不是一串动作。
- 读者视角提示：这一段只有外观，没有名字，也没交代他是谁；「从未见过」是伊莱此刻的判断。读者的信息和他一样少——直到后半章他自报身份：先是「A man searching for answers」，接着「In short, a therapist」，最后才是那句分量最重的「And EON’s new director」。
- **原文**：原文 L96-L96
- **结论**：引语 2 句 48 词（原文 L96）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=玻璃，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（46 词 3 句）：Panic churned inside his chest, but anger rushed to meet it. Because maybe there had been something, a higher plane, too great to comprehend on waking. Maybe, but if there was, its memory was lost to him, stripped back by this involuntary resurrection, this unnatural return.
- 中文理解：恐慌在胸口翻，怒气紧跟着冲上来。因为也许真有过什么：一个更高的层面，大到醒来时无法理解。也许有；可就算有，那份记忆也已经丢了，被这次不由他做主的复活、这次不合常理的返回抹掉。
- 关键词：Panic churned · involuntary resurrection
- 为什么这样写：先说 panic，再用 but 把 anger 拉进来，两种情绪并排站着，谁也不压谁。Because 引出的不是解释，而是他自己给的假设：一个 maybe 接另一个 maybe，句子自己把假设越推越远。落在 resurrection 与 return 上的 involuntary、unnatural 两个词，是他给这件事定的性——不是我要的，也不该发生。stripped back 把记忆写成被一层层剥掉的东西。
- 读者视角提示：这一段一个字也没提是谁把他弄回来的；他在给自己死后的空白找说法。他赌的是「有，只是记不得」，不是「什么都没有」。
- **原文**：原文 L174-L174
- **结论**：引语 3 句 46 词（原文 L174）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（31 词 3 句）：The command rolled over Eli, and his hand fell back to his side. The tension left his limbs, and for a terrible instant, so did the desire. His mind went blank.
- 中文理解：那道命令从他身上碾过去，他的手落回身侧。绷着的力气从四肢退掉，而就在那可怕的一瞬，连想反抗的念头也退了。他脑子里一片空白。
- 关键词：command rolled over · mind went blank
- 为什么这样写：句子按「命令—身体—欲望—意识」四层往下压。rolled over 是命令的动作，hand fell back 是身体让开，so did the desire 把退掉的东西从力气换成念头，最后 His mind went blank 落到什么都不剩。for a terrible instant 只给一瞬，说明退掉的不止是力气，还有他那一部分自己。
- 读者视角提示：这一句里没有挣扎的过程，只有三样结果：落回身侧的手、退掉的念头、一片空白。读者得自己去量那一下有多长。
- **原文**：原文 L255-L255
- **结论**：引语 3 句 31 词（原文 L255）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符

### 原句 6
- **md**：引语（18 词 1 句）：“I’ve buried dozens of EOs, Dr. Gray,” he said, “And I will find a way to bury you.”
- 中文理解：「我埋过几十个 EO，格雷医生，」他说，「我会找到办法把你也埋了。」
- 关键词：buried dozens of EOs · bury you
- 为什么这样写：他先用复数把旧账一次结清——dozens 是几十个，不是几个；埋 EO 这件事对他来说是做过很多遍的活。后半句换成将来式，find a way 把「做不到」留成技术问题：现在做不到，不等于永远做不到。话是冲着「Dr. Gray」这个称呼说的，敬称挂在句尾，像一张收据。
- 读者视角提示：这是他在本章里唯一一次亮出过去的数目。读者由此知道他不是第一次处理 EO，而是做过很多次；而对方让他害怕的原因也在这里——他要对付的不是一个 EO。
- **原文**：原文 L264-L264
- **结论**：引语 1 句 18 词（原文 L264）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L68）
- **档**：相符

### 原句 7
- **md**：引语（37 词 2 句）：A second wave of pain. He hissed as something sharp tore through his skin, fresh blood welling from his knuckles as tiny shards of broken bone pushed up like jagged teeth, and fell, ringing, to the floor.
- 中文理解：第二波疼来了。有什么尖的东西撕开他的皮，血从指节处涌出，细小的碎骨像参差的牙一样顶上来，然后叮当落地。
- 关键词：second wave of pain · jagged teeth
- 为什么这样写：这一块几乎全靠触觉和声音推进：hissed、tore through、welling、pushed up、fell, ringing。疼被写成「第二波」，说明前面已经疼过一轮，这一轮是新的、也是他没料到的。碎骨用 like jagged teeth 来比——牙本该长在嘴里，现在从他指节上顶出来。ringing 一个词把画面接到听觉，读者能听见碎片落地。
- 读者视角提示：这一块只写疼与碎骨，没写他因此想到什么、也没写他接下来做什么。句子停在碎片落地的那一声上。
- **原文**：原文 L300-L300
- **结论**：引语 2 句 37 词（原文 L300）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L78）
- **档**：相符
