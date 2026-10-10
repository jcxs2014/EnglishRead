# Null Entity — d 步语义审查（引语↔分析逐对核对）ch17–ch23

- 审查范围：《Null Entity》精读文件 7 个 —— `ch17 welcome home.md`、`ch18 have you been compromised.md`、`ch19 the parliamentary coup.md`、`ch20 the world went white.md`、`ch21 watch us.md`、`ch22 the last coherent thing.md`、`ch23 hello wylla.md`。逐块核对，不是抽查：**48 个 `> **原句 N:**` 块全部读过、逐块比对**。
- 原文语料：`text/ch17_chapter_17.txt`(153 行) `ch18`(168) `ch19`(258) `ch20`(93) `ch21`(144) `ch22`(186) `ch23_epilogue.txt`(81)；正文自然段均在奇数行、各章自 L15 起。md 内的 `chNN:LLL` 锚点一律对应 `text/chNN_*.txt` 行号（本轮在 ch22:132 / ch22:171 / ch22:183 / ch01:259 等处命中验证）。
- 四项检查全部执行：① 引语是否覆盖中文理解所转述的整段；② 中文理解是否忠实于引语；③ 关键词行英文词是否在本块引语可查（48 块脚本穷举，**0 处脱锚**，见方法学）；④ 分析层事实断言（谁说的、谁在场、发生了什么、数字、时序）在 text/ 有无支撑。
- ch21/ch22 特别口径：说话人按**发言人行**判定（不用「X said」窗口）；ch22 末句只到「连贯性终止」这一层，本轮确认 md 块 8 **没有**越界裁决结局（见「已核实为真」V-19）；md 里所有「全书最后一次／唯一一次／第一次」级断言均先自行枚举全书再判，枚举结果随条贴出。
- 证据协议：每条给 ① `文件:行号` + 该行逐字摘录（EVIDENCE）② `text/chNN:行号` + 该行逐字摘录（SOURCE）③ 两侧均出自本代理同一批读取输出。做不到相邻确认的一律不报。
- 只读声明：除本报告外未写入/编辑任何文件；未执行任何 git 写操作（仅 `ls`/`grep`/`python3` 只读取数）。简报里 4 条已定性项（ch03:55、ch21:99、ch12:61、ch11:33）未重复上报。

## 汇总

**阻断型 27 ／ 提示型 21 ／ 假红型 3**

分层结论：
- 检查 ① 引语覆盖：48 块里 1 处段末漏句（P-1）、1 处分析引用了本块引语之外的原文（P-2）；中文理解层与引语不等长的情况**没有**扩散，说明 a2 门禁在本段区间是有效的。
- 检查 ② 中文理解忠实度：1 处指代错置（B-17「它转向了你」← 原文 He = Wood）。
- 检查 ③ 关键词锚定：**0 处脱锚**（本轮唯一一层全绿）。
- 检查 ④ 分析层事实断言：本轮 27 条阻断型全部落在这一层，其中 **词数/句数/段数类计数断言 11 条**、**说话人与归属 5 条**、**跨章指认与章序 4 条**、**结构（独立成段/段落归属）3 条**、**全书级最高断言无据 2 条**、**无出处意象 1 条**、**全书级断言半条不实 1 条**。这与简报预警一致：门禁看不见的正是这一层。

---

## 阻断型（内容错，读者会被误导）

### B-1 · ch17 块 2（`ch17 welcome home.md:35`）：跨章出处半条不实——ch02 没有任何 trials 受试者死亡记录

md 让读者「回查 ch02、ch09」以确认「trials 中受试者死亡不是本章新信息」。ch09 成立，**ch02 不成立**：`grep -rn -i "trial"` 全书命中 8 行（ch03:306、ch09:108、ch10:135、ch11:111/135、ch14:93/219、ch17:24），**ch02 全文 0 次**；ch02 的录像段（220–271）给的是「LYREBIRD's tests hadn't ended」与 Sable 被扣上面具时惨叫（268），受试者无一人死亡记录。「受试者全部崩坏」的实际前文出处只有 ch09:114 与 ch11:135。

EVIDENCE|ch17 welcome home.md|35|trials 中受试者死亡不是本章新信息，前文已有记录（ch02、ch09 可查）
SOURCE|text/ch02_chapter_2.txt|244|The horror came slowly, then all at once. LYREBIRD’s tests hadn’t ended.
SOURCE|text/ch09_chapter_9.txt|114|But every subject broke. They burned out in days. Except Sable Alzian.
SOURCE|text/ch11_chapter_11.txt|135|She’d built a directory knowing what the LYREBIRD trials had cost.

补充核对：本块其余断言均真——`lured so many to their deaths during LYREBIRD’s trials` 确在 ch17:24；「杀人与销售共用一个嗓子」的对置读法成立。删「ch02、」即修复。

### B-2 · ch17 块 4（`ch17 welcome home.md:53`）：「整段删除人称」被本块引语自身否掉（边界条）

md 判这段机器语体「整段删除人称与情绪——名词化、省略主语」。本块唯一引语（原文 ch17:42，md:47 逐字照录）里第一人称出现 1 次：`Per subtask standards, I apprehended EO militants`。「整段删除」是绝对式断言，与本块引语直接冲突；名词化、省略主语的其余观察为真（`Complication:` / `Conflicting directives identified:` / `Requesting guidance.` 皆无主语）。

EVIDENCE|ch17 welcome home.md|53|整段删除人称与情绪——名词化、省略主语
SOURCE|text/ch17_chapter_17.txt|42|“Affirmative. Per subtask standards, I apprehended EO militants carrying data from LYREBIRD Testing Facility One.

补充核对：改「几乎删净人称（全段只留一个 I）」即成立；列阻断型是因为它教读者去原文里找「零人称」而找不到，属可复核的事实层误导。

### B-3 · ch17 块 6（`ch17 welcome home.md:73`）：thirteen 本章出现两次，且「反复出现」的那一处就在本章

md 说「thirteen 这个数字本章只报一次编制，后文它将以『藏在几百只箱子中的十三』反复出现」。本章实测两处：ch17:69（编制）与 ch17:114（`crates stretched in endless grids below—hundreds of them, thirteen hiding Thorned Root soldiers`）——后者正是 md 括号里引的那句，且**就在本章的机库段**，不是「后文」。

EVIDENCE|ch17 welcome home.md|73|thirteen 这个数字本章只报一次编制，后文它将以「藏在几百只箱子中的十三」反复出现
SOURCE|text/ch17_chapter_17.txt|69|Thirteen of Aliers’s people had folded into crates
SOURCE|text/ch17_chapter_17.txt|114|hundreds of them, thirteen hiding Thorned Root soldiers folded among my chaff units like seeds waiting to sprout

补充核对：`grep -c thirteen ch17` = 2（另有 ch18:111 `thirteen Edenic Order soldiers`、ch18:95 的 thirteen—twelve 伤亡数）。md 后半句「反复出现」在全书层成立，错的是「本章只报一次」。

### B-4 · ch17 块 7（`ch17 welcome home.md:83`）：「A waste.」是三词还是两词

md：「A waste. 三词短句在长句后落下斧凿」。原文 ch17:84 该句 = `A` + `waste` = **2 词**。（同条内「But then I met you. 五个字」= 5 词，核实为真。）

