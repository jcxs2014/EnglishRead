# ch11（书内 Chapter Ten）深审 R3/R4 三张单子

素读基线：`review/ch11/1-suread.json`（96 条事实／0 MISS，只读 `text/ch11_chapter_ten.txt`，写完才开 md）
机器层：`review/ch11/2-machine.json` → verdict `ok`（blocks 4 ∈ target [2,4]；segments 4／MISS 0；words 1248；struct_bad 0）
直撇号探针：`/tmp/apos.txt` 未列 ch11 ⇒ 0 站
词表：16 行例句展平逐字 **0 MISS**

## 🟥 阻断（8）

### C-11-1 事件写错：「那封引来母女的信」
- md:10：**「她随即坦白那封引来母女的信是她写的」**
- 反证逐字：`text/ch02_chapter_one.txt:107` — `I’m Caroline Beaumont’s daughter, Dartrine. I found your letter while cleaning out her belongings. I’m sorry to say she passed this week due to surgical complications.`；`text/ch02_chapter_one.txt:9` — `The letter lay in the kitchen trash, nestled between a mound of browning orange peels…`
- 判定：信**没有引来母女**——Mama 在 Dart 发出那封回信的那一周已经去世，信是 Dart 整理遗物时从厨房垃圾里翻出来的；来佛州的只有 Dart 一人。本章 :54 的 `before Mama actually reunited with the Greers` 里的 actually 正是这个未竟。改法：「那封写给 Mama、最终只把 Dart 引来的信」。

### C-11-2 全称断言有反例：「把此前所有不合理处一次归位」
- md:34：**「Dart 把此前所有不合理处一次归位：邮箱地址、失联理由，全是仿签名这同一个动作的零件」**
- 反证逐字（信里仿签名解释不了的东西）：`text/ch02_chapter_one.txt:24` — `Out fell a short letter written in sprawling cursive—and two halves of a ripped check for $30,000.`；`text/ch05_chapter_four.txt:219` — `Gazzie’s letter had mentioned copies.`；`text/ch06_chapter_five.txt:174` — `remembering that her letter had mentioned a certain attitude toward phones, but didn’t dare ask her.`
- 判定：归位的只有收件地址与失联理由两项（md 自己列出的这两项）；三万美元的半张支票、信里提到的画像副本、信里对电话的态度都仍挂着。⇒ 把「两项」写成「所有不合理处」，正好替读者关掉了本书最要紧的几条未决账。改法：「一次归位了收件地址与失联理由这两处——而信里的其余部分（三万美元、副本、对口径的要求）并未随之落定」。

### C-11-3 全称断言：「对话推动全部信息」
- md:14：**「对话推动全部信息，叙述层的缝隙用来放身体的背叛」**
- 反证逐字：`text/ch11_chapter_ten.txt:54` — `She’d forged it. Lied. That’s why the letter had asked Mama to email Aunt Virginia, not Gazzie.`（本章的关键定性全在叙述层，Virginia 本人从未说出 forge 一词，见 T-11-2）；`:9` 温室的构造全部由叙述给出；`:102` 她的职业幻想（HR manager→director、Atlanta／Charlotte／DC）亦全在叙述层。
- 改法：「对话交出本章绝大多数新信息，但最关键的一步（仿签名）由叙述层替她补上」。

### C-11-4 分析层语法误称：「两个 Why 开头的句子是省略主句的名词性残句」
- md:34：**「两个 Why 开头的句子是省略主句的名词性残句，语气是拼图落槽」**
- 原文逐字：`text/ch11_chapter_ten.txt:54` — `That’s why the letter had asked Mama to email Aunt Virginia, not Gazzie. Why it had claimed Gazzie didn’t check her email or answer phone calls.`
- 判定：第一句以 **That’s** 开头、主谓齐全（That is why…），不是残句；只有第二句 `Why it had claimed…` 是无主句的名词性残句。同族缺陷见 ch08 C-08-6（语法术语误称×2）。改法：「一句完整的 That’s why 起头，随后一句只留 Why 引导的残句——第二句把主句省掉，才做出拼图落槽的语气」。

