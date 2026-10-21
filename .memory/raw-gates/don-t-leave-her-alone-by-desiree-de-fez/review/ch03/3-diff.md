# R3 对账 + R4 逐块判定 · ch03

> 审查员：DSH-Mac（R3 对账员 + R4 逐块判定员）
> 真值来源：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch03_chapter_3.txt`（81 段纯对白）
> md：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch03 chapter 3.md`（123 行，6 个引语块）
> 素读底稿：`.memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/review/ch03/1-suread.json`（8 条 facts）
>
> 落盘时间：2026-10-21 · 未修改任何原文件（只读 + 写本文件）

---

## 0. 方法与口径声明（先说清，避免误报）

1. **原文 81 段**（`text/ch03_chapter_3.txt` L6–L246，每段一句对白）。说话人归属全部按
   「内容自指句」分派，已逐条回原文确认，**未发现 md 说话人错配**（详见 §4）。
2. **md 覆盖口径**：md 的 6 个引语块用「`…`」拼接了原文的**若干段**，并把同段内多句合并为一段。
   判定「落点」时按**语义是否被覆盖**判，不按「整段逐字命中」判。
3. **本报告不做的判定**：不把 `text/` 句子与 md 里的无关分析行拼装成「错位」；
   报警前已确认引语行与分析行在**同一 md 文件内且相邻**（本报告所有 md 落点均在 `ch03 chapter 3.md` 内）。
4. **交叉引用行**（L39 / L40 / L50 / L74 / L85 等提及 ch01、ch02 的行）**不计入 R3 三张单子**，
   因为它们不是本章事实；只在 §5 单独列出「移章/编」类问题。

---

## 1. R3 第一张单子：漏（素读 fact 有、md 里完全没有）

