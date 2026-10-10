# Null Entity — d 步语义审查（引语↔分析逐对核对）ch01–ch08 · v2

- 审查范围：`ch01 the game begins.md` … `ch08 a feast just out of reach.md`，共 8 章 / 61 个原句块
- 原文语料：`text/ch01_chapter_1.txt`(308 行) `ch02`(358) `ch03`(462) `ch04`(518) `ch05`(117) `ch06`(408) `ch07`(201) `ch08`(438)，行号一律以 `wc -l` 与 `sed -n 'Np'` 为准
- 交叉引用锚点约定：本书 md 里的 `chNN:LLL` 一律对应 `text/chNN_*.txt` 的行号（已在 ch01:51/72/120/128/187、ch02:259/268/277、ch03:432、ch04:33 等多处命中验证）
- 证据协议合规说明：以下每条 EVIDENCE / SOURCE 子串均由本代理用 `sed -n '<行号>p'` 与逐字节 python `in` 判定双重确认，且长度均 ≥12 字符（唯一例外见阻断型 B-2 的说明：`text/ch03:234` 整行仅 `“Yes.”` 四字符，不足以组一条合规 SOURCE，故改用同场景的 228/231 两行为正式 SOURCE，234 只在正文说明里引用）。
- 只读声明：除本报告文件外未写入/编辑任何文件；未执行任何 git 写操作。

## 汇总

**阻断型 3／提示型 16／假红型 0**

分层结论：
- 检查 1（引语覆盖率，AGENTS 第 9 条 a2）：主会话已全书跑过，ch01–ch08 该层 0 缺陷，本报告不重复报。
- 检查 3（关键词锚定）：61 块全部逐块用脚本核验（每个 `**关键词**` 的每个词条在该块自身引语内做词形还原后的包含判定），**0 处脱锚**。
- 本报告 3 条阻断型全部落在检查 4（分析层事实断言 / 章内时序），与本 brief 指出的「时序倒置是第一缺陷簇」一致。

---

## 阻断型（内容错，读者会被误导）

### B-1 · ch03 导航层（`ch03 i woke to fire.md:10` 一句话概括）：firewall 与「you 醒来」因果+时序双倒置

md 写的是「叙述者筑起 firewall 把 you 挡在外面；you **因此**醒来」。原文里 you 在 300 行已被创伤与肾上腺素「snapped awake」，firewall 直到 330 行才立起——晚 30 行。即：醒来在前，筑墙在后；md 把顺序反过来，还把「挡在外面」写成了醒来的原因。

EVIDENCE|ch03 i woke to fire.md|10|叙述者筑起 firewall 把 you 挡在外面；you 因此醒来
SOURCE|text/ch03_chapter_3.txt|300|That shock snapped you awake—you were choking
SOURCE|text/ch03_chapter_3.txt|330|Fearing you’d lose your body, I threw up a firewall

补充核对：300 之后 303 行 `“No—!” you gasped.` 才是醒来者的第一声，330 之后叙述者才被封在体外。导航层其余事实（Marek Cintel 身份植入、License Agreement 划管辖、医护认出 Specter、章末 `Without a word, you stepped inside the vessel and sealed the door.`）逐条对过，均真。

### B-2 · ch03 块 6（`ch03 i woke to fire.md:103`）：章内时序倒置——「Four 早已当众报出过」发生在该场景之后

md 的原话是「Four 早已在 ch03:267 当众报出过 “Most likely Wylla Sotain”，**她当时没有承认**，而这一次她对着一个陌生人的脸认了」。锚点 267 本身是对的（该行确为 Four 的公开点名）。错在时序：医护认人与那句 `“Yes.”` 在 228–234，Four 的公开点名在 267，晚 33–39 行。也就是说 234 那一刻 Four **还没有**当众报过她的名字，md 用「早已……她当时没有承认」把一个尚未发生的事件写成了她此前回避过的事，并据此构造出「这次才认」的弧线。全书 `ch03` 内 `Sotain` 只出现在 267 行一处（已 grep 穷举），不存在更早的公开点名。

