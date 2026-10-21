# 3-diff.md · ch34 漏／编／错 三张单子（独立复核）

- 被审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch34 matt breaks into a house at priory square.md`
- md 版本：sha256 `7fe50baf874f160d2da4758c5bb910a5b1097c6b3f86ab52caef1186abf2f6f1` · mtime `2026-10-21 15:09:15` · 11436 字节
- 权威源：`text/ch34_34.txt`（4503 字符 / 38 段，与 epub `OPS/s048-Chapter-034.xhtml` 逐段比对 **0 差异**）
- 机器层：`2-machine.json`（本轮对上述版本重跑 `scripts/chapter.sh --json`，**exit 0**，verdict `ok`）
- 执行者：独立复核代理（第二实例）；引用逐字抄，行号＝`text/ch34_34.txt` 行号

## 〇、版本变动记录（先读这条）

15:07 的首轮复核（主会话写的同名三件）针对的是 **15:09 之前**的 md，其 3 条阻断型缺陷——

1. 导航·视角「直到**妹妹**被赶出房间」
2. 导航·一句话概括「**逼问出**真正让她害怕的事」
3. 导航·一句话概括「**看完三处摄像头**与整套警报系统」

——在 15:09:15 的 md 里**已全部修掉**（现文为「直到**梅尔被妹妹赶出房间**」「说出真正让她发难的理由」「**听她报出**三处摄像头」），本单不再重复计。

本单只对 **15:09:15 之后的 md** 负责。下面两条新的阻断型是首轮**没有**抓到的，都落在**原句 6**（末段）——首轮把这一块判成了「属实 / 对应」。

---

## 一、漏（原文有，md 未覆盖）4 条

### 漏-1 · 马特为什么上门（本章的动机三句）｜ch34:32、35、38（字符 697–908）

- 原文逐字：
  - `‘We’ve had two break-ins on the square.’`
  - `‘And a murder or two, right?’`
  - `‘Yes, well. I just wanted to come in and talk to you about your security? We’re worried that your house may be targeted in the future.’`
- md 现状：6 个引语块**无一选取**；正文也未复述"两起入室盗窃""可能成为目标"。仅在词汇表里把 `break-ins`、`targeted` 列为词条（例句逐字 ✓）。
- 为什么算漏：这是马特敲这扇门的理由，也是女主人"安全不是问题"（ch34:41）的触发点；`And a murder or two, right?` 还是全章最见性格的一句台词（她把杀人当口头禅）。引语块 3 直接接在它后面，却不选它，等于把这一段的功能句空在块外。

### 漏-2 · 地下到底是什么：录音棚 +「我妹妹是音乐人」｜ch34:50、53（字符 1635–1892）

- 原文逐字：
  - `‘You’ve got a recording studio down here,’ Matt said, poking his head through. ‘That’s cool.’`
  - `‘My sister’s a musician,’ she said. She smiled weakly. Matt didn’t think she sounded totally pleased about that. ‘We’ve done an extensive renovation down here.’`
- md 现状：6 个引语块**无一选取**；而**原句 4 的读者视角提示**反而去讲它——「他在地窖里看的不是储藏间，而是一间刚被整理出来的私人空间」（md 行 57），越过了引语 4 的边界（引语 4 止于 `He opened the door off the space.`，录音棚在下一段 ch34:50）。
- 为什么算漏：录音棚 +「我妹妹是音乐人」+`extensive renovation` 是"这栋房子地下藏着什么"的答案，也是"她笑得勉强、并不高兴"的伏笔（原文写明 `Matt didn’t think she sounded totally pleased about that`）。

### 漏-3 · 全章最锋利的一处对照：`we've` 与 `you've`｜ch34:104、107（字符 3198–3447）

- 原文逐字：
  - `‘If you ruin this for me, I will never forgive you. We are so fucking close to everything we’ve ever wanted.’`
  - `‘We’re close to everything you’ve wanted, Mel. I’m just here for the ride. I’m just a lamb to be sacrificed, to be defiled. Pawed over.’`
- md 现状：无引语块覆盖。导航·人物弧线只写了「护着妹妹，也护着那个『离想要的一切只差一步』的计划」（= ch34:104 那句），把 ch34:107 的反转整段丢了；**而 md 自己的词汇表里 `defiled` 的例句正是 ch34:107 的末句**——作者见过这句，却没让它进任何一个引语块。
- 为什么算漏：这一处是全章的胜负手（"我们"变"你"，"共同计划"变"你一个人的欲望"，"羔羊"），也是本章唯一把"计划"二字说透的地方。

### 漏-4（次要）· 门铃为什么没人应｜ch34:23（字符 363–482）

- 原文逐字：`‘Yes?’ A surly woman stared down imperiously at him. The chorus of Radiohead’s ‘Creep’ slinked feebly down the stairs.`
- md 现状：全文未出现 `Creep` / `Radiohead`。原句 1 的读者视角提示（md 行 27）只笼统说"低音"让人先感到"屋里有人"，没有点出这一层：屋里正放着 Radiohead 的《Creep》，所以按两次门铃没人应；也所以门是从里面被"啪"地拉开（人是从楼上下来应门的）。
- 为什么算漏：这是原文给出的"谁在房子里、屋里在做什么"的唯一具体答案，也是一个可复用的意象线索。

---

## 二、编（原文没有，md 写出来了）2 条

### 编-1 · 「尽头是一间小房间」｜原句 4 中文理解（md 行 51）

- md 原文：`……地窖是新近翻修的，灰泥线脚完美得不像话；尽头是一间小房间，沙发随手靠着墙摆着，马特推开了旁边那扇门。`
- 原文逐字（ch34:47）：`He came out in a small area with a sofa plonked against a wall. He opened the door off the space.`
- 问题：原文是 `a small area`（一小片区域／一处空间），md 升格成"**一间小房间**"；原文也没有"**尽头**"（`came out`＝走出来，不是走到尽头）。
- 判据：把 `area` 读成"房间"属推断性升格；"尽头"属原文没有的空间方位。

### 编-2 · 「早早就布置好的」｜原句 3 读者视角提示（md 行 47）

- md 原文：`……也说明这套防护不是临时起意，而是早早就布置好的。`
- 原文逐字（ch34:41）：`‘Security isn’t a problem,’ she said, gesturing to the camera above him pointed at the front door. ‘There’s one at the basement level and the back door as well. We have a fully functioning alarm system too.’`
- 问题：原文只列了设备清单，没有"布置时间"的任何依据，"不是临时起意／早早就布置好"是 md 自己加的时间性断言。
- 判据：可核事实之外的合理推演若**没有原文支点**，记编（提示级）。

> 其余评析性判断（"完美过头反而可疑""领带是警察制服上的符号""尴尬先于冲突"等）属评论，不计编。

---

## 三、错（与原文相反／失真）6 条

### 错-1 【阻断】原句 6 中文理解：离开房间的是"妹妹"｜md 行 71

- md 原文：`她轻声让她出去。梅尔又要来管她，她露出那种眼神。欧拉莉亚转回笔记本电脑，妹妹离开房间时她并不惊讶：梅尔说的每一句她都不感到意外，她知道妹妹是冲自己来的——她在与 Cal 的那顿晚餐上派过一个人去盯着，那人还端来过小杯的毒药。`
- 原文逐字（ch34:131，字符 4123–4503）：
  `‘Get out of my room,’ she said quietly. Mel would try to meddle with her now. She had that look. Eulalia turned back to her laptop to scroll obsessively as her sister left the room. She hadn’t been surprised by a single thing Mel had said. She knew she was out to get her. She’d sent a spy to watch over her at dinner with Cal, after all. He’d offered them little cups of poison.`
- 原文事实：**留下的是欧拉莉亚，离开的是她姐姐（梅尔）**。三条互证：
  1. `Eulalia turned back to her laptop ... as her sister left the room.`——转回电脑的是欧拉莉亚，走掉的是"她的姐姐"；
  2. 被闯的是欧拉莉亚的房：ch34:68 `Then she climbed up the two flights of stairs to her sister’s room. She shoved the door open without waiting to be admitted.`；ch34:71 `‘Hey, my door was shut. What the hell, Mel?’`；ch34:74 `Mel went over to Eulalia’s record player`；
  3. 说 `Get out of my room` 的是房主欧拉莉亚，被赶出去的是梅尔。
- md 的两重矛盾：
  - ① **称谓**：全书称谓是**梅尔＝姐姐、欧拉莉亚＝妹妹**（`00_概述:30`「欧拉莉亚负责露面，梅尔负责出声」、`00_概述:84`「妹妹在台上做那张漂亮的脸，她在幕后替妹妹盯药、管钱」、`00_金句精选:206`「姐姐 Mel…Mel 是声音，Eulalia 是脸」、`ch18 mel tests the death scent samples.md:11`「姐姐 Mel…妹妹 Eulalia」）。md 同文件的原句 5（行 65「妹妹却被留在原地」）与导航（行 12「推开妹妹的房门，直到梅尔被妹妹赶出房间」）也都按这个约定用"妹妹"指欧拉莉亚 ⇒ 原句 6 的"**妹妹**离开房间"只能指欧拉莉亚，于是同一句里欧拉莉亚"转回笔记本电脑"又"离开房间"，逻辑自闭。
  - ② **与 md 自己的导航打架**：导航（行 12，15:09 已修为）写的是"直到**梅尔被妹妹赶出房间**"，原句 6 写的是"**妹妹**离开房间"，同一份文件里两处对同一动作给了相反的主语。
- 改法：原句 6 中的"妹妹"改回"**梅尔**"（离开房间者＝梅尔），并按错-2 重写指代链。

### 错-2 【阻断】原句 6：猎人与"派眼线的人"被拆成两人，毒药被记到被对付方头上｜md 行 71、行 75

- md 原文（行 75 为什么这样写）：`……摔门、互骂、逼问，在她那里全被算成「妹妹要对付我」的证据，而她的对策早已就位——眼线，与小杯的毒药。`
- 原文逐字（ch34:131）：`She knew she was out to get her. She’d sent a spy to watch over her at dinner with Cal, after all. He’d offered them little cups of poison.`
  - 英文里 `She knew [that] she was out to get her.` 的内层主语 `she`（要对付她的人）与下一句 `She'd sent a spy` 的主语是**同一个人**——同一主语贯穿两句。
  - `watch over` 只是掩护说法；递出 `little cups of poison` 的是这个人的眼线。
