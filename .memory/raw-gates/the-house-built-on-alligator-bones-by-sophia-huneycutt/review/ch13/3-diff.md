# ch13（书内 Chapter Twelve）深审 R3/R4 三张单子

素读基线：`review/ch13/1-suread.json`（139 条事实／**0 MISS**，只读 `text/ch13_chapter_twelve.txt`，写完才开 md）
机器层：`review/ch13/2-machine.json` → verdict `ok`（blocks 6 ∈ target [4,7]；segments 8／MISS 0；words 2286；struct_bad 0；cjk_low 0；template 0）
直撇号探针：`/tmp/apos.txt` 列 ch13 **8 站**（本文件末节逐站落点）
词表：15 行例句展平逐字 **0 MISS**（`python3` 现算，见假红 F-13-6 下方命令）

> 本章形态与 ch07／ch09／ch11／ch12 同型：引语层全绿，人工发现**全部落在中文断言层**；且承重判读集中在导航五句，所以红点一半在 md:10–md:14。

## 🟥 阻断（9）

### C-13-1 施事归错：把叙述者的同位语安到 Harrison 嘴里
- md:54：**「"the official term for" 由讲解者自己说出，等于当场承认 processing 是一个官方消毒词」**
- 原文逐字：`text/ch13_chapter_twelve.txt:135` — `Harrison pulled a key off his belt loop ring and opened one of them, explaining that we were entering the processing spaces—the official term for alligator killing and skinning.`
- 判定：`:135` 是**转述层**（`explaining that we were entering…`，无人称引号），破折号后的同位语属于叙述语言，不是 Harrison 说出的话；本章 Harrison 关于 processing spaces **没有任何直接引语**（他开口的是 :138 凉拖、:150 之后逐间报名，均为 `He named each room` 转述）。「由讲解者自己说出」「当场承认」两词把叙述者的措辞升级成角色的自认，随后整段分析（术语的体面 vs 房间的实情）就架在错归属上。md:14 的「由他亲口给出并被叙述者当场戳破为官方说法」同型但方向勉强对，只需与改后口径统一。
- 改法：「同位语 `the official term for alligator killing and skinning` 出自叙述者的转述层——Harrison 的这一路讲解在原文里全用 `explaining that…`／`He named each room` 转写，没有一句直接引语。把杀戮改写成车间词汇的是叙述语言本身。」

### C-13-2 计数断言错：「自报两件事」漏掉本姓
- md:13：**「叙述者在本章自报两件事：心脏喝不了多少咖啡、她画的是 nightmares」**
- 原文逐字：`:45` — `I wasn’t a coffee drinker—my heart couldn’t handle much of it`；`:66` — `“Nightmares.”`；**`:249` — `“It’s Beaumont,” I said absently.`**（紧接 `I didn’t want Harrison to think he could order me around`）
- 判定：本章第三次自报是她**本姓 Beaumont**（对 Harrison 的 "Miss Greer" 的更正），且是全书叙述者真名落点之一；写成「两件事」是把计数当修辞，实际构成漏项。取证：`/usr/bin/grep -n 'It’s Beaumont' text/ch13_chapter_twelve.txt` → 249 命中；md 内 `/usr/bin/grep -c Beaumont` 见「已核实为正确」节。
- 改法：「自报三件事：心脏喝不了多少咖啡、她画的是 nightmares、以及被叫 Miss Greer 时更正自己本姓 Beaumont」。

### C-13-3 凭空时距（成组同类，两处）
- md:44：**「一句就把前面两分钟的寒暄全部重写成刺探」**
- md:70：**「骨头去哪的问题脱口而出，她过了几秒才明白为什么会问这句」**
- 原文逐字：`:78` — `So that’s why he’d brought me the coffee.`（前无分钟数，递咖啡到顿悟横跨 :15–:78 数十个对白回合）；`:241`–`:243` — `“What do you mean?”` / `I’d asked the question before realizing why:`（`before realizing` 只写「说完才意识到」，无秒）
- 判定：分析层给原文没有的时间量词盖章，属本库既有缺陷簇「无据时刻／时距」。两处同一形态，一并整改。
- 改法：md:44「一句就把前面那番寒暄全部重写成刺探」；md:70「话出口之后她才明白自己为什么会问这句」。

