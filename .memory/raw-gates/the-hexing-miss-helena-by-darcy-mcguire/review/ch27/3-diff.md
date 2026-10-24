# ch27 深审 R3 三张单子（漏 / 编 / 错）

> 章：`text/ch27_chapter_27.txt` ↔ `ch27 a new oath and a red dress.md`
> 流程：R1 素读（`1-suread.json`，65 个事件、76 个片段全部为原文子串，`BAD=0`）→ R2 机器（`2-machine.json`，verdict ok）→ R3 本文件 → R4 逐块对应（§四）→ R5 判定（见 `4-verdict.md`）
> 只出指令，不改稿。

---

## 〇、结构底账

| # | 事实 | 证据（`text/ch27_chapter_27.txt`） |
|---|---|---|
| 1 | 正文体范围 `:35`–`:364`（`:364` 末句 `protecting the two women whose hearts beat as one.`） | 逐行核；`:365`–`:383` 空白，`:384` `MORE FROM DARCY McGUIRE` |
| 2 | 三场景、两次切换：场景一 `:35`–`:137` 贴 **Cynthia**（`:35` `She heard the click`；`:41` `her love’s eyes`）；场景二 `:153`–`:243` 贴 **Helena**（`:171` `she wished she could read Cynthia’s thoughts`；`:189`／`:192` 心声入她脑中）；场景三 `:259`–`:364` 贴 **Cynthia**（`:259` `Cynthia stared`；`:298` `she realised`） | 逐行核 |
| 3 | 两次正文分场空白各 15 行：`:138`–`:152`、`:244`–`:258` | `python3` 连续空行统计：`(138,152,15)`／`(244,258,15)` |
| 4 | 海伦娜先立新誓，辛西娅逐句回应；回应在同一章内、紧接两块 | `:47` 邀请 → `:53` 海伦娜誓词 → `:56` 辛西娅誓词 |
| 5 | 誓词只改结尾：`for the rest of my days.` → `Always.`；称呼 `Cynthia,` → `Helena,` | `:53`／`:56` |
| 6 | 新月疤 = ch26 `:185` 那道伤；星形胎记在海伦娜胸骨 `:71`——两者不是同一物 | `:47` `the new crescent moon`；`:71` `The birthmark shaped like a star` |
| 7 | 离床悬空「至少三尺」发生在高潮后 | `:125` `hovering at least three feet above the bed` |
| 8 | 第二场景地点是**侯爵夫人套房／更衣室**，不是门厅 | `:168` `Will you have her meet us in the marchioness’ suite?`；`:171` 上楼；`:174` `her dressing room` |
| 9 | 希金斯太太的恐惧心声：`Dear God. She knows.` 与 `Mrs Higgins’ terrified thoughts echoed in Helena’s head` | `:189`／`:192` |
| 10 | 辛西娅先说「我告诉警司休伯特是自杀」（`:207`），**之后**希金斯太太才哭诉撞见掐波莉（`:210`） | 逐行核；md:10 顺序相反 |
| 11 | 凶器是休伯特桌上的拆信刀；受害者是 Polly | `:210` `took the letter opener from his desk`；`:210` `when I saw him with Polly` |
| 12 | 辛克莱不会出卖她是有条件的：`If he does, his word will never stand against mine.` | `:207` |
| 13 | 退休安排：海边小屋＋终身收入＋贬 Lady Argyle；事务律师面谈 | `:231`／`:240` |
| 14 | 辛西娅弃夫姓与管家职衔发生在套房内、在场者只有海伦娜与希金斯太太 | `:237` |
| 15 | 舞厅三句闲话各自独立成段、以省略号起头 | `:262`／`:265`／`:268` |
| 16 | 「这些蠢货永远不会懂」的是**旁人**，辛西娅与海伦娜有爱 | `:325` `We have something these fools will never understand. Love.` |
| 17 | 问「你怎么忍住不动手」的是**托马斯**，回答的是辛西娅 | `:322` Thomas growled；`:325` Cynthia |
| 18 | 芒特罗街联排宅改避难所是**对海伦娜说**的（`wait until they hear` 尚未公开）；Cotswold 宅与 All Things Bright and Beautiful 同段 | `:304` |
| 19 | 海伦娜读到公爵夫人的念头并据此说「we have her blessing」 | `:352` |
| 20 | 本章无正文中段推广行；推广页只在文末 `:384`–`:394` | `/usr/bin/grep -n "MORE FROM"` → `:384` |
| 21 | md：13 块（`md:17/27/37/47/57/67/77/87/97/107/117/127/137`）、词表 24 行 9/9/6、导航 5 项 | `2-machine.json`：`blocks=13`、`block_target=[6,10]`、`block_hint`＝「块数 13 偏离本章篇幅建议 6–10（本章 3244 词）」、`segments=14`、`segment_miss=0`、`issues` 全空 |

