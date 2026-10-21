# ch06 人工审查 · R3 三张单子（漏 / 编 / 错）＋ R4 逐块对应

审查员手记，**只出指令不改稿**。

## 0. 取证基线

| 项 | 值 |
|---|---|
| 原文（唯一真值） | `notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch06_chapter_6.txt`（285 行 / 12,508 字符 / 2,223 词；第 1 行是章号 `6`；正文段落各占一行：P2=`:6`、P3=`:9`、P4=`:12`、P5=`:15`、P6=`:21`，厨房对白=`:24`–`:87`，第一通电话=`:90`–`:168`，第二通电话=`:171`–`:285`） |
| 成品 | `notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch06 chapter 6.md`（129 行） |
| R1 素读 | `.memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/review/ch06/1-suread.json`（先于开 md 完成） |
| R2 机器层 | `.memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/review/ch06/2-machine.json`（`bash scripts/chapter.sh "…ch06 chapter 6.md" --json`，**退出码 0**） |
| 交叉件 | `text/ch05_chapter_5.txt`、`00_概述.md`、`00_情感节点.md` |

判级口径（沿用 `docs/rules/审查表.md` R3/R4/R5）：**阻断**＝与原文不符或缺失且落在 S1/S2/S3（含 §⑥ 施事·归属反转）；**提示**＝措辞正当但与原文有出入、不动摇事实成立；**假红**＝初判报警被原文证伪；**跳过**＝本轮未核。

---

## 1. 漏单子（素读有、md 无或未展开）

> 判级说明：本单**无一条判阻断**。理由见每行「判级理由」——md 的导航/人物弧线已覆盖这些场景的叙述，且引语块数 6 落在本书众数区间（`chapter.sh` 形态项：`block_median 7.0`、`block_range [5,8]`、本书 `profile novels`），不构成「形态偏离无理由」。

| # | 素读内容（原文逐字） | md 侧现状 | 判级 | 理由 |
|---|---|---|---|---|
| 漏-1 | 厨房整场褪黑素对白：`text/ch06_chapter_6.txt:24`「Maybe I’ll take Tomás’s melatonin tonight,” said Diana, sliding a frozen pizza into the oven.」／`:87`「Diana, you give these drops to your six-year-old son, who doesn’t even weigh fifty pounds. … tomorrow we’ll be back with your family.」 | 导航 `:11`「厨房里为一片褪黑素跟丈夫讨价还价」、情感弧线 `:12`「然后落到厨房那场关于一片褪黑素的拉锯」有概括，但**无任何引语块**；原句 1 读者提示 `:27`「还有她自己要吞下去的那片药」、原句 4 读者提示 `:63`「她要说服丈夫，自己可以吞下那片药」两处铺垫**始终没有兑现为引语块** | 提示 | 属 S2 家族的「引语覆盖不足＋读者提示承诺未兑现」；但 md 并非「无」，且块数在众数区间 ⇒ 不判阻断。建议增补一块 `ch06:87`（Carlos）可同时补上「六岁」「不到五十磅」两个数字 |
| 漏-2 | `text/ch06_chapter_6.txt:12`「There was absolutely no way to get him to sleep in his own bed. … he always went back to his parents’ bed. … They never got any rest … The psychologists hadn’t been much help with this, either.」（Tomás 夜里睡父母床、父母彻夜不睡、看心理医生无用） | md 完全未提 | 提示 | 是本章的处境设定，非本章转折；md 的夜戏线只取 Brisa 一侧。属可选补写（可并入漏-1 的厨房块一起解决） |
| 漏-3 | `text/ch06_chapter_6.txt:12`「The kids’ room was right next to theirs; they shared a wall, and her side of the bed was right up against it. Even so, she felt as if the two of them were on different floors of the building.」 | md 未提 | 提示 | 背景细节，不影响原句 3 的对应 |
| 漏-4 | `text/ch06_chapter_6.txt:21`「Brisa had thrown up on the taxi ride home, right around the Corte Inglés on Avinguda Diagonal」／「Three hours later, they had all showered and their clothes were going around in circles in 130-degree water.」 | md 未提 | 提示 | 场景细节（从 Alba 家回来的余波）；md 只写到「他们回家之后的那一夜」 |
| 漏-5 | `text/ch06_chapter_6.txt:9`「It usually took her three days to recover.」 | md 未提 | 提示 | 数字细节，可并入导航「推不掉的生日派对照样去」一句补写 |

---

## 2. 编单子（md 有、原文无）

