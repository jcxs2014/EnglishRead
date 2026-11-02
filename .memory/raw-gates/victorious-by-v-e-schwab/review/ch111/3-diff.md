# 3-diff.md · 《Victorious》第 111 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch111_chapter_i.txt`
- 受审 md：`ch111 the door and the roof.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（asked Victor in his ear if he was ready, and Victor answered）
- **原文**：原文 L45：“Hey, Vic,” said a voice in his ear. “Are you ready?”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L45：原文 L45 的事实「asked Victor in his ear if he was ready, and V」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（Eli speaks into Victor's ear and Victor's mouth tugs into a ）
- **原文**：原文 L48：His mouth tugged into a grim smile. Of all the ways this could have gone. All the paths and permutations.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L48：原文 L48 的事实「Eli speaks into Victor's ear and Victor's mout」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（Eli always puts a lot of stock in the Almighty and would tak）
- **原文**：原文 L96：Victor began to chuckle. Not at the sky so much as Eli’s obvious displeasure. The fact it wasn’t giving him this last reward, the fact he’d expected it to in the first place, the fact he would probably take it as a sign of disapproval from the Almighty he was always putting so much stock in, made th
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L96：原文 L96 的事实「Eli always puts a lot of stock in the Almighty」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 3（阻断 0 / 提示 3） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（31 词 7 句）：VICTOR stood before the metal door. The one that led into EON. He knew what lay beyond the threshold. What was waiting for him there. Death. And the doctor. And Sydney.
- 中文理解：维克多站在那扇金属门前，就是通向 EON 的那一扇。他知道门槛后面是什么，是什么在那儿等着他：死亡。还有那位医生。还有西德妮。
- 关键词：metal door · led into EON
- 为什么这样写：开头不写时间，也不写地点，先给一具站定的身体和一扇门。第二句才把门通向哪里说出来，`EON` 三个字母落在句尾。第三句把门后的东西说出来，但不写成一句完整的话，拆成三项，一项一句：`Death.`、`And the doctor.`、`And Sydney.`。前两项是类别，第三项是一个名字。`He knew` 放在清单前面，这份清单他事先就有了。
- 读者视角提示：读者先看见一个人和一扇门，再看见门通向哪里，最后才看见门后等着什么。三项各占一句，读到第三项，清单才落到一个具体的人名上。
- **原文**：原文 L21-L36
- **结论**：引语 7 句 31 词（原文 L21）：中文理解逐句对得上，主语=维克多、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（45 词 3 句）：The door was unlocked, but as Victor brought his hand to the cold steel he paused, and drew the inhaler from his coat. He held it to the light, studying the violet liquid in the cartridge, calculating how much he’d need. How much was left.
- 中文理解：门没有上锁，可维克多把手按上冰冷的钢面时停住了，从外套里取出吸入器。他把它举到光下，端详药筒里的紫色液体，算自己需要多少。还剩多少。
- 关键词：cold steel · violet liquid
- 为什么这样写：第一句先给一个否定的事实：门没上锁。紧接着一个 `but`，他在钢面前停住。后面三个动作连成一串：取出、举到光下、端详。算的是两件事，需要多少，还剩多少；第二问单独成句，只有四个词。这一段没有写他为什么停，也没有写剂量不够会怎样。
- 读者视角提示：读者跟着他停在门口，看他取药、对着光看、在心里算。段落停在「还剩多少」这一问上，没有给答案。
- **原文**：原文 L39-L39
- **结论**：引语 3 句 45 词（原文 L39）：中文理解逐句对得上，主语=维克多、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L24）
- **档**：相符

### 原句 3
- **md**：引语（60 词 2 句）：He crossed the roof with the grim determination of a penitent, and Victor followed, the ghost of the hospital bracelet still on his wrist, compliments of his own failed attempt at transformation. It was Eli’s turn tonight, the ice already melting in the bath downstairs, but he’d insisted on seeing the stars one last time, in case something went wrong.
- 中文理解：他带着忏悔者那种沉着的决意穿过屋顶，维克多跟在后面，手腕上还留着住院手环的印子，那是他自己那次失败的转化尝试留下的。今晚轮到伊莱，楼下浴缸里的冰已经在化，可他坚持要最后看一次星星，以防出什么差错。
- 关键词：hospital bracelet · failed attempt at transformation
- 为什么这样写：一句里分出先后：`He crossed the roof` 是伊莱，`Victor followed` 是维克多，两个人一前一后。手腕上的印子写成 `the ghost of the hospital bracelet`，后面紧跟 `compliments of his own failed attempt at transformation`，印子的来由在同一句里交代。末句把今晚的安排一次给全：轮到伊莱、冰在化、他要先看星星，理由是 `in case something went wrong`。
- 读者视角提示：读者先看见两个人一前一后穿过屋顶，再看见维克多手腕上的印子。末句把今晚要做的事和可能出的差错放在同一句里。
- **原文**：原文 L87-L87
- **结论**：引语 2 句 60 词（原文 L87）：中文理解逐句对得上，主语=维克多、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L30）
- **档**：相符

### 原句 4
- **md**：引语（45 词 8 句）：Eli stopped in the center of the roof, hands at his sides as his head tipped back. He frowned. Victor followed his gaze. And smirked. It was fucking overcast. Not even low clouds that banked the city light, but a flat, uninspired gray. Starless. Dull.
- 中文理解：伊莱在屋顶中央停下，双手垂在身侧，头往后仰。他皱起眉。维克多顺着他的目光看过去，撇嘴笑了。天阴得厉害。连那种压着城市灯光的低云都没有，只有一片平平的、没什么看头的灰。没有星。沉闷。
- 关键词：tipped back · banked the city light
- 为什么这样写：先给一个停住的动作：站到屋顶中央、双手垂着、头往后仰，三样都落在身体上。接着两个短句分给两个人，`He frowned.` 是伊莱，`And smirked.` 是维克多。写天空一路往下减：先说 `It was fucking overcast`，再排除一种更好看的阴天，`Not even low clouds that banked the city light`，最后落到 `a flat, uninspired gray`。收尾两个词，`Starless. Dull.`
- 读者视角提示：读者先看见伊莱仰头，再看见他皱眉；视线转到维克多，他笑了。天空的写法一路往下减：先是阴，再是连低云也没有，最后只剩一片灰、没有星、沉闷。
- **原文**：原文 L93-L93
- **结论**：引语 8 句 45 词（原文 L93）：中文理解逐句对得上，主语=维克多、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L36）
- **档**：相符

### 原句 5
- **md**：引语（43 词 3 句）：Of all the moments in his life, this might be the one he’d choose to live inside. He and Eli, laughing beneath a starless, ordinary sky. The scales, yet to tip, the lines, not yet crossed, the energy around them electric with potential.
- 中文理解：在他一生的所有时刻里，这也许是他愿意住进去的那一个。他和伊莱，在一片没有星的、普通的天空底下笑着。天平还没有倾斜，界线还没有越过，两个人周围的能量满是可能。
- 关键词：live inside · electric with potential
- 为什么这样写：第一句把范围放到最大，`Of all the moments in his life`，再从中挑出一个，`might be` 留了余地。第二句只有两个人、一片天，`starless, ordinary sky` 把前面那片阴天收进来。第三句三个短语并排，前两个都带 `yet` 与 `not yet`，说的是还没发生，`The scales, yet to tip`、`the lines, not yet crossed`，最后一个落在 `electric with potential`。
- 读者视角提示：读者先拿到一个从一生里挑出来的时刻，再看见这个时刻里只有两个人、一片普通的天。最后一句三样东西都还没有发生，句子停在「可能」上。
- **原文**：原文 L108-L108
- **结论**：引语 3 句 43 词（原文 L108）：中文理解逐句对得上，主语=伊莱、受事=线，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符
