# ch17 · R5 判定表（`ch17 the dog in cheapside.md`）

- 审查日：2026-10-23 ｜ 档位：**深审**（R1 素读底稿为深档：143 events／24 rel／13 num／12 unresolved／30 traps，`checked=196 BAD=0`，投毒两步通过）
- 铁律执行：**先**读 `text/ch17_chapter_17.txt` 全文并落 `1-suread.json`，**后**开 md。未违反。
- 取证口径：全部用 `/usr/bin/grep` 显式路径（**不用 `git grep`**，`text/` 被 `.gitignore` 排除）；每条阻断均附 `text/<文件>:<行>` ＋ 原文逐字。
- 分工：**只出指令不改稿**。以下「改后」文本是给执行方的成品行，执行方落盘后我再验「改没改、有没有改坏」。

## 一 报数（只报四组）

| 组 | 实测 | 结论 |
|---|---|---|
| **逐字** | 引语块 8/8 verbatim（`segment_miss 0`，8 块全为单段连续引语、无 `…` 拼接）；词表例句 22/22（`/tmp/vocab_check_hx.py 17` → `rows=22 missing=0`）；词头 22/22（`/tmp/vocab_head_hx.py 17` → rc=0）；素读 196 条逐字校验 `BAD=0` | ✅ 无缺陷 |
| **对应** | R4 逐块 8/8；施事／归属**调转 0 处**（含本章三处最高危，见 §五 29/30/34） | ✅ 无缺陷 |
| **形态** | 8 项查 7 项过：H1 ✅／导航 5 项 ✅／子项集 ×8 ✅／词表标准 `\|` 表格 ✅／一句话总结 ✅／frontmatter ✅／无 `…` 拼接 ✅；**块数 8 超 `block_target [3,6]`**（`block_hint` 已报，`chapter.sh` rc=0，提示型） | ⚠️ 1 项提示 |
| **断言** | 共核 **78** ＝ 相符 **56**（§五）／提示 **18**／**阻断 4**／假红 0／凭空编造 **0** | ❌ 4 条阻断 |

**块数 ⇒ 硬约束**：本章 8 块已**超**上限 6 ⇒ **任何补漏禁增第 9 块**，L1 只能写进导航。

## 二 阻断（4 条，逐条带原文逐字）

### 阻断 1 · L1（漏）——`:212` 辛西娅把「失去海伦娜」排在「失去力量」之前，md 全篇零提及

**原文逐字**（`text/ch17_chapter_17.txt:212`）：
> `Perhaps they could bespell her to stop stealing Helena’s magic. A part of her ached at the thought. The rush was intoxicating. She would miss feeling the pulse of power. **But she would miss Helena more**, and she couldn’t imagine the woman remaining friends with Cynthia if she kept robbing her gifts.`

**为什么是阻断**：md:11 把本章弧线定为「情绪从心动一路滑到恶心」，md:13 把辛西娅写成「机灵、逞强 → 追问自己做了什么 → 信心消失」。**这条弧线在原文里的转折点就是 `:212`**——她宁可被施咒停下这份力量，因为「她会想念力量的脉动，但她更想念海伦娜」。少了它，md:11 的「心动」在本章没有落点，`:245`–`:254` 的「恶心」也失去对照物。属 S1「漏掉关键转折」。

**修复位置**：md:11（导航·情感弧线位置）。**禁增第 9 块。**

### 阻断 2 · E1（错·跨章术语）——md:40「拉克兰叔叔」×2

**md 原文**（md:40）：「等拿到确凿证据，再交给**拉克兰叔叔**，让苏格兰场去当面质问；或者现在就掉转马车，带着乔治·利珀特的地址去找**拉克兰叔叔**。」

**原文依据（逐字）**：
- `text/ch11_chapter_11.txt:44`：`There’s a superintendent at Scotland Yard ’as nieces with the name of Blair. Lachlan MacDougal.`
- `text/ch06_chapter_6.txt:273`：`his infuriating (beautiful) niece`
- `text/ch07_chapter_7.txt:122`：`took the necklace from his niece`
- `text/ch06_chapter_6.txt:35`：Blair 是**母系**女巫世家姓（`passed down to the Blair women through generations … circle of sisterhood`）

⇒ 他的侄女／外甥女**姓 Blair**，关联走**母系**；「叔叔」＝父之弟，**无立足点**。