---

## 一、漏

| # | 原文事实 | md 现状 | 判定 |
|---|---|---|---|
| L1 | `:192` 希金斯太太说 `I won’t let anyone else suffer for my choices.`（另一句是 `I just couldn’t let him hurt another girl.`） | md:10 只写「不能让别的女孩再受害」，漏掉「不让人替我的选择受罪」 | 提示（P30） |
| L2 | `:231` 退休安排的具体内容：海边小屋、终身不愁的收入、贬 Lady Argyle、她的才能在她手下会被浪费 | md:10 只写「优厚退休金…安排事务律师面谈退休细节」 | 提示（P31） |
| L3 | `:304` 两人仍保留 Cotswold 宅，夏天在海伦娜的 All Things Bright and Beautiful 帮忙，因此两地分住 | md:10 只写联排宅改避难所 | 提示（P32） |
| L4 | `:352` 海伦娜读到公爵夫人的念头：「we have her blessing」，且「given me some ideas to try with you later」 | md:10 只写「意味深长地看克莱奥…热风…离场」 | 提示（P33） |

---

## 二、编

**本节无独立新增事实。** 下列都按「属性补写／归属错／形式计数错」记在 §三，不重复计入凭空：`:10`「当众宣布」、`:13`「当众放弃夫姓」、`:117`「当众说出来」、`:10`「反问哥哥」、`:10`「自己与这些人永不会懂」、`:11`「唯一发生在室内的高点」、`:11`「门厅」。

**成立取证表（md 事实主张逐条回原文，58 条）**

