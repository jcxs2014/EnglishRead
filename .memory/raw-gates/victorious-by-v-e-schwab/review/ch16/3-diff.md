# 3-diff.md · 《Victorious》第 16 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch16_chapter_xv.txt`
- 受审 md：`ch16 the director comes to call.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（pulled a page out of the battered notebook and read it aloud）
- **原文**：原文 L198：“You shouldn’t have that,” he said, but the woman ignored him. She plucked one of the pages out and began to read aloud.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L198：原文 L198 的事实「pulled a page out of the battered notebook and」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（are Gabriel’s wife and son, whose ashes he scattered among t）
- **原文**：原文 L87：There hadn’t been enough of Ian and Iris to bury, but he’d taken a handful of ash from each and scattered it among the flowers.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L87：原文 L87 的事实「are Gabriel’s wife and son, whose ashes he sca」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 2（阻断 0 / 提示 2） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（42 词 2 句）：LESS than a week after Gabriel Gray destroyed what was left of his wife and son, he heard a car pull up outside. The telltale sound of tires against gravel, disrupting the silence that had settled like a shroud over the house.
- 中文理解：妻儿只剩下一点残骸，被他毁掉还不满一周，他就听见屋外有车碾上碎石。那声音打散了笼罩整栋房子的死寂，而作者把这层死寂写成了一块盖下来的裹尸布。
- 关键词：car pull up outside · shroud
- 为什么这样写：时间在一句里被压成两段：先是「不到一周」的期限，再是「有车来了」的打断。第二句把声音写成破坏者，被破坏的是安静；安静随即被比作裹尸布，于是这栋房子里剩下的一切都带着葬礼的气味。车声刚落，读者已经知道有人要走进来。
- 读者视角提示：注意作者没有写他听见之后的反应，只把声音与寂静并排放着。他的情绪被推迟了，读者只能自己补上那份警觉。
- **原文**：原文 L21-L21
- **结论**：引语 2 句 42 词（原文 L21）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（38 词 3 句）：Gabriel had dismissed the sentiment as paranoia. Now, he wondered if he’d been mistaken. If there was another reason Paul was the first and only patient he’d encountered in his twenty-three years whose trauma translated into something more.
- 中文理解：那种说法，他原先是当成偏执打发掉的。现在他怀疑自己判断错了：会不会另有原因，让保罗成为他二十三年里遇到的第一个、也是唯一一个创伤真的变成了别的东西的病人。
- 关键词：paranoia · translated into something more
- 为什么这样写：三句话里有两句是 if 从句，一句答案也没有。他把「我可能错了」拆成两个可能：一个是 mistaken，另一个是「另有原因」，第二个可能立刻指向保罗的特殊性。二十三年这个数字搁在句中，不解释来历，却把「第一次遇到」变成一次职业长度的对账。
- 读者视角提示：留意「现在」这个词的落点：他没得出新结论，只是把旧结论挪开了一条缝；缝一开，她后面说的每一句都能顺着进去。
- **原文**：原文 L51-L51
- **结论**：引语 3 句 38 词（原文 L51）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（30 词 2 句）：“After the incident”—a tasteful euphemism—“police found her at Paul’s house. She’d been stabbed twenty-seven times.” Gabriel saw Paul in his office, covered in blood. “Did he strike you as violent?”
- 中文理解：她用「那件事之后」替代了事故的说法，随后说警方在保罗家发现了他的妹妹，身上被刺了二十七下。加百列眼前浮出保罗满身血坐在诊室里的样子。她接着问：他给你的印象是暴力的人吗。
- 关键词：stabbed twenty-seven times · covered in blood
- 为什么这样写：破折号里那半句是旁注，等于替读者点出说话人的措辞习惯——她把事故说成「那件事」，却把妹妹的死说得毫厘不差。数字二十七来得干硬，与满身血的画面挤在同一段，谁也没解释。她不递结论，只把两样东西并排放好，然后发问；问句比陈述更像审讯，因为回答的人得先选一边。
- 读者视角提示：那个画面是加百列自己补上的，不是她给的。作者连「他想起」都没写，画面直接插进来，插进来的位置正好在二十七与问句之间。
- **原文**：原文 L174-L174
- **结论**：引语 2 句 30 词（原文 L174）：中文理解逐句对得上，主语=加百列、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 4
- **md**：引语（47 词 4 句）：“According to the coroner, the wounds weren’t made by a knife, but glass. Twenty-seven different shards. And yet, no broken glass was found at his apartment.” “Strange,” said Gabriel, because it was. Everything about Paul Barnett had been strange. “But I’m not sure how I can help.”
- 中文理解：按验尸官的报告，那些伤口不是刀造成的，是玻璃——二十七块不同的碎片。可他公寓里根本找不到碎玻璃。加百列说「奇怪」，因为他知道保罗·巴内特身上全是奇怪的事；他拿不准自己能帮上什么忙。
- 关键词：different shards · no broken glass
- 为什么这样写：前半句用 weren’t made by… but… 把凶器的性质整个换掉；中间的碎片数与前文「刺了二十七下」对上，却换了材质。最后一句是让步：加百列不肯接这个案子，理由不是案子不重要，而是保罗这个人从头到尾说不清。
- 读者视角提示：二十七块玻璃是本章留下的第一个问号。读者会记住：有伤口，现场却没有凶器。
- **原文**：原文 L180-L183
- **结论**：引语 4 句 47 词（原文 L180）：中文理解逐句对得上，主语=加百列、受事=玻璃，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L52）
- **档**：相符

### 原句 5
- **md**：引语（46 词 5 句）：“A sleepwalking accident,” said Gabriel. “According to the file, he fell from a fourth-floor window. By all accounts, he should have died.” “He did. Technically. For three minutes on the way to the hospital.” Gabriel frowned, unsure why that was relevant. “Did Paul ever mention EOs?”
- 中文理解：「梦游造成的事故，」加百列说。「按病历，他是梦游着从四楼的窗户摔下去的。按所有记录，他不该活下来。」「他死了。严格来说，死了三分钟——去医院的那路上。」加百列皱起眉，不明白这有什么相干。「保罗有没有提过 EO？」
- 关键词：fourth-floor window · for three minutes
- 为什么这样写：前两句是病历腔，事实一个一个往下摆：四楼、摔下去、本不该活。第三句突然把语体切掉，剩三个孤零零的短句：He did. Technically. For three minutes…。最后那个补充句像在更正自己——技术上而已。三分钟这个数字把「本该死」改成了「差一点」，也把本章的问题摆到了桌上：他当初也差点没活下来。
- 读者视角提示：海伦娜临走问的「那一晚你也差点没命」，问的就是这三分钟。读者到这里才明白加百列为什么懂得濒死是什么。
- **原文**：原文 L273-L276
- **结论**：引语 5 句 46 词（原文 L273）：中文理解逐句对得上，主语=加百列、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L62）
- **档**：相符

### 原句 6
- **md**：引语（38 词 2 句）：“It’s short for ExtraOrdinary,” she explained. “It’s a term that caught on, several years ago, in certain corners of the internet. A word for those rare people who, following a near-death experience, found themselves alive, but permanently altered.”
- 中文理解：她解释说，EO 是 ExtraOrdinary 的缩写；这词几年前在某些网络圈子里传开，用来指那样一小群人——经历过濒死，活了下来，却从此被永久改变。
- 关键词：near-death experience · permanently altered
- 为什么这样写：定义排得很讲究：先给缩写，再给这个词的来历，最后才给所指的人。来历被放在中间，等于给这个称呼一份不太体面的出处；可她的语气像在解释常识，不像在提一个假说。alive 与 permanently altered 之间只隔一个 but，那个转折把「活着」和「被改动过」绑在同一句里，读者会立刻把它往加百列身上套。
- 读者视角提示：她整段都在描述一类人，没有一句指着他。加百列有没有把自己算进这一类，作者一个字也没写——接下来的沉默是他的。
- **原文**：原文 L282-L282
- **结论**：引语 2 句 38 词（原文 L282）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=网，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L72）
- **档**：相符

### 原句 7
- **md**：引语（44 词 2 句）：“You asked me, when I first arrived, what I was the director of.” Helena produced a small card, black on black, and handed it to him. When he took it, he found a number ghosted on one side, and three letters on the other.
- 中文理解：她先提醒他，刚进门时他问过她这个主任管的是什么；然后取出一张小小的卡片，黑底黑字，递到他手里。他接过去才发现，一面压着一串号码，另一面是三个字母。
- 关键词：black on black · three letters
- 为什么这样写：动作都很轻：取出、递过来、接过、发现，没有一个词在强调分量。黑底黑字的卡片本身就是自我介绍——不靠显眼，靠不显眼。她先把「你自己问过」说出来，答案就成了他求来的，而不是她塞给他的；一句提醒，把递卡片的动作换成了回答。
- 读者视角提示：这一段只给了他数量，没给他内容：三个字母是看得见的，是哪三个却要等；读者和他一样，手里先只有一张黑卡片。
- **原文**：原文 L300-L300
- **结论**：引语 2 句 44 词（原文 L300）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L82）
- **档**：相符

### 原句 8
- **md**：引语（43 词 2 句）：“You had your own close call that night.” Her voice was light, as if the question was nothing but an afterthought. But her gaze was sharp, searching. “I suppose I should ask, have you experienced anything abnormal in the aftermath of your accident?”
- 中文理解：临走前她提起，那一晚他自己也差点没命。她的声音很轻，仿佛这问题只是顺口想起；可她的目光是紧的，在找东西。随后她把话说全：事故之后，他有没有经历过任何不正常的事。
- 关键词：close call that night · afterthought
- 为什么这样写：轻的声音与锐的目光被摆在同一段里：作者用 as if 把前者标成表演，用 But 把后者标成真的，两个信号互相拆台，读者因此知道哪一句是她真正在意的。问题本身问的是有没有经历过，不是你现在怎么样——她要的不是安慰他，是确认他身上出现过什么。
- 读者视角提示：这是她把问题包成闲聊的又一次：前面的礼貌全在这里露出用途。注意她问的是过去那晚，而不是此刻他的心情。
- **原文**：原文 L315-L315
- **结论**：引语 2 句 43 词（原文 L315）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L92）
- **档**：相符
