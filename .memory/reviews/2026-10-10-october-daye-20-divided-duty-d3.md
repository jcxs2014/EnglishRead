# A Divided Duty（October Daye #20）五步审查 · d 步语义二审 — d3

组号：d3（读者代理，无写作上下文）
覆盖章节：ch09 nine / ch10 ten / ch11 eleven / ch12 twelve（4 章）
依据的 text/ 文件：`text/ch09_nine.txt`、`text/ch10_ten.txt`、`text/ch11_eleven.txt`、`text/ch12_twelve.txt`
方法：逐块「引语↔分析」四查（对应性/截短 · 说话人 · 事实与章节引用 · 语法断言）；引语逐字用展平子串核（31/31 全命中）。

---

## ch09 nine（`ch09 nine.md` ↔ `text/ch09_nine.txt`）

### 逐块核对

- 原句 1 — ✅（引语 :26 逐字；镜像句法/开场提问均属实）
- 原句 2 — ✅（引语 :74 逐字；白雪公主三联符、:86 Tybalt"讲故事的人"确在其后）
- 原句 3 — ❌【事实断言】"石墙"实为木墙；另 ❓存疑"破折号插入语"
- 原句 4 — ❌【语义不对应】读者视角"他抗议的内容不是『别嘲讽我』"与引语直接冲突
- 原句 5 — ❌【无出处断言+同块自相矛盾】"信息欠账留到 Acacia 出场才还"
- 原句 6 — ✅（引语 :422 逐字；"第一次看见幻象盖住的东西"、pain 之"推测从句"属实）
- 原句 7 — ❌【空间事实】"Luna 就躺在**附近**的储藏室"——实为同一间、叙述者跪其旁
- 原句 8 — ✅（引语 :524 逐字；三词回答 I don't know. 属实）

本章块数 8/8；报警 4；存疑 1

### 发现明细

**ch09-1［报警·事实断言］ch09 nine.md:43 · 原句 3 —— 墙的材质写错，且与同文件互斥**

- md 逐字（:43 首句）：「石墙在他们面前自行裂开、露出一条黑暗通道」
- text 证据：`text/ch09_nine.txt:110` 逐字「facing a tall wall made of tree trunks bound together and stabbing into the sky」；`:149` 逐字「And the wood between them groaned.」——墙以树干捆成，是木墙；且门是被白烛火引燃后开启的（:131–149），"自行"亦不确。
- 同文件自证：本 md:10 导航自称「以白色烛火叩开**木墙**」，与 :43「石墙」互斥。
- 建议：改「木墙……应火而开」。

**ch09-2［报警·语义不对应］ch09 nine.md:55 · 原句 4 —— 读者视角否定了引语里实际存在的要求**

- md 逐字（:55）：「注意他抗议的内容不是"别嘲讽我"，而是"别把我看成需要护着的对象"」
- text 证据：`text/ch09_nine.txt:191` 逐字「But if you could refrain from responding to everything I say with sarcasm, I would appreciate it.」——"别每句都嘲讽"正是他提出的要求本身，"不是『别嘲讽我』"与引语直接冲突。
- 建议：改「他抗议的不**只**是『别嘲讽我』，更是『别把我看成需要护着的对象』」。

**ch09-3［报警·无出处断言+同块矛盾］ch09 nine.md:63 · 原句 5 —— "信息欠账留到 Acacia 出场才还"在本章无出处**

- md 逐字（:63 末）：「作者在这里不给解释、不给名字，只让一个匿名身影道谢、再让全场用动作复述一遍，信息欠账留到 Acacia 出场才还」
- text 证据：ch09 全章 `grep -i "grateful\|thank"` 仅 :308 一处（即引语本身）；Acacia 出场（:320）之后至章末（:530）未再出现"感激/致谢"的任何解释，那名匿名身影的名字也未再交代。
- 同块自相矛盾：本块 :65 逐字「这群人在"领主已死"之后立场悬空，本章没有把答案补齐」——与 :63「留到 Acacia 出场才还」互斥。
- 建议：删「信息欠账留到 Acacia 出场才还」或改「这笔欠账本章未还」。

**ch09-4［报警·空间事实］ch09 nine.md:85 · 原句 7 —— "附近的储藏室"**