- md 的问题：① 中文理解把"派过一个人去盯着"记在"妹妹"名下、为什么这样写又把"眼线与小杯的毒药"写成"**她的对策**"（被对付方的对策）——**同一件事被拆给两个人，方向也反了**；② md 的读法在 ch34 与 ch27 都落不了地：那顿"与 Cal 的晚餐"在 ch27 里是**卡莉与欧拉莉亚**的晚餐（ch27:62 `Eulalia was already waiting for her outside`、ch27:71 `Table for two, please`），两杯 limoncello 是从吧台那个男人那儿"送的"（ch27:197 `The waiter reappeared with two limoncellos. ‘Courtesy of the gentleman over there,’ he said, gesturing to a man sat eating at the bar.`），ch46:171 杰妮转述 `Mel sent a creepy man from the label to watch us when we went out for dinner. He sent limoncello to our table.`——无论最终是谁派的，**眼线与毒药属于"在对付人"的那一方，不属于被盯梢、被倒酒的那一方**。
- 改法：「为什么这样写」应写成"眼线与那两杯酒出自**同一个她**（原文主语贯穿两句）；欧拉莉亚之所以对梅尔的每一句都不惊讶，是因为她早知道有人在动她"。

### 错-3 【提示】原句 6 为什么这样写：「摔门」｜md 行 75