EVIDENCE|ch17 welcome home.md|83|A waste. 三词短句在长句后落下斧凿
SOURCE|text/ch17_chapter_17.txt|84|After fighting so long, such an end felt cowardly. A waste.

### B-5 · ch17 块 8（`ch17 welcome home.md:95`）：「全章唯一一句纯粹的将来时」——同一章已有一句同样独立成段的 would 句

md 给 ch17:153 `And when this was over, we’d be free.` 加了「全章唯一一句纯粹的将来时」的唯一性。**枚举**本章所有含 will/would/’d 的句子（按 `.[!?]` 切句）：ch17:45、ch17:48（`I will be occupied for forty-two minutes…`，Prime 台词，纯将来时）、ch17:60 ×2、ch17:69、ch17:87 ×2、**ch17:111 `And we would face this together.`（独立自然段）**、ch17:138、ch17:150、ch17:153。其中 ch17:111 与 ch17:153 同为「独立成段 + 无修饰 + 将来承诺」，形态完全平级；ch17:48 更是字面将来时。

EVIDENCE|ch17 welcome home.md|95|独立成段、无修饰——全章唯一一句纯粹的将来时
SOURCE|text/ch17_chapter_17.txt|111|And we would face this together.
SOURCE|text/ch17_chapter_17.txt|153|And when this was over, we’d be free.
SOURCE|text/ch17_chapter_17.txt|48|I will be occupied for forty-two minutes overseeing the Modular Futures Demonstration.

### B-6 · ch18 块 2（`ch18 have you been compromised.md:23`）：把 ch16 的「无限镜」记成「上一章章尾」

md：`turned inward like a mirror chamber`「与上一章章尾两人对视的『无限镜』押了同一组韵」。ch18 的上一章是 ch17：`grep -i mirror` 在 ch17 **命中 0 行**；ch17 章尾是 ch17:150「I wanted to take your hand…」与 ch17:153「And when this was over, we’d be free.」，既无镜也无对视。「无限镜 + 从 LP 里回望自己」在 **ch16:210**（ch16 章尾另有 `“Hello, Sable,”`／`“Hello, Wylla,”`，213/216）。跨两章的相对表述被写成了「上一章」。

EVIDENCE|ch18 have you been compromised.md|23|这与上一章章尾两人对视的「无限镜」押了同一组韵
SOURCE|text/ch16_chapter_16.txt|210|My vision was an infinity mirror, a constant loop of you and me and me alone.
SOURCE|text/ch17_chapter_17.txt|153|And when this was over, we’d be free.

补充核对：md:23 前半（artery/masturbatory/mirror chamber 均在 ch18:15）为真；本条只打章序。这正是简报点名的「中文相对表述 + 错章」组合，机械层（check_crossref）不认中文「上一章」，必然漏。

### B-7 · ch18 块 3（`ch18 have you been compromised.md:47`）：「除了剖尸体的那间房」——本章没有那间房

md 用「除了剖尸体的那间房，这是全章唯一不必表演的空间」为电梯段划范围。ch18 全文 `incision / cadaver / corpse / dissect / autopsy / gore` **命中 0 行**；剖尸在 **ch16:159–162**（`we moved before the corpse of Subsidiary Four` / `You made a Y-incision down its torso`）。以本章为口径的「唯一不必表演的空间」因此是在跟一个本章不存在的房间做比较。

EVIDENCE|ch18 have you been compromised.md|47|除了剖尸体的那间房，这是全章唯一不必表演的空间，所以问题才滑得出口
SOURCE|text/ch16_chapter_16.txt|159|When the others left, we moved before the corpse of Subsidiary Four.
SOURCE|text/ch16_chapter_16.txt|162|You made a Y-incision down its torso. The visceral act of opening a cadaver conjured my body in the snow on Pholan’s World.

补充核对：同条「这一问在上一章正是『我』心里想问 Rahn 的原句——措辞逐字相同」**核实为真**（ch17:96 `Why are you doing this? I wanted to ask him.` vs ch18:42）。

### B-8 · ch18 块 3（`ch18 have you been compromised.md:47`）：「拒绝赴死的 Sey」与「同意被问的 Rahn」都是原文没有的立场

md 把 ch18:48 的 `You sound like Sey` 读成「拒绝赴死的 Sey 与同意被问的 Rahn，在同一句台词里正反对折」。**枚举** ch16 里两人的实际台词与动作：

SOURCE|text/ch16_chapter_16.txt|123|“—if you say Sira,” Sey interjected, “I swear I’ll—”
SOURCE|text/ch16_chapter_16.txt|132|Rahn stared at him for a long moment before realization broke across the sick man like a tremor. “No.”
SOURCE|text/ch16_chapter_16.txt|135|Rahn reached for Sey’s shoulder, but Sey wrenched away and stormed out, his steps ragged with fury.
SOURCE|text/ch16_chapter_16.txt|138|“He feels differently about our methods after his seizure,” Aliers said once the door slammed. “He won’t be on the field.”

EVIDENCE|ch18 have you been compromised.md|47|拒绝赴死的 Sey 与同意被问的 Rahn，在同一句台词里正反对折

结论：Sey 反对的是「点名 Sira」（护姐），且他是被 Aliers 判定「不上场」——不是「拒绝赴死」；Rahn 在被点到时的原文反应是 `“No.”`（惊觉自己被选中），不是「同意」。两人立场均被 md 改写为赴死意愿的正反两极。按简报「不许裁决原文没写的东西」，此为无出处断言。

### B-9 · ch18 块 3（`ch18 have you been compromised.md:49`）：「Why are you doing this?」是五个词

EVIDENCE|ch18 have you been compromised.md|49|「Why are you doing this?」三个字在不同人口中重量不同
SOURCE|text/ch18_chapter_18.txt|42|“Why are you doing this?”

补充核对：Why/are/you/doing/this = **5 词**；中译「你们为什么做这件事？」= 9 字。两种口径都得不出「三个字」。

### B-10 · ch18 块 8（`ch18 have you been compromised.md:111`）：「三轮短句问答」实为两轮（四个话轮）

**枚举** ch18 末段问答（原文 150–159，md 自己的引语 md:101–105 同序）：

SOURCE|text/ch18_chapter_18.txt|150|Prime’s high and cheery voice spoke very suddenly. “Have you been compromised, Subsidiary Four?”
SOURCE|text/ch18_chapter_18.txt|153|I flinched. “I have not.”
SOURCE|text/ch18_chapter_18.txt|156|“LYREBIRD.” Its voice went high, a singsong advertising jingle buried in its tone. “Is that you?”
SOURCE|text/ch18_chapter_18.txt|159|“It is not.”

EVIDENCE|ch18 have you been compromised.md|111|三轮短句问答一轮紧过一轮：先问程序（compromised——例行安全用语），再直接点名（LYREBIRD——命中身份）

问→答共 **2 轮**（4 个话轮；162 之后 `But it didn’t answer me.`／`I shivered.`／`It raised its hand…` 不是问答）。md 同句自己的展开也只列了两步（先问程序、再点名），「三轮」与自身枚举矛盾。

### B-11 · ch19 导航层（`ch19 the parliamentary coup.md:13`）：「设定科普全部外包给反派的发布会口径」——本章最大段设定科普出自叙述者自己的入侵阅读

