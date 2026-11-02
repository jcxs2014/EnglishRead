# 3-diff.md · 《Victorious》第 24 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch24_chapter_v.txt`
- 受审 md：`ch24 the first eo with a badge.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L3 · R1 事实未进 md（disappeared when Stell prompted him to lower himself into a ）
- **原文**：原文 L159：“A fellow soldier,” the director had said with a weighted look. Then, at his prompting, Noah had lowered himself into a chair, and proceeded to disappear.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L159：原文 L159 的事实「disappeared when Stell prompted him to lower h」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（is one of the two EO field agents among EON's thirty-three a）
- **原文**：原文 L99：And of those thirty-three field agents, thirty-one were ordinary humans, and the other two were EOs.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L99：原文 L99 是一处静态状态描写（is one of the two EO field agents am…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

### L5 · R1 事实未进 md（is the other EO hiding in plain sight, an ally and an anchor）
- **原文**：原文 L219：It was enough to know she was no longer the only one hiding in plain sight.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L219：原文 L219 是一处静态状态描写（is the other EO hiding in plain sigh…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

### L6 · R1 事实未进 md（needed an hour of supplemental oxygen and two aspirin after ）
- **原文**：原文 L24：Apparently, there had been an incident with the EO in cell 008. A young man with the ability to alter the pressure of the air around him. Until that point, the guards had assumed he could only amplify it, increasing the outward force. But apparently, he could create a vacuum, too. And his cell wasn’
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L24：原文 L24 是回忆/前史交代（needed），md 未复述不影响本章线索理解；本条属背景交代，判提示不修
- **档**：提示

### L9 · R1 事实未进 md（number eighty, of whom forty-seven are guards at the compoun）
- **原文**：原文 L96：Of the eighty soldiers who now worked for EON, forty-seven were guards stationed at the compound, and thirty-three were agents in the field.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L96：原文 L96 的事实「number eighty, of whom forty-seven are guards 」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L10 · R1 事实未进 md（number two, Rios and Noah）
- **原文**：原文 L99：And of those thirty-three field agents, thirty-one were ordinary humans, and the other two were EOs.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L99：原文 L99 的事实「number two, Rios and Noah」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 6（阻断 0 / 提示 6） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（43 词 3 句）：Apparently, there had been an incident with the EO in cell 008. A young man with the ability to alter the pressure of the air around him. Until that point, the guards had assumed he could only amplify it, increasing the outward force.
- 中文理解：据说 008 号牢房出过一次事故。里面是个能改变周身空气压力的年轻人。在那之前，看守们一直以为他只会往外加压。
- 关键词：cell 008 · alter the pressure
- 为什么这样写：Apparently 先给这条消息定了来源——不是叙述者亲见的，是通报。三句话的顺序是房号、人、误判：能力一句就交代完了，真正危险的是看守们先前的假设。until that point 把这件事压在一个时间点上，能力没有变，变的是他们终于知道了边界在哪。
- 读者视角提示：这段只讲前提，不讲后果；读者要自己把「不密封的牢房」和「一群人开始发晕发笑」连起来。
- **原文**：原文 L24-L24
- **结论**：引语 3 句 43 词（原文 L24）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=牢房，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（46 词 3 句）：But this latest one, which had been so promising, turned out to be worse than a dead end. It was a setup, the whole place rigged to blow the moment they went in. Which was, if nothing else, irrevocable proof that Vale was not a ghost.
- 中文理解：可最近这条线索本来很有希望，结果比白跑一趟还糟：那地方是个圈套，他们一进去就会炸。要说有什么用，它彻底证明了维克多不是鬼。
- 关键词：rigged to blow · not a ghost
- 为什么这样写：worse than a dead end 先把结果定级，再解释为什么更糟——不是没抓到，而是被对方算准了他们一定会来。rigged to blow the moment they went in 把时间卡在进门那一刻，泄露出对方熟悉他们的行动节奏。最后一句把失败换算成情报：死胡同给不出结论，陷阱能给出一个。
- 读者视角提示：if nothing else 是自嘲的口气，但这句其实是本章对维克多唯一的判断——他在，而且他在逗他们。
- **原文**：原文 L39-L39
- **结论**：引语 3 句 46 词（原文 L39）：中文理解逐句对得上，主语=维克多、受事=线，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（34 词 3 句）：She was the first EO to ever be offered a badge instead of a cell. Or at least, the first to accept. Stell had believed that not every ExtraOrdinary deserved to be locked up.
- 中文理解：她是第一个被递上警徽而不是牢房的 EO——至少是第一个肯接的。斯特尔相信，不是每个非常人都活该被关起来。
- 关键词：badge instead of a cell · Stell
- 为什么这样写：第一句是纪录式的断言，第二句立刻自己打折（Or at least, the first to accept），这份谨慎让整段可信。接着把功劳推给斯特尔，动词用 believed 而不是 ordered：这套做法当时只是一个人的信念，还没有变成制度。
- 读者视角提示：the first to accept 这半句只说她是第一个肯接的人，没有交代在她之前有没有别人收到过同样的条件——留下一个没写满的空格。
- **原文**：原文 L60-L60
- **结论**：引语 3 句 34 词（原文 L60）：中文理解逐句对得上，主语=斯特尔、受事=牢房，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 4
- **md**：引语（32 词 2 句）：One moment he was there and the next, he wasn’t. But when Stell reached out to touch the place where he had been, should be, his hand came down on something solid.
- 中文理解：前一刻他还在那儿，下一刻就不见了。可斯特尔伸手去摸他原本在、本该在的那个位置，手落下去，碰到的是实体。
- 关键词：reached out to touch · something solid
- 为什么这样写：这段把「消失」拆成两路信息：先写眼睛看到的（不在了），再写手摸到的（还在）。where he had been, should be 叠了两个时态，等于把「他该在」这句判断也写进叙述里；而 something solid 一落，隐身就降级成伪装。
- 读者视角提示：全段没有一个字解释能力如何运作，读者和那只伸出去的手同时拿到答案：看得见和存在是两件事。
- **原文**：原文 L165-L165
- **结论**：引语 2 句 32 词（原文 L165）：中文理解逐句对得上，主语=斯特尔、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L52）
- **档**：相符

### 原句 5
- **md**：引语（44 词 3 句）：Rios knew an EO’s power was tied somehow to their near-death. She could move through solid surfaces after nearly being crushed beneath the rubble of a house when it was bombed, her last moments consumed by the desperate urge to escape. To be free.
- 中文理解：里奥斯知道，EO 的能力多少都和他们的濒死有关。她自己能穿过实体表面，是因为房子被炸时她差点被压在废墟底下——最后那几秒只剩下一个念头：逃出去。要自由。
- 关键词：near-death · move through solid surfaces
- 为什么这样写：somehow 是这句最诚实的地方：她只知道有关联，不知道机制。接着拿自己的经历当唯一证据，动词全落在身体上（crushed、move through），最后把能力还原成一个愿望——urge to escape，而不是一件武器。To be free 单独成句，短得像一次呼吸。
- 读者视角提示：这句替全章定了一个坐标：在这个机构里，能力不是本事，是一次没死成的经历留下的形状。
- **原文**：原文 L180-L180
- **结论**：引语 3 句 44 词（原文 L180）：中文理解逐句对得上，主语=里奥斯、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L62）
- **档**：相符

### 原句 6
- **md**：引语（38 词 1 句）：They both laughed, and Rios felt the pressure easing in her chest as she stepped through the security checkpoint, the doors of EON breaking like a seal, allowing her to do the one thing the other EOs couldn’t.
- 中文理解：两个人都笑了；她穿过安检口时，胸口那股压力松开了——EON 的门像封条一样被撕开，让她能去做别的 EO 做不到的那件事。
- 关键词：security checkpoint · breaking like a seal
- 为什么这样写：笑声和松一口气写在同一句里，先给声音，再给身体。breaking like a seal 把机构写成一层封住人的膜：她不是被放出去，是封条开了。最后半句把整章的特权与孤独压在一处——同一扇门，对别的 EO 是关着的，对她是开的。
- 读者视角提示：注意 breaking 的主语是门，不是她：放行是机构做的动作，她只是被允许。
- **原文**：原文 L312-L312
- **结论**：引语 1 句 38 词（原文 L312）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L72）
- **档**：相符
