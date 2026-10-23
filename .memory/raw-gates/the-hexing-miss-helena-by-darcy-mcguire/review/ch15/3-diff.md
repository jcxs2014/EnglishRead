# ch15 · R3 对账（三张单子）＋R4 逐块对应

> 审查对象：`notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/ch15 the parlour kiss.md`（160 行，**未改**）
> 语料：`text/ch15_chapter_15.txt`（309 行有效内容，末行 `:309`）
> 素读底稿：`1-suread.json`（100 events / 12 rel / 12 num / 8 unresolved / 25 traps，BAD 0，含行号回验）
> 机器层：`2-machine.json`（rc=0 / verdict ok / blocks 10 / words 2923 / segment_miss 0）
> 读取顺序：先素读落盘、后开 md（铁律未破）

## 〇 结构要点（判定前必须先钉住的七件事）

1. **POV 在章中途换人，这是全书前十四章没有过的形态。** 第一场（`:35`–`:131`，晚宴散场·门厅）贴**海伦娜**；第二场（`:147`–`:309`，一周后·辛西娅家前客厅）贴**辛西娅**；`:133`–`:145` 是 13 行空白的场景分隔。⇒ 心声归属必须按场分：`:116`/`:128`/`:131` 归海伦娜，`:195`/`:249` 归辛西娅，跨场归错即阻断。
2. **四处心声各有主人，且两个不属于人。** `:83` `That wasn’t me.` ＝**罗温**（归属由 `:80` `She shook her head.` 与 `:86` `Thomas glared at Aunt Rowan` 双重钉住）；`:192` `Don’t ask me for advice. I’m in love with a ferret.` ＝**狐狸哈姆雷特**（由 `:189` 它跟着女主人小跑、`:195` 辛西娅回嘴 `A lot of help you are.`、`:198` `He yipped an agreement.` 三点钉住）；`:116` `She is mine to protect.` ＝**海伦娜**；`:249` `Damnation! Caramel and salt. I knew it.` ＝**辛西娅**。
3. **`:77` 的能量波没有主人，原文四处都指向「没人知道」。** `:77` 只写 `A wave of energy pulsed`；`:80` 三表姐妹望向姨妈、姨妈摇头；`:83` 罗温心声否认；`:86` 托马斯**误以为**是姨妈（`no doubt assumed she orchestrated the magical moment`，`He`＝托马斯，且这句是海伦娜 POV 下的推断）；`:89` `Cynthia didn’t seem to notice the energy shift.`。⇒ **不得断言为辛西娅所为**。
4. **三种动物伙伴不可互换。** 哈姆雷特＝狐狸（海伦娜的，`:189` `his mistress`）；奥菲莉亚＝雪貂（埃莉的，`:74` 上下文与 ch14）； Sir Robin＝鹦鹉（克里奥的，`:44`）。`:74` **拦下托马斯的是克里奥**（`Clio gripped Thomas’ arm`，火花沿他的晚宴礼服跳动），不是海伦娜（海伦娜那边是 `:71` 掌心聚水成露）。
5. **`:270`–`:297` 的施事与受事极易调转。** `:270` `They were smaller than Cynthia’s and firm` 说的是**海伦娜的**胸；`:273` 一句里两个方向相反（`Pull pleasure from Helena the way Helena was pulling Cynthia from her sanity`）；`:297` 留 love bites 的是**辛西娅**。
6. **两处「无主的力量」同类。** `:77` 能量波（罗温否认）与 `:270` `the sun burst from the clouds in a dazzling display of light`（海伦娜呻吟时，原文未说因果）——都不得写成某人施法。
7. **`原句 5`（`:116`）与 ch09 `Mine.` 同一条占有线、不同措辞**，不得互替；**`:249` 回收 ch13 `:113`**（焦糖与咸味）；**`:174`（想不起能唤蜂鸟的小女孩、过去像被偷走）承接 ch14 结尾「有人封住了她的力量」**——这三条跨章关系机器层零覆盖。

