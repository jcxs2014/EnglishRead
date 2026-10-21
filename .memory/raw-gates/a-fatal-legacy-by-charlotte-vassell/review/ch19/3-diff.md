# 3-diff · ch19《A Fatal Legacy》三张单子（漏 / 编 / 错）

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch19 the post office box leads to harrogate.md`
> 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch19_19.txt`（4,783 字符，156 行）
> 铁律遵守：**R1 素读已完成并落盘**（`1-suread.json`）后才开 md；本文件写作时 md 已开、源文本未变。
> 引用规则：**每条都附两侧逐字原文**（源文按 `text/ch19_19.txt:<行>` ＋ 字符区间给出；md 按 `<md>:<行>` 给出）。
> 取证纪律：所有「查无」均用**显式文件路径** + `/usr/bin/grep`（不用 git grep / rg），命令与退出码见文末「取证三件套」。

---

## 一、单子「漏」：素读/源文有，md 无

### L1 ｜「身份盗用」假设 + 「Digby 当时正准备搬到 York」整段对话（md 完全未收）— 档：提示（关键情节已覆盖，非阻断）

- 源文逐字（`text/ch19_19.txt:26`，字符区间 **[464, 515]**）：
  > ‘Do you think it was some sort of identity theft?’
- 源文逐字（`text/ch19_19.txt:29`，字符区间 **[517, 616]**）：
  > ‘Possibly? Although Digby was going to move to York, wasn’t he? Maybe there’s a connection there?’
- md 侧：6 条引语（`:19 :25 :31 :37 :43 :49`）**无一条**取这两段；导航五项（`:11`–`:15`）与一句话总结（`:99`）也未出现「身份盗用 / 身份盗用假设」或「Digby 即将搬去 York」这一条线索。
  md 中唯一与 York 有关的文字是原句 5 的「他们醉得差点误了**回约克**的末班车」（`:44`），与「Digby 正搬去 York」不是一回事。
- 取证：`/usr/bin/grep -n "identity theft" "<md>"` → 退出码 1（无命中）；`/usr/bin/grep -n "搬" "<md>"` → 退出码 1（无命中）。
- 判定理由：这是本章唯一的**地理系线索**——Harrogate 这个地址之所以能被拿来做文章，靠的正是「Digby 正准备搬去 York」这座桥；md 把「Harrogate」写足了，却没写这座桥。因本章情节主干（信箱→付款人→Nathan→三年前→Priory Square）全部在 md 里，不构成「关键事件/转折未出现」，故记**提示**而非阻断。
- 建议（不改语义，只补一句）：在导航「线索结构」里把这一环补成「→ 身份盗用假设 + Digby 即将搬去 York（Harrogate 与 York 挂上钩）→」。

### L2 ｜Caius 开场的「周末小住 / 快下班」轻松话头 — 档：提示

- 源文逐字（`text/ch19_19.txt:23`，字符区间 **[265, 462]**）：
  > ‘Oh that’s a lovely part of the world. Very fancy.’ It was just the sort of place to go for a weekend away. A baby moon, maybe? Caius checked his watch. It was coming up to the end of their shift.
- md 侧：无一条引语取此段；导航「叙事手法」只提到结尾的打趣，未提开场的班次尾声。
- 判定理由：这是氛围/过场级内容，不承载情节转折 ⇒ **提示**（不阻断）。

### L3 ｜Caius 计划去 Barnet 邮局调监控 — 档：提示（但属「后续全书要用」的伏笔，建议补）

- 源文逐字（`text/ch19_19.txt:107`，字符区间 **[3505, 3633]**）：
  > ‘I’ll get hold of Barnet Post Office and get the CCTV for the days that the letters were posted,’ Caius said, shaking his head.
- md 侧：无一条引语取此段，全文未出现「监控 / CCTV」。
- 交叉证据（说明它不是可有可无的过场）：本书 `ch25 scott brown goes missing.md:11` 写「**三天邮局监控**里，两个女人各来两天，只有一个男人三天全到」；`text/ch25_25.txt` 承此线。⇒ 该伏笔在本章就立起来。
- 判定理由：本章情节主干不缺这一环 ⇒ **提示**；但它是「信箱→监控→寄信人」这条线的唯一起点，补一句成本极低。

