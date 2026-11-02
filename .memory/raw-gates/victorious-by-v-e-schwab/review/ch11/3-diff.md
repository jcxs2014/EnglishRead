# 3-diff.md · 《Victorious》第 11 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch11_chapter_x.txt`
- 受审 md：`ch11 the doctor brings them back.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（wheeled Gabriel down the hall to the morgue after the elevat）
- **原文**：原文 L166：The doors chimed open, and Walsh wheeled him down the hall.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L166：原文 L166 的事实「wheeled Gabriel down the hall to the morgue af」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（is one of Gabriel's old colleagues, an internist who is trea）
- **原文**：原文 L48：Gabriel dragged his gaze to the right and was confronted by one of his old colleagues, Walsh. An internist, known for his booming laugh and easy bedside manner. Gabriel had never cared for either.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L48：原文 L48 是一处静态状态描写（is one of Gabriel's old colleagues, …），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（is Ian's father, and lifted Ian from the table after bringin）
- **原文**：原文 L340：He lifted Ian from the table, wrapped in nothing but the white sheet, and set him, barefoot, on the tile floor before remembering Walsh. Ian had always been afraid of blood. He’d burst into tears at the sight of a cut finger or scraped knee. But now, he didn’t even seem to notice the wide red pool s
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L340：原文 L340 是一处静态状态描写（is Ian's father, and lifted Ian from…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 3（阻断 0 / 提示 3） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（45 词 2 句）：“Intubation,” explained Walsh. “You’ve been in a medicated coma for the last”—he checked his watch, as if it held the answers, and not the file in his hand—“nineteen days.” He lifted the glasses from the bedside table and handed them back. “How are you feeling?”
- 中文理解：沃尔什先给了一个术语——插管，然后说他在药物昏迷里躺了十九天；说这话时低头看了一眼手表，好像答案在表盘上、而不在手里那份病历里。末了他把床头的眼镜递回来，问一句感觉怎么样。
- 关键词：medicated coma · nineteen days
- 为什么这样写：数字被压在破折号之后，读者得先听完一个医学程序，才等到那个时长。看表这个动作把十九天从病情换算成一段被人计过数的日子；而「感觉怎么样」这种日常问候紧跟着十九天，轻重完全不成比例。作者不形容他有多震惊，只让这句轻飘飘的问候挂在数字后面。
- 读者视角提示：先把十九天记住。一个人昏迷十九天，意味着这中间所有该由他到场的事他都缺席了；后来他非要从床上起来，力气就从这个数里来。
- **原文**：原文 L54-L54
- **结论**：引语 2 句 45 词（原文 L54）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（54 词 2 句）：“According to the medics, that steel bar kept you from being crushed beneath the wall, but you lost an awful lot of blood. By the time they cut you free, you didn’t have a pulse. No telling exactly how long your brain went without oxygen, but a good old-fashioned defib and two transfusions later…”
- 中文理解：按医护的说法，那根钢条保住了他，没让他被压在墙底下；但他失血太多，他们把他挖出来的时候已经没有脉搏，也说不准大脑缺氧多久——「一阵老式的除颤、加上两次输血之后……」
- 关键词：defib and two transfusions · steel bar
- 为什么这样写：沃尔什这段话把加百列的身体账目一次报清：钢条挡了挤压（没有塌方的直写），失血过量（后来复活时才需要处理），挖出来时没有脉搏（所以才用得上除颤）。三项全用间接说法——「according to the medics」「you didn’t have a pulse」「no telling exactly how long」——把结论推给专业判断，像一份转述的诊断书。末尾那个悬着的省略号停在「之后」，把结果交给加百列自己——他已经知道了。
- 读者视角提示：读者此时还不知道他后来能复活活人，所以这句除颤加两次输血只是「他差一点点就死了」的医学背景。等他在地下室把妻子拉回来，同一段身体的严重程度才被重新解释成别的东西。
- **原文**：原文 L60-L60
- **结论**：引语 2 句 54 词（原文 L60）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（44 词 3 句）：He knew, and so he braced for the force of the cataclysmic news to hit, unsure which would overwhelm him first. He waited for the sickening lurch of his world crashing down a second time. He waited, but the world did not even tremble.
- 中文理解：他清楚悲恸会以哪些方式到来，所以提前绷紧了身体，等着那条灾难性的消息砸下来，还猜不准先压垮他的是消息本身，还是世界第二次塌陷的那种失重。他等着，可世界连抖都没有抖一下。
- 关键词：cataclysmic news · did not even tremble
- 为什么这样写：三个句子由同一个动作串着——brace、wait、wait。前两处后面跟着越来越具体的灾难：力道、失重的猛晃、世界第二次塌陷；第三处只剩一个否定。期待铺得越高，落空就越安静，最该爆发的段落被写成了静止。这一章的麻木正是从这里开始计时的。
- 读者视角提示：注意 a second time。世界已经塌过一次，这次连塌都省了——他等的其实是自己该有的反应，而那个反应没有来。
- **原文**：原文 L75-L75
- **结论**：引语 3 句 44 词（原文 L75）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（48 词 2 句）：He felt her lungs expand, slow and smooth, like a body on the edge of sleep. Gabriel pulled back and saw the color creeping back into her skin, the postmortem incisions erased, along with the cut on her cheek, the shadows where blood had pooled beneath her skin.
- 中文理解：他的手还贴在她脸上时，她的肺慢慢鼓起来，平顺得像一个刚要睡着的人。他退开，看见血色一点点回到她皮肤里，尸检的切口不见了，脸颊上那道小伤口也不见了，皮下沉着的淤血影子一并退掉。
- 关键词：lungs expand · incisions erased
- 为什么这样写：复活没有一道光，只有一连串被撤回的细节，顺序从里到外：肺、颜色、切口、小伤口、淤血。这几样凑成的正是死亡的一整套凭据——尸检切口、脸上那道口子、皮下沉住的淤血，现在被逐项划掉。slow and smooth 是全章少见的、不带痛的形容；机制一个字不解释，让证据自己消失。
- 读者视角提示：这一段里没有「奇迹」，也没有「能力」这类词。他还在看，还没开始想自己做了什么——理解要晚一步才到。
- **原文**：原文 L238-L238
- **结论**：引语 2 句 48 词（原文 L238）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（67 词 3 句）：Gabriel moved—injuries forgotten, or at least, suppressed by the hierarchy of need. He swept a scalpel from a nearby tray, reaching the call button just before Walsh. His body had come free of his mind, and he watched, as if outside himself, as one hand caught the doctor’s shoulder, spinning him round, and the other drew the blade in a quick, clean slice across the man’s throat.
- 中文理解：他动了，伤被忘掉，或者说是被「需要的轻重缓急」压了下去；他从旁边的托盘上抄起一把手术刀，比沃尔什早一步赶到呼叫按钮前。身体像从意识里脱了钩，他站在自己之外看着：一只手扣住医生的肩，把他转过来，另一只手飞快、干净地横过他的喉咙。
- 关键词：hierarchy of need · call button
- 为什么这样写：暴力被写成一次旁观。主语始终是他，可动作一到要紧处就换成了 one hand 与 the other，他自己的意识退到「看」的位置。quick, clean 是外科医生的用词，不是凶手的——他用的还是同一双手、同一套训练。hierarchy of need 是本章的一句暗语：需要排好了队，杀人也占到一个位置。
- 读者视角提示：他先赶到的是呼叫按钮，不是门。他拦住的是「求救」这个动作；从这一下起，这间屋子对外的通道就归他管了。
- **原文**：原文 L280-L280
- **结论**：引语 3 句 67 词（原文 L280）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手术刀，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符

### 原句 6
- **md**：引语（41 词 3 句）：He closed them and imagined reaching out for Ian. Catching his son’s fingers as he couldn’t on the stairs, pulling him forward, and there it was again, that cresting feeling, the swell he’d taken for grief. But this time, he understood.
- 中文理解：他闭上眼，想象自己伸手去够伊恩——像在楼梯上没能抓住那样，这一回抓住儿子的手指，把他往前拉。那股涌上来的感觉又出现了，就是他先前当成悲恸的那一阵涨潮。可这一次，他明白了。
- 关键词：reaching out · cresting feeling
- 为什么这样写：能力的开关被交给一个想象中的动作：不是咒语，是「抓住手指」。as he couldn’t on the stairs 是他第一次回头看那场事故——他一直没抓住他们，于是先在想象里补上这一把。the swell he’d taken for grief 把前面的误读翻了过来：那阵把他压得弯下腰的东西，原来不是悲伤。最后几个词 he understood 既是句号，也是转向。
- 读者视角提示：往后读时留意「抓」这个动作。他失手过一次，此后每一次伸手都带着把它补回来的意思——这也是他越来越不问对方愿不愿意的原因。
- **原文**：原文 L313-L313
- **结论**：引语 3 句 41 词（原文 L313）：中文理解逐句对得上，主语=伊恩、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L68）
- **档**：相符

### 原句 7
- **md**：引语（60 词 3 句）：Iris used to cock a brow if he ever asked her to do something without a please and thank you on the end, but now, she obeyed. A quiet dread crept over Gabriel, and his mind began to tick through a litany of diagnoses—from shock to cognitive impairment—before he pushed the thought away. There would be time for questions later.
- 中文理解：从前他支使她做事、句尾不带「请」和「谢谢」，艾瑞斯会挑起一边眉毛；现在她照做了。一阵安静的恐惧爬上来，他的脑子开始一条条过诊断，从休克到认知损伤，然后把这个念头推开了。末尾他自己给自己留了一句：问题以后再问。
- 关键词：cock a brow · she obeyed
- 为什么这样写：判断「不对」的证据不是她做了什么，而是她没做什么——没有挑眉。used to… but now 一组对照就把人换掉了。接着他立刻启动医生的那套程序，把恐惧翻译成一张清单；结尾 before he pushed the thought away 才是要害：他不是没看出来，是看出来了、然后决定不看，再补一句以后再问。
- 读者视角提示：把「挑眉」记牢。整章他都在用「她只是休克」说服自己，而读者手上已经有了对照：会挑眉的艾瑞斯和照做的艾瑞斯，不是同一个人。
- **原文**：原文 L358-L358
- **结论**：引语 3 句 60 词（原文 L358）：中文理解逐句对得上，主语=艾瑞斯、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L78）
- **档**：相符

### 原句 8
- **md**：引语（42 词 2 句）：“We need to go,” said Gabriel, holding out his hands for his wife, his son. They came to him, of course, their fingers sliding through his, Iris’s soft, smooth palm, and Ian’s small fist, and in the moment, that was what mattered.
- 中文理解：「我们得走了，」他说，向妻子和儿子伸出手。他们当然过来了，手指滑进他手里——艾瑞斯柔软平滑的掌心，伊恩的小拳头。那一刻，要紧的就是这个。
- 关键词：fingers sliding through · what mattered
- 为什么这样写：of course 是这一段全部的重量。他们过来，不是因为想过来，是因为被叫；「当然」两个字把顺从写成了理所当然，而理所当然才是最冷的地方。他一样一样数着手里的触感，把「活着」缩小成可以摸到的东西，再用 that was what mattered 把其余的问题关在门外。
- 读者视角提示：读这一句要听 of course 的语气——它不像重逢，像点卯。他握住的既是妻子和儿子的手，也是「他们归他」这件事；收得越整齐，越不像团圆。
- **原文**：原文 L427-L427
- **结论**：引语 2 句 42 词（原文 L427）：中文理解逐句对得上，主语=艾瑞斯、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L88）
- **档**：相符
