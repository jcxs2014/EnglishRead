# ch12 人工审查 · R3 三张单子 + R4 逐块对应

- 书：《Don't Leave Her Alone》（Desirée de Fez）· 第 12 章 · 审查员 DSH-Mac · 2026-10-21
- 真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch12_chapter_12.txt`（15,022 字符 / 83 段 / Alba 视角）
- 成品：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch12 chapter 12.md`（115 行）
- 本轮口径：**只出指令不改稿**——未改动任何 `ch*.md` / `00_*.md`，未 git add / commit / push。
- 过程件：R1 `1-suread.json`（23 条 events，含字符区间）／R2 `2-machine.json`（chapter.sh EXIT=0）
- 本章型：**重述 + 回忆插叙章** ⇒ 加权 S1（素读原文）＋ S5（总结与总览层）。故本轮把「总结层／导航层」当成主要打靶面：**4 条阻断全部落在导航层与总览层，不在 6 个引语块内**。

---

## R3 单子一：漏（原文有、md 缺）

| # | 漏项 | md 侧 | text 侧（逐字 + 区间） | 档位 |
|---|---|---|---|---|
| 漏-1 | **2005 年**（El Prat 机场扩建那一年） | 全文检索 `2005` → False | [4554,4592)「In 2005, the El Prat airport expansion」 | 提示 |
| 漏-2 | **二十年** | 全文检索 `二十` → False | [8012,8039)「for twenty years after that」 | 提示 |
| 漏-3 | **十二岁**（中文层） | 中文层无「十二」；仅 L67「十几岁以前」；英文例句里有 "Twelve-year-old Alba" | [8101,8121)「Twelve-year-old Alba」 | 提示 |
| 漏-4 | 女孩**自陈正在消失**的三句（本章的情感赌注） | 6 个引语块与 5 条导航均未出现「我在消失／没剩几个人了／我希望你早就消失」；只有 L13 的规则层「替身就消失」 | [4026,4046)「started to disappear」／[4142,4160)「barely anyone left」／[4166,4199)「I wish you had disappeared sooner」 | 提示（状态揭示非情节转折，不判阻断） |
| 漏-5 | 插叙第二段（营地慢死）的质地：鬼魂住废弃房车、每周五打比奥、没水也照跳泳池、跳 El Venao | L15 只压成「营地缓慢消失」六字 | [5414,7220) | 提示（密度缺口，与漏-1/2/3 同一根因） |

**不判阻断的理由**：本章 md 是「6 块精选引语 + 总结层」体例，md 未写明取舍理由，但 6/N 的精选本身是体例常态；漏-1~5 没有一项是**关键事件或转折**缺失（本章的关键转折＝耳环九只、女孩登场、拔环与踢、触手结尾，md 全覆盖）。按审查表「漏＝关键事件/转折未出现→阻断，除非 md 写明取舍理由」的口径，只记提示。**唯一可能升级为阻断的是本轮 4 条错位（见单子三），它们不依赖取舍。**

---

## R3 单子二：编（md 有、原文无）

**0 条。** 核验范围与结果：

- md 中全部英文串逐字核对：**27/27 命中**原文（6 块引语 + 18 条例句 + 3 处行内片段 `“I remember the sign at the entrance, the cartoon turtle.”` / `“That’s the chorus. It doesn’t count.”` / `“Wait a sec,”`）。
- 机器层 `segment_miss=0 / keyword_bad=0 / cjk_low=0 / struct_bad=0 / quote_long=0 / empty_quote=0`。
- 无凭空造词、无造句、无造数字。md 出现的所有量（九只耳环、五个＋四个、三个月、十二岁〔仅英文例句〕、两个时间层、三段历史叙述）均能在原文找到对应。

---

## R3 单子三：错（两边都有、不一致）

**本轮全部 4 条阻断都在这里，且同属一个病根：把「女孩背诵童年给 Alba 听」读成了「Alba 背诵童年给女孩听」。**

### 错-1（阻断）一句话总结 L115 · 背诵归属反转

- md 侧：「她要证明自己还记得，于是把童年连同营地一起一件件数给对方听」
- text 侧（逐字，[11663,11675) 起）：
  - [11586,11660)「I don’t want to forget you. There are lots of things I want to remember.」← **Alba**
  - [11663,11675)「Like what?」← **女孩问**
  - [11732,11755)「My little freckled nose」／[11858,11913)「how Diana would blast El Último de la Fila in the cabin」／[12022,12064)「I don’t even want to forget the bad things」← **女孩在背诵**（第一人称「My」「I」；且她身上正穿着红泳衣与那双旧运动鞋）
  - [12277,12297)「That’s stupid stuff.」← **Alba 收尾**
