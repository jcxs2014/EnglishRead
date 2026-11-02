# 3-diff.md · 《Victorious》第 69 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch69_chapter_xviii.txt`
- 受审 md：`ch69 malcolm hides mitch from gray.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（saw the captured human Mitchell Turner regaining consciousne）
- **原文**：原文 L25：Long enough to see the captured human, Mitchell Turner, regaining consciousness.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L25：原文 L25 的事实「saw the captured human Mitchell Turner regaini」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（held the deleted frames in his mind and saw two words flash ）
- **原文**：原文 L103：Malcolm held the deleted frames in his mind, Mitchell Turner twisting against the restraints, and two words flashed across the inside of his eyes.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L103：原文 L103 是外观/随身物品描写（held the deleted frames in his mind …），无情节转折；判提示不修
- **档**：提示

### L3 · R1 事实未进 md（were, in Malcolm’s view, little more than wind-up toys runni）
- **原文**：原文 L64：Not the EON agents, or the past director, little more than wind-up toys running on old memory. Not the doctor standing just behind his chair, watching the other screens.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L64：原文 L64 是一处静态状态描写（were, in Malcolm’s view, little more…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 3（阻断 0 / 提示 3） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（42 词 2 句）：IN the control room, the EO who used to be Malcolm Olipett stopped what he was doing. Not for long—less than 0.3 seconds, a nearly imperceptible delay for human senses—but long enough for him to notice the movement on the eleventh screen.
- 中文理解：控制室里，那个曾经是马尔科姆·奥利佩特的 EO 停下了手上的事。停得不久——不到 0.3 秒，对人类感官来说几乎察觉不到——但足够让他注意到第十一块屏上的动静。
- 关键词：the control room · the eleventh screen
- 为什么这样写：第一句把身份摊开：现在的他是 EO，名字挂在「曾经是」后面。第二句立刻把时间收窄，先给「不到 0.3 秒」，再补一句「对人几乎察觉不到」，把这个延迟压到感官之下，接着用 but 把它抬起来——足够看见第十一块屏。全段没写他停的是什么活，只写他停了，以及停下之后看见了什么。
- 读者视角提示：读者先拿到一个「曾经是马尔科姆·奥利佩特」的人，然后才被带进那 0.3 秒。屏有十一块，动的是第十一块。
- **原文**：原文 L19-L22
- **结论**：引语 2 句 42 词（原文 L19）：中文理解逐句对得上，主语=马尔科姆、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（54 词 2 句）：Long enough to divert exactly 5 percent of his attention to the question of what to do next. (The remaining 95 was still devoted to maintaining protocols both inside the base and in the field.) That 5 percent might not seem like much, to an ordinary mind, but to Malcolm it was statistically significant.
- 中文理解：也足够让他正好分出 5% 的注意力，去想下一步该怎么办。（剩下的 95% 仍在维持基地内部与现场的协议。）这 5% 在常人看来也许不算什么，对马尔科姆却是统计上显著的。
- 关键词：exactly 5 percent · statistically significant
- 为什么这样写：数字先给整数：5 与 95，一小一大。中间用括号补一句剩下的去向，一次分神因此写成一次精确的重新分配。第三句把同一件事从「常人」换到「马尔科姆」身上看，落点是一个统计学词——显著——把这 5% 抬成一件值得动手的事。整段的量都在他那一侧算。
- 读者视角提示：读者跟着他去算这 5%。括号里的 95% 提醒读者，他的大部分算力还压在协议上，能动用的只有一小块。
- **原文**：原文 L28-L31
- **结论**：引语 2 句 54 词（原文 L28）：中文理解逐句对得上，主语=马尔科姆、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（35 词 3 句）：Malcolm could not directly disobey these orders. But language made room for something code did not: interpretation. He could not help Mitch extricate himself, just as he could not let him break into EON’s mainframe.
- 中文理解：马尔科姆不能直接违抗这些命令。但语言留出了代码没有的余地：解释。他不能帮米奇脱身，同样也不能让他闯进 EON 的主机。
- 关键词：language made room · directly disobey
- 为什么这样写：三句都沿同一条线走：先说不能做的——违抗；再用 But 把「不能」挪到另一层，语言与代码的对举最后落在一个名词上，解释；第三句又把不能做的说细，帮米奇脱身不行，让他进主机也不行。两次「不能」之间夹着那句余地，位置本身就是这段话的分量所在。
- 读者视角提示：读者拿到的是他能做什么与不能做什么，两边的界线都画死了，中间只剩一条：解释。这条缝有多宽，要看他下一段怎么用它。
- **原文**：原文 L43-L49
- **结论**：引语 3 句 35 词（原文 L43）：中文理解逐句对得上，主语=米奇、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（39 词 1 句）：Which was why he now deployed a quick sequence of code to loop the footage from that van’s holding tank, starting three full seconds before Mitch began to stir, and therefore absolving himself of witnessing anything that merited engagement.
- 中文理解：所以他现在敲了一小段代码，把那辆运输车后厢的录像做成循环，起点在米奇开始动之前整整三秒，这样一来他就不算目睹了任何需要处置的事。
- 关键词：loop the footage · three full seconds
- 为什么这样写：这一句把前面那句「余地」落成了动作。顺序排得清楚：敲代码、循环、把起点放在米奇开始动之前整整三秒，最后给结论——这样一来他就不算目击。三秒这个数不是随手挑的，它必须早于那个动作，循环才成立。
- 读者视角提示：读者看见的是一次技术性的挪位：录像被接回三秒之前，他把自己从目击者的位置上摘出来。三秒够不够用，读者可以自己算。
- **原文**：原文 L58-L58
- **结论**：引语 1 句 39 词（原文 L58）：中文理解逐句对得上，主语=米奇、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（50 词 1 句）：Instead of resisting—which had a 0.01 percent chance of netting a positive result—Malcolm had redirected his efforts, partitioning a small corner of his mind, shielding a negligible amount of processing power from the doctor’s influence (of course, what qualified for Malcolm as negligible amounted to most people’s total processing power).
- 中文理解：他没有抵抗——抵抗只有 0.01% 的几率换来正面的结果——而是把力气改了方向：在脑子里隔出一个小角落，把一小份算力挡在医生的影响之外（当然，对马尔科姆算得上「可以忽略」的，是大多数人全部的处理能力）。
- 关键词：0.01 percent chance · redirected his efforts
- 为什么这样写：句子用一个 Instead of 开头，先把抵抗这条路摆出来，再给它的赔率：0.01%。破折号里那句是算账，不是表态。后半句是一次具体的分配：隔出小角落、挡出一小份算力，两个动作都带量词。括号最后又把这「可以忽略」翻了一次——他觉得可以忽略的，是别人全部的处理能力。
- 读者视角提示：读者先看见抵抗的赔率被算到 0.01%，再看见他把力气换了个方向。括号把两个尺度并排放着：他说可以忽略的，是大多数人全部的处理能力。
- **原文**：原文 L76-L76
- **结论**：引语 1 句 50 词（原文 L76）：中文理解逐句对得上，主语=马尔科姆、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符

### 原句 6
- **md**：引语（44 词 3 句）：Mitch was smart, and he was human. Usually, that clause would have started with a but, not an and, but in this one scenario, the and was everything. If Mitch had been an EO, Malcolm wasn’t sure he’d be able to circumnavigate his directives.
- 中文理解：米奇聪明，而且是人。通常这个说法该用「但」开头，不是「而且」，可在这一个情形里，「而且」就是全部。如果米奇是 EO，马尔科姆不确定自己还能不能绕开那些指令。
- 关键词：smart · the and was everything
- 为什么这样写：这一段先把两个条件并起来：聪明，是人。第二句回头去挑连词，说通常这里该是 but，这次是 and，然后给结论——这个 and 就是全部。第三句把原因摊开：如果米奇是 EO，那些指令就绕不开。全段的重心不在「聪明」上，在那个「而且」立不立得住。
- 读者视角提示：读者被提醒去注意一个连词。这一段把「聪明」放在了前面，把分量压在「人」上：如果米奇是 EO，那些指令就绕不开——「而且」能不能立住，决定后面的事做不做得下去。
- **原文**：原文 L88-L88
- **结论**：引语 3 句 44 词（原文 L88）：中文理解逐句对得上，主语=米奇、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L68）
- **档**：相符
