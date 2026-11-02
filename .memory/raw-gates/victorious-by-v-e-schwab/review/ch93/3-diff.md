# 3-diff.md · 《Victorious》第 93 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch93_chapter_xxiii.txt`
- 受审 md：`ch93 the girl who was not syd.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（used a corpse as a shield until she heard an empty magazine,）
- **原文**：原文 L75：The other agent started shooting as the first one slumped, but she held the body up, the corpse shield absorbing the damage until she heard the telltale click of an empty magazine. She dropped the body, crouching with it, before bringing the blade up behind the agent’s armor.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L75：原文 L75 的事实「used a corpse as a shield until she heard an e」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（climbed into the transport, knelt in front of Syd, unclipped）
- **原文**：原文 L93：“Hey, kiddo,” she murmured, climbing up into the transport. She knelt in front of Syd, unclipping the IV. Undoing the straps. “Let’s get out of here.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L93：原文 L93 的事实「climbed into the transport, knelt in front of 」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（took the whole fight from start to finish in less than a min）
- **原文**：原文 L81：June stood, winded from the effort, her borrowed body—a soldier’s—flecked with blood. The whole thing, start to finish, had taken less than a minute. Not bad.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L81：原文 L81 的事实「took the whole fight from start to finish in l」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 3（阻断 0 / 提示 3） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（43 词 3 句）：“We’ve got an obstruction,” said the first agent, the one behind the wheel, as the armored transport slowed, then stopped. “Investigate,” he instructed the second, in the passenger seat. They nodded, and climbed down, drawing a weapon as they approached the stranded vehicle.
- 中文理解：开车的探员报告前方有障碍，装甲运输车减速、停下；他让坐在副驾的同伴下去查看。那人应了一声，下车，一边走一边拔出武器，走向那辆抛锚的车。
- 关键词：an obstruction · drawing a weapon
- 为什么这样写：三句话把一套程序走完：发现、下令、执行。说话的人始终留在驾驶座，动作交给副驾；命令只有 "Investigate" 一个词，语气是公事。直到最后才出现 "stranded vehicle"，读者和那名探员一起走近它，而车里有什么，这一段一个字没提。
- 读者视角提示：读者看到的是一支按流程办事的队伍：减速、下令、下车、拔枪，四步之间没有一句多余的话；本段最后三个词把视线留在车上，人反而退到旁边。
- **原文**：原文 L45-L45
- **结论**：引语 3 句 43 词（原文 L45）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（44 词 2 句）：The agent leaned in and turned the key, triggering the generous block of C4 June had strapped to the roadster’s undercarriage. The blast not only blew the car—and the agent—to pieces but was strong enough to rock the armored van a dozen yards away.
- 中文理解：探员俯身拧动钥匙，引爆了琼绑在跑车底盘上的那一大块 C4。爆炸把车和那名探员一起炸成碎片，冲击力还足够把十几码外的装甲车震得摇晃。
- 关键词：turned the key · armored van
- 为什么这样写：引爆被压进一个顺手的小动作：拧钥匙。C4 的来历只用半句交代——琼绑上去的——没有写她什么时候动的手。第二个句子把爆炸的规模从近处量到远处：车与那名探员成了碎片，十几码外的装甲车被震得摇晃；伤害一圈圈往外扩，落点在 "a dozen yards away"。
- 读者视角提示：钥匙是那名探员自己拧的，「查看」在他手指底下变成了「引爆」。读者跟着他的手走，爆炸在同一句里发生，前面没有预警的句子，也没有人喊一声。
- **原文**：原文 L60-L60
- **结论**：引语 2 句 44 词（原文 L60）：中文理解逐句对得上，主语=琼、受事=碎片，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L25）
- **档**：相符

### 原句 3
- **md**：引语（20 词 1 句）：June fired, painting the window behind him red as the agents in the back of the van sprang into action.
- 中文理解：琼开了枪，把车窗外那一片染成红色，与此同时，车厢后面的探员们弹起身来。
- 关键词：window behind him red · sprang into action
- 为什么这样写：分词短语 painting…red 把一次开枪写成一笔涂抹：不是 bullet，是 paint，人被写成了一幅画的底。as 一边连接后面的动作，车里的人正在起身——两个动作被绑在同一时间里，读者没法先处理其中一个。最后一个词用了跳（sprang），说明战斗在枪响的同时才真正开始。
- 读者视角提示：这一章的追车在烟幕里打。琼一直在借别人的身体开路——司机、探员、车厢——这一枪是本章她第一次直接动手。
- **原文**：原文 L63-L63
- **结论**：引语 1 句 20 词（原文 L63）：中文理解逐句对得上，主语=琼、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 4
- **md**：引语（47 词 2 句）：She stumbled, swapping bodies before the first one died, and drawing a serrated knife. She darted forward, slipping in beneath the agent’s guard before they could get off a second shot, and fit the blade into the crook just beneath the helmet’s chin, carving quick and deep.
- 中文理解：她踉跄了一下，趁借用的那具身体还没断气就换成另一具，同时抽出一把锯齿刀。她往前一冲，钻进那名探员防守的内侧，抢在对方开出第二枪之前，把刀嵌进头盔下缘与下巴之间的凹处，划得又快又深。
- 关键词：a serrated knife · the helmet’s chin
- 为什么这样写：换身体被写成连贯动作里的一个环节：中弹、踉跄、换、抽刀，全挤在第一句里，中间没有停顿。第二句给的是路线：往前、钻进去、抢在第二枪之前、找头盔护不到的地方。刀的落点写得极具体——"just beneath the helmet’s chin"——对方护甲越完整，这一处空隙就越要紧。
- 读者视角提示：换身体发生在她挨枪的那具身体断气之前，两个动作几乎同时。读者看到的是效率：中弹没有让她退，只让她换一个身体继续往前。
- **原文**：原文 L72-L72
- **结论**：引语 2 句 47 词（原文 L72）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 5
- **md**：引语（39 词 2 句）：She turned toward the rear doors, and saw Sydney’s small form, curled on her side at the far end, her back to June. She was strapped to the bench, blindfolded and hands bound, an IV running into her wrist.
- 中文理解：她转向车尾的门，看见西德妮小小的身子蜷在最里头，背对着她。人被绑在长凳上，蒙着眼，双手捆着，手腕里插着输液管。
- 关键词：Sydney’s small form · hands bound
- 为什么这样写：镜头先给纵深——最里头、背对——再一层层收窄：绑在长凳上、蒙眼、手被捆、输液。四个细节全是束缚，最后一项带着医疗气息：她不是被关着，是被处理着。整段没有她的一句话，也没有琼的呼喊。
- 读者视角提示：读者跟着琼的视线往里看，先看到的是一个姿势，不是一张脸；她背对着门，所以脸留到了后面。
- **原文**：原文 L84-L84
- **结论**：引语 2 句 39 词（原文 L84）：中文理解逐句对得上，主语=西德妮、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L49）
- **档**：相符

### 原句 6
- **md**：引语（31 词 2 句）：She was about to tell him when Sydney’s sister sighed, and her eyes drifted open, cloudless and blue. As they did, the dark interior of the transport van blurred around June.
- 中文理解：她正要回答电话那头，那个女孩——句子里第一次把她叫作「西德妮的姐姐」——叹了口气，睁开眼睛，一双没有云的蓝眼睛。就在那一瞬，运输车暗下来的车厢在琼周围糊开了。
- 关键词：Sydney’s sister · blurred around June
- 为什么这样写：第一个分句还挂在上一通电话上，"when" 一转折，注意力就交给那个女孩。她只做了两个动作：叹气、睁眼；随后变化发生在车厢上——暗、糊、失去形状，全部写在琼的视野里，没有一句写女孩做了什么。眼睛的颜色是这一段唯一的外貌描写，也是最后一件还清楚的东西。
- 读者视角提示：读者和琼同时听到「西德妮的姐姐」这个称呼，也同时看见车厢开始化开。到这里，读者手里同时有一个新称呼和一间正在化开的车厢。
- **原文**：原文 L141-L141
- **结论**：引语 2 句 31 词（原文 L141）：中文理解逐句对得上，主语=西德妮、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L56）
- **档**：相符

### 原句 7
- **md**：引语（42 词 2 句）：And this wasn’t just any diner. It was the one back home, and she was sitting in her favorite booth, emptying sachet after sachet into her coffee, waiting to see how many it would take for the spoon to stand up straight.
- 中文理解：这不是随便一家餐馆，是她老家那一家；她坐在自己最喜欢的卡座里，一包接一包往咖啡里倒糖，想看要倒多少包，勺子才能立起来。
- 关键词：any diner · favorite booth
- 为什么这样写：前一句先否掉「随便一家」，第二句把地点钉回「老家」，再用一个具体动作把场景填满：撕糖包、数着倒、等勺子立起来。整段没有一个字写她怎么到这里，也没有一个字提刚才的车厢；全部内容是一个卡座、一杯咖啡和一件孩子气的实验。
- 读者视角提示：读者刚看完车厢里的画面，句子就把人放到卡座上，中间没有过渡词。细节越具体——卡座是「最喜欢的」，糖是一包接一包——读者越容易先认出这是哪儿，再想起问怎么会在这儿。
- **原文**：原文 L165-L165
- **结论**：引语 2 句 42 词（原文 L165）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L63）
- **档**：相符