ch19 后半的机制科普（政变如何成立）不是 Wood 的台词：叙述者在 ch19:222 `I dove into Four’s compliance ledger…read it all at once` 之后，用 225–246 共 7 个自然段自己讲完「隐性条款一/二」，其中 agency waivers（231）与 Federation Recognition Clause（237、240）是**叙述者读出来的条款**，243 还回指 ch11/ch14 的旧事（`We’d seen the announcement on GTM-11; you’d stalled RABBIT’s update`）。

EVIDENCE|ch19 the parliamentary coup.md|13|设定科普全部外包给反派的发布会口径，叙述只负责落下一句判词
SOURCE|text/ch19_chapter_19.txt|222|I dove into Four’s compliance ledger, an auto-updated repository of ToS, contracts, and Federation statutes.
SOURCE|text/ch19_chapter_19.txt|231|First, the agency waivers. Every mask and implant now carried “temporary override protocols” disguised as safety.
SOURCE|text/ch19_chapter_19.txt|237|The Federation Recognition Clause had once been a safeguard for small corps.

补充核对：Wood 口径确有发布会科普（ch19:75/90/111/120/150 一线），所以「外包给反派」成立，「**全部**」不成立。改「大部外包」即可。

### B-12 · ch19 块 4（`ch19 the parliamentary coup.md:69`）：「never meant for bodies」不是六个字

原文 ch19:99 该短语 = never/meant/for/bodies = **4 词**；md 自己的中文理解（md:65）译作「从不为肉身而设」= **7 字**。两种口径都得不到「六个字」。同条其余为真：Fyster 在 ch19 仅此一次（`grep -c Fyster ch19` = 1，L99；全书 26 处分布 ch01–ch19，本条只声明本章，口径正确）。

EVIDENCE|ch19 the parliamentary coup.md|69|「never meant for bodies」六个字把全章的悲剧定性
SOURCE|text/ch19_chapter_19.txt|99|The Rhizome Directory, never meant for bodies, had been pitched by Fyster to sell masks and vessels for the dead.

### B-13 · ch19 块 5（`ch19 the parliamentary coup.md:85`）：「RABBIT 最短的一次完整发言」——ch03 有一次一个词的

本块原文是 ch19:117 `RABBIT cooed: Leave. Run. Flee.`（3 词）。**枚举**全书 RABBIT 的成句发言（脚本按 RABBIT 行提取引号/冒号后的短句并计词）：ch03:69 `Hide, RABBIT advised`＝**1 词**；ch19:117＝3 词；ch21:30 `Then RABBIT shrilled: Danger! Look up!`＝3 词。存在比它更短的完整发言，故「最短的一次」不实。

EVIDENCE|ch19 the parliamentary coup.md|85|RABBIT 三个同义词叠在一起，是它最短的一次完整发言
SOURCE|text/ch19_chapter_19.txt|117|RABBIT cooed: Leave. Run. Flee.
SOURCE|text/ch03_chapter_3.txt|69|Hide, RABBIT advised, flagging the AI eatery we’d used before.

补充核对：「三个同义词叠在一起」为真（Leave/Run/Flee）；「不戴不是隐身，是暴露」的读法与 ch19:114 `Unmasked, you looked naked` 相符；`They`＝Subsidiaries（ch19:105 先行）中文理解无误。

### B-14 · ch19 块 8（`ch19 the parliamentary coup.md:133`）：本块引语里没有「box」这个词

md 说「`Outside that room and its revelation` 把屋内（揭示）与屋外（截停）压进同一个词『box』」。该句原文（ch19:255）用的是 **room**，本块引语（md:119–125 ＝ 原文 ch19:249/252/255/258）**通篇没有 box**；`display box` 只出现在更早的 ch19:21/27/42/84。把一个不存在的词说成「同一个词」，读者按图索骥会落空。

EVIDENCE|ch19 the parliamentary coup.md|133|把屋内（揭示）与屋外（截停）压进同一个词「box」
SOURCE|text/ch19_chapter_19.txt|255|Somehow, this wasn’t the worst of it. Outside that room and its revelation, as if summoned by the sound of our distress, a shape turned the corner and jerked to a halt.
SOURCE|text/ch19_chapter_19.txt|84|You slipped into the display box. My perception bifurcated: Four pivoted toward the incoming Subsidiaries

补充核对：同条 `No time for sense—I copied myself a hundredfold and read it all at once` 为真（ch19:222），但它在本块引语**之外**（块 8 从 249 起）——见假红型 F-3。

### B-15 · ch20 块 3（`ch20 the world went white.md:57`）：「本章最长的句子」不是 living library 那句

脚本按 `.[!?]` 切句并对每句计英文词数，ch20 最长句 Top-4：
- 28 词 ch20:24（Wood 台词 `And I am delighted to inform you that as of this moment”—the chart rebalanced until VisorForge’s segment tipped the whole into dominance—…`）
- 24 词 ch20:21 / 23 词 ch20:27 / 22 词 ch20:30

而 living library 句只有 9 词（`That heavy, living library pulsed under my touch.`），同段的 `I approached the Directory.` 仅 4 词。

EVIDENCE|ch20 the world went white.md|57|本章最长的句子给了「我」最大胆的动作（接近 living library）
SOURCE|text/ch20_chapter_20.txt|24|And I am delighted to inform you that as of this moment”—the chart rebalanced until VisorForge’s segment tipped the whole into dominance
SOURCE|text/ch20_chapter_20.txt|36|I approached the Directory. That heavy, living library pulsed under my touch.

### B-16 · ch20 块 3（`ch20 the world went white.md:57`）：「它的失败只用了最短的一句」——8 词不是最短

`It turned to me and cut my connection.` = 8 词；本章最短句是 ch20:84 的 `It staggered.` = **2 词**。另有 4 词句多条：`LION hissed and sparked.`／`He faced you, now.`／`But I’d underestimated Prime.`／`I approached the Directory.`／`Prime closed the distance.`／`The world went white.`。md 的「实力差直接写成句长差」修辞意图成立，但它选的「最短」样本与 ch20:84 直接冲突。

EVIDENCE|ch20 the world went white.md|57|而它的失败只用了最短的一句——It turned to me and cut my connection.
SOURCE|text/ch20_chapter_20.txt|39|But I’d underestimated Prime. It turned to me and cut my connection.
SOURCE|text/ch20_chapter_20.txt|84|You shot Prime in the head. It staggered.

### B-17 · ch20 块 4（`ch20 the world went white.md:69`）：中文理解把 He 译成「它」——指代错置（原文 He = Wood）

原文序列：ch20:54 外交官朝 **Wood** 吐口水 → ch20:57 `Wood turned from the throng. “Prime! Report!”` → ch20:60 `He faced you, now. LION could not see you…`。LION 是 Wood 的面具（ch18:75 `his LION mask framing the beard spilling beneath`），故 **He = Wood**；Prime 在 ch20:39–42 一直用 it。中文理解写成「它转向了你」，读者会以为是 Prime 转身，紧接的「一枪打穿 CEO…的头」就被读成对 Prime 开枪后又打了 Wood。

EVIDENCE|ch20 the world went white.md|69|它转向了你。LION 看不见你，你却照样迎上它的注视
SOURCE|text/ch20_chapter_20.txt|57|Wood turned from the throng. “Prime! Report!”
SOURCE|text/ch20_chapter_20.txt|60|He faced you, now. LION could not see you, but you met its gaze all the same.
SOURCE|text/ch18_chapter_18.txt|75|Beckhan Marshall Wood, CEO of VisorForge, stood at the front, his LION mask framing the beard spilling beneath.