### C-13-4 语法术语误称：`I'd be creating` 不是「习惯性将来时」
- md:24：**「"one minute… the next" 配 "I'd be creating" 这个习惯性将来时，把走神写成每天重播的循环而不是一次失误」**
- 原文逐字：`:9` — `I’d be creating a new file on the computer one minute, then labeling it with Mama’s words the next.`
- 判定：句中 `I’d` = `I would`，`would be creating` 是**过去反复／惯常**的进行式（回忆视角里「每天都是这样」），与「将来」无关；叙述者此刻在写第二天下午的既往状态。时态误称属中文分析层四组成片同类之一。后半句的判断（重播的循环）是对的，只换术语。
- 改法：「配 `I’d be creating` 这个 would 进行式（过去视角里的每日重播）」。

### C-13-5 词义误读撑起一环分析：`short with` 被当成数量「短」
- md:34：**「末句把法庭从公司缩小到个人道德账面，"short with him" 把坏脾气写成"短"了一点的小数目——小到不配记进坏账，于是她当场宣判自己无罪。」**
- 原文逐字：`:33` — `I wasn’t a bad person for being short with him.`
- 判定：`be short with someone` ＝ 态度生硬／简短，是 manners 词不是 quantity 词；「小数目」「不配记进坏账」是把形容词按字面折算成算术。该块其余分析（"openly" 承认给对方听、`but I didn’t care` 卸责、so 焊死献殷勤与遗嘱因果）成立。
- 改法：「末句把法庭从公司账目缩到个人道德账面——罪名从『抢帝国』降到『态度生硬了一次』，她当场宣判自己无罪」。

### C-13-6 情感弧线结论无据，且与本章自白正面相抵
- md:11：**「收束她的不是恐惧，而是看见一个人低头一瞬带来的安静。」**
- 原文逐字：`:225` — `Closing my eyes, I stepped backward. I didn’t want to know what I’d feel if I kept watching, didn’t want her words to be true, didn’t want to be the twisted person she believed I was—a raging creature drawn to darkness.`；`:255` — `Gazzie had turned to face Ida Greer’s portrait. For a breath—only a breath, no longer—she bowed her head, like she was praying.`
- 判定：本章末句只写 Gazzie 的动作＋`like she was praying`，**通篇没有叙述者被「安静」收束的记录**；而紧邻的 :225 给出的恰恰是她对自家 appetite 的恐惧（不想知道再看下去自己会有什么感觉）。md 一边删掉「不敢知道自己会有什么感觉」这笔，一边代她宣布「不是恐惧」——凭空心理结论 + 认知对冲被抹平，同一句里两犯。
- 改法：「收束处她把目光从玻璃上收回来——先是不敢知道自己再看下去会有什么感觉（:225），最后停在 Gazzie 对着画像低头的那一息上；原文没有交代这一瞬给她什么情绪，只给了时长」。

