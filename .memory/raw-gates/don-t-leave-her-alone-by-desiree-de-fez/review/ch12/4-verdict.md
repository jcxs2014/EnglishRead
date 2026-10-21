# ch12 人工审查 · R5 判定书

- 书：《Don't Leave Her Alone》（Desirée de Fez）· 第 12 章 · 审查员 DSH-Mac · 2026-10-21
- 真值：`text/ch12_chapter_12.txt`（15,022 字符 / 83 段）· 成品：`ch12 chapter 12.md`（115 行）
- 配套件：`1-suread.json`（R1 素读，23 events）／`2-machine.json`（R2 机器层）／`3-diff.md`（R3 三单 + R4 逐块）
- 边界：本轮**只出指令不改稿**；未改动任何 `ch*.md` / `00_*.md`；未 git add / commit / push。

---

## 一、报数（四组）

| 组 | 口径 | 结果 |
|---|---|---|
| **逐字** | md 中全部英文串（6 块引语 + 18 条例句 + 3 处行内片段）对原文逐字核对 | **27/27 命中，0 编造** |
| **对应** | 6 块 × 4 字段（24）＋ 导航 5 ＋ 一句话总结 1 = 30 个对应点 | **26 位置正确 / 4 位置错位**（4 条阻断）；正确位中 10 处措辞属提示 |
| **形态** | H1 形态、导航项数、子项集、块数、块长区间 vs books 基线 | **5/5 合格**（H1「12. Chapter 12」；导航 5 项；子项 [中文理解, 关键词, 为什么这样写, 读者视角提示]；块数 6；block_median 7.0 / range [5,8] 未偏离众数） |
| **断言** | 本判定表的断言条数 | **26 条 → 阻断 4 / 提示 12 / 假红 7 / 跳过 3** |

机器层（`bash scripts/chapter.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch12 chapter 12.md" --json`）：**退出码 0**，`"verdict": "ok"`；6 块引语逐字全 ok（`segment_miss=0, keyword_bad=0, cjk_low=0, struct_bad=0, quote_long=0, empty_quote=0`）。**退出码 0 只证明机器层无阻断，不等于人工审查通过**——本轮 4 条阻断全部落在机器层看不见的**导航/总结层**（本章型为重述+回忆插叙章，加权 S5）。

---

## 二、判定表（26 行）