**舅／姨父不裁决**，零命中取证（命令＋输出＋退出码）：
```
$ /usr/bin/grep -nEi 'Rowan.{0,80}(husband|wife|married|spouse)|(husband|wife|married|spouse).{0,80}Rowan' text/*.txt
（无输出）  rc=1     ← Rowan 全书无配偶表述
$ /usr/bin/grep -nEi '(Lachlan|MacDougal).{0,80}(husband|wife|married|brother|sister)|(husband|wife|married|brother|sister).{0,80}(Lachlan|MacDougal)' text/*.txt
15 行  rc=0；逐行读毕：brother 全部指 Thomas（辛西娅之兄）、husband 全部指 Hubert（辛西娅之亡夫），
                       没有一条写 Lachlan 自己的兄弟或配偶。
```
⚠️ **命中≠证据**：第一版探针 `Rowan.{0,80}(husband|wife|brother|sister|married)` 返回 rc=0／1 行，命中的是 `ch02:212` `Clio and Ellie were true sisters`——与 Rowan 的兄弟姊妹无关；已拆成上面两条重跑。

**全书分布实测**：`拉克兰叔叔` **12**（ch02×2／ch04×2／ch06×3／ch09×2／ch14×1／**ch17×2**）｜`拉克兰舅舅` **9**（ch23×3／ch24×2／ch25×1／ch26×3）。
**建议**：全书统一为 **`拉克兰舅舅`**——① 唯一有原文支撑的方向是母系，「叔叔」必错；② 后段 4 章（含结局）已在用「舅舅」；③ 舅／姨父既不裁决，取一个**母系且不新增第三套译名**的既有词，改动量最小（12 处）。**依据须写进 `.memory/review-ledger.md`。**

### 阻断 3 · E2（错）——md:24「信则被夹在同一张羊皮纸里」

**md 原文**（md:24）：「地址是这趟出门的目的，**信则被夹在同一张羊皮纸里**，两样东西一主一次，已经分出轻重。」

**原文依据（逐字）**：
- `text/ch17_chapter_17.txt:35`：`carrying a folded piece of parchment holding George Lippert’s address **and a letter**`（两样**并列**）
- `text/ch17_chapter_17.txt:41`：`Cynthia **pocketed the address** and **picked up the letter** to inspect the seal.`

⇒ 地址被揣进衣袋、信被**单独拿起来**验封蜡，是**两个独立物件**，不是一封信夹在羊皮纸里。

**md 自相矛盾（判据 d）**：md:119 词表 `pocketed` 行的例句**正是 `:41` 这一句**，释义「把……揣进衣袋」——同一份 md 里，词表用对了，分析层写反了。

### 阻断 4 · E3（错）——md:94／md:96「读者会自己补上那个名字」／「听不到那个名字被说出口；这份留白……」

**md 原文**：
- md:94：「第二句没有点名，只说'她心里清楚'……句子短，停顿重，**读者会在这句之后自己补上那个名字**。」
- md:96：「读者读到这里，只能确认她心里已经有了答案，**却听不到那个名字被说出口**；这份**留白**让读者的判断和她的判断撞在一起。」

**原文依据（逐字）**（`text/ch17_chapter_17.txt:248`→`:251`）：
> `:248` `Suspicion slithered in Cynthia’s mind like a poisonous snake. Because she knew exactly who sired the babe.`
> `:251` `**Hubert**, you bastard.`

⇒ 名字在**三行之后**就由辛西娅自己在心里骂出来了，原文**没有留白**。

**md 自相矛盾（判据 d）**：md:10 一句话概括自己写了「**又断定孩子的父亲就是休伯特**」——同一份 md 里，导航点出了名字，精读层却说「听不到那个名字被说出口」。

## 三 提示（18 条）

