# 3-diff.md · 《Victorious》第 72 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch72_chapter_ii.txt`
- 受审 md：`ch72 the blue vial on the desk.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（took the formula back down to studs to find a better solutio）
- **原文**：原文 L222：Dani was still talking. “I’m going to take the formula back down to studs. See if I can find a better solution.” He could hear the excitement in her voice. A bored mind, finally being offered a challenge. “I’ll need to run some tests.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L222：原文 L222 的事实「took the formula back down to studs to find a 」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（saw in Dani a distorted version of himself as he'd been: you）
- **原文**：原文 L63：Now that he was sitting here, across from her, his suspicion turned to certainty. In her, Victor saw a distorted version of himself. Not as he was, but as he’d been. Young and brilliant, ambitious and ignored.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L63：原文 L63 的事实「saw in Dani a distorted version of himself as 」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（had been taking the compound for two and a half years）
- **原文**：原文 L198：She rapped her fingers on the desk. “Half the chemicals in this are highly toxic. And you’ve been taking it for, what, two and a half years? It’s a miracle you haven’t done more damage.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L198：原文 L198 是一处静态状态描写（had been taking the compound for two…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 3（阻断 0 / 提示 3） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（33 词 1 句）：It had been a lifetime, but his body remembered the route between the science buildings, legs carrying him as if to class while his mind was tugged between the present, and the past.
- 中文理解：回到洛克兰让他觉得陌生：明明像过了一辈子，身体却还记得科学楼之间那条路，两条腿自己就往教室的方向走，而脑子被拉到当下与过去之间来回。
- 关键词：body remembered · as if to class
- 为什么这样写：整段只有一句话，用 but 把「过了一辈子」和「身体还记得」并排放着，时间的长短和身体的熟悉互相顶着。后半句拆成两半：legs carrying him 是腿在自己走，his mind was tugged 是脑子被拽着，一个主动一个被动，走路和走神分给了两个部位。
- 读者视角提示：读者跟着他走进校门，先知道的是身体认得这条路、脑子不认得眼下。这一句没有交代他离开多久，只给了 a lifetime 这个说法。
- **原文**：原文 L21-L21
- **结论**：引语 1 句 33 词（原文 L21）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（39 词 3 句）：A shadow danced at the edge of his vision. He knew that if he turned his head, he’d see a blond-haired girl, or a black-furred dog, a cellmate, or a dead best friend. The hallucinations were almost constant now.
- 中文理解：视野边上有个影子在动；他知道只要转头，就会看见一个金发女孩、一条黑毛狗、一个狱友，或者一个死去的好友。这样的幻觉现在几乎不间断。
- 关键词：black-furred dog · almost constant now
- 为什么这样写：看见被写成条件句：if he turned his head, he'd see。影子先在边缘，看清要配上转头这个动作，名单就等在那一步后面。四个人物用 or 串成一列，没有一个是名字，全是「什么样的谁」；最后一句用 almost constant 交代频率，前面那份名单就不再是一次意外。
- 读者视角提示：读者到这一块才知道他一直跟不在场的人同处一室。名单最后一项是「死去的好友」，前三项还能当成校园里撞见的人，这一项不能。
- **原文**：原文 L39-L39
- **结论**：引语 3 句 39 词（原文 L39）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L25）
- **档**：相符

### 原句 3
- **md**：引语（48 词 3 句）：Victor’s mouth quirked. He hadn’t known the details, but he’d noticed the discrepancy between Dani’s potential and her posting, recognized a talent being stifled, squandered. Add to that her past interest in stress-induced hormonal shifts and synthetic cortisol, and he suspected she was the person for the job.
- 中文理解：维克多的嘴角动了一下。他事先并不知道细节，只注意到丹妮的能力和她拿到的职位对不上，认出一个被压住、被浪费掉的人才；再加上她过去对压力引起的激素变化和合成皮质醇有兴趣，他判断她就是能做这件事的人。
- 关键词：talent being stifled · suspected she was
- 为什么这样写：三句话排出一条推理链：先声明不知道细节，再写他注意到什么（潜力与职位之间的落差）、认出什么（被压住的人才），最后把她的旧研究方向加进来，落到 suspected。动词从 noticed 到 recognized 再到 suspected，一步步往里走，却始终停在「猜」上。
- 读者视角提示：读者跟着他做了一遍背景调查：他手上没有档案，只有职位的落差和她过去的研究兴趣。丹妮为什么坐在这个办公室，也从她自己那句调侃换成了他这一侧的观察。
- **原文**：原文 L60-L60
- **结论**：引语 3 句 48 词（原文 L60）：中文理解逐句对得上，主语=维克多、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 4
- **md**：引语（52 词 9 句）：Victor thought of hurting her. To prove the point. He’d timed his visit well. His powers had come online just after she walked in. Now, his nerves were humming, and so were hers. He could force her. Bend her. Break her. Instead, he told the truth. “Have you heard the term EO?”
- 中文理解：维克多想伤她。为了证明这一点。他把这次来访的时机算得很好：她刚走进来，他的能力就上线了。此刻他的神经在嗡鸣，她的也是。他可以强迫她。折断她。摧毁她。可他反而说了实话：「你听说过 EO 这个词吗？」
- 关键词：thought of hurting her · told the truth
- 为什么这样写：前半段用三个短句列举他能做的事（强迫、折断、摧毁），全是动词；后半段只用了一句实话作为回答，而且用的是问句。三个动词同一个词根，读者能听见那扇门在关——而最后一句把它推开。
- 读者视角提示：他本可以用能力拿到任何答案，却选择先亮出这个词。因为他要的是她自己的判断，而不是被撬出来的答案。
- **原文**：原文 L102-L105
- **结论**：引语 9 句 52 词（原文 L102）：中文理解逐句对得上，主语=维克多、受事=线，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L39）
- **档**：相符

### 原句 5
- **md**：引语（45 词 3 句）：He ejected the inhaler cartridge and set the vivid blue vial on the desk. “This is what I’m asking you to make. What I need you to teach me how to make,” he amended. “It’s a serum that, when inhaled, severs me from my abilities.”
- 中文理解：他把药筒退出来，把那管鲜蓝色的药放在桌上，说这就是他要她做的东西——更准确地说，是他要她教他做的东西：一种吸入之后能把他和自己的能力的联系切断的血清。
- 关键词：vivid blue vial · severs me from
- 为什么这样写：先说 make，紧接一个 amended 改成 teach me how to make，「替我代做」变成「教会我做」，两个人的位置也跟着从买主与工匠换成学生与老师。血清的作用只用一句交代：when inhaled, severs me from my abilities；被切断的是他和能力之间的连接，不是能力本身。
- 读者视角提示：本章开头他还捏在指间转的那支吸入器，到这一块变成一件要复制的东西，也变成一份要教的手艺。蓝色的药先落在桌上，话才跟上。
- **原文**：原文 L156-L156
- **结论**：引语 3 句 45 词（原文 L156）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L49）
- **档**：相符

### 原句 6
- **md**：引语（62 词 3 句）：It was a calculated risk, so much transparency. Explaining what happened if he ran out of the compound was the same as pointing to the space between his second and third ribs, showing her exactly where to drive a knife. But in the wake of that dark night, between Eli’s goading and the gun, he realized, he had nothing left to lose.
- 中文理解：把实情讲到这个程度是一次算过的冒险：说出药用完会怎样，等于指着自己第二根和第三根肋骨之间，告诉她刀该往哪里送。但在那个黑夜里，在伊莱的挑动和那把枪之后，他明白自己已经没有可失去的了。
- 关键词：calculated risk · nothing left to lose
- 为什么这样写：先说这是 calculated risk，紧接着把风险换成一个身体坐标：两根肋骨之间，刀进去的位置。抽象的词落地，读者手上多了一个能指的地方。最后一句把时间推回那个黑夜，between Eli's goading and the gun 把两样东西并排放在一起，收在 nothing left to lose 上。
- 读者视角提示：读者在这一块听见他把自己交出去的理由——他自己管这叫「算过的风险」，理由是没有别的可失去的。刀的位置由他自己指出来：第二与第三根肋骨之间，这个动作比任何威胁都具体。
- **原文**：原文 L171-L171
- **结论**：引语 3 句 62 词（原文 L171）：中文理解逐句对得上，主语=伊莱、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L56）
- **档**：相符

### 原句 7
- **md**：引语（27 词 2 句）：“How long until you need another dose?” she asked. “Seven hours.” At first, it had been nearly twelve, but that window, like all of them, was shrinking.
- 中文理解：她问：还要多久你才需要再补一剂？他答：七小时。最初的时候接近十二小时，但那个窗口——和所有窗口一样——正在缩短。
- 关键词：another dose · was shrinking
- 为什么这样写：一问一答两句就把药效的账目摆完：现在七小时，起初近十二小时。一个在缩，一个没缩，这组对比本身就是威胁——他剩下的时间只会更少，不必任何人开口提醒。最后那个 like all of them 把这一次的收缩推广成通例：不止这一剂在缩。
- 读者视角提示：这是全书第一次给出药效的具体数字。它同时是本章的倒计时：他必须在一个窗口不断收窄的时间里，找到一个不靠这管药活下去的办法。
- **原文**：原文 L234-L237
- **结论**：引语 2 句 27 词（原文 L234）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L63）
- **档**：相符

### 原句 8
- **md**：引语（37 词 2 句）：She glanced at a clock on the wall, lips moving as she counted. “Come back tomorrow night at eight.” She was timing it so a dose would wear off while he was there. “I’ll reserve the lab.”
- 中文理解：她瞥了一眼墙上的钟，嘴唇动着在默算。「明天晚上八点再来。」她在算准时间，让一剂药在他到的时候正好失效。「实验室我给你留着。」
- 关键词：lips moving · reserve the lab
- 为什么这样写：她回答之前先默算：lips moving as she counted 把这个决定写成一个算术动作，八点这个数字是被推出来的，不是随口说的。叙事者随后把这层意图点破——她要的是药效正好掉下去的那一刻，也就是他最虚弱的那一刻。最后那句 I’ll reserve the lab 用将来时收尾：实验室已经预留，人却还没到。
- 读者视角提示：这一章的规则在这里被交出来：约的是八点，不是「明天」，是精确到小时的。她把一个未来的自己交出去当试验材料——而实验室那句平常得像在安排会议室。
- **原文**：原文 L240-L240
- **结论**：引语 2 句 37 词（原文 L240）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L73）
- **档**：相符
