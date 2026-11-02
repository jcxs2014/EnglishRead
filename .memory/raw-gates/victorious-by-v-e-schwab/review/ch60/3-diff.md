# 3-diff.md · 《Victorious》第 60 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch60_chapter_ix.txt`
- 受审 md：`ch60 we have a problem.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（said not every shot is lethal and that he could have slowed ）
- **原文**：原文 L123：Eli blew out a breath. It was true, the sight of Sydney had been provoking. But Gabriel’s orders had been clear—he couldn’t kill her. At least, not yet. “Not every shot is lethal. I could have slowed her down.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L123：原文 L123 的事实「said not every shot is lethal and that he coul」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（reported over the ear comms that Turner was secured and that）
- **原文**：原文 L114：“Turner secured,” said Noah. “In pursuit of Clarke.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L114：原文 L114 的事实「reported over the ear comms that Turner was se」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（was ordered not to make any attempt at escape and to do no v）
- **原文**：原文 L207：Of course, there had been caveats. Several orders, the first of which was not to kill Sydney. The second was to make no attempt at escape. The third, to do no violence against EON.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L207：原文 L207 是回忆/前史交代（was），md 未复述不影响本章线索理解；本条属背景交代，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 3（阻断 0 / 提示 3） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（44 词 2 句）：ELI shot the dog, but not before it tore open his throat. He emptied the magazine into the animal, which finally loosened its jaws, and toppled sideways, half a dozen darts jutting from its fur, as Eli coughed and rolled over, choking on blood.
- 中文理解：伊莱朝那条狗开了枪，可枪响之前，狗已经把他的喉咙撕开了。他把整个弹匣打进这头动物身上，它才终于松口、侧身倒下，毛里还支着六支麻醉针；伊莱咳着翻过身，血堵在喉咙口。
- 关键词：emptied the magazine · choking on blood
- 为什么这样写：第一句就把顺序拧了一下："but not before" 让读者先看到枪，再看到喉咙，受伤这件事反而落在句子末尾。第二句的动词全给了狗——松口、倒下、针从毛里支出来——人只剩咳和翻身；"half a dozen darts" 让读者看清扎在狗身上的是六支麻醉针。写到血，句子就断了，没有给他一句喘息。
- 读者视角提示：喉咙被撕开还能站起来的角色，后面再挨什么都吓不到读者。狗还活着，麻醉针还插在毛里，这两件事在这一段就交到读者手上。
- **原文**：原文 L18-L21
- **结论**：引语 2 句 44 词（原文 L18）：中文理解逐句对得上，主语=伊莱、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（58 词 3 句）：The sun was going down, the sky overhead streaked orange and pink, bright enough that it made the world look lamplit. It was his favorite kind of evening. His father hated skies like this—said they were a bad omen—but his father was dead, and Eli relished the way the warm light clashed with the bite in the air.
- 中文理解：太阳正在落，头顶的天空被拉成一道橙一道粉，亮得让整个世界像点着灯。这是他最喜欢的那种傍晚。他父亲讨厌这样的天色，说那是不祥之兆；可他父亲已经死了，伊莱偏偏享受暖光撞上冷空气的那一下。
- 关键词：favorite kind of evening · bad omen
- 为什么这样写：三句话走了三步：先给光，再给自己的评价，最后把父亲搬进来。"favorite" 是轻的，可第三个句子里 "bad omen" 与 "was dead" 挤在一起，喜欢与不祥并排放着，谁也不让谁。父亲的死只用 "was dead" 两个词交代，语气平得像在说别人的事。
- 读者视角提示：读者读到这里会觉得这段太舒服了，舒服得不像追人途中该有的段落。父亲那句「不祥之兆」留在句子里，信不信由读者自己拿主意。
- **原文**：原文 L48-L48
- **结论**：引语 3 句 58 词（原文 L48）：中文理解逐句对得上，主语=伊莱、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（41 词 3 句）：A hand wrenched him back. Lockland University was gone, Victor Vale was gone, the pink-streaked night was gone, all replaced by the cold steel of the motel steps. Eli perched precariously on the top stair, Noah’s fists tangled in his jacket.
- 中文理解：一只手把他拽了回来。洛克兰大学没了，维克多没了，那道粉色的夜也没了，全换成了旅馆楼梯的冷钢。伊莱在最上面一级台阶上坐得摇摇欲坠，诺亚的拳头攥着他的夹克。
- 关键词：wrenched him back · cold steel
- 为什么这样写：三个 "was gone" 排着队，把上一段的世界一样一样撤销：学校、朋友、天色，句式不变，速度越来越快。到第四句才让他落地，"cold steel" 同时给出温度和材质，前面那段暖光被一句话抹干净。抓住他的不是手，是 "fists"，力道写在名词上。
- 读者视角提示：读者和他一起被拽出梦境，也和他一样不清楚刚才那几分钟算什么。他被放在最上一级台阶的最外沿，重心悬着，镜头就停在那个位置上。
- **原文**：原文 L84-L87
- **结论**：引语 3 句 41 词（原文 L84）：中文理解逐句对得上，主语=维克多、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（36 词 3 句）：But something caught Eli’s eye—a red metal tin, its lid thrown back. It was empty now, but it hadn’t been. He crouched, and ran a fingertip along the inside, a film of gray coating his skin.
- 中文理解：可有样东西抓住了伊莱的眼睛——一只红铁盒，盖子被掀开。它现在是空的，可刚才不是。他蹲下去，指尖沿着内壁抹过，一层灰沾在皮肤上。
- 关键词：red metal tin · lid thrown back
- 为什么这样写：先给一个空容器，紧跟一句 "but it hadn’t been"：空是现在，之前装过东西。整段证据只有一根手指和一层灰，没有化验，也没有人开口。灰被写成 "a film"，薄，贴在内壁上，抹得下来却抓不住。
- 读者视角提示：盒子开着，里面空了，装过什么要读者自己补。伊莱没有说破，他只让指尖沾上那层灰。
- **原文**：原文 L132-L132
- **结论**：引语 3 句 36 词（原文 L132）：中文理解逐句对得上，主语=伊莱、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（36 词 3 句）：One moment, Sydney was crouched down on the roof, alone, and the next, there were two of her. At least, that’s how it looked at first glance. But the Clarke sisters had always been carbon copies.
- 中文理解：前一秒西德妮还一个人蹲在屋顶上，下一秒那里就有了两个她。至少第一眼看上去是这样。可克拉克家的姐妹从来就是一模一样的复写本。
- 关键词：two of her · carbon copies
- 为什么这样写："One moment" 与 "and the next" 之间不许有过程，两个画面直接对贴。第二句马上退一步（"at first glance"），承认可能是看错；第三句又把退掉的那步收回来，用 "carbon copies" 给一个不靠眼睛的解释。三句里读者的判断被推了两次。
- 读者视角提示：读者先数人数，再怀疑自己数错。姐妹长得一样这件事放在最后一句，等于把「多出来的那个是谁」先按下去。
- **原文**：原文 L243-L243
- **结论**：引语 3 句 36 词（原文 L243）：中文理解逐句对得上，主语=西德妮、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符

### 原句 6
- **md**：引语（40 词 1 句）：There was Sydney, collapsing at her feet, as if the effort of bringing her sister back had taken everything, while Serena stood tall, blond hair caught in the cold breeze, blue eyes half lidded and lips twitching in a smirk.
- 中文理解：西德妮瘫在她脚边，像把姐姐带回来这件事已经用光了她所有力气；塞雷娜却站得笔直，金发被冷风兜住，蓝眼睛半睁，嘴角抽出一个笑。
- 关键词：bringing her sister back · lips twitching
- 为什么这样写：一句话里两个人体位相反：西德妮是 "collapsing"，塞雷娜是 "stood tall"。前半句用 "as if" 给瘫下去的那个一个说法——力气花在复活上；后半句对塞雷娜不给任何解释，只递上头发、眼睛、嘴角三样东西，最后停在 "a smirk" 这个词上。
- 读者视角提示：塌下去的人和站直的人在同一句里，读者很难替她们高兴。那个笑没有对象，也没有声音。
- **原文**：原文 L264-L264
- **结论**：引语 1 句 40 词（原文 L264）：中文理解逐句对得上，主语=西德妮、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L68）
- **档**：相符