| # | md 主张 | 原文（行） |
|---|---|---|
| 1 | 三场景、两次十五行空白；一、三贴辛西娅，二贴海伦娜 | `:35`／`:153`／`:259`；空白 `:138`–`:152`／`:244`–`:258` |
| 2 | 门一锁上海伦娜自白 | `:38` `She heard the click of the lock, and then Helena’s arms were around her` |
| 3 | 「我看见你倒在那些浴室的地上，我的世界停住了」 | `:38` |
| 4 | 可以无惧赴死、不能没有她地活；认下自己是最大的傻子 | `:38` |
| 5 | 辛西娅看着她灰眼里的银渗满整双眼 | `:41` `she watched silver bleed into grey until her love’s eyes were glowing` |
| 6 | 两人急切褪去对方衣物 | `:44` `Helena stripped Cynthia from her borrowed dress`；`:47` `Cynthia spun Helena to untie her corset laces` |
| 7 | 手覆心口、发抖的手指描过新月 | `:47` |
| 8 | 一生活得靠誓约、想立新誓、先问「这样可以吗」 | `:47` |
| 9 | 辛西娅屏住呼吸、一顿一顿地点头 | `:50` `She nodded in jerky movements` |
| 10 | 誓词四句：身／心／灵／庇护 | `:53` |
| 11 | 辛西娅想不起婚誓、那是顺从中的空话 | `:56` `Empty words repeated in dutiful obedience` |
| 12 | 逐句回应并把结尾改成「永远」 | `:56` `... sanctuary. Always.` |
| 13 | 这些词把两颗灵捆成不可解的结合 | `:59` `binding their spirits into an unbreakable union` |
| 14 | 海伦娜低吼「你是我的夫人，此刻与永远」 | `:113` |
| 15 | 两人在高潮里离床三尺悬着 | `:125` |
| 16 | 落回床垫后吸进佛手柑与香蜂草，如今是家的气味 | `:137` |
| 17 | 说「看看我能不能让我们再飞一次」 | `:137` |
| 18 | 两人已站在辛西娅宅门前台阶 | `:153` |
| 19 | 辛西娅拒绝先去取裙，说要同希金斯太太谈 | `:156`／`:159` |
| 20 | 管家开门时眼睛睁大 | `:162` |
| 21 | 海伦娜随她上楼，想读心又明白那是不公平的优势 | `:171` |
| 22 | 辛西娅抱出沉重的礼服说「我等不及要离开这栋房子，和你开始新生活」 | `:174` |
| 23 | 海伦娜听得口干，身旁花瓶开始旋转 | `:177` |
| 24 | 希金斯太太进来、双手紧扣在身前 | `:180` |
| 25 | 「她知道」的心声直接映进海伦娜脑中 | `:189`／`:192` |
| 26 | 她僵住（原文 `freezing halfway across the room`） | `:192` |
| 27 | 自首、本该立刻坦白、不能让别的女孩再受害 | `:192` |
| 28 | 辛西娅快步拉她入座 | `:195` |
| 29 | 「请她来不是为了对质，而是为了道谢——谢她做了我做不到的事」 | `:198` |
| 30 | 海伦娜心口发痛，原文点明这是爱的另一面 | `:201` `This was the other side of love` |
| 31 | 撞见休伯特掐波莉、从他桌上拿走拆信刀、尖叫着他也不停 | `:210` |
| 32 | 心里认定要为罪下地狱 | `:213` `I shall burn in hell for my crimes.` |
| 33 | 「保护无辜者不是罪」 | `:216` |
| 34 | 辛克莱虽混蛋却不会出卖她；他的话压不过她的话；她安全了 | `:207` |
| 35 | 哈姆雷特把身体贴上老太太的腿 | `:219` |
| 36 | 「你结果休伯特性命时也把我放了，现在轮到我为你做同一件事」 | `:225` |
| 37 | 以侯爵夫人最后一个举动给优厚退休金 | `:231` `My last act as Marchioness of Kentmore` |
| 38 | 安排事务律师面谈退休细节 | `:240` `her man of business... details of her retirement` |
| 39 | 不再是布尔洛斯夫人、对方不再是管家，两人都自由 | `:237` |
| 40 | 抬裙过门槛时说最后一次走出这道门痛快 | `:243` |
| 41 | 三句闲话独立成段：不穿黑／尸骨未寒／没准是她动的手 | `:262`／`:265`／`:268` |
| 42 | 危险的微笑一拉，弹指让斯特拉斯莫男爵夫人的红酒泼上前襟 | `:271` `flicked her fingers at Lady Strathmore’s goblet`；`:271` `sloshed down the front` |
| 43 | 海伦娜笑她坏，她答「我和女巫们待久了，肯定被带坏了」 | `:274`／`:277` |
| 44 | 狐狸在裙摆之间昂首走过，心声「众人只是不敢招惹它的怒气」 | `:283` `They’ve noticed me. They just don’t dare court my wrath.` |
| 45 | 制造丑闻正是公爵夫人买裙请她的原因 | `:289` |
| 46 | 低领水晶、如罪一般红；寡妇守寡第一个月最不该穿 | `:292` |
| 47 | 一周前只想让上流社会滚蛋 | `:295` |
| 48 | 舞厅中央、海伦娜一身如水流过皮肤的海蓝礼服、不同的声明 | `:298` |
| 49 | 预备一种新的女士、不再在顺从的祭坛上自我牺牲、拒绝消失 | `:301` |
| 50 | 联排宅改未婚妈妈与受虐女性的避难所，与海伦娜交换坏笑 | `:304` |
| 51 | 克莱奥与托马斯走来，托马斯为流言动怒 | `:307`／`:310`／`:313` |
| 52 | 托马斯问怎么忍住不动手 | `:322` |
| 53 | 「这些蠢货永远不会懂的东西是爱」 | `:325` |
| 54 | 公爵夫人一句「只有蠢货才会看出不当之处」 | `:337` |
| 55 | 海伦娜看克莱奥，火女巫眨眼送来热风，两人借露台离场 | `:343` |
| 56 | 不在乎任何人的认可；也许永远不能在舞厅共舞、在海德公园接吻、在牧师与亲友面前宣告 | `:355` |
| 57 | 星空、月光、夜莺邀舞 | `:358` |
| 58 | 共舞摇摆，哈姆雷特像哨兵守着两颗一同跳动的心 | `:364` |

---

## 三、错

### 阻断（E1–E2）