| # | 断言 | 证据(章:区间) | 结论 | 档位 |
|---|---|---|---|---|
| 1 | L115「她要证明自己还记得，于是把童年连同营地一起一件件数给对方听」 | text/ch12_chapter_12.txt:[11586,11660)「I don’t want to forget you. There are lots of things I want to remember.」／[11663,11675)「Like what?」／[11732,11755)「My little freckled nose」／[11858,11913)「how Diana would blast El Último de la Fila in the cabin」／[12022,12064)「I don’t even want to forget the bad things」／[12277,12297)「That’s stupid stuff.」 | **施事/受事反转**：整段背诵是**女孩**说的（Alba 侧只有「I don’t want to forget you…」一句，并以「That’s stupid stuff.」收尾）；md 把它归给 Alba＝与原文相反 | **阻断** |
| 2 | L12「她把营地、家人、连难堪的小事都记得清清楚楚，对方却说她正在被遗忘」 | 同上三处 ＋ [3726,3805)「No. It’s because you’re forgetting yourself. The earrings are just the start.」／[11498,11583)「But you want to forget me, and if you forget me, I’ll just die. Like everyone else.」 | **记忆归属反转＋主动/被动反转**：记得的是女孩；女孩的指控是"你在忘记自己/你想忘记我"（**Alba 才是忘记方**，要被记住、会死的是女孩）。且与本文件 L11「她正在忘记自己」、块 5「**她说**连糟糕的事也不想忘」自相矛盾 | **阻断** |
| 3 | 块 5·为什么这样写 L65「去顶住**对方**那句「你在忘记自己」」 | [3726,3805)「No. It’s because you’re forgetting yourself. The earrings are just the start.」（说话人＝女孩） | **归属方向反转**：本块「她」＝引语说话人（女孩）⇒「对方」＝Alba，而该句是女孩自己说的；与同块中文理解「她说…」直接冲突 | **阻断** |
| 4 | L115「而对方要她做的恰恰是**别再想起**」 | [3521,3542)「So you would remember」／[11498,11583)「if you forget me, I’ll just die. Like everyone else.」／[12639,12686)「See, that’s because you’ve decided to forget us.」 | **要求方向反转**：女孩要的是"记住"（别再忘记），不是"别再想起"；与同句后半「那个一心要被记住的女孩」自相矛盾 | **阻断** |
| 5 | L11「浑身是血的她醒来」 | [843,867)「Her face was bloody, too」＋[700,780)「her face was a big, dark smudge」 | 只有**脸**血污，没有"浑身" | 提示 |
| 6 | L11「耳朵上多出九个银圈」 | [994,1034)「They appeared to be silver, but she wasn’t sure—everything was scabbed over, brown and black.」 | 原文是"**看上去**是银的，但也不确定"；md 块 1 中文理解保留了限定，导航层落成定论"银圈" | 提示 |
| 7 | L11「一边**蹲下来**给她做假指甲」 | [8596,8622)「She sat down on the ground」 | 原文是**坐下**（坐在地上） | 提示 |
| 8 | L15「（唱歌、**争耳环**、给对方做假指甲）」 | [4204,4233)「Alba didn’t have the reflexes to protect herself when the girl came over and ripped some of the earrings out of one of her ears.」＋「Then she kicked her in the side with one worn-out sneaker.」 | 女孩**单方强拆耳环＋踢**（Alba 无还手），不是"争" | 提示 |
| 9 | L13「这里没有索命的怨魂，**只**有一条退场规则」 | [11498,11583)「if you forget me, I’ll just die. Like everyone else.」＋[4204,4600) 拔环与踢 | 「被忘记即死」本身就是一条索命式因果；且章内女孩确有施暴，「只」字过满 | 提示 |
| 10 | L13 / L45「原型不再记得，替身就消失」 | [7360,7448)「Some vanished when their originals lost their memories **or their minds, or when they died**.」 | 原文规则有**三**个条件，md 只留一项，漏"心智丧失""原型死亡" | 提示 |
| 11 | L14「最后连**她需要被记住**这件事，也由别人替她执行了」 | [11498,11583)「But you want to forget me, and if you forget me, I’ll just die.」 | 「需要被记住」的是**女孩**；本段「她」一路指 Alba（Alba 才是正在忘记的人）⇒ 指代含混，归属方向存疑。同句「身体替我做了决定」方向正确 | 提示 |
| 12 | 块 3「最后一句偏偏用**两个**琐碎场合收尾」＋中文理解「正在**海里庆祝进球**」 | [7450,7581)「The end came for them when they were swimming in the ocean, celebrating a goal, putting on makeup in secret in the shared bathrooms.」 | 原文是**三项**并列；md 把前两项并成一项，并给"庆祝进球"加了"海里"这一原文没有的地点 | 提示 |
| 13 | 块 1·为什么这样写 L25/L27「一场…**手术**」「一次**诊疗记录**」 | [1074,1125)「The appointment she couldn’t remember must have been long, unhygienic, and cruel.」 | 原文是 appointment；md 中文理解已正确译作「预约」，分析层升级为"手术/诊疗记录"，重量超出原文 | 提示 |
| 14 | 插叙的三个年代量（**2005 / 十二岁 / 二十年**） | [4554,4592)「In 2005, the El Prat airport expansion」／[8101,8121)「Twelve-year-old Alba」／[8012,8039)「for twenty years after that」 | md 全文检索：`2005`=False、`二十`=False、`十二`=False ⇒ 三个量在**中文层全部缺席**（英文例句里仅有 "Twelve-year-old Alba"），插叙的年代坐标缺失 | 提示 |
| 15 | L12「不再是**怀疑自己的身体**」 | ch11:12「…A highway three fingers wide, bloody and viscous, was splitting her in two」／ch12:192「her body clamored for something different」 | 方向成立（ch11 确有身体恐怖自述），但"怀疑"偏心理化；原文是身体已不听她的 | 提示 |
| 16 | 女孩自陈"我正在消失"的三句未被任何引语块覆盖 | [4026,4046)「started to disappear」／[4142,4160)「barely anyone left」／[4166,4199)「I wish you had disappeared sooner」 | 6 块引语与 5 条导航均未收这条线（只有 L13 规则层的"替身就消失"）。属状态揭示而非情节转折，按口径不判阻断 | 提示 |
| 17 | 叙述者姓名/「妹妹」是否跨章搬运 | text/ch12:6「Alba came to in the dark, sprawled across the floor.」／ch05:549「She, on the other hand—who was six years older than Alba—did sometimes express her bewilderment.」／ch02:129「Only her older sister, Diana, insisted she go to a specialist…」 | **本章自证**：ch12 首句即点名 Alba；Alba 是妹妹、Diana 是姐姐（长六岁）有逐字支撑；md 未擅自译名。审查方怀疑不成立 | 假红 |
| 18 | 回忆插叙是否被写成"当下正在发生" | ch12 [4554,5411)/[5414,7220)/[7223,8221) 三段插叙；md L15「中间插入**三段历史叙述**（机场扩建、营地缓慢消失、替身的退场规则）」 | md 明确按历史层处理，未把 2005 往事写成此刻正在发生 | 假红 |
| 19 | 块 2「her perfect upturned nose」的 her 指代 | [1658,1690)「Seeing her perfect upturned nose gave Alba a pang of nostalgia.」＋「when an errant swing hit her face and knocked her bridge off center.」 | her＝**女孩**，Alba 随后想的是**自己**的鼻梁；md 中文理解「看到对方那个挺翘完美的鼻尖…她想起自己的鼻梁」处理正确 | 假红 |
| 20 | 块 5 的说话人（「她说连糟糕的事也不想忘」） | [11663,11675)「Like what?」／[12022,12064)「I don’t even want to forget the bad things」／[12277,12297)「That’s stupid stuff.」 | 说话人是**女孩**，md 块 5 中文理解正确；错在导航层（见 #1–#3） | 假红 |
| 21 | 「九个耳环＝五个＋四个」数字核对 | [913,992)「nine hoops in total, all different sizes, five in one ear and four in the other」／[3297,3302)「Nine.」 | md 块 1 中文理解「一共九个银圈…一只耳朵五个、另一只四个」与原文一致 | 假红 |
| 22 | 词汇例句是否逐字（18 条） | 见 3-diff.md R3 单子二 | **18/18 全部命中**原文 | 假红 |
| 23 | 词汇档位是否注水（常见词进 ⭐⭐⭐） | md「本章词汇」三档各 6 条 | ⭐⭐⭐ 六条（rhythmically / unhygienic / convulsions / sun-bleached / autonomous / unknowingly）均为原文用词；基础档（chorus / belly button / cartoon turtle / blond ponytail / breath / body）层级合理 | 假红 |
| 24 | 本章以外的章节内容与体裁判定 | ch02 / ch05 / ch11 / ch16 / ch17 | 超出本章审查范围，本轮仅按 md 的跨章断言取证（见 3-diff.md 附录） | 跳过 |
| 25 | 「全书查无」类断言 | md 全文 | md 未做任何"全书查无"式主张，本轮无需触发 R5-补的零命中自证 | 跳过 |
| 26 | 插叙中未被选用的次级质地（鬼魂住废弃房车、每周五打比奥、没水也照跳泳池、El Venao、Camela 卡带、El Último de la Fila 等） | [5414,7220)／[11858,11913) | 属 md 的体例取舍（6 块精选引语），非关键事件/转折缺失；仅其年代量缺口计入 #14 | 跳过 |