EVIDENCE|ch03 i woke to fire.md|103|Four 早已在 ch03:267 当众报出过 “Most likely Wylla Sotain”，她当时没有承认
SOURCE|text/ch03_chapter_3.txt|267|Most likely Wylla Sotain, null entity in possession
SOURCE|text/ch03_chapter_3.txt|228|You’re the Specter, aren’t you? The Null

补充核对：`“Yes.”`（234）与「they pushed their face close」（231）均真实存在，md 对这两处的读法没问题；本条只打「早已」这个先后关系。若把 103 这句改成「几段之后 Four 才当众报出……」即成立，故修订成本极低，但性质上属于事件顺序错误，不是措辞偏好，因此仍列阻断型。

### B-3 · ch05 块 6（`ch05 we revolted together.md:77`）：把本章自己的内容记成了「上一章」

md 写「上一章你们刚借用 RABBIT 的猎物本能站立」。`prey-animal` 与「站立」的组合只在 **ch05:69** 出现，正是本块所在的那一章；ch04 里唯一相关的一句是 116 行 `Old prey thoughts tried to rise, but fury drowned them.`——猎物念头被怒火压了下去，既没有 RABBIT 也没有站起来。所以「上一章借用猎物本能站立」在 ch04 里没有任何出处，属于无出处断言。

EVIDENCE|ch05 we revolted together.md|77|上一章你们刚借用 RABBIT 的猎物本能站立
SOURCE|text/ch05_chapter_5.txt|69|driven upright by the ghost of RABBIT’s prey-animal reflex

补充核对：穷举 `grep -rn "prey"`：ch04 仅 116 行、ch05 仅 69 行。对照之下，ch06 md:47 写「请回读上一章的猎物反射」从 ch06 的视角看**是正确的**（69 确在 ch05），可见这条错误是 ch05 内部把「前文」误升格成了「上一章」。md:77 同段其余断言（`code clashed against meat`、`dying insect`＝实验尾段的中毒标本）均对得上 111 行。

---

## 提示型（措辞正当性 / 启发式误报，只记不改）

### P-1 · ch01 块 2（`ch01 the game begins.md:35`）：「叙述者开口第一件『我』做的事」

在 36 行 `I split in thirds` 之前，已有 21 行 `"Local hackers are aware of our presence," I told you.`（第一句「我」的开口）、24 行 `I stayed silent`、30 行 `I flicked my focus to your MARK I RABBIT`（第一件「我」的动作）。若读成「第一件以分布式自我为内容的『我』句」则成立，故只记不改。

EVIDENCE|ch01 the game begins.md|35|叙述者开口第一件“我”做的事，就是把自身拆成三路
SOURCE|text/ch01_chapter_1.txt|21|I told you. “Probably a minute before station security
SOURCE|text/ch01_chapter_1.txt|30|I flicked my focus to your MARK I RABBIT

### P-2 · ch01 块 4（`ch01 the game begins.md:57`）：「只隔了数段」

消息板那句在 120 行，全大写喊话在 199 行，中间实数 **23 个非空自然段**（124/128/132/136/140/144/147/151/154/157/160/163/166/169/172/175/178/181/184/187/190/193/196 逐行数过），不是「数段」。互证关系本身成立。

EVIDENCE|ch01 the game begins.md|57|只隔了数段：地下网络里的绰号与屏幕上的称呼互证
SOURCE|text/ch01_chapter_1.txt|120|Agreed. The specter is the VF fugitive
SOURCE|text/ch01_chapter_1.txt|199|AM I BETTER THAN YOU, SPECTER?

### P-3 · ch02 块 4（`ch02 desire outweighed the risk.md:57`）：「这一区」给原文加了范围限定

原文 45 行是无范围限定的 `all VisorForge masks within twenty-four hours`；「这一区」在本块引语里没有对应词（`this sector` 出现在 42 行，但那是另一件事：off-grid 面具「our leaks in this sector」）。且同文件导航 md:10 自己写的是「向**全域** VisorForge 面具推送」，两处口径不一致。

EVIDENCE|ch02 desire outweighed the risk.md|57|一次强制更新会被推给这一区所有 VisorForge 面具
SOURCE|text/ch02_chapter_2.txt|45|pushed to all VisorForge masks within twenty-four hours

