# ch14 深审 R3 三张单子（漏 / 编 / 错）

- 章文件：`notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/ch14 the witches at dinner.md`
- 语料：`notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/text/ch14_chapter_14.txt`（367 行，正文 `:35`–`:366`）
- 素读底稿：`review/ch14/1-suread.json`（104 events / 10 rel / 10 num / 7 unresolved / 23 traps；BAD 0）
- 机器层：`review/ch14/2-machine.json`（rc=0，verdict ok，blocks 9，segments 9，segment_miss 0）

## 〇 结构要点（判读前提）

1. **POV 与 ch13 相反**：本章全程贴**海伦娜·布莱尔**第三人称限知（`:35`–`:366`）；ch13 贴辛西娅。凡「读者／她」的指称都要先定谁。
2. **心声段四处，归属必须分清**：
   - `:213`–`:216` 罗温姨妈的心声（`Aunt Rowan’s thoughts echoed in Helena’s head.` 明写归属）
   - `:222` **克里奥**的心声（`Cynthia is a witch.`，紧跟她出声的 `Oh, my goddess.`）
   - `:363`+`:366` **罗温**的心声（`Aunt Rowan sent Helena a look laden with meaning.` → `She is a witch. Someone trapped her powers…`）
   - 海伦娜自己的：`:69`、`:144`、`:198`、`:273`
3. **两处无归属心声，不得替它定主**：`:225` `This changed everything.`／`:351` `Seven. The age a witch first comes into her powers.`
4. **三种动物伙伴不可混**：哈姆雷特＝海伦娜的狐狸（`:50` 与雪貂对跑）／奥菲莉亚＝**埃莉的雪貂**（`:50` `her ferret`，`:204` 才给名）／罗宾爵士＝**克里奥的鸟，会说话**（`:171`、`:183`、`:207`、`:288`）。
5. **三表姐妹能力不可互换**（`:159`）：克里奥 delve into their pasts／海伦娜 read their thoughts／埃莉 see any possible future。
6. **场景切分**：`:35`–`:50` 早晨卧室 → `:51`–`:65` 空行分隔 → `:66`–`:135` 傍晚镜前独处 → `:138`–`:366` 晚宴。
7. **`原句 5` 与 `原句 6` 出自同一自然段 `:204`**（辛西娅的爆发被天气切成四截，md 拆成两块引用，合法）。

## 一 漏（原文有、md 无）

