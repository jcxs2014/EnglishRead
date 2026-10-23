# ch16（书内 Chapter Fifteen）深审 R3/R4 三张单子

素读基线：`review/ch16/1-suread.json`（**127 条事实／0 MISS**，只读 `text/ch16_chapter_fifteen.txt`，写完才开 md）
机器层：`bash scripts/chapter.sh "ch16 aunt virginia reveals uncle leon.md"` → 退出码 0，verdict `ok`
- 引语块 8／片段 8／查无 0；块数 8 ∈ 建议 [4,8]（硬限 2–15）；words 2426；struct_bad／empty_quote／keyword_bad／cjk_low／template／hole 全 0
- `…` 拼接块：本章 8 块均为单段连续引文（`quote_long` 0），已由书级 `verify_fragments_indep.py`（313 条／443 片段／MISS 0）覆盖
- 词表：16 行例句展平逐字 **0 MISS**（`presumably` 行释义已明写「标示推断而非断言」✓）
- 字形：`'` 直撇号 **0 个**；除 frontmatter 外正文无直双引号混用

> 长章（2,426 词／8 块）形态：块层普遍扎实，红集中在**导航五句**与**读者视角提示**；与 ch13/ch14/ch15 同一风险模型，另加一条本章独有的——**跨章已建立的人物（Henri）在本章被记成「出现而不解释」**。

## 🟥 阻断（10）

### C-16-1 语法术语误称：resent 的宾语被写成「不是人」
- md:24：**「怨恨的宾语是两个动名词——隔离（"isolating"）与隐瞒（"concealing"）——而不是人，这笔账因此有精确的名目」**
- 原文逐字：`:15` — `I still resented Mama for isolating me and concealing my extended family, particularly Aunt Virginia.`
- 判定：`resented` 的直接宾语就是 **Mama**（人）；`isolating`／`concealing` 是介词 `for` 的宾语，表**控罪的内容**而非怨恨的对象。md 的「而不是人」与句子结构正相反——本章稍后 :234 她也明确把情绪指向人（`I still resented Mama`），且「精确的名目」这个洞察本身依赖"理由被写成两桩作为"，不必靠错认宾语来支撑。**连续第六章同族缺陷**（ch11 残句／ch12 单音节／ch13 习惯性将来时／ch14 宾语前置／ch15 陈述句误称「自问」／本章 宾语误认）。
- 改法：「`resented` 的宾语仍是人（Mama），但两桩控罪被装进 `for`＋两个动名词里——她恨的不是血缘身份，是可数的两项作为，这笔账因此有精确的名目。」

### C-16-2 章内时序写反：`Slips.` 在引语的上文，不是「紧接的下文」
- md:56：**「紧接的下文里，Virginia 讲到 Gazzie 偶尔『just—』然后摇头补一个 Slips。」**
- 原文逐字：`:162` — `…occasionally she just—” She shook her head. “Slips.”` → `:165` — `Relieved, I confirmed, “So you don’t think it’s real.”` → `:168` —（本块引语 `Ida—imaginary Ida—shows up when Gazzie’s stressed.…`）
- 判定：`Slips` 在 **早 6 行的上文**，且中间还隔着叙述者自己的一句松了口气的确认（:165）——这一隔正是本章的机制：她先把「不觉得是真的」听成保证，Virginia 才在 :168 犹豫着补出 `imaginary Ida`。写成「紧接的下文」既丢顺序也丢了 :165 这层。**本库缺陷簇第一名。**
- 改法：「**上文** :162 里 Virginia 说到「occasionally she just—」就摇头，只补出一个 `Slips`；中间还夹着她自己那句如释重负的确认（:165），所以 :168 的 `imaginary Ida` 是被**追加**的降级，不是顺势的解释。」