### P-4 · ch02 导航层（`ch02 desire outweighed the risk.md:11`）：把「羞耻」安在录像处

全章唯一一处 `embarrassment` 在 39 行（谁去动手的拌嘴段），录像在 208–262。录像段给的是 horror（244、262）。按行文顺序 39 也在「餐馆里罕见的柔软」（114 `I loved you. I hadn’t told you`）**之前**，所以弧线里的位置说明与文本顺序不符。属弧线概括的松写法，只记。

EVIDENCE|ch02 desire outweighed the risk.md|11|在录像前跌为恐怖与羞耻，末段被压成一句法律判断
SOURCE|text/ch02_chapter_2.txt|39|Your mouth pulled tight. I imploded with embarrassment.
SOURCE|text/ch02_chapter_2.txt|244|The horror came slowly, then all at once.

### P-5 · ch03 块 4（`ch03 i woke to fire.md:77`）：「三段呼号」只枚举了两段

md 自己给的括号只有（"No!"、"Wait!"）两例，对应 93、96 两个自然段；`A flare.` 在 99。若「三段」指 75/78/93 那组更早的喊话则跨了场景。**按 brief 要求先枚举**：本章 `“No!”` 与 `“Wait!”` 形态的呼号共 4 处——75 `"Those Corp bastards!"`/`"Their machine—it killed Ray!"`、78 `"Ray's dead?"`、93 `"No!"`、96 `"Wait!"`；紧邻 99 的只有 93、96 两处。故「三段」不成立、且枚举不全。计数口径问题，不改判读。

EVIDENCE|ch03 i woke to fire.md|77|作者先给三段几乎连不成句的呼号
SOURCE|text/ch03_chapter_3.txt|93|“No!” she screamed. “You did this!”
SOURCE|text/ch03_chapter_3.txt|96|“Wait!” someone said, but a seam was opening

### P-6 · ch04 导航层（`ch04 part of the subsidiary was in your head.md:10`）：「一小时后」把「不到一小时」读反了方向

30 行原文是 `We weren’t even an hour out from GTM-11`——不足一小时。md 写「一小时后」在数值方向上偏紧。概括层，只记。

EVIDENCE|ch04 part of the subsidiary was in your head.md|10|逃离 GTM-11 一小时后，在 Subsidiary Four 的血肉船上
SOURCE|text/ch04_chapter_4.txt|30|We weren’t even an hour out from GTM-11

### P-7 · ch04 块 7（`ch04 part of the subsidiary was in your head.md:93`）：回扫指令指向的两个例子都在本章后半段（边界条）

md 说「请回扫本章**前半段**的每一次决定——跳转时机、坐标"随机"」。ch04 共 518 行，前半段≈1–259；而「跳转时机」在 461 行（89% 处）、「punched in random coordinates」在 488 行（94% 处），且 488 落在 482 行「Realization hit」的揭底**之后**。位置说明错误会让读者回扫不到目标段落；但它不改变任何剧情判断，故仍列提示型，交主会话定夺。

EVIDENCE|ch04 part of the subsidiary was in your head.md|93|请回扫本章前半段的每一次决定——跳转时机、坐标
SOURCE|text/ch04_chapter_4.txt|488|Furious, you punched in random coordinates and jumped again
SOURCE|text/ch04_chapter_4.txt|461|having jumped the instant we were in the ship

### P-8 · ch04 块 6（`ch04 part of the subsidiary was in your head.md:81`）：「屡攻不下的原因」是无据因果

帖子串（267–288）只说 Edenic 去中心化「You can't kill what doesn't have a head」，全章没有任何「"我"与你在网络层攻不下 Order」的表述（已 grep `couldn’t crack|penetrat|untraceable` 等，无命中）。因果为评论者补写。同段的「帖串里就有 Shut up」则**核实为真**（282 行，距 274 引语仅 8 行）、`“Chatty hackers,”` 在 422 行也真。

EVIDENCE|ch04 part of the subsidiary was in your head.md|81|正是“我”与你在网络层屡攻不下的原因
SOURCE|text/ch04_chapter_4.txt|274|cells grow sideways, not up