| 编号 | md 位置 | 问题 | 原文依据 | 建议 |
|---|---|---|---|---|
| L2 | md:64 vs md:139 | 「作者没有站出来评论贫富」与 md:139 自己写的金链子／笼子互相拉扯 | `:125` `bound by golden chains` / `their cages were far less comfortable` | 已并入 §四 md:64 改法（E7 同一处） |
| L3 | md:74 | 「用'奇迹'二字把解释推开」漏了紧接一行的自我更正 | `:137` `Or magic.` ／ `:140` `But that is impossible.` | 已并入 §四 md:74 改法 |
| L4 | md:10 | 「用天气打岔遮掩」没写**当着谁** | `:146` `The coachman … looked wide-eyed at the dog, then Helena, then Cynthia.` | 已并入 §四 md:10 改法 |
| L5 | md:13 | 写了「信心消失」，没写信心的**来源** | `:149` `A strange calm flooded Cynthia…` ／ `:152` `Her voice resonated with command.` ／ `:161` `As soon as the dog disappeared, so did her confidence.` | 已并入 §四 md:11 改法 |
| L6 | md:10 | 海伦娜的**两道遮掩指令**全篇未提 | `:173` `Hamlet to stay in the carriage` ／ `:176` `Act normal.`（`:173` 明写是 `The message in her gaze`） | 已并入 §四 md:10 改法 |
| L7 | md:10 | 把「要她当晚去布莱尔宅」写成海伦娜单方面安排，实际是辛西娅先要求解释 | `:191` `‘You’ll have to explain what just happened when we’re alone.’` → `:194` `I think it’s best you come to Blair House tonight.` | 已并入 §四 md:10 改法 |
| L8 | md:13 | 家庭女教师与「两套规矩」这条心理线未收 | `:206` `Governess Smithers had taught her well with her biting birch stick.` | 已并入 §四 md:13 改法。**跨章陷阱**：`Smithers`（辛西娅的家庭女教师）≠ ch11 的管家 `Smith`，两者不是同一人，勿合并 |
| L9 | md:11 | 马车里的调情对答只用「调笑」两字带过 | `:92` `I shouldn’t have said that.` ／ `:116` `I find I like trouble far too much for my own good.` | 可保留现状（md:11 已含「靠近、调笑」）；若要补，**禁增块**，只能扩 md:11 |
| L10 | md:10 | 读起来像「到门口就看见莉莉」，实际先被一个**无名男人**拦住 | `:227` `A large man … ‘Who are ye?’`（**无姓名 tag**）／ `:230` `Behind him, Cynthia heard a gasp.` ／ `:233` 莉莉从里屋出来 | 已并入 §四 md:10 改法。⚠️ 只能写「一个无名的男人」，**不得**写成乔治·利珀特（见 §六 U1） |
| L11 | md:10 | 只写辛西娅的恶心，没写海伦娜**当场骂了一句** | `:236` `‘Oh my,’ Cynthia whispered.` ／ `:239` `‘Damnation,’ Helena cursed.` | 可选：在 md:10 末句前加「海伦娜骂了一声」 |
| E4 | md:13 | 「海伦娜**一路沉着**」 | `:167` `Her **painfully bright** smile made the man wince.` ／ `:173` `Her silver eyes slowly darkened back to grey.` | 已并入 §四 md:13 改法（她在**用力装没事**） |
| E5 | md:12 | 「狐狸**灵兽**」＝第三套译名 | 全书实测：魔宠 **53**／使魔 **13**／灵兽 **2**（`灵兽` 只出现在 ch06、ch17） | 已并入 §四 md:12 改法，统一为**魔宠**（多数派） |
| E6 | md:34 / md:36 | 「两个人都在试探」「海伦娜没有躲」超出引语 | 引语（`:50`）内只有辛西娅一侧的反应 `A secret thrill ran through her.`；海伦娜的主动在 `:59` `She lifted her pinkie up and down over the silk.` | 已并入 §四 md:34／md:36 改法（S3 分析层伸手到引语之外） |
| E7 | md:64 | 「作者没有站出来评论贫富，只让辛西娅的鼻子和眼睛先受不了」把 `:125` 整段抹掉 | `:125` 紧接街景就是一整段贫富评论；**md:139 自己写了这段** | 已并入 §四 md:64 改法。严格说叙述者确实没评论（是自由间接思想），改法据此措辞 |
| E8 | md:10 | 「**随手搁下**」 | `:41` `Can you put this in my room? I shall read it later.` ／ `:44` `Mrs Higgins retrieved the letter` ⇒ 是**叫管家收走** | 已并入 §四 md:10 改法 |
| E9 | md:74 | 「推开解释」的方向不准：原文是推开「奇迹」、马上换上「魔法」、再立刻否认 | `:137` `Or magic.` ／ `:140` `But that is impossible.` | 同 L3，已并入 §四 md:74 改法 |
| E10 | md:106 / md:120 | 词表 `unwarranted`、`dismissal` 两条例句**开头残留原文开引号 `‘`**（其余 20 条无） | `:56` 原句确有 `‘`；属格式瑕疵，`check_vocab.py` 不查 | 删掉两条例句开头的 `‘` |
| E11 | md:110 / md:111 | `Superintendent`、`attractions` 放 ⭐⭐⭐ 高级 ⇒ **档位注水**（S4 ③） | `:77` / `:95`；两词在本书的频率与难度都属进阶 | 移入 ⭐⭐ 进阶（高档留 6 条：condolences／uncommonly／unwarranted／cobblestones／inadvertently／suspicions） |

**形态提示（第 19 条，不计入上表 18）**：块数 **8** 超 `block_target [3,6]`（1894 词，短章）。**判提示不判阻断**，理由：按词数折算的建议区间对短章偏严，8 块与本书众数同量级（ch15=10／ch16=9／ch18=13）。⇒ 但因此**禁增第 9 块**。

## 四 修复指令（整行合并版）

> ⚠️ 以下行**每行同时收到 2–6 条修复**，逐条打补丁会互相覆盖 ⇒ **一律整行替换**。
> 行号以当前 md（139 行）为准。