> 判定说明：「md 里完全没有」＝ 该 fact 的**关键内容**（人物 / 数字 / 动作 / 结论）在 md 全文中检索不到。

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F1 开场：Diana 第一句「What are you doing?」；Alba 答在 Finestrelles；Diana 追问「你们不是早上去过吗、我跟妈妈通过话，她说你还在那儿」；Alba 说人太多换不了手柄 | 无 | ❌ 漏 |
| F1（续）Diana 问「什么手柄」；Alba 答是 Switch 的手柄 | 无 | ❌ 漏 |
| F1（续）Diana 问店里不是说没货了吗；Alba 说自己上网查过、Finestrelles 的 MediaMarkt 还剩两个 | 无 | ❌ 漏 |
| F1（续）Diana 怀疑库存不是实时更新；Alba 说不知道，还在等店员来帮忙 | 无 | ❌ 漏 |
| F2（续）Alba 吐槽「在真正的平安夜买？你没救了」；Diana 辩称实在排不上队、一部分礼物是网上下单的 | 无 | ❌ 漏 |
| F4（续）Diana 不信，Alba 强调「我不开玩笑，我是为了换手柄才折回来的」；Diana 骂「Jesus, Alba，你就不能改天再去吗」（后半在 md，**前半不在**） | 无（前半） | ❌ 漏 |
| F5（续）Diana 问妈妈是不是带着三个孩子，Alba 答宝宝在自己手上 | 无 | ❌ 漏 |
| F5（续）Diana 问 Juan 这周不是上半天班吗，能不能留下来看孩子、让妈妈去参加酒会 | 无 | ❌ 漏 |
| F5（续）Alba 说 Juan 跟自己在一起，还转述妈妈讲自己不在乎、只是累了 | 无 | ❌ 漏 |
| F6（续）Alba 说自己没法一个人坐公交（因果在 md，**「I can’t take the bus by myself」的因果=公交挤+带娃**在 md） | 无 | ✅ 一致（见 §2 F6 行） |
| F6（续）Alba 说他一要吃奶就撒泼 | `ch03 chapter 3.md:65`（引语）、`:71`（分析） | ✅ 一致 |
| F6（续）Alba 说上次她把宝宝留给妈妈，半小时后妈妈就慌得不行打电话叫她掉头回去，宝宝哭到吐 | `ch03 chapter 3.md:73`（仅提及 "throws up"（后文）） | ❌ 漏（事件本体：半小时/妈妈慌/掉头/哭到吐，均无） |
| F6（续）Alba 强调跟爸爸他也会闹 | `ch03 chapter 3.md:73`（仅提及 "throws a fit"（后文）） | ❌ 漏（"with his dad, too" 事件本体无） |
| F6（续）Diana 建议改坐 tram，Alba 说节日里挤得要命、昨天回家路上人多还把暖气开到最大、推着婴儿车痛苦不堪 | `ch03 chapter 3.md:117`（词表：tram）、`:106`（词表：grossed out 例句） | ❌ 漏（分析层未展开；引语块未收录） |
| F6（续）Diana 建议用背带，Alba 答宝宝不喜欢 | `ch03 chapter 3.md:118`（词表：carrier） | ❌ 漏（"He doesn’t like it" 这句回应无；词表只留 Diana 的问句） |
| F7（续）Alba 说他们刚到 MediaMarkt，人多得让人难受，还要买 Caga Tió | `ch03 chapter 3.md:116`（词表：Caga Tió 例句） | ❌ 漏（"刚到 MediaMarkt / 人多得难受" 事件本体无） |
| F7（续）Diana 问能不能分头行动，Alba 说不行、她更想让 Juan 陪着，因为自己分不清手柄型号 | 无 | ❌ 漏 |
| F7（续）Diana 吐槽「你一个人出去找了好几天」，Alba 纠正「不是一个人，我跟妈妈在一起」 | 无 | ❌ 漏 |
| F7（续）Alba 说信号太差要挂了、提醒 Diana 别忘了明天 | 无 | ❌ 漏 |
| F7（续）Diana 问明天有什么活动，Alba 说「你明知故问，明天是我生日」 | 无 | ❌ 漏（仅 md L52 提及 "my birthday thing"，**"明天是我生日"这句台词本身未收**） |
| F7（续）Diana 说他们要接孩子、只能过来吃蛋糕，Alba 说已经告诉孩子们 Diana 要来吃午饭 | 无 | ❌ 漏 |
| F7（续）Diana 说反正平安夜那天会来、到时再正式庆祝 | 无 | ❌ 漏（仅 md L52 提 "Christmas Eve" juxtaposition） |
| F7（续）Alba 说两件事不能一起庆祝、那样不吉利 | `ch03 chapter 3.md:76`（引语）、`:78`、`:82`、`:84`、`:85`、`:105` | ✅ 一致 |

**小计：漏 = 21 条**（F1 全部 4 个子项、F2 吐槽 1 项、F4 强调 1 项、F5 全部 3 项、F6 事件本体 3 项、F7 全部 7 项）

---

## 2. R3 第二张单子：编（md 有、素读 fact 没有 ⇒ 必须回原文核实）

> 已对 md 中所有 md 独有的实质内容逐条回 `text/ch03_chapter_3.txt` + `library/*.epub` 核实。