### P-9 · ch05 块 6（`ch05 we revolted together.md:77`）：「倒数第二个自然段」实为倒数第三

**枚举本章末尾非空自然段**：105 / 108 / 111 / 114 / 117（117 `And fired.` 为末段）。被分析的两处（`code clashed against meat`、`dying insect`）同在 111 行＝倒数第三段。措辞偏差，只记。

EVIDENCE|ch05 we revolted together.md|77|本章倒数第二个自然段停在败局定格
SOURCE|text/ch05_chapter_5.txt|111|You were a dying insect inhaling poison

### P-10 · ch06 块 4（`ch06 i feel sick.md:57`）：「全章第一个属于 Wylla 的英文句子」

120 行 `“I feel sick,” you said—filtered through the Subsidiary’s voice box.` 之前，102 行已有 `“Sable,” the Subsidiary choked.`。按施动关系核过 66–105 上下文：69–78 的持枪威胁与 `Where is she?`（72、78）都是叙述者；102 那声 “Sable” 之后 105 才描写 Subsiadiary 躯体像「ill-fitting clothing」地活动、108 才是 `Oh, Wylla.` 的认出。所以 102 按情节归属应是 Wylla 借机器喉出的第一个词，早于 120。md 的限定「第一个**完整**／被明码标注为借来通道的句子」可以成立，故列提示型。

EVIDENCE|ch06 i feel sick.md|57|是全章第一个“属于 Wylla”的英文句子
SOURCE|text/ch06_chapter_6.txt|102|“Sable,” the Subsidiary choked.
SOURCE|text/ch06_chapter_6.txt|120|filtered through the Subsidiary’s voice box

### P-11 · ch06 块 6（`ch06 i feel sick.md:77`）：「第三人称化的第二人称」——原文只有 you

147 行整段无第三人称代词，全部是 `you / your / you had`（已读全行）。md 想说的应是「被外化／被拉开距离的第二人称回顾」，写成「第三人称化」会让读者去找不存在的 she。判读本身（借 distance 才看见身体的贬值）成立。

EVIDENCE|ch06 i feel sick.md|77|本章的主题句藏在第三人称化的第二人称里
SOURCE|text/ch06_chapter_6.txt|147|Years ago, you might have chosen nothingness over the body

### P-12 · ch06 块 8（`ch06 i feel sick.md:101`）：「上一章结尾」的押注实际在上一章开篇

md 说 crisp／feminine 声线「正是上一章**结尾**两人押注的那个『唯一盟友』」。原文 `our only allies were listening` 在 ch05:24（占 117 行的 20%，属开篇出逃段）；ch05 结尾（105–117）是夺身中枪，全章末尾无盟友字样。

EVIDENCE|ch06 i feel sick.md|101|正是上一章结尾两人押注的那个“唯一盟友”
SOURCE|text/ch05_chapter_5.txt|24|in the hopes our only allies were listening

### P-13 · ch07 导航层（`ch07 welcome to the thorned root.md:12`）：「『我』的复仇动机首次自白」跨章首次性不成立

**枚举 ch07 之前的复仇自白**：ch02:84 `Revenge felt good, but not enough.`（叙述者第一人称自陈）；ch04:131 `Of course you mattered more than revenge.`。ch07:69 是 Wylla 用 Four 的嗓音指控 `"You want revenge, and you want my body…"`，属他人指认而非「我」的自白，且晚于前两处。同条里「Sable 在本章的第一次出现就在 Wylla 的怒骂里」经核为真，不在本条范围。

EVIDENCE|ch07 welcome to the thorned root.md|12|的复仇动机首次自白，Wylla 的“想退出”首次说出口
SOURCE|text/ch02_chapter_2.txt|84|Revenge felt good, but not enough
SOURCE|text/ch04_chapter_4.txt|131|Of course you mattered more than revenge.

### P-14 · ch08 块 1（`ch08 a feast just out of reach.md:23`）：「本章中段才揭底」——揭底在前 12%