| # | 位置 | md 写法 | 原文（行） | 改法 |
|---|---|---|---|---|
| E1 | md:10 | 「**她反问哥哥**是怎么忍住不动手的」 | `:322` `‘How did you endure these insipid fools saying such things about your family without punching one or two of them in their smug little faces?’ **Thomas growled.**`；`:325` `Cynthia smiled at her brother.`——问句出自托马斯，辛西娅是回答者 | 改为「哥哥反问她是怎么忍住不对这些人动手的」 |
| E2 | md:10 | 「说**自己与这些人永不会懂**的东西是爱」 | `:325` `We have something these fools will never understand. Love.`——不懂的是「这些蠢货」，辛西娅与海伦娜正是拥有爱的人 | 改为「说这些蠢货永远不会懂的东西是爱」 |

### 提示（P1–P33）

| # | 位置 | md 写法 | 原文（行） | 改法 |
|---|---|---|---|---|
| P1 | md:10 | 「她**当众宣布**要把芒特罗街的联排宅改成…避难所」 | `:304` `‘If they think this dress is a scandal, wait until they hear that I’m turning my Mount Row townhouse into a refuge…’`——话是对海伦娜说的，`wait until they hear` 说明尚未公开 | 改为「她对海伦娜说要…」 |
| P2 | md:10 | 「…接着说自己告诉警司休伯特是自杀，辛克莱…」 | `:207` 这段在 `:210` 希金斯太太哭诉**之前**；md 把它排在 `:216`「保护无辜者不是罪」之后 | 前移：先写「告诉她警司那边已经了结」，再写老太太哭诉 |
| P3 | md:10 | 「辛克莱虽是混蛋却不会出卖她、他的话也压不过她的话」 | `:207` `he won’t betray you. **If he does**, his word will never stand against mine.`——「压不过」有前提 | 补「即便他真供出她」 |
| P4 | md:10 | 「心里说众人只是不敢招惹**她**的怒气」 | `:283` 说话者是狐狸哈姆雷特（`his tail`、`his wrath`），不是辛西娅 | 改为「不敢招惹**它**的怒气」 |
| P5 | md:11 | 「是全章情感的最高点，也是**唯一发生在室内的高点**」 | 第二场景（`:153`–`:243`）同样在室内，且 md:11 下一句自己说「全章真正的泪点在这里」 | 删「唯一」，或改为「第一段的高点在室内」 |
| P6 | md:11 | 「**门厅**里白得吓人的脸」 | `:196` `The poor woman’s face had gone frighteningly pale` 发生在侯爵夫人套房（`:168` 明写 `marchioness’ suite`）；门厅只在 `:162` 出现 | 改为「套房里白得吓人的脸」 |
| P7 | md:12 | 「泼酒小报复（**一句**闲话换一次法术）」 | `:262`／`:265`／`:268` 共三句 | 改为「三句闲话换一次法术」 |
| P8 | md:13 | 「并**当众**放弃夫姓」 | `:237` 发生在套房内，在场只有海伦娜与希金斯太太 | 改为「在管家面前放弃夫姓」 |
| P9 | md:13 | 「这是她**全书第一次**克制自己的能力」 | `ch14:216` `Aunt Rowan’s thoughts echoed in Helena’s head.`——她听到罗温的心声后并未揭穿；跨章「第一次」无据 | 改为「这是她少有的克制自己的能力」 |
| P10 | md:13 | 「希金斯太太从上一章**一句**被提及的名字…」 | `ch26:237` 与 `ch26:309` 两处点名 | 改为「从上一章两处被提及的名字」 |
| P11 | md:14 | 「誓词出现两次、逐字重复、**只改末词**」 | `:53` 结尾 `for the rest of my days.`；`:56` 结尾 `Always.`；且称呼 `Cynthia,`／`Helena,` 也不同 | 改为「只改称呼与结尾一句」 |
| P12 | md:19 | 「我一直在**当**天底下最大的傻子」 | `:38` `I’ve been the biggest fool.`——中文病句（「在当…傻子」） | 改为「我一直是天底下最大的傻子」 |
| P13 | md:23 | 「**四句话**里三句是失去的恐惧、一句是自我羞辱」 | `:38` 引语实为六句：`my world stopped.`／`living without you is impossible.`／`I love you, Cyn.`／`I’m not afraid of that any more.`／`The only thing that scares me is losing you.`／`I’ve been the biggest fool.` | 改为「六句」并重算归类，或删数字 |
| P14 | md:23 | 「是全章**唯一一处**对读者的解释」 | 「对读者的解释」无客观口径，且 `:243`、`:352` 等处同样在向读者补信息 | 删「唯一一处」 |
| P15 | md:25 | 「作者让**被爱者先开口**，被爱的一方先用眼睛回答」 | 先开口的是海伦娜（爱人者），辛西娅是被爱者；同句自相矛盾 | 改为「作者让爱人者先开口，被爱的一方先用眼睛回答」 |
| P16 | md:43 | 「这也是**下一章**她能逐句回应的前提」 | 回应在**同一章** `:56`，紧接两块之后 | 改为「这也是紧接的回应能逐句成立的前提」 |
| P17 | md:63 | 「这与**上一章**海伦娜心里那句嘀咕…」 | `ch25:141` `A proper lady like Cynthia Burrows would never use such coarse language.`——是**两章前**（上一章是 ch26） | 改为「这与 ch25 海伦娜心里那句嘀咕…」 |
| P18 | md:73 | 「佛手柑在**上一章**是辛西娅靠风辨出爱人就在附近」 | `ch25:41` `the wind breathed over her, carrying with it the scent of bergamot`——在 ch25，不是上一章 | 改为「在 ch25」 |
| P19 | md:73 | 「『再飞一次』回指**其后第三自然段**两人离床三尺悬着」 | 悬空在 `:125`，在原句（`:137`）**之前** | 改为「回指此前的悬空」 |
| P20 | md:93 | 「四个短句，**每句都比前一句短**」 | `:198` 四句词数 2／8／5／6，并非递减 | 删「每句都比前一句短」 |
| P21 | md:113 | 「是**全书阶级语言第一次**被她自己拆掉」 | 跨章最高级需全书取证；`ch22:177` 她已在为被休伯特开除的女仆奔走 | 删「第一次」，改「是全书少有的…」 |
| P22 | md:117 | 「正是这句…的**公开兑现**」（同段前文称「当众说出来」） | `:304` 是对海伦娜私下说的 | 改为「私下说出来」 |
| P23 | md:123 | 「**最后两句都是名词短语开头、无主语无动词**」 | `:301` 末两句：`Because she possessed something far more valuable than their approval.`（有主语 she、动词 possessed）；`Determination to live an authentic life, consequences be damned.`（前为名词短语，后为从句） | 改为「最后一句是名词短语＋独立从句，节奏像签字」 |
| P24 | md:133 | 「『牧师、朋友、家人』在上一自然段被**明文放弃**」 | `:355` `We might never be able to ... declare our love in front of a priest and all our friends and family.`——是承认也许永远做不到，不是放弃 | 改为「在上一自然段被明说也许永远做不到」 |
| P25 | md:135 | 「读者会记得**每一次**需要独处时，克莱奥的火都在场」 | 全书只 `ch27:343` 有一次「热风清场」；`ch20:168` 是仪式点烛，不是独处 | 改为「这一次需要独处时，克莱奥的火正好在场」 |
| P26 | md:143 | 「『心跳同步』回收**上一章**辛西娅隔着一栋楼要找的那个节拍」 | `ch25:41` `Her heart thumped painfully, straining for the rhythm of its mate.`——在 ch25，不是上一章 | 改为「回收 ch25 的那个节拍」 |
| P27 | 词表 md:173 | `bodice`｜「上身衣身，**紧身胸裙**」 | `:307` `The bodice comprised rich purple lace... rose high around her shoulders in a structured collar.`——bodice 是连衣裙的上半身（含肩部结构），不是「紧身胸裙」 | 改为「连衣裙的上半身」 |
| P28 | 词表 md:154 | `unbreakable`｜「**不可破解的**」 | `:59` `binding their spirits into an unbreakable union`——指结合不可破 | 改为「牢不可破的」 |
| P29 | md:117（形态 F7） | 原句11 在 `altar of obedience.` 与 `But she refused…` 之间插 `…` | `:301` 被删的是一整句 `They could spread gossip about her, cut her direct on Bond Street, refuse to send her invitations to their soirées and garden parties.`，与前后同属**同一自然段**，无段差 | 补回该句，或把省略号改为句号并另起一块（**禁增第 14 块 ⇒ 只能补回**） |
| P30 | md:10（补漏 L1） | 「…本该立刻坦白、不能让别的女孩再受害」 | `:192` 另有 `I won’t let anyone else suffer for my choices.` | 补「也不让人替自己的选择受罪」 |
| P31 | md:10（补漏 L2） | 「给她优厚退休金，安排事务律师面谈退休细节」 | `:231` 海边小屋、终身不愁的收入、贬 Lady Argyle（`The horrid Lady Argyle could never appreciate someone of your excellence.`） | 补「海边小屋与终身收入，并说她会被 Lady Argyle 浪费」 |
| P32 | md:10（补漏 L3） | 「要把芒特罗街的联排宅改成…避难所」 | `:304` 后半段：仍保留 Cotswold 宅，夏天在海伦娜的 All Things Bright and Beautiful 帮忙，两地分住 | 补「夏天去 Cotswold，在海伦娜的 All Things Bright and Beautiful 帮忙」 |
| P33 | md:10（补漏 L4） | 「海伦娜意味深长地看克莱奥，火女巫眨眼送来一阵热风」 | `:352` 海伦娜读到公爵夫人的念头，据此说「we have her blessing」，并说她还给了「some ideas to try with you later」 | 补「海伦娜读到她已默认祝福，还说她留了些主意」 |