### C-13-7 承重信息缺失：监管、通融与「Greers 建得早」（整块）
- md 导航五句、6 个精读块、15 行词表**全无**。
- 原文逐字：`:198` — `“The farm must not get regular inspections,” I mused, shifting uncomfortably.`；`:201` — `“We get them pretty frequently from the Florida Fish and Wildlife Conservation Commission and the Florida Department of Agriculture and Consumer Services. But Gazzie gets a heads-up from her contacts, so when they’re around, she’s on her best behavior. And even if she weren’t…” His cheek twitched into an ironic smile. “The Greers have been around forever. One of the oldest farms in the state. There’s a certain amount of leniency that comes with that. Friends in high places and all.”`；另 `:195` — `I wondered if my coworkers in Savannah could name the exact regulations my grandmother was surely violating. Probably not.`
- 判定：这是本章唯一由在场者**直接说明**的「农场怎么运转」制度信息，也是 ch12:141「Greer Fine Alligators was in some sort of trouble」在本章的兑付点——违规靠提前得到消息＋建场最老换通融，与书名句「built their fortune on alligator bones」同一条账；:195 还带着 `surely violating` / `Probably not` 两层对冲，md 一个都没接。
- 取证：`/usr/bin/grep -nE 'Fish and Wildlife|Agriculture|检查|监管|豁免|通融|contacts' "ch13 processing spaces and alligator bones.md"` → **无输出，退出码 1**
- 改法：md:14 或原句 4／5 的「为什么这样写」补一句「Harrison 答得比她预期坦白：检查来自州渔务与农业两个厅，但 Gazzie 有内线提前接到信儿；就算不接也另有照拂——Greer 家是有史以来最老的场子之一，『上面有朋友』」。

### C-13-8 承重信息缺失：第二次挥棒与「鼻子贴上玻璃」
- 原文逐字：`:216` — `When Gazzie stood, the alligator feebly moved its foot forward. It wasn’t dead. Not quite. She cursed and grabbed the baseball bat. The pathetic beast dragged itself along the floor, trying to escape, but she followed it to the wall, lifted the baseball bat, and slammed it over its head. Then she raised it again.`；`:219` — `I leaned forward, nose bumping the glass. What did alligators look like inside?`
- 判定：md:11 的情感弧线直接从「第一次敲＋刀」跳到「闭眼退开」，把本章的道德 hinge（鳄鱼没死透、它往墙根爬、她跟着再打、**然后又举起来**）与叙述者的反应（不是后退而是**把鼻子贴到玻璃上**、自问里面长什么样）整块删掉。:219 正是 Mama 那句 "tame that devil" 要坐实的**动作证据**——没有它，md:11 的「被钉在观察窗上」与 md:64 的「判断被暂扣着」都失去原文支撑。词表只在 `baseball bat` 一行引到 `She cursed and grabbed the baseball bat.`（例句层），判读层没有。
- 改法：md:11 弧线补「第二次挥棒＋她把鼻子贴上玻璃自问鳄鱼里面长什么样」，再接 `You’d better tame that devil in you`（:222）与闭眼退开。

### C-13-9 自造对照替换原文比喻：「和一把锤子没有区别」
- md:64：**「棒球棍在她手里和一把锤子没有区别」**
- 原文逐字：`:180` — `She’d shut down the alligator as easily as anyone else might pull a battery out of a toy.`
- 判定：原文把去仪式化写成「像别人从玩具里抠电池一样随手」——**对象是省力与家常**，且随后 :192 还有 `Did she care that she was hurting the alligator? Or did she simply not think about it anymore?` 两问；md 换成工具类比（锤子），既无出处又丢掉「家常」这一层（:162 她仍穿着到场那身牛仔裤白衬衫）。属「分析层自造对照＝凭空属性」，同时是原文比喻的漏收。
- 改法：删「和一把锤子没有区别」，改引 :180 的抠电池比喻，并补一句「叙述者随即自问：她在不在乎这条鳄鱼疼？还是她早就不去想它疼了（:192）」。

## 🟡 提示（6）

### C-13-T1 章内时序微偏：「离场时她问出骨头去哪」
- md:10 — 问答发生在屠宰间窗外、Harrison 说 `Show’s over, Miss Greer.`（:246）**之前**；「Show's over」之后两人才转身，且她还在回头看（:252）。改「临走前／看完最后一眼时」。

### C-13-T2 关系极性放大：「调情式的对峙」
- md:12 — 吸引的评点全在叙述者单方面：:18 衣着与 `he could’ve been a porn star`、:48 `smelled like dryer sheets`（"to my annoyance"）、:90 仰头看清身高差后「更生气」；Harrison 侧是 `Politeness strained his voice`（:69）、`eagerness crept into his voice`（:75）的刺探。「调情式」把单向写成双向。