md 说 supposed monument 与「本章中段才揭底的底牌」同属一条伏笔链。底牌（船不是他们的）在 51–54 行，ch08 共 438 行，即全章前 12%，不是中段。伏笔链判断本身成立（15 行 `belly of a warship` → 48–54 揭底顺序正确，是伏笔而非倒错）。

EVIDENCE|ch08 a feast just out of reach.md|23|与本章中段才揭底的底牌同属一条伏笔链
SOURCE|text/ch08_chapter_8.txt|51|The Thorned Root were never meant for this warship.

### P-15 · ch08 块 2（`ch08 a feast just out of reach.md:37`）：「一句比一句短」与词数相反

**实数词数**（`awk '{print NF}'`）：51 行 = 9 词；54 行 = 11 词。后一段并不更短。「后两段各自独句成段」为真（51、54 各成一段），三段论结构（48 证据→51 判断→54 翻转）为真，`open veins` 与本章第一句 `belly`（15 行）同属解剖隐喻亦为真。

EVIDENCE|ch08 a feast just out of reach.md|37|后两段各自独句成段，一句比一句短
SOURCE|text/ch08_chapter_8.txt|51|The Thorned Root were never meant for this warship.
SOURCE|text/ch08_chapter_8.txt|54|They had taken it—and now held it together by sheer discipline.

### P-16 · ch08 块 5（`ch08 a feast just out of reach.md:67`）：「头两拍各只有两词」——第二拍是三词

159 行原文：`Forests gutted.`（2 词）`Species wiped out.`（**3 词**）。同条其余为真：`They hoard engineered crops` 确在 159 行中段变长；`What a neat little explanation.` 与 `“But that’s not the real reason.”` 确在紧随的 162 行。

EVIDENCE|ch08 a feast just out of reach.md|67|头两拍各只有两词——受损物加过去分词
SOURCE|text/ch08_chapter_8.txt|159|Forests gutted. Species wiped out.

---

## 假红型：0

判据层（引语真实相邻、行号可查、锚点映射）在 ch01–ch08 未出现坏判据。为避免被误读为「没测」，记录本轮主动排查并否决的三类假红来源：

1. **全角标点 / `「」` 内中英混排**：按 brief 与既有定性，不当伪造引语处理。已避让的 4 条不再报：ch03:55 全角 `Ray？Ray！`、ch21:99 全角 `RABBIT！RABBIT！`、ch12:61 `whole minds crushed…grown from`、ch11:33 `I was gleeful ... but`（后三条在 ch01–ch08 之外，此处仅作不重复报的声明）。
2. **引语覆盖率层（a2）已由主会话跑过**：ch01–ch08 该层 0 缺陷（3 条候选已在别处判为合法：ch19:108 They、ch20:24 Wood、ch01:199 全大写），本报告不重复。
3. **Read 工具截断导致的假「无出处」风险（两次，均已自救）**：
   - `text/ch06_chapter_6.txt` 408 行只显示到 372 行 → 用 `awk 'length($0)>0 && NR>=145'` 取回 396（`TR.Δ.SAB.05.`）、402、405、408。
   - `text/ch08_chapter_8.txt` 438 行只显示到 432 行 → 用 `wc -l` + `tail -c` + `grep -n` 取回尾部。
   - 直接后果：曾疑 ch08 md:109 的「章末 Aliers 的 Follow me.」为伪造，`grep -n "Follow me" text/ch08_chapter_8.txt` 命中 **438 行 `Aliers grinned widely. "Follow me.”`**，正是全章末句，真实无误，**未报警**。这正是上一位代理被否决的失效形态，故在此留痕：凡拟报「原文没写」，必须先跑完文件尾部。

## 已核对块数：61

块数由 `grep -c` 五类计数器同章互校得出（`> **原句` / `**关键词**` / `**中文理解**` / `**为什么这样写**` / `**读者视角提示**` 每章数值相等，无缺项）：ch01=8、ch02=8、ch03=8、ch04=8、ch05=6、ch06=8、ch07=7、ch08=8。

逐块读取清单（章-块号-读过；标 ⚑ 者为本报告有结论的块，导航层单列）：