## 一 漏（素读有、md 无）

> 硬约束：本章 `blocks=10`，而 `block_target=[5,9]`（`block_hint`：**块数 10 偏离本章篇幅建议 5–9**，提示型、rc 仍 0）⇒ **已超上限一格，任何补漏都不得新增第 11 块**。首选改法一律落在导航层。

| # | 缺什么 | 原文逐字（`text/ch15_chapter_15.txt`） | 档 |
|---|---|---|---|
| **L1** | **吻的正体 `:240`–`:306` 全部无引语块覆盖**，导航只用「吻到一半」四字带过。文件名即 `the parlour kiss`，而十个块的最后一条止于 `:237`。缺的不是氛围，是**全章最大的关系转折**：辛西娅问海伦娜以前吻别的女人是不是也这样，海伦娜答「对我来说从来没有过」——这与 ch14 `:102`–`:108` 海伦娜「不求长久关系、怕重蹈母亲」的界线正面相撞。 | `:288` `‘Is this what it was like with the other women you kissed?’` ／ `:294` `‘No. It’s never been like this for me. I don’t know what this is, Cyn.’` ／ `:291` `Whatever was happening between them was shattering her foundations and rebuilding her anew.` ／ `:297` `The primal need to mark Helena as hers was shocking in its intensity.` ／ `:300` `‘Cyn, you’re sweeping me away.’` ／ `:303` `‘Should I stop?’` ／ `:306` `‘Never.’` | **阻断** |
| **L2** | **`:174` 辛西娅自述「记不起那个能唤蜂鸟的小女孩」「我的过去像被人偷走了」全无覆盖。** 这是 ch14 结尾「有人封住了她的力量」第一次从本人嘴里落地，也是本章唯一把「重塑自己」从心理话题接到魔法线上的证据。md 只取了海伦娜的回答（`原句 7`＝`:177`），没取被回答的那一句。 | `:174` `Thomas described me as a wild thing, but I can’t remember. I can’t remember that little girl who ran through the fields and could call the hummingbirds from the flowers to hold them in her hand. … It’s as though my past was stolen away from me. But I yearn to find that girl and let her free.` | **阻断** |
| L3 | `:86` 托马斯**误以为**是姨妈动的手。「力量没有主人」这条判断有三个支点（罗温否认／辛西娅未察觉／托马斯误认），md:10 与 md:14 只写了前两个。 | `:86` `Thomas glared at Aunt Rowan before returning his focus to Cynthia. He had felt their aunt’s powers before, and no doubt assumed she orchestrated the magical moment.` | 提示（词表 `orchestrated` 例句正好取自本行，算半覆盖） |
| L4 | `:41` 两周期限与堂兄弟太太来信索要**前客厅尺寸**——与 `:147` 的前客厅构成闭环，也解释 `:150` `And soon, she would be free of it.`。 | `:41` `There is much left to pack if I’m to be out of the house before Hubert’s cousin arrives in a fortnight. His lovely wife has already sent a letter expressing her condolences for my loss and asking for the measurements of the front parlour.` | 提示（词表 `fortnight`/`condolences`/`parlour` 三条例句同出 `:41`） |
| L5 | `:71`/`:74` 冲突的**魔法形态**：海伦娜掌心聚水成露、克里奥抓住托马斯手臂、火花沿晚宴礼服跳动。导航只写「一声"停"让满屋人僵住」，没写她为什么要喊停；且**拦下托马斯的是克里奥不是海伦娜**这一层全无覆盖。 | `:71` `water pooling in her palms and gathering on her skin like dew` ／ `:74` `Clio gripped Thomas’ arm to pull him back as sparks danced along his dinner jacket.` | 提示 |
| L6 | `:56` 罗温把辛西娅正式纳入家族的那一句（每个星期天一起吃饭、缺席即奇耻大辱、最不该做的就是侮辱一个女巫）。md:12 Tropes 只有「女巫家族」四字。 | `:56` `‘You’re family now. We eat together every Sunday, and if you don’t attend, I shall take it as a grave insult. Trust me, the last thing you want to do is insult a witch.’` | 提示 |
| L7 | `:189`–`:198` 狐狸哈姆雷特那一小段：跟着**女主人海伦娜**小跑、蜷成铜色球、`I’m in love with a ferret.`、辛西娅回嘴、yipped 同意。md:12 列了「狐狸哈姆雷特」，正文与词表都无。这是全章唯一的喜剧卸力点，也是**心灵相通**在本章的第二个实例。 | `:189` `Hamlet had been sitting on the couch with Helena, and he padded after his mistress, hopping onto the cushion next to her and curling into a tight, copper ball.` ／ `:192` `Don’t ask me for advice. I’m in love with a ferret.` ／ `:195` `A lot of help you are.` | 提示 |
| L8 | `:249` 焦糖与咸味的**跨章回收**（ch13 `:113` 海伦娜身上就是这个味道），本章是辛西娅第二次尝到并当场认出来。 | `:249` `Damnation! Caramel and salt. I knew it.` | 提示 |
| L9 | `:180` 辛西娅对「别人的恭维」的判断——年轻公子或老勋爵指望她**步丈夫出轨的后尘**、恭维是讨价还价的筹码。这一句同时反证**休伯特不忠**，也正是 `原句 7`「不像报价，也不像交换」的原文依据；md 只写了结论没写依据。 | `:180` `There was always a young buck or an old lord sniffing around in hopes she might be willing to follow in her husband’s example of infidelity. But their compliments, whether obsequious or obscene, never felt real. They were bargaining cards for favours Cynthia had no wish to barter.` | 提示 |
| L10 | `:186` 原文此刻把两人关系命名为 **friendship**（还没定下新长出的友谊的 parameters、没有海图的水域）。md 全篇按恋情写，未标出作者用的这个词。**不裁决**作者是否留白，只要求不要当它不存在。 | `:186` `They hadn’t established the parameters of their newly developing friendship. … These were uncharted waters.` | 提示 |
| L11 | `:153` 一周内的调查落差：`:35` 拉克兰说「明天去追利珀特」，`:153` 是**没找到任何线索**、辛克莱把船管得很紧没有漏洞、七丘没人开口。导航无。 | `:153` `Superintendent MacDougal and her brother had found no leads into the location of George Lippert. Sinclair might be an evil man bent on destruction, but he ran a tight ship with no holes in it. No one in Seven Dials was talking.` | 提示 |
| L12 | `:270` 第二处「无主的力量」：海伦娜呻吟时太阳从云里冲出。原文未说因果，与 `:77` 同类，md 无。 | `:270` `When Helena moaned into her mouth, the sun burst from the clouds in a dazzling display of light.` | 提示 |
| L13 | `:101` 第一场冲突的**实际收束方式**：辛西娅把哥哥拉进一个短促的拥抱、在他耳边低声说了某句话使争论当场结束（内容原文始终未给）。导航写成「答应不鲁莽→除非有女巫」就跳走了，没写托马斯是怎么被按下去的。 | `:101` `She pulled her brother into a quick hug, whispering something into his ear that ended the argument.` | 提示 |