- 判定：**施事/受事反转**。原文＝女孩背诵、Alba 听着并贬一句；md＝Alba 背诵、女孩听着。与原文相反。

### 错-2（阻断）导航·情感弧线 L12 · 记忆归属 + 主动/被动双重反转

- md 侧：「她把营地、家人、连难堪的小事都记得清清楚楚，对方却说她正在被遗忘」
- text 侧：
  - 记得这些的是**女孩**（错-1 的逐字区间），不是 Alba；
  - 女孩的指控原文是 [3726,3805)「No. It’s because you’re forgetting yourself. The earrings are just the start.」与 [11498,11583)「But you want to forget me, and if you forget me, I’ll just die. Like everyone else.」——即 **Alba 是忘记方**；要被记住、会死的是**女孩**。
- 判定：md 写成「Alba 记得清清楚楚 ＋ 女孩说 Alba 被遗忘」，两半都反了。**并且与本文件自相矛盾**：L11 写「一边数落她正在忘记自己」（方向正确），块 5 中文理解写「**她说**连糟糕的事也不想忘」（说话人正确）——错的是导航层。

### 错-3（阻断）块 5·为什么这样写 L65 · 指控归属反转

- md 侧：「用一份「连坏事都记得」的清单，去顶住**对方**那句「你在忘记自己」」
- text 侧：[3726,3805)「No. It’s because you’re forgetting yourself. The earrings are just the start.」——说话人＝**女孩自己**。
- 判定：本块「她」＝引语说话人（女孩）⇒「对方」＝Alba；于是 md 把女孩自己说的指控安到 Alba 头上。**归属方向反转**，与同块中文理解「她说……」直接冲突。

### 错-4（阻断）一句话总结 L115 · 要求方向反转

- md 侧：「而对方要她做的恰恰是**别再想起**」
- text 侧：[3521,3542)「So you would remember」／[11498,11583)「if you forget me, I’ll just die. Like everyone else.」／[12639,12686)「See, that’s because you’ve decided to forget us.」
- 判定：女孩要 Alba 做的是**记住**（别再忘记），不是「别再想起」。**与原文相反**，且与同句后半「那个一心要被记住的女孩」**自相矛盾**。

### 错-5（提示）其余不一致，逐条（详见 4-verdict.md 判定表）

| 项 | md 侧 | text 侧 | 档位 |
|---|---|---|---|
| L11 | 「浑身是血的她醒来」 | [843,867)「Her face was bloody, too」＋脸上「a big, dark smudge」——只有脸 | 提示 |
| L11 | 「耳朵上多出九个银圈」 | [994,1034)「They appeared to be silver, but she wasn’t sure」——"看上去是银的，但也不确定" | 提示 |
| L11 | 「蹲下来给她做假指甲」 | [8596,8622)「She sat down on the ground」——坐下 | 提示 |
| L15 | 「（唱歌、**争耳环**、给对方做假指甲）」 | [4204,4233)+「ripped some of the earrings out of one of her ears… Then she kicked her in the side with one worn-out sneaker.」——单方强拆＋踢，无争夺 | 提示 |
| L13 | 「只（有一条退场规则）」＋「没有索命的怨魂」 | [7360,7448)「Some vanished when their originals lost their memories or their minds, or when they died.」（三条件）；[11498,11583)「if you forget me, I’ll just die」＝「被忘记即死」，本身是索命式因果 | 提示 |
| L13 / L45 | 「原型不再记得，替身就消失」 | 同上：漏「心智丧失」「原型死亡」两条件 | 提示 |
| L14 | 「最后连**她需要被记住**这件事，也由别人替她执行了」 | 「需要被记住」的是女孩（[11498,11583)）；本段「她」一路指 Alba（Alba 才是那个正在忘记的人）⇒ 指代含混 | 提示 |
| 块 3 | 「最后一句偏偏用**两个**琐碎场合收尾」＋中文理解「正在**海里庆祝进球**」 | [7450,7581)「The end came for them when they were swimming in the ocean, celebrating a goal, putting on makeup in secret in the shared bathrooms.」——三项并列；md 把前两项并成一项并给"庆祝进球"加了"海里"这一原文没有的地点 | 提示 |
| 块 1 | 「一场…**手术**」「一次**诊疗记录**」 | [1074,1125)「The appointment she couldn’t remember must have been long, unhygienic, and cruel.」——原文是 appointment；md 中文理解已正确译作「预约」，分析层升级为"手术/诊疗记录" | 提示 |
| L12 | 「不再是**怀疑自己的身体**」 | 方向成立（ch11 身体恐怖自述在），但性质偏心理化；原文是身体已不听她的（ch12「her body clamored for something different」；ch11「A highway three fingers wide…was splitting her in two」） | 提示 |

---

