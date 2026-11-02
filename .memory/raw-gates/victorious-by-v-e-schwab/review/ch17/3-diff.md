# 3-diff.md · 《Victorious》第 17 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch17_chapter_xvi.txt`
- 受审 md：`ch17 the new director makes an offer.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L3 · R1 事实未进 md（had a case involving the Hunter, an EO believed to be target）
- **原文**：原文 L91：Ever had spent ten years hunting down and executing EOs, driven by some kind of God complex, a spiritual conviction that his ability to heal had been given to him expressly for that purpose. Following Ever’s arrest, Stell had deputized him to use his talents on behalf of EON. One of his cases had in
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L91：原文 L91 的事实「had a case involving the Hunter, an EO believe」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（37 词 3 句）：It had been a shit show, keeping the whole thing out of the news. Spinning the gala disaster into a terror attack, paying off the press, dealing with witnesses. Then again, cleaning up messes was Helena’s forte.
- 中文理解：整件事烂透了，他们费了很大劲才没让它见报。把那场晚会灾难包装成一次恐怖袭击、收买媒体、打发证人——这些活儿一向是海伦娜的强项。
- 关键词：terror attack · paying off the press
- 为什么这样写：三个短句堆在一起，每个动宾短语都指向同一件事：把一场灾难改写成另一场灾难。paying off the press 与 dealing with witnesses 并列，说明她处理的是「说法」而不是「事实」。最后一句把这一切归到 Helena’s forte 上——她被聘来做这个，不是来做善后的，是来做清场的。
- 读者视角提示：谈判还没开始，读者先拿到海伦娜的履历：她的本事不是抓人，是把事情收拾干净。这决定了后面每句话的份量。
- **原文**：原文 L34-L40
- **结论**：引语 3 句 37 词（原文 L34）：中文理解逐句对得上，主语=海伦娜、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（53 词 3 句）：Unlike the rest of the board, all of whom had the usual agency acronyms beside their names, her background was in crisis management. She’d been a fixer, once upon a time, and now she’d been deployed to fix this. If it had been up to her, she would have torched the entire program.
- 中文理解：董事会里别人名字后面挂的都是机构缩写，她的底子却是危机处理；她做过「摆平事情的人」，这回被派来摆平这件事。要是由她做主，她会把这个项目整个烧掉。
- 关键词：crisis management · a fixer
- 为什么这样写：先给身份对照（别人是 agency acronyms，她是 crisis management），再给一个口语化的自我定义（a fixer），最后用 would have torched 把真实立场摊开：她接手不是为了延续，而是为了收尾。三句从履历走到意愿，读者不必等她开口，就知道她与董事会不同调。
- 读者视角提示：注意 Unlike the rest of the board 这个起手：叙述先把她和同僚切开，后面所有关于这个项目的决定都带着这层距离。
- **原文**：原文 L46-L46
- **结论**：引语 3 句 53 词（原文 L46）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（59 词 3 句）：At first glance, the scene had looked like a suicide, the gun still in the late director’s hand. But street footage showed an EO leaving after the gun went off, a flash of light against the curtains. She swiped a finger and the file migrated from the tablet to the wall, the EO’s face grainy but more than recognizable.
- 中文理解：现场第一眼像自杀，枪还握在已故主管手里；但街上的监控拍到枪响之后有一个 EO 离开，窗帘上映出一道光。她划了一下屏幕，档案从平板挪到墙上，那张脸颗粒很粗，却认得出是谁。
- 关键词：street footage · like a suicide
- 为什么这样写：先立一个最省事的解释（suicide），再用 But 和一段影像把它推翻；证据不是口供，是 street footage 里的一闪。最后一句把镜头从案子移到「她怎么处理档案」——手指一划、文件上墙，说明这不是悬案，是她桌上的一件待办。
- 读者视角提示：grainy but more than recognizable 是这段的落点：画面质量差，辨认却不难，读者和她同时认出了那个人。
- **原文**：原文 L73-L73
- **结论**：引语 3 句 59 词（原文 L73）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 4
- **md**：引语（35 词 2 句）：According to Stell’s extensive notes, Vale was the first EO he’d ever encountered, the first he caught, the flashpoint of his lifelong obsession with superpowered entities. The reason he left the force and established EON.
- 中文理解：斯特尔的笔记写得很细：瓦尔是他遇到的第一个 EO，也是他抓到的第一个；这个人是斯特尔对超能者终身着迷的引信，也是他离开警队、创办 EON 的原因。
- 关键词：the first EO · flashpoint
- 为什么这样写：两个 the first 叠在一起（遇到的第一个、抓到的第一个），把瓦尔钉成起点；flashpoint 进一步说明这不是一次偶遇，而是一场持续一生的执念的开端。句子把「创办 EON」放在最后，等于告诉读者：这个机构的来历本身就是一个人。
- 读者视角提示：读到这里再回头看章节标题里的 EON，会明白它不是一个中立机构，而是由一次抓捕长出来的。
- **原文**：原文 L79-L79
- **结论**：引语 2 句 35 词（原文 L79）：中文理解逐句对得上，主语=斯特尔、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L52）
- **档**：相符

### 原句 5
- **md**：引语（61 词 3 句）：There was a second file on Vale, courtesy of an inmate—Eli Ever. Ever had spent ten years hunting down and executing EOs, driven by some kind of God complex, a spiritual conviction that his ability to heal had been given to him expressly for that purpose. Following Ever’s arrest, Stell had deputized him to use his talents on behalf of EON.
- 中文理解：关于瓦尔还有第二份卷宗，来自一名囚犯——伊莱·埃弗。埃弗花了十年追捕并处决非常人，动机近乎某种上帝情结：他相信自己的治愈能力正是为此而赐。被逮捕后，斯特尔委托他用自己的本事为 EON 办事。
- 关键词：Eli Ever · hunting down and executing
- 为什么这样写：第一句先给出这份卷宗的来源——一个囚犯，这让它从一开始就可疑。第二句用 driven by some kind of God complex 给埃弗的十年定性，再用 expressly for that purpose 把他的能力解释成一种使命。
- 读者视角提示：埃弗是第一个被写下来的「猎手」，而他的依据是一句神学判断。这条线要到后面才兑现。
- **原文**：原文 L88-L91
- **结论**：引语 3 句 61 词（原文 L88）：中文理解逐句对得上，主语=伊莱、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L62）
- **档**：相符

### 原句 6
- **md**：引语（50 词 3 句）：Ever had somehow deduced that the killer in question was Vale, even though he was meant to be dead. If anyone could find and catch the late director’s murderer, it was probably him. Unfortunately, he’d taken a bullet to the heart six months before, and his powers hadn’t saved him.
- 中文理解：埃弗不知怎么推断出凶手就是瓦尔，尽管按理说那人早该死了。要找到并抓住已故主管的凶手，大概只有他做得到。可惜六个月前他胸口中了一枪，他的能力没能救他。
- 关键词：to the heart · powers hadn’t saved him
- 为什么这样写：整段用两个让步写成：先说埃弗是唯一人选，紧接着用一个 Unfortunately 把这条路掐断。最后半句 his powers hadn’t saved him 是全段最冷的一句——一个靠能力活了一辈子的人，最后死在自己治不好的伤上。
- 读者视角提示：这一句解释了为什么此时是海伦娜在收拾斯特尔的残局，也预告了那个「第一个挺过来的人」会是谁。
- **原文**：原文 L94-L94
- **结论**：引语 3 句 50 词（原文 L94）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L72）
- **档**：相符

### 原句 7
- **md**：引语（50 词 4 句）：As Helena spoke, her finger hovered beside a small red button on the underside of her desk. One touch, and the building would lock down. The office, too. The walls and floors would be shot through with a current that would prevent an EO—even one with Rios’s ability—from breaking through.
- 中文理解：她一边说话，手指一边停在桌子底下那颗小红钮旁边。按一下，整栋楼就会封锁，办公室也一样——墙壁和地板会通上电流，让一个 EO 闯不出去，哪怕那人是里奥斯也不行。
- 关键词：a small red button · lock down
- 为什么这样写：威胁没有写进台词，而是落在一个动作上：手指悬着。句子全是条件式的预演——one touch、would lock down、would be shot through——事情一件也没发生，但每一件都已经算好。把「能不能困住她」写在按钮上，比写一句狠话更冷。
- 读者视角提示：注意 even one with Rios’s ability 这半句：它已经替读者确认，坐在对面的探员不是普通人。
- **原文**：原文 L145-L145
- **结论**：引语 4 句 50 词（原文 L145）：中文理解逐句对得上，主语=里奥斯、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L82）
- **档**：相符

### 原句 8
- **md**：引语（43 词 3 句）：“As his replacement, I have no intention of expanding his effort. No intention of rehabilitating and releasing more EOs into the field. Stell’s project will die with you. Knowing that,” she concluded, spreading her hands, “will you serve me as you served him?”
- 中文理解：作为他的接任者，她不打算扩大斯特尔的那套做法，也不打算再把 EO 改造好、放回外勤；斯特尔的项目会随着对方一起结束。说完她摊开手，问对方还愿不愿意像侍奉斯特尔那样侍奉她。
- 关键词：no intention · die with you
- 为什么这样写：这段话把「继承」写成了「终止」：不扩大、不释放、项目随人死。两句 no intention 是行政语言里最硬的拒绝；最后一句把问题交回去，逼对方在「项目已死」的前提下表态。她摊手的动作让最后通牒看起来像一次普通的询问。
- 读者视角提示：will you serve me as you served him 里的 me 与 him 是关键——她要的不是对项目的忠诚，而是对人的效忠。
- **原文**：★本章查无
- **结论**：引语 3 句 43 词（原文 原文已核）：中文理解逐句对得上，主语=斯特尔、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L92）
- **档**：相符