**漏·合计 13 条＝阻断 2（L1、L2）＋提示 11。**

## 二 编（md 有、原文无）

**0 条凭空。** 十五处疑点逐条排除：

| md | 疑点 | 排除依据 |
|---|---|---|
| md:30 | 「危险从来不是女人造成的」原文无此否定句 | 是从 `men have always been a threat` 推出的**升级**，不是凭空 ⇒ 归入「错·提示」E2 |
| md:12 | 「保护者反而被弄得说不出话」 | `:122` `Helena’s mouth went dry as every thought evaporated in the heat of Cynthia’s gaze.` **有据**，只是挂错了因 ⇒ 归入「错·提示」E5 |
| md:12 | 「读心术」列在 trope 里，本章真有吗 | `:83` 罗温心声被海伦娜听到；`:192` 狐狸心声被辛西娅听到、`:195` 当场回嘴 ⇒ **成立** |
| md:64 | 「五个词」 | `She(1) is(2) mine(3) to(4) protect(5)` ⇒ **实测 5** |
| md:104 | 「两个"不是"」 | `:234` `Not Lady Burrows. Not Miss Cynthia Grey.` ⇒ **实测 2** |
| md:104 | 「落在最短的那个名字上」 | `Cyn`(3) < `Lady Burrows`(11) < `Miss Cynthia Grey`(16) ⇒ **成立** |
| md:110 | 「两个名字各削去一截」 | `:237` `Cyn and Hel`；Cynthia→Cyn、Helena→Hel ⇒ **成立** |
| md:100 | 「辛西娅·格雷小姐」是不是新造实体 | `:234` `Not Miss Cynthia Grey.`；且 `Grey` 与 ch02:62/65、ch04:191/269 的 `Lieutenant General Grey`（托马斯）同姓，兄妹同姓一致 ⇒ **不是新造，U7 已结** |
| md:10 / md:159 | 「门外是谁，原文没有交代」会不会是漏断言 | `:309` 只有 `A knock sounded on the parlour door.`，之后即章末 ⇒ **正确的拒答** |
| md:14 | 「那股让众人一僵的力量始终没有主人」会不会过头 | `:77`/`:80`/`:83`/`:86`/`:89` 五处无一给出主人 ⇒ **成立，且是本章最容易越级的地方，md 没有越** |
| md:13 | 「海伦娜从"我要当那个女巫"走到…」引号内不是原文 | `:113` `‘Will you promise that I am the witch who keeps you safe in this investigation?’`——本书 md 一贯用中文引号装**译文式转述**，非逐字引用 ⇒ **体例一致，不判缺陷** |
| md:24 | 「"从今往后"划出一条线」 | `:65` `from this point forward` ⇒ **成立** |
| md:34 | 「用"自古以来"把争论抬到整部历史」 | `:68` `since the beginning of time` ⇒ **成立** |
| md:74 | 「句子里没有谦卑，也没有撒娇」 | `:119` 字面确无谦卑或撒娇标记 ⇒ **否定断言字面成立** |
| md:125 词表 `door` | 例句里 `her sister` 疑为 md 抄错（应作 his） | `:125` 原文就是 `Thomas opened the door for her sister` ⇒ **原文自身瑕疵，逐字照抄正确，不得「修正」** |