- md 原文：`摔门、互骂、逼问……`
- 原文逐字（ch34:68）：`Matt left the house. Mel bolted the front door.`
- 问题：原文是**闩上**前门（`bolted`），全章没有摔门；被赶出房间那一下也没有摔门动作（欧拉莉亚只是说 `Get out of my room`）。

### 错-4 【提示】导航·人物弧线：「摔唱片」｜md 行 14

- md 原文：`梅尔则是从勉强应付警察到摔唱片、逼问妹妹的转折`
- 原文逐字（ch34:86）：`Mel took the LP off the player and snapped it in half.`
- 问题：原文是**掰成两半**，不是摔。（同句的"逼问妹妹"另有出处：`‘What have you done?’`（ch34:92）确实是梅尔在追问，这半句可留。）

### 错-5 【提示】原句 1 为什么这样写：「闯进去」｜md 行 25

- md 原文：`开篇把「闯进去」写成一场狼狈的意外：……`
- 原文逐字（ch34:20、ch34:47）：
  - `He opened the letterbox and yelled ‘Hello’ at someone’s crotch. The door swung open so quick that he didn’t have a chance to stand up.`
  - `‘All right,’ she said, letting Matt in. She didn’t want to but it would be the quickest way to get rid of him.`
- 问题：马特**没有任何闯入动作**——拍门、按铃、开投信口喊话，然后门**从里面被拉开**，而且是她**主动放他进屋**。「闯进去」只来自文件名 slug（`ch34 matt breaks into a house at priory square`），本章没有对应事件。（这条同时牵出派工单的前提问题，见 `4-verdict.md` 的「前提更正」。）

