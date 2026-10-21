# R3 三张单子 · A Fatal Legacy ch17《The National Portrait Gallery》

> 审查方：独立审查员（只管 ch17）
> 原文（唯一权威源）：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch17_17.txt`（6,133 字符；行号按该文件）
> 被审 md：`.../ch17 callie sketches elizabeth at the gallery.md`（12,553 字节；行号按该文件）
> 铁律已守：先读 text 落盘 `1-suread.json`，再读 md；本文件在 md 落盘后写。
> 引语逐字已用两套路径独立核过（`scripts/chapter.sh --json` 6/6；另用 Python 逐块 `str.find` 连续子串 + 行号复算，6/6 且全部连续无 `…` 缝合）。
> 词汇例句 30 条逐条 `in` 命中本章原文（30/30）。

---

## 一、漏（素读有、md 无）

### L1 ｜「她其实没吐」这一事实缺失 ｜ 档：提示

- 原文侧（`text/ch17_17.txt:29`）：
  > `Callie stared at the white porcelain bowl for a moment, not sure if she was going to be sick or not. The wave of nausea seemed to abate and she stood up. Judging by the tutting, quite a queue was forming outside. She performatively flushed the empty toilet and went to wash her hands.`

  其中 `the empty toilet`（马桶是空的）＋ `performatively flushed`（做样子冲水）＝**她在馆里并没有吐**。
- md 侧（`ch17 … .md:11`）：
  > `卡莉在国家肖像馆临摹伊丽莎白一世的画像，等消息的半个钟头里坐不住：合同的回音刚到，她的胃却先开始反酸；中途躲进洗手间，……`

  md 写到「躲进洗手间」为止，全章精读与总结都未出现「马桶是空的／冲水是表演」这一层。
- 影响：读者容易把「躲进洗手间」读成「她在里面吐了」，而原文恰恰相反——她难受着走出来，还在众目下做了一次假冲水。
- 修法（不需改结论）：在原句 4 的「读者视角提示」或导航「身体线」补半句「马桶是空的，她其实没吐，冲水只是做样子」。

### L2 ｜欧拉莉亚「其实很孤独、把卡莉当安慰」这层人物转折缺失 ｜ 档：提示

- 原文侧（`text/ch17_17.txt:83`）：
  > `Callie didn’t expect the world’s most mysterious pop girlie, who had gripped a certain section of the internet with a whole lot of unprocessed trauma and obsessive tendencies, to be lonely, let alone to see her as a source of comfort.`
  > `Callie remembered reading on some blog somewhere that Eulalia had studied at the Royal College of Music.`

  紧接其后才是电话与 `She checked her email for the ‘thing’ that Eulalia had seen but nothing came through.`
- md 侧：导航「线索结构」只列 **工作线／等待线／身体线** 三条（`md:13`）；「一句话总结」（`md:110`）与六个引语块的分析里都没有「欧拉莉亚的孤独」这一转向。该段文字在 md 中只以两条词汇例句（`unprocessed`、`transient`）的形式存在。
- 影响：等待线之所以「滑」（Eulalia 一直在绕），原文给出的动机是她的创伤与孤独；md 把它读成单纯的闪躲。这属覆盖缺口，不是事实错误。
- 修法：导航「线索结构」或「人物弧线」补一句「欧拉莉亚的孤独才是她不肯直说的原因」。

### L3 ｜怀孕／瞒着家人的那条线未进入导航与总结 ｜ 档：提示

- 原文侧（`text/ch17_17.txt:23`）：
  > `Or rather than a beach holiday she should use some of the money on a good pram. Something they could use for all their children. Although she thought that her father would make a show of buying the baby one from Rolls-Royce. Not that they made prams, but she thought there was a chance he would ask them to make an exception for him. She needed to work out how she’d tell her mother, but that was a problem for another day.`
- md 侧：「身体线」被写成等待消息引起的焦虑（`md:13`、`md:110`），导航与总结里都看不到「她已怀了孩子、还没想好怎么告诉母亲」这一层；`pram` 只作为基础词条出现（`md:103`），例句正是上面这句。
- 影响：原文里这具身体不只是「紧张」，它连着婴儿车、父亲、母亲；md 的「反酸／反胃」（见 C1、W2）正是被这一层撑起来的。
- 修法：导航「身体线」或「一句话总结」补一句「这具身体连着她瞒着家人的孩子」。

---

## 二、编（md 有、原文无）

### C1 ｜「反酸」这一症状原文没有 ｜ 档：**阻断**

- md 侧（`ch17 … .md:11`，导航「一句话概括」）：
  > `合同的回音刚到，她的胃却先开始反酸`
- 原文侧：本章原文对同一具身体只有这些词——`text/ch17_17.txt:26` `She’d suddenly started to feel a bit sick.`；`:29` `The wave of nausea seemed to abate and she stood up.` / `The nausea had returned and she didn’t want to puke …`；`:29` `she just felt rough`（`:68`）；`:83` `unsure as to whether she was going to have to run to the loo to puke or not.`
- 取证（原文全文检索，无命中）：
  ```
  /usr/bin/grep -n -iE "acid|reflux|heartburn|burn" text/ch17_17.txt
  → 无输出；退出码 1
  ```
  本书其他章节 md 从未用「反酸」（全书 54 章 md 中「反酸」仅出现在 ch17 这一行与 `00_金句精选.md:96,98`）。
- 问题：`反酸`（胃酸反流）与原文的 `nausea / sick / puke` 不是同一症状；同一份 md 自己在「一句话总结」（`md:110`）写的是「两次**反胃**、两次退下」，词汇表又把 `sick` 释为「想吐；恶心」——三处口径不一致。
- 联动（本次不判其档，属另一文件）：`00_金句精选.md:96` `这条身体线（紧张、反酸、恶心、想吐）从 ch06 一路铺到 ch29 的抽血和 ch54 那句「这里没有胎心」`、`:98` `与 ch17 里她在国家肖像馆等消息时胃里反酸、躲进洗手间那段同源`。修 ch17 时若只改 ch17，这两处会留下悬空断言。
- 修法：`反酸` → `恶心` 或 `反胃`（与其余各处统一）；并同步 `00_金句精选.md:96,98`。

### C2 ｜「走廊」是原文没有的场景 ｜ 档：提示

- md 侧（`md:44`，原句 4「为什么这样写」）：
  > `……把等待换算成了身体在走廊里的具体位置：她不是在经历什么大事件，她是在占一个位置、排在队里。`
- 原文侧：原句 4 的原文只给了两处空间——`the white porcelain bowl`（洗手间里的白瓷马桶）与 `a queue was forming outside`（洗手间外）；整章没有 `corridor` / 走廊 一词。
- 修法：`走廊` → `洗手间外`（或直接删）。

---

## 三、错（两边都有但不一致）

### W1 ｜「临摹」与原文明确否定句冲突，且与本章自己的分析冲突 ｜ 档：**阻断**

- 原文侧（`text/ch17_17.txt:20`，逐字）：
  > `Callie had been sitting in front of a portrait of Elizabeth I for the last half an hour. She had her sketchbook out. She wasn’t copying the image of the golden-age queen, she was just picking out the details that she liked.`
- md 侧：
  - `md:11`（导航「一句话概括」）：`卡莉在国家肖像馆临摹伊丽莎白一世的画像`
  - `md:110`（一句话总结）：`卡莉在国家肖像馆临摹伊丽莎白一世`
  - `md:58`（原句 6 分析）：`展厅里被临摹的那位是伊丽莎白一世`
  - **但同一份 md 的** `md:21`（原句 1 中文理解）：`她并没有在临摹这位黄金时代女王的形象，只是在挑自己想要的细节`
  - **以及** `md:23`（原句 1 为什么这样写）：`作者不让她老老实实临摹，而是让她“挑选”`
- 判定：原文专门用一句 `She wasn’t copying the image of the golden-age queen` 否定「临摹」，改用 `picking out the details`；md 的中文理解层其实读对了，但两处摘要层把作者明写的否定翻了过来，且摘要与自己正文的读法互相矛盾。读者先读导航/总结、后读精读，会拿到相反的结论。
- 修法：`md:11` 与 `md:110` 的「临摹」改为「对着伊丽莎白一世的肖像挑细节速写」（原文是 `had her sketchbook out` + `picking out the details`，并非照原样复制）；`md:58` 的「被临摹的那位」可改为「被画的那位」。

### W2 ｜「两次退下」——原文只有一次消退，章末那一次根本没退 ｜ 档：**阻断**

- md 侧：
  - `md:13`（导航「线索结构」）：`身体线（恶心两次袭来又两次退下）`
  - `md:110`（一句话总结）：`而她的身体两次反胃、两次退下`
- 原文侧（逐字，`text/ch17_17.txt:29` 与 `:83`）：
  > `:26` `She’d suddenly started to feel a bit sick.`
  > `:29` `The wave of nausea seemed to abate and she stood up.`  ← **只有这一处退下**
  > `:29` `The nausea had returned and she didn’t want to puke in one of those clear plastic bags attached to a hoop that passed for a bin.`
  > `:29` `She made it home, although the cab driver couldn’t help but comment on the shade of chartreuse she’d turned.`（到家时脸色仍发绿）
  > `:83` `Pausing the recording periodically, unsure as to whether she was going to have to run to the loo to puke or not.` ← **章末仍未退**
- 判定：原文是「一次退下 + 一次卷土重来 + 章末悬而未决」，md 写成「两次退下」，把章末的开放状态抹平了。md 自己的原句 6（`md:56`）译的恰恰是悬而未决：`不确定自己会不会又要冲去洗手间去吐`——两处自相矛盾。
- 修法：`md:13` 与 `md:110` 的「两次退下」改为「一次退下、第二次一直没退」，或「身体线（恶心两次袭来，只退下一次，章末仍未退）」。

### W3 ｜排队的人被安到卡莉身上（施事／位置归属反转）｜ 档：**阻断**

- 原文侧（`text/ch17_17.txt:29`，逐字）：
  > `Callie stared at the white porcelain bowl for a moment, not sure if she was going to be sick or not. The wave of nausea seemed to abate and she stood up. Judging by the tutting, quite a queue was forming outside. She performatively flushed the empty toilet and went to wash her hands.`

  此刻卡莉**在洗手间里**（对着白瓷马桶、冲水、洗手），`a queue was forming outside` 是**别人在洗手间外排队**。
- md 侧：
  - `md:14`（导航「人物弧线」）：`到洗手间外排着队、只能对着空邮箱一遍遍伸手的卡莉` ← 主语是卡莉
  - `md:44`（原句 4 为什么这样写）：`……她不是在经历什么大事件，她是在占一个位置、排在队里。` ← 同一段里又说 `而是门外一排人都在等`
  - `md:45`（原句 4 读者视角提示）：`这个展厅里除了她还有别人在排队。` ← 又把队伍挪到展厅
- 判定：这是 R4 固定追问里的「每个动词的主语是谁 / 受事是谁」——md 把「她占了洗手间」写成「她在排队」，且同一文件三处口径互斥（排队的是她／门外一排人／展厅里的人）。四道机器探针（引语逐字、中文是中文、关键词、形态）全绿，抓不到这一类。
- 修法：`md:14` 改为「到被排队等在洗手间外的卡莉」之类；`md:44` 的「她…排在队里」改为「是她把别人排在了门外」；`md:45` 的「展厅」改「洗手间外」。

### W4 ｜「等消息的半个钟头」一段的时序与情境被写反 ｜ 档：提示（但同句含阻断级用词，见 C1）

- 原文侧（`text/ch17_17.txt:20` 与 `:23`）：
  > `:20` `Callie had been sitting in front of a portrait of Elizabeth I for the last half an hour. She had her sketchbook out.`
  > `:23` `But Callie had had enough of drawing for now. She checked her phone and saw that Mel had replied to ‘Amelia’s’ email stating that Callie was happy to take on the consultation work as long as the fee was commensurate with the short deadline and wide scope of the project.`
  > `:26` `Callie packed up her sketchbook and drawing pencils and wandered around the gallery … She’d suddenly started to feel a bit sick.`
- md 侧：
  - `md:11`：`等消息的半个钟头里坐不住：合同的回音刚到，她的胃却先开始反酸`
  - `md:110`：`等消息的半个钟头里从从容容地挑细节走到坐立不安`
- 三处对不上：
  1. 那半小时是在画像前**坐着画**（`had been sitting … for the last half an hour. She had her sketchbook out.`），不是「坐不住」；而且同份 md 的 `md:110` 又说这半小时是「从从容容地挑细节」，与 `md:11` 自相矛盾。
  2. 原文顺序是**先**查到梅尔的回信（`md` 的 `md:28` 自己译得对：`发现梅尔已经回复了“阿米莉亚”的邮件`），**后**在展厅里犯恶心；`md:11` 的「胃却先开始」把先后倒过来了。
  3. 「合同的回音刚到」——原文没给到达时刻，只说查手机时它已经在那儿。
- 修法：`md:11` 与 `md:110` 的「等消息的半个钟头里」改为「画了半个钟头、查手机看到回信之后」；「坐不住」删或改为「画到画够了才起身」。

### W5 ｜「甩头发…也是掩饰」——原文无「掩饰」义 ｜ 档：提示

- md 侧（`md:37`，原句 3 为什么这样写）：
  > `前一句是卡莉还能掌控的社交动作——甩头发既是挑衅也是掩饰`
- 原文侧（`text/ch17_17.txt:26`）：
  > `A very serious-looking woman who didn’t even work there, wearing an ill-fitting cardigan (in this weather), gave her a dirty look and was ready to pounce and tell her that the flash would damage the pigments in the paintings, but she was disappointed. Callie flicked her hair in her direction when she turned abruptly to find the loos.`
- 判定：原文的动作是**轻蔑地一甩**（那位女士没等到她开闪光灯、扫兴而已），没有任何「掩饰／藏起什么」的语义。
- 修法：`也是掩饰` → `也是打发`（或删）。

### W6 ｜「失控的生理反应」与原文的行为相悖 ｜ 档：提示

- md 侧（`md:15`，导航「叙事手法」）：`把庄严的展厅布景与失控的生理反应并置`
- 原文侧：她全程在**管理**身体——`turned abruptly to find the loos`（主动找洗手间）、`The wave of nausea seemed to abate`（自己缓过来）、`She performatively flushed the empty toilet`（当众把戏做圆）。
- 修法：`失控` → `压不住的`（或 `半失控的`）。

---

## 四、交叉说明

- 引语**逐字**：6/6 全部命中原文且为连续子串，无 `…` 缝合、无跨话轮拼接；30 条词汇例句 30/30 命中本章原文。**本组无缺陷。**
- 形态：H1 `17. The National Portrait Gallery`（与原文标题一致、与本书 `# NN. 标题` 一致）；导航 5 项（`一句话概括/视角/线索结构/人物弧线/叙事手法`）与全书 54 章同名同序；子项集 = profile（`中文理解/关键词/为什么这样写/读者视角提示`）；块数 6，本书块数中位 7、区间 [5,10]，且 6 正是全书出现最多的块数（19/54 章）。**无偏离，不需写理由。**
- 「对应」类问题（引语选短／分析越出引语）见 `4-correspondence.md`，不重复计入本表。
- 本次只读不写：未改动书目录任何 md，未 `git add` / `commit`。