## 三 错（两边都有但不一致）

| # | md | 原文 | 定性 | 档 |
|---|---|---|---|---|
| **E1** | md:54 `原句 4`·为什么这样写：「整句只有一个条件，**没有主语**，也没有解释」 | md:48 的引语自身 `:95` `‘Unless I have a witch with me to keep me safe.’` 主语是 **`I`**。缺的是**主句**（整句只有一个从属条件句，没有主句），不是主语 | **形式断言被 md 自身引语当场证伪**（判据 f）。四个机器探针全绿：引语逐字、中文是中文、关键词 `Unless/witch/safe` 成立、形态正常 | **阻断** |
| E2 | md:30 `原句 2`·中文理解：「接着说**危险从来不是女人造成的**」 | `:68` `Life is dangerous. Women have known this since the beginning of time, because men have always been a threat.` 说的是「女人自古就知道危险，因为男人一直是威胁」，**没有一句否定女人造成危险** | 把暗示升级为定论（判据 c）。字面仍可辩，故不判阻断 | 提示 |
| E3 | md:74 `原句 6`·为什么这样写：「后半句用"回报"而不是"报酬"」 | `:119` 只有一个 `repay`。「回报／报酬」之分是 md 自己的中文选词 | 译文层的辨析被写成原文的词义辨析，读者会误以为英文里也有这个区别 | 提示 |
| E4 | md:114 `原句 10`·为什么这样写：「句子短，**尾音却往上走**」 | `:237` `‘Cyn and Hel. What a pair we make.’` 以**句号**收，是感叹不是疑问；英语 `What a …!` 感叹句通常降调 | 韵律断言无原文支撑（判据 f 的弱形态：可由标点核，但不能量化，故不判阻断） | 提示 |
| E5 | md:12 导航 Tropes：「辛西娅先设条件，**再主动索吻，保护者反而被弄得说不出话**」 | 「说不出话」的据在**第一场** `:122`（紧接 `:119` 的条件）；第二场索吻之后海伦娜台词不断：`:258` `‘Is this too much?’`、`:285` `‘Yes. For us. Just for us.’`、`:294` `‘No. It’s never been like this for me.’`、`:300` `‘Cyn, you’re sweeping me away.’` | 事实存在，但**语序把结果挂到了错误的因上** | 提示 |
| E6 | md:54 `原句 4`·为什么这样写：「**句子越短，留白越大**」 | 无基线。若与紧邻上文比：`:92` `I promise that I won’t do anything rash.` ＝ **8 词**，`:95` 的「除非」句 ＝ **11 词**，反而更长 | 「越…越…」无比较对象（判据 f）。作格言读可通，作比较读不成立 | 提示 |
| E7 | md:66 `原句 5`·读者视角提示：「接下来的条件**正对着这份私心而来**」 | 同一份 md 的 md:76 说这句条件「**让她的私心无处落脚**」。前者读成「针对／迎向」，后者是「化解」，两处对同一条件的定性方向不同 | 同文件内自相矛盾（判据 d 的弱形态：不构成与原文相反，故不判阻断） | 提示 |
| E8 | md:80 `原句 7`·中文理解：「三个判断**一个比一个近身**」 | `:177` `a wonder. And a mystery. And very, very beautiful.` 三项由 `And … And …` **并列**连接，原文未标远近；md 自己在 md:84 写的是「前两个词还停在远处…第三个词忽然落到脸上」＝**二远一近**，不是三级递进 | 递进断言与原文的并列结构不符，且与同块下一子项不同构 | 提示 |

