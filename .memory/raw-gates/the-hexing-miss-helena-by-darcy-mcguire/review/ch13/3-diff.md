# ch13 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，326 行全读，96 事件 / 10 关系 / 10 数字 / 5 未决 / 16 陷阱）与 `2-machine.json`（rc=0 / verdict ok / blocks=8 / words=2553 / block_target=[5,8] / segments=8）。
> 机器层：`segment_miss=0`（引语逐字）、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`、`template=0`、`hole=0`、`empty_quote=0`。
> 补验（机器盲区）：本章 8 条引语**无一条含 `…`**（R0 全书级 `verify_fragments_indep.py` 312 片段 / 0 MISS 已覆盖）；22 行词表例句 **22/22 逐字回源命中**（`/tmp/vocab_check_hx.py 13`：`ch13: rows=22 missing=0`）、**22/22 词头落在例句内**（`/tmp/vocab_head_hx.py`，无输出＝零失配）；**引号配对**探针 `/tmp/pair4_hx.py` 全书扫描 ⇒ 全书 TOTAL 1（唯一一处在 ch09 原句 7），**本章 0 处偏离**。

---

## 〇、本章结构要点（对账前先钉住）

- **单 POV**：全章贴辛西娅（`:35`–`:326`），**不是**双 POV 切换章（与 ch12 不同）。
- **无引号的心声段**共 4 处，归属必须分清：`:95`＝**海伦娜**的心声、`:164` `She is mine.`＝**辛西娅**的心声、`:293`＝**辛西娅**对狐狸说、`:296`＝**狐狸哈姆雷特**的心声。
- **闪回**：`:212`–`:260` 是辛西娅七岁生日那天的记忆（恩师史密斯夫人 + 母亲 + 托马斯在场），`:263` 马车一停拉回当下。
- **三段式**：车厢内的读心试探（`:35`–`:101`）→ 坦白与克拉拉往事（`:104`–`:209`）→ 闪回（`:212`–`:260`）→ 门口告别与新名字（`:263`–`:326`）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号 + 逐字） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:209` `Cynthia took Helena’s hand from her thigh and pressed her lips against the other woman’s fingers… ‘I’ve always believed in facing my fears. Sometimes, it is better to leap than dither with uncertainty.’ … she couldn’t remember what if felt like to just be **Cyn**.` —— 辛西娅**主动**吻对方手指、并说出「跳下去比犹豫好」的宣言 | md **未覆盖**（导航·人物弧线只写「把欲望说出口」，指的是 `:110` 的坦白，不是 `:209` 的主动选择） | **不构成阻断**（人物弧线有概括性覆盖）；⚠️ 但这是辛西娅侧本章的情感转折点，**建议**在导航·人物弧线补半句 |
| L2 | `:269` `She had instructed the driver to take them to Helena’s home first before returning Cynthia to **the house she would soon be leaving**.` —— 辛西娅**即将搬离**现住处 | md **全篇未提** | **不构成阻断**（一句副线信息，去向原文亦未说）；**建议**补——这是全书唯一一处明示她要离开那栋房子 |
| L3 | `:176` `‘Nothing happened. We were just children. Clara was in love with the stable master’s son. She used to rhapsodise endlessly about the lad’s brown eyes.’` —— 海伦娜**主动澄清**「什么也没发生」、克拉拉当时爱的是马厩管事之子 | md **未覆盖**（原句 5 的引语止于 `It was then I knew.`，导航只写「初次心动」） | **不构成阻断**（覆盖取舍）；⚠️ 但「初次心动」这个概括**只靠 `:176` 的澄清才不至于被读成一段旧情**，建议导航补「什么也没发生」四字 |
| L4 | `:83` `A crimson curl broke free as she shook her head. ‘No. **With you, it’s quiet.**’` | md 只在导航·Tropes 里概括为「能读人心的海伦娜偏偏读不到辛西娅」，**未收这句原文表述** | **不构成阻断**（概念已覆盖） |
| L5 | `:71` `‘Sometimes, people are thinking so loudly, I don’t have to delve into my magic at all… Other times, when I’m seeking a particular truth, **I have to push**, and then my eyes change.’` —— 眼睛变银的**机制**（被动听见 vs 主动用力推） | md **未覆盖**（导航只写「眼睛在暗处转成银色」） | **不构成阻断**（设定细部） |
| L6 | `:227`–`:233` 封口费从「**double**」谈到「**Triple**」，母亲接受并威胁 `‘…I will decimate you. When I’m through, you won’t be fit to train field mice.’` | md 导航／总结只写「女教师向母亲告状、母亲盼魔法绕过女儿」；**这段交易与威胁未进分析层**，只在词表里以 `wages`、`decimate` 两个词头露头 | **不构成阻断**（未构成情节转折）；⚠️ 与 E4 同源——正因为漏了这段，总结里才会写成「**只**盼」 |
| L7 | `:317` `‘No idea. But Uncle Lachlan might know. And if he doesn’t, he’ll find out.’` —— 下章钩子 | md **未提** | **不构成阻断**（钩子非本章主弧） |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–8 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的十一处疑点：