**md:10（收 E8＋L4＋L6＋L7＋L10）**
- 改前：`- **一句话概括**：希金斯太太送来乔治·利珀特的地址和一封信，辛西娅猜是德文公爵夫人的吊唁信，随手搁下；她与海伦娜乘马车去齐普赛德，商量以向莉莉道歉为名探访。一条恶狗扑向哈姆雷特，辛西娅掌心射出一道能量，用看不见的牵绳把狗拦住；海伦娜用水把狗冲开，辛西娅喝令它回家，随后怀疑自己在偷海伦娜的力量。海伦娜用天气打岔遮掩，要她当晚去布莱尔宅谈。到了利珀特家门口，莉莉掩不住身孕，辛西娅明白休伯特当初开除她正是因为这个孩子，又断定孩子的父亲就是休伯特，骂了一句，恶心涌上来。`
- 改后：`- **一句话概括**：希金斯太太送来乔治·利珀特的地址和一封信，辛西娅猜是德文公爵夫人的吊唁信，叫管家先收进屋里、回头再看；她与海伦娜乘马车去齐普赛德，商量以向莉莉道歉为名探访。一条恶狗扑向哈姆雷特，辛西娅掌心射出一道能量，用看不见的牵绳把狗拦住；海伦娜用水把狗冲开，辛西娅喝令它回家，随后怀疑自己在偷海伦娜的力量。马车夫瞪着眼看完全程，海伦娜便拿天气打岔，要哈姆雷特留在车上、装作什么都没发生；辛西娅要她解释，她约当晚去布莱尔宅谈。到了利珀特家门口，先来开门的是个没有报名字的男人，莉莉从里屋出来，掩不住身孕，辛西娅明白休伯特当初开除她正是因为这个孩子，又断定孩子的父亲就是休伯特，骂了一句，恶心涌上来。`

**md:11（收 L1 阻断＋L5）**
- 改前：`- **情感弧线位置**：利珀特的地址刚到手，两人带着地址一起出门。马车里先是靠近、调笑和轻敌，狗一扑，力量从辛西娅掌心出去，轻松立刻变成惊恐；章末落在利珀特家门口的生理反应上，情绪从心动一路滑到恶心。`
- 改后：`- **情感弧线位置**：利珀特的地址刚到手，两人带着地址一起出门。马车里先是靠近、调笑和轻敌，狗一扑，力量从辛西娅掌心出去，轻松立刻变成惊恐；惊恐之后涌上来一股陌生的镇定，她喝令狗回家，狗一走，镇定也跟着走，剩下的只有「我刚才做了什么」。她甚至愿意被施咒停下这份力量——她会想念力量的脉动，但她更想念海伦娜。章末落在利珀特家门口的生理反应上，情绪从心动一路滑到恶心。`

**md:12（收 E5）**
- 改前：`- **Tropes 兑现/反转**：伪装访客、狐狸灵兽、隐藏力量都在；“需要女巫保护”的人反手用力量拦住恶狗，是这一章的反转；结尾让“解雇女仆”接上“身孕”这条线，前文的家务事由此接上命案线索。`
- 改后：`- **Tropes 兑现/反转**：伪装访客、狐狸魔宠、隐藏力量都在；“需要女巫保护”的人反手用力量拦住恶狗，是这一章的反转；结尾让“解雇女仆”接上“身孕”这条线，前文的家务事由此接上命案线索。`

**md:13（收 E4＋L8）**
- 改前：`- **人物弧线**：辛西娅从马车里的机灵、逞强，到出手后追问自己到底做了什么，狗一走，信心也跟着消失；海伦娜一路沉着，替辛西娅遮掩，又安排晚上的谈话；莉莉只在门口露一面，身孕就把她放到最脆弱的位置。`
- 改后：`- **人物弧线**：辛西娅从马车里的机灵、逞强，到出手后追问自己到底做了什么，狗一走，信心也跟着消失；她记得家庭女教师史密斯尔斯那根桦木条教出来的规矩，如今要在女巫的世界里把规矩重学一遍。海伦娜不是沉着，是当着马车夫用力装没事——笑得过分明亮，反而让对方皱起脸——她替辛西娅遮掩，又应下晚上的谈话；莉莉只在门口露一面，身孕就把她放到最脆弱的位置。`

**md:24（收 E2 阻断）**
- 改前：`**为什么这样写**：开头两句把行动压得很紧：先支使人备车，再让地址和信几乎同时送到。作者没有写她等了多久，只用“男仆还没回来”一句交代时间，读者的注意力就被引到那张羊皮纸和那封信上。地址是这趟出门的目的，信则被夹在同一张羊皮纸里，两样东西一主一次，已经分出轻重。`
- 改后：`**为什么这样写**：开头两句把行动压得很紧：先支使人备车，再让地址和信几乎同时送到。作者没有写她等了多久，只用“男仆还没回来”一句交代时间，读者的注意力就被引到那张羊皮纸和那封信上。地址和信是并列递过来的两样东西，轻重靠处置分开：地址是这趟出门的目的，当场就被揣进衣袋；信则被单独拿起来验封蜡，再交给管家收走，留到以后再看。`