| 编号 | 原文（行号＋逐字） | 性质 | 判定 |
|---|---|---|---|
| **L1** | `:108` `She closed her eyes, refusing to acknowledge the sacrifice her mother was willing to make for blood magic, or the price she forced Helena to pay.` | **全书首次出现 `blood magic`**（另见 ch20 `:132`、ch21 `:284`），且同句给出「母亲逼海伦娜付的代价」——md 全篇 0 处；`原句 3` 的引语止于 `:105`，未含此句 | **阻断** |
| L2 | `:75`–`:90` 海伦娜两次问哈姆雷特「辛西娅能不能听见你的心思」（`Can you hear animals’ thoughts?`／`Can she hear your thoughts, Hamlet?`／`Is that a yes? Or are you telling me I’m crazy?`），**狐狸始终没有回答** | 承接 ch13 `:320`–`:326` 的悬念；md 未提 | 提示（覆盖建议） |
| L3 | `:159` 罗温早年施法，封住三表姐妹读「罗温↔拉克兰彼此的心思」；`Clio couldn’t delve into their pasts. Helena couldn’t read their thoughts about each other. Ellie couldn’t see any possible future for them.` | 三能力分工＋本章唯一的读心失效范围；md 未提，且与 `原句 8` 的「身边每个人」冲突（见 E11） | 提示（覆盖建议） |
| L4 | `:291`+`:294` 托马斯说 `Cynthia isn’t like you. She doesn’t have the powers you and your family have.`（**假话，他不知道妹妹是女巫**），罗温与埃莉交换一个心照不宣的眼神 | 本章主要的戏剧反讽；md 未提 | 提示（覆盖建议） |
| L5 | `:285`–`:303` 克里奥指尖冒火花 → 煤气灯猛亮（`a sure sign of Clio’s temper`）→ 掌心成一团火 → 托马斯把她的手按在自己心口把火掐灭 → 克里奥反过来抚他的脸，`a disconcertingly intimate moment` | 另一条「以魔法回护」的对照线；`disconcertingly` 只进了词表，事件未进正文 | 提示（覆盖建议） |
| L6 | `:339` 托马斯回忆辛西娅童年野事：`Always begging me to go on adventures with you in the forest, rolling down the hills until your dress was ruined, sneaking to the stables to whisper secrets to the horses and feed them stolen apples from the kitchen.` 与 `You were a wild thing once.` | 「被驯成淑女」这条线的正面证据；md 只写「问出她七岁那年的事」，未及内容 | 提示（覆盖建议） |
| L7 | `:345` `‘But you would have been happy,’ Helena murmured.`——**原文下一句无任何回应** | 海伦娜唯一一次替辛西娅说出「快乐」；md 未提 | 提示（覆盖建议，且不得补写回应，见 U7） |
| L8 | `:249`+`:255` 拉克兰 `I don’t know him.`、托马斯 `Never.`——**两个男人都没听过乔治·利珀特** | md 一句话概括只写「说出名字」，未写「谁都不认识」 | 提示（轻） |
| L9 | `:141`+`:144`+`:147` 罗温那句 `Helena never invites… friends… to dinner.`、海伦娜想用一道咒让她当场失声、心里骂 `Meddling witch!` | 开场第二拍的姑侄过招；`withering` 只进了词表 | 提示（轻） |
| L10 | `:237` `There would be time to speak with her coven about Cynthia later.` | 全书首次点出「coven」这个组织词；md 未提 | 提示（轻） |
| L11 | `:99` `She had explored pleasure with a few women, but she never let it go beyond fulfilling a physical desire. Like scratching an itch or indulging in a slice of cake.` | 「绝不承诺」那条界线的来历；`原句 3` 只讲了母亲那一半 | 提示（轻） |
| L12 | `:276` 海伦娜慌忙用 `she is Clio’s sister-in-law now` 把「我们自己人」圆回去 | md 人物弧线只写「当众算进我们自己人」，未写她随即退半步 | 提示（轻） |

> L2–L12 均**不构成阻断**：本章的关键转折（雷雨暴露魔法／罗温断定力量被封／利珀特这个名字上桌／海伦娜认出同类）md 都已覆盖，缺的是次级事件与铺垫。L1 是唯一判阻断的漏项，理由是「全书首次出现的设定词＋一条关于海伦娜本人的事实」。

## 二 编（md 有、原文无）

**0 条。** 以下 11 处曾疑似凭空，逐条回源后确认有据，列此备查：