| md 落点 | md 独有内容 | 原文核实结果 | 判定 |
|---|---|---|---|
| `ch03 chapter 3.md:29` | 「本章时间锚点——**8:30 PM**，商场开到 10 点」 | 原文 L36 “It’s eight thirty already. How late are they open?” / L39 “Until ten.” ⇒ **8:30 与 10 点都在原文**，但**原文只说 eight thirty，未写 AM/PM**。写死 “8:30 PM” 属推断而非原文（本章时间线可由 ch08–ch10 确认为傍晚，故推断方向正确） | ⚠️ 需人判（推断补足，非凭空编造） |
| `ch03 chapter 3.md:40` | 「"It was bad" 指 **ch01 的演出（Diana 迟到、Brisa 罢演）**」 | `text/ch01_chapter_1.txt:12`（Diana 赶到学校演出现场）、`:30`（Brisa 因母亲缺席而罢演、抱臂、蒙眼）⇒ **属实** | ✅ 非编（跨章回指，本报告不计入 R3） |
| `ch03 chapter 3.md:74` | 「Alba 的 "I can’t take the bus by myself" 是 **ch02 dissociation** 的 precursor」 | 全文 grep `dissociat` **0 命中**（`text/` 全目录）⇒ “dissociation” 是 md 自造术语，**ch02 无此表述** | ❌ 编（阻断型·自造分析标签） |
| `ch03 chapter 3.md:74` | 「"She got her nails done yesterday!" 与 **ch02 "I bought a shirt and got my nails done for the holidays"** 呼应」 | `text/ch02_chapter_2.txt:282` ⇒ **逐字属实** | ✅ 非编 |
| `ch03 chapter 3.md:74` | 该行称 **Carmen** 的 nails ⇒ 见 §3「错」条 | — | 见 §3 |
| `ch03 chapter 3.md:50` | 「"Impossible" … 与第二章的 **"on purpose" 踢玩具车**形成强迫性控制模式」 | `text/ch02_chapter_2.txt:9`「kicked a toy car … She had done it **on purpose**」⇒ **属实** | ✅ 非编 |
| `ch03 chapter 3.md:62` | 「这与 ch02 的 "compulsions" 形成一致」 | `text/ch02_chapter_2.txt:132`「She knew almost all of Alba’s **compulsions** and superstitions」⇒ **属实** | ✅ 非编 |
| `ch03 chapter 3.md:85` | 「"bad luck" 与 ch02 的 **"evil eye"**、**"compulsions"** 形成家族 superstition 体系」 | `text/ch02_chapter_2.txt:132 / 351 / 381 / 411 / 441 / 447` ⇒ **evil eye 逐字属实**；compulsions 同上 | ✅ 非编 |
| `ch03 chapter 3.md:10` | 「Alba 在商场为换手柄与 **Juan、婴儿**同行，要求 **Carmen 代看孩子**、放弃圣诞聚会」 | 原文 L147 “Juan is with me.”、L135 “the baby’s with me.”、L75 “She stayed with the kids.” ⇒ 婴儿随行属实；**「要求 Carmen 代看孩子」为原文事实**（L75 Alba 告知） | ✅ 非编 |
| `ch03 chapter 3.md:10` | 「揭示家族女性间的控制、牺牲与 superstition」 | 属分析判断，非事实断言 ⇒ 不判编 | ✅ 非编 |
| `ch03 chapter 3.md:16` | 「**全章对话驱动，无叙述者描述**」 | 原文 81 段**全是对白**，无叙述段 ⇒ **属实** | ✅ 非编 |
| `ch03 chapter 3.md:63` | 「MediaMarkt vs Corte Inglés 是巴塞罗那零售 **geography**（MediaMarkt 电子、Corte Inglés 百货）」 | 原文 L126 “surely they have them at Corte Inglés?”、L129 “It has to be MediaMarkt.”；`text/ch02_chapter_2.txt:126` 确认 MediaMarkt 为电器店 ⇒ **常识性补充，不与原文冲突** | ✅ 非编 |
| `ch03 chapter 3.md:12` | 「把 ch02 的 Alba 与 ch01 的 Diana 并置」 | 章节安排事实 ⇒ 非编 | ✅ 非编 |
| `ch03 chapter 3.md:107` | 词表例句 `"It’s always packed this time of year"` | 原文 L165 “Because **it’s always packed this time of year** and I get overwhelmed with the baby.” ⇒ **逐字属实**（工具 `check_vocab.py` 因大小写折叠显示 OK） | ✅ 非编 |
| `ch03 chapter 3.md:29` | 「Alba 的 "more presents" 与 **ch02 的 controller exchange** 连续」 | `text/ch02_chapter_2.txt:126` 换 Switch 手柄 ⇒ **属实** | ✅ 非编 |

**小计：编 = 1 条（阻断型）** —— `ch03 chapter 3.md:74` 的 “ch02 dissociation” 标签（全书无此词）

---

