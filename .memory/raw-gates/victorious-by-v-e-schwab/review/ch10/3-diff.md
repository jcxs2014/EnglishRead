# 3-diff.md · 《Victorious》第 10 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch10_chapter_ix.txt`
- 受审 md：`ch10 the house comes down.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（said his name in the dark and sat upright in their bed, waki）
- **原文**：原文 L22：“Gabe.” A tense exhale, whispered in the dark. He dragged himself from sleep to find Iris sitting upright in their bed, sheets clutched against her chest.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L22：原文 L22 是外观/随身物品描写（said his name in the dark and sat up…），无情节转折；判提示不修
- **档**：提示

### L3 · R1 事实未进 md（filled the syringe from the vial with a lethal dose, saying ）
- **原文**：原文 L124：“I just want to sleep.” His hands were shaking as he filled the syringe. A lethal dose.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L124：原文 L124 的事实「filled the syringe from the vial with a lethal」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 2（阻断 0 / 提示 2） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（40 词 2 句）：Halfway down, he heard the sound of breaking glass, of straining wood, a voice muttering, half to itself. His office door hung open, the frame splintered around the lock, and through the gap, he saw the man behind the desk.
- 中文理解：下到一半，他就听见玻璃碎裂的声音、木头被撑裂的声音，还有一个人在低声嘟囔，半是对自己说。他诊室的门敞着，锁边的门框裂开了；隔着那道缝，他看见桌子后面站着一个人。
- 关键词：straining wood · splintered around the lock
- 为什么这样写：顺序是耳朵先到、眼睛后到：三种声音一个个报完，才让门缝里那个人出现。half to itself 说明说话的人还没注意到他，所以他此刻还站在暗处。门是从锁那儿被撬开的：裂的是锁一圈的木框，着力点在锁上，等于说明对方是硬来的。他一路走下来停在中段，所以只拿到一条缝的视野，读者拿到的信息和他一样少。
- 读者视角提示：看清最后一个词是 desk——坐在书桌后面的是别人，而这间诊室是他的。位置先易主，对话才开口。
- **原文**：原文 L43-L43
- **结论**：引语 2 句 40 词（原文 L43）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（42 词 2 句）：Paul began to shake his head, a rhythmic motion that didn’t stop, even when he sank his hands into his hair, clawing at his scalp. “You let me think it was all in my head. You let me think I was safe.”
- 中文理解：保罗开始摇头，那个动作有节奏地一直不停，连他把双手插进头发、抓挠头皮的时候都没停。他说：你让我以为这一切都是我脑子里的事。你让我以为我是安全的。
- 关键词：rhythmic motion · think I was safe
- 为什么这样写：先写身体，再让他说话：摇头是有节奏的、停不下来，抓头皮也没让它停——身体已经先一步不听使唤。两句话都以 You let me 开头，把责任钉在同一件事上：指的不是「你害了我」，是「你让我以为」。最后落在 safe 这个词上，最短、最轻的一个词被放在最重的位置。他不喊也不问，只把「我以为」重复两遍。
- 读者视角提示：注意这个句式指控的是隐瞒，不是伤害。后面医生所有解释，都得先过这一关。
- **原文**：原文 L82-L82
- **结论**：引语 2 句 42 词（原文 L82）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（58 词 6 句）：“What happened, Paul?” The air shuddered in his chest. “My sister, Sarah, showed up. I told her she could stay.” Dread began to twine through Gabriel. Over the course of their biweekly sessions, Paul had only mentioned his family once—his grandparents, dead, his parents, estranged. He’d never mentioned a sister. As far as he’d known, Paul was alone.
- 中文理解：「发生了什么，保罗？」他胸腔里的空气抖了一下。「我妹妹莎拉来了。我让她留下了。」恐惧开始在加百列心里缠绕。在此前一系列每两周一次的会谈里，保罗只提过一次家人：祖父母已故，父母疏远。他从没提过有个妹妹。在加百列看来，保罗一直是独自一人。
- 关键词：My sister, Sarah · never mentioned a sister
- 为什么这样写：医生的问话、保罗的回答、医生的核对，三步递进。第三步最有杀伤力：文本用档案式的列举证明保罗从没提过妹妹——正因为没有这个妹妹，他才说谎说她在场。整段以加百列的认知收尾，语气平得像在读病历。
- 读者视角提示：这一段揭穿了保罗整套说辞的底：没有莎拉，也没有那场谋杀。加百列不知道的是，他自己的房子才是那场梦的现场。
- **原文**：原文 L85-L94
- **结论**：引语 6 句 58 词（原文 L85）：中文理解逐句对得上，主语=加百列、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（35 词 0 句）：The walls were glass, and I started to pound on them, but they didn’t break, and I remembered what you said, about being in control, so I imagined them shattering, all those pieces flying outward—
- 中文理解：墙是玻璃的，我开始捶它们，可它们没碎；然后我想起你讲过的话，关于「在掌控之中」，于是我想象它们碎开，所有碎片往外飞——
- 关键词：walls were glass · imagined them shattering
- 为什么这样写：这一句把「他怎么做到的」讲成一条因果链：出不去 → 捶 → 没用 → 想起那句话 → 想象 → 碎。三个 and 把链子串得很紧，读起来像他一边说一边重新走进那个房间。破折号把话截断在碎片飞出去的一刻，动作没有收尾，下一句直接跳到他的声音——作者不给读者看结果，让结果自己从后面追上来。
- 读者视角提示：关键短语是 being in control：他的能力不是失控时才有的，是可以被「想」出来的。而这句话的来源是「你说的」——教他的人此刻就站在他面前。
- **原文**：原文 L109-L109
- **结论**：引语 0 句 35 词（原文 L109）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=玻璃，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（48 词 3 句）：That wasn’t why he’d done it—he’d made the difficult decision to prioritize the experiment, and the data it would give him—them. But the truth was a fine line, a matter of nuance that Paul was in no state to comprehend. “I was trying to protect you,” said Gabriel.
- 中文理解：他当初那样做并不是为了这个——他做过一个艰难的决定：把实验放在前面，也把实验能带来的数据放在前面，那些数据会给他、也给他们。可真相是一条细线，是一种分寸，而保罗现在根本没有能力听懂。「我是想保护你，」加百列说。
- 关键词：prioritize the experiment · a fine line
- 为什么这样写：叙述先替他把动机摊开，用词一个比一个冷：difficult decision、experiment、data。接着一个 But 把话拐回自我衡量：真话被说成一条细线、一种分寸，等于把隐瞒归到「你听不懂」上。最后才给他出声的半句 protect you——比前面的独白短得多，也空得多。心里那套和嘴上那句摆在一起，差出来的部分就是这一章要读者自己填的。
- 读者视角提示：留意 him—them 那一处：数据不只给他，还给他们两个。同一句里既有「我为你好」，也有「我要它」。
- **原文**：原文 L112-L112
- **结论**：引语 3 句 48 词（原文 L112）：中文理解逐句对得上，主语=加百列、受事=线，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符

### 原句 6
- **md**：引语（32 词 1 句）：But then the roof caved in, and the stairs gave way, and the last thing Gabriel felt was her fingers skimming his before the whole house came down on top of them.
- 中文理解：可接着屋顶塌了下来，楼梯断了；加百列最后感觉到的，是她的手指擦过他的，然后整栋房子压到他们身上。
- 关键词：roof caved in · fingers skimming his
- 为什么这样写：三个 and 把三次坍塌串成一条下坠的线：屋顶、楼梯、整栋房子。中间硬插进 the last thing Gabriel felt，让触觉抢在结局之前报到——他先感觉到手指，再被压住。用的是 them 而不是 him：压下去的是三个人。skimming 这个词很轻，只擦到，没有握住；整章从「下楼去救」开始，收在「差一点够到」。
- 读者视角提示：全文最后落在一个感官上，不是画面，也不是声音。作者不写他看见什么，只写他没抓住什么。
- **原文**：原文 L226-L226
- **结论**：引语 1 句 32 词（原文 L226）：中文理解逐句对得上，主语=加百列、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L68）
- **档**：相符