---

## 四、R4 逐块对应（13 块）

| 块 | md 行 | 原文行 | 内容 | 说话人／主语 | 受事 | 判定 |
|---|---|---|---|---|---|---|
| 1 | 17 | `:38` | 海伦娜自白：世界停住、不能没有你地活 | 海伦娜 | 辛西娅 | ✔ |
| 2 | 27 | `:47` | 手覆心口、描新月、请求立新誓 | 海伦娜 | 辛西娅 | ✔ |
| 3 | 37 | `:53` | 四句誓词 | 海伦娜 | 辛西娅 | ✔ |
| 4 | 47 | `:56` | 辛西娅回誓，结尾改「永远」 | 辛西娅 | 海伦娜 | ✔ |
| 5 | 57 | `:113` | 「你是我的夫人，此刻与永远」 | 海伦娜 | 辛西娅 | ✔ |
| 6 | 67 | `:137` | 「傻女巫…再飞一次」 | 辛西娅 | 海伦娜 | ✔ |
| 7 | 77 | `:177` | 口干、花瓶旋转 | 海伦娜（叙述） | 花瓶 | ✔ |
| 8 | 87 | `:198` | 「不是为了对质，是为了道谢」 | 辛西娅 | 希金斯太太 | ✔ |
| 9 | 97 | `:225` | 「你放了我，现在轮到我」 | 辛西娅 | 希金斯太太 | ✔ |
| 10 | 107 | `:237` | 「我们都自由了」 | 辛西娅 | 希金斯太太 | ✔ |
| 11 | 117 | `:301` | 预备新的女士、拒绝消失 | 辛西娅（叙述） | 上流社会 | ✔（省略号见 P29） |
| 12 | 127 | `:358` | 星空月光夜莺、邀舞 | 海伦娜 | 辛西娅 | ✔ |
| 13 | 137 | `:364` | 共舞、哈姆雷特作哨兵 | 两人／哈姆雷特（叙述） | 彼此 | ✔ |