### C-11-5 章内时序写反：末拍位置放错
- md:11：**「……落到 Harrison 名字砸下来的失重，最后停在「 bewildered but excited」的上扬上——本章收在希望一侧」**
- 原文行序：`:102` — `Aunt Virginia gazed after them while I processed her words, bewildered but excited.` → `:108` `“Not even Harrison.”` → `:111` `His name hit me like a steel wall.` → `:126` `This was my chance…` → `:129` `“I’m in,” I said breathlessly.` → `:132` `“Good,” she replied. “You’ll start tomorrow.”`
- 判定：`bewildered but excited` 在 Harrison 名字砸下来**之前**，不是之后；本章真正的末拍是 :126 的「这是我唯一的机会」＋:129 的气喘吁吁应下＋:132 的「你明天开始」。本库缺陷簇第一名。改法：把「bewildered but excited」移到失重之前，末拍改用 :126／:129／:132 三连。

### C-11-6 凭空属性：「靠鳄皮与阳光运转百年的家族生意」
- md:24：**「对一门靠鳄皮与阳光运转百年的家族生意来说」**
- 反证逐字：`text/ch08_chapter_seven.txt:219` — `“Gators grow faster in the dark… Some of ours don’t see the sun till the day they die, and they grow just fine.”`
- 判定：本书对这门生意的明写属性恰是**避开阳光**（黑暗养殖；温室这一段本身也在讲「把佛罗里达挡在外面」）。把「阳光」写进家族生意的定语，与该章的设定正面相撞。「百年」按 :93 `founding in the late 1800s` 尚可（略短，宜作「一个多世纪」）。改法：「一门靠鳄皮、在黑暗里养大鳄鱼的百年生意」，或直接删去「与阳光」。

### C-11-7 跨章全称预告无取证：「后文每当她咽下一次火，都会给出一笔账」
- md:46（block 3 读者视角提示）：**「后文每当她咽下一次火，都会给出一笔账」**
- 判定：这是对后 38 章叙事手法的**全称**预言，未经取证（本次深审尚未跑到后章）。同句的「画面、掐灭、转成安慰」有本章凭据（:60／:63／:69）✓，可保留；只有「每当…都会」需处理。改法：「本章给了这笔账：eager to console her，要证明自己是宽容的人（:69）」，把全称改为本章实证。

### C-11-8 承重信息缺失：派对当晚的天气与 Virginia 的酒
- md:10／md:11／md:12 三处都提到「夏至派对」，但没有一句带出这条：
- 原文逐字：`text/ch11_chapter_ten.txt:78` — `Somehow, the weather always behaves around the house the evening of.` 与 `Every year I swear I’ll never drink again, yet I find myself downing hurricanes soon as the first guest arrives.`
- 判定：`the weather always behaves` 是本书超自然线索库里的一条（带 Somehow 对冲，正是不裁决项），md 全篇不提，读者就少一根与 ch07 门外声、ch09 水面显形并列的梁；第二句还给出 Virginia 的年度失态，与她在本章「急切前倾／把手抽回」的自我管理构成对照。⇒ 按「整块信息单元缺失」判阻断。改法：md:10 或 md:11 补一句「派对当晚房子一带的天气『总是配合』（Somehow 是原话自带的对冲），而她年年发誓不喝、年年一开席就灌 hurricanes」。

## 🟡 提示（9）

- **T-11-1**「从轻松的**下午茶**色调起步」：本章是早餐（:9 台面自助餐、:12 冰茶），且 md:10 自己写「温室早餐桌上」。建议「早餐的闲适色调」。
- **T-11-2**「Gazzie 的签名是她仿的」被写成坦白的内容：Virginia 本人只说 `“After a life in the same house, you get to know a person’s signature pretty well.”`（:51），`She’d forged it. Lied.`（:54）是 Dart 的补完。建议标为「Dart 由此认定」。
- **T-11-3**「而人选里有外人 Harrison」：:87 是 Virginia 心里有「别人」，:108 是「外人继承她受不了，连 Harrison 也不行」，:114 才是 Dart 推出 Harrison＝内定继承人。原文不是一个并列候选名单，而是「Gazzie 已选（外人）／Virginia 想换」。
- **T-11-4**「正中 Virginia 姨妈**暗中的**期盼」抹掉了 :30 的 `Apparently,`（叙述者的读取标记）；与她 :21 的 hint of a smile、:27 的 leaning forward eagerly 并置才是凭据。同族：ch09 C-09-1。
- **T-11-5** md:54「分号后的**自我更正**最狠」：分号后是把她与 Gazzie 归并（`he, like Gazzie, had assumed`），不是更正；后半句「把 Harrison 与 Gazzie 并成一类」本身正确。
- **T-11-6** md:54「回头把**先前每桩疑点**重新归档」：这条推论只收编三桩（逗留／倚重／敌意）；摄像头（ch08:33/:87）、通电围栏（ch08:114）、红牌（ch08:21）、农场正在闹的事（ch08:42-:57）都不在其中。
- **T-11-7** md:34「Virginia 布局时假定重聚必然发生，信只负责修路」：漏掉原文 actually 的反事实色（重聚从未发生，见 C-11-1 的 ch02:107）；「更冷的一层」因此站得太实。
- **T-11-8** md:24「被**同一株**蔫植物串上」：原文是 `fingering another wilting plant`（:9）——another 至少给出第二株，而她先浇的那盆非洲堇是好的；「同一株」丢掉了这层计数。另：本章 md 未列派对清单本身（弦乐四重奏演奏 Jimmy Buffett／pigs in blankets／caviar／有时整猪烤肉／总是很多酒，:78）与 Dart 的碎花裙幻想（:81），仅以「派对清单」四字带过，属轻漏。