- md 逐字（:85）：「注意这段话的场合：她说这些时，被袭击成重伤的 Luna 就躺在附近的储藏室里。」
- text 证据：`text/ch09_nine.txt:461` 逐字「We entered into what had apparently been a storage room of some point in the past」；`:470` 逐字「rushed to drop to my knees beside her」；`:476` 即本块引语（Acacia 当场答话）。Luna 就在**同一间**储藏室里、叙述者跪在她身旁，不是"附近"的另一间。
- 建议：「就躺在同一间储藏室里（她跪在一旁）」。

**ch09-5［存疑］ch09 nine.md:43 · 原句 3 —— "破折号插入语"**

- md 逐字：「更妙的是那个破折号插入语」
- text 证据：`text/ch09_nine.txt:152` 逐字「After a momentary pause, no doubt to question why he had married a madwoman to begin with, Tybalt followed.」——英文原文是逗号插入语，全句无破折号（本 md 自己的中译 :39 用了双破折号）。
- 处置建议：属"描述的是译文标点而非原文"：若按英文作语法分析，宜改「逗号插入语」；若确指中译标点，可不动。留待修复方定夺。

（本章导航四项、一句话总结回核通过，未计发现。）

---

## ch10 ten（`ch10 ten.md` ↔ `text/ch10_ten.txt`）

### 逐块核对

- 原句 1 — ❌【断言不实】"三句一处比一处短"（实 26/14/16 词）；❌【时序错置】"与本章前面『召唤树木仍来不及』"（该内容在引语**之后**）
- 原句 2 — ✅（引语 :134 逐字；"被识破而非被说服"、:137 伸臂"交割"均属实）
- 原句 3 — ❌【引语截短】分析论"结尾的排比"（good children, strong children…）不在引语内，原文紧接其后
- 原句 4 — ❓存疑【相邻引用】"that daughter of hers" 在引语前一句（断言本身可独立成立）
- 原句 5 — ❓存疑【相邻引用】"I don't remember it hurting that much." 在引语后三行
- 原句 6 — ✅（引语 :254 逐字；三段论与"紧跟在血统审判之后"属实）
- 原句 7 — ❓存疑【相邻引用】"you need to run" 在引语后一段（且被分析称为"收尾"）
- 原句 8 — ✅（引语 :362 逐字；"三句里两句让步"、:368 收据、:392 chores 玩笑均属实）

本章块数 8/8；报警 3；存疑 4（其中 3 条为同一模式）

### 发现明细

**ch10-1［报警·断言不实］ch10 ten.md:23 · 原句 1 —— "三句一处比一处短"与原文句长不符**

- md 逐字（:23）：「三句一处比一处短，句幅的收缩对应她从复述到收尾的语气，像在念一份事件报告」
- text 证据：`text/ch10_ten.txt:29` 三句逐字依序「But when I stepped through the gap in the wall, I was immediately beset by warriors, all armed with sword and axe, bronze tipped in iron.」/「There was no silver, or my wounds would be nearer by far to mortal.」/「They hurt me direly, but they could not kill me with what they brought to bear.」
- 计数：26 / 14 / 16 词（字符 137 / 67 / 79 同序）——末句比第二句**长**，"一处比一处短"不成立。
- 建议：改"前两句大幅收短、末句略回升"，或删该半句。

**ch10-2［报警·时序错置］ch10 ten.md:23 · 原句 1 —— "本章前面『召唤树木仍来不及』"实在其后**

- md 逐字（:23）：「与本章前面"召唤树木仍来不及"的无力感同构」
- text 证据：`text/ch10_ten.txt:35` 逐字「I had no time to retaliate, although I called for the trees as I was falling, and they answered.」；`:41` 逐字「But they didn't reach you in time.」——均在本块引语（:29）**之后**。
- 建议：改"紧接下文"或"本章后段"。

**ch10-3［报警·引语截短］ch10 ten.md:43 · 原句 3 —— 分析所论的"结尾排比"缺在引语外**

- md 逐字（:43 末）：「结尾的排比 good children, strong children, children with the blood of Titania 越念越顺——布道式的顺口，恰是这段话真正让人发凉的地方。」
- text 证据：引语止于 `text/ch10_ten.txt:146`「…not when Mother had decreed that the future must be allowed to pass unseen.”」，同段紧接其后逐字：「He will forget them in the light of the children they/we will have together, good children, strong children, children with the blood of Titania running bright through their veins, keeping them close to hearth and home.」
- 判据：分析把"结尾的排比"当作"这段话真正让人发凉的地方"来讨论，而该排比整句在引语之外——引语短于它所支撑的分析（本库高发模式：引语本身逐字正确、只是截短）。
- 建议：引语补全至段末（含 good children…keeping them close to hearth and home.）。

