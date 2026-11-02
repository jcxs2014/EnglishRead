# 3-diff.md · 《Victorious》第 125 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch125_chapter_xv.txt`
- 受审 md：`ch125 sydney digs the grave open.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（骗了她、离开她并伤了 Syd 的心）
- **原文**：原文 L66：Victor, who lied, and left, and broke Syd’s heart.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L66：原文 L66 的事实「骗了她、离开她并伤了 Syd 的心」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（51 词 3 句）：SYDNEY hoisted the shovels on her shoulder as she wove between the old, half-sunken graves. She knew where she was going, even after eight years. Eight years—that’s how long it had been, since the night they dug Victor up the first time, and now they were here to put him back.
- 中文理解：西德妮把几把铁锹抬到肩上，从那些老旧、半边陷进土里的坟之间穿过去。八年过去，她仍知道该往哪儿走。八年——从他们第一次把维克多从土里挖出来的那一夜算起，就是这么长；而这一夜他们来，是要把他放回去。
- 关键词：half-sunken graves · put him back
- 为什么这样写：第一句把两个动作并起来：`hoisted` 是把铁锹抬上肩，`wove` 是在坟之间绕行，两件事落在同一个人身上。第二句只给一句判断 `She knew where she was going`，后面缀上 `even after eight years`。第三句从 `Eight years—` 重新起头，把那个数字再说一遍，然后把两件事并排放：`dug Victor up the first time` 与 `put him back`。
- 读者视角提示：`that’s how long it had been` 里的 `that` 指的就是八年前那一夜。`the first time` 与 `now` 对着看：同一座坟，同一批人，一次挖出来，一次放回去。`shovels` 是复数，几把锹一起压在一个人肩上。
- **原文**：原文 L21-L27
- **结论**：引语 3 句 51 词（原文 L21）：中文理解逐句对得上，主语=维克多、受事=肩，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（37 词 2 句）：Mitch walked in her wake—two of him, in fact, sharing the weight—Victor’s body wrapped in his black coat. Dol drifted, listlessly, behind them, nose to the ground like he was trying to catch a scent but couldn’t.
- 中文理解：米奇跟在她走过的路上——实际是两个他，一起分担那份重量——维克多的遗体裹在他的黑外套里。Dol 无精打采地跟在后头，鼻子贴着地面，像要闻出什么气味却闻不到。
- 关键词：sharing the weight · catch a scent
- 为什么这样写：第一句中间插进两个破折号，把 `two of him, in fact, sharing the weight` 夹在 `walked in her wake` 与 `Victor’s body` 之间：先写跟随，再补一句分身，最后才落到被抬的东西上，补语是 `wrapped in his black coat`。第二句主语换成 `Dol`，三个逗号一路往下压：`drifted, listlessly, behind them`，收在 `nose to the ground` 与 `catch a scent but couldn’t`。
- 读者视角提示：`his` 在 `Victor’s body wrapped in his black coat` 里紧跟 `wrapped`，外套是谁的，这一句没有点名。`two of him` 被破折号点明是分身，那份重量由两个身体分担。Dol 的 `couldn’t` 后面没有宾语，闻不到的东西没有名字。
- **原文**：原文 L30-L30
- **结论**：引语 2 句 37 词（原文 L30）：中文理解逐句对得上，主语=维克多、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L24）
- **档**：相符

### 原句 3
- **md**：引语（39 词 3 句）：They worked together, one of her and four of him, making their way down to the empty wooden box. Each scoop of earth she moved dislodged a memory. Victor, standing on the side of the road in the rain.
- 中文理解：他们一起动手，她一个、他四个，一路挖到那只空木箱。她每铲起一铲土，就翻出一件旧事——维克多站在雨里的路边。
- 关键词：empty wooden box · dislodged a memory
- 为什么这样写：第一句把人数并排摆出 `one of her and four of him`，动作是 `worked together`，落点在 `the empty wooden box`，那只箱子是空的。第二句靠一个动词 `dislodged` 带出两层结果：土被铲走，记忆被翻起。第三句只有 `Victor,` 加一个分词短语 `standing on the side of the road in the rain`，没有主句谓语，是一行清单的开头。
- 读者视角提示：`down to` 标出方向朝下，挖的是坟底。`the empty wooden box` 前面用定冠词 `the`，要挖到的东西是已知的那一只。第三句的雨接在这一夜挖坟的土后面，中间没有过渡句，靠 `dislodged a memory` 那一句挂上去。
- **原文**：原文 L51-L54
- **结论**：引语 3 句 39 词（原文 L51）：中文理解逐句对得上，主语=维克多、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L30）
- **档**：相符

### 原句 4
- **md**：引语（37 词 2 句）：Syd stayed where she was, knuckles white on the shovel, because she didn’t trust her hands. Because, even now, she wanted to climb down into the grave, place her palms on Victor’s chest, and drag him back.
- 中文理解：西德妮留在原来的位置没有动，指节在铁锹上攥得发白，因为她信不过自己的手。因为即便到了这个时候，她还想爬进坟里，把两只手掌按在维克多的胸口，把他拽回来。
- 关键词：knuckles white · drag him back
- 为什么这样写：第一句先定位置 `stayed where she was`，再给一个身体细节 `knuckles white on the shovel`，理由用 `because` 接在后头：`she didn’t trust her hands`。第二句又用一个 `Because` 开头，把理由再压深一层，落到三个动作上：`climb down`、`place`、`drag him back`。
- 读者视角提示：两句各带一个 `Because`，第二个接的是第一句没有说完的那层理由。`her hands` 与 `palms` 是同一双手：一双手按在铁锹上，另一双手想按的是维克多的胸口。`climb down into the grave` 是她想做的事，这一块里只有 `wanted to`。
- **原文**：原文 L84-L84
- **结论**：引语 2 句 37 词（原文 L84）：中文理解逐句对得上，主语=维克多、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L36）
- **档**：相符
