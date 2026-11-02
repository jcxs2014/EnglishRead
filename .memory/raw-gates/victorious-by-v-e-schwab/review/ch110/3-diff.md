# 3-diff.md · 《Victorious》第 110 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch110_chapter_xl.txt`
- 受审 md：`ch110 the clone and the hammer.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（fired off a text from Dani's phone while pulling out of the ）
- **原文**：原文 L33：As Victor pulled out of the lot, he fired off a text from Dani’s phone.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L33：原文 L33 的事实「fired off a text from Dani's phone while pulli」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（wrote back to Mitch on the message board while keeping the w）
- **原文**：原文 L78：Victor kept the weapon trained on Jeremy as he wrote back.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L78：原文 L78 的事实「wrote back to Mitch on the message board while」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（Jeremy is Dani's younger brother, and they have a standing p）
- **原文**：原文 L30：I’m there if he needs me, and he’s there if I need him.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L30：原文 L30 的事实「Jeremy is Dani's younger brother, and they hav」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L6 · R1 事实未进 md（the state of the dot beside his handle on the board: green t）
- **原文**：原文 L105：Meanwhile, the seconds turned to minutes, and Mitch didn’t call. And the dot beside his handle had gone from green to gray. Offline. Victor swore under his breath and followed the pilot up the stairs.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L105：原文 L105 是外观/随身物品描写（the state of the dot beside his hand…），无情节转折；判提示不修
- **档**：提示

### L7 · R1 事实未进 md（the digits in Mitch's board handle: 1652）
- **原文**：原文 L81：SHARPENEDSPADE1652: ACTUAL STORM? OR CLOUDS ON THE HORIZON?
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L81：原文 L81 的事实「the digits in Mitch's board handle: 1652」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 5（阻断 0 / 提示 5） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（39 词 3 句）：He sank behind the wheel, and double tapped an icon on his phone. The screen changed color, the backdrop no longer flat black but a constellation, a chemical formula, rendered as stars. No longer his phone, but Dani’s—a clone.
- 中文理解：他坐进驾驶座，双击手机上的一个图标。屏幕换了颜色，底色不再是纯黑，而是一片星座，一道化学式，化成星子。那不再是他的手机，是丹妮的——一个克隆。
- 关键词：behind the wheel · rendered as stars
- 为什么这样写：这一段把三件事按顺序摆开：人坐下、手指点两下、屏幕变色。`no longer flat black but a constellation` 用一对反义词换掉底色，接着 `a chemical formula, rendered as stars` 把化学式写成星图，专业符号与夜空叠在一处。最后一句才交代手机是谁的，`No longer his phone, but Dani’s—a clone`，破折号后只留两个词。
- 读者视角提示：视线从方向盘后的身体移到手指，再移到屏幕：先看见颜色变了，再看见底色成了星图，最后一句才知道这部手机不是他的。
- **原文**：原文 L24-L24
- **结论**：引语 3 句 39 词（原文 L24）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（35 词 3 句）：By the time he reached the airstrip, the tracker had finally stopped moving. Dol’s red dot now hovered in some place called Bethany, six hours to the west and south. Halfway between Victor and Merit.
- 中文理解：等他到简易机场，追踪器终于不再移动。DOL 的红点这时悬在一个叫贝瑟尼的地方，向西向南各六小时。正好在维克多与梅里特之间。
- 关键词：stopped moving · west and south
- 为什么这样写：`By the time he reached the airstrip` 把整段路程压进一个从句，落脚点是 `finally stopped moving`——从上一章起一直在动的那个点，到这里停住。接着三句给位置，一句比一句窄：先地名（`some place called Bethany`），再时距（`six hours to the west and south`），最后是三点之间的相对位置（`Halfway between Victor and Merit`）。`Halfway` 只给几何关系。
- 读者视角提示：先得到「停了」，再得到「在哪」，最后得到「在谁和谁之间」。地图一层层收窄，落在一个居中的位置上。
- **原文**：原文 L39-L39
- **结论**：引语 3 句 35 词（原文 L39）：中文理解逐句对得上，主语=维克多、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L24）
- **档**：相符

### 原句 3
- **md**：引语（32 词 2 句）：In person, the resemblance between the Dean siblings was even sharper. The same keen eyes, the same pointed chin, the same frown that spread outward from his mouth, took over his face.
- 中文理解：当面看，迪恩家兄妹的相像更明显。一样的锐利眼睛，一样的尖下巴，一样的、从嘴向外铺开占满整张脸的皱眉。
- 关键词：the Dean siblings · pointed chin
- 为什么这样写：开头 `In person` 把比较放到当面，后面三个 `The same` 排着队往下压：眼睛、下巴、皱眉，一处比一处大。最后落在 `took over his face`，皱眉不是长在脸上，而是从嘴向外扩、把整张脸接管过去。`even sharper` 把「像」写成有程度的东西，当面这一看把它推得更高。
- 读者视角提示：三个「一样的」由小到大排下去：眼睛、下巴、整张脸。读到最后一个分句，脸已经被一个表情占满。
- **原文**：原文 L48-L48
- **结论**：引语 2 句 32 词（原文 L48）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L30）
- **档**：相符

### 原句 4
- **md**：引语（39 词 2 句）：Victor thought of hurting him. But pain made people sloppy, and he needed the pilot sharp, so he settled for pulling out his gun, thumbing off the safety as he swung it up, the barrel level with Jeremy’s head.
- 中文理解：维克多想过伤害他。但疼痛会让人手脚变钝，而他需要这个飞行员保持清醒，于是他退一步，只把枪拔出来，拇指推开保险，把枪抬起来，枪口与杰瑞米的头齐平。
- 关键词：pain made people sloppy · his gun
- 为什么这样写：第一句是念头，只有六个词；第二句用 `But` 把它按住，理由落在效率上：`pain made people sloppy`，而他要的是 `the pilot sharp`。`settled for` 把这一步定在退而求其次的位置上。后面四个动作连成一条线：`pulling out`、`thumbing off the safety`、`swung it up`，最后停在 `the barrel level with Jeremy’s head`。
- 读者视角提示：先看见一个没做的动作，再看见一个做了的动作。枪的行程被拆成拔、开保险、抬起、端平四步，落在与头齐平的高度上。
- **原文**：原文 L63-L63
- **结论**：引语 2 句 39 词（原文 L63）：中文理解逐句对得上，主语=维克多、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L36）
- **档**：相符

### 原句 5
- **md**：引语（33 词 2 句）：On the top step, Jeremy hesitated. Victor suspected it was more out of a sense of obligation than a real desire to resist, but either way, he didn’t have time for noble gestures.
- 中文理解：在舷梯最上面一级，杰瑞米迟疑了一下。维克多猜这更多是出于一种义务感，而不是出于真想反抗，但无论哪一种，他都没时间应付体面的姿态。
- 关键词：Jeremy hesitated · a sense of obligation
- 为什么这样写：停顿被放在 `On the top step` 这个位置上——一只脚已经踏上飞机。第二句用 `suspected` 给出判断，`more out of … than …` 把两种动机放在天平两头，`either way` 随即取消分辨的必要，因为结论不取决于哪一种。收尾 `didn’t have time for noble gestures` 把迟疑记在时间账上，而不是勇气上。
- 读者视角提示：镜头停在最高一级台阶上。判断只出现一次，随后被 `either way` 推开，句子落在「时间」这个词上。
- **原文**：原文 L108-L108
- **结论**：引语 2 句 33 词（原文 L108）：中文理解逐句对得上，主语=维克多、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符
