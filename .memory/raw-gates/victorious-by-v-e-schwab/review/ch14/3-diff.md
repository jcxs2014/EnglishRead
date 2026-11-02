# 3-diff.md · 《Victorious》第 14 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch14_chapter_xiii.txt`
- 受审 md：`ch14 try harder.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（typed in the address of EON’s former employee portal and met）
- **原文**：原文 L33：EON used to have a forward-facing portal, albeit an encrypted one, for employee access. But nearly a year ago, it had ostensibly gone dark. Now there was no public site, and he was greeted with a blank page and an error message. But Mitch was undeterred.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L33：原文 L33 是回忆/前史交代（typed），md 未复述不影响本章线索理解；本条属背景交代，判提示不修
- **档**：提示

### L3 · R1 事实未进 md（hit a sequence of keys and opened a coding window with a sin）
- **原文**：原文 L39：He hit a sequence of keys, and a coding window popped up.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L39：原文 L39 是外观/随身物品描写（hit a sequence of keys and opened a …），无情节转折；判提示不修
- **档**：提示

### L5 · R1 事实未进 md（dumped the hardware and forced Syd to upend her life again）
- **原文**：原文 L72：Mitch found himself rebuffed, expelled. Which would have been bad enough, but worse, the system pursued him when he fled. Leaping like a virus from their server onto his computer, attacking as it tried to unearth anything and everything it could with terrifying speed. Mitch had triggered a self-dest
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L72：原文 L72 是外观/随身物品描写（dumped the hardware and forced Syd t…），无情节转折；判提示不修
- **档**：提示

### L6 · R1 事实未进 md（stores its information nested, with the employee roster in a）
- **原文**：原文 L63：It had been painstakingly slow, full of trial and error, but over the course of those first two years on the run, he’d peeled back the layers of the EON mainframe. Carefully, so he wouldn’t trigger any recoil, he slipped behind their digital defenses. EON’s computers had always been a complex system
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L63：原文 L63 是回忆/前史交代（stores），md 未复述不影响本章线索理解；本条属背景交代，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 4（阻断 0 / 提示 4） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（40 词 3 句）：As far as he could tell, this was the only remote access with the EON server. And even if it looked defunct, it wasn’t. The door had been sealed, painted over, but underneath, some point of contact was still there.
- 中文理解：在他看来，这是唯一还能远程够到 EON 服务器的入口。就算它看上去已经废弃，其实并没有。门被封死了、还刷了漆盖住，可漆层底下，仍留着一处可以接触的地方。
- 关键词：remote access · painted over
- 为什么这样写：三句话在做同一件事——先给判断，再拆掉判断的反面，最后把判断落到一个能看见的物件上：封死的门、刷上去的漆、漆下还在的接触点。他的说法不是「我猜里面还有人」，而是「底下还有一个接触点」，语气像已经摸过一遍。门这个比喻把「废弃」和「仍在使用」放在同一个表面上，读者看见那道漆，也就跟着相信漆底下有东西。
- 读者视角提示：留意 painted over 这个动作——它要挡的不是所有人，只是让路过的人以为这里什么都没有。米奇能说出 underneath 有什么，说明他不是路过的那一个。
- **原文**：原文 L36-L36
- **结论**：引语 3 句 40 词（原文 L36）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（44 词 3 句）：Mitch found himself rebuffed, expelled. Which would have been bad enough, but worse, the system pursued him when he fled. Leaping like a virus from their server onto his computer, attacking as it tried to unearth anything and everything it could with terrifying speed.
- 中文理解：他被弹了回去，被驱逐出来。这本来已经够糟，更糟的是他逃的时候系统追了上来：它像病毒一样从他们的服务器跳到他的电脑上，一边攻击，一边以可怕的速度想把他机器里的东西全挖出来。
- 关键词：rebuffed · like a virus
- 为什么这样写：三句一层比一层更往里：先是门关上（rebuffed, expelled），再是追出门（pursued him when he fled），最后是进到他机器里（from their server onto his computer）。主语一直是 the system，米奇只出现在受格 him 的位置上，三个句子里他一次也没有还手。Leaping like a virus 把一段程序写成有生命的东西；terrifying speed 是这里唯一形容速度的词，它形容的不是攻击本身，而是他来不及反应。
- 读者视角提示：读这三句时数一下米奇做了几个动作——零个。失败被写成一串被动语态，而不是一场打斗；越是这样写，他在这段里的位置就越清楚：他不是在打，他是在被找。
- **原文**：原文 L72-L72
- **结论**：引语 3 句 44 词（原文 L72）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（36 词 2 句）：The next time he tried (and failed to so much as crack the outer layers of the EON mainframe), the system didn’t chase him off again. Instead, after rebuffing his attempts, it responded with two words.
- 中文理解：下一次他再试，连 EON 主机的表层都没能撬开，系统这回没有把他赶走。它挡回他的尝试之后，回了他两个词。
- 关键词：outer layers · two words
- 为什么这样写：括号里那半句是这一段的秤砣：他退得更远了，连 outer layers 都碰不到；可对方的反应却软下来，didn’t chase him off again 与 responded 之间只隔一个 Instead。一边在退，一边在让，两条方向相反的线在这里交叉，读者会先松一口气，然后才觉出不对：一个肯回话的系统，比一个只会追人的系统更不像机器。
- 读者视角提示：注意 responded 这个词——它把「被挡回」换成了「被回答」。他没有拿到任何入口，却拿到了回应；这两件事在句子里只隔一个逗号，重量完全不同。
- **原文**：原文 L84-L84
- **结论**：引语 2 句 36 词（原文 L84）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符