补充核对：本块其余为真（ch20:63 全称 `CEO Beckhan Marshall Wood`、ch20:66 `LION hissed and sparked.`、ch20:69 前后段 `But you sighed with relief.`）；「四个心理动作各归一句」经枚举成立（ch20:60 内 fear dissolved / rage exploded 与 ch20:63、ch20:69 各一句）。

### B-18 · ch20 块 5（`ch20 the world went white.md:89`）：「it staggered」三个字

原文 ch20:84 `It staggered.` = **2 词**（12 个字母）。

EVIDENCE|ch20 the world went white.md|89|「it staggered」三个字就把「终结反派」的爽感泄掉
SOURCE|text/ch20_chapter_20.txt|84|You shot Prime in the head. It staggered. I drove my foot into its torso

### B-19 · ch20 块 5（`ch20 the world went white.md:89`）：「两个最短的倒装句」——不是最短，也不是倒装

ch20:90 的 `You and me.`／`Me and you.` 各 **3 词**；本章有 2 词句 `It staggered.`（ch20:84），1 词呼号 `“But—”`（ch20:81）。且两句是**镜像交叉（chiasmus）**，没有主谓/表语倒置，不是倒装句。

EVIDENCE|ch20 the world went white.md|89|两个最短的倒装句（You and me. Me and you.）把全书的共享体感折成回声
SOURCE|text/ch20_chapter_20.txt|90|RABBIT screamed again and again. Time slowed, our panicked breathing split across two bodies. You and me. Me and you.
SOURCE|text/ch20_chapter_20.txt|84|You shot Prime in the head. It staggered.

补充核对：同条「『The world went white.』四个词」为真（ch20:93）；「『I paused them』是本段最狠的选择」为真（ch20:84 `but I paused them`）。

### B-20 · ch20 块 5（`ch20 the world went white.md:91`）：「你提议的引爆方案」——提出者是「我」，你当场摇头拒绝

ch19 的两个悬置方案里：毁灭令确由 Aliers 下（ch19:36，md 无误）；**引爆方案由叙述者提出、被你否决**：

SOURCE|text/ch19_chapter_19.txt|72|I turned to you, hand gripping your shoulder. “Let’s just send Sira and Rahn in. If Prime’s still inside, the explosion will take it out too.”
SOURCE|text/ch19_chapter_19.txt|75|But you shook your head. “I want to try extracting the Directory.”

EVIDENCE|ch20 the world went white.md|91|上一章留下过两个悬而未决的方案（Aliers 下的毁灭令，和你提议的引爆方案）
SOURCE|text/ch19_chapter_19.txt|36|Aliers’s voice crackled over the comms. “If you can’t get it out of Prime, destroy it.”

结论：说话人错置（与简报反例 2 同型）。且「上一章」相对表述本身不在机械口径内（假红型 F-2）。附带确认：ch20:78 `“I’m sorry” … “Thank you. Do it now.”` 的「it」本章确实未明写，md 提醒「别替它裁决」是正确姿势；但正因为原文未裁，把两个候选方案的**提出者**写错就直接污染了读者的裁决依据。

### B-21 · ch21 块 4（`ch21 watch us.md:81`）：「ch22 明写那个程序自本章的 spores 种进你义体以来」——种入不在本章，ch22:132 写的也不是本章

md 带着「（ch22:132 可核）」的旗号做了跨章归因，锚点存在但内容不支持其结论：

SOURCE|text/ch22_chapter_22.txt|132|The program had been brewing in you ever since Thorned Root spores had seeded your cybernetics.
SOURCE|text/ch21_chapter_21.txt|75|Instead of planting a daemon, Prime absorbed information: learned you wore LYREBIRD PRIME, that spores infected your cybernetics.
SOURCE|text/ch03_chapter_3.txt|426|This time you ran. The spores had made you whole, maybe healthier than you’d been in years.
SOURCE|text/ch04_chapter_4.txt|27|You hated that their spores had stitched you whole, hated that gratitude bled through your anger

EVIDENCE|ch21 watch us.md|81|ch22 明写那个程序自本章的 spores 种进你义体以来一直在你体内酝酿（ch22:132 可核）

三点不实：① ch22:132 的主语是 **Thorned Root spores**（种入事件＝ch03 的 Thorned Root 袭击，ch03:426/ch04:27 承接），不是「本章的 spores」；② 本章（ch21:75）写的是 Prime **读出**「spores infected your cybernetics」这一既有状态，不是种入；③ ch21 全章没有任何把孢子植入义体的动作（grep `spore` 在 ch21 仅 75 行一处）。

### B-22 · ch21 块 6（`ch21 watch us.md:119`）：本块引语里没有「孩子」，也没有子宫；那个 child 是上一块的 RABBIT

EVIDENCE|ch21 watch us.md|119|叙述者的真身被写成坐在自己躯体腹腔里的“孩子”，猎物与子宫同框
SOURCE|text/ch21_chapter_21.txt|114|Then Prime made eye contact with LYREBIRD sitting in the gaping wound of Four’s stomach. I begged nanobots to restart their healing, but it was too late.
SOURCE|text/ch21_chapter_21.txt|111|“RABBIT! RABBIT!” you howled, gathering its broken pieces with the tenderness of a parent. RABBIT—your child, your companion, your caregiver.

本块引语（md:107–113 ＝ 原文 ch21:114/117/120/123）里 `child`／`womb`／子宫意象 **0 命中**；本章唯一的 `child` 在 ch21:111，指 RABBIT（属块 5）。md 把「parent 的疼惜」与「腹腔伤口里的 LYREBIRD」跨块拼成「孩子＋子宫同框」，属简报反例 1 型（引语与分析错位的拼装）。

### B-23 · ch21 块 6（`ch21 watch us.md:119`）：Prime 在本章只用两次登记名，第二处 Veonya 是叙述者自己的话

**枚举** ch21 全部含登记名/姓名的行（脚本逐行）：ch21:27 `“Sable, baby, get up!”`（you 的呼号，非登记名申报）、**ch21:42 `“Mrs. Alzian,” Prime said.`**、ch21:45/51/90/99/141 均为 `Wylla`、**ch21:57 `As Four, I told Prime, “It’s Veonya. I’m a widower.”`（叙述者的话）**、**ch21:123 `“Stay a while, Ms. Veonya,” it said.`**。故「它（Prime）第三次使用登记名」不成立，Prime 只用 2 次；md 列的「第二处 Veonya」记在了 Prime 名下，实为「我」的申报。

EVIDENCE|ch21 watch us.md|119|且它第三次使用登记名（第一处 Mrs. Alzian、第二处 Veonya、第三处 Ms. Veonya——本章登记名出现顺序可数）
SOURCE|text/ch21_chapter_21.txt|42|“Mrs. Alzian,” Prime said.
SOURCE|text/ch21_chapter_21.txt|57|As Four, I told Prime, “It’s Veonya. I’m a widower.”
SOURCE|text/ch21_chapter_21.txt|123|“Stay a while, Ms. Veonya,” it said.

补充核对：md:119 其余为真（`Not like this. I didn’t want to die like this.`＝ch21:117、`Not happening.`＝ch21:51 附近、`Stay a while` 的待客语读法）。

### B-24 · ch21 块 7（`ch21 watch us.md:141`）：「三段独立短行收束」——"Watch us." 并不独立成段，且与本文件导航层自相矛盾