| # | md 侧原文 | 原文侧 | 判级 | 理由 |
|---|---|---|---|---|
| 编-1 | `:14` 丈夫「逐条帮她数检查项（**插着的充电器**、拔掉的微波炉、睡前反复检查）」 | `text/ch06_chapter_6.txt:51`「Diana, that’s not going to happen. **You never leave anything charging.** You even unplug the microwave. And you check everything a thousand times before bed.」；全章 `charger` 零命中（取证见 `4-verdict.md` §3） | 提示 | 原文只有泛指「anything charging」，从未点名「充电器」；md 把泛指具体化成实物名词。三项清单与原文一一对应、语义等价，故按「措辞具体化」判提示而非阻断；若从严按「md 有、原文无」处置，可升为阻断 |

**本单无「编」级阻断项。**

---

## 3. 错单子（两边都有但不一致：主语 / 因果 / 数字 / 时序）

### 3.1 阻断级（4 条）

**错-1｜`md:11`「打给母亲那通」——第一通电话的方向被写反**

- md 侧（`:11`）：「收尾两通电话把这份恐惧分成两路——**打给母亲那通**，孩子在急诊待了五个小时……；**妹妹打来那通**，则把一夜惊吓归给了邪眼……」
- text 侧：
  - `text/ch06_chapter_6.txt:90`「**Diana’s iPhone lit up on the kitchen table.**」——手机亮屏＝来电，不是她拨出。
  - `text/ch06_chapter_6.txt:108`「**Who was it? Your mom or your sister?**」→ `:111`「**My mom.**」（Carlos 问的是「谁打来的」）
  - 对照第二通 `text/ch06_chapter_6.txt:171`「**She was getting a call.**」→ `:174`「**It’s me,** Alba said.」
- 结论：原文两通电话**都是打进来的**；第一通＝母亲打给 Diana，第二通＝Alba 打给 Diana。md 用「打给母亲那通／妹妹打来那通」这一对并列介词，把第一通断言成「Diana 主动打给母亲」，方向反转（§⑥ 施事/归属反转）。
- 最小修法：`:11`「打给母亲那通」→「母亲打来那通」（或中性「与母亲的那通」）。

**错-2｜`md:11`「说她是在替姐姐开脱」——把 Alba 写成 Diana 的姐姐**

- md 侧（`:11`）：「她一句「要紧的是孩子没事」当场被丈夫顶回，说她是在**替姐姐开脱**」
- text 侧：`text/ch06_chapter_6.txt:162`「Are you going to start making excuses for your **sister** now?」／`:168`「When you say things like that, you’re rationalizing it.」（说话人 Carlos）——被开脱的对象是 Alba。
- 关系方向证据：`text/ch05_chapter_5.txt:549`「She, on the other hand—who was **six years older than Alba**—did sometimes express her bewilderment. **She called her sister selfish**」⇒ Diana 大六岁＝长姐，Alba＝妹妹。
- 旁证（本书总览自身的口径）：`00_概述.md:74`「**阿尔巴 / Alba——妹妹，两个孩子的母亲。**」；`00_概述.md:68`「**戴安娜 / Diana——**自由撰稿人，**妻子的姐姐**、母亲。」；`00_概述.md:22` 与 `00_情感节点.md:55` 把 Carlos 的原话（`text/ch05_chapter_5.txt:513`「Your sister is never alone.」）译作「**你妹妹**从不独处」。
- 结论：md 的「姐姐」与原文 ch05/ch06 及本书总览三方证据冲突；且与 md 同一行前半「替**妹妹**查一下也做不到」自相矛盾。
- 最小修法：`:11`「替姐姐开脱」→「替妹妹开脱」。

**错-3｜`md:14`「走到当面说她「在替姐姐开脱」」——同源错误第 2 处**

- md 侧（`:14`）：「丈夫从逐条帮她数检查项（插着的充电器、拔掉的微波炉、睡前反复检查），走到当面说她「**在替姐姐开脱**」」
- text 侧／关系方向证据：同错-2（`text/ch06_chapter_6.txt:162`、`:168`；`text/ch05_chapter_5.txt:549`；`00_概述.md:74`）。
- 最小修法：`:14`「在替姐姐开脱」→「在替妹妹开脱」。

**错-4｜`md:13`「他们知道这是她跟母亲或**姐姐**说话时的调子」——同源错误第 3 处**

- md 侧（`:13`）：「连丈夫和两个孩子都习惯了不为她的大音量惊慌（电话那头近乎喊叫，这边谁都没有反应，他们知道这是她跟母亲或**姐姐**说话时的调子）」
- text 侧：`text/ch06_chapter_6.txt:93`「All of them knew that this was the tone Diana used when she was talking with her mother or **her sister**.」——「her sister」＝Alba＝妹妹。
- 结论：同错-2；同句前半「他们知道这是**她**…的调子」（tone 归属＝Diana 本人）经核对**正确**，错在关系方向词。
- 最小修法：`:13`「跟母亲或姐姐说话」→「跟母亲或妹妹说话」。

### 3.2 提示级（7 条）