### L4 ｜本章所属分部「A TUESDAY IN MAY」未标注 — 档：提示（形态项，不计入漏的阻断）

- md 侧：`/usr/bin/grep -n -i "tuesday\|分部" "<md>"` → **退出码 1（零命中）**；md 全文没有任何分部/星期标注。
- 权威源侧（源文本章无此信息，属**提取件不载**，须回到 epub）：
  - epub TOC（`OPS/TOC.xhtml`）：`TUESDAY` 分部下辖章号 **16 17 18 19 20** —— ch19 确在 TUESDAY 分部内。
  - epub 分部文件 `OPS/s027-Part-005.xhtml` 正文首行即 `TUESDAY`；该分部文件位于 ch19 章节文件 `OPS/s031-Chapter-019.xhtml` 之前。
  - `OPS/s031-Chapter-019.xhtml` 的场景标题为 `The Police Station`，正文首段与 `text/ch19_19.txt` 逐字一致（已做片段包含比对：命中）。
  - 命令与退出码：`python3 -c "<zipfile 读 TOC/Part/Chapter>"` → 退出码 0，输出见上。
- 横向对照（本书 54 章 md）：`/usr/bin/grep -rl "分部" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/*.md` → 退出码 0，命中 **26** 个文件（ch13/ch16/ch18/ch21/ch22/ch24/ch25/ch26/ch27/ch28/ch29/ch30/ch31/ch33/ch34/ch36/ch38/ch39/ch42/ch44/ch47/ch49/ch50/ch51/ch53/ch54）；**ch19 不在其中**；同属 TUESDAY 分部的 ch17、ch20 也不在其中。
- 判定理由：分部标签不是事件，不属 R3「关键事件/转折」⇒ **提示**（且本书仅约半数章节带此标注，非众数义务）。

---

## 二、单子「编」：md 有，原文无

### C1 ｜「一张收据」贯穿四处（导航一句话概括 / 线索结构 / 原句 1 的「为什么这样写」/ 一句话总结）— 档：**提示**（比喻性引申，非凭空情节）

- md 侧逐字：
  - `<md>:11` 「邮局**回信里的一张收据**把邮政信箱指向 Barnet……」
  - `<md>:13` 「**收据与信箱**（Barnet、只买三个月）→」
  - `<md>:22` 「作者把一张**收据**拆成三步，让它变成一个可以出行的方向。」
  - `<md>:99` 「一张邮局**收据**把信箱、付款人和一个哈罗盖特的地址串成一条线……」
- 源文侧逐字（`text/ch19_19.txt:20`，字符区间 **[40, 263]**）：
  > ‘I’ve got the information from the Post Office,’ Matt said, opening the email. ‘The PO Box is located in Barnet and was paid for by a Mrs Beverley Parkin, her address is in Harrogate. They only bought it for three months.’
- 取证（本章查无 receipt）：
  - `/usr/bin/grep -c -i "receipt" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch19_19.txt` → 输出 `0`，退出码 1。
  - 全书范围查（说明本书的「收据」另有所指）：`/usr/bin/grep -rn -i "receipt" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/` → 命中仅 `text/ch04_4.txt:35`（果蔬店收据）、`text/ch04_4.txt:62`、`text/ch04_4.txt:68`、`text/ch16_16.txt:205`、`text/ch16_16.txt:223`、`text/ch27_27.txt:176`、`text/ch32_32.txt:137`，退出码 0。
- 判定理由：本章原文的载体是**邮局发来的一封邮件**（「opening the email」＋「the information from the Post Office」），并无「收据」这一实物；把它称作「一张收据」是把它读成「付款记录」的比喻。**它没有凭空造出情节、关系或数字**（信箱/付款人/地址/三个月四项事实全部与原文一致），故按「措辞引申」记 **提示**；但「邮局**回信**里的一张**收据**」字面上指一件实物，本章不存在 ⇒ 若要保真，可改为「邮局发来的一封邮件」「一份付款记录」。
- 备注：本次审查任务简报本身使用了「从一张收据到一个活人」这一措辞，故本条更可能是**承任务措辞**而非笔误；此处只作提示，不建议照单硬改。
- 另：本书 ch04 的「收据」确有实物（`text/ch04_4.txt:35`「He found a receipt for the greengrocer’s…」），故「收据」一词在本书并非生造 —— 但**不可与本章混用**，本章那封邮件与 ch04 的果蔬店收据不是同一件东西。