## R4 逐块对应（每块四字段 + 固定三问）

**固定三问**：① 每个动词的主语是谁 ② 受事/宾语是谁 ③「谁的 / 谁欠谁 / 谁问的」归属方向。

### 块 1（L19 引语）— 醒来：脸、九只耳环、不记得的预约

- 引语区间：ch12 [0,1125)（P1–P2）
- 中文理解：对应 ✓（「她的脸也是血糊糊的」「一共九个银圈…一只耳朵五个、另一只四个」「结痂把一切都盖成褐色和黑色」「那场她怎么也想不起来的「预约」」）
- 关键词：对应 ✓（血/耳环/银/结痂/预约 全部落在本块引语内）
- 为什么这样写：对应 ✓（把恐怖写成一张收据＝数目＋状态＋诊断，正是本块三段）
- 读者视角提示：对应 ✓（「预约」＝把耳环从饰品变诊疗记录，正是本块末句）
- ① 主语：Alba（[7,31)「Alba came to in the dark」）✓
- ② 受事：九只耳环（[913,992)）／不记得的那场预约（[1074,1125)）✓
- ③ 归属：「The **appointment she** couldn’t remember」＝属于 Alba 的预约 → md「那场她怎么也想不起来的「预约」」✓ 正确
- 判定：**通过**（措辞提示 2 条：L11 的「浑身是血」「九个银圈」；块 1 分析层「手术/诊疗记录」）

### 块 2（L29 引语）— 完美上翘的鼻尖与自己被秋千打歪的鼻梁

- 引语区间：ch12 [1658,1783)（P6）
- 中文理解：对应 ✓；**her 的指代处理正确**（原文 her＝女孩，Alba 随后想的是自己的鼻梁 → md「看到**对方**那个挺翘完美的鼻尖」「她想起**自己的**鼻梁」）
- 关键词：对应 ✓（鼻尖/鼻梁/秋千/公园/习惯）
- 为什么这样写：对应 ✓（把营地消失刻进一张脸；「习惯了不再完美」＝原文 "she'd gotten used to"）
- 读者视角提示：对应 ✓（时间点＝营地关门前后，身体替她记着）
- ① 主语：Alba（"She thought about how **she'd** lost it"）✓
- ② 受事：她自己的鼻梁（"an errant swing hit **her** face and knocked **her** bridge off center"）✓
- ③ 归属：her perfect upturned nose ＝**女孩**的鼻尖 → md「对方」✓
- 判定：**通过**

### 块 3（L39 引语）— 替身的退场规则

- 引语区间：ch12 [7223,8221)（P55，含规则句 [7360,7581)）
- 中文理解：对应 ✓（「有的在「原型」失去记忆或心智时跟着散了」方向正确：消失方＝替身，条件方＝原型）
- 关键词：对应 ✓（原型/替身/消失/心智/浴室）
- 为什么这样写：对应 ✓（把超自然事件写成可核对规则——规则句确在本块引语内）
- 读者视角提示：对应 ✓（「被记得＝存在」＝本块规则的核心）
- ① 主语："the ghosts of La Tortuga" / "Some" ✓
- ② 受事："their **originals**"＝条件方 ✓
- ③ 归属：「The end came for **them**」＝them＝替身 → md「替身就退场」✓
- 判定：**通过**（措辞提示 2 条：规则表述漏两条件；"两个琐碎场合"＋"在海里庆祝进球"）

### 块 4（L49 引语）— 营地＝最后的自由；商场＝如今零星的几分钟

- 引语区间：ch12 [9268,9420)（P59）
- 中文理解：对应 ✓（「她在营地的记忆里躲得太久，只因为那是她最后一次彻底自在、轻松、不依赖任何人的地方」「零星地出现在商场里，一次不过几分钟」）
- 关键词：对应 ✓（自由/营地/记忆/商场/几分钟）
- 为什么这样写：对应 ✓（「躲进去」＝原文 "taken refuge"；「按理说商场是花钱的地方」是本块 "The only place she'd experienced anything similar since then" 的合理读法）
- 读者视角提示：对应 ✓（「记住『在商场里』这四个字，结尾会绕回它」——本章末尾确在商场内）
- ① 主语：she＝Alba ✓
- ② 受事：地点 the mall ✓；"anything similar"＝类似的片刻 ✓
- ③ 归属：「在商场里」＝Alba 的自由来源 ✓
- 判定：**通过**

### 块 5（L59 引语）— 女孩背诵童年（Mom 晕倒／与 Diana 同床／肚脐被安全别针戳破）