### 错-6 【提示】原句 2 读者视角提示：「这个姓名在本章后半段还会再出现一次」｜md 行 37

- md 原文：`留意他自报姓名的方式——这个姓名在本章后半段还会再出现一次。`
- 原文：`Matthew Cheung` 在本章只出现**两次**（ch34:26 马特自报、ch34:65 梅尔看名片时念出），两次都在原句 5（ch34:86）**之前**；原句 5 提到那位警官时**不写名字**，只说 `the police officer who was just here`。
- 问题：读者按这句提示往后翻，会在原句 5 找不到第三次；该提示实际指向的是同一场访问中的 ch34:65（拜访中段），不是"后半段"。

---

## 四、计数

**漏 4（其中 1 条为次要）· 编 2 · 错 6（阻断 2 · 提示 4）**

阻断型 2 条，全部落在**原句 6**（md 行 71 / 行 75），且互相独立：
- 错-1 ＝ 离开房间者主语错（并与 md 自己的导航矛盾、与全书称谓矛盾）；
- 错-2 ＝ 末段行动者归属倒置（猎人与派眼线者被拆开，毒药记到被对付方头上）。

> 同一处缺陷不重复计数：错-1 与错-2 虽同在原句 6，但一处是"谁离开房间"（行 71 前半），一处是"谁派的眼线／谁的毒药"（行 71 后半＋行 75），判据不同、改法不同，故分列。

## 五、复核过的前提事实（供 `4-verdict.md` 引用）

- **这栋房子有没有门牌号**：ch34 全文**没有**门牌号（逐字符扫描：正文数字只有 `34` 与 `999`）；姐妹俩的房子是 **35 Priory Square**（ch33:228/231/255、ch37:101/139、ch39:26、ch44:104、ch45:20、ch48:259、ch50:166），且 ch36 的场景即 `Callie knocked on Eulalia and Mel’s front door`（epub `OPS/s051-Chapter-036.xhtml`）——与 ch34 是同一栋。**md 全文没有写出任何门牌号**，因此不存在编造。
- **摄像头数量与位置**：**三处**（`the front door` / `the basement level` / `the back door`）＋`a fully functioning alarm system`（ch34:41）；马特**只看到**一台（ch34:44 `saw the camera she was referring to`）。md 现文「听她**报出**三处摄像头」与原文一致。
- **谁在房子里**：欧拉莉亚（楼上自己房间，放着 Radiohead 的《Creep》与唱盘）与梅尔（开门、应答安保、事后闩门上楼）；"门铃没人应"是音乐盖的，不是有人拒不应门。


---

## 收口复核（2026-10-21，主会话接手后）

> 本目录 3-diff.md / 4-correspondence.md 是**独立复核（第二实例）**对 md sha256 `7fe50baf…`（15:09:15）的重做版本；
> 其查出的**二轮 2 条阻断型**（原句 6 里的「离开房间的是妹妹」、猎人与派眼线者被拆成两人）已由主会话在 commit `78717e852`（16:20）整改，
> 裁定与逐条理由见 `4-verdict.md` 的「派工人裁定」节。**当前被审版本 = sha256 `854e0e8a69829c18af67cc1222b78020eb9e8af8adc8c7c8da9e28653b33f2ef`**（= 本目录 4-verdict.md 末节所记版本 ✓）。

### 收口四组数（对现版）

| 组 | 结果 |
|---|---|
| 逐字 | 6/6 引语逐字命中（strict 子串 6/6、跨段 0）；27/27 词汇例句逐字命中 |
| 对应 | **6/6 块成立**（二轮 2 条阻断修后，对应组归零）；提示 4 条（错-1 小房间／错-2 早早就布置好／错-4 「摔」／原句 4 轻度选短）只记不改 |
| 形态 | H1 `34. Priory Square`、导航 5 项、子项 4 项、块数 6 ∈ 5–10 ⇒ 0 偏离 |
| 断言 | 核 34 条：**阻断型 5 → 0**（一轮 3 条导航层 + 二轮 2 条原句 6 归属） |

- 派工单前提错误三条（强行闯入／本章有门牌号／分部名 A THURSDAY IN MAY）已在 `4-verdict.md` §八 更正，**md 原本是对的，勿按派工单改**。
- 本目录底稿由两个实例接力写成，故保留**双份 R1**：`1-suread.json`（主会话首轮）＋ 独立复核代理重做版（含 `second_pass_notes`）；两者对同一章的事件序列一致，以 `4-verdict.md` 的最终裁定为准。
