# 3-diff.md · 《Victorious》第 48 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch48_chapter_iii.txt`
- 受审 md：`ch48 gabriel asks if eli wants to kill him.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（named Serena as the EO who had held him）
- **原文**：原文 L57：Fuck. Eli clenched his teeth against the name, felt it rise up anyway. “Serena.” Before Gabriel could pry, Eli changed course. “I’m amazed they let someone like you take charge of EON.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L57：原文 L57 的事实「named Serena as the EO who had held him」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（31 词 2 句）：He was sitting in a room across from Gabriel, a low round table the only thing between them. The walls were the same muted green as the ones in his cell.
- 中文理解：他坐在一间房里，对面是加百列，两人之间只隔着一张矮圆桌。墙的绿色和他牢房里那一种是一样的。
- 关键词：a low round table · muted green
- 为什么这样写：两人之间只有一张矮桌，没有栅栏、没有审讯台，隔开的距离短得可以伸手够到；这一句先把场面摆成对谈，再让读者自己发现这场对谈不对等。第二句只写颜色：换了房间，墙色没换，他仍坐在同一种绿里。
- 读者视角提示：本块没有交代这场会面由谁安排、为什么安排，只有两个人、一张桌子和一种颜色。读者掌握的信息跟推门进来那一刻一样少。
- **原文**：原文 L21-L21
- **结论**：引语 2 句 31 词（原文 L21）：中文理解逐句对得上，主语=加百列、受事=牢房，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（48 词 3 句）：He considered the space between the chairs, wondered if he could break the table glass and cut the EO’s throat—wondered, the way he had a hundred times when he was in Serena’s grip—and knew, even as he thought it, that he couldn’t. His body wouldn’t let him. Yet.
- 中文理解：他打量两把椅子之间的距离，想自己能不能砸开桌面玻璃，割开这个 EO 的喉咙；这样的念头他在塞雷娜手里时起过上百次。可他想的同时就知道自己做不到：他的身体不让他动。暂时不。
- 关键词：the EO’s throat · Serena’s grip
- 为什么这样写：一个长句把「想」和「知道做不到」压在同一条线上，中间用破折号插进旧经验，把这次杀意接到上百次的旧念头上，杀意因此不是新起的，而是熟悉的。末句只剩一个词 Yet.，把「做不到」留成时限，不写成结论。
- 读者视角提示：挡住他的是身体，不是他改了主意。Yet. 单独成句，读的时候要留意它把门留着。
- **原文**：原文 L30-L30
- **结论**：引语 3 句 48 词（原文 L30）：中文理解逐句对得上，主语=塞雷娜、受事=玻璃，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（41 词 3 句）：Eli looked down and saw a paper excerpt. The headline read: LOCAL PASTOR LEADS NEW FLOCK. Beneath the heavy type, a black-and-white photo of his father, standing before the church with Eli on one side and his mother on the other.
- 中文理解：伊莱低下头，看见一段纸上的摘录。标题写着「本地牧师带领新会众」。粗体字下面是一张黑白照片：他父亲站在教堂前，伊莱在一边，他母亲在另一边。
- 关键词：The headline read · before the church
- 为什么这样写：剪报把这个家摆成公开的版面：全大写的标题先把父亲写成带领者，照片再把三个人按站位排开，父亲在中间偏前，母亲与儿子分在两侧。叙述只给标题与位置，不给照片里的情绪，读者要自己把这张合影和前面那些话对起来。
- 读者视角提示：这是纸上的一页，不是伊莱主动回忆的往事；读它的人和被它指认的人是同一个人。
- **原文**：原文 L69-L69
- **结论**：引语 3 句 41 词（原文 L69）：中文理解逐句对得上，主语=伊莱、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（37 词 1 句）：But in a way, he is the source of my faith.” Eli dragged his gaze up to meet the therapist’s. “The first time I felt the grace of God was when I pushed him down the stairs.”
- 中文理解：可某种意义上，父亲正是他信仰的来源。伊莱把目光抬起来，对上治疗师的眼睛，说第一次感到神的恩典，是他把父亲推下楼梯那一次。
- 关键词：the grace of God · my faith
- 为什么这样写：两句自述中间夹着一个动作：dragged his gaze up to meet the therapist’s，把承认从自言自语变成对视。grace of God 与 pushed him down the stairs 落在同一句里，两个分量差得极远的说法贴在一起，句子不解释，也不收回。
- 读者视角提示：这句话是他自己说出来的，不是被追问逼出的结论；本块没写他为什么推那一下，也没写父亲当时怎样。
- **原文**：原文 L75-L75
- **结论**：引语 1 句 37 词（原文 L75）：中文理解逐句对得上，主语=伊莱、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（35 词 2 句）：You were in control, when you killed your father. You were in control, when you went in search of powers, and when you found them, and you were in control of every life you took.
- 中文理解：你杀你父亲的时候，是你在掌控。你去找力量的时候、找到力量的时候，也是你在掌控；你取走的每一条命，同样是你在掌控。
- 关键词：in control · killed your father
- 为什么这样写：同一个开头重复三次，把一段人生按节点数过去；每重复一次，掌控的范围就扩大一格，从一个人扩到力量，再扩到所有被他取走的命。句子不给形容词，只给句式，指控因此像清点。
- 读者视角提示：这是加百列说的话，不是叙述者的判断；他把它说完，没有停在那里等回应。
- **原文**：原文 L96-L96
- **结论**：引语 2 句 35 词（原文 L96）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符

### 原句 6
- **md**：引语（40 词 3 句）：“What I do know,” he pressed on, “is that we are monsters, all of us. I used to think I was an exception, but I’m not. EOs are an error, a crime against nature and a danger to the world.
- 中文理解：他说自己确实知道一件事：他们都是怪物，一个不落。他以前以为自己是例外，现在不这么看了。EO 是错误，是对自然的犯罪，是世界的危险。
- 关键词：we are monsters · an exception
- 为什么这样写：开头一句把「不知道」翻成「知道」，靠一个插入语 pressed on 抢回主动权。三句一步一退又一步一进：先把自己并进「我们」，再撤掉「例外」，最后用三个并列的说法给 EO 定性。他撤掉的是自己那个「例外」。
- 读者视角提示：这一段里他把「例外」这个词用在自己身上，又亲手划掉；话说到这里，还没有提对面这个人。
- **原文**：原文 L117-L117
- **结论**：引语 3 句 40 词（原文 L117）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L68）
- **档**：相符

### 原句 7
- **md**：引语（34 词 4 句）：He tried to picture it. Crossing to the therapist, wrapping his hands around his throat, feeling the pulse falter, and fail. It should have steadied him. Instead, Eli recoiled from the image, the idea.
- 中文理解：他试着把那件事想出来：走过去，双手掐住治疗师的喉咙，感觉那脉搏乱掉、停掉。这本该让他定下来。可他从这幅画面前、从这个念头前，缩了回去。
- 关键词：picture it · around his throat
- 为什么这样写：先是三个连续的动作短语（crossing、wrapping、feeling），全在想象里完成，读起来像已经动手。第四句 It should have steadied him 把期待摆明，第五句一个 Instead 把这期待掀翻；收在 recoiled from the image, the idea，连「念头」本身也一起退开。
- 读者视角提示：动手全程只发生在想象里，他一步也没离开座位。本块没有解释他为什么缩手。
- **原文**：原文 L129-L129
- **结论**：引语 4 句 34 词（原文 L129）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L78）
- **档**：相符