| 疑点 | 取证 | 结论 |
|---|---|---|
| `原句 2` 中文理解的「**红发**」不在引语内 | `:47` `grappled with the wild red curls obstructing her view` | 有据（同章），仅属引语外属性 ⇒ 降级为提示 E6 |
| 一句话总结「**布莱尔家**的女巫们」 | ch06 `:122` `providing the Blair women with a lavish lifestyle`（该段主语即罗温与克里奥合制的产品） | 有据，罗温计入 Blair women |
| 情感弧线位置「赌场会面之后的**第二天**」 | `:162` `her adventure with Cynthia at The Devil’s Bargain the previous evening`；ch13 `:299` `Are you free tomorrow for dinner?` | 有据 |
| 「可以调情、可以试探、绝不承诺」 | `:123` `Flirtations? Fine.`／`:126` `Explorations? Marvellous.`／`:129` `Commitment? Never.` | 有据（三短句是内心决定，不是台词） |
| `原句 9` 读者视角提示「看出来的**不止一个人**」 | `:213`–`:216` 罗温、`:219` 埃莉 `Holy Hecate.`、`:222` 克里奥、`:231` 海伦娜 | 有据 |
| `原句 6` 为什么这样写「**没有一个人说**『她在施法』」 | 全章无人出声断言；罗温 `:213`、克里奥 `:222` 都是心声 | 有据（「说」字用得准） |
| 人物弧线「晚上却**两次**越过去」 | `:267`+`:273`（our own → `Did I just call her my own?`）／`:309` `‘Bravo.’ The word escaped before Helena could stop it` | 有据 |
| `原句 9` 归**罗温**的心声（不是海伦娜自己的结论） | `:363` `Aunt Rowan sent Helena a look laden with meaning.` 紧接 `:366`；追问链 `:318` `When?`／`:327` `When exactly do your memories become clear?`／`:348` `And you were seven…? You’re sure?` 全是罗温在问；同口径的心声她 `:213` 已有过一次；`:159` 的封禁只覆盖「罗温↔拉克兰彼此的心思」，不含她对辛西娅的判断 | 归属正确，md 两处导航都写对了 |
| 词表 22 条例句 | `python3 /tmp/vocab_check_hx.py 14` ⇒ `rows=22 missing=0`；`/tmp/vocab_head_hx.py 14` ⇒ 无输出 rc=0 | 例句逐字、词头齐全 |
| 一句话概括「每说一句雷声、闪电与雨点就**重一分**」 | `:204` `Thunder rumbled` → `Lightning cracked` → `Rain pelted` → `Another boom of thunder` | 有据（四级递进） |
| `原句 4` 中文理解「他和**拉克兰叔叔**想的一样」 | `:192` `Thomas was of one mind with Uncle Lachlan on this point.` | 有据；称谓口径见 §六 |

## 三 错（主语／因果／数字／时序／方向）