**块序**：`38＜47＜53＜56＜113＜137＜177＜198＜225＜237＜301＜358＜364`——**0 调转**。
**说话人**：13 块内所有直接引语逐条归属（海伦娜 4 处、辛西娅 5 处、其余为叙述），**0 错**。

---

## 五、形态（8 项）

| 项 | 结果 |
|---|---|
| F1 块数 | `blocks=13` vs `block_target=[6,10]`；`block_hint` 是提示型、rc 仍 0 ⇒ **禁增第 14 块** |
| F2 块格式／外层引号 | 13 块全部 `> **原句 N:** "…"`；编号 1–13 连续；无断号 ✔ |
| F3 四子项 | 中文理解／关键词／为什么这样写／读者视角提示 各 13/13 ✔ |
| F4 词表 | 24 行＝高级 9／进阶 9／基础 6；标准 Markdown 表 ✔ |
| F5 块内引号 | 原句4、6、8、9、10、12 的内层引语均与外层引号区分 ✔ |
| F6 独立尺子 | `/tmp/hx_md_frag.py` → `checked=14 BAD=0` ✔ |
| F7 省略号 | 原句11 的 `…` 删的是同一自然段内一整句、无段差 ⇒ **提示 1 条（P29）**；其余 12 块无省略号 |
| F8 导航 | 5 项（一句话概括／情感弧线位置／Tropes 兑现反转／人物弧线／叙事手法）✔ |