---

## 三、「阻断」级清单（4 条）

**均为总结层/分析层的施事与归属反转；引语块（6 块）本身无阻断。**

1. **断言**：L115「她要证明自己还记得，于是把童年连同营地一起一件件数给对方听」
   - **证据区间**：`text/ch12_chapter_12.txt:[11586,11660)`「I don’t want to forget you. There are lots of things I want to remember.」／`[11663,11675)`「Like what?」／`[11732,11755)`「My little freckled nose」／`[11858,11913)`「how Diana would blast El Último de la Fila in the cabin」／`[12022,12064)`「I don’t even want to forget the bad things」／`[12277,12297)`「That’s stupid stuff.」
   - **为什么阻断**：原文是**女孩**向 Alba 背诵童年（第一人称 "My"/"I"，且她身上正穿红泳衣与旧运动鞋），Alba 只有一句「I don’t want to forget you…」并以「That’s stupid stuff.」收尾。md 把「谁在证明自己还记得」整个调转＝**施事/受事反转**，与原文相反。

2. **断言**：L12「她把营地、家人、连难堪的小事都记得清清楚楚，对方却说她正在被遗忘」
   - **证据区间**：同上 ＋ `[3726,3805)`「No. It’s because you’re forgetting yourself. The earrings are just the start.」／`[11498,11583)`「But you want to forget me, and if you forget me, I’ll just die. Like everyone else.」
   - **为什么阻断**：两处都反——(a) 记得营地/家人/难堪小事的是**女孩**（Alba 正是那个在失去记忆的人）；(b) 女孩的指控是"**你在忘记自己**""**你想忘记我**"，即 Alba 是忘记方、女孩才是不被记住就会死的一方，md 写成"Alba 正在被遗忘"＝主动被动颠倒。**且与本文件 L11「一边数落她正在忘记自己」、块 5「她说连糟糕的事也不想忘」自相矛盾**，属可内部证伪的错。