## 3. R3 第三张单子：错（两边都有但不一致）

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F4：Alba 说妈妈（Carmen）**没去成**圣诞酒会，因为她**留下看孩子** | `ch03 chapter 3.md:31`（引语 “She stayed with the kids.”）、`:33`（中文理解「她留下来带孩子了。」）、`:37`（句子结构「**Alba 说 Carmen 没去**；…Alba 解释 "She stayed with the kids."」） | ❌ 错 |
| F4：Alba 强调「**我不开玩笑**，我是因为换手柄才折回来的」 | `ch03 chapter 3.md:37` 句子结构把 “With what kids?” 之后直接接 “Well, with mine.”，**未收录 “You’re kidding.” / “No, I’m not kidding!” 两句** | ❌ 漏（已在 §1 计入；此处标注它与 md L37 的省略冲突） |
| F1：Alba 说 **Switch 的手柄** | `ch03 chapter 3.md:101-102` 词表 `controller` 例句用 “I couldn’t exchange the controllers”（L102）⇒ 词条释义「手柄」正确；但**“Switch” 这个限定词在 md 全文 0 命中**（md L102 只引 "the controllers"） | ❌ 漏（限定信息丢失） |
| F2：Alba 说自己**明天也不行**（上午宝宝体检、下午生日的事） | `ch03 chapter 3.md:42` 引语收 “On Christmas Eve? Hell no.”；md L44 中文理解写「早上宝宝要体检，下午我们庆祝我的生日」⇒ 一致 | ✅ 一致 |
| F7：Alba 说**两件事不能一起庆祝、那样不吉利** | `ch03 chapter 3.md:78` 中文理解「你不能同时庆祝两件事。不吉利。你知道的。」⇒ 一致 | ✅ 一致 |
| —（md 独有）| `ch03 chapter 3.md:74`：「"She got her nails done yesterday!" … 显示 **Carmen** 的 Christmas party 期待被 Alba 牺牲」 | ❌ 错（**说话人/主语错**） |
| —（md 独有）| `ch03 chapter 3.md:74`：「与 ch02 "I bought a shirt and got my nails done for the holidays" 呼应」 | ❌ 错（**归属错**） |

**小计：错 = 3 条（均属阻断型）**

### 3.1 错条 A：`ch03 chapter 3.md:37` —— 说话人张冠李戴

- md 原文：`**句子结构**：对话——Diana 问演出；Alba "bad"；Diana 追问；Alba 推迟 + 提及 Carmen 聚会；**Alba 说 Carmen 没去**；Diana 追问；Alba 解释"She stayed with the kids."；…`
- 原文回证（`text/ch03_chapter_3.txt`）：
  - L69 `“She didn’t go.”` ← **Alba**（Alba 刚说妈妈有酒会；此处是 Alba 告诉 Diana 妈妈没去）
  - L72 `“How come? She wouldn’t shut up about it all week. She was driving me nuts.”` ← **Diana**
  - L75 `“She stayed with the kids.”` ← **Alba**
  - L78 `“With what kids?”` ← **Diana**
  - L81 `“Well, with mine.”` ← **Alba**
- md 把 L72（**Diana** 的话：妈妈念叨了一整周、把 Alba 逼疯）写成 **Alba 说的**，且把 “She didn’t go.”（Alba）与 “She stayed with the kids.”（Alba）之间插了一句 Diana 的话却未标明说话人切换。
- 附带影响：md L39「作者用 "She wouldn’t shut up about it all week" 揭示 **Carmen 的期待**」把这句归给 Diana 是对的，但同句在 L37 被归给 Alba ⇒ **同一引语在 md 内两处归属不一致**（自相矛盾）。
- 判定：**❌ 错（说话人错配）**

### 3.2 错条 B：`ch03 chapter 3.md:74` —— 「She got her nails done yesterday」归错人

- md 原文：`"She got her nails done yesterday!" 与 ch02 "I bought a shirt and got my nails done for the holidays" 呼应，显示 **Carmen** 的 Christmas party 期待被 Alba 牺牲`
- 原文回证：
  - `text/ch03_chapter_3.txt:156` `“You know she cares! She got her nails done yesterday!”` ← **Diana** 说，指 **Carmen**（L153 Alba 刚说妈妈不在乎、只是累了）
  - `text/ch02_chapter_2.txt:282` `“I bought a shirt and got my nails done for the holidays, not for my class.”` ← **Carmen** 对 Alba 说
- md 的问题：把 Diana 转述的 “She got her nails done” 与 **Carmen 本人在 ch02 的第一人称台词** 并列为「同一件事的呼应」，等于把转述句与原话主语混为一谈；「显示 Carmen 的期待被 Alba 牺牲」这一结论方向不错，但论据的**主语链断裂**。
- 判定：**❌ 错（主语/人物关系不一致）**