---

## 六、实跑取证

| 项 | 命令 | 输出／退出码 |
|---|---|---|
| A 门禁 | `bash scripts/chapter.sh "<md>" --json` | `verdict=ok`；`blocks=13`、`segments=14`、`segment_miss=0`、`words=3244`、`block_target=[6,10]`、`issues` 全空；`rc=0` |
| B 独立尺子 | `python3 /tmp/hx_md_frag.py "<md>" "text/ch27_chapter_27.txt"` | `checked=14 BAD=0`；`rc=0` |
| C R1 片段 | 逐条 `verbatim` 比对（整串优先，含原生省略号的整行按原串核） | `events=65 checked=76 BAD=0` |
| D 空白带 | `python3` 连续空行统计 | `(138,152,15)`／`(244,258,15)`；另 `(2,21,20)`／`(23,34,12)` 是卷首，`(365,383,19)`／`(385,390,6)` 是推广页 |
| E 推广页 | `/usr/bin/grep -n "MORE FROM" text/ch27_chapter_27.txt` | `384:MORE FROM DARCY McGUIRE`；末行 `394` 为 URL |
| F ch26 点名 | `/usr/bin/grep -n "Higgins" text/ch26_chapter_26.txt` | `237`／`309` 两处——P10 依据 |
| G ch25 嘀咕 | `sed -n '137,145p' text/ch25_chapter_25.txt` | `:141` `A proper lady like Cynthia Burrows would never use such coarse language.`——P17 依据 |
| H ch25 佛手柑与节拍 | `/usr/bin/grep -n "bergamot" text/ch25_chapter_25.txt` | `:41` `carrying with it the scent of bergamot`＋`straining for the rhythm of its mate`——P18／P26 依据 |
| I ch14 克制先例 | `sed -n '210,225p' text/ch14_chapter_14.txt` | `:216` `Aunt Rowan’s thoughts echoed in Helena’s head.`，她听见后未揭穿——P9 依据 |
| J 三句闲话排版 | `/usr/bin/grep -rn "^‘…" text/ch*_chapter_*.txt` | 仅 `ch27:262/265/268` 三行——md:14「以省略号起头的独立段」成立 |
| K 火女巫清场 | `/usr/bin/grep -rn -i "clio.*\(fire\|heat\|warm\|hot air\|blast\)\|firewitch" text/` | 隐私清场只有 `ch27:343`；`ch20:168` 是仪式点烛——P25 依据 |
| L 誓约全书分布 | `/usr/bin/grep -rn -i "oath\|vow" text/ch*_chapter_*.txt` | 共 20 行：ch02/03/12/16(3)/18(4)/20/21(3)/22/24/26(2)/27(2)；无更早的「邀请对方立新誓」场景 |
| M 计数 | `python3` 解析 md | 块行 `17/27/37/47/57/67/77/87/97/107/117/127/137`；四子项 13/13；词表 9/9/6；导航 5；原句11 原串 2 段 |

---

## 七、悬置（不裁决）

| # | 悬置点 | 原文状态 |
|---|---|---|
| U1 | `Dear God. She knows.` 是希金斯太太的心声还是海伦娜的领悟 | `:192` 明写 `Mrs Higgins’ terrified thoughts echoed in Helena’s head`，两读皆可；md 取前者，不裁 |
| U2 | 旋转的花瓶由谁的力量带动 | `:177` 未写；两位女主都能以意念动物 |
| U3 | 辛克莱是否真会供出希金斯太太 | `:207` 是辛西娅的判断，章内未发生 |
| U4 | 辛克莱最终是否被定罪 | 本章只写舞会与收容所，未提审判 |
| U5 | ch26 的照片与逃走巨人的下落 | 本章零提及 |
| U6 | 公爵夫人是否确切知道两人的关系 | `:331`–`:337` 是暗示与打趣，未明写 |
| U7 | 公爵夫人「ideas to try with you later」具体所指 | `:352` 未展开 |