| 章 | 逐块读取 | 该章命中 |
|---|---|---|
| ch01 | 1 ✓ / 2 ✓⚑ / 3 ✓ / 4 ✓⚑ / 5 ✓ / 6 ✓ / 7 ✓ / 8 ✓ | P-1、P-2 |
| ch02 | 1 ✓ / 2 ✓ / 3 ✓ / 4 ✓⚑ / 5 ✓ / 6 ✓ / 7 ✓ / 8 ✓ | P-3 |
| ch03 | 1 ✓ / 2 ✓ / 3 ✓ / 4 ✓⚑ / 5 ✓ / 6 ✓⚑ / 7 ✓ / 8 ✓ | B-2、P-5 |
| ch04 | 1 ✓ / 2 ✓ / 3 ✓ / 4 ✓ / 5 ✓ / 6 ✓⚑ / 7 ✓⚑ / 8 ✓ | P-7、P-8 |
| ch05 | 1 ✓ / 2 ✓ / 3 ✓ / 4 ✓ / 5 ✓ / 6 ✓⚑ | B-3、P-9 |
| ch06 | 1 ✓ / 2 ✓ / 3 ✓ / 4 ✓⚑ / 5 ✓ / 6 ✓⚑ / 7 ✓ / 8 ✓⚑ | P-10、P-11、P-12 |
| ch07 | 1 ✓ / 2 ✓ / 3 ✓ / 4 ✓ / 5 ✓ / 6 ✓ / 7 ✓ | （仅导航层 P-13） |
| ch08 | 1 ✓⚑ / 2 ✓⚑ / 3 ✓ / 4 ✓ / 5 ✓⚑ / 6 ✓ / 7 ✓ / 8 ✓ | P-14、P-15、P-16 |

导航层（每章 本章导航 / 本章词汇 / 一句话总结）4 章段另计，读过并产出：B-1（ch03:10）、B-2 之外另有 P-4（ch02:11）、P-6（ch04:10）、P-13（ch07:12）。

## 方法学与可复算性

- 检查 3（关键词锚定）用一次性内联 python（heredoc，不落盘）解析 `ch0[1-8]*.md`，把每块 `> **原句` 引语累积到该块 `**关键词**` 行，做含词形还原的子串判定；输出仅 `scan done`，即 61 块 0 脱锚。
- 所有计数类断言（「五遍」「三段」「倒数第二」「前半段」「各只有两词」「一句比一句短」「唯一」「首次」）均先枚举再判，未凭印象；因此 ch02 的「说了五遍 trap」、ch05 的「Thorned Root 只出现一次」、ch07 的「Sable 首现/Wylla 首次说退出」、ch03 的 Marek 三行、ch06 的「第三段」与「三词段」、ch08 的「Auren Pell. 两词」等经枚举后**判为真，未报**。
- 本章前瞻引用双向核过且成立：ch04 末指向 ch05 开篇的「你把手拍上 RABBIT 的那一秒」＝ch05:15；ch05 的「血是热的」＝ch06:15。
- ch06/ch07/ch08 说话人逐一按施动关系核过：`I feel sick`＝Wylla 经 voice box；`Your explosion on GTM-11 injured both myself and VisorForge Subsidiary Four`＝叙述者（md 的「『我』换成了另一套口径」正确）；`Sable. Be careful.`＝Wylla（ch08:168+171）；`I don’t want to get used to it`/`I did not repeat it`＝Wylla/叙述者（ch08:351）；Pell/Vex/Spektral 影像由 Wylla 经 Four 送出（ch08:246/249）与 Aliers 的 Monk Lorien 档案（ch08:372）出处不混，md 的提醒正确。换身后的 `I`/`you` 指称翻转（brief 点名的最高危处）在 ch06 全章未发现错标。

## 一条自我更正（供主会话核验时参考）

本报告起草过程中曾有一条待报内容为「ch03:103 的锚点写错，应为 279→267」。按协议重跑 `sed -n '103p'` 后确认 md 原文印的就是 `ch03:267`，**锚点无误**，该子结论已删除，只保留经证实的时序倒置部分（B-2）。此处留痕是为了说明：本轮所有行号都经过重取，未沿用上一位代理的行号，也未沿用本代理自己的记忆。