- **T-11-9** 漏 `text/ch11_chapter_ten.txt:12` 的场景约束与自陈：`I should have asked her the questions Gazzie wouldn’t answer about the farm and the ominous words in Mama’s closet, but I didn’t want Gazzie to overhear and freeze me out again.`——两点在 md 里没有落点：①这场早餐是在 Gazzie 听得见的屋内进行的（本章的空间约束），②她明知该问农场与衣橱上的字却主动不问（md:13 只写了「想多与她相处」的正面动机，漏掉这条回避）。轻漏。

## ⬜ 判为假红／不报警（9）

- **F-11-1** md:44「it 选的是刚才还在被欣赏的那株红色凤梨花」——:12 `I absently admired a red bromeliad` → :60 `My eyes fell on the bromeliad`（定冠词同指）✓ 正确。
- **F-11-2** md:44「could 而非 would 留着分寸」＋「紧跟的 `I froze, blinked away the image` 由讲述者自己把这帧画面掐掉；引语停在实施之前」✓ 与 :60→:63 行序一致。
- **F-11-3** md:54「结论先在上一句钉死——他才是内定的继承人」✓ :114 段内 `So he was Gazzie’s heir apparent.` 确在三个 No wonder 之前。
- **F-11-4** md:14「皮肤发麻、手指发痒、胃往下沉」三处逐字对应 :36／:60／:114 ✓。
- **F-11-5** md:12「让开篇的信（称 Gazzie 不查邮箱）露出第二双手」✓ 与 :54 一致。
- **F-11-6** Virginia「她第一次一起吃饭时提过这事」有前章凭据：`text/ch06_chapter_five.txt:285` — `“A long-lost granddaughter shows up a month before I name my heir…”` ✓（md 未展开，故不另报）。
- **F-11-7**「三个 No wonder」数量正确 ✓；md:56「这是 Dart 单方面替 Harrison 想的，不是 Harrison 说的」正确——Harrison 本章不出场、无台词。
- **F-11-8** md:13「不必再拖着坏身体抢安全感」对应 :102 `run my poorly functioning body into the ground for security` ✓（未据此断言她患有何种病，处理正确）。
- **F-11-9** md:11「在坦白处跌进愤怒与羞耻的拉锯（想砸盆、又抢先安慰对方）」✓ :60／:69 顺序与措辞均对。

## 逐块对应（R4）

- block1（:9）关键词 sensitive／wilting／fingering／damn 全在引语内 ✓；中文理解逐句对应 ✓；「铁框玻璃把佛罗里达挡在外面」对应 :9 `framed by a combination of intricate wrought iron and glass windows` ✓；**「她母亲」未被写成 Ida** ✓（本章只给 built by her mother，身份未列）。
- block2（:54）关键词 letter／claimed／get ahead of／reunited ✓；中文理解「先把这句谎话安置到位」对 `get ahead of the lie` ✓；「Greer 这一家人」对 `the Greers` ✓。
- block3（:60）关键词 itching／hurl／terracotta／shatter ✓；中文理解「炸成一千片锋利的碎片」对 `shatter into a thousand sharp pieces` ✓；落点「颧骨」对 `against her cheekbone` ✓。
- block4（:114）关键词 No wonder／relied on／dislike／inheritance ✓；「头一天他在宅子里逗留」对 `linger at the house that first day` ✓（首日均在 ch05，指认一致）；「天知道在闹什么」对 `whatever the hell was going on` ✓；「并不全错」对 `he wasn’t entirely wrong` ✓。
- 全章无 cliffhanger 收尾（收在「你明天开始」:132），md:14 未误称悬念 ✓。