**md:34（收 E6）**
- 改前：`**为什么这样写**：先摆出两个“本来可以”的位置，再一句“她没有”，把选择写成主动。接着只写腿、手指和裙料，动作很小，分量却不轻；最后才给出“隐秘的悸动”，让读者明白这不是无意碰触，而是两个人都在试探。`
- 改后：`**为什么这样写**：先摆出两个“本来可以”的位置，再一句“她没有”，把选择写成主动。接着只写腿、手指和裙料，动作很小，分量却不轻；最后才给出“隐秘的悸动”，让读者明白这不是无意碰触，而是辛西娅自己认领的一次靠近。`

**md:36（收 E6）**
- 改前：`**读者视角提示**：读者看得出辛西娅是故意坐近的，也看得出海伦娜没有躲；这一小段没有一句表白，却比表白更清楚地说明她们走到了哪一步。`
- 改后：`**读者视角提示**：读者看得出辛西娅是故意坐近的；海伦娜在这一段里只露出一根小指，她怎么想、有没有躲，要再过一段——她把小指在绸裙上上下挪动——才见分晓。这一小段没有一句表白，却比表白更清楚地说明她们走到了哪一步。`

**md:40（收 E1 阻断 ×2）**
- 改前：`**中文理解**：海伦娜摇头，说她们不能让对方知道她们已经了解他的罪行，只说自己是去收集消息。等拿到确凿证据，再交给拉克兰叔叔，让苏格兰场去当面质问；或者现在就掉转马车，带着乔治·利珀特的地址去找拉克兰叔叔。`
- 改后：`**中文理解**：海伦娜摇头，说她们不能让对方知道她们已经了解他的罪行，只说自己是去收集消息。等拿到确凿证据，再交给拉克兰舅舅，让苏格兰场去当面质问；或者现在就掉转马车，带着乔治·利珀特的地址去找拉克兰舅舅。`

**md:64（收 E7＋L2）**
- 改前：`**为什么这样写**：先写孩子，再写热，再写污水和臭味，感官一层层压过来；最后一句突然把镜头拉回两人之间那点暧昧，形成硬碰硬的反差。作者没有站出来评论贫富，只让辛西娅的鼻子和眼睛先受不了，读者的不适也就跟着来了。`
- 改后：`**为什么这样写**：先写孩子，再写热，再写污水和臭味，感官一层层压过来；最后一句突然把镜头拉回两人之间那点暧昧，形成硬碰硬的反差。叙述者没有站出来评论贫富，评语是紧接在街景之后、由辛西娅自己想出来的：她承认自己虽被金链子拴着，这些人的笼子却更不舒服。读者的不适先跟着鼻子和眼睛来，判断再跟着她的念头来。`

**md:74（收 E9＋L3）**
- 改前：`**为什么这样写**：动作写得极快：喊、伸手、能量飞出、狗被拽住，几乎不给读者喘息。等到“看不见的绳子”出现，作者才停下来解释，却又用“奇迹”二字把解释推开。力量在这里不是仪式，而是身体的本能反应，越是这样，越让人不安。`
- 改后：`**为什么这样写**：动作写得极快：喊、伸手、能量飞出、狗被拽住，几乎不给读者喘息。等到“看不见的绳子”出现，作者才停下来解释，却先把它叫作“奇迹”，下一行立刻自我更正成“魔法”，紧接着又否认这是可能的。力量在这里不是仪式，而是身体的本能反应，越是这样，越让人不安。`

**md:94（收 E3 阻断）**
- 改前：`**为什么这样写**：临近章末，作者用一条蛇来收束这份怀疑，把“怀疑”写成会动、会咬人的东西。第二句没有点名，只说“她心里清楚”，既保留了她的判断，也没有让叙述者替她把话说死。句子短，停顿重，读者会在这句之后自己补上那个名字。`
- 改后：`**为什么这样写**：临近章末，作者用一条蛇来收束这份怀疑，把“怀疑”写成会动、会咬人的东西。第二句没有点名，只说“她心里清楚”，既保留了她的判断，也没有让叙述者替她把话说死。句子短，停顿重；名字压在这一句之外，再过三行，由她自己骂出来。`

**md:96（收 E3 阻断）**
- 改前：`**读者视角提示**：读者读到这里，只能确认她心里已经有了答案，却听不到那个名字被说出口；这份留白让读者的判断和她的判断撞在一起。`
- 改后：`**读者视角提示**：读者读到这里，先只拿到“她心里已经有了答案”，答案本身还压着；等下一句“休伯特，你这个混蛋”落下，读者的判断和她的判断就在同一个名字上撞在一起。`

