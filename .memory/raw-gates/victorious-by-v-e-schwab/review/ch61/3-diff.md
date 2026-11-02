# 3-diff.md · 《Victorious》第 61 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch61_chapter_x.txt`
- 受审 md：`ch61 both of them alive.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（proposed that the team split up in case the drone sighting w）
- **原文**：原文 L48：“We should split up,” he said, “in case that isn’t right.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L48：原文 L48 的事实「proposed that the team split up in case the dr」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（laughed and headed toward the nearest van instead of splitti）
- **原文**：原文 L51：But Noah only laughed and headed toward the nearest van.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L51：原文 L51 的事实「laughed and headed toward the nearest van inst」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（explained the appearance of Sydney's sister to Noah and to G）
- **原文**：原文 L54：While they drove, Eli explained the appearance of Sydney’s sister to Noah and Gabriel, who he knew was listening.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L54：原文 L54 的事实「explained the appearance of Sydney's sister to」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（there were no towns within a ten-mile radius）
- **原文**：原文 L21：The five remaining agents circled, waiting for instructions. The motel was in the middle of nowhere. There were no towns in a ten-mile radius. The only structures were a couple farms, an abandoned theme park, and a shuttered mall.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L21：原文 L21 的事实「there were no towns within a ten-mile radius」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 4（阻断 0 / 提示 4） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（35 词 4 句）：And yet, Serena Clarke had somehow come back stronger. She wasn’t just commanding minds. She was controlling every sense, creating a kind of altered reality. Which was dangerous enough, but her reach was greater, too.
- 中文理解：可塞雷娜·克拉克回来之后，不知怎么反而更强了。她不只是摆布人的念头，她控制的是每一种感官，造出的是一层被改过的现实。这已经够危险，可她够得着的范围还更大。
- 关键词：come back stronger · altered reality
- 为什么这样写：四个句子只朝一个方向加码，没有一句往回退。第二句先把原先那件事降格——"wasn't just"，第三句换成更大的范围，第四句把结果命名成"a kind of altered reality"。命名之后本该收住，句子却用"Which was dangerous enough, but"把这个判断也推开，接上"reach"；危险已经被承认过一次，还要再加一层。
- 读者视角提示：读完这一段，读者才看清屋顶上那些人的遭遇不只是有人在摆布念头，而是一层现实被换掉了。最后半句把问题从"她能做什么"改成"她够得着多远"，而这个问题下面马上要用三处对照来回答。
- **原文**：原文 L30-L30
- **结论**：引语 4 句 35 词（原文 L30）：中文理解逐句对得上，主语=塞雷娜、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（40 词 4 句）：But on the roof, she hadn’t spoken. And yet, she’d not only influenced the agents there. Eli had been impacted on the floor below. Meanwhile, Noah was on the other side of the motel, securing Mitchell Turner, and felt nothing.
- 中文理解：可屋顶上她并没有开口。然而她影响的不只是屋顶上那几个探员：楼下那一层的伊莱也中了招。同一时间，诺亚在旅馆另一侧看着米奇·特纳，什么都没感觉到。
- 关键词：on the floor below · felt nothing
- 为什么这样写：这一段在做排除法。第一句掐掉最省事的解释（她没开口），第二句把范围往外推一层（不止屋顶），第三句再推一层（楼下也中），第四句给出反例（另一侧毫无反应）。前三句一路往外扩，最后一句忽然停住：三处三种反应，界线就摆在这三种反应之间。
- 读者视角提示：读者跟着伊莱数人头，屋顶中、楼下中、另一侧不中。三个点落在纸上，这条界线读者会自己去补。
- **原文**：原文 L33-L33
- **结论**：引语 4 句 40 词（原文 L33）：中文理解逐句对得上，主语=米奇、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（30 词 4 句）：He didn’t know exactly what had happened on the stairs, but it was overpowering. He’d been convinced he was somewhere else, somewhen else. He hadn’t been hallucinating. He’d been dreaming.
- 中文理解：楼梯上究竟出了什么事，他说不准，只知道那股力量压得人没有还手之力。他当时确信自己在别的地方、别的时刻。那不是幻觉——他是在做梦。
- 关键词：on the stairs · been dreaming
- 为什么这样写：两个否定句在这里是划界用的。"didn't know"先把解释撤掉，"hadn't been hallucinating"再把最容易被拿来顶替的那个词也撤掉，最后才给出他要的那个词——dreaming。前面三句都短，末句只有三个词，落在一个句号上，把一件失控的事说成一件他当时毫无察觉的事。
- 读者视角提示："somewhen else"在英语里不是常用词，读者和伊莱一起被放在一个说不清时间的坐标上。做梦的人不知道自己正在睡，这一句把他当时的状态说成睡着的状态，而不是看错。
- **原文**：原文 L63-L63
- **结论**：引语 4 句 30 词（原文 L63）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（34 词 2 句）：“She overrode you,” snapped Eli. “Do you get that, Gabriel? She got inside your agents’ heads, even though you were already in there, and if that’s not enough reason to shoot on sight, I—”
- 中文理解："她把你压过去了，"伊莱呛了一句。"你听明白了吗，加百列？她钻进了你那些探员的脑子里——而你本来就已经在里面了。要是这还不算当场开枪的理由，我——"
- 关键词：She overrode you · shoot on sight
- 为什么这样写：这是全章唯一一次有人打断上级。三句话一句比一句近：先下结论（她压过你），再逼对方确认（你听明白了吗），第三句把两件事并在一起——她进去，而你早就在里面。末尾那个破折号让话被截断，句子没有说完，谁在说话、谁能说完，落在标点上。
- 读者视角提示：读者听到的是一个人在替自己的判断争最后一寸。破折号后面的话被截掉了，接下来的是一句命令，不是回答。
- **原文**：原文 L72-L72
- **结论**：引语 2 句 34 词（原文 L72）：中文理解逐句对得上，主语=伊莱、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（47 词 5 句）：“If that happens, I will instruct you. Until then, your orders are to capture both Sydney and Serena Clarke. Alive.” The static went flat again in Eli’s ear, the auditory equivalent of a phone call going dead. Arrogance, he thought. The same arrogance he’d seen in Victor.
- 中文理解："真到那一步，我会另行指示你们。在那之前，你们的任务是把西德妮和塞雷娜·克拉克两个都抓回来，活的。"耳机里的静电又平了下去，像一通电话被挂断。傲慢，他想。跟他在维克多身上见过的同一种傲慢。
- 关键词：capture both · phone call going dead
- 为什么这样写：回答被推到将来（"If that happens, I will instruct you"），命令却被钉在现在（"Until then, your orders are"）——回答在将来，命令落在现在，两句之间隔着一个时间差。后面那个比喻把断线写成电话挂断，声音一停，一个名词单独起句："Arrogance"。最后一句把这个人并到维克多身上，两个人共用同一个名词，不共用别的东西。
- 读者视角提示：维克多这个名字在这里从伊莱心里冒出来，落在一个贬义词后面，读者看得出这不是夸奖。命令是活的、两个、一起；而读者在伊莱耳朵里听到的最后一样东西，是一通挂断的电话。
- **原文**：原文 L84-L84
- **结论**：引语 5 句 47 词（原文 L84）：中文理解逐句对得上，主语=维克多、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符