| 编号 | 位置 | md 原文 | 原文取证 | 判定 |
|---|---|---|---|---|
| **E1** | 导航·人物弧线 | 「辛西娅从被追问的人变成**拍桌**的人」 | 拍桌的是**托马斯**：`:168` `Thomas slammed his hand down so hard, the cutlery jumped.`（`/usr/bin/grep -rn "slammed his hand" text/` ⇒ 全书仅此一处）；辛西娅的动作是 `:204` `Cynthia rose from her chair and leaned over the table.` | **阻断**（施事归属错） |
| **E2** | `原句 5`·为什么这样写 | 「**句子越往后越短**，最后落在『任何人』上」 | 实测五句词数 **15 / 10 / 4 / 4 / 7**（脚本见下），末句比前两句**长** ⇒ 被 md 自身引语当场证伪 | **阻断**（形式断言被自身引语证伪；判据同 ch12 E1） |
| **E3** | `原句 7`·中文理解 | 「那个**向自己示好**、让自己动心的女人」 | `:231` `the woman claiming her attentions and stirring her desires`——`claiming her attentions` ＝辛西娅**占据海伦娜的心思**（心思由海伦娜流向辛西娅），不是辛西娅向海伦娜示好 | **阻断**（R4 三问之「归属方向」反转） |
| **L1** | 见 §一 | 血魔法与「母亲逼海伦娜付的代价」整条缺失 | `:108` | **阻断**（漏·关键设定首次出现） |
| E5 | `原句 1`·中文理解 | 「**最可爱的一处**是她完全不知道自己有多美」 | `:35` `There were many endearing things about Ellie, but her complete lack of awareness…`——只把这一处单独挑出，未做「最」的排序 | 提示（最高级升级） |
| E6 | `原句 2`·中文理解 | 「与**红发**形成对比的深蓝」 | 引语只写 `contrasted with her hair`；红发在 `:47` 有据但不在引语内 | 提示（轻；判据区分见 §五） |
| E7 | `原句 2`·为什么这样写 | 同段先写「第二条给了一个理由——与发色相衬」，后写「三次都只有衣料和颜色，**没有一句解释**」 | 引语内 `the dark-blue one that contrasted with her hair` 正是那一个理由 ⇒ 同段自相矛盾 | 提示 |
| E8 | `原句 6`·中文理解 | 「把**奥菲莉娅**吓得钻进埃莉怀里」 | `:50` `her ferret`（埃莉的雪貂）、`:204` `Ophelia burrowing into Ellie’s arms` ⇒ md 未交代它是雪貂，易被读成在场的人 | 提示（漏·身份） |
| E9 | `原句 6`·读者视角提示 | 「她还在生气，天气却已经按她的句子行事，**这份不知情**让场面更惊人」 | 原文对辛西娅是否知情**无一处着墨**：`:204` 天气随怒而起、`:228` `Cynthia took a deep breath and the rain eased to a soft patter.` 均未写她的自觉 | 提示（无原文逐字 ⇒ 不得判阻断） |
| E10 | `原句 7`·读者视角提示 | 「她知道了，**辛西娅还不知道**」 | 原文只支持「没说破」：`:315` `My memories of our younger years have always been fuzzy.`／`:360` `If Thomas says I was seven, then I must have been seven.`；是否自知属悬置（U1／U7）。且与同 md `原句 9`「辛西娅本人还没有把这件事说破」口径不一 | 提示 |
| E11 | `原句 8`·读者视角提示 | 「也就意味着她随时可能读到**身边每个人**的心事」 | 本章即有反证：`:156` `his thoughts, usually clear and easy for Helena to read, would become muddled and fuzzy.`／`:159` `Helena couldn’t read their thoughts about each other.`；辛西娅更是全书读不到（ch13 `:83`） | 提示（推测语气＋「可能」兜底，故不判阻断，但同章有反证） |
| E12 | 导航·情感弧线位置 | 「开场是海伦娜**一个人**的早晨：被埃莉看穿、在镜前挑衣服」 | 埃莉在场：`:35`–`:50`（`Ellie had flounced into her room`、`:50` 她的雪貂跑上床）；真正独处的只有 `:66`–`:129` 镜前那段（在场者仅狐狸哈姆雷特） | 提示 |
| E13 | 词表 ⭐⭐ `flounced` | 释义「（**带荷叶边地**）轻快闯进」 | 荷叶边属原文 `ruffles`（`:35` `Her cotton nightgown, covered in ruffles`），是睡裙上的褶边，不属动词 `flounce`；`flounce` 义为莽撞／大摇大摆地闯进 | 提示（释义错） |
| E14 | `原句 9`·中文理解 | 「结尾**这句心声**给出结论」 | 心声主人是罗温（`:363` 递眼色 → `:366`）；md 的导航两处都写明了归属，唯独引语块内没写 | 提示（轻，补归属即可） |

E2 取证脚本与输出：

```
$ python3 -c "q='I am sick to death … anyone.'; [print(len(s.split()),s) for s in …]"
15 | I am sick to death of men telling me what I can and cannot do
10 | I have spent my entire life following other people’s orders
 4 | My husband is dead
 4 | I am finally free
 7 | I won’t be dictated to by anyone
（退出码 0）
```

## 四 R4 逐块对应表（人判；固定三问：动词的主语／受事／归属方向）