| # | md 侧原文 | 原文侧 | 判级理由 |
|---|---|---|---|
| 错-5 | `:14`「插着的**充电器**」 | `text/ch06_chapter_6.txt:51`「You never leave anything charging.」；全章 `charger` 零命中 | 泛指被具体化成实物名词，语义等价，见编-1 |
| 错-6 | `:15`「两个人又都拒绝再往下查——一个**不肯回应那五个小时**，一个不肯自己去搜」 | `text/ch06_chapter_6.txt:120`「At urgent care? At nine p.m.? They’ve been at urgent care with all three kids for five hours?」→ `:123`「**Yeah, they just got out.**」 | 她字面上**回应了**；md 想说的应是「不肯接 Carlos 对延误/丈夫失职的指责」（`:132`–`:144`）。建议改为「一个不肯接丈夫对那五个小时的抱怨」 |
| 错-7 | `:12`「孩子**一律**套上**反光外套**」 | `text/ch06_chapter_6.txt:9`「On the few occasions when they had no excuse, Diana would dress Brisa and Tomás in **reflective hoodies**」 | ①hoodie＝连帽衫/卫衣，非外套；②「一律」与原文「仅在没有推不掉的理由的那几次」不符 |
| 错-8 | `:13`「从母亲讲起的那桩**旧事**传到姐妹俩手上」 | `text/ch06_chapter_6.txt:219`「She said the mediums came up to you **yesterday** at Finestrelles?」；`text/ch05_chapter_5.txt:336`「some old women went up to her **yesterday** at Finestrelles」 | 灵媒一事发生在「昨天」，不是「旧事」 |
| 错-9 | `:11` 同句内「**母亲**白天怕孩子在公园、在学校出事」＋「打给**母亲**那通」 | `text/ch06_chapter_6.txt:6`（Diana＝孩子的母亲）、`:111`「My mom.」（Diana 的母亲＝Carmen） | 一句之内「母亲」兼指 Diana 与 Diana 的母亲，一词二义，读者易把两通电话的对象混成同一人。建议首处改「当妈妈的她」，或后处改「她母亲」 |
| 错-10 | `:129`「**这个家里**有两个人急着把惊吓收尾」 | `text/ch06_chapter_6.txt:171`–`:180`（Alba 与丈夫 Juan、孩子在急诊/回家路上，不在这个家里） | 「这个家里」指代不准（Alba 不是这个家的成员）。建议改「这两个人」或「这一夜里有两个人」 |
| 错-11 | `:73`「作者还顺手让这通电话差点烤焦了自家那份披萨：**丈夫的一声抱怨**，把急诊室里的五个小时和厨房里的晚饭接在了同一处」 | `text/ch06_chapter_6.txt:99`「**“Well, this almost burned thanks to you,” she said**, crouching to check on the pizza.」（说披萨快烤焦的是 **Diana**，不是丈夫）；「丈夫的抱怨」＝ `:120`／`:132`／`:144` 对急诊五个小时的抱怨 | 第二半句为真（Carlos 在厨房里抱怨五个小时，把急诊与晚饭并置）；但冒号让读者把「烤焦」的因由挂到「丈夫的一声抱怨」上，而那句抱怨出自 Diana。建议拆成两句：「……差点烤焦了自家那份披萨（她进办公室前把烤箱丢给了丈夫）：Carlos 在厨房里对那五个小时的抱怨，又把急诊室和晚饭接在了同一处。」 |

---

## 4. R4 逐块对应（6 块；人判）

判据：只看每块的中文分析是否在讲**这句引语**；固定三问＝①每个动词的主语是谁 ②受事/宾语是谁 ③「谁的/谁欠谁/谁问的」回原文看 by/to/from/of 决定方向。

