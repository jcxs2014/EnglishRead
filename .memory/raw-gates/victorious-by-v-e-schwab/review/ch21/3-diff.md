# 3-diff.md · 《Victorious》第 21 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch21_chapter_ii.txt`
- 受审 md：`ch21 mitch hears of a visitor.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（Cracked his knuckles and checked his watch, making a final a）
- **原文**：原文 L25：He cracked his knuckles, and checked his watch, was about to make a final attempt when he caught sight of Jenny coming toward the booth.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L25：原文 L25 是外观/随身物品描写（Cracked his knuckles and checked his…），无情节转折；判提示不修
- **档**：提示

### L2 · R1 事实未进 md（Told Mitch that a guy came into the diner a few days back lo）
- **原文**：原文 L40：“Suit yourself!” Jenny started to turn, then caught herself. “Oh, hey. I almost forgot. A guy came in a few days back, looking for you.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L40：原文 L40 的事实「Told Mitch that a guy came into the diner a fe」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（Knew where Mitch lived, which made Jenny assume he was a fri）
- **原文**：原文 L55：Jenny shrugged. “I figured he was a friend, given that he knew where you lived.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L55：原文 L55 的事实「Knew where Mitch lived, which made Jenny assum」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L5 · R1 事实未进 md（came into the diner a few days back）
- **原文**：原文 L40：“Suit yourself!” Jenny started to turn, then caught herself. “Oh, hey. I almost forgot. A guy came in a few days back, looking for you.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L40：原文 L40 的事实「came into the diner a few days back」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L6 · R1 事实未进 md（was about to make a final attempt at the code）
- **原文**：原文 L25：He cracked his knuckles, and checked his watch, was about to make a final attempt when he caught sight of Jenny coming toward the booth.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L25：原文 L25 是一处静态状态描写（was about to make a final attempt at…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 5（阻断 0 / 提示 5） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（32 词 1 句）：MITCH was at it again, a plate of pie crumbs—apple this time—at his elbow and the laptop filled by the black coding window, the same two words glowing white on the screen.
- 中文理解：米奇又来了。手肘边搁着一盘吃剩的派渣——这次是苹果派——笔记本上是那个黑色的代码窗口，同样两个字发着白光。
- 关键词：at it again · glowing white
- 为什么这样写：开篇不写他敲了什么，也不写那两个词是哪两个，只把三样东西摆在同一张桌上：派渣、笔记本、屏幕上的白光。at it again 说明这不是第一回，读者进来时事情已经进行到第若干次；the same two words 把「读者该认得」当成前提，句子因此省掉了解释。派是苹果派、派已经吃空——这类琐碎信息把场面钉在一个具体的下午，重复的信号堆得越密，这个人被卡住的时间就越长。
- 读者视角提示：数一下这句里的重复信号：again、the same、this time。三个词说的是同一天又过了一遍，而屏幕上那两个字一次也没变。
- **原文**：原文 L19-L19
- **结论**：引语 1 句 32 词（原文 L19）：中文理解逐句对得上，主语=米奇、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（33 词 2 句）：“No idea,” she said. “I told him I didn’t know when you’d be in, but he didn’t seem to mind. Said he’d just swing by your place, next time he was passing through.”
- 中文理解：她说她也不知道，她只告诉那人不知道米奇什么时候会在店里，可那人好像并不在意。他说下次路过，就直接去他住的地方。
- 关键词：didn’t seem to mind · swing by
- 为什么这样写：整段威胁由一个不知情的人转述，语气轻到几乎没有起伏：No idea、didn’t seem to mind，两个否定都在形容对方不在乎。重量落在最后半句——next time he was passing through，一个没被任何人邀请的人，已经知道该往哪儿走。珍妮说得越随意，这句话越像宣判，因为她的口气证明：在她看来这件事完全正常，没有任何需要压低声音的地方。整段话里他没有回一句。
- 读者视角提示：注意 she said 之后一句形容她神情的词都没有。传话的人不紧张，紧张就全部交给听的人去承担。
- **原文**：原文 L46-L46
- **结论**：引语 2 句 33 词（原文 L46）：中文理解逐句对得上，主语=米奇、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（56 词 1 句）：But as his hand drew the cash from his wallet, as his legs shifted him out of the booth, as he tipped his head to Jenny and wished her a good day, his mind was in a full-out sprint, racing to the truck, pealing down the road toward the cabin at the edge of the woods.
- 中文理解：可就在他的手从钱包里抽出现金、他的腿把他挪出卡座、他偏头向珍妮道一声日安的同一串动作里，他的脑子已经在全速冲刺——冲向卡车，一路呼啸着下了公路，奔向林子边的那间木屋。
- 关键词：full-out sprint · pealing down the road
- 为什么这样写：一句话里三个 as 从句排开，全是身体在做的事：掏钱、离座、点头道别，每一件都正常得像任何一个吃完派要走的客人。主句一直压到最后才出现——his mind was in a full-out sprint。身体慢、脑子快，这层时差是靠三个从句的长度撑出来的：读者跟着他把动作做完，才被告知他的注意力早就不在这里。收尾的 racing 与 pealing 都是速度词，可路上什么也没写，没有人也没有车，只有一个方向，the cabin at the edge of the woods。
- 读者视角提示：别被 but 骗过去——它连的不是两个场景，是两套速度。真正被写出来的是他维持正常所花的力气。
- **原文**：原文 L67-L67
- **结论**：引语 1 句 56 词（原文 L67）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符