### C-16-3 悬置指代被径判：`when she was eighteen` 的 she
- md:40 中文理解：**「在 Gazzie 十八岁那年正式把农场交接给了她」**；md:12：**「一个从十八岁起就没离开过农场的人」**
- 原文逐字：`:129` — `Oh, she didn’t buy it. Our mother had it built to get away. She hated the farm, let Gazzie take over officially when she was eighteen. Only a year after Ida died.`
- 判定：本句里 `she` 可指 `Our mother`（立别墅、恨农场那一位），也可指 `Gazzie`；原文两处皆女称、无任何同位语定住。**全书 `eighteen` 只有两处**，另一处是 ch10:72 讲 Ida（`When Ida was eighteen…`），本章前后都没有第二把尺子能量出接手年龄。取证：`$ /usr/bin/grep -rn "eighteen" <书>/text/` → `ch10_chapter_nine.txt:72` 与 `ch16_chapter_fifteen.txt:129` 两条，无第三条。md 把歧义在**中文理解**里译成定年，又在导航里叠上 :135 的 `Never`（那只回答「会不会离开」，不含起点年），合成一句原文未给的「从十八岁起就没离开过农场」。
- 改法：中文理解照原文留白——「她（指代未定）十八岁那年正式把农场交给他/她接手」→ 写作「在『她十八岁』那年正式交给 Gazzie 接手；这个 she 本章未定」；md:12 删「从十八岁起」，改「一个被问到会不会离开时只答 Never 的人」。并列入**不许裁决**。

### C-16-4 指代径判＋语用读反：「把亡母数落会客的好手」
- md:13：**「礼数（把亡母数落会客的好手）」**（Virginia 的人物弧线三项之一）
- 原文逐字：`:57` — `“Not the beach,” she said… “The farm. I’ve been a bit busy this week, and I feel awful about neglecting you. Mama would have been livid. She was a wonderful hostess. Made little itineraries for her guests. Brought out the good china.”`
- 判定两处：
  1. **指代径判**：本章把 `Mama` 安成「（叙述者的）亡母」。但这一句出自 **Virginia 口中**，而她在同章 :129 称自家母亲为 `Our mother`（那位「讨厌农场」、把产业交给 Gazzie 的人）；把「会给客人做小行程表、端出好瓷器」的东道主读成 Caroline 与本章信息相左——ch07:78 明写「Something bad had driven Mama from Greer House」（她是被赶出去的那一个），本章对她也只用 `left`（:168）／`departure`（:234），**通章未说其死亡**。⇒「亡母」是双重的越权（指代＋生死）。
  2. **语用读反**：`I feel awful about neglecting you` 是 Virginia **自责**，`Mama would have been livid` 是引一位逝者立标准来责己；md 写成「数落」（谁数落谁？）既无对象也与「自责」相反。
- 改法：「礼数（以自己那位逝去的长辈立待客的规矩，反衬她这周怠慢了客人——:57，句中的 Mama 指代本章未定）」。

### C-16-5 承重缺失：把话题从客套推向 Ida 的那一拍（:138／:141）
- 原文逐字：`:138` — `She knew Greer House in and out—and had hinted that she knew what I’d seen that morning.`；`:141` — `“She didn’t seem to think I was dreaming earlier,” I said tentatively.` → `:144` — `Aunt Virginia rubbed her temples, then sucked in a deep breath, like she was bracing herself. “She believes she sees Ida from time to time.”`
- md 现状：导航与 8 块只写「Gazzie 相信自己时不时看见 Ida」这一**结论**，未写它是怎么被问出来的。
- 判定：全章最关键的一次转场（缅因别墅 → `Never` → **她主动点破早上的事** → Virginia 壮胆后才吐口）整块缺席；且 :138 的「**had hinted**」是叙述者的读法（原文从未给出 Virginia hinted 的话），这一层不落账，读者会把「姨妈知道」当实写。取证：`$ /usr/bin/grep -nF "had hinted" "<ch16 md>"` → 输出空，**退出码 1**（`/usr/bin/grep -c 正常` 亦 0）。
- 改法：块 4 的「为什么这样写」或导航补「而这条信息不是自动交代的：她先替 Virginia 记下一笔『她暗示过她知道我早上看见的东西』（:138），再试探着把话挑明（:141），对方揉太阳穴、深吸一口气——像在给自己壮胆（:144）——才给出那句判词」；并注明 `had hinted` 属她的读法。