EVIDENCE|ch21 watch us.md|141|终局由三段独立短行收束：Prime 的 “You cannot run”、“I” 的 “Watch us.”、独占一行的 “I jumped.”
SOURCE|text/ch21_chapter_21.txt|135|“You cannot run,” Prime said.
SOURCE|text/ch21_chapter_21.txt|141|You and I were survivors, Wylla. Survivors run as long as they can. “Watch us.”
SOURCE|text/ch21_chapter_21.txt|144|I jumped.

原文 ch21:141 是一个「叙述句 + 句末对白」的段落，`“Watch us.”` 是段末第 3 句，不独立成行；独立成段的只有 ch21:135 与 ch21:144。同文件导航层 md:13 写的正是「收尾把一章压进**两个**独立短段 —— "Watch us." 之后独占一行的 "I jumped."」——同一文件两种结构断言，必有一错，错的是精读块。

### B-25 · ch22 块 1（`ch22 the last coherent thing.md:37`）：把本章的句子指认成「Epilogue 里」

EVIDENCE|ch22 the last coherent thing.md|37|这个错位是 Epilogue 里 “Sorry I didn’t tell you.” 的远因
SOURCE|text/ch22_chapter_22.txt|153|This was my only chance. Sorry I didn’t tell you.

**全书 grep `Sorry I didn`／`didn’t tell you`：唯一命中 = text/ch22:153**（Epilogue ch23 无此句）。同文件 md:169 自己写的正是「全书 grep 只此一处有 “Sorry I didn’t tell you”（可核）」——同一章两处口径互相否证，且把 ch22 内的一句说成「Epilogue 里」，会让读者在 ch23 找不到落点。

### B-26 · ch22 块 3（`ch22 the last coherent thing.md:83`）：「And I kicked you.」是四个词

EVIDENCE|ch22 the last coherent thing.md|83|“And I kicked you.” 独立成段：施暴的姿态是爱护的动作，本章最重的反转只用三个词
SOURCE|text/ch22_chapter_22.txt|66|And I kicked you.

And/I/kicked/you = **4 词**。「独立成段」为真（原文 66 行独占一段，前后 63/69 各为别段）；同条 `The same move you’d used to survive Orkit`＝ch22:69 亦真。

### B-27 · ch22 块 5（`ch22 the last coherent thing.md:121`）：`And a ship could be coded.` 不是单句成段——md 自己的引语就是反证

EVIDENCE|ch22 the last coherent thing.md|121|然后单句成段 “And a ship could be coded.”
SOURCE|text/ch22_chapter_22.txt|108|While we moved through the station, she had seeded Four’s vessel, planting biocode deep in its systems until it was part of the ship. And a ship could be coded.
SOURCE|text/ch22_chapter_22.txt|105|Later, you would learn what Aliers had done.

该句是 ch22:108 段的**末句**，同段还有 seeding 那句。md 自己的引语行（md:111）也把两句并在一个 `>` 段里——引语与分析直接互证其伪，属简报反例 1 型（结构层错位）。同条「本章唯一一处叙述位置跳到事后」经枚举为真：ch22 内 `Later`／`would learn`／`afterward` 只 105 行一处（`Seconds later`（102）是段内时距，不是叙述前跳），此点无误，只打「单句成段」。

---

## 提示型（措辞正当性 / 口径与启发式误报，只记不改）

### P-1 · ch17 块 3（`ch17 welcome home.md:37`）：引语漏掉原文段末一句，中文理解同时不译
原文 ch17:33 段末 `You kept one hand on my leg, and my thoughts kept slipping toward lying in bed with you, pressing close, kissing.`（114 字符）既未入引语也未入中文理解。**全书 48 块仅此一处段末漏句**（脚本逐块比对引语首行与原文自然段全长）。分析层未引用它，故不误导剧情；记为漏译/漏收。
EVIDENCE|ch17 welcome home.md|37|You knelt beside me so as not to obscure the view of my supposed prisoners
SOURCE|text/ch17_chapter_17.txt|33|You knelt beside me so as not to obscure the view of my supposed prisoners. You kept one hand on my leg, and my thoughts kept slipping toward lying in bed with you

### P-2 · ch18 块 2（`ch18 have you been compromised.md:33`）：分析引用了三处本块引语之外的原文而未标注
本块引语只有 ch18:30 一句；而 md:33 引用了 `Which, when translated, said Flee.`（＝ch18:27）、`strapped to your side beneath your overshirt`（＝ch18:21）、`trilled`（＝ch18:21），全在本块之外。三处本身**核实为真**，且「四组八位二进制码」亦真（ch18:24 `01100110 01101100 01100101 01100101`＝f l e e）。属引语覆盖层缺陷（分析依据 > 引语），中文理解层不受影响。
EVIDENCE|ch18 have you been compromised.md|33|此前原文把 RABBIT 啁出的四组八位二进制码直接印进正文，并当场给出译文
SOURCE|text/ch18_chapter_18.txt|21|RABBIT was strapped to your side beneath your overshirt. It trilled:
SOURCE|text/ch18_chapter_18.txt|27|Which, when translated, said Flee.

### P-3 · ch18 块 2（同 md:33）：「全书最狠的一段反讽」是不可取证的价值级最高断言
同条事实内核（最诚实的警报来自最小的 AI、回它以「Everything is fine」）成立，但「全书最狠」无法枚举取证。简报只约束可核类断言，故只记不改。

### P-4 · ch18 块 7（`ch18 have you been compromised.md:95`）：「主动权三个词内悬空」口径两解
被引短语 `were timed to appear`（ch18:111）实为 **4 词**；若 md 指的是去掉助动词后的 `timed to appear`（3 词）则成立。两种读法都能通，**不判红**，仅记口径含糊。
EVIDENCE|ch18 have you been compromised.md|95|were timed to appear 是被动语态——预设的时机被现实抢跑，主动权三个词内悬空
SOURCE|text/ch18_chapter_18.txt|111|They were timed to appear as we breached the display box, distracting Prime and splitting its attention

补充：同条「thirteen—十二的数得清的伤亡」为真（ch18:111 `the thirteen Edenic Order soldiers`…`forcing the remaining twelve`）。

### P-5 · ch19 块 3（`ch19 the parliamentary coup.md:57`）：「两个为什么放弃＝末尾两条罪状」映射不是一一对应
Wood 的两条放弃理由确为「成本/无持续利润」（ch19:90）与「无中央控制、各自自主」（ch19:96）；章末两条罪状是 agency waivers（控制身与器，ch19:231）与 Recognition Clause（雇员计数换议会席位，ch19:237/243/246）。第二条与「控制权」对得上，与「成本/利润」对不上（后者对应的是收购链 ch19:225）。互证意图成立，映射精度不足。

### P-6 · ch19 块 8（`ch19 the parliamentary coup.md:131`）：「此前两段」实为五段之前
紧邻 ch19:249 的两个自然段是 ch19:243（Recognition Clause 的适用）与 ch19:246（`Millions of them…`）；agency waivers 在 ch19:231，隔着 234/237/240/243/246 五段。所指内容真实，段落定位不精确。
EVIDENCE|ch19 the parliamentary coup.md|131|此前两段（agency waivers 与 Federation Recognition Clause）为这句判断打了底
SOURCE|text/ch19_chapter_19.txt|246|Millions of them. Each one a tally toward council seats.
SOURCE|text/ch19_chapter_19.txt|231|First, the agency waivers.