| 块 | md 行 | 引语出处 | 中文分析是否在讲这句引语 | 三问 |
|---|---|---|---|---|
| 1 | `:19`–`:27` | `text/ch06_chapter_6.txt:6`（She couldn’t wrap… / Her blood went cold…） | **是**。`:21` 中文理解逐句对得上；`:25` 的 simulacrum＝原文「a fenced-in, miniature depiction」；`:27` 读者提示是前瞻（允许）。**注**：`:21` 首句「她始终活在一种恐惧里……随着压力陡增而加剧」取自引语**之前**的同段句（`:6`「Diana lived in terror…」「coinciding with a spike in stress」）⇒ 引语截短（S2 家族），但主体分析仍落在引语上 ⇒ 提示级，不判阻断 | ①主语 She／Her＝Diana ✓；②受事 children、the park ✓；③simulacrum 归属＝公园那座「an angry, hostile society」的缩小复制品（belonging to the park）✓ 方向正确 |
| 2 | `:31`–`:39` | `text/ch06_chapter_6.txt:9`（Before, the hypothetical tragedies…） | **是**。`:33` 对应引语三句；`:37` 的「几乎全是家里的→也→学校」并置分析对应原文 `almost exclusively domestic → also took place at the school → kidnappings`；`:39` 对应同段紧接的「She had told Carlos that lately she’d been feeling more afraid. But she didn’t mention the visions; she never had.」✓ | ①主语 the hypothetical tragedies ✓；②受事 her children ✓；③they＝她的孩子（被错交给别人）✓ 方向正确；md 未把叙述者「幻象」误当事实 ✓ |
| 3 | `:43`–`:51` | `text/ch06_chapter_6.txt:12`（mushroom-shaped lamp…） | **是**。`:45`「像梦游的探险者那样走近女儿，再小心翼翼地把光洒在她身上，直到能看清她的胸口或后背正有节奏地起伏」逐动作对得上；`:49` 分析有「为什么」（比喻的双关）✓ | ①主语 she＝Diana ✓；②受事 Brisa ✓；③「cast **her** with light」的 her＝Brisa（`:45`「把光洒在**她**身上」「直到能看清**她**的胸口或后背」指 Brisa，未与 Diana 混）✓ |
| 4 | `:55`–`:63` | `text/ch06_chapter_6.txt:15`（sprawled… trapped between the wheels… as if the toy had run her over…） | **是**。`:57`「四仰八叉地躺在房间尽头的地上，卡在洋娃娃推车的轮子之间，好像那件玩具趁她睡着时把她碾过去」对应引语；`:61` 的「母亲的眼睛自动补出了被碾过去的画面」正是原文 `as if` 的来源 ✓ | ①主语 She'd found＝Diana ✓；②受事 Brisa ✓；③as if 的施事＝stroller（玩具）、受事＝Brisa ✓ 方向正确 |
| 5 | `:67`–`:75` | `text/ch06_chapter_6.txt:147`（Well, the important thing is, the baby is fine…） | **是**。`:69`「要紧的是孩子没事／做了 X 光／等出院手续／把披萨端出来」对应引语；`:73` 的「三件手续性事实」「漏掉了时间、漏掉了在场的人数」对应这句里只有 the baby、没有三个孩子也没有五小时（五小时是 Carlos 在 `:120` 说的）✓；`:75` 对应 `:156`「You really think that’s the important thing—that the baby is OK?」✓ | ①主语＝说话人 Diana ✓（`:147`「Diana answered while she took out the pizza」）；②受事 the baby ✓；③**归属方向错在这里**：紧接的 `:162`「Are you going to start making excuses for your sister now?」＝替 **Alba（妹妹）** 开脱 ⇒ md:11／:14 的「替姐姐开脱」判阻断（错-2、错-3） |
| 6 | `:79`–`:87` | `text/ch06_chapter_6.txt:180`（Yes, we’re on our way home now… get rid of an evil eye?） | **是**。`:81`「对方先答：是啊，我们已经在回家的路上了；信号不好是因为我们在过隧道。然后她忽然问：你知道怎么解邪眼吗？」对应引语三句 ✓；`:85` 的三级跳分析对应原文三句结构 ✓；`:87` 的前瞻对应 `:186`/`:216`/`:219`/`:267`/`:276`/`:285` ✓ | ①主语＝Alba（`:174`「It’s me,” Alba said.」）✓；②受事 the evil eye ✓；③提问者＝Alba 问 Diana（`:81`「然后**她**忽然问」指 Alba）✓ 方向正确，未反转。**附带核实**：`:87`「妹妹一再说自己看得很清楚」经轮次核对成立——第二通电话以 `:249`「I don’t know, **Alba**. Let me think of someone who knows about this stuff.」与 `:285`「No, **Alba**. It’s late.」两句锚定「奇数轮＝Alba、偶数轮＝Diana」，故 `:270`「No. I didn’t. It was very clear what was happening.」出自 Alba＝妹妹 ✓ |

**逐块结论：6/6 块的中文分析都在讲本块引语；0 处「讲引语之外的上下文」、0 处「只复述字面而无为什么」、0 处施事反转**（唯一方向错发生在块 5 的**后文**引用——即 Carlos 那句 `your sister`——已计入错-2／错-3）。

---

## 5. R4 汇总

- 逐块对应：**6/6 通过**（2 处提示级：块 1 引语截短、块 3/块 4 的读者提示前瞻）。
- 固定三问：**18 问**（6 块 × 3 问）全部回原文核过；主语 6/6 正确、受事 6/6 正确、归属方向 5/6 正确（块 5 的 Carlos「your sister」→ 妹妹，md 写「姐姐」）。
- 本轮不产生新的 S2（选引语）阻断：6 条引语均为本章原文整句、无 `…` 缝合、无跨话轮拼接、无一行塞多句（机器层 `quotes` 6/6 ok:true，另用 Python 逐条 `count` 复核均命中 1 次）。