### 存疑（不混入确定缺陷）

**ch10-4［存疑·相邻引用·模式观察］原句 4 / 5 / 7 —— 分析层引用紧邻块外英文**

同章三块出现同一形态，先取证 3 条：
- 原句 4：md:53「记忆主人甚至拒绝用名字称呼 Raysel，只说 that daughter of hers。」——该短语在引语**前**一句（`ch10_ten.txt:167` 首句「She's hauling that daughter of hers, the one who should never have been possible…」；引语自第二句起）。断言本身在引语内亦可独立成立（引语全段未出现 Raysel 之名）。
- 原句 5：md:63「后脚 Acacia 补上一句 I don't remember it hurting that much.」——在 `ch10_ten.txt:188`；同句「前脚 Tybalt 把它当求救信号」对应 `:218`。
- 原句 7：md:83「她则用一句直截了当的祈使句收尾——全段请求的分量，就落在 you need to run 这句话上」——"you need to run" 在 `ch10_ten.txt:350`（引语后一段）。
- 说明：三者均属"分析引用紧邻引语之外的英文"，各断言可在引语内独立成立；块外引用属本库通行写法（`check_anchor` 口径：只在块外 ⚠️ 不判红）。**是否统一扩引语，请修复方定口径**。
- 另注：原句 7 处「一句直截了当的祈使句收尾」——"you need to run" 形式上为陈述句（you need + 动词原形），非祈使句句式；按功能口径（发出指令）可宽泛称呼"祈使句"，故不单列报警，建议改「一句直截了当的通牒」更稳。

**ch10-5［存疑·场景枚举］ch10 ten.md:13 · 导航 —— "屋内—林地—荒原—堡垒"的"屋内"**

- md 逐字：「场景沿屋内—林地—荒原—堡垒连续位移」
- text 证据：ch09 结尾 `text/ch09_nine.txt:509` 逐字「Acacia carried Luna out of the room and through the building, back to the skerry outside.」、`:510`「set Luna on the ground」；ch10 开篇至追猎离场均在同一屋外场域，全章未见室内场景。若以 `text/ch10_ten.txt:209`「the building where Luna was resting」为准勉强可通，故列为存疑。
- 建议：改"屋外/建筑旁"更稳。

（本章导航其余各项、一句话总结回核通过。）

---

## ch11 eleven（`ch11 eleven.md` ↔ `text/ch11_eleven.txt`）

### 逐块核对

- 原句 1 — ✅（引语 :17 逐字；章首整句大写、变猫—跳窗台—回头甩尾动作链均属实）
- 原句 2 — ✅（引语 :47 逐字；believed→knew 两重信任属实；:50「Not that I was particularly invested in trying.」确为其后紧接的句子）
- 原句 3 — ✅（说话人核对：:83 October「Yes, and…」半句被 Tybalt :86 截断，「读者听不到 October 的后半句、Tybalt 听懂了」属实；:89 她自认该半句正是"分头找"提议属实）
- 原句 4 — ❌【标点断言不实·低危】「分号把句子劈成两半」劈错位置（见明细）
- 原句 5 — ✅（引语 :182 逐字；I agreed 互证属实）；另 ❓存疑一处语法标签（见存疑）
- 原句 6 — ✅（引语 :302 逐字；三层递进、crush 三现、Raysel/Luna 词位错置均属实）
- 原句 7 — ❌【语法类别断言·低危】「句法全是简单句」与引语实况不符（见明细）
- 原句 8 — ✅（引语 :539 逐字；两处 Even those of us、称谓三级跳、:545「as a side effect」、:554 姓名与请求均属实）；另 ❓存疑一处术语（见存疑）

本章块数 8/8；报警 2；存疑 2

### 发现明细

**ch11-1［报警·标点断言不实·低危］ch11 eleven.md:53 · 原句 4 —— 「分号把句子劈成两半」劈错了地方**

- md 逐字（:53）：「分号把句子劈成两半：知道会被追 / 未必知道追的人是谁，if not who 这个插入让恐惧变了质」
- text 证据：`text/ch11_eleven.txt:149` 逐字「The people who'd taken Raysel had clearly known that they would be followed, if not who would be following them; their trail had been so straight and easily followed because they'd known that they were laying it.」——分号位于 following them 之后，其两半是「他们会知道被追踪（即便未必知道是谁）」/「路铺得笔直好跟」；而「知道会被追 / 未必知道追的人是谁」的对照由逗号 + if not who 插入承担（本句下文自亦称其为「插入」）。英文原文与本 md 中译（:49 用破折号处）该分隔均非分号。
- 建议：改「逗号插入 if not who 把第一半再劈开——被追是肯定的、追的人未必；分号则把"知情"与"铺路"对置」。
- （本块其余断言——身体/理智/推理的三步顺序、:152「下一段 It might not have been a trap…」引证——均核实属实。）