**错·合计 8 条＝阻断 1（E1）＋提示 7。**

**时序专查（无缺陷）**：md:10 与 md:159 的事件顺序实测与原文一致——`:62` 拥抱 → `:65` 请交调查 → `:68` 反问 → `:71`/`:74` 魔法对峙 → `:77` 「停」 → `:80`/`:83` 罗温否认 → `:92` 承诺 → `:95` 除非 → `:113` 海伦娜请缨 → `:119` 条件 → `:153` 一周后 → `:159` 提问 → `:177` 赞美 → `:216` 索吻 → `:234` 弃称呼 → `:237` 答 → `:309` 敲门。**无一处写反。**

## 四 R4 逐块对应（十块，含固定三问）

| 块 | 引语出处 | 中文是在讲这句引语吗 | ① 动词主语 | ② 受事/宾语 | ③ 归属方向（`by`/`to`/`from`/`of`） |
|---|---|---|---|---|---|
| `原句 1` | `:65` | ✅ 全在讲托马斯这句请求 | md 写「托马斯把请求说得客气」＝托马斯 ✅ | 「把决定权从**她**手里拿走」＝辛西娅 ✅ | `let **us** handle`→ md:26 专门点出「他用的是"我们"，不是"我"」✅ |
| `原句 2` | `:68` | ✅ | md 写「**海伦娜**先抓住那个"我们"」✅ | 「问它是不是只指**男人**」✅ | `men have always been a threat`→「男人一直是威胁」方向 ✅；但补出「危险从来不是女人造成的」＝**升级**（E2） |
| `原句 3` | `:77` | ✅ 且**明确拒绝越级**（md:44「原文不说是谁放的」、md:46「没有交代力量从哪来」） | md 写「**辛西娅**站到哥哥和海伦娜中间」＝`Stepping between … Cynthia` ✅ | 「伸出双手」＝`held her hands out` ✅；「屋里的人一时间全僵住」＝`they all froze` ✅ | 主动方＝辛西娅、被拦的双方＝`her brother` 与 Helena ✅ |
| `原句 4` | `:95` | ✅ | md 写「**她**刚答应不做鲁莽的事」＝辛西娅（`:92`）✅ | 「除非身边有位女巫护着**她**」✅ | 承诺者与被保护者同为辛西娅 ✅；但「没有主语」＝**形式断言错**（E1） |
| `原句 5` | `:116` | ✅ | md 写「这是**海伦娜**的心里话」——`:116` 无引号独立成段，夹在 `:113` 海伦娜私语与 `:119` 辛西娅回答之间 ✅ | 「**辛西娅**归她保护」＝`She is mine` 的 she ✅ | `mine to protect`→「归**我**保护」方向 ✅；「不是"我们"，也不是家族」与 `:65`/`:56` 构成对照 ✅ |
| `原句 6` | `:119` | ✅ | md 写「**辛西娅**只提一个条件」✅ | 「让**她**回报**海伦娜**的出力」＝`let **me** repay **you**`，说话人辛西娅 ⇒ me＝辛西娅、you＝海伦娜 ✅ **方向未调转** | `repay … for your efforts`→「回报你的出力」✅；但「回报／报酬」是译文层（E3） |
| `原句 7` | `:177` | ✅ | md 写「**海伦娜**给出的是一串短句」✅ | 「你是奇迹，是谜，非常美」的「你」＝辛西娅 ✅ | 赞美者海伦娜→受者辛西娅 ✅；「一个比一个近身」与原文并列不符（E8） |
| `原句 8` | `:216` | ✅ 两句同段，第二句是叙述 | md 写「**辛西娅**把请求说得很正式」✅；「**叙述**紧接着承认」——第二场贴辛西娅，`It was glorious to take the lead` 是她的视角 ✅ | 「如果**对方**肯给她这样的自由」＝`If you would allow me`，you＝海伦娜 ✅ | 请求者辛西娅→许可者海伦娜 ✅ **未调转** |
| `原句 9` | `:234` | ✅ 四句同段 | md 写「**辛西娅**往后一缩」＝`Cynthia recoiled` ✅；「**她**要褪掉…名字」✅ | 「问**对方**能不能这样叫她」＝`Will you call me that?`，you＝海伦娜 ✅ | `recoiled **from** the title`→「听到那个称呼…往后一缩」，而那个称呼来自 `:231` 海伦娜说的 `Lady Burrows` ⇒ **因果与来源都对** ✅ |
| `原句 10` | `:237` | ✅ | md 写「**海伦娜**把这声"辛"接住」✅ | 「又把自己也叫成"海儿"」✅ | 应答者海伦娜→发问者辛西娅（`:234` 末句）✅；「尾音往上走」无据（E4） |