| 块 | 引语出处 | 主语 → 受事 | 归属方向核对 | 对应判定 |
|---|---|---|---|---|
| 原句 1 | `:35`（段末三句） | Helena（smile）→ Ellie 的 lack of awareness；「too bloody early」的评判者＝海伦娜 | 方向无误 | 对应 ✓（分析层 E5） |
| 原句 2 | `:66` | Helena（changed / settled）→ 三条裙子；`contrasted with her hair` 的主语＝深蓝裙 | 方向无误 | 对应 ✓（分析层 E6／E7） |
| 原句 3 | `:105` | Helena（didn’t want）→ permanent bonds；mother（sacrificed）→ all that was light and good；受益者＝a man（**未具名**，U3）；`twisted` 的主语＝那个男人 → 受事＝her magic | 方向无误；男人不得补名 | 对应 ✓（漏 L1 阻断） |
| 原句 4 | `:192` | Thomas（说）→ Cyn；`of one mind with` 的对象＝Uncle Lachlan；`allow` 的主语＝托马斯 → 受事＝辛西娅的行动 | 方向无误 | 对应 ✓ |
| 原句 5 | `:204`（同段前半） | Cynthia（说）→ men（泛指）；`dictated to by anyone` 的施动者＝任何人 → 受事＝辛西娅 | 方向无误 | 对应 ✓（形式断言 E2 阻断） |
| 原句 6 | `:204`（同段后半） | Thunder / Lightning / Rain / Another boom（各自主语）→ the house·windows / the sky / the roof；`burrowing` 的主语＝Ophelia → 去向＝Ellie’s arms | Ophelia＝雪貂，md 未标（E8） | 对应 ✓（E8／E9） |
| 原句 7 | `:231` | Helena（processed）→ the shocking news；`claiming her attentions` 的主语＝the woman（辛西娅）→ 受事＝**her＝海伦娜的**注意力 | **md 反了**（E3） | **对应失配 1 处** |
| 原句 8 | `:261` | Helena（说）→ 在座众人；`he thought` 的 he＝辛克莱；the name＝George Lippert（`:246`）；`asked` 的主语＝Cynthia → 对象＝辛克莱 | 方向无误 | 对应 ✓（分析层 E11） |
| 原句 9 | `:366` | 心声主人＝罗温（`:363` 递眼色）；`She`＝辛西娅；`Someone trapped her powers` 的 someone＝**未具名**（U1） | 方向无误；不得替 someone 补名 | 对应 ✓（块内未标归属，E14） |

**对应小结：9 块中 8 块对应完好，1 块（原句 7）方向失配 ⇒ 对应 8/9。**
`segment_miss = 0` 只证逐字，不证对应——本章失配正是「逐字全对、方向错」这一类。

## 五 形态

| 项 | 实测 | 判定 |
|---|---|---|
| H1 | `14. Chapter Fourteen`，`h1_shape_ok: true` | ✓ |
| 导航子项 | 5 项（一句话概括／情感弧线位置／Tropes 兑现反转／人物弧线／叙事手法），`nav_count_ok: true` | ✓ |
| 精读子项 | 4 项（中文理解／关键词／为什么这样写／读者视角提示）×9 块，与 `profile_subitems` 一致 | ✓ |
| 块数 | **9**；`block_range` [6,13]、`block_target` [6,9] ⇒ **已触上限** | ✓ 但**不得再加第 10 块**；L1 的修法只能走「改导航」或「延引语」，不能新增块 |
| 字数 | `words: 3038` | ✓ |
| 引号配对 | `/tmp/pair4_hx.py` 全书扫描 ⇒ `TOTAL 1`，唯一一条仍在 ch09 `原句 7`（孤儿闭引号，已登记），**ch14 零偏离** | ✓ |
| 引语跨段 | `原句 5`／`原句 6` 同出 `:204` 一个自然段（辛西娅的爆发被天气切成四截） | 合法，非缺陷；但两块的分析不得互相搬用「同段」以外的证据 |
| 词表分隔行 | `|------|------|------|`（三章同形） | 合法 GFM，不判缺陷 |

**判据分级补充（本章新增，接 ch11–ch13 的 (a)–(e)）**

- **(f) 形式／节奏断言可被 md 自身引语量化证伪 ⇒ 阻断**（E2：「句子越往后越短」对 15/10/4/4/7）。凡「越…越…」「每…都…」「没有一处」这类可数的形式断言，落笔前先数一遍。
- **(g) 引语内名词的「属性」被补写，且同章可核 ⇒ 提示；引语外「新增情境事实」⇒ 阻断（轻）**（E6「红发」属前者，ch13 E2「那个雨天」属后者）。
- **(h) 施事归属错（谁拍了桌、谁站起来了）⇒ 阻断**（E1）。本章同一自然段里两个动作分属两人，最易错。
- **(i) 同章有反证的「全称断言」（每个人／从来／随时）⇒ 至少提示**（E11）。