---

## 三、单子「错」：两边都有，但不一致

### E1 ｜「独自出现在哈罗盖特」与原文冲突 — 档：**阻断**（本章最实的一处）

- md 侧逐字（`<md>:41`，原句 4 的「读者视角提示」）：
  > 留意这个妹妹的特征：被姐姐管着、**独自出现在哈罗盖特**、让 Nathan 看着她不自在。
- 源文侧逐字（`text/ch19_19.txt:77`，字符区间 **[1901, 2232]**）：
  > ‘It was a Saturday evening and we were a little worse for wear. There was this girl there **with her troll of a sister**. It started out as normal flirting. …’
- 源文侧逐字（`text/ch19_19.txt:89`，字符区间 **[2828, 3353]**）：
  > … ‘The beauty got **pulled away into the night by her sister** who’d got pissed off and was never seen again. …’
- 冲突点：她是**与姐姐同来**、最后**被姐姐拖走**的，源文两处都明写姐妹同行；md 说「独自出现在哈罗盖特」与两处原文均相反。同一块的中文理解（`<md>:38`「酒馆里有两个姐妹，姐姐一直想带妹妹走」）写对了，因此这是 md **内部也自相矛盾**的一处。
- 建议改法（保真、保留原意）：「留意这个妹妹的特征：被姐姐管着、和姐姐一起出现在哈罗盖特、让 Nathan 看着她不自在。」
- 唯一可能的宽松读法：把「独自」读成「作为一个具体的人（而非笼统的『那个妹妹』）」—— 但同块下一句「她在本章始终没有名字」已承担了「没有名字」这层意思，故「独自」在此只能是「一个人／单独」之意 ⇒ 判为**阻断**（1 处、1 个词的量级）。

### E2 ｜「排除掉一圈人」——本章只排除了一个人，且与 md 自己的一处说法打架 — 档：提示

- md 侧逐字（`<md>:11` 导航「一句话概括」）：
  > 警方顺着这个名字**排除掉一圈人**，又从迪吉的大学好友嘴里挖出三年前哈罗盖特的一次日游……
- md 侧逐字（`<md>:99`「一句话总结」）：
  > 警方用姓名和阶层先**排除掉一圈人**，再从迪吉的大学好友嘴里翻出三年前那个周末……
- md 侧逐字（`<md>:29`，原句 2 的「读者视角提示」——**自相矛盾的一边**）：
  > 注意排除的方向：不是说 Beverley Parkin 不可能是凶手，而是说她不像是这个圈子里的人——**排掉一个人**，就等于把范围收窄一圈。
- 源文侧逐字（`text/ch19_19.txt:32`，字符区间 **[618, 758]**）：
  > ‘I’d say with a name like Bev though there’s at least one generation difference between her and Digby, and probably a social class or two.’
- 判定：源文这一拍只排除了**一个**名字（Beverley Parkin 这一类）；本章从未出现「排除一圈人」的动作。md 自己在 `<md>:29` 写的是「排掉一个人」⇒ 与 `:11`、`:99` 不一致。**数字口径不一致 ⇒ 提示**（未凭空造出人物/情节，故不判阻断）。建议统一成「排除掉一个人」或「先排除掉一类人」。

### E3 ｜「当馆长」vs 原文「a curator in a museum」 — 档：提示

- md 侧逐字（`<md>:38`，原句 4 的「中文理解」）：
  > 迪吉一见到妹妹就被迷住了，拼命讲自己在伦敦一家博物馆**当馆长**的故事来打动她
- 源文侧逐字（`text/ch19_19.txt:83`，字符区间 **[2276, 2816]**）：
  > … Digby was enamoured the moment he saw her. He was telling her all about his life, trying to impress her with **saying that he was a curator in a museum down in London** and all that. …
- 判定：`curator` 的准确中文是「策展人／博物馆馆员」，「馆长」是**职级上移了一格**（且「馆长」在本义的「curator of a museum」之外另有所指）。md 同块关键词写的是 `curator in a museum`（`<md>:39`）⇒ 中文处理与关键词不一致。属用词不准 ⇒ **提示**。
- 附带肯定项（不需改）：md 用「拼命讲……**的故事**来打动她」保住了原文 `saying that he was a curator` 的**自称**性质（他当时在对女孩吹牛），没有把「他真是策展人」写成事实 —— 这一点是对的，见 §已核实为正确。

