# 3-diff.md · 《Victorious》第 50 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch50_chapter_v.txt`
- 受审 md：`ch50 ashes to ashes.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（said EOs are a puzzle he is determined to solve, and that he）
- **原文**：原文 L54：“EOs are a puzzle,” he said, “One I’m determined to solve. To do that, I need as many pieces as possible. To understand the big picture. And you, Eli, are a very important piece.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L54：原文 L54 的事实「said EOs are a puzzle he is determined to solv」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（resolved to put Gabriel in the ground after watching Xavi de）
- **原文**：原文 L205：And Eli would put him in the ground.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L205：原文 L205 的事实「resolved to put Gabriel in the ground after wa」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（is bound to Gabriel by an invisible cord and fights to push ）
- **原文**：原文 L69：The cord drew taut as he fought to push Gabriel back. A waste of energy. For both of them.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L69：原文 L69 是一处静态状态描写（is bound to Gabriel by an invisible …），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 3（阻断 0 / 提示 3） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（36 词 2 句）：Eli did as he was told, and only that, all the while clearly searching for any loophole, any opportunity he might exploit. Like a child, looking for ways to disobey a parent without breaking their rules.
- 中文理解：伊莱照吩咐做，也只做吩咐过的那些，与此同时明明白白地在找缝子——任何可以钻的漏洞、任何可以借的机会，他都在找。像一个小孩，想法子在不动规矩的前提下不听话。
- 关键词：any loophole · Like a child
- 为什么这样写：先把「听话」写满，再把「找缝」并排放进同一个分句：did as he was told, and only that 后面紧跟 all the while clearly searching，两件事是同时发生的。第二句换成小孩的比喻，把越狱式的念头落回家里那点小动作——不破规矩，只绕规矩。反抗在这里不靠动作，靠搜索。
- 读者视角提示：这一块只写他怎么找，没写他找到了什么。any 连着出现两次，读者的视线也跟着把每条缝走一遍。
- **原文**：原文 L30-L30
- **结论**：引语 2 句 36 词（原文 L30）：中文理解逐句对得上，主语=伊莱、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（51 词 3 句）：He’d read Eli’s files—every single one of them—and so he knew not only the extent of his abilities, but also his belief. Not in God—his faith there seemed to waver—but in his purpose. It made Eli an asset, not only to his current research, but to the future of his program.
- 中文理解：伊莱的档案他全读过，一份没漏，所以他手上的不只是这个人能力有多大，还有他信什么。信的不是上帝——那一处似乎摇摆——而是他自己的使命。这让伊莱成了一件资产：对眼下的研究有用，对这项计划的将来也有用。
- 关键词：read Eli’s files · an asset
- 为什么这样写：档案在前，结论在后。破折号里塞一句 every single one of them，先把读了多少摆出来，再说知道了什么。中间连用两组 not…but，把「信什么」一层层钉住：不信上帝，信使命。末句换成算账的词——asset、research、program——人被归进了资产那一栏。
- 读者视角提示：这一块只有他和那些档案，没有伊莱的反应。读到这里，被读完的那个人还不知情。
- **原文**：原文 L81-L81
- **结论**：引语 3 句 51 词（原文 L81）：中文理解逐句对得上，主语=伊莱、受事=档案，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（37 词 3 句）：As for the guards they passed, they hardly seemed to notice Eli, blank expressions landing briefly before sliding away. As if he weren’t a threat. He would have been insulted, if he hadn’t learned they were dead.
- 中文理解：一路经过的守卫几乎不看伊莱，空白的表情在他身上停一下就走开，像他算不上什么威胁。要不是他已经知道这些人是死的，他大概会觉得受了侮辱。
- 关键词：blank expressions · they were dead
- 为什么这样写：先写「没被看见」，再补一句短判断 As if he weren’t a threat，把忽视说成一次掂量。末句把被冒犯的情绪和一个更冷的消息兑在一起：insulted 只在还不知道 they were dead 的前提下成立，何况那个前提已经没了。表情滑走的速度由 briefly 和 sliding 两个词管着。
- 读者视角提示：这一块只给表情和一句「他们是死的」，没写谁把他们弄成这样的。守卫不看他，读者也只看得到那张空白。
- **原文**：原文 L106-L106
- **结论**：引语 3 句 37 词（原文 L106）：中文理解逐句对得上，主语=伊莱、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（48 词 3 句）：Eli watched, in fascination and in horror, as the one EO, flesh and blood moments before, crumbled to ash beneath the other’s touch. Apparently, it wasn’t enough that Gabriel Gray could resurrect the dead and bind them to his will. He could send them back just as easily.
- 中文理解：伊莱看着——着迷与恐惧各占一半——那个前一刻还有血有肉的 EO，在另一个人的触碰下塌成灰。看来加百列·格雷能把死人唤回来、把他们的意志拴住，这还不够；他也能一样轻易地把他们送回去。
- 关键词：crumbled to ash · send them back
- 为什么这样写：第一个动词落在看的人身上：watched，紧跟两个相反的反应，fascination 和 horror 中间只隔一个 and。第二句把「复活」和「绑住」并列摆出，第三句用 just as easily 收口，能力的两头就此对齐。当事人从头到尾只有 the one EO 和 the other，两个都不具名。
- 读者视角提示：这一块只有一次触碰和一堆灰，没有一句解释。名字在这里缺席：叙述只写 the other，不写是谁。
- **原文**：原文 L160-L160
- **结论**：引语 3 句 48 词（原文 L160）：中文理解逐句对得上，主语=伊莱、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（49 词 2 句）：Eli sank onto his cot, reached up and brushed the last flecks of ash from his shoulder. He didn’t know if the demonstration was meant only as a threat, or a promise, designed to unnerve Eli, or convince him that he and Gabriel were cut from the same cloth.
- 中文理解：伊莱坐回床铺，抬手把肩上最后那点灰拂掉。他分不清这场演示只是一个威胁，还是一个许诺；是存心让他不安，还是要他相信自己和加百列是从同一块料子上裁下来的。
- 关键词：flecks of ash · as a threat
- 为什么这样写：坐下的动作和拂灰的动作连着写，一样接一样，中间不插话。第二句一口气排出两组对立：threat 对 promise，unnerve 对 convince，四个选项全留在句子里，一个也不勾掉。末句的 cut from the same cloth 把两个人放进同一块布。
- 读者视角提示：这一块只有他一个人的判断，而这个判断的内容是「不知道」。威胁和许诺在他的句子里一样重，读者也没有多一分的线索。
- **原文**：原文 L196-L196
- **结论**：引语 2 句 49 词（原文 L196）：中文理解逐句对得上，主语=伊莱、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符