3. **断言**：块 5·为什么这样写 L65「用一份「连坏事都记得」的清单，去顶住**对方**那句「你在忘记自己」」
   - **证据区间**：`text/ch12_chapter_12.txt:[3726,3805)`
   - **为什么阻断**：本块「她」＝引语说话人（女孩）⇒「对方」＝Alba；而「you're forgetting yourself」这句**是女孩自己说的**。md 把说话人安到 Alba 头上＝**归属方向反转**，与同块中文理解直接冲突。

4. **断言**：L115「而对方要她做的恰恰是**别再想起**」
   - **证据区间**：`text/ch12_chapter_12.txt:[3521,3542)`「So you would remember」／`[11498,11583)`「if you forget me, I’ll just die. Like everyone else.」／`[12639,12686)`「See, that’s because you’ve decided to forget us.」
   - **为什么阻断**：女孩要 Alba 做的是**记住**（别再忘记），md 写成"别再想起"＝**要求方向与原文相反**，且与同句后半「那个一心要被记住的女孩」自相矛盾。

> R5 硬约束自检：以上 4 条**均带原文逐字 + 字符区间**，无一条靠推断立论；4 条的更正方向均可在原文逐字上直接读出。

---

## 四、改稿指令（只出指令，本轮未执行）

1. `ch12 chapter 12.md` L115：把「她要证明自己还记得，于是把童年连同营地一起一件件数给对方听」改为**女孩背诵给 Alba 听**的方向（Alba 只有「I don't want to forget you. There are lots of things I want to remember.」与收尾「That's stupid stuff.」）；把「对方要她做的恰恰是别再想起」改为**"别再忘记／记住"**方向。
2. L12：把「她把营地、家人、连难堪的小事都记得清清楚楚」的主体改为**女孩**；把「对方却说她正在被遗忘」改为女孩的指控是"你在忘记自己／你想忘记我"（Alba 是忘记方）。
3. 块 5·为什么这样写（L65）：删去「顶住**对方**那句"你在忘记自己"」的归属错误，或改为"用这份清单去回答对方的'你正在忘记自己'"。
4. 提示级（可批量处理）：L11 的"浑身是血→脸血污"、"九个银圈→看上去是银的圈（她也不敢肯定）"、"蹲下来→坐在地上"；L15 的"争耳环→女孩把耳环拽下来"；L13 的规则三条件补全＋"只/没有索命的怨魂"收敛；L14 的"她需要被记住"明确指代；块 3 的"两个琐碎场合→三项"并去掉"海里庆祝进球"；块 1 的"手术/诊疗记录→预约"；补 2005／十二岁／二十年三个年代量。

---

## 五、已核实为正确

> R5.5：以下写法**看起来像错、核对后成立**，后续不得误改。

