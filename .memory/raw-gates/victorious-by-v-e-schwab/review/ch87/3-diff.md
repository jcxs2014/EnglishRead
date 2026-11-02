# 3-diff.md · 《Victorious》第 87 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch87_chapter_xvii.txt`
- 受审 md：`ch87 the violet cartridge works.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（与 Victor 的关系：在 Victor 头痛到看不见时仍安慰他说自己越来越接近了）
- **原文**：原文 L42：“I’m getting closer,” she said, when the headache got so bad he couldn’t see.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L42：原文 L42 的事实「与 Victor 的关系：在 Victor 头痛到看不见时仍安慰他说自己越来越接近了」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（与 Victor 的关系：坚持紫色配方只是原型，在更多测试完成前要他继续用旧配方）
- **原文**：原文 L135：“This is a massive breakthrough, Victor, don’t get me wrong, but this,” she said, holding up the violet vial, “is a prototype, not a finished product, and until I can run more tests, I want you to keep using the old compound. Just to be safe.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L135：原文 L135 的事实「与 Victor 的关系：坚持紫色配方只是原型，在更多测试完成前要他继续用旧配方」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 2（阻断 0 / 提示 2） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（45 词 2 句）：Victor slotted her latest formula into the inhaler as Dani set the timer for five minutes. That was all the time he had these days, between Haverty’s serum wearing off, his powers returning in its wake, and the moment he would start to die again.
- 中文理解：维克多把丹妮最新配的那支装进吸入器，丹妮同时把计时器按到五分钟；这五分钟就是他如今全部的空档——哈弗蒂的血清退掉，能力跟着回来，然后他又开始死，三件事都挤在这段时间里。
- 关键词：her latest formula · serum wearing off
- 为什么这样写：两个动作并排放着，他装药，她按表，中间没有一句对白。紧接的那句把五分钟拆成先后三段：血清退、能力回、人开始死，顺序就是他能试药的窗口；「全部的时间」这个说法，让五分钟同时是机会和倒计时。
- 读者视角提示：读者手里也有一只表。这一段只交代窗口有多窄，不交代吸下去会怎样，后面每读一次秒都压着这个数。
- **原文**：原文 L54-L54
- **结论**：引语 2 句 45 词（原文 L54）：中文理解逐句对得上，主语=维克多、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（33 词 3 句）：There was no sudden change, no cataclysmic shift, but he noticed a quiet humming just beneath his skin. Not unpleasant. More like the mismatch between a power source and the device it’s charging.
- 中文理解：没有突变，也没有天翻地覆那种变化，他只是觉出皮肤底下有一阵很轻的嗡响；不难受，更像电源和它正在充的那台设备对不上。
- 关键词：cataclysmic shift · quiet humming
- 为什么这样写：先把读者等的两种动静都否掉，再给一个几乎要贴着皮肤才听得见的信号。接着拿电源与设备不匹配来解释它，起效被写成仪器层面的不合，而不是身体上的痛快。
- 读者视角提示：这里没有结论，只有一个要静下来才感觉得到的动静；结果还在计时器那头，读者只能先停在这个几乎听不见的信号上。
- **原文**：原文 L66-L66
- **结论**：引语 3 句 33 词（原文 L66）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L29）
- **档**：相符

### 原句 3
- **md**：引语（34 词 2 句）：He flexed, his powers still online, turned the dials down and up while he waited for the timer on the table to run out. The minutes wound to seconds, and then, the clock chimed.
- 中文理解：他活动了一下，能力还在线上；等桌上那只计时器走完的工夫，他把旋钮往下拨、再往上拨。分钟一点点收到只剩秒，然后表响了。
- 关键词：turned the dials · the clock chimed
- 为什么这样写：这一段只干两件事，手上试旋钮，眼睛盯着表。所有判断都押给那只表，响之前不下结论，响之后才轮到身体表态；「分钟收成秒」把等待写成可数的东西。
- 读者视角提示：注意力被按在计时器上。表响的这一刻，读者得到的不是一个结果，而是一个可以往下读的许可。
- **原文**：原文 L78-L78
- **结论**：引语 2 句 34 词（原文 L78）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=线，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L36）
- **档**：相符

### 原句 4
- **md**：引语（52 词 3 句）：Just then, someone swiped into the lab. A young man came barging in, head bowed over his phone. Before he could look up, Victor reached out, not with his hand, but his power, took hold of the intruder’s nerves, and snapped the dial up, hard and fast enough to blow the circuitry.
- 中文理解：就在这时有人刷卡进了实验室，一个年轻人低着头看手机撞进来；他还没抬头，维克多已经伸手——不是用手，是用能力：捏住这人的神经，把旋钮猛地拧上去，快得足够烧掉线路。
- 关键词：barging in · snapped the dial up
- 为什么这样写：入场写得日常到不能再日常，刷卡、低头、看手机。紧接着一句否定把动作的性质翻过来，不是手，是能力；再往后三个动词连着落，捏住神经、拧旋钮、烧线路。用的还是他在计时器前拨过的那只旋钮。
- 读者视角提示：这一下是给读者的证明，能力不只是回来了，还能随手把一个人放倒；被放倒的人连脸都没露全，读者只看见他低头的那一瞬。
- **原文**：原文 L117-L117
- **结论**：引语 3 句 52 词（原文 L117）：中文理解逐句对得上，主语=维克多、受事=线，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L43）
- **档**：相符

### 原句 5
- **md**：引语（41 词 2 句）：Dani checked the TA’s pulse. “My guess is anywhere from eight to twelve hours, since I modeled it on the original.” She straightened. “But I don’t exactly have a wealth of data to go on, so, I suggest you take notes.”
- 中文理解：丹妮摸了一下那个技术员助理的脉搏。「我猜是八到十二小时，因为我参照原型做的。」她直起身。「不过我手头数据不多，所以，我建议你做笔记。」
- 关键词：eight to twelve hours · take notes
- 为什么这样写：数字用「我猜」领起，后面立刻补上原因（参照原型做的），再补一句自我限定（数据不多）。三步把一个估计值包成了一份可记录的东西。
- 读者视角提示：八到十二小时这个数字，是这一章里唯一可被计划使用的东西——包括他自己能在这个窗口里做多少事。
- **原文**：原文 L129-L129
- **结论**：引语 2 句 41 词（原文 L129）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L50）
- **档**：相符

### 原句 6
- **md**：引语（35 词 2 句）：As Victor accepted the old cartridge, the scientific side of his mind applauded her due diligence. But the rest of him—the part that had spent nearly a decade either powerless or dying—wasn’t interested in safe.
- 中文理解：接过旧药管的时候，他脑子里讲科学的那一半是在给她这份谨慎叫好的；可另一半——那将近十年不是在没力量就是在等死的部分——对「安全」不感兴趣。
- 关键词：due diligence · interested in safe
- 为什么这样写：一句把人劈成两半，一半认账，一半不认。破折号里那串年头一摆出来，谨慎这个建议就自己失重了；「不感兴趣」比「拒绝」轻，落点却更硬。
- 读者视角提示：结尾没写他要做什么，只写了他不打算做什么。读者拿到的是两个并排的事实：旧药管进了他的手，他的另一半已经不在「安全」这一边。
- **原文**：原文 L138-L138
- **结论**：引语 2 句 35 词（原文 L138）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L60）
- **档**：相符
