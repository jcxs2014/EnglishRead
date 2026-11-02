# 3-diff.md · 《Victorious》第 45 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch45_chapter_xv.txt`
- 受审 md：`ch45 gabriel walks his morning rounds.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（在 Gabriel 查房时记下笔记，把他的想法抄下来以备后用）
- **原文**：原文 L78：As he did his morning rounds, she took notes, transcribing his thoughts for later reference.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L78：原文 L78 的事实「在 Gabriel 查房时记下笔记，把他的想法抄下来以备后用」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（命令 Helena 派最近的特遣员去调查三名新候选人的所在位置）
- **原文**：原文 L171：“Helena,” instructed Gabriel, “please dispatch the closest agents to investigate.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L171：原文 L171 的事实「命令 Helena 派最近的特遣员去调查三名新候选人的所在位置」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 2（阻断 0 / 提示 2） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（56 词 2 句）：He still rose before six to run three miles, still took a cold five-minute shower, still drank an espresso in silence on the porch. For that brief stretch, between the first alarm and the last sip of coffee, he could pretend—if he wanted to—that Iris was in the bedroom, humming to herself as she got dressed.
- 中文理解：他照旧六点前起床，跑三英里、冲五分钟冷水澡、在门廊上一言不发喝完一杯浓缩咖啡；从闹钟响到咖啡喝尽这段空隙里，他只要愿意，就能当艾瑞斯还在卧室里哼着歌穿衣服。
- 关键词：rose before six · cold five-minute shower
- 为什么这样写：三个 "still" 连着压在同一句里，把作息写成一套不肯改的规程，读起来像清单而不是抒情。后半句用 "could pretend—if he wanted to" 把这点自由交回他自己手上，假装因此是他主动选的，不是失控；时间窗由闹钟与最后一口咖啡夹出来，短得刚好装下一场想象。
- 读者视角提示：注意这段里没有别人出场，艾瑞斯的哼歌与穿衣都发生在他的假想里。"still" 把这几行钉在习惯上——写的是每天的早晨，不是某一个例外。
- **原文**：原文 L27-L27
- **结论**：引语 2 句 56 词（原文 L27）：中文理解逐句对得上，主语=艾瑞斯、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（46 词 3 句）：It was fascinating, the minute differences, between an ordinary convert and an EO, even one so firmly under his control. The animation in his face, the agency with which he moved and spoke, his personality intact. Ironic, that in Gabriel’s hands, only the EOs remained human.
- 中文理解：普通皈依者与 EO 之间那些细微差别让他着迷，哪怕这个 EO 已经牢牢在他控制之下；那人脸上还有神情，走动与说话还有自己的主张，个性也完好。他觉得讽刺的是，经他的手之后，只剩 EO 还算得上人。
- 关键词：the minute differences · remained human
- 为什么这样写：落点在最后一句。前面用 "animation"、"agency"、"personality" 三个词把「像人」拆成看得见的三处，中间两句短到几乎只是列举；最后一个词 "Ironic" 一转折，把他自己也写进这个判断里——他是下手的人，也是说出这句话的人。
- 读者视角提示："even one so firmly under his control" 这半句先把控制摆出来，最后那句讽刺才有对照物。读的时候不妨把「皈依者」与「EO」两个词的位置对调想一想，句子的意思会不会反过来。
- **原文**：原文 L90-L90
- **结论**：引语 3 句 46 词（原文 L90）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（38 词 2 句）：Take Dominic, who, despite the fact he’d been resurrected months ago, had shown no signs of waking up. Some delay was normal—the longer they were dead, the longer it often took for them to wake—but this was different.
- 中文理解：多米尼克复活已经几个月，却一直没有醒来的迹象；醒来有延迟本来算正常，死得越久往往醒得越慢，但这一例不属于那种正常。
- 关键词：no signs · this was different
- 为什么这样写：先给一条能被接受的规律，再用 "but this was different" 把它掐断。句子因此不是病情报告，而是让他自己把这一例从规律里挑出来；挑出来之后他也不解释，下一段才补上烟影与穿过去的手。
- 读者视角提示：这一段只写「没醒」和「不一样」，多米尼克此刻的样子要等下一段。两段之间隔着一次判断：先说不一样，再写不一样在哪儿。
- **原文**：原文 L120-L120
- **结论**：引语 2 句 38 词（原文 L120）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 4
- **md**：引语（65 词 3 句）：The bald man sat before the wall of screens, his hands resting on bare circuitry, his eyes unblinking behind his glasses as his mind spread through the mainframe. Part of his mind trawled the internet for signs of potential EOs, cross-referencing and compiling a target list, while simultaneously scrubbing any public mention. The other half secured EON itself, both its physical and its digital security.
- 中文理解：光头男人坐在整面屏幕墙前，双手按在裸露的电路上，眼镜后面的眼睛不眨，心思顺着主机铺开去；一半心思在网上翻找可能是 EO 的人，交叉比对、编出一份名单，同时把任何公开提及抹掉；另一半守着 EON 的实体与数字安全。
- 关键词：wall of screens · his mind spread
- 为什么这样写：这一段把一个人的工作拆成两半同时进行——一半找人，一半抹去痕迹、守住大门。"trawled" 是拖网，"scrubbing" 是擦洗，两个动作都落在看不见的地方；身体却几乎不动，只有手按在电路上。写「效率」不用形容词，用两件事并行。
- 读者视角提示：注意 "Part of his mind" 这个说法，它把这个人剩下的部分留在别处；下面一段才交代他拔不掉线、也离不开系统，读的时候把两段接起来。
- **原文**：原文 L141-L141
- **结论**：引语 3 句 65 词（原文 L141）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=网，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L52）
- **档**：相符

### 原句 5
- **md**：引语（58 词 1 句）：Gabriel laid his palm against the scanner, and the doors unsealed, letting him pass into the corridor that ran around what used to be the cell, and was now a simple, well-appointed room, a suite in fact, complete with a shower, a toilet, partitioned for privacy, the walls painted a docile shade of green, just like his office.
- 中文理解：他把手掌按上扫描器，门解封，他走进一条绕着旧牢房修的走廊；旧牢房如今是一间陈设齐整的房间，实际上算个套间，带淋浴、带马桶、做了隔断，墙刷成一种温顺的绿色，和他办公室用的一样。
- 关键词：against the scanner · docile shade
- 为什么这样写：一句里塞进很长一串附加成分，从门、走廊、旧牢房一路铺到淋浴、马桶、隔断和墙色，句子跟着走廊一起绕。被关的人还没露面，关他的地方先被写得像客房；最后落在 "just like his office"，把这间屋子和医生自己的空间并到一起。
- 读者视角提示：可以把 "what used to be the cell" 当成整句的支点——后面的 "a suite in fact" 是对它的改写，两种说法指的是同一间屋子；反差就在这两个说法之间。
- **原文**：原文 L240-L240
- **结论**：引语 1 句 58 词（原文 L240）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L62）
- **档**：相符