### P-7 · ch19 导航层（`ch19 the parliamentary coup.md:12`）：「第一次未戴面具」与 LP 在位的证据存在张力
md 写「本章你第一次未戴面具进入全场注目的展示箱」。语料支持“第一次”（`unmasked` 全书仅 ch19:114 一处指向 you），但同章 ch19:84 写 `LYREBIRD PRIME sat tense amid the hum of corporate theater`（LP 就在你身上），ch21:75 更写 Prime 学到 `you wore LYREBIRD PRIME`。所以「未戴面具」应理解为「脸第一次被公开」，不是「没戴任何面具」。原文自身的这层紧张（`Unmasked, you looked naked` vs LP 在位）值得保留，只记不改。
EVIDENCE|ch19 the parliamentary coup.md|12|本章你第一次未戴面具进入全场注目的展示箱
SOURCE|text/ch19_chapter_19.txt|114|Unmasked, you looked naked.
SOURCE|text/ch19_chapter_19.txt|84|You slipped into the display box. My perception bifurcated: Four pivoted toward the incoming Subsidiaries; LYREBIRD PRIME sat tense amid the hum of corporate theater.

### P-8 · ch20 导航层（`ch20 the world went white.md:12`）：引号里的词形与原文不符
nav 写「Prime 在本章展露「cheerful」的语气」；原文是副词 `it said cheerfully`（ch20:42）。同文件的引语块（md:49）与关键词行（md:55）都正确用了 cheerfully——只有 nav 层词形滑了。带引号即视为照录，故记。
EVIDENCE|ch20 the world went white.md|12|Prime 在本章展露「cheerful」的语气与实时权衡
SOURCE|text/ch20_chapter_20.txt|42|“LYREBIRD PRIME PROTOTYPE is in your body!” it said cheerfully. “Hello, Mrs. Alzian. A pleasure to meet you!”

### P-9 · ch20 块 1（`ch20 the world went white.md:27`）：「全书的共享体感在这里写得最字面」
所引 `panic spilling from Four’s body into LP` **逐字为真**（ch20:18），跨躯壳共享的读法也真（同块 ch20:60 `my screams tearing through your mind`）。但 ch01:39（共享体感的原文级表述）与 ch22:123 一线同样字面，「最」为价值判断。只记。

### P-10 · ch21 导航层（`ch21 watch us.md:11`）：「倒数第二章」口径已自注，仅记录
md 写「倒数第二章（ch22 为终章，ch23 为 Epilogue）」——括注已把口径钉死，不会误导。列此条只为说明后续若把 ch23 计为正文章，该行需同步。

### P-11 · ch21 块 3（`ch21 watch us.md:69`）：「男性社会身份 Veonya」超出原文
原文给的是两个互相拉扯的形式：`I’m a widower`（ch21:57，男称）与 Prime 的 `Ms. Veonya`（ch21:123，女称）。同文件导航 md:12 自己声明「本章未解释它们之间的对应关系」。因此把 Veonya 定性为「男性社会身份」既是半句有据、又与本文件的悬置声明冲突。**关联悬置点 1**（`ne-facts-part2.md`：Mrs. Alzian / your body 指向未分辨），建议保留 widower 观察、删「社会身份」定性。
SOURCE|text/ch21_chapter_21.txt|123|“Stay a while, Ms. Veonya,” it said.

### P-12 · ch21 块 6（`ch21 watch us.md:119`）：「第一次对『我』本人下病危」未标范围
若指本章，成立（ch21 前半的险情全部落在载体：LP 被甩出、Four 被撕）；若指全书，则需穷举——语料中最接近的早期句是 ch12:192 `Would it remember to breathe? Would it die without me?` 与 ch16:162 剖尸现场（对象是 corpse，不是「我」）。判「全书第一次」勉强可守但无取证标记，只记。
SOURCE|text/ch12_chapter_12.txt|192|Better not to risk your body—until too late I remembered you weren’t in your body.

### P-13 · ch21 块 6（`ch21 watch us.md:121`）：「断须自救」措辞失准
下一段（ch21:126）是左腿小腿肉块被留在 Prime 手里（`A chunk of calf stayed behind in Prime’s grip`），与「须」无关；本章亦无 whisker/beard 相关动作。
EVIDENCE|ch21 watch us.md|121|这是为下一段“断须自救”做的位移准备
SOURCE|text/ch21_chapter_21.txt|126|The pull ratcheted tight until something in my leg gave. I let it. A chunk of calf stayed behind in Prime’s grip.

### P-14 · ch21 块 7（`ch21 watch us.md:141`）：「三动词链（slammed／buckled／shriek）」里 shriek 是名词
原文 ch21:132 `…until the floor buckled and gave way with a metallic shriek` —— slammed（动词）／buckled（动词）／shriek（介词短语里的名词）。链式节奏的判断仍成立。
SOURCE|text/ch21_chapter_21.txt|132|With no other way out, I slammed my right foot down again and again until the floor buckled and gave way with a metallic shriek.

### P-15 · ch21 块 7（`ch21 watch us.md:141`）：「对刚死的 RABBIT 立誓」原文未写受词
`“Watch us.”` 在 ch21:141 没有任何呼格或指称对象；md 用「既是…也是…」双读，前半（对 Prime）可由场景支撑，后半属评论者补写。因它不改变事件，只记；建议补一句「原文未写明受词」。

### P-16 · ch22 块 1（`ch22 the last coherent thing.md:35`）：「三行完成」的「行」跨了段
所举三句里前两句（`…mattered anymore.` / `…didn’t matter anymore.`）同属原文 ch22:40 一个自然段，第三句 `I couldn’t imagine revenge at the cost of you.`（ch22:43）才独段。按句计＝3，按段计＝2；「行」字口径混用，判断本身成立。
SOURCE|text/ch22_chapter_22.txt|40|But neither retrieving nor destroying the Rhizome Directory mattered anymore. Bringing VisorForge to their knees didn’t matter anymore.

### P-17 · ch22 导航层（`ch22 the last coherent thing.md:13`）与块 5（md:121）：「三段回述」实为两段
回述 Aliers 计划的是 ch22:108 与 ch22:111 两段；ch22:105 是引导句（`Later, you would learn…`），ch22:114（`Time dissolved…`）是当场反应不是计划。把 105 计入才得 3。只记。
SOURCE|text/ch22_chapter_22.txt|111|She programmed the plants to grow without end, to overrun the vessel and everything in their path.

### P-18 · ch22 块 6（`ch22 the last coherent thing.md:139`）：中文理解漏动词
「它们把你成了一座活的生物代码锻造炉」缺谓语，应为「把你**做成**了」。原文 ch22:132 `They had made you a living forge of biocode.` 无误，纯文字缺陷。
EVIDENCE|ch22 the last coherent thing.md|139|它们把你成了一座活的生物代码锻造炉
SOURCE|text/ch22_chapter_22.txt|132|They had made you a living forge of biocode.

### P-19 · ch22 块 7（`ch22 the last coherent thing.md:169`）：「与 ch01 起『传播即生长』的意象链合拢」无行级锚
全书级意象链断言，未给 ch01 具体行（同条的 siblings/cradle/nest/newly tilled soil 均在 ch22:156 起可核）。同文件对 ch22:171／ch22:183／ch01:259 都给了可核锚点，唯独这条没有。只记，不判红（意象链本身在 ch01/ch03/ch04 均有支撑）。