**md:106 / md:120（收 E10）**：删掉两条例句开头的 `‘`，其余不动。
**md:110 / md:111（收 E11）**：把 `Superintendent`、`attractions` 两行整行移到 `### ⭐⭐ 进阶` 表内（高档留 6 条）。

> **不许动的地方**：① 8 个引语块（全部 verbatim，动一个字就破坏逐字层）；② md:86「书里没有谁证实她真的在偷力量」——已被后文两处**正面支持**（见 §五 37），任何人不得以「读着不对」为由改动；③ 词表 `pocketed`／`brother`／`mother` 等行的例句与释义（逐字核过，正确）；④ 块数 8（禁增第 9 块）。

## 五 R5.5 · 已核实为正确（56 条）

> 凡在此列出的，**不得再被后续审查以「感觉不对」为由改动**。

**内容断言（17）**
1. md:10「德文公爵夫人的吊唁信」→ `:41` `the Duchess of Devon has no doubt written to extend her condolences.`
2. md:10「商量以向莉莉道歉为名探访」→ `:56` `I have wanted to apologise to Lily for Hubert’s abrupt and unwarranted dismissal. Perhaps that could be our reason for visiting?’`
3. md:10「一条恶狗扑向哈姆雷特」→ `:128` `a stray dog caught sight of Hamlet poking his copper nose out of the door` ／ `:131` `Hamlet had no escape as the much larger, much fiercer dog bunched his muscles to leap into the carriage.`
4. md:10「辛西娅掌心射出一道能量」→ `:134` `A snap of energy flew from her palm to the dog.`
5. md:10「海伦娜用水把狗冲开」→ `:143` `rushing water pooled around the animal’s feet, forcing him to lose his ground and be swept several feet away`
6. md:10「辛西娅喝令它回家」→ `:152` `‘Go home.’ Her voice resonated with command.` ／ `:158` `‘Now.’ She pointed away from the carriage.`
7. md:10「海伦娜用天气打岔遮掩」→ `:167` `‘Such strange weather we’re having today.’ Helena spoke to the coachman as though nothing untoward had taken place.`
8. md:10「莉莉掩不住身孕」→ `:242` `Lily’s hastily altered dress couldn’t hide a painfully obvious swelling.`
9. md:10「明白休伯特当初开除她正是因为这个孩子」→ `:245` `That is why Hubert fired her. Because she is with child.`（自由间接思想，POV＝辛西娅，md 写「辛西娅明白」**未误挂叙述者**）
10. md:12「'需要女巫保护'的人反手用力量拦住恶狗」＝反转 → 反转对象是 ch15 `:95` `‘Unless I have a witch with me to keep me safe.’`
11. md:12「结尾让'解雇女仆'接上'身孕'这条线」→ `:56` dismissal → `:242`/`:245` with child
12. md:14「全章贴辛西娅的限知，没有视角切换」→ `:176` `Act normal.` 是**海伦娜的眼神讯息**（`:173` `The message in her gaze was impossible to miss.`），不是心声、不是 POV 切换
13. md:14「也没有空行分场」→ `:35`–`:254` 无场景分隔符（源文件空行是提取件的段落分隔）
14. md:14「后半把句子切短，用连续问句和单句段落加快心跳」→ **实数核过**：单句成段 4 处（`:176` `Act normal.`／`:182` `Later.`／`:188` `Like a sensible person.`／`:200` `Hellfire.`）＋连问 2 组（`:164` 三连问／`:197` 四连问）
15. md:14「章末停在一个生理反应上，不解释」→ `:254` `Nausea washed through her.` 是全章最后一句
16. md:139「海伦娜只回了一句'很多事'」→ `:83` `‘Many things.’`
17. md:139「自己虽被金链子拴住，别人的笼子却更不舒服」→ `:125`

**时序（3）**
18. md:10 事件链顺序与 `:35/:41 → :47/:56 → :128/:131 → :134 → :143 → :152/:158 → :140/:197 → :167 → :194 → :221–:254` 一致
19. md:11「马车里靠近调笑 → 狗一扑 → 惊恐」与 `:50`–`:116` → `:131` → `:134` → `:164` 一致
20. md:14「前半对话、后半短句」实测成立（前半 `:35`–`:125` 以对话为主）
> 附注：「怀疑偷力量」在原文出现**两次**——`:140`（紧随拦狗）与 `:197`。md:10 把它排在「喝令回家」之后，与 `:197` 一致，**不算时序错**。