1. **「十岁的哥哥托马斯」**——`:245` `He was ten, only three years older than her` ⇒ **成立**（且与 `:248` `her seventh birthday` 互证：10−3＝7）。
2. **「随即被女教师拉走，第二天就要去上学」**——`:245` `as Governess Smithers pulled him away` ＋ `:242` `You’re leaving for school on the morrow` ⇒ **成立**。
3. **「九、十岁那年」**——`:158` `I was near to nine or ten` ⇒ **成立**（原文为模糊表述，md 未写成确数）。
4. **「心里第二次冒出『她是我的』」**——`:164` `She is mine.` ＋ `:167` `For the second time` ⇒ **成立**（第一次在 ch11 `:89`，跨章引用正确）。
5. **「辛克莱脑中闪过的名字乔治·利珀特」**——`:305` `the name that came into his mind` ＋ `:311` `he thought it clear as church bells on Sunday. George Lippert.` ⇒ **成立**；且 md **没有**写成「辛克莱供出了凶手」（`:311` 明写 `Not intentionally`）⇒ **未越级**。
6. **「两人同车回梅费尔」**——`:35` `towards Mayfair` ⇒ **成立**。
7. **「俱乐部 The Devil’s Bargain」**——`:35` `outside The Devil’s Bargain` ⇒ **成立**。
8. **「狐狸哈姆雷特用一句气味的问题，把两人之间的亲密点破」**——`:95` `Like why you two smell of each other.` ＋ `:98` `some magic must be at play to let her hear Helena’s familiar` ⇒ **成立**。
9. **「母亲也曾被绕过、她自己的母亲也是」**——`:260` `As it did me, and my mother.` ⇒ **成立**（三代血缘，md 未写成两代）。
10. **「恩师告她跟动物低语、召来天气」**——`:221` `I’ve seen her whispering to the animals. Conjuring all kinds of weather.` ⇒ **成立**。
11. **md 没有犯以下四类常见凭空**：没有写「海伦娜能读动物心思」（正确保留 `:323` `Only people`）；没有写「辛西娅是女巫」（正确保留 `:326` 的自我否认）；没有写「克拉拉是海伦娜的恋人」（正确保留 `:176` `Nothing happened`）；没有写「母亲反对魔法」（`:260` 母亲说的是「魔法在这个世界没有位置」，md 原句 6 的分析「句句是在关门」与此相合）。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| **E1** | 原句 1·读者视角提示 | 「读者读完这句会知道，**这一章要交代的不是案情**，而是她怎么重新看自己」 | `:305` `He said there were others who had reason to murder Hubert, but what he didn’t tell us was the name that came into his mind.`；`:311` `George Lippert.`；`:317` `‘No idea. But Uncle Lachlan might know. And if he doesn’t, he’ll find out.’` —— **本章章末正是案情推进**；且**同一 md** 的原句 7·读者视角提示写「这一句**把追查的方向整个换了**：此前问的是辛克莱，现在多出一个从没听过的人」 | 章级内容断言与原文矛盾，**且与自身原句 7 自相矛盾** ⇒ **阻断**（本章第一优先修复项） |
| **E2** | 原句 5·为什么这样写（末句） | 「气味写得比动作更牢，**那个雨天**就这样被一句话钉住」 | 原句 5 的引语从 `Clara and I hid together in a linen cupboard.` 起，**不含**「雨天」；雨天在引语之外的上一句 `:158` `It was a rainy day, and we were playing hide-and-seek. Ellie was seeking us.` | 分析覆盖的原文比引语长（引语截短型越界）⇒ **阻断**（轻）：所述事实本身为真（`:158`），故修法是换词而非撤回 |
| E3 | 原句 8·为什么这样写（首句） | 「四句都短，**句子之间没有连接词**，读起来像一句接一句地给自己找理由」 | 引语自身：`**But** she saw Helena’s lips press together. She shouldn’t have asked. It was impossible **at any rate**. She wasn’t a witch, **no matter what** the fox said.`；且 md 自己的中文理解把 `at any rate` 译作「**反正**」 | 措辞级：四个句子**之间**按字面确实无连接词（`But` 在首句句首、`at any rate` 在第三句句内），但读者眼前的引语里 `But` 与「反正」都在 ⇒ **提示**。⚠️ **与 ch12 E1（阻断）的区分**：ch12 那句「两句之间没有转折词」被 `But` **正好夹在所描述的两句中间**当场证伪；本章的「句子之间」仍可字面成立，只判提示 |
| E4 | 一句话总结（`:139`） | 「女教师告她跟动物低语、召来天气，**母亲却只盼魔法绕过女儿**」 | `:218` `‘…Whatever is wrong, **train it out of her**.’`；`:227` `‘…**I will double your wages** to keep what you have seen a secret.’`；`:230` `‘Triple.’`；`:233` `‘Fine. But if you breathe a word of this, **I will decimate you**…’` | 「只」字把母亲的**三项行动**（吩咐训练掉／买沉默／威胁毁人）压成一句心愿 ⇒ **提示**（与 L6 同源） |
| E5 | 导航·叙事手法 | 「中段插入一段**没有过渡的**童年闪回，靠马车一顿把人拽回现在」 | `:212` `**A memory flashed, fast and vivid.**` —— 明示的过渡句；且 `:209` 末句 `she couldn’t remember what if felt like to just be Cyn.` 已是软引子；`:263` `The carriage lurched to a stop.` ＋ `:266` 把人拉回（这半句 md 说对了） | 技法描述与原文相反 ⇒ **提示**（本章第二优先修复项） |
| E6 | 导航·人物弧线 | 「那份沉默既让她**挫败**，也让她**着迷**」 | `:89` `‘It’s **frustrating**. I’m used to the constant noise, but the silence is impossible.’`（挫败 ✓）；`:200` `You **bewilder** me.`（＝摸不着头脑）；`:131` `**Infuriatingly** so.` | 「挫败」有直接对应；「着迷」在原文**无对应词**，最接近的是 `bewilder`（困惑）⇒ **提示**（措辞级） |
| E7 | 原句 3·为什么这样写 | 「先写她猛一转头，再写狐狸的闲适：舔嘴、搁鼻子，**一副说完就不管的样子**」 | 引语（`:98`）只有 `He licked his chops and placed his sharp nose between delicate paws.`；「说完」这件事在引语之外的 `:95`（狐狸的心声） | 「说完」依赖引语外的一句，但 md 导航已写「狐狸哈姆雷特在心里插话」⇒ 全篇内部可自证，**提示**（轻） |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 纱被揭掉、她看清了；外面没变，变的是她心里 | 「纱被揭掉」为被动、**施事未写**（md 未代填）；「看清」＝辛西娅 | 她的眼睛／外面的世界与她内心 | 「外面」＝俱乐部外，「里面」＝辛西娅 | **对应成立**（但见 E1：读者视角提示的章级断言越界） |
| 2 | 眼睛开始变；暗里辨不出颜色，只看见变亮、发光、转银 | 海伦娜的眼睛 | 颜色（shade） | 「结冰」比喻归叙述者 | **对应成立** |
| 3 | 她猛转头看狐狸；狐狸舔嘴搁鼻；她没感到失重，但一定有魔法在起作用 | 辛西娅（转头／没感到）；狐狸（舔嘴／搁鼻子） | 狐狸；她自己的感觉 | 「一定」＝**辛西娅的推断**，md 写「说明她拿不准，只肯把这件事归给某种魔法」⇒ 未升格为叙述者断言 | **对应成立**（「说完」见 E7） |
| 4 | 答应过的事不反悔；头发像落日、像秋色；想尝她 | 辛西娅 | 承诺／头发／海伦娜 | 「想尝你」＝辛西娅对海伦娜 | **对应成立** |
| 5 | 那天两人躲在亚麻橱；记得浆粉和梨的气味；克拉拉贴着她，她活了过来；那一刻她明白了 | 海伦娜（说）；克拉拉与海伦娜（躲）；克拉拉（贴） | 橱柜／气味／海伦娜的身体 | 「她明白了」＝海伦娜自述；md 未替她说明「明白了什么」（原文亦未说） | **对应成立**（但「那个雨天」越界 ⇒ E2） |
| 6 | 母亲说本盼魔法绕过女儿，如当年绕过她与她母亲；女儿注定做贵妇；魔法没有位置；叫她走 | 母亲 | 女儿／魔法 | 「绕过我，也绕过我的母亲」＝母亲自述**三代** | **对应成立** |
| 7 | 他并非有意说出；当她问是谁杀了她丈夫时，他心里清楚得像周日教堂钟声；名字是乔治·利珀特 | 海伦娜（转述）；辛克莱（想） | 那个名字 | `when **you** asked` → md 译「当**她**问」＝辛西娅 ⇒ 方向正确 | **对应成立** |
| 8 | 她看见海伦娜抿嘴；她不该问；反正不可能；不管狐狸说过什么，她都不是女巫 | 辛西娅（看见／后悔／否认） | 海伦娜的嘴唇／她自己 | 「不管狐狸说过什么」＝辛西娅内心；md 未替原文裁决她究竟是不是女巫 | **对应成立**（但「没有连接词」见 E3） |

