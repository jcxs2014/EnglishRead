# 3-diff.md · 《Victorious》第 94 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch94_chapter_xxiv.txt`
- 受审 md：`ch94 the voice on the line.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（recalled Sydney practicing until she needed only incomplete ）
- **原文**：原文 L51：He’d seen Sydney practicing. Seen her go from needing whole bodies to only incomplete remains. Not just trying to improve, he gathered now, but working toward a goal.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L51：原文 L51 的事实「recalled Sydney practicing until she needed on」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（seconds）
- **原文**：原文 L24：He bristled, assuming for a moment she’d hung up on him, but when he checked, the call hadn’t disconnected. The seconds continued ticking upward on the screen.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L24：原文 L24 的事实「seconds」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 2（阻断 0 / 提示 2） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（48 词 2 句）：Victor held up a hand, strained to hear something, anything, beyond the silence on the line. He strained and caught the soft echo of footsteps over metal grating, and a voice murmuring, “Sweet dreams,” followed by the scrape of the phone being lifted before the call abruptly disconnected.
- 中文理解：维克多抬起一只手，越过听筒里的静默去听点什么。他再使了一次劲，才捕到金属格栅上那串脚步的轻响，还有人低声说的一句「Sweet dreams」；接着是手机被拿起来的刮擦声，通话随即断掉。
- 关键词：strained to hear · metal grating
- 为什么这样写：抬手这个动作被单独放在句子最前面，没交代是给谁看的；紧接着才是「听」，而且还要再使一次劲才捕到东西——前一句里，听筒那头只有静默。声音由远及近排过来：先是格栅上的脚步，再是一句道别，最后才是手机被拾起的刮擦。道别那句话夹在中间，说话的人始终没有露面。收尾用 abruptly disconnected 把这条线掐断。
- 读者视角提示：读者听到的只有维克多听到的东西：脚步、一句道别、刮擦声。那头究竟发生了什么，这一段一个字都没给；电话断掉这一下，读者和维克多同时失去线索。
- **原文**：原文 L33-L33
- **结论**：引语 2 句 48 词（原文 L33）：中文理解逐句对得上，主语=维克多、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（38 词 2 句）：And that voice, like Syd’s, but softer, sweeter, more grown-up. A voice he’d never heard with his own ears because he’d stopped them up, so it couldn’t get inside his head, the night he cut its owner’s throat.
- 中文理解：那个声音像西德妮的，却更软、更甜、更像长大以后的人。他从来没有用自己的耳朵听过它——那晚他割断它主人的喉咙时把耳朵堵上了，为的是不让它进到自己脑子里。
- 关键词：like Syd’s · cut its owner’s throat
- 为什么这样写：三个比较级连着来：更软、更甜、更成熟，把「像西德妮」这个判断往细处推，每推一步都离西德妮更远一点。第二句把顺序倒过来：先说他从没亲耳听过，再给原因——他把耳朵堵上了；最后才落到那一晚他做的事。整段的落点是割喉，前面所有柔软的形容都压在这一下上。
- 读者视角提示：读者拿到的是维克多自己的辨认：像，但不一样。他没亲耳听过，因为他堵上了耳朵；读到这一句的末尾，读者才知道他堵耳朵的那晚做了什么。
- **原文**：原文 L42-L42
- **结论**：引语 2 句 38 词（原文 L42）：中文理解逐句对得上，主语=西德妮、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L24）
- **档**：相符

### 原句 3
- **md**：引语（33 词 3 句）：But there was a reason crematoriums had to burn at such high heats. Bones didn’t disintegrate in ordinary fires. Certainly not in hasty ones lit with gasoline in the middle of the night.
- 中文理解：可火葬场要把温度烧到那么高，是有缘故的。骨头不会在普通的火里化掉；夜里临时点起来、浇上汽油的那种火，更不会。
- 关键词：such high heats · ordinary fires
- 为什么这样写：这一段只写火，不写人。三句话一路往下降：从火葬场的高温，到普通的火，再到夜里浇上汽油临时点的火——温度一层比一层低，句子一层比一层短。最后一句用 Certainly not 起头，把「这种火不行」讲成不容商量的判断。全段没有一个人物动作，只有温度、骨头和时间。
- 读者视角提示：读者在这一段里暂时离开车厢，落到一场火的具体条件上：火葬场要烧到多高，普通的火能烧掉什么，夜里浇汽油的火又差在哪里。三句都是常识，没有一句写人。
- **原文**：原文 L48-L48
- **结论**：引语 3 句 33 词（原文 L48）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L30）
- **档**：相符