**R4 施事／受事／归属（16）**
21. 原句 1：`carrying…` 的逻辑主语＝Mrs Higgins → md:20「希金斯太太先敲了门，手里拿着…」✅
22. 原句 2：`Helena’s pinkie brushed against **her** black silk skirt` 的 her＝**Cynthia** → md:30「擦过她的黑绸裙」**未调转** ✅
23. 原句 2：`A secret thrill ran through her` 的 her＝Cynthia → md:30「从她身上窜过」✅
24. 原句 3：说话人＝**Helena**（`:74` `Helena shook her head.`）→ md:40「海伦娜摇头，说…」✅
25. 原句 4：说话人＝**Cynthia**（`:83` 才轮到 Helena `‘Many things.’`）→ md:50「辛西娅说…」**未把话安到海伦娜头上** ✅
26. 原句 4：`And I have a witch to protect me` 的 witch＝Helena、me＝Cynthia → md:50「身边还有一位女巫护着」✅
27. 原句 5：`The heat was amplified **by** the brick buildings` → md:60「砖楼把太阳吸进去…把热气放大」**`by` 的施动者方向正确** ✅
28. 原句 5：`It rather distracted Cynthia` 的施动者＝街景 → md:60「这一切反倒把辛西娅…拽了出来」✅
29. ★原句 6：`A snap of energy flew from **her palm**` 的 her＝Cynthia → md:70「从她掌心飞出」**未误挂到海伦娜** ✅
30. ★原句 6：`An invisible leash **she** controlled` 的 she＝Cynthia → md:70「由她控制的隐形牵绳」✅；`he jerked back` 的 he＝狗（阳性）→ md:70「狗猛地往后一扯」✅
31. 原句 7：`Nerves threatened to choke **her**`＝Cynthia → md:80「几乎让她喘不上气」✅
32. 原句 7：`Helena looked very serious` → md:80「海伦娜神色很严肃」✅
33. 原句 8：`Suspicion slithered in **Cynthia’s** mind` → md:90「在她脑子里滑行」✅
34. ★原句 8：`**she** knew exactly who sired the babe` 的 she＝Cynthia、`sired` 的施动者＝孩子的父亲 → md:90「她太清楚这个孩子的父亲是谁了」✅
35. 原句 7：`she was stealing **Helena’s** powers` 的方向＝**辛西娅偷海伦娜** → md:80「偷走海伦娜的力量」**未调转** ✅
36. R4 三问全 8 块通过，**施事／归属调转 0 处**（本章三处最高危＝29／30／35，全部未踩）

**跨章与形式（20）**
37. ★md:86「这些只是辛西娅的猜测，**书里没有谁证实她真的在偷力量**」→ 被后文**两处正面否定**支持：`text/ch19_chapter_19.txt:342` `‘You aren’t stealing my magic, Cyn. Your power comes from within you.’` ／ `text/ch20_chapter_20.txt:204` `You spoke of stealing Helena’s abilities, but that isn’t possible. Humans can’t steal our elemental power.` ⇒ **此句为正确 hedge，不得改成断言**
38. md:24「作者没有写她等了多久，只用'男仆还没回来'一句交代时间」→ `:35` `Before he returned`
39. md:26「读者会先看见地址，再看见信」→ `:35` `address and a letter` 顺序一致
40. md:34「先摆出两个'本来可以'的位置，再一句'她没有'」→ **实数核过**：`:50` `could have sat` ／ `Or shifted` ／ `But she did not.`＝两项＋一句否定
41. md:44「先把'知道'藏起来，再把'取证'摆在前面，最后给出两条路」→ `:74` `won’t let him know` → `gathering information`/`firm evidence` → `Or we can turn the carriage around`
42. md:44「海伦娜没有把话说成命令」→ `:74` 全段为陈述句＋选项，无祈使
43. md:54「前两句是给自己壮胆，第三句干脆把保护者抬出来」→ **实数核过**：`:80` 引语内三句切分与内容一一对应（7 词／11 词／13 词）
44. md:54「只用'闭上嘴'一个动作收住」→ `:80` `She snapped her mouth shut`（**一个**动作，量化成立）
45. md:64「先写孩子，再写热，再写污水和臭味」→ `:122` 四句顺序一致
46. md:66「这条街不是背景板：它闯进她的感官，也把她的心思…拽开」→ `:122` `It rather distracted Cynthia`
47. md:74「喊、伸手、能量飞出、狗被拽住」→ `:134` 四个动作按此序出现在同一句与紧邻句
48. md:76「她做到了，但她并不知道自己怎么做到的」→ `:137` `Or magic.` ／ `:140` `Unless I’m somehow stealing power from Helena` ／ `:164` `What the bloody hell just happened? What did I just do? And how in blazes did I do it?`
49. md:84「一连**四个**问句」→ **实数核过**：`:197` `What if…?`／`Is that how…?`／`Or why…?`／`Or the reason…?`＝**4**（md 引语块内即可数）
50. md:84「海伦娜的严肃表情只放在开头，剩下全是辛西娅的内心」→ `:197` 结构一致
51. md:90「怀疑像一条毒蛇」→ `:248` `like a poisonous snake`
52. md:10／md:12「哈姆雷特」是**狐狸**、雄性、**海伦娜的**魔宠 → `:68` `At Helena’s question, he lifted his own copper brows`
53. 词表 22 条例句**全部**是本章原句（`missing=0`），逐条抽核行号见 `3-diff.md` §六
54. 词表 22 条词头**全部**在本章原文（rc=0）
55. 词表 `pocketed` 释义「把……揣进衣袋」与 `:41` 一致 ⇒ **反过来证 md:24 的 E2 是分析层单点错误**，不是词表错
56. 引语块无 `…` 拼接（`segment_miss 0`）；H1 `# 17. Chapter Seventeen` 与本书 `# NN. Chapter NN` 形态一致；导航 5 项齐；子项集（中文理解／关键词／为什么这样写／读者视角提示）×8 齐；frontmatter 与一句话总结齐