**R4 无「分析讲全书主旨」「只复述字面」两类失配；唯一一类失配是「分析讲到引语之外」（E2、E7）。**

## 五、形态

`H1 = 13. Chapter Thirteen`（形状合规）；导航 **5** 项；子项 **4** 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 **8**，落在本书区间 [6,13] 与本章 `block_target=[5,8]` 内 ⇒ **已触上限**：若因修复 E2 而**扩引语**（把 `It was a rainy day…` 并入原句 5），不会增块，安全；但**不得新增第 9 块**，否则触发 `block_count`。

### 引号配对（机器层零覆盖，自建探针）

`/tmp/pair4_hx.py` 全书扫描 ⇒ 全书 **TOTAL 1**（唯一一条在 ch09 原句 7）；**ch13 八个引语块全部配对完整**（含原句 4、原句 5 这类从对白中途切起的形态）⇒ **本章引号配对 0 偏离**。

## 六、语料层观察（非 md 缺陷，不计入三张单子）

### ⚠️ 更正早前记录：全书站点推广行是 **5 章 8 行**，不是「5 章 6 行」

早前（ch08 §六）记为「ch03:188 / ch08:170+173 / ch13:185 / ch19:197 / ch25:214」＝ 6 行，**漏算了 ch13 `:182` 与 ch19 `:194` 各一行**。本轮用 `/usr/bin/grep -rn -E "Lokepub|wait quietly in the background|Add one to your list"`（rc=0）重扫全书，并回读上下文确认：