**对应层：10/10 块的中文都在讲自己那句引语，无一块漂到引语之外的上下文，无一块只复述字面（十块的「为什么这样写」都给了写法层面的理由）。**
**施事/归属三问：十块全部通过，无一处调转。** 唯一的归属问题是 E5（导航层把「说不出话」挂到索吻之后），不在块内。
**⚠️ 但对应的反面是覆盖：`:240`–`:306` 这 67 行（占全章 22%）没有任何块与之对应——见 L1。**

## 五 形态

| 项 | 实测 | 判 |
|---|---|---|
| H1 | `# 15. Chapter Fifteen`（md:6），与 `2-machine.json` 的 `h1` 一致 | ✅ |
| 导航项数 | 5（md:10 一句话概括 / md:11 情感弧线位置 / md:12 Tropes / md:13 人物弧线 / md:14 叙事手法）＝`nav_count 5` | ✅ |
| 子项集 | 每块 4 项（中文理解／关键词／为什么这样写／读者视角提示）×10 块＝40，无缺无多 | ✅ |
| 块数 | **10** vs `block_target [5,9]` ⇒ `block_hint`：**块数 10 偏离本章篇幅建议 5–9（本章 2923 词）** | **提示**（rc 仍 0）⇒ **不得再增块** |
| `## 本章词汇` 位置 | md:118，在 `## 精读`（md:16）之后、`## 一句话总结`（md:157）之前 | ✅ |
| 词表表体格式 | 三档均为标准 Markdown 表格：`| 词/短语 | 释义 | 例句 |` + `|------|------|------|`（md:122/123、135/136、148/149）⇒ 符合 2026-10-23 新增判据「表体必须是标准表格，斜杠分隔会整档判空」 | ✅ |
| 词条数 | 22（⭐⭐⭐ 8 ＋ ⭐⭐ 8 ＋ ⭐ 6） | ✅ |
| `## 一句话总结` | md:157 有标题、md:159 有正文（非空） | ✅ |
| 引号配对 | `/tmp/pair4_hx.py` 全书扫描 ⇒ `TOTAL 1`，唯一一条在 ch09 `原句 7`（孤儿闭引号），**ch15 零偏离**；`原句 2` 的 `‘By “us”, do you mean the men?’` 内外两层引号嵌套正确 | ✅ |