## 六 不裁决（U1–U8）＋ 覆盖声明

| 编号 | 事项 | 为什么不裁决 |
|---|---|---|
| U1 | `:227` 开门的高大男人是谁 | **无姓名 tag**。按地点与 `:233` 推断很可能是乔治·利珀特本人，但原文未点名 ⇒ md 未写他是谁**不算缺陷**；修复时只能写「一个无名的男人」 |
| U2 | 德文公爵夫人的信里写了什么 | `:41` 辛西娅只是**猜**（`has no doubt written`），当场没拆（`I shall read it later`）⇒ 不得写实 |
| U3 | 辛西娅是否真的在偷海伦娜的力量 | 本章不裁决；`ch19:342`／`ch20:204` 明确否定 |
| U4 | Lachlan 是舅舅还是姨父 | 见 §二 阻断 2；原文未写血缘或姻亲 |
| U5 | Lachlan 是辛西娅的 uncle 还是海伦娜的 uncle | `ch03:315` `her uncle`（Cynthia 的）vs `ch16:209` `your uncle`（海伦娜的）⇒ **原文自身不一致**，不裁决、不判 md 缺陷 |
| U6 | `:245` `That is why Hubert fired her.` 是否确为事实 | 是辛西娅的**推断**（自由间接思想），不是叙述者断言；莉莉一侧的说法要到 ch18 才有 |
| U7 | `:248` `who sired the babe` 的答案是否属实 | 原文 `:251` 给出的是**辛西娅的判断**，是否属实本章不裁决 |
| U8 | `:170` 马车夫是否真看出了什么 | `:146` 他 `looked wide-eyed`，但 `:167`–`:170` 他顺着海伦娜的话头接了下去 |

**覆盖声明**：本章已覆盖——引语逐字（8/8）、词表例句与词头（22/22）、R4 逐块对应与三问（8/8）、导航 5 行的全部内容断言、8 块的「为什么这样写／读者视角提示」共 16 段分析层、一句话总结、形态 8 项、时序、语料层（推广行 0）、跨章 hedge 核实。**未覆盖／本章特有盲区**：
1. **中文分析层的断言无门禁**（`check_chinese_layer.py` 只查中文占比与敷衍，不查事实）——E2／E3／E7 全靠人判。
2. **否定断言无门禁**——「作者没有站出来评论贫富」「听不到那个名字被说出口」这类句子，机器一律绿灯。
3. **形式／节奏断言**（「句子越说越轻快」「句子短，停顿重」）需**落笔前先数词**才可判；本章已逐条数过（§五 40/43/44/49），未数的一律不判。
4. **词表档位合理性无门禁**（E11 注水靠人判）；`## 本章词汇` 节不在 `check_vocab.py` 扫描域，本章用自建 `/tmp/vocab_check_hx.py`＋`/tmp/vocab_head_hx.py` 补。
5. **词表例句的行内标点残留**（E10）无门禁。
6. **块数是提示型**（`block_hint`，rc 仍 0）⇒ 门禁不会因「该补而未补」判红，也不会拦住修复方增块；**「禁增第 9 块」只存在于本判定表**。
7. **R1 底稿的 traps/unresolved 是「主张」不是「事实」**（ch16 T17 实证被子代理判错）⇒ 本章 30 条 traps 已由主会话逐条回原文核，其中 T 层无一升级为缺陷。
8. **跨章译名一致性无门禁**（E1 拉克兰叔叔／E5 灵兽）——只能靠全书 grep 计数。

## 七 结论

**ch17：阻断 4（L1／E1／E2／E3）· 提示 18＋形态 1 · 凭空 0 · 假红 0 · 对应 8/8 · 逐字全绿。**
修复方式：§四 整行替换（md:10／11／12／13／24／34／36／40／64／74／94／96）＋ md:106/120 删残留引号 ＋ md:110/111 移档。**不改引语、不增块、不动 md:86。**