### C-16-6 承重缺失：:147 三层（信念的出处／Haints／替 Gazzie 归因）
- 原文逐字：`:147` — `There wasn’t such a thing as a friendly ghost; people who came back from the grave were, at least according to my mother, evil spirits. Haints.` ／ 同段末 `Gazzie must have thought the face belonged to Ida; that’s why she’d been so eager to investigate.`
- md 现状：md:14 收了「坏虾致幻／看到的是真人」，md:12 只用「『鬼』从理性者嘴里第二次经手」带过。
- 判定：三层皆缺，且都承重——
  1. `at least according to my mother`：她的反鬼信念**记在母亲名下**（不是她的独立理性），与本章开头对 Mama 的怨恨（:15）同轴；
  2. `Haints` 是本书南方语汇的关键项（词表与导航均无）；
  3. `Gazzie must have thought… that’s why she’d been so eager to investigate` 是**她替外婆的旧行为补的因果**（回收 ch08/ch09 的"急切调查"），`must have`／`that’s why` 全在叙述者一侧，若不给这条，读者会以为文本确认了「Gazzie 查的是 Ida」。
- 改法：块 4 之后补一条或在 md:14 展开：「她的理性不是自立的，是继承的（:147 `at least according to my mother`），用的词还是本地的 `Haints`；而同段里她替外婆补了一条因果（`must have thought… that’s why`）——这条**是她的推断**，不是文本给的解释。」

### C-16-7 承重缺失：`Well, you know.` 与她「我什么都不知情」的错位
- 原文逐字：`:168` 末 — `Though by then, he’d— Well, you know.”`；`:180` — `“I don’t know a Leon,” I said slowly.`；`:183` — `“Caroline really didn’t tell you anything,” she said, unable to hide the hurt in her voice.`
- md 现状：md:10 写「谈崩处掉出一个 Mama 从未提起的弟弟 Leon」；8 块引语（原句 4）在 `Her whole world tipped upside down.` 处截断，`Well, you know` 半句不在任何块、导航或词表里。
- 判定：本章的引爆点不是"掉出名字"，而是 **Virginia 假定她已知情**（`Well, you know`）而她答「我不认识什么 Leon」（:180）——这个错位才是 :183「Caroline 真的一事未告」那句受伤的直接来由；`he’d—` 的破折号是原文刻意留的悬置（Leon 到底"成了什么"），必须登记为不可裁决。取证：`$ /usr/bin/grep -nF "Well, you know" "<ch16 md>"` → 空，**退出码 1**。
- 改法：原句 4 的「为什么这样写」补「且这段话的末尾她停住了：`Though by then, he’d— Well, you know.”`（:168）——她以为这孩子知道；于是下文的 `“I don’t know a Leon,” I said slowly.`（:180）才是把 Virginia 打到「Caroline 真的一事未告」（:183）的那一击」；`he’d—` 的省略列入不许裁决。

### C-16-8 承重缺失：「这是我这辈子第一个让我觉得自己正常的地方」（:120）
- 原文逐字：`:120` — `“This is the first place I’ve ever felt normal,” I volunteered. “Most of the time, at least.”`
- md 现状：`felt normal`／「正常」在本章 md 全文 **0 命中**。取证：`$ /usr/bin/grep -nF "felt normal" "<ch16 md>"` → 空，**退出码 1**；`/usr/bin/grep -c "正常" "<ch16 md>"` → `0`。
- 判定：这是她在全章最松弛处（刚听完沙滩球段子、正被 `A real peacekeeper` 打动）主动" volunteer "出来的一句自我披露，是 :11 情感弧线所说「缓慢的松紧交替」的最高点，也是章末 Leon 一击的对照面；更要紧的是第二句 `Most of the time, at least.`——她立刻给这句加了折扣，正是本章缓冲词链（`presumably`／`tentatively`／`doubtfully`／`probably`）里最贴身的两枚。导航与弧线两处都没记 ⇒ 属**整块承重信息缺失**。
- 改法：md:11 弧线段补「她在 :120 主动交出全章最软的一句（『第一个让我觉得自己正常的地方』），随即自己把话收半步（`Most of the time, at least.`）——随后 Leon 才掉下来」；或在原句 2 之后增设一块。