**形态：8 项核，相符 7、提示 1（块数超上限）。**

## 六 语料层

**推广行（零命中，附取证）**
```
$ /usr/bin/grep -nE 'Lokepub|Also by|Continue the adventure|Next in the series|Discover more|Available now' \
      text/ch15_chapter_15.txt
（无输出）
rc=1
```
⇒ **ch15 零推广行**。（全书分布为 5 章 8 行：ch03 `:188`／ch08 `:170`+`:173`／ch13 `:182`+`:185`／ch19 `:194`+`:197`／ch25 `:214`。）

**⚠️ 反面陷阱（与 ch13 `:287` 同类）**：`:192` `Don’t ask me for advice. I’m in love with a ferret.` 孤立读极像出版方插页，**实为狐狸哈姆雷特的心声**——归属由 `:189`（它跟着女主人小跳上软垫）、`:195`（辛西娅回嘴 `A lot of help you are.`）、`:198`（`He yipped an agreement.`）三点钉住。任何「删推广行」的批量脚本都必须先过这三点。

**原文瑕疵扫描（八项全 0）**
```
U+FFFD 0 ／ 零宽字符(200b/200c/200d/2060/feff) 0 ／ 叠词 0 ／ 双逗号 0
双空格+小写 0 ／ 直撇号 0 ／ 直双引号 0 ／ 双句点 0
```
⇒ **ch15 语料干净**，与 ch14 同。`:183`／`:210`／`:261` 的省略号是原文的迟疑停顿（`‘No, I just don’t… That is, I’m not sure…’`），**不是拼接痕迹**；`:47` 的省略号收尾（`What wicked mischief they could make.` 之前的 `tiptoeing up to her room without the staff even knowing…`）同理，且 `they` 是**复数**。

**逐字与行号回验（本轮实跑输出）**
```
blocks found: 10
原句1: verbatim=True lines=[65]  len=117     原句6:  verbatim=True lines=[119] len=48
原句2: verbatim=True lines=[68]  len=260     原句7:  verbatim=True lines=[177] len=68
原句3: verbatim=True lines=[77]  len=135     原句8:  verbatim=True lines=[216] len=176
原句4: verbatim=True lines=[95]  len=48      原句9:  verbatim=True lines=[234] len=214
原句5: verbatim=True lines=[116] len=23      原句10: verbatim=True lines=[237] len=35
vocab bad: 0     （22 条例句全部为 ch15 text 精确子串）
  obsequious :180   post-haste :41    orchestrated :86   exhilarating :150
  evaporated :122   recounting :153   unfiltered  :246   simpered    :147
  fortnight  :41    condolences :41   conjured    :153   converge    :168
  vibration  :171   boundaries  :210  wallflower  :183   flurry      :153
  napkin     :35    door        :125  parlour     :41    settee      :153
  sconce     :150   coat        :110
```
另有 `/tmp/vocab_head_hx.py 15` ⇒ **rc=0 无输出**（22 个词头全部出现在自己的例句里）。

