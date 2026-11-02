# 3-diff.md · 《Victorious》第 49 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch49_chapter_iv.txt`
- 受审 md：`ch49 because you are not god.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L5 · R1 事实未进 md（was Eli’s troublesome cellmate）
- **原文**：原文 L78：“Mitchell Turner,” muttered Eli, recalling the troublesome cellmate.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L78：原文 L78 是一处静态状态描写（was Eli’s troublesome cellmate…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

### L6 · R1 事实未进 md（showed that Three were empty）
- **原文**：原文 L60：Gabriel took up a tablet, and tapped it a few times, then offered the device to Eli. On the screen, a grid of videos—footage from a dozen cells that looked identical to his. Three were empty. The others contained figures who sat, or stood, rested, paced. “EON’s current patients. As you can see, Mr.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L60：原文 L60 的事实「showed that Three were empty」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 2（阻断 0 / 提示 2） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（51 词 2 句）：Without windows to the outside world, it was hard to keep track of hours, days. Eli would have had no sense of it at all, if not for the cycle of the lights in his cell, or the clock on the wall of Gabriel’s office, which now read half past three.
- 中文理解：牢房没有一扇通向外面世界的窗，几点、第几天都难算。若不是牢房里的灯光一轮一轮地明灭，若不是加百列办公室墙上那只钟，伊莱对时间根本不会有感觉；那只钟此刻指着三点半。
- 关键词：Without windows · half past three
- 为什么这样写：开头先把昼夜抽掉，再一样一样补回替身：灯光的循环、别人房间里的钟。他算时间得借加百列办公室的钟，读时间的家什挂在别人的墙上。前两句还在说「很难分得清」，末句忽然递来 half past three 这个准数，模糊与精确挨着放，读者手里就有了一个可以抓的刻度。
- 读者视角提示：这一块只写他怎么数时间，没写他在这地方待了多久。三点半是全章唯一一个钟点，后面再没有第二个。
- **原文**：原文 L21-L21
- **结论**：引语 2 句 51 词（原文 L21）：中文理解逐句对得上，主语=伊莱、受事=牢房，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（31 词 3 句）：It was the first time Gabriel had said his name. The first time since Eli’s resurrection that he had heard it said aloud. The sound rang through him like a bell.
- 中文理解：那是加百列第一次把那个名字说出口，也是伊莱复活之后第一次听见它被人念出声。那声音像钟一样从他身上穿过。
- 关键词：said aloud · like a bell
- 为什么这样写：三句绕着同一个名字打转，却一次也没把名字写出来，只用 his name、it、The sound 顶着——名字被听见了，读音却留在空白里。第二句用 The first time 再起一遍，与第一句叠成两级：一级是加百列开口，一级是伊莱听见，中间隔着一个 resurrection。末句给声音一个具体的响法，钟声一响就散，句子也停在这一下上。
- 读者视角提示：这一块只有名字和声音，没有名字的主人在哪儿。读者知道的和他一样多：这个名字刚刚被人念出来，别的都还空着。
- **原文**：原文 L42-L42
- **结论**：引语 3 句 31 词（原文 L42）：中文理解逐句对得上，主语=伊莱、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（33 词 2 句）：Gabriel took up a tablet, and tapped it a few times, then offered the device to Eli. On the screen, a grid of videos—footage from a dozen cells that looked identical to his.
- 中文理解：加百列拿起一台平板，点了几下，把它递到伊莱面前。屏幕上映着一片视频格子，是十几间牢房的画面，每一间都跟他这间一个样子。
- 关键词：offered the device · a dozen cells
- 为什么这样写：三个动作连着走：took up、tapped、offered，中间不插一句解释，读者跟着这串手势走到屏幕前才看见里面是什么。破折号后的 footage from a dozen cells 把「视频」换成「场地」，identical to his 又把十几间并成一间——看过去全是他待的那种屋子。递过来的是画面，不是一句话。
- 读者视角提示：这一块只给格子和十几间同形的牢房，没写屏幕里坐着谁。读者此刻看到的东西，和递到伊莱眼前的那一片几乎分不出差别。
- **原文**：原文 L60-L60
- **结论**：引语 2 句 33 词（原文 L60）：中文理解逐句对得上，主语=伊莱、受事=牢房，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（37 词 1 句）：“Cognitive emphasis,” he said, finally surrendering the device, which vanished into the chair at Gabriel’s side. “The idea that under extreme duress, the necessary circumstances for an EO’s power to emerge, the subject’s determination played a part.”
- 中文理解：「认知强调。」他说，同时终于把平板交了回去，那台机器一进加百列身边的椅子就不见了。他接着解释：在极度胁迫之下——那正是能力显现所必需的条件——受试者的决心也起了一份作用。
- 关键词：extreme duress · determination played a part
- 为什么这样写：术语先出口，动作随后跟上。Cognitive emphasis 只有两个词，交还平板的动作被塞进插入语，等这一小段说完，机器已经 vanished 了。第二句把定义摊开，三个逗号一级一级往上堆条件：under extreme duress、the necessary circumstances、for an EO’s power to emerge，一路压到句末，才落下 played a part 这四个词。
- 读者视角提示：这一块只给理论，不给来处。这套话在他说出口的时候已经成形，读者没看见它是怎么被想出来的。
- **原文**：原文 L87-L87
- **结论**：引语 1 句 37 词（原文 L87）：中文理解逐句对得上，主语=加百列、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（33 词 3 句）：Tell that to the bones I pulled out of my hand, thought Eli grimly. Or my rib, which is still growing spikes. He said nothing, but his expression must have given him away.
- 中文理解：这话你留着跟那堆骨头说去——他阴沉地想——那些骨头是我从自己手里拔出来的。或者跟我那根还在长尖刺的肋骨说。他一个字也没讲，可脸上那点神色大概已经把他漏了出去。
- 关键词：growing spikes · said nothing
- 为什么这样写：这一块把里外分成两半。前两句全是 thought 里的东西，用的还是祈使句 Tell that to...，像在回嘴，可被回的那个人不在句子里。两处伤都带着第一人称 my：pulled out of my hand、my rib，句子因此贴着他的身体走。最后一句掉到外面：嘴上 He said nothing，脸却 must have given him away——一个「必须」把推测留在了半空。
- 读者视角提示：这一块只有心里话和一张没管住的脸。他回嘴的对象不在这里，读者得自己接上前面那几句对话。
- **原文**：原文 L114-L114
- **结论**：引语 3 句 33 词（原文 L114）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符