### C-16-9 跨章关系漏登记：Henri 被记成「出现而不解释」
- md:36：**「Henri 出现而不解释——先记住这两个坐标。」**
- 反证逐字：`text/ch04_chapter_three.txt:234` — `“I only work part-time, which I appreciate mightily,” she continued. “My girlfriend, Henri, runs a bakery, and I have plenty of time to help her.”`
- 判定：Henri **不是**本章新出现的悬空名——ch04 里 Nova 亲口介绍过她（Nova 的女友、烘焙坊主人，因此 Nova 才只兼职）。本章 :111 的 `walking the two of us back to Henri’s house` 于是多出一层可读的关系（当年 Virginia 与 Gazzie 被送回的是这户人家；今日 Nova 在这屋里/店里的位置）；md 反向把它记成待解的空白，等于把一条已连上的线剪断。**按「进了词表≠已登记」的同类判据，跨章已建立的人物须回接。**
- 改法：md:36 改「Henri 并非首次出场：ch04:234 由 Nova 亲口介绍（她的女友、烘焙坊主人）；此处是她当年被 Harrison 坚持送回的那户人家」，并把这条关系登记进跨章清单。

### C-16-10 评价与同章反证相抵：「谈崩处掉出」
- md:10：**「而谈崩处掉出一个 Mama 从未提起的弟弟 Leon」**
- 原文逐字（同章后续）：`:198` — `“He was an artist, like you. A traditionalist. Used oils, I think?…`（Virginia 继续从容讲述）→ `:210` — `Her smile grew. “Ida’s the odd-looking doll.”` → `:213` — `A laugh slipped out of me.` → `:222` 两人一同收起毛巾、`:267` 还车后 Virginia 主动带她看 Leon 的画。
- 判定：:183／:189 确有痛感（`unable to hide the hurt`、`like she was holding back tears`），但谈话**没有崩**：之后三人共享一次笑（:213）、Virginia 还带她去看了画（:267）。把这一拍写成「谈崩」把「痛点出真相」压成「关系破裂」，与同章后半直接相抵。另 :210 的 `Ida’s the odd-looking doll.`（餐厅茶会画里 Ida 是哪个）**全篇 0 命中**（`/usr/bin/grep -nF "odd-looking" "<ch16 md>"` → 空，退出码 1）——这一识别是本段笑点的落处，也是 :267「每张的主角都是 Ida」的前哨。
- 改法：md:10 改「而讲到继承人链时失口带出一个 Mama 从未提起的弟弟 Leon——姨妈红了眼眶却把话讲完」；块 6 之前若不便增设，至少在导航的叙事手法一句里记下「:204→:210 用一句『Ida 是那个长相古怪的玩偶』把餐厅那幅画认了出来」。

## 🟡 提示（7）