- 引语区间：ch12 [12022,12300)（P67 末段 + Alba 收尾）
- 中文理解：对应 ✓，**说话人正确**（「**她说**连糟糕的事也不想忘」＝女孩说的）
- 关键词：对应 ✓（糟糕的事/妈妈/晕倒/同床/肚脐/安全别针/冰块）
- 为什么这样写：**✗ 错位**——「用一份「连坏事都记得」的清单，去顶住**对方**那句「你在忘记自己」」把女孩自己说的指控（[3726,3805)）安到 Alba 头上 → 见 R3 错-3
- 读者视角提示：对应 ✓（「她一件件数的全是十几岁以前的事」）
- ① 主语：背诵者＝**女孩**（"My little freckled nose"／"Diana and I"／她正穿着红泳衣与旧运动鞋）✓ md 的中文理解对，**分析层错**
- ② 受事：「连坏事都记得」的清单 ✓
- ③ 归属：「你在忘记自己」的说话人＝**女孩**；md 写成「对方」（=Alba）⇒ **归属方向反转**
- 判定：**1 处阻断**（R3 错-3）+ 1 条提示（「她们共睡」称"姐姐"的跨章取证已核实正确）

### 块 6（L69 引语）— 触手：抱住、顺毛、拖回，Alba 睡梦中吞掉女孩

- 引语区间：ch12 [14557,15022)（P83）
- 中文理解：对应 ✓（「触手朝女孩的身体展开扑过去」「抱住她、顺着她的头发、拍着她」「又把她拖回那个昏过去的人身边」「而她在睡梦中把女孩吃了下去，自己毫不知情」）
- 关键词：对应 ✓（触手/栏杆/拖回/睡梦/吞吃）
- 为什么这样写：对应 ✓（「护着与吞吃写成同一串动作」＝embraced/stroked/petted → dragged → devoured）
- 读者视角提示：对应 ✓（「她全程昏着，清醒的是那具不承认她的身体」＝[14653,14665)「Alba fainted」）
- ① 主语：They＝触手（Alba 体内的）✓
- ② 受事：the girl ✓（"embraced her, stroked her hair" 的 her＝女孩）
- ③ 归属：「dragged her back **over to Alba**, who unknowingly devoured the girl as she slept」＝女孩被拖回 Alba 身上、Alba 昏睡中吞吃 ✓ md 方向正确
- 判定：**通过**

### R4 汇总

- 6 块 × 4 字段 = **24 个块内对应点**：23 点在讲本块引语，1 点错位（块 5·为什么这样写，L65）→ 阻断。
- 导航 5 条（L11–L15）＋一句话总结（L115）= **6 个总结层对应点**：L11 对（含 2 措辞提示）、L12 **错位**（阻断）、L13 对（含 2 措辞提示）、L14 对（含 1 措辞提示）、L15 对（含 1 措辞提示）、L115 **两处错位**（阻断 ×2）。
- 三问结论：6 块内部的施受与归属全部正确；**错位只发生在总结层对「谁在背诵／谁在指控」这一组归属的再叙述上**。

---

## 附：本轮取证命令（全部 `/usr/bin/grep` 显式路径；`text/` 被 .gitignore，`git grep` 不可用）

```
$ /usr/bin/grep -cw "Diana" text/*.txt
text/ch00_prologue.txt:0 … text/ch05_chapter_5.txt:58 … text/ch12_chapter_12.txt:2 … text/ch17_chapter_17.txt:27
exit=0

$ /usr/bin/grep -cwn "sister" text/*.txt
text/ch02_chapter_2.txt:2 … text/ch12_chapter_12.txt:1 … text/ch17_chapter_17.txt:4
exit=0

$ /usr/bin/grep -n "older sister, Diana" text/ch02_chapter_2.txt
129:…Only her older sister, Diana, insisted she go to a specialist and sent her a dermatologist’s number several times.
exit=0

$ /usr/bin/grep -n "six years older than Alba" text/ch05_chapter_5.txt
549:…She, on the other hand—who was six years older than Alba—did sometimes express her bewilderment.
exit=0

$ /usr/bin/grep -n "six years between them" text/ch17_chapter_17.txt
96:…Still, when they were together, even with six years between them, they mimicked each other and somehow seemed like twins.
exit=0

$ /usr/bin/grep -n "Claire’s, where they sold" text/ch11_chapter_11.txt
126:Alba knew that song. … The store with the lights on was, in fact, Claire’s, where they sold cheap costume jewelry, trinkets, and accessories, mostly for kids and teenagers.
exit=0

$ /usr/bin/grep -n "Alba came to in the dark" text/ch12_chapter_12.txt
6:Alba came to in the dark, sprawled across the floor. …
exit=0
```

**本轮无「全书查无」类断言**（md 未做此类主张），故 R5-补的「零命中自证」条款本轮无需触发；上表所有取证命令退出码均为 0（真命中），无一条靠「查无」立论。
