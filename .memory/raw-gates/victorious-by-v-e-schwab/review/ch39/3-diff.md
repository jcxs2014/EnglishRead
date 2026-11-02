# 3-diff.md · 《Victorious》第 39 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch39_chapter_ix.txt`
- 受审 md：`ch39 gabriel killed noah.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（Reports that Agent Rios’s location is known but that Rios is）
- **原文**：原文 L160：Helena cleared her throat. “We have Agent Rios’s location,” she said. “But she’s not answering.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L160：原文 L160 的事实「Reports that Agent Rios’s location is known bu」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（43 词 4 句）：One moment he’d been sitting in the chair across from Dr. Gray, and the next, well, he was still sitting in the chair across from the doctor, but something felt different. Time had gone missing. Seconds, or minutes, or hours, he wasn’t sure.
- 中文理解：上一刻他还坐在格雷医生对面的椅子上；下一刻他仍在同一把椅子上，可有什么不一样了。时间少了一截——是几秒、几分钟还是几小时，他说不准。
- 关键词：Time had gone missing · wasn’t sure
- 为什么这样写：开头两个画面几乎一样：同一把椅子、同一个医生，中间只隔一个 the next，还塞进一个 well，像说话的人自己也在找词。到第三句才把「少了什么」点了名：Time had gone missing；第四句又把答案收回去，几秒、几分钟、几小时，他都不知道。读者被留在同一个空白里。
- 读者视角提示：他的姿势没变，变的是他记得的东西。读者拿到的时钟和他的一样，是断的。
- **原文**：原文 L22-L22
- **结论**：引语 4 句 43 词（原文 L22）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（36 词 3 句）：The day he joined EON, Director Stell warned him to use his ability only when on a mission with his team and even then, only when necessary. He trained him to be cautious. To be careful.
- 中文理解：加入 EON 的那一天，斯特尔主任就警告过他：只有在和队友一起出任务时才能使用能力，即便如此，也只在必要的时候。他训练他要谨慎，要小心。
- 关键词：Director Stell · To be careful
- 为什么这样写：整段是过去时的嘱咐，三层收窄：只有在队里、只在必要、还要谨慎小心。每一次限定都在缩小能力的使用空间。最后两个短句 To be cautious. To be careful. 单独成句，像反复叮嘱。
- 读者视角提示：斯特尔给诺亚立下的规矩，本章却由加百列一句「让我看看你的能力」就打破了。两套规矩第一次正面对撞。
- **原文**：原文 L49-L49
- **结论**：引语 3 句 36 词（原文 L49）：中文理解逐句对得上，主语=斯特尔、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（52 词 9 句）：When I resurrect someone, I gain control over them. Humans return as little more than puppets. But the EOs have proven more resistant. You’re the first one who’s come through it. You see, Noah. You are the evidence I needed. The proof it could be done. So thank you. For trusting me.
- 中文理解：他说，自己复活一个人，就能控制那个人。人回来之后差不多只是傀儡；EO 被证明更抗拒。诺亚是第一个挺过来的。他说，诺亚就是他要的证据，证明这件事做得到；最后一句是谢谢他信任自己。
- 关键词：gain control over them · more resistant
- 为什么这样写：规则被拆成一句一条：先给能力（gain control over them），再给人的结果（little more than puppets），再给 EO 的例外（more resistant），最后才落到 the first one who’s come through it。收尾不是命令，是 thank you；For trusting me 单独断开，道谢和信任被放进同一口气里。
- 读者视角提示：他说的每一条都落在自己身上——控制、傀儡、更抗拒，最后落在 the first one who’s come through it 和一句道谢上。读者拿到的是一条明说的规则，不是猜的。
- **原文**：原文 L100-L100
- **结论**：引语 9 句 52 词（原文 L100）：中文理解逐句对得上，主语=诺亚、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 4
- **md**：引语（39 词 4 句）：For the first time Noah felt himself resist. He brought the tip of the blade to the doctor’s palm, but he didn’t press down. His mind warned him not to do it. His hand clenched around the grip, unwilling.
- 中文理解：这是诺亚第一次感到自己在抗拒。他把刀尖送到博士掌心，却没有按下去。脑子里有个声音叫他别做；他的手攥紧刀柄，不肯动。
- 关键词：felt himself resist · didn’t press down
- 为什么这样写：resist 前面带着 felt himself，这一下是他自己觉出来的，不是旁人看出来的。接下来三句只写「没做」：刀尖送到了、没按下去、手攥住刀柄不肯。全段不给理由，停顿本身就占满这一段。
- 读者视角提示：他第一次感到自己在抗拒，抗拒落在手上：刀尖送到了位，按下去的力气没有。读者看见的是一处停顿，理由不在这一段里。
- **原文**：原文 L145-L145
- **结论**：引语 4 句 39 词（原文 L145）：中文理解逐句对得上，主语=诺亚、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L52）
- **档**：相符