- **T-16-1**（md:12）「『鬼』从理性者嘴里**第二次**经手（imaginary Ida）」——跨章计数未给第一次的出处；候选是同章之外的 ch15:87 `“Could it have been a bad dream?”`（Virginia 的合理化）。补第一次，或删「第二次」。
- **T-16-2**（md:26）「`extended family` **点明**被隐瞒的是母系这一支」——`extended family` 本身不含母系信息；判定来自Virginia/Gazzie 与 Mama 的关系（:129 `Our mother`）。改「由上下文确定是母系这一支」。
- **T-16-3**（md:34）「把『一个外姓人怎样长进**这座岛**』讲完」——:21 的 island 指她们骑车去的 Main Beach Park 所在岛；:111 的 `moved here` 未写明 here 是岛、Greer House 还是农场。勿把 here 写实。
- **T-16-4**（md:36）「判断这个人，用别人讲的段子就够」——:114 的 `Charming when he wanted to be… The kind of person I’d never be.` 四句是她自己的补写（凭她这几日的亲历），不全是段子的功劳。
- **T-16-5**（md:11／md:80／md:84／md:86）同卷两译：`gators` 在 md:11 译「短吻鳄」、在 原句 7 一线译「鼍」；本书书名级区分就是 alligator／crocodile，建议全章统一（如"短吻鳄／真鳄鱼"），并在词表或首现处点一句。
- **T-16-6**（md:13／md:11）两处微滑：①「看出姨妈**下唇紧抿**」——:234 只写 `seeing her downturned mouth`（向下撇的嘴角，未指定下唇）；②「岸上趴着不动的短吻鳄**松开一小口气**」——:255/:258 给的是认知修正（`weren’t the aggressive killers I’d assumed`）与 Virginia 的 `Nonplussed`，原文此段无"松口气"的缓和。
- **T-16-7**（md:96）「办公室与 Ida 肖像的关联**此前由 Leon 的画铺好**」——Leon 的画在原文里明写挂在**餐厅**（:204 `“They’re hanging in the dining room.”`）；把关系铺到办公室的是 :279 那份「只修原作」清单（`The collection in Gazzie’s study, the portrait in the parlor, and the painting in the farm’s front office`）。另 :282 只写 `Gazzie’s office`，与「farm’s front office」是否同一间原文未打通 ⇒ 建议改「此前铺好的是 :279 那份原作清单（含农场办公室那幅），而 Leon 的画另在餐厅——两间房的 Ida 在本章末尾合到同一道瞪视上」。

## ⬜ 判为假红（8，勿改）

- **F-16-1** md:64「`Another secret, kept from me for years` 没有主语也没有限定动词，一个压缩的名词短语」✓——:192 原文正是无动词片段；这是本库少见的**正确**句法定性，整改批不得反向改动。
- **F-16-2** md:50「破折号里的 `imaginary` 是 Virginia 的处理术」✓——该串确在 :168 的**引号内**，属角色亲口（与 ch13 的 C-13-1 判据一致，此次判对）。
- **F-16-3** md:74「对话被叙述语拆头拆尾，中间只剩关于死亡的一句」✓ :228 形态如此。
- **F-16-4** md:76「同章回城路上她自问：Nova 和 Gazzie 前几日提到的 an accident 是不是此事」✓——:234 `Had they been referring to Leon’s death?` 是真问句，「自问」在此不属句式误称（与 ch15 C-15-8 区别开）。
- **F-16-5** md:86「紧接的下文 `So they weren’t the aggressive killers I’d assumed they were`」✓——:255 确在 :252 之后，顺序正确。
- **F-16-6** md:94「三个动作（knock、crack open、close）两次落空」✓ :282 全部在原文里；`to ask about my uncle` 的目的状语亦逐字。
- **F-16-7** md:13 把 `A real peacekeeper`（:117）放进 Virginia 的弧线✓ 可保留——但 :117 全段是**叙述者的读法**（`She wanted me to inherit but didn’t want to pit…` 无引号），整改时不得升格成 Virginia 自称或他人转述。
- **F-16-8** md:24「`coldness`……Gazzie 的为人**第一次**由体感定义」经枚举无反证：`/usr/bin/grep -n "cold\|icily\|frost" <书>/text/ch0*.txt <书>/text/ch1[0-5]*.txt` 仅 ch06:132 `The silence was just as cold`（写静默，不写人）、ch06:198 `a salad piled with cold shrimp and chopped oranges`（写菜）、ch10:132 `its cold scales`（梦里的鳄）；另查 `chilly|frigid|icy|glacial|frozen` 无一指 Gazzie 性格 ⇒ 「第一次」成立，**勿删**（但建议注明取证口径只到 ch15）。
- 附：词表 16 行例句 0 MISS；本章 8 块引语在书级 313 条口径中条数不变。