**ch11-2［报警·语法类别断言·低危］ch11 eleven.md:83 · 原句 7 —— 「句法全是简单句」不成立**

- md 逐字（:83 末）：「句法全是简单句加一个反问，写得越平，读着越疼」
- text 证据：`text/ch11_eleven.txt:386` 引语内至少两句含从属从句：「I used to wish she was my mother, not Amandine, so I could feel like someone loved me when I went to bed in the morning.」（宾语从句 + so 目的从句 + when 时间从句）；「And now she hates me, and when I have to be around her, all I want is to get away as quickly as I can.」（when 从句 + as…as 比较）——均非简单句（单一主谓、无从属从句）。
- 建议：改「句式平实、几乎不设修饰，最后收在一个反问上」，回避语法专名。

### 存疑（不混入确定缺陷）

**ch11-3［存疑·术语·低危］ch11 eleven.md:93 · 原句 8 —— 「our Lady 对 our savior，一组头韵短语」**

- md 逐字（:93）：「our Lady 对 our savior，一组头韵短语把 October 的两种可能人生摆上台面」
- text 证据：`text/ch11_eleven.txt:539` 逐字「who could have been our Lady, but chose to be our savior instead」——两短语共享的是同一个限定词 our（严格修辞口径应称平行/首语重复，本句前半段亦以「平行结构」描述 Even those of us），而 Lady 与 savior 的首辅音 l/s 并不相同；若取「同词 our 起首」的最宽口径，则勉强可通。
- 处置建议：宜改「一组平行短语（our Lady / our savior）」；是否改动请修复方定夺。

**ch11-4［存疑·语法标签·低危］ch11 eleven.md:63 · 原句 5 —— 「一个动词、一个宾语」**

- md 逐字（:63）：「一个动词、一个宾语，靠 by 与 from 两个介词把方向相反的两次绑架折叠进同一口气里」
- text 证据：`text/ch11_eleven.txt:182` 逐字「Rayseline has been abducted both by and then from her mother.」——被动句中 Rayseline 为表面主语；若按「abduct 的深层受事」的宽泛教学口径，亦可自圆，故不列报警。
- 处置建议：可改「一个动词、一个受事主语」更稳。

（本章导航回核：空堡骗局、:191–:194「被抱着跑过荒原」转场、:332 Luna「准备了房间却坚称没有告诉任何人」、:557–:566 Eutychia 请托，均属实；一句话总结回核通过。）

---

## ch12 twelve（`ch12 twelve.md` ↔ `text/ch12_twelve.txt`）

### 逐块核对

- 原句 1 — ✅（引语 :17 逐字，含章首大写"I THINK I'M GOING TO be sick"；破折号自嘲、两个进行时、:29 Tybalt 呕吐均属实）
- 原句 2 — ❌【数字断言·低危】「几百个人」与引语的一百五十八不符（见明细）；另 ❓存疑一处语法标签（见存疑）
- 原句 3 — ❌【结构断言与引语不符·低危】「被夹在两句以 And 起头的短句之间」（见明细）；另 ❓存疑一处表述（见存疑）
- 原句 4 — ✅（引语 :155 逐字；说话人 May；:149/:152 水疗日与"欠我一次"铺垫、:161 挂断时一阵大笑，均属实）
- 原句 5 — ✅（引语 :224 逐字；说话人 Athan；:200「a voice like stones rattling down the side of a hill」、:233 刷马节拍、:263「She finally begins to ask the right questions.」均属实）
- 原句 6 — ✅（引语 :272 逐字；:329 结尾的"仆役层"翻译链、Athan 耸肩、should 双句均属实）
- 原句 7 — ✅（引语 :341 逐字；:347 章末"牵起她的手，一起走回林中"、将来动词清单、"our child"均属实）

本章块数 7/7；报警 2；存疑 2

### 发现明细

**ch12-1［报警·数字断言·低危］ch12 twelve.md:33 · 原句 2 —— 「几百个人」与引语中的一百五十八不符**