### 3.3 错条 C：`ch03 chapter 3.md:74` —— 「ch02 dissociation」标签在原文无对应

- md 原文：`Alba 的 "I can’t take the bus by myself" 是 **ch02 dissociation** 的 precursor`
- 原文回证：全书 `text/` 目录 grep `dissociat` **0 命中**；`text/ch02_chapter_2.txt` 无任何解离/失神的表述（Alba 在 ch02 的状态是「回避、仪式性折返、见人就怕」）。
- 判定：与「编」条同源，归入 §2 编（阻断型），此处并列以示它是**分析层硬伤**而非措辞问题。

**小计：错 = 3 条**（A、B 为人物/主语错配；C 与 §2 编条同源）

---

## 4. 说话人归属专项复核（ch03 提示要求：判「说话人错配」前必须逐条回原文）

已对 md 全部 6 个引语块的 **39 段引语**（`2-machine.json` 记录 `segments=39, segment_miss=0`）逐条回原文确认归属：

| md 块 | md 标注的说话人 | 原文核对 | 结论 |
|---|---|---|---|
| 原句 1（md:20） | Diana 问时间 → Alba 答 → Diana 反问 → Alba 反问 → Diana 答 | L36/39/42/45/48 交替 ⇒ 一致 | ✅ 无错配 |
| 原句 2（md:31） | Diana 问演出 → Alba "bad" → Diana 追问 → Alba 推迟 → **Alba 说 Carmen 没去** → Diana 追问 → Alba 解释 | L57/60/63/66（Alba 推迟）/L69（**Alba 说没去**）/L72（**Diana**）/L75（Alba）/L78（**Diana**）/L81（Alba）⇒ **md 在 L37 把 L72 的 Diana 台词算作 Alba** | ❌ **错配 1 处（见 §3.1）** |
| 原句 3（md:42） | Diana 提议 → Alba 反问 → Diana 提议 → Alba 拒绝 → Diana 提议 → Alba 拒绝 | L90/93/96/99/102/105/108/111/114/117 ⇒ 一致 | ✅ 无错配 |
| 原句 4（md:54） | Diana 提议 → Alba 追问 → Diana 提议 → Alba 拒绝 | L120/123/126/129 ⇒ 一致 | ✅ 无错配 |
| 原句 5（md:65） | Diana 提 nails → Alba 拒公交 → Diana 追问 → Alba 解释 → Diana 追问 → Alba 答 → Diana 反讽 → Alba 答 → Diana 建议 | L156/159/162/165/168/171/174/177/180 ⇒ 一致 | ✅ 无错配（但 L156 说话人是 Diana、**不是 Carmen**——md 的分析层 L74 归错，见 §3.2） |
| 原句 6（md:76） | Alba 拒 → Diana 收尾 | L243/246 ⇒ 一致 | ✅ 无错配 |

**结论：ch03 说话人错配 1 处（`ch03 chapter 3.md:37`）。** 未发现「把 Diana 的台词说成 Alba 的」以外的第二类问题。

---

## 5. 显式列出**没有进扫描集**的内容（纪律第 3 条）