**跨章术语（本章涉及的部分）**
- **罗温**：ch15 md:10／md:14 用「**罗温姑妈**」，与 ch04·06·07·14·16 同派；ch24·25·26 作「罗温姨妈」。原文只写 `Aunt Rowan`，父系母系未给 ⇒ **不裁决哪个对，只统一，建议取多数派（姑妈）**。
- **Burrows**：ch15 md:12／md:100／md:159 用「**伯罗斯**」，另有章作「布尔洛斯」⇒ 同上，建议取多数派。
- **honeysuckle**：原文出现于 ch06:95／ch07:50／ch12:273／**ch15:68**／ch18:380／ch25:123；md 译名分裂为「忍冬」（ch06 ×2）与「金银花」（ch07 ×2、ch25 ×3）。**ch15 md 未翻译该词**——`原句 2` 的引语从 `‘By “us”, do you mean the men?’` 起，`:68` 前半句 `catching the hint of vanilla and honeysuckle` 不在引语内，中文理解也未提 ⇒ **本章不构成冲突**，但汇总时仍须统一另三章。
- **Cyn / Hel**：ch15 md 作「辛」「海儿」，需与后续章（ch16 起）核一致。
- **decimate**：ch13「毁灭，严惩」vs ch11「大量毁掉，严重削弱」——与 ch15 无关，留汇总。

## 七 不裁决（U1–U9）

| # | 问题 | 处置 |
|---|---|---|
| U1 | `:101` 辛西娅在托马斯耳边说了什么 | 原文始终未给。md 未猜 ⇒ **处置正确**；覆盖建议见 L13 |
| U2 | `:264` `It was nothing like her past experiences.` 的 `her` 指谁 | 第二场贴辛西娅 ⇒ 最自然是辛西娅；但海伦娜 `:294` 说「对我来说从来没有过这样」⇒ **两读并存，不裁决**。md 未涉及此句 |
| U3 | `:270` 太阳冲出云层是否与辛西娅相关 | 原文未说因果 ⇒ **不裁决**；不得写成辛西娅施法（T20） |
| U4 | 章末敲门者是谁 | 原文未给 ⇒ **不裁决**；md:10 与 md:159 两处都明写「原文没有交代／没有说」⇒ **处置正确** |
| U5 | `:77` 的能量波是谁放的 | 四处证据（罗温否认／托马斯误认姨妈／三表姐妹望向姨妈／辛西娅毫无察觉）都指向「没人知道」；最自然推读是辛西娅，但**不得写成断言**。md:14／md:44／md:46 三处均拒绝归属 ⇒ **处置正确** |
| U6 | 堂兄弟夫妇无名、townhouse 无址 | 原文未给 ⇒ **不裁决** |
| U7 | `Grey` 是不是新造实体 | **已结**：`Lieutenant General Grey`＝托马斯（ch02:62/65、ch04:191/269），`Miss Cynthia Grey`（`:234`）＝其妹，兄妹同姓一致 ⇒ **不是新造，不是矛盾** |
| U8 | 利珀特下落 | `:35`「明天去追」与 `:153`「没找到任何线索」的落差，本章未交代结果 ⇒ **不裁决**；覆盖建议见 L11 |
| U9 | `:186` 原文把两人关系命名为 `friendship`，而全章描写远超友谊 | 是作者留白还是人物自欺 ⇒ **不裁决**；只要求 md 别当这个词不存在（L10） |