## 六 语料层与跨章口径

**推广行**：ch14 **零命中**。取证：

```
$ /usr/bin/grep -n "Lokepub\|A new book can wait\|Add one to your list" text/ch14_chapter_14.txt
（无输出）rc=1
```

全书推广行仍为 **5 章 8 行**：ch03 `:188`／ch08 `:170`+`:173`／ch13 `:182`+`:185`／ch19 `:194`+`:197`／ch25 `:214`。**ch13 `:287` 不是推广行**（是狐狸哈姆雷特的心声，全书仅此一处），已在 ch13 的 3-diff 立档，本章无同类陷阱。

**ch14 原文瑕疵扫描：干净。** 零宽字符／U+FFFD／叠词／两点／双逗号／双空格＋小写／直撇号／直双引号 全部 0 命中（`/usr/bin/grep -c "'" text/ch14_chapter_14.txt` ⇒ `0`，rc=1）。唯一易误判处是 `:141` `Helena never invites… friends… to dinner.`——两个省略号是**罗温故意的停顿**，属原文笔法，不得「修正」，也不得当成提取事故。

**跨章术语不一致（本章涉及）**

| 项 | 两种写法 | 分布 | 处置 |
|---|---|---|---|
| Aunt Rowan | 罗温**姑妈** / 罗温**姨妈** | 姑妈：ch04(1)·ch06(3)·ch07(1)·**ch14(4)**·ch15(3)·ch16(5)；姨妈：ch24(3)·ch25(2)·ch26(5) | 原文只作 `Aunt Rowan`，血缘侧未写 ⇒ **不裁决哪个对，只统一**。ch14 用「姑妈」属多数派，本章不改 |
| Uncle Lachlan | 拉克兰**叔叔** / 拉克兰**舅舅** | 叔叔 12 处：ch02(2)·ch04(2)·ch06(3)·ch09(2)·**ch14(1)**·ch17(1)；舅舅 9 处：ch23(3)·ch24(2)·ch25(1)·ch26(3) | 原文只作 `Uncle Lachlan`（ch11 `:44` 另给全名 Superintendent Lachlan MacDougal），未写父系或母系 ⇒ **不裁决，只统一**；建议取多数派「叔叔」 |
| apothecary | 药妆店 / 药草店·药剂师 | ch06 `:122` 明示 `Her apothecary was now the city’s premier beauty shop`，店名 `All Things Bright and Beautiful`（ch14 `:138` 亦出现） | 已有条目，本章不涉及 |

**本章 md 未出现上述任一种混用**：`罗温姑妈` 4 处、`拉克兰叔叔` 1 处，各自内部一致。

## 七 不裁决（原文悬置，md 亦未断言，不得补写）

| 编号 | 悬置点 | 原文 |
|---|---|---|
| U1 | 谁封住了辛西娅的力量 | `:366` `Someone trapped her powers`——只作 someone |
| U2 | 罗温与拉克兰之间的「古怪敌意」是什么 | `:159` 罗温施法封住，三表姐妹「spinning out possible stories」而未得 |
| U3 | 母亲献身的那个男人是谁；血魔法的牺牲内容；海伦娜付的是什么代价 | `:105` 只作 `a man`；`:108` 只作 `the price she forced Helena to pay` |
| U4 | 乔治·利珀特是谁 | `:246` 只有名字；`:249`/`:255` 两个男人都没听过 |
| U5 | 辛西娅能不能听见动物的心思 | `:75`–`:90` 海伦娜两次问狐狸，**狐狸始终未答** |
| U6 | 克里奥「不久前」护住托马斯免于何种危险 | `:297` `I kept you protected against certain danger not so long ago` |
| U7 | `:345` `‘But you would have been happy,’ Helena murmured.` 之后无人应答 | 原文下一行即转罗温的追问，**不得替辛西娅补写反应** |