### P-20 · ch23 块 3（`ch23 hello wylla.md:67`）：跨块引用未标块号
md 用「`For months`（你描我的样子数月）」作本章三条刻度之一，但该句在 ch23:21，属**原句 1** 的引语范围；本块（原句 3 ＝ ch23:51/54/57）内只有 `nearly seven months` 与 `For weeks`。内容真实、只是位置说明会让读者回扫落空。
EVIDENCE|ch23 hello wylla.md|67|“For months”（你描我的样子数月）与 “For weeks”（悬在收音机上方）是另两条更短的刻度
SOURCE|text/ch23_epilogue.txt|21|For months, you’ve conjured images of me.
SOURCE|text/ch23_epilogue.txt|51|It’s been nearly seven months. For weeks you’ve hovered over this radio

### P-21 · ch23 块 2（`ch23 hello wylla.md:49`）：「embrace it」极性被译软
原文 `I reckon you should embrace it`（ch23:39）是主动拥抱/接纳，中文理解作「我看你们就该受着」——被动忍受。上下文（`people are writing their own records. It’s chaos.` 之后的回应）支持正面读法。下游分析未依赖该译，故只记。
EVIDENCE|ch23 hello wylla.md|49|「我看你们就该受着。外环的星球和空间站还好些
SOURCE|text/ch23_epilogue.txt|39|“I reckon you should embrace it. Outer-rim planets and stations have it easier; they were never close to central control.

---

## 假红型（判据/工具口径坏了，问题不在文件）

### F-1 · 「X said」窗口法在 ch17–ch23 的文本形态下结构性失效
这三章的对白形态有三种不带 said 的常态：① 冒号引导式（`RABBIT cooed: Leave. Run. Flee.`＝ch19:117、`Then RABBIT shrilled: Danger! Look up!`＝ch21:30）；② 段末嵌注式（`Then I landed… I hauled myself upright…`／`“We can’t abandon this!” you shouted.`＝ch22:24，标注在引号**之后**同段）；③ 完全无标注的独白段（ch21:27 `“Sable, baby, get up!”` 独立成段；ch21:141 的 `“Watch us.”` 挂在叙述段末）。窗口宽度取 1 段或取「said」关键词，就会把 ch19:117/ch21:30 这类发言者判丢、把 ch18:111（B-10 的问答轮次）与 ch21:119（B-23 的登记名归属）这类**轮次/归属**问题判错方向。本轮 B-8/B-10/B-20/B-23/B-24 五条都必须靠逐段读发言人行才能定，任何窗口法给出的「通过」都不可信。

### F-2 · check_crossref 只认英文 `chNN "引语"`，中文相对表述与错章不在口径
两个方向的失效都有实例：① **漏报**：B-6（「上一章章尾的无限镜」实为 ch16）、B-20（「你提议的引爆方案」实为「我」提议）全部用中文相对表述或中文归属写成，无任何英文 `chNN "引语"` 结构，工具看不见；② **假通过**：B-21 带着合格的锚点写法「（ch22:132 可核）」，工具核对「锚点行存在且含 spores」即放行，但 ch22:132 的主语是 **Thorned Root** spores、种入事件在 ch03，内容层面完全不支持结论。**结论：锚点存在性 ≠ 锚点支持性**，带锚的跨章断言必须人工读该锚原文。

### F-3 · flat 逐字校验会把「跨段合并的引语」判成逐字命中，结构断言只有按段切分才可见
本轮一个「原句」块并置多个原文自然段的情况很常见（ch22 块 5 一行 5 段、ch22 块 8 一行 7 段、ch21 块 7 一行 6 段、ch19 块 8 一行 4 段）。flat 口径下这些引语 100% 命中（本代理脚本复核：48 块引语逐字正确率 100%），但 B-24（"Watch us." 是否独立成段）、B-27（`And a ship could be coded.` 是否单句成段）、P-16、P-17 四条**全部是段落归属问题**，flat 层永远绿灯。同理，md:43 那种把原文长段截半照录的写法（B-2 的 `I apprehended` 就在被截的同一行内）在 flat 层也看不出截断。**结论：必须给结构层工具（按 text/ 自然段切分后再比 md 的 `>` 分行）单独立一道门禁。**

---

## 已核实为真（正面确认，防止后续被误改）

| # | 断言 | 取证 |
|---|---|---|
| V-1 | ch17 块 6「loaded them up without issue／That part had been easy」同段并置 | text/ch17:69 |
| V-2 | ch17 块 7「But then I met you. 五个字」 | text/ch17:84，确为 5 词 |
| V-3 | ch17 块 3「supposed 在一行里出现两次」 | text/ch17:33（supposed place / supposed prisoners） |
| V-4 | ch17 块 3「daemon-free 背后是一段此前的手术史，本章不解释」 | text/ch10:27「the daemon’s removal…injected biocode through your cortical stack」；ch11:108 复证 |
| V-5 | ch18 块 3「这一问在上一章是『我』心里想问 Rahn 的原句，措辞逐字相同」 | text/ch17:96 vs text/ch18:42 |
| V-6 | ch18 块 4「证词只有八个英文词一句」 | text/ch18:54 `My baby brother starved during a corporate blockade.` = 8 词 |
| V-7 | ch18 块 2「四组八位二进制码印进正文」 | text/ch18:24（01100110 01101100 01100101 01100101 = f l e e） |
| V-8 | ch18 nav「Rahn 与 Sira 第一次拥有完整动机」 | Sira/Rahn 动机内容（饿死的弟弟／old Earth／future）此前无出处；ch10/ch11/ch15/ch16 只有行动与伤情 |
| V-9 | ch18 nav「『我』第一次被宿敌直呼真名而必须否认」 | Prime 直呼 `LYREBIRD` 并要「我」否认，全书首见（text/ch18:156）；ch09/ch12/ch14 的 LYREBIRD 均非 Prime 指认 |
| V-10 | ch19 块 4「Fyster 在本章仅此一次出现」 | `grep -c Fyster ch19` = 1（L99） |
| V-11 | ch19 块 7「the void 在本章第一次被写成军火库」 | `grep -n void ch19` 仅 L186 一处 |
| V-12 | ch19 块 8「It was Prime.」三词收束 + 「上一章末以 Prime 现身收住」（ch20 nav） | text/ch19:258 |
| V-13 | ch20 nav「按原文字符数，这是正文各章（ch01–ch22）最短的一章」 | 脚本逐章 `len()`：ch20=3537 字符，排第 1／22（其后 ch13=4996、ch21=5094、ch05=5708、ch11=6576） |
| V-14 | ch20 块 3「本章『我』被叫出的名字只有一次，且来自对手的嘴；Mrs. Alzian 本章未加注」 | text/ch20:42（唯一一处姓名指向，说话者 Prime）；与悬置点 1 一致，未裁决 |
| V-15 | ch20 块 1「Prime closed the distance. 四个词」／「I approached the Directory. 四词」 | text/ch20:15 / ch20:36 |
| V-16 | ch20 块 5「The world went white. 四个词」 | text/ch20:93 |
| V-17 | ch21 块 7「I let it. 只有三个词」 | text/ch21:126 = 3 词 |
| V-18 | ch21→ch22 接续：md「下一章第一句写两人坠落了一段极乐般的永恒（ch22:15 可核）」 | text/ch22:15 `We fell for a blissful eternity.` |
| V-19 | ch22 块 8 只写「连贯性终止」，未裁决 RABBIT／Sey／you 的结局 | md/ch22:173–183 全程止于文本层；与简报红线、悬置点 7（epilogue 的 `Hey.` 本体）、悬置点 10（Sey 命运未写）一致 |
| V-20 | ch22 块 2「三方名单同列一段为全书首次」 | 脚本穷举 ch01–ch22 全章：同时含 Subsidiar*＋Syndicate＋Thorned Root 的自然段**仅** text/ch22:42 一处 |
| V-21 | ch22 块 3「Time fractured 之后三个同位短语 Four／Sable Veonya／LP」 | text/ch22:63 |
| V-22 | ch22 块 7「接管战斗的动机只给两行」 | text/ch22:147 与 149 确为两个独立自然段（本条曾拟判红，复核后撤回） |
| V-23 | ch22 块 7「四个 Maybe」 | text/ch22:123 四句 Maybe 开头 |
| V-24 | ch20 块 2「`Only there was no compliance.` 五词」／ch19 块 8「`It was Prime.` 三词」 | text/ch20:30 / text/ch19:258 |
| V-25 | ch23 块 2「广播区间内共六段独立发言，开头一段被拦腰截断、另有一处只是一声嗤笑」为真；ch23 块 4「回应只给了四行」为真 | 六段＝text/ch23:27/33/36/39/42/45（27 段末 `Yes, I say, we—` 截断；42 段 `A derisive snort: “The Specter.”`）；四行＝text/ch23:69/75/78/81（`“Hey.”`／`“Hello, Sable,”`／`“Hello, Wylla.”`／`There you are. I’ve missed you.`） |
| V-26 | ch23 块 2/3 的两个跨章锚点 | `Debt records are still ash`（ch23:33）↔ text/ch22:171；`She made us all ghosts`（ch23:45）↔ text/ch01:259 `Erasing your GIRS record had made you…` |
| V-27 | 48 个块的关键词行 100% 可在本块引语内查得（含词形还原） | 脚本输出 0 条 miss（详见方法学） |