### C-13-T3 中文理解人称不统一：「叙述者已经漂进」
- md:20 — 同栏其余各块用「她／两人」，此处插入元叙述称谓。第一人称原句的中文理解宜统一（本库既有口径：译成「我」或「她」，不写「叙述者」）。

### C-13-T4 削平限定：「身高差六英寸」
- md:12 — 原文 :90 `he had at least six inches on me`；「至少」被吃掉。与 C-13-6 同源（认知对冲）。

### C-13-T5 「家务物件」+ 漏掉着装的时间连续线索
- md:64 — `duct tape` 讲成家务物件勉强；更值是 :162 `To my surprise, she still wore the jeans and white button-down shirt she’d arrived in.`——这是「同一天／连日」的连续证据（她到场那身还没换），md:60 中文理解未译该句（引语块也未截到），判读层未点。

### C-13-T6 读者视角提示承诺了一个原文没有的回环
- md:46：**「留意"答案"这个词在这章后面几段里的兑价」**
- 取证：`/usr/bin/grep -n -i 'answer' text/ch13_chapter_twelve.txt` → 仅 `:78` 一处命中（退出码 0，1 hit）；后续问答用的是 `What’s next?`（:231）、`bones`／`skulls`／`trash`（:243–:246）。改法：换成「留意她此后每一处『不让他拿到答案』的答复，如何换来下一步靠近农场内部」。

## ⬜ 判为假红（6，勿改）

- **F-13-1「Gazzie 全程没有台词」（md:13）** — 含引号且含 `Gazzie` 的行共 8 处（:36/:84/:111/:120/:141/:183/:189/:201），全部是 Harrison 或叙述者**提及**她，无一句直接引语归她 ⇒ 判定正确，属本章「在场却不出声」手法，不许在下一轮被"补台词"。
- **F-13-2「第二天工作到下午／第二个下午」（md:10、md:20）** — 与 ch12（首个农场日）时序自洽：ch11 早餐 `You’ll start tomorrow` → ch12 次晨 → ch13 `by my second afternoon`。非偏移。
- **F-13-3「Nova 声明过禁止进入的那几扇门」** — :135 `the doors Nova had declared off-limits`，过去完成与 ch12:93 的声明点正确对应，跨章指向无误。
- **F-13-4「她前一天就见过的那个瘦削、留山羊胡的男人」** — :162 `the thin goateed man I’d seen the day before`，与 ch12:84 走过窗口的 `A thin goateed man in a bright green tee` 同一人，不是凭空认人。
- **F-13-5「Ida 主画像的又一份拷贝挂在屠宰间门上方」** — :150 `another copy of Ida’s primary portrait hung`；「又一份」是原文 `another copy` 的直读。
- **F-13-6「不加引号不加说明」（md:24）** — :9 原文确为 `…with Mama’s words the next. The devil’s inside.`，无引号 ✓。
- 词表逐字复核命令（0 MISS，15 行）：`python3` 展平（弯引号／直引号、`—`、多空格归一）后 `例句 not in 原文` 计数＝0。

## ✏️ 直撇号（8 站，md 侧引语字形与原文不符）

原文通篇弯撇号；md 这 8 处用直撇号书写**英文原句片段**，机器层不覆盖，须手改：

| 行 | 站 | 站点 |
|---|---|---|
| 11 | ×2 | `couldn't tear my eyes away`／`You'd better tame that devil in you` |
| 20 | ×1 | `The devil's inside` |
| 24 | ×1 | `I'd be creating` |
| 34 | ×2 | `but I didn't care`／`so she'd will him her empire` |
| 44 | ×2 | `"So that's why"`／`"wouldn't make it easy for him to get answers"` |

（注：md:34 的 `"openly"`、md:74 的 `"asked the question before realizing why"` 无撇号，不列。）