- md 逐字（:33 末）：「用算术宣判几百个人的下场，是这个角色与本章共同的残酷语法」
- text 证据：`text/ch12_twelve.txt:62` 逐字「One hundred and fifty-eight kittens have vanished from my court since I grew old enough to become aware of the threat posed by Blind Michael. One hundred and fifty-eight Cait Sidhe from my court alone…which means most of them have long since stopped their dancing.」——两处同一数字、同指同一批人（本 md 同句亦称「同一个数字换一副名目」），为一百五十八；「算术」宣判的正是这一百五十八条性命的去向，非「几百」。
- 建议：改「用算术宣判这一百五十八条性命的下场」。

**ch12-2［报警·结构断言与引语不符·低危］ch12 twelve.md:43 · 原句 3 —— 「被夹在两句以 And 起头的短句之间」**

- md 逐字（:43）：「真正的表白 And I love you, too 被夹在两句以 And 起头的短句之间，故意不独立、不给排场」
- text 证据：`text/ch12_twelve.txt:71` 逐字「"Yeah, well, I would have said no if you'd only wanted to marry me because I did something stupidly heroic," I said. "And I love you, too. And I think … talking to Eutychia gave me an idea.」——表白句的前一句以 "Yeah, well" 起头（且为长句），其后一句才以 And 起头；上一段 Tybalt 的话（:68）亦无以 And 起头的句子。
- 建议：改「被夹在前后两句短句之间」并另述「与下一句同以 And 起头」，或径改「又被写成一句以 And 起头的短句，不给排场」。

### 存疑（不混入确定缺陷）

**ch12-3［存疑·语法标签·低危］ch12 twelve.md:33 · 原句 2 —— 「第一次的宾语是 kittens、第二次是 Cait Sidhe」**

- md 逐字（:33）：「第一次的宾语是 kittens、第二次是 Cait Sidhe——同一个数字换一副名目」
- text 证据：`text/ch12_twelve.txt:62`——「…kittens have vanished…」中 kittens 为**主语**；「…Cait Sidhe…tortured and transformed and finally wiped clean…」中 Cait Sidhe 亦为（省略被动式的）主语；称「宾语」无据，疑为「主语/搭配名词」之笔误（同类宽泛用法亦见于 ch11 eleven.md:63「一个宾语」）。
- 处置建议：改「第一次搭配的（主）名词是 kittens、第二次是 Cait Sidhe」。

**ch12-4［存疑·文字表述·低危］ch12 twelve.md:43 · 原句 3 —— 「她那快得同样的脑子」表述不通**

- md 逐字（:43）：「省略号在句法上模拟她那快得同样的脑子，感情刚交付，方案就上桌」
- 说明：疑为「转得同样快的脑子」一类笔误；原句 :71「And I think …」确有省略号，分析本意可读，仅措辞待校。
- 处置建议：修复方校订中文即可。

（本章导航回核：「身体反应—铃声—移动」三幕、"儿童逻辑"（:266）与 Neverland 比喻（:323）两处停步格言、Athan 谜语与捉迷藏规则、「她独行、他回家」分工（:335–:341）均属实；一句话总结回核通过。）

---

## 全书汇总（d3 范围：ch09–ch12）

- 覆盖：31/31 块全部逐块四查（ch09 8 + ch10 8 + ch11 8 + ch12 7）；引语逐字核对 31/31 全命中（展平子串法）。
- 报警合计 11：ch09 4 · ch10 3 · ch11 2 · ch12 2。
  - 模式一「硬事实松动」（5 条）：ch09-1 石墙、ch09-4「附近的储藏室」、ch10-1 句长计数、ch10-2 时序错置、ch12-1「几百个人」。
  - 模式二「语法/标点断言与原文不符」（3 条）：ch11-1 分号劈位、ch11-2「全是简单句」、ch12-2「两句以 And 起头」；同类更低危者已另列存疑（头韵、宾语标签等）。
  - 单发（3 条）：ch09-2 语义不对应、ch09-3 无出处断言、ch10-3 引语截短。
- 存疑合计 9：ch09 1 · ch10 4 · ch11 2 · ch12 2；集中于：相邻引用（块外英文，本库通行写法；ch10 一处 3 例）、语法/修辞术语宽松（头韵、宾语标签、「祈使句」「破折号插入语」「三段论」）、场景枚举（ch10 导航「屋内」）、文字表述（ch12「快得同样」）。
- 说话人核对：ch09–ch12 各对话体引语的说话人（Tybalt、Acacia、Luna、Eutychia、May、Athan 等）均与 text 上下文一致，未发现错配。