| 章 | 行号 | 逐字 |
|---|---|---|
| ch03 | `:188` | `Look up Lokepub on Google for more options.` |
| ch08 | `:170` | `Still in the reading mood?`（该行不含 Lokepub 字样，靠上下文认定为同一广告单元的抬头） |
| ch08 | `:173` | `You can find more novels waiting at Lokepub.` |
| ch13 | `:182` | `A new book can wait quietly in the background.` |
| ch13 | `:185` | `Add one to your list from Lokepub.` |
| ch19 | `:194` | `A new book can wait quietly in the background.` |
| ch19 | `:197` | `Add one to your list from Lokepub.` |
| ch25 | `:214` | `You may find the next one at Lokepub.` |

⇒ **合计 5 章 8 行**（ch13 与 ch19 是同一段两行广告，逐字重复）。

### ⚠️ 反面陷阱：ch13 `:287` **不是**推广行，是正文（狐狸的心声）

`Secrets have a way of bubbling up. Good luck with yours.`（`:287`）极易被误认作广告：它同样是**无引号独立段**、同样是**面向读者的口吻**。三条证据判定它是**正文**：

1. `/usr/bin/grep -rn "bubbling up" text/`（rc=0）**全书仅命中 ch13:287 一处**；而真广告行都是**跨章逐字重复**的（ch13 `:182`/`:185` ＝ ch19 `:194`/`:197`）。
2. 上下文构成一组完整对话：`:284` 海伦娜 `‘How unfortunate.’` → `:287` 狐狸插话 → `:290` `Hamlet sprang to his feet` → `:293` `You are not helpful. Cynthia glared at the fox.`（**辛西娅的回嘴**）→ `:296` `I’m incredibly helpful.`（**狐狸的答话**）。若 `:287` 是广告，`:293` 就成了无来由的一句。
3. `:326` `She wasn’t a witch, **no matter what the fox said**` 需要「狐狸说过话」这一前提；`:287` 正是本章狐狸说的第二句（第一句是 `:95`）。