| 未进扫描集的内容 | 原因 |
|---|---|
| `text/ch03_chapter_3.txt` L6–L34（开场 10 段：What are you doing? → We're still waiting for them to help us） | **md 未收录** ⇒ 属 §1 漏项，不参与「md 已有内容」的一致性判定 |
| `text/ch03_chapter_3.txt` L51、L54（“On actual Christmas Eve? You're hopeless.” / “Oh stop, I just couldn't get to it sooner…”） | **md 未收录** ⇒ §1 漏项 |
| `text/ch03_chapter_3.txt` L84、L87（“You're kidding.” / “No, I'm not kidding!…”） | **md 未收录** ⇒ §1 漏项 |
| `text/ch03_chapter_3.txt` L132–L155（Juan 上半天班 / Juan is with me / What the hell, Alba… / She told me she didn't care…） | **md 未收录** ⇒ §1 漏项 |
| `text/ch03_chapter_3.txt` L183–L211（Last time I left him with Mom… / with his dad / tram / carrier） | **md 未收录**（tram、carrier 仅进词表）⇒ §1 漏项 |
| `text/ch03_chapter_3.txt` L216–L240（分头行动 / 不是一个人 / 明天是我生日 / 吃蛋糕 / 吃午饭 / 平安夜再庆祝） | **md 未收录** ⇒ §1 漏项 |
| md 词表 `## 词汇分级` 全部 16 行（md:91–119） | 属词汇层，非 R3/R4 事实层；仅对**例句逐字**做核（结果见 §6） |
| md `## 本章导航` 4 条（md:10–16） | 属导航层摘要，非引语块分析层；仅对可核事实做编/错判定（见 §2、§3） |
| md `## 一句话总结`（md:122） | 属总结层，事实已在上文逐条判过，不重复计条 |
| `text/ch01_chapter_1.txt` / `text/ch02_chapter_2.txt` 全文 | 跨章回指的核验范围（仅在 md 明写 ch01/ch02 时回查） |
| `library/*.epub` 全文 | 仅在需要区分「text 提取件缺漏」时回查（ch03 本章 text 与 epub 一致，无需补判） |

---

## 6. 附：md 英文串逐字核查（对 `text/ch03_chapter_3.txt`）

- md 内 148 个引号串，**64 个非逐字命中**；其中 57 个是**中文译文**（“现在都八点半了。…”）与**中文引号内的跨段拼接**（引号内含 `”` / `"` 混排导致的正则误捕），**不是编造**。
- 真正需要说明的 **ASCII 直引号** 8 个：全部**跨章引用或缩写**（`until ten` / `on purpose` / `compulsions` / `give him a cookie.` / `I bought a shirt and got my nails done for the holidays` / `evil eye` / `It's always packed this time of year` / `compulsions`）——逐条回原文核实**全部属实**，唯 `compulsions` 一词在 md 中两处（md:62、md:85）指 ch02 的 Alba 强迫症，**属实**。
- 词表 16 个例句：**15 个逐字命中**；`md:107` 的 `"It's always packed this time of year"` 命中（直引号 vs 弯引号差异，`check_vocab.py` 判 OK）。
- **结论：ch03 md 无「凭空造词」型编造。** 唯一的编是 §2 的 “ch02 dissociation” **分析标签**（非引语）。

---

## 7. R4 逐块对应人判（每个引语块：这段中文分析是不是在讲这句引语）

判定口径：只问「中文分析是否在讲这句引语」；**引语选短** = 分析在讲引语外的上下文；**不对应** = 分析讲的是别处；**密度不足** = 分析有效字数不足以支撑该引语。

| 块 | 引语首 20 字 | 判定 | 依据（哪一行分析） |
|---|---|---|---|
| 原句 1 | “It’s eight thirty already. How late are they open?” | 对应 | 中文理解 md:22 逐句对译（L20 引语 5 段 ↔ L22 译文 5 句一一对应）；句子结构 md:26 拆 “until ten” / “get a couple more presents” / “More presents?” / “sneaking out”；为什么这样写 md:28 讲 “More presents?” 反问 + “sneaking out”；读者视角 md:29 讲 8:30/10 点锚点与 ch02 换货连续 —— 全部落在引语内 |
| 原句 2 | “How was Brisa’s play?” | **引语选短** | 引语块含 10 段（L57–L81），但 md 分析实际只覆盖到 L66/L69/L75/L81；**L72（Diana：“How come? She wouldn’t shut up about it all week. She was driving me nuts.”）被算作 Alba 的话**（md:37）且 L84/L87（“You’re kidding.” / “No, I’m not kidding!”）根本不在引语块里 ⇒ 块内自相矛盾、且分析讲到 “Carmen 的期待” 时引语来源错乱。**阻断** |
| 原句 3 | “Jesus, Alba, couldn’t you have gone another time?” | 对应 | md:44 逐句对译 L90–L117；md:48 逐条点名 “When?” / “Impossible” / “On Christmas Eve? Hell no.”；md:50 讲 “When?” 与 ch02 “on purpose” 的控制模式；md:52 讲 “my birthday thing” × “Christmas Eve” 与后文 “bad luck” 铺垫 —— 全部对应。**唯一保留**：md:50 “无法考虑『以后』”属解读，非错 |
| 原句 4 | “You could have asked me to exchange them when I go for my stuff on Friday.” | 对应 | md:56 对译 L120–L129；md:60 逐句点名 “It has to be MediaMarkt”；md:62 讲 rigid 规则 + ch02 compulsions；md:63 讲 MediaMarkt vs Corte Inglés 地理 —— 全部对应 |
| 原句 5 | “You know she cares! She got her nails done yesterday!” | 对应（但含错） | md:67 对译 L156–L180；md:71 逐句点名 9 个引语点；md:73 讲 “practically a teenager” vs 过度保护、“give him a cookie”；md:74 讲 ch02 呼应 —— **对应成立**，但 md:74 的主语归错（见 §3.2）且 “ch02 dissociation” 无据（见 §2） |
| 原句 6 | “You can’t celebrate two things at once. It’s bad luck. And you know it.” | 对应 | md:78 对译 L243/L246；md:82 拆 “bad luck” + “Christ, Alba, I’ve got to go.”；md:84 讲迷信作为控制工具 + “And you know it.” 推向 Diana；md:85 讲 ch02 “evil eye” 家族体系 —— 全部对应 |