1. **叙述者姓名在本章自证**（非跨章搬运）——`text/ch12_chapter_12.txt:6`「Alba came to in the dark, sprawled across the floor.」
2. **「妹妹」关系成立**——`text/ch05_chapter_5.txt:549`「She, on the other hand—who was **six years older than Alba**—did sometimes express her bewilderment.」＋`text/ch02_chapter_2.txt:129`「Only her **older sister, Diana**, insisted she go to a specialist and sent her a dermatologist’s number several times.」＋`text/ch17_chapter_17.txt:96`「even with **six years between them**, they mimicked each other and somehow seemed like twins.」⇒ Diana 是姐姐（长六岁）、Alba 是妹妹；md 导航「全书视角转到妹妹的一章」成立。
3. **块 5「她和姐姐」成立**——`text/ch12_chapter_12.txt:[11678,12273)`「Diana and I were so scared we slept in the same bed for days」＋`text/ch05_chapter_5.txt:549` 同上 ⇒ 「姐姐」称呼正确。
4. **「Claire's＝饰品店、在商场里」成立**——`text/ch11_chapter_11.txt:126`「The store with the lights on was, in fact, **Claire’s**, where they sold cheap costume jewelry, trinkets, and accessories, mostly for kids and teenagers.」＋ch12 内 Claire's[13050] / escalator[13159] / mezzanine[13756] / bridge[13738] ⇒ md 的「商场的饰品店」可立。
5. **块 2「her」指女孩，md 处理正确**——`text/ch12_chapter_12.txt:[1658,1690)`「Seeing **her** perfect upturned nose gave Alba a pang of nostalgia.」＋「when an errant swing hit **her** face and knocked **her** bridge off center.」⇒ md「看到对方那个挺翘完美的鼻尖…她想起自己的鼻梁」无误。
6. **女孩的指控措辞与顺序未被 md 重排**——`text/ch12_chapter_12.txt:[3726,3805)`「No. It’s because you’re forgetting yourself. The earrings are just the start.」／`[3853,3894)`「The earrings. Camp La Tortuga Ligera. Me.」／`[11498,11583)`「But you want to forget me, and if you forget me, I’ll just die. Like everyone else.」／`[12639,12686)`「See, that’s because you’ve decided to forget us.」⇒ md 引用的「你在忘记自己」逐字无误，且未擅自调序。
7. **块 6 的受事与归属方向正确**——`text/ch12_chapter_12.txt:[14557,15022)`「They embraced her, stroked her hair, petted her, and then dragged her back over to Alba, who unknowingly devoured the girl as she slept.」＋`[14653,14665)`「Alba fainted」⇒ md「抱住她、顺着她的头发」「拖回那个昏过去的人身边」「她在睡梦中把女孩吃了下去，自己毫不知情」逐字方向正确。
8. **L11/L15 的现在时动作方向正确**——`[8596,8622)`「She sat down on the ground」＋`[4204,4233)` 女孩强拆耳环＋踢 ⇒ 「给她做假指甲」「她拖着女孩走」等受事方向无误（仅动词强度属提示）。
9. **「三个月营地」「商场里零星几分钟」成立**——`[7714,7738)`「three months of vacation」＋`[10774,10821)`「her only responsibility was to have a good time」＋`[9291,9326)`「sporadically, for minutes at a time」＋`[9331,9342)`「at the mall」⇒ md L14 对应无误。
10. **「被记得＝存在」的规则方向正确**——`[7360,7448)`「Some vanished when **their originals** lost their memories or their minds, or when they died.」⇒ 消失方＝替身、条件方＝原型，md「原型…替身就消失」方向无误（仅漏两个条件，见判定表 #10）。
11. **L11「她肚子里伸出的触手把女孩拖了回来」成立**——ch12 结尾区（触手自 Alba 腹部射出、女孩被拖回）＋`text/ch11_chapter_11.txt`「Seeing that her abdomen was swollen…」⇒ 触手归属 Alba、拖回对象＝女孩，方向正确。
12. **词汇 18 条例句逐字成立**（rhythmically / unhygienic / convulsions / sun-bleached / autonomous / unknowingly / clutching / makeshift / safekeeping / perpetual / worn-out / nostalgia / chorus / belly button / cartoon turtle / blond ponytail / breath / body）——18/18 命中 `text/ch12_chapter_12.txt`，逐字命中证明见 3-diff.md R3 单子二。