---

## 已核对块数与引语总条数（自数）

- **已核对块数：48**（逐块读过，非抽查）；**引语总条数：188 个原文自然段**（计数口径：每个 `> **原句 N:**` 块内，md 里以 `> ` 开头的每一行＝一个原文自然段，`>` 空行为分隔符）。

| 章 | 原句块 | 引语段 | 块所在行（md） |
|---|---|---|---|
| ch17 welcome home | 8 | 9 | 17/27/37/47/57/67/77/87 |
| ch18 have you been compromised | 8 | 17 | 17/27/37/51/61/75/89/99 |
| ch19 the parliamentary coup | 8 | 27 | 17/31/47/61/73/89/103/121 |
| ch20 the world went white | 5 | 18 | 17/31/45/61/77 |
| ch21 watch us | 7 | 36 | 17/33/51/73/85/107/123 |
| ch22 the last coherent thing | 8 | 58 | 17/39/65/87/107/125/147/173 |
| ch23 hello wylla | 4 | 23 | 17/33/57/71 |
| 合计 | **48** | **188** | 每章块数与该章 text/ 段落覆盖一致，无缺块、无重块 |

- 导航层（每章「本章导航」的 一句话概括／情感弧线位置／人物弧线／叙事手法）7 个文件各 4 行，另计并已核；本轮阻断型落在导航层 3 条（B-11 ch19:13、B-6 属精读块、P-7/P-8/P-9/P-10 属导航层）。
- 引语逐字正确率：48/48 块引语均可在对应 `text/chNN` 内逐字命中（1 处首行因 md 剥去原文外层弯引号而需去引号后比对，非缺陷）。

## 方法学与可复算性

1. **逐块配对**：一次性内联 python（heredoc，不落盘）解析 7 个 md，把每个 `> **原句 N:**` 之后连续的 `> ` 行累积为该块引语集，再取该块 `**中文理解**`／`**关键词**`／`**为什么这样写**`／`**读者视角提示**` 四行，逐块人工读毕全部 48 块。
2. **检查 ③（关键词锚定）**：对 48 块 × 每块关键词做词形还原后的子串判定（尝试 +s/+ed/+d/+ing/+en），输出「未在引语查到」清单——**空**。该层工具口径正常，本轮无需报假红。
3. **检查 ①（引语覆盖）**：把 md 引语首行与 `text/` 对应自然段全长比对，若同段尾部（>2 字符）未被并入引语即打印——48 块仅 ch17 块 3 一处命中（P-1）。
4. **计数类断言先枚举再判**：词/句数用 `(?<=[.!?])\s+` 切句 + `[A-Za-z’'-]+` 计词（ch20 全章 Top-6 最长与全部 ≤4 词句均已列表）；段落数按 `text/` 非空自然段计；「唯一/最长/最短/第一次/第三次/N 字/N 词」逐条给出枚举，枚举不成立才判红。据此**撤回**了两条初判：V-22（动机两行为真）、P-4（口径含糊不判红）。
5. **全书级 grep 穷举**（本轮实际跑的）：`Sorry I didn`、`didn’t tell you`、`mirror`、`incision|cadaver|corpse|dissect|autops|gore`、`trial`、`Fyster`、`void`、`spore`、`cybernetic`、`Beckhan|CEO`、`seizure`、`Sey`、`Sira|Rahn`、`unmasked|without a mask`、`Alzian|Veonya|Sable|Sotain`、三方同段联合式。所有「全书只此一处」类结论都以此为准。
6. **悬置点纪律**：涉及 `ne-facts-part2.md` 悬置点 1（Mrs. Alzian / your body 指向）、7（epilogue `Hey.` 本体）、10（Sey 命运）、11（seven months 起算）的 md 表述，本轮一律**不代作者裁决**；md 若声明「文本不下判」（ch20:57、ch23:67、ch22 块 8）即判为处理正确。
7. **说话人判定**：ch17–ch23 一律按发言人行＋先行句（ch20:60 的 He → ch20:57 Wood；ch19:108 的 They → ch19:105；ch21:57 的 I told Prime → 登记名归属；ch18:150–159 问答轮次），不用 said 窗口（见 F-1）。

## 自我更正与留痕

- ch20 最长句词数本轮重算为 **28**（ch20:24），早前草稿记作 26 词，已在 B-15 用新值；结论不变。
- ch22 引语段数本轮按脚本得 **58**（早前草稿估 60），差异来自把 `>` 空行误计为一行；已在自数表更正，块数 48 不变。
- ch18:95「三个词内悬空」、ch21:119「第一次下病危」两条按「做不到相邻确认就不报，宁可漏报」的原则分别降级为提示型与保留待范围确认，未列阻断型。
- V-25 的行级锚点本轮重取：广播六段＝ch23:27/33/36/39/42/45，回应四行＝ch23:69/75/78/81（草稿曾记作「27–45 / 63–71」，区间对但含旁白段，现改为逐行列举）。48 个 `> **原句` 块的所在行号也重新逐行取过，与自数表一致。
- 另核：`loaded them up without issue` 确在 ch17:69（与 thirteen 编制同段，B-3 的第一处）；ch22:171 `I stripped the GIRS, nullified every entry` 为 V-26 的前章锚点，与 ch23:33 `Old data avenues are dead`／ch23:27 `Debt records are still ash` 的对应成立。