**误判后果**：会把一句正文心声当语料污染删掉／漏掉，并使「狐狸说过什么」少算一条（本章素读底稿曾一度把它记为推广行，已在本轮更正，见 `1-suread.json` 的 event 83 与 trap T4b）。

### 原文自身瑕疵（不得「修正」、不得当作语料污染）

- `:209` `she couldn’t remember what **if** felt like to just be Cyn` —— `if` 疑为 `it` 之误（原文如此，md 未引用此句，无影响）。
- `:131` `You make it **dashed** difficult` —— `dashed` 作强化副词（＝该死的／异常的），非错字；md 词表未收，亦未误释。

### 跨章术语不一致（进汇总修复指令文件，**本章不改**）

| 词 | 本章写法 | 其他章节写法 | 处置 |
|---|---|---|---|
| decimate | 词表释「毁灭，严惩」（例句 `:233` 母亲威胁恩师） | ch11 词表释「大量毁掉，严重削弱」（例句 `It would decimate her family and her livelihood.`） | 列入汇总：两处语境不同，释义可各自成立，但**同一本书同一词头给两种释义**须统一口径 |
| Governess Smithers | 「女教师」／词表 `governess` 释「女家庭教师」 | ch11 的管家 **Smith** 是另一人 | ⚠️ 记录在案：**Smithers（恩师）≠ Smith（管家）**，不可混同；本章 md 未混 |
| Ellie | 本章 `:158` 素读作「艾莉」 | ch09 `:53`/`:242` 幻象（深红天鹅绒＋黑蕾丝房间）同一人 | 本章 md **未提**艾莉（原句 5 的引语不含该句），无冲突 |
