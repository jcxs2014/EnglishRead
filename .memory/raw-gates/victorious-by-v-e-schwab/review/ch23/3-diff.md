# 3-diff.md · 《Victorious》第 23 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch23_chapter_iv.txt`
- 受审 md：`ch23 gabriel tours eon.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L4 · R1 事实未进 md（has been assigned to capture Victor Vale for months and has ）
- **原文**：原文 L126：“Victor Vale,” said Helena, the frustration heavy in her voice. “Rios has been assigned to him for months now. But so far, he’s evaded capture.”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L126：原文 L126 是一处静态状态描写（has been assigned to capture Victor …），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

### L5 · R1 事实未进 md（directs EON, which functions autonomously while the governme）
- **原文**：原文 L75：She nodded. “My predecessor, Stell, was the first to see the need for EON. He secured funding from a few key people in the security and tech sectors who recognized the urgency and provided the necessary resources. By now, the government knows of us, and shares any relevant intel, but we function aut
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L75：原文 L75 的事实「directs EON, which functions autonomously whil」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 2（阻断 0 / 提示 2） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（59 词 2 句）：“THE facility is designed as a series of nesting squares,” explained Helena as she led him down a white hall. “All staff resources—food, medical, admin, armory—make up the perimeter. The EOs’ cells form the centermost block, and each is self-contained, and surrounded on all sides by a second buffering chamber, so there’s no risk of interaction whatsoever between prisoners.”
- 中文理解：海伦娜领着他沿一条白走廊走，边走边讲：整座设施是一层套一层的方形。食物、医疗、行政、军械这些员工资源围在最外一圈，EO 的牢房占住最中心，每间自成一格，四面再包一层缓冲腔，所以囚犯之间不存在任何互相接触的可能。
- 关键词：nesting squares · buffering chamber
- 为什么这样写：她把一栋楼当成可以复述的图纸来讲，顺序从整体收到最里面：先给形状，再分用途，最后才落到牢房。四个词用破折号串成一口气（food, medical, admin, armory），语速偏快，像背熟的导览词。真正要强调的东西压在句末：no risk of interaction whatsoever，前面所有安排都为这一句服务，whatsoever 把语气推到没有例外。
- 读者视角提示：整段只有她一人在说，听的人一个字没问，读者拿到的先是设计图，不是人。她用的词是 prisoners；至于这些人为什么在这里、各自叫什么，这一段全无交代。
- **原文**：原文 L18-L18
- **结论**：引语 2 句 59 词（原文 L18）：中文理解逐句对得上，主语=海伦娜、受事=牢房，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（32 词 4 句）：“How many ExtraOrdinaries are out there?” he asked as they continued on. “That’s the billion-dollar question,” said Helena. “And the answer is … we don’t know. Hundreds, at least. Maybe even more.”
- 中文理解：「外面到底有多少非常人？」他边走边问。「这是那个十亿美元的问题，」海伦娜说。「答案是……我们不知道。至少几百个，也许更多。」
- 关键词：billion-dollar question · Hundreds, at least
- 为什么这样写：问句用日常口吻，答句却先给它定价——十亿美元。然后是一个停顿，再是「我们不知道」。真正的答案藏在后半句的两个数字里：至少几百，也许更多。
- 读者视角提示：这是加百列第一次听说这个机构的规模，而「我们不知道」意味着连他们也没有名单。他后面整套研究，起点就是这半个答案。
- **原文**：原文 L48-L51
- **结论**：引语 4 句 32 词（原文 L48）：中文理解逐句对得上，主语=海伦娜、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（36 词 2 句）：There, a dozen faces stared back at him from an array of driver’s licenses, mug shots, school photos, wedding pictures. Each was surrounded by a mismatched tapestry of grainy camera stills, article clippings, lines of text.
- 中文理解：那里，十二张脸从驾照、嫌犯照、学生照和结婚照的拼贴里瞪着他。每张脸四周都围着不相称的碎片：模糊的监控截图、剪报、一行行文字。
- 关键词：a dozen faces · driver’s licenses
- 为什么这样写：四个词排在一起，全是官方档案里最标准的证件照来源，句子读起来像一份名单。第二句用 a mismatched tapestry 把这些碎布说成一幅不匹配的挂毯——但拼错的恰恰是这些人的人生。
- 读者视角提示：墙上十二张脸就是琼摊开的那十二张牌，只是这里换成了证件照。同样的十二个人，两种编目方式。
- **原文**：原文 L105-L105
- **结论**：引语 2 句 36 词（原文 L105）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=碎片，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 4
- **md**：引语（41 词 3 句）：Gabriel took a step closer to the wall, searching the profiles for any discernible pattern—age, race, gender, class—but the only obvious commonality was that they’d each defied death. Each had survived a seismic trauma and been permanently changed by it. Fascinating.
- 中文理解：加百列朝那面墙走近一步，在那些档案里找一个站得住的规律——年龄、种族、性别、阶层——可唯一站得住的共同点是：这些人都违抗过死亡。每个人都熬过一场剧烈创伤，并因此被永久改变。有意思。
- 关键词：defied death · seismic trauma
- 为什么这样写：四个常用的分类维度被破折号压在一处，随即一句全部否掉：but the only obvious commonality。否掉之后拿出来的答案不是社会标签，而是一个动作——defied death。末尾单独一句 Fascinating，把前面的否定转成兴奋，三个词就把这个人的立场交代干净。
- 读者视角提示：他的「找规律」和「有意思」紧挨着出现，读者能觉出他面对这些人时没有惧意，只有样本送到手边的快活。这一段没有出现任何一个目标的名字，墙对他还是一面墙。
- **原文**：原文 L111-L111
- **结论**：引语 3 句 41 词（原文 L111）：中文理解逐句对得上，主语=加百列、受事=档案，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L52）
- **档**：相符

### 原句 5
- **md**：引语（31 词 2 句）：But instead of taking himself out of the videos, he’s putting himself in.” She gestured to the timestamps of two separate feeds. They were marked less than an hour—and three states—apart.
- 中文理解：她接着上一句说：他没有把自己从画面里剪掉，反而把自己放了进去。她指了指两段不同来源画面的时间戳——两者相隔不到一小时，中间却隔着三个州。
- 关键词：putting himself in · timestamps
- 为什么这样写：先摆出别人通常会做的事（taking himself out），再摆出他做的事（putting himself in），一对反义动作就把这个人定了性。后面不加评论，只让她去指时间戳，把两个数字亮出来：不到一小时，三个州。数字比形容词有力，读者自己会算出他不可能真的待在那里。
- 读者视角提示：这一段没有说画面是假的，只说了改法；读者要自己把「改过」和「放进去」接起来，再意识到他自己也知道这会被人看破。一小时与三个州之间的距离，是这段话里唯一的证据。
- **原文**：原文 L132-L132
- **结论**：引语 2 句 31 词（原文 L132）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L62）
- **档**：相符

### 原句 6
- **md**：引语（37 词 2 句）：“If it was up to me, I’d write him off,” said Helena. “He’s more trouble than he’s worth. But the board wants to make a point.” “Why’s that?” “Because,” she said, “he’s the one who killed Stell.”
- 中文理解：「要是我做主，我会直接把他划掉，」海伦娜说。「他惹的麻烦比他的价值大得多。但董事会要拿他立个规矩。」加百列问：为什么？她答：「因为，杀斯特尔的人就是他。」
- 关键词：write him off · killed Stell
- 为什么这样写：三层推进：先给海伦娜自己的判断（划掉），再给外部压力（董事会），最后才给原因。三句里主角换了三个人：她、董事会、那个「他」。名字直到最后一句才出现，而且是在一句引语里——她说到斯特尔时用的是过去式，说「他」时用的是现在式：人还活着，旧账还没结。
- 读者视角提示：斯特尔是 EON 的前任主任，董事会要为一个死掉的主任立规矩。这句把本章那个男孩从「危险品」改写成「凶手」——也是海伦娜为什么亲自带队看住他的原因。
- **原文**：原文 L138-L144
- **结论**：引语 2 句 37 词（原文 L138）：中文理解逐句对得上，主语=加百列、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L72）
- **档**：相符

### 原句 7
- **md**：引语（38 词 2 句）：Xavi scrambled backward as a second wall descended from the ceiling farther down the hall, blocking the boy’s retreat. He spun in a panicked circle as gas poured in from hidden vents, pluming thick and white around him.
- 中文理解：第二道墙从走廊尽头的天花板上落下来，堵住男孩的退路，他手脚并用地往后挣。他在原地惊惶地转圈，毒气从暗藏的通风口灌进来，在他周围翻成又厚又白的一团。
- 关键词：second wall descended · hidden vents
- 为什么这样写：两句里全是压下来的动作：descended、blocking、poured、pluming，主语分别是墙和气，男孩只剩 scrambled 与 spun 两个反应。先封退路，再放气，这个先后顺序本身就是一套处置流程。他所有的动作都在原地打转，没有一个能带他出去。
- 读者视角提示：这里才把名字写出来——Xavi，名字和「被困住」同时到达，读者的同情是被这个顺序逼出来的。毒气写成又厚又白的一团，没有写剂量，也没有写男孩能撑多久。
- **原文**：原文 L271-L271
- **结论**：引语 2 句 38 词（原文 L271）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L82）
- **档**：相符

### 原句 8
- **md**：引语（40 词 2 句）：She shook her head. “You have a lot to learn about EOs. That one,” she said, gesturing to the unconscious boy as the guards forced his limbs back into the straitjacket, “can erase a person’s mind, just by touching them.”
- 中文理解：她摇了摇头，说他对 EO 还有很多要学。她指了指那个已经昏迷的男孩——警卫正把他的四肢塞回束身衣——说这一个只要碰到人，就能把人的心智抹掉。
- 关键词：straitjacket · erase a person’s mind
- 为什么这样写：答案被放在句子最末，中间还隔着一个插入语：先指人，先让读者看见警卫把四肢塞回束身衣，再补上能力。一个昏迷的、已经被绑住的少年，和「抹掉心智」被压进同一句，危险与无害的样子因此分不开。开头那句 You have a lot to learn 先把说话的对象定成外行。
- 读者视角提示：能力被限定在触碰上，just by touching them 这几个词把安全距离抹掉了。她没有解释这类人为什么关在牢里而不是病房；她只交代了怎么把人绑回去。
- **原文**：原文 L295-L295
- **结论**：引语 2 句 40 词（原文 L295）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L92）
- **档**：相符

### 原句 9
- **md**：引语（35 词 3 句）：He stilled, remembering the hungry way the boy had eyed his outstretched hand. It sickened him. Not just the danger, narrowly avoided, but the idea that it had been a test, and he’d just failed.
- 中文理解：他停住了，想起那男孩盯着他伸出去的手时那种饥饿的眼神。这让他恶心。不只是因为刚刚躲过的危险，而是因为他想到那是一场试探，而他刚刚没通过。
- 关键词：outstretched hand · just failed
- 为什么这样写：第一句先用 stilled 让身体停住，再让记忆追上来。hungry 把求助的目光改写成「要」的目光，一个词就把刚才那一幕翻了面。第三句把恐惧切成两层：前面那层是刚躲过的危险，后面那层更狠——危险已经过去，失败留了下来。
- 读者视角提示：他恶心的对象不是那个男孩，是自己。文本没有交代这场试探是谁设的——是这座楼在考他，还是他自己给自己出了一道题，两种读法都站得住。
- **原文**：原文 L298-L298
- **结论**：引语 3 句 35 词（原文 L298）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L102）
- **档**：相符