### E4 ｜「她从没被人这样正眼看过」把 `as if` 写成事实 — 档：提示

- md 侧逐字（`<md>:38`）：
  > 她**从没被人这样正眼看过**，于是为这点关注上了瘾。
- 源文侧逐字（`text/ch19_19.txt:83`）：
  > It was **as if** Digby was the only man who’d ever seen her and she’d gone wild for the attention.
- 判定：原文是 Nathan 的揣测语气（as if），md 写成陈述句。属表述强度问题 ⇒ **提示**（建议加「像是」二字）。

### E5 ｜「Simm 从不敢进屋」— 档：提示

- md 侧逐字（`<md>:14`，导航「人物弧线」）：
  > Tiny Simm 则**从不敢进屋**到自己跑去报告一条也许无关的入室案，那种想被看见的冲动写得清清楚楚。
- 源文侧逐字（`text/ch19_19.txt:116`，字符区间 **[3755, 4066]**）：
  > ‘Thanks, sir.’ Tiny Simm **moved on the spot**. He felt like he was **sticking his head above the parapet**. Caius had a reputation for being a bit of a bastard when he wanted to be around the station, but he liked the guy. …
- 判定：原文写的是他「紧张得动个不停」＋「像把头探出矮墙外」＝ **怕出风头／想被看见**（这个方向 md 抓对了），但「不敢进屋」是原文没有的具体行为 ⇒ 引申过头，**提示**。（可改作「从在门口踱步到自己跑去报告一条也许无关的入室案」。）

### E6 ｜「把一场命案包成一次好玩的周末」— 档：提示

- md 侧逐字（`<md>:15`，导航「叙事手法」）：
  > Nathan 的大段独白用俚语、粗话和玩笑把**一场命案包成一次好玩的周末**
- 源文侧逐字（`text/ch19_19.txt:89`）：
  > … We were so twatted we nearly missed the last train back to York. **It was a fun day.** I’m going to miss him so much. He’d bring that girl up every now and then.
- 判定：Nathan 在这段独白里**从头到尾没有提到命案**（他说的是 Digby 活着时那次「好玩的周末」，并且用的是现在时「I'm going to miss him」——他此刻仍以为 Matt 不知道 Digby 已死）。被「包成好玩的周末」的是**那次艳遇**，不是命案。属转述对象的错位 ⇒ **提示**。（可改作「把三年前的一次艳遇包成一次好玩的周末」。）

### E7 ｜原句 1「读者视角提示」自述的顺序与同块「为什么这样写」不一致 — 档：提示

- md 侧逐字（`<md>:22`，原句 1 的「为什么这样写」）：
  > 三项信息被排进同一句，顺序是**地点、付款人、地址**，而收尾落在「只买了三个月」上……
- md 侧逐字（`<md>:23`，原句 1 的「读者视角提示」）：
  > 记住这个顺序：**谁付的钱 → 钱付给了谁 → 人在哪**。
- 源文侧逐字（`text/ch19_19.txt:20`）：
  > ‘The PO Box is located in Barnet and was **paid for by a Mrs Beverley Parkin, her address is in Harrogate**. They only bought it for three months.’
- 判定：源句的排列是 地点→付款人→地址→期限；`:23` 给读者记的却是 付款人→收款方→地点，且「钱付给了谁」并不在引语里（原文只有 `paid for by`，钱付给的是邮局=信箱，隐含而已）。同一块自述两套顺序 ⇒ **提示**。

---

## 四、三张单子汇总

| 单子 | 条数 | 阻断 | 提示 | 说明 |
|---|---|---|---|---|
| 漏 | 4（L1–L4） | 0 | 4 | 本章情节主干在 md 内；缺的是 York 桥、班次尾声、CCTV 伏笔、分部标签 |
| 编 | 1（C1 收据） | 0 | 1 | 比喻性引申，未凭空造情节/数字；取证见 §取证三件套 |
| 错 | 7（E1–E7） | **1（E1）** | 6 | E1「独自出现在哈罗盖特」与源文两处相反 |

**阻断型合计：1 条**（E1）。
