# 3-diff.md · 《Victorious》第 112 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch112_chapter_ii.txt`
- 受审 md：`ch112 mitch leaves the dream cabin.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（shoved Mitch forward through the open doors, saying “Bottoms）
- **原文**：原文 L48：“Bottoms up,” said June, shoving him forward, through the open doors.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L48：原文 L48 的事实「shoved Mitch forward through the open doors, s」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（42 词 3 句）：“Hard to explain,” she said, loading a gun, and handing it to Mitch. He hated weapons, the lifeless weight of them, how easily they ended things. But he also knew he would use it in a heartbeat, if it meant saving Syd.
- 中文理解：她说这事儿不好解释，一边给枪装弹，一边把枪递给米奇。米奇讨厌武器，讨厌它们那种没有生命的重量，讨厌它们了结事情有多容易。但他也知道，只要是为了救西德妮，他会立刻用它。
- 关键词：loading a gun · saving Syd
- 为什么这样写：回答只有三个词，`Hard to explain`，先说难讲，再往下接动作。递枪不单独成句，而是挂在 `she said` 后面，`loading a gun` 与 `handing it to Mitch` 用 and 串在同一句里，装弹和递枪是一口气做完的。第二句写米奇的排斥，三个并列成分都落在 `weapons` 上：`the lifeless weight of them`、`how easily they ended things`。第三句用 `But` 转过来，条件压在句尾，`if it meant saving Syd`。
- 读者视角提示：读者先拿到一句「不好解释」，紧接着看见的不是解释，是一把正在装弹的枪被塞到米奇手里。第二句才进到米奇的想法，第三句把排斥与接受并排放在一句里，谁也没压过谁。
- **原文**：原文 L24-L24
- **结论**：引语 3 句 42 词（原文 L24）：中文理解逐句对得上，主语=西德妮、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（31 词 2 句）：As Mitch crossed the threshold, he braced for the world to drop away, for the surreal sensation of falling out of waking, into dream. But his boot landed on the floor.
- 中文理解：米奇跨过门槛的时候，已经做好了世界塌下去的准备，准备迎接那种从清醒里掉出去、掉进梦里的怪异感觉。可他的靴子落在了地板上。
- 关键词：crossed the threshold · boot landed
- 为什么这样写：第一句把期待写满，`braced for` 后面挂两个 for 短语，第二个比第一个长，从 `the world to drop away` 一路写到 `falling out of waking, into dream`，一层比一层低。第二句只有六个词，以 `But` 开头，主语是 `his boot`，动词是 `landed`，落点是 `on the floor`。上一句铺的坠落感，被这一句的一只靴子踩住。
- 读者视角提示：读者跟着他做准备，等着地面消失；等来的是鞋底碰到地板。落差是用两个动作对出来的：`drop away` 之后没有下坠，只有 `landed on the floor`。
- **原文**：原文 L51-L51
- **结论**：引语 2 句 31 词（原文 L51）：中文理解逐句对得上，主语=米奇、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L24）
- **档**：相符

### 原句 3
- **md**：引语（39 词 3 句）：The sun was just starting to go down over the trees. He turned to look back at the cabin, windows glowing warmly. From here, he could see Syd, sitting at the kitchen table, her head bent over a book.
- 中文理解：太阳正要落到树林后面去。他回头望那间木屋，窗子暖融融地亮着。从这里他能看见西德妮，她坐在厨房桌边，低着头看书。
- 关键词：windows glowing warmly · head bent
- 为什么这样写：三句都是看，视点一步步收近：先是他眼前的太阳，`just starting to go down over the trees`；再是他回头，`look back at the cabin`；最后落到屋里的人，`From here, he could see Syd`。第三句在 Syd 后面挂两个短语，`sitting at the kitchen table` 与 `her head bent over a book`，人没有动作，只有一个姿势。这一段里没有出现「梦」字。
- 读者视角提示：读者顺着他的视线走：太阳、木屋的窗、屋里的西德妮。第三句先写距离，`From here`，人被看见，没有被叫到；整段没有一句对话，也没有一点声音。
- **原文**：原文 L69-L69
- **结论**：引语 3 句 39 词（原文 L69）：中文理解逐句对得上，主语=西德妮、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L30）
- **档**：相符

### 原句 4
- **md**：引语（34 词 2 句）：He turned back to the woodpile and brought the axe down a second time. Or at least, that’s what he meant to do, but as his fingers tightened, the axe let out a BANG.
- 中文理解：他转回柴堆，第二次把斧头砍下去。至少他是打算这么做的，可就在手指收紧的时候，斧头发出一声「砰」。
- 关键词：fingers tightened · let out a BANG
- 为什么这样写：第一句是干净的动作句，三个动作连着：`turned back`、`brought ... down`、`a second time`。第二句马上把这个动作撤掉，`Or at least, that’s what he meant to do` 先说这只是打算；`but` 之后是手指收紧，接着声音自己出来了，`the axe let out a BANG`，BANG 全大写，压在句尾。
- 读者视角提示：读者先读到一次已经做完的劈柴，再被告知那只是打算。声音不是谁听见的，是斧头自己发出来的；全大写的 BANG 让响声先落在纸上，落点写的是声音。
- **原文**：原文 L81-L81
- **结论**：引语 2 句 34 词（原文 L81）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L36）
- **档**：相符

### 原句 5
- **md**：引语（31 词 2 句）：Mitch recoiled, the sound so close and loud it was painful, and for an instant, the whole world cracked, and he saw white walls, metal doors, a gun. There and gone.
- 中文理解：米奇往后一缩，那声音又近又响，响得发疼；有那么一瞬间，整个世界裂开了，他看见白墙、金属门、一把枪。来了又没了。
- 关键词：the whole world cracked · white walls
- 为什么这样写：一句里排了四件事：他缩回去、声音、世界裂开、他看见了什么，中间用 and 串起来，`for an instant` 卡在裂开之前，把这一瞬框住。看见的东西并列成三个名词短语，`white walls, metal doors, a gun`。第二句只有三个词，两个短句，`There and gone.`，一个名词加一个过去分词，把刚才那一瞬收掉。
- 读者视角提示：读者被按在声音里：先缩、再疼、再看见世界裂开一道缝，缝里是三样实物，缝随即合上。第二句只有三个词，张开和合上之间没有留下别的字。
- **原文**：原文 L84-L84
- **结论**：引语 2 句 31 词（原文 L84）：中文理解逐句对得上，主语=米奇、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符
