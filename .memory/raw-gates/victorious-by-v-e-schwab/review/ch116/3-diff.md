# 3-diff.md · 《Victorious》第 116 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch116_chapter_vi.txt`
- 受审 md：`ch116 the knife and the camera.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（which resurrection this was, by Victor’s count: second）
- **原文**：原文 L96：“Something wrong?” asked Victor. “You don’t seem to be healing quite as … gracefully. Then again,” he added, “second resurrections always come with complications.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L96：原文 L96 的事实「which resurrection this was, by Victor’s count」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（40 词 1 句）：Not a phantom, or a dream, but flesh and blood, and looking at him now, Victor should have known, back when he saw Eli glaring at the edge of the road, dressed in combat fatigues, that it wasn’t a hallucination.
- 中文理解：不是幻影，也不是梦，是有血有肉的人；此刻看着他，维克多本该想起当初在路边看见穿作战服的伊莱瞪着自己时，就知道那不是幻觉。
- 关键词：flesh and blood · wasn’t a hallucination
- 为什么这样写：三个否定先排开——`Not a phantom, or a dream`——把先前的两种解释摘掉，才落到 `flesh and blood`。`should have known` 把镜头倒回路边那一幕，那时他把人当成幻觉，这里补上一个迟到的判断。`glaring` 与 `combat fatigues` 只给姿态和衣服，不给一句对话。
- 读者视角提示：这一段没有交手，只有一次回看：路边、军装、瞪视，以及一个早该做出的判断。
- **原文**：原文 L24-L24
- **结论**：引语 1 句 40 词（原文 L24）：中文理解逐句对得上，主语=维克多、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（28 词 3 句）：“Eli. You’re alive.” The word went up at the end, caught between a statement and a question. Not just because Sydney had killed him, but because he looked—wrong.
- 中文理解：「伊莱。你活着。」最后一个字往上扬，悬在陈述与疑问之间。不只是因为西德妮杀过他，还因为他看起来——不对。
- 关键词：went up at the end · he looked—wrong
- 为什么这样写：这一句先给台词，再由叙述者拆它的语调：The word went up at the end，caught between a statement and a question——一句话被作者从外部量出它的音高，落在陈述与疑问之间。解释为什么用 Not just because 起头，先给一个读者以为的理由（她杀过他），再用 but 引出真正的理由：不是那个，是他看起来不对。前半是语法上的犹豫，后半是内容上的不安——被打断的破折号把最后那点判断悬在半空。
- 读者视角提示：读者在这里第一次听见西德妮的声音，而它没有落在陈述或疑问的任何一边。作者不写她害怕还是激动，只说这句话的两端都站不住；紧跟着的「他看起来不对」，把这章后面要打的架提前交代了。
- **原文**：原文 L33-L33
- **结论**：引语 3 句 28 词（原文 L33）：中文理解逐句对得上，主语=西德妮、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L24）
- **档**：相符

### 原句 3
- **md**：引语（40 词 4 句）：Since the night he’d first become an EO, Eli Ever had been pressed in amber. Unchanged. Unchangeable. But now, fresh scars ran across his knuckles, ringed his throat, and what looked like a short knife was embedded in his side.
- 中文理解：从成为 EO 的那一夜起，伊莱·埃弗就像被封在琥珀里，没有变化，也无法变化；可如今他指节上有新疤，喉咙绕着一圈伤痕，侧腹还插着一把像短刀的东西。
- 关键词：pressed in amber · fresh scars
- 为什么这样写：`pressed in amber` 把「不变」写成一枚封住的标本，后面两个单词句各占一处停顿，`Unchanged.` 说状态，`Unchangeable.` 说没有改动的可能。`But now` 一转，落到三处伤：指节上的 `fresh scars`、绕喉一圈的 `ringed his throat`、侧腹的 `what looked like a short knife`。三处都先报位置，刀只写 `looked like`，谁插的没有交代。
- 读者视角提示：先给一个「不变」的旧印象，再用三处伤把它推翻；伤的位置从上往下走，手、喉咙、侧腹。
- **原文**：原文 L36-L36
- **结论**：引语 4 句 40 词（原文 L36）：中文理解逐句对得上，主语=伊莱、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L34）
- **档**：相符

### 原句 4
- **md**：引语（45 词 2 句）：Eli took a step toward Victor, who reached out before he could take a second one and wrenched on the pain in Eli’s side, as effectively as if he’d twisted the knife. Eli faltered, and Victor took the opportunity to shoot him in the face.
- 中文理解：伊莱朝维克多迈出一步，维克多在他迈第二步之前伸手拧住他侧腹的痛，效果就像直接拧动那把刀；伊莱踉跄了一下，维克多趁机朝他脸上开了一枪。
- 关键词：wrenched · shoot him in the face
- 为什么这样写：`took a step` 与 `before he could take a second one` 把时间压在一两步之间。`wrenched on the pain` 把痛本身当成把手来拧，后半句 `as effectively as if he’d twisted the knife` 才点出对应物是侧腹那把刀。`faltered` 只有一个词，紧接的 `took the opportunity` 把这一下踉跄换成了开枪的窗口。
- 读者视角提示：这一块是两步之间的交换：一步、一拧、一踉跄、一枪，谁先动谁后动都写在句子的主从结构里。
- **原文**：原文 L78-L78
- **结论**：引语 2 句 45 词（原文 L78）：中文理解逐句对得上，主语=维克多、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L40）
- **档**：相符

### 原句 5
- **md**：引语（65 词 3 句）：Victor swung the gun up as Eli started toward him. He dodged the first shot, caught the next three in the chest, but didn’t stop. Eli was brute force, a battering ram, charging toward Victor, who turned the dials up as high as they would go, until Eli finally buckled, the pain enough to bring him to his knees, a scream tearing up his throat.
- 中文理解：伊莱一动，维克多就抬枪；伊莱躲开第一枪，胸口接下后面三枪，脚步没有停。伊莱是一股蛮力，像撞门的槌，直冲过来；维克多把旋钮调到最高，直到伊莱终于弯下去，痛得跪倒，一声尖叫从喉咙里撕出来。
- 关键词：brute force · turned the dials up
- 为什么这样写：三枪用 `the next three` 一次带过，`but didn’t stop` 把中枪和前进并排放着。`brute force, a battering ram` 两个同位语连着给，第二个比第一个更具体，把人和一件撞门用的器物并在一处。`turned the dials up as high as they would go` 把旋钮推到顶，结果用三个动作交代：`buckled`、`to his knees`、`a scream tearing up his throat`。
- 读者视角提示：这一段的速度来自枪与人的对比：子弹打中，人不倒；旋钮拧到头，人才跪。最后落下的不是画面，是声音。
- **原文**：原文 L141-L141
- **结论**：引语 3 句 65 词（原文 L141）：中文理解逐句对得上，主语=维克多、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L46）
- **档**：相符

### 原句 6
- **md**：引语（37 词 2 句）：He swung the gun up, aiming not for Eli but the camera in the corner of the room. “Therapy requires a foundation of mutual respect,” he said, addressing Gabriel. “If you want mine, come kill me yourself.”
- 中文理解：他抬起枪，枪口不指伊莱，而指向房间角落的摄像头；他说治疗需要相互尊重作底子，又对加百列说，想要他的尊重，就自己来杀他。
- 关键词：mutual respect · come kill me yourself
- 为什么这样写：`aiming not for Eli but the camera` 用 not...but 把目标从人换成机器，一句里改掉了整场对峙的对象。台词先讲条件 `requires a foundation of mutual respect`，再提要求；`If you want mine` 是条件句的前半，后半句 `come kill me yourself` 是命令句，动作直接派给加百列。
- 读者视角提示：这一段没有交手，只有一个转向：枪口从眼前的人移到墙角的镜头，话也从打斗转向谈判。
- **原文**：原文 L174-L174
- **结论**：引语 2 句 37 词（原文 L174）：中文理解逐句对得上，主语=伊莱、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L52）
- **档**：相符

### 原句 7
- **md**：引语（55 词 3 句）：There was no time to wonder if it would pay off. In the time it had taken to deliver the message, Eli was there, sinking the other shard of glass into Victor’s side. Too shallow to do more than scrape over his hip bone, but with his nerves turned up so high, it fucking hurt.
- 中文理解：他没有时间去想这一枪值不值；就在他把话说完的这段时间里，伊莱已经到了跟前，把另一块玻璃碎片扎进他侧腹。伤口浅得只能刮过髋骨，可他的神经调得那么高，疼得骂了出来。
- 关键词：sinking the other shard · hip bone
- 为什么这样写：第一句先把赌注的账按住，`no time to wonder if it would pay off`。第二句用 `In the time it had taken to deliver the message` 把代价算在说话的长度上：话说完，人已经到。伤口用 `Too shallow` 起头，先报轻，再用 `but` 翻到 `it fucking hurt`，最后两个词把前面那点克制撤掉。
- 读者视角提示：章末停在伤口上：浅、刮过骨头、疼。旋钮在前面被拧到最高，代价在这里落回身体。
- **原文**：原文 L183-L183
- **结论**：引语 3 句 55 词（原文 L183）：中文理解逐句对得上，主语=伊莱、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符