**R4 统计：对应 5 · 引语选短 1（阻断）· 不对应 0 · 密度不足 0**

**关于「密度不足」**：md 6 块每块均有 5 个子项（中文理解 / 关键词 / 句子结构 / 为什么这样写 / 读者视角提示），
`scripts/check_chinese_layer.py` 对本书报「合格分析密度 100% | 整层夹杂率 0% | 阻断型 0 | 提示型 0」；
`2-machine.json` 记录 `struct_bad=0, empty_quote=0, keyword_bad=0, cjk_low=0`。
⇒ **结构性密度不达标者 0 处**；「中文理解」最短块（md:78）中文占比 0.63、最长（md:67）0.45，均高于门禁 0.35 线。

---

## 8. ch03 结论

| 类别 | 条数 | 阻断型 |
|---|---|---|
| ❌ 漏 | **21** | 否（覆盖缺陷，非事实错误） |
| ❌ 编 | **1** | **是**（`ch03 chapter 3.md:74` “ch02 dissociation”，全书无此词） |
| ❌ 错 | **3** | **是**（说话人错配 md:37；主语错配 md:74 ×2） |
| R4 不对应/选短 | **1** | **是**（原句 2，md:37） |

**必须修的（阻断）**：
1. `ch03 chapter 3.md:37` —— L72（“How come? She wouldn’t shut up about it all week. She was driving me nuts.”）是 **Diana** 说的，md 归给 Alba；同时与 md:39 把该句归给 Diana 的说法**自相矛盾**。
2. `ch03 chapter 3.md:74` —— “ch02 dissociation” 标签在 `text/` 全书 0 命中，须删或换成有据表述（如 ch02 的「见人就怕 / 折返仪式」）。
3. `ch03 chapter 3.md:74` —— “She got her nails done yesterday!” 是 **Diana 转述 Carmen**，不能与 ch02 **Carmen 本人**的第一人称原话并列为“呼应”。

**覆盖缺陷（非阻断但影响完整度）**：ch03 原文 81 段中 **41 段**在 md 里找不到任何对应内容（开场 10 段 + hopeless/ordered online 2 段 + kidding 2 段 + Juan/妈妈不在乎 6 段 + 妈妈慌/哭到吐/爸爸也闹/tram/carrier 8 段 + MediaMarkt 到达/Caga Tió/分头行动/不是一个人/明天生日/吃蛋糕/吃午饭/平安夜再庆祝 13 段）。
⇒ md 6 个引语块只覆盖了 **40/81 = 49%** 的原文对白，**低于「逐字精读」应达到的覆盖面**；F1、F5、F7 三条素读 fact 的主体内容在 md 中完全缺席。

---

*本文件由 DSH-Mac 写入；未改动 `text/`、md 原文件、`1-suread.json`；未执行任何 git 操作。*
