# 3-diff.md · 《Victorious》第 83 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch83_chapter_xiii.txt`
- 受审 md：`ch83 the ice shatters and eli draws his gun.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（was freed when Serena’s illusion shattered and the ice surro）
- **原文**：原文 L18：THE moment Serena’s illusion shattered, so did the ice surrounding Eli.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L18：原文 L18 是一处静态状态描写（was freed when Serena’s illusion sha…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（37 词 1 句）：The frozen tomb around him crumbled, and the real world came rushing back, the sisters’ well-lit house replaced by Madman’s Mansion, darkened rooms and clapboard walls and warping floors, the boards shot through with early morning light.
- 中文理解：围着他的那座冻起来的坟塌了，真实世界一下涌回来：姐妹俩那栋亮着灯的房子换成疯人宅邸——昏暗的房间、木条墙、翘起的地板，木板缝里透进清晨的光。
- 关键词：the real world · came rushing back
- 为什么这样写：一场幻觉的收场不写塞雷娜那边，只从冰壳这侧落笔：先让 tomb 塌，再一样一样换掉地点——亮着的房子换成昏暗房间、木条墙、翘地板，最后一道清晨的光从板缝里穿进来。地点是靠几样看得见的东西换掉的，没有一句交代「这里是哪里」。
- 读者视角提示：读者上一章还在那间复刻的卧室里，这里第一眼站到伊莱的位置上：房子不是走出来的，是塌掉的；板缝里已经透进清晨的光。
- **原文**：原文 L21-L21
- **结论**：引语 1 句 37 词（原文 L21）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（30 词 2 句）：Eli staggered and gasped, lungs hitching as they finally found air. Sank to one knee, and let out a guttural sound, blood dripping from his nose, his eyes, his ears.
- 中文理解：伊莱踉跄了一下，大口喘气，肺终于吸到空气，一顿一顿地抽；他单膝跪下去，喉咙里挤出一声粗哑的响，血从鼻子、眼睛、耳朵里往下滴。
- 关键词：staggered and gasped · blood dripping
- 为什么这样写：两个动作挨着来：先站不稳，再跪下去；中间的 lungs finally found air 把「冻了多久」写成一件身体上的事。声音只给一个 guttural，血却点了三处——鼻子、眼睛、耳朵，一处比一处不像外伤。全句没有一句写疼。
- 读者视角提示：读者看到的不是「他脱困了」，而是脱困之后身体先垮：气是抢回来的，血是从三个不该出血的地方流出来的。
- **原文**：原文 L24-L24
- **结论**：引语 2 句 30 词（原文 L24）：中文理解逐句对得上，主语=伊莱、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L25）
- **档**：相符

### 原句 3
- **md**：引语（30 词 2 句）：He retched blood onto the floor, head ringing like a bell as Noah’s voice played in the room and in his ear. “Target B acquired. In pursuit of Target A.”
- 中文理解：他朝地板上呕出血来，头像被敲响的钟一样嗡鸣；诺亚的声音同时在房间里、也在他耳边的通讯里响着：「已获取 B 目标。正在追 A 目标。」
- 关键词：head ringing · Target B acquired
- 为什么这样写：这一块把人分成两半：身体在地上呕血，耳朵已经在接战况。head ringing like a bell 是明喻，钟的余响正好对上声音「在房间里也在耳朵里」的双重来源。报点分成两个短句，中间一个句号，像通讯里的通话，没有多余的字。
- 读者视角提示：读者和他同时听到这两句：先知道 B 目标已经到手，再知道有人在追 A 目标；A 是谁，这两句里没有说。
- **原文**：原文 L36-L36
- **结论**：引语 2 句 30 词（原文 L36）：中文理解逐句对得上，主语=诺亚、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 4
- **md**：引语（34 词 2 句）：Eli spat, and forced his body upright, wiping blood from his mouth with the back of one hand and drawing his gun with the other as a wisp of blond hair vanished overhead. Sydney.
- 中文理解：伊莱啐了一口，把身体撑直：一只手用手背抹掉嘴上的血，另一只手拔枪；就在这时候，一缕金发在头顶一闪而过。西德妮。
- 关键词：blond hair vanished · drawing his gun
- 为什么这样写：一句话里排了两只手的分工——抹血、拔枪——中间用 and 连住，动作之间没有停顿。金发只给「一缕」和「一闪」，人没有露脸；紧接的一个词 Sydney 单独成句，认人这一步比她本人先到。
- 读者视角提示：读者先看见金发，再看见名字单独占一行；她人还没出场，名字已经被叫出来，追的人也已经把枪拿在手里。
- **原文**：原文 L39-L39
- **结论**：引语 2 句 34 词（原文 L39）：中文理解逐句对得上，主语=西德妮、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L39）
- **档**：相符
