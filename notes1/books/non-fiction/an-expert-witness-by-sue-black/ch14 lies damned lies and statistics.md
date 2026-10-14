---
状态: 未读
modified: "2026-09-22"
---

# 14. 谎言、该死的谎言与统计学：概率、检察官谬误与三位母亲（精读分析）

## 概览

- **出处**：*An Expert Witness* by Sue Black，Chapter 13 "Lies, damned lies and statistics"
- **作者**：Sue Black（法医人类学家、解剖学家）
- **章节定位**：全书"方法论内核"章——把前三章反复出现的"统计地基"问题正式立为题面：先讲清 probability 与 likelihood ratio 的区别、0–1 概率谱与"可量化错误率"的铁律，再以三桩"统计学压倒常识"的标志性冤案（英国 Sally Clark 与 Meadow 医生、荷兰 Lucia de Berk、意大利 Daniela Poggiali）解剖"检察官谬误"与"德州神枪手谬误"，收束于仍在审理、争议巨大的 Lucy Letby 案——一桩"没有 CCTV、没有口供、没有物证、只有专家意见"的审判；终以 RSS 2022 报告七条建议与"问一位合格统计学家"的朴素药方作结
- **字符数**：约 53,000
- **一句话主旨**：统计学既是鉴定科学离不开的骨架，也是最容易被滥用的凶器——它不能告诉你被告是否有罪，只能给"最可能的解释"加权；一旦把"证据在有罪假设下的概率"偷换成"有罪假设在证据下的概率"，73 万比 1、3.42 亿比 1 这样的天文数字，就能把三位无辜母亲和一名清护士送进监狱。

**结构**：
- 题记：Ronald Coase——把数据拷问足够久，它什么都会招认
- 科学家的宿命：躲不开统计；不会用概率为解读辩护，就别上证人席
- 术语之辨：probability（基于模型）vs likelihood ratio（模型对已观测数据的解释力）
- 0 到 1 概率谱：0.1=10%、0.5=各半；"没有可量化错误率的方法不配上庭"
- 抛硬币例：公平硬币的正反面概率 vs 二十次只出四面时"硬币有偏"的似然更高
- DNA 例外之思：十亿分之一 × 全球 80 亿 = 约 8 人同谱；同卵双生 1/250 出生
- 手相研究的算数：双手≠百分百、断肢更具区分力、左撇子、疤痕分布、静脉 99% 不完全匹配
- 统计入庭的审慎：作者坦承唯一一次"无完整数据集"出庭是阴茎静脉案，因能解剖学排除而"站在安全地带"
- 医学数据最易翻车：新冠疫情把统计学家推上发布台、政客也读不懂数据
- RSS 2015 设委员会、2022 出报告《连环杀手还是巧合？》
- Meadow 登场：权威儿科医生、Munchausen by proxy 命名者、Allitt 案奠基庭上声望
- Meadow's Law：一死是悲剧、二死可疑、三死在未证清白前即谋杀；作者判"不知从哪开始纠正"
- Sally Clark 案（1999）："7300 万比 1"、Grand National 连中比喻、陪审团偏爱魅力专家 →  majority 有罪
- 统计学反击：RSS 公开信、独立性假设错误、检察官谬误（四腿与马之喻）、双 SIDS vs 双杀 5:1
- 平反与代价：2003 上诉撤销、Clark 服刑四年出狱、2007 酒精中毒离世；另三案（Anthony/Cannings/Patel）连锁翻案
- 赔偿之账：2016–2024 五百余申请仅一百余受理、均赔不足一万八千英镑；2023 废除生活费扣减
- de Berk 案（荷兰）：一条不靠谱的纱布血检 + "3.42 亿比 1" + 非统计专家的犯罪学者 → 2010 完全平反
- Poggiali 案（意大利）："死亡天使"标签、竖大拇指照、轮值表假相关 → "Mickey Mouse 统计"、德州神枪手谬误
- 相关性 ≠ 因果性；RSS 七条建议（用合格统计学家、报 p 值与效应量、双盲、识别混杂因素）
- Letby 案（2023）：无 CCTV / 口供 / 物证、辩方竟未请医学与统计专家、退休超十年的控方专家"主动请缨"
- 魔眼立体画之喻：盯久了图案自现、"我当初怎么没看见"——确认偏误的可视化
- 收尾：老律师批医生专家"傲慢 + 缺统计地基"；引 M. Scott Peck"人是蹩脚的检验者"；寄望 AI 去偏但警惕 GIGO

**段落脉络**：

| 段落群 | 内容 | 功能 | 支撑什么 |
|------|------|------|------|
| 立规 | 概率是鉴定科学的骨架 | 定义学科纪律 |
| 术语 | 概率与似然之比的分野 | 破除混用 |
| 硬币例 | 有偏与公平的似然高下 | 让抽象可感 |
| 铁律 | 无错误率者不配上庭 | 准入门槛 |
| 医学之危 | 数据解读最易翻车 | 圈定高风险域 |
| Meadow | 权威越界、以修辞代数据 | 全章头号反面案例 |
| Clark | 七千三百万比一的杀伤 | 冤案标本 |
| 反击 | 统计学拆穿检察官谬误 | 纠错机制 |
| 代价 | 出狱三年后离世、赔偿吝啬 | 制度之耻 |
| 跨国 | 荷兰意大利同错复现 | 谬误的普遍性 |
| 神枪手 | 先画靶再开枪 | 认知根源 |
| Letby | 只有一侧专家意见的审判 | 未决的活标本 |
| 药方 | 问合格统计学家 | 朴素收束 |

**核心金句**：
> "Everything we do has to be wrapped up in probability; every method we use must have a quantifiable error rate."

> "It is powerful, it is beguiling and it is dangerous."

> "Human beings are poor examiners, subject to superstition, bias, prejudice and a profound tendency to see what they want to see rather than what is really there."

## 论证结构

**核心论点**：概率与似然是鉴定科学唯一能言说"确定性"的语言，正因如此，它也是最危险的武器——它能把"证据有多不支持无罪"偷换成"被告几乎一定有罪"（检察官谬误），能把随机聚集看成犯罪铁证（德州神枪手谬误）。作者用 Sally Clark、Lucia de Berk、Daniela Poggiali 三桩翻案冤狱证明：压垮正义的往往不是坏科学，而是"权威 + 修辞 + 一个吓人的天文数字"的化学反应——魅力专家的一句"三死即谋杀"、一张 7300 万比 1 的算术、一则轮值表，就足以让陪审团"关掉大脑"。因此她的处方朴素到近乎冒犯：当任何人（医生、警察、律师、她自己）对统计心里没底时，去问一位合格的统计学家；而真正的科学诚实，是像她那样公开承认"唯一一次没带完整数据上庭"并说清当时为何仍安全。

**证据链**：

| 证据 | 类型（案例/研究/数据/类比）| 支撑什么 |
|------|------|----------|
| 抛硬币二十次仅四面 | 类比 | 概率与似然的分野 |
| 十亿分之一乘全球八十亿 | 数据 | 再小概率也有"撞车"者 |
| 断肢比双手更具区分力 | 数据 | 特征越稀有越有鉴定价值 |
| 萨利·克拉克案七千三百万比一 | 案例 | 独立性假设之错 + 魅力专家的杀伤 |
| 四腿与马之喻 | 类比 | 检察官谬误的通俗解剖 |
| 双婴儿猝死比对双杀五一比 | 研究 | 凶案比双发巧合更罕见 |
| 荷兰案三亿四千二百万比一 | 案例 | 非统计专家造出的伪证据 |
| 意大利案轮值表假相关 | 案例 | 相关性被误当因果 |
| 德州神枪手先画靶 | 类比 | 确认偏误的认知根源 |
| 英国六案仅一百余获赔 | 数据 | 制度对冤狱的吝啬 |
| 莱茨比案仅一侧专家 | 案例 | 活案复现同一谬误结构 |

**论证脉络**：
立规（统计是骨架）→ 释义（概率 vs 似然）→ 铁律（无错误率不上庭）→ 转向（医学数据最易翻车）→ 头号反例（Meadow / Clark）→ 纠错（统计学 + 检察官谬误）→ 代价（死亡 + 赔偿吝啬）→ 跨国复现（荷兰 / 意大利）→ 认知根源（神枪手）→ 制度回应（RSS 七条）→ 活标本（Letby）→ 药方（问统计学家 / 警惕 GIGO）

**可质疑处**：
1. 作者把 Letby 案与 Clark / de Berk / Poggiali 三桩已翻案的冤狱并置，反复强调"三案结构相同"（无硬证据、统计滥用、辩方缺专家），并在结尾明说"我怀疑她是否得到公正审判"。但她同时声明"我对她有罪无罪没有立场"——这个分寸在修辞上很难两全：把一桩尚在法律程序中的定罪，与三桩"最终被证明清白"的冤案放进同一叙事框架，本身就构成一种暗示。相较之下，她对 Meadow 是"事后盖棺"（已平反），对 Letby 却是"未审先叙"，方法的说服力恰建立在它承认自己不下结论，却已铺满结论的轨道上。
2. 全章把 Meadow 的"7300 万比 1"定为统计学犯罪，理据扎实；但作者对"错误率/概率"的绝对推崇（"没有可量化错误率就不配上庭"）与本章另一诉求——RSS 建议之六"识别混杂因素并量化其影响后方可归因"——之间存在张力：许多临床与法医学现实（如某死因是否可疑）本就没有干净的"错误率"可报，若严格到"无量化即排除"，可能把大量本应存疑的、连"双 SIDS 是否独立"都无从精算的问题一并挡在庭外，而这既是保护，也是一种对"科学可及性"的高估。
3. 结尾把"去偏见"的希望寄托于 AI / 机器学习，与前文"人是蹩脚检验者"衔接自然；但整章的冤案恰恰多是"人算错了数"，而非"人带了偏见"——机器能纠正算术谬误，却未必能纠正"先画靶"的动机性推理（作者自己点出的德州神枪手）。用 GIGO 一句收住乐观，分寸尚可，但"AI 或成统计学偏见的解药"这一展望，与本章"权威 + 修辞"才是祸根的诊断为界尚浅。

## 选择性精读

> **原句 1:** ‘If you torture the data long enough, it will confess to anything.’

**中文理解**：题记引经济学家科斯："只要你对数据逼供得够久，它什么都会招认。"

**句子结构**：If 条件句；torture the data 是拟人化的核心隐喻（把数据当受审者）；confess to anything 承接"逼供"意象——刑讯之下无人不招。

**关键词**：torture / data / long enough / confess / anything

**表达方式**：一句警句式反讽——用司法"刑讯逼供"的意象，讽刺统计滥用；与本章"法庭"语境严丝合缝。

**为什么这样写**：题记即全章判词。科斯是经济学家（又一次"他山题记"，延续 Namdeo / Oates / Gates 的节奏），一句话把"数据不会说谎、但会被屈打成招"讲透。torture / confess 的司法隐喻精确预告本章三桩冤案的共性：Meadow 从有限的 SIDS 观察"逼"出 7300 万比 1、荷兰非统计专家"逼"出 3.42 亿比 1——数据没变，变的是拷问它的手法。它也立起作者全章的姿态：她自己反复声明"不敢在数据成熟前出庭"，正是对"别逼供数据"这条自律的践行。题记用一句关于"证词可信度"的话，开篇就把统计学和它最古老的罪行——屈打成招的假口供——钉在一起。

---

> **原句 2:** For a scientist, there can be no escaping statistics. And there is no way a forensic expert should ever contemplate stepping into the witness box if they cannot justify their interpretation of the evidence in the light of probability.

**中文理解**：对科学家而言，统计学无所逃于天地之间。而一个法医专家，若不能在概率的光照下为自己的证据解读辩护，就压根不该动走上证人席的念头。

**句子结构**：第一句 there can be no escaping statistics 双重否定表绝对义务；第二句 there is no way + 主语从句（a forensic expert should ever contemplate stepping into the witness box）+ if 条件从句（cannot justify their interpretation... in the light of probability）。

**关键词**：no escaping / no way / contemplate / justify / interpretation / in the light of probability

**表达方式**：两道"绝不"叠加成职业律令——no escaping（逃不掉）、no way（不可以），把统计从"工具"抬升为"资格门槛"。

**为什么这样写**：这是全章的宪章式开篇——作者用两个绝对否定句，把"懂统计"从加分项改写成准入资格。in the light of probability 这个介词短语是钥匙：不是说"要给出概率结论"，而是"你的任何解读都要在概率的光下经得起追问"。它呼应第 3、4 章 DNA / 手相反复强调的"没有统计基，识别就只是情报"——本章把这条暗线正式升为明规则。这也是全书对 expert witness 的核心定义之一：专家的权威不来自头衔（这正是 Meadow 的教训），而来自能否在法庭把"我为什么这么判断"的概率链条讲清。开篇即把本章的靶子（权威越界）立了起来。

---

> **原句 3:** Every time I open my mouth in a courtroom to utter the words ‘probability’ or ‘likelihood’, I notice jurors’ eyes glazing over. You can almost see them switching off.

**中文理解**：每次我在法庭上一开口说出"概率"或"似然"这两个词，就注意到陪审员的眼神涣散。你几乎能看见他们的大脑"关机"。

**句子结构**：Every time 时间从句（I open my mouth... to utter the words）+ 主句（I notice jurors’ eyes glazing over，notice + 宾语 + 现在分词）；第二句 You can almost see them switching off，see + 宾语 + 分词，泛指 you。

**关键词**：open my mouth / utter / probability / likelihood / eyes glazing over / switching off

**表达方式**：自嘲式场景速写——eyes glazing over（眼神发直）、switching off（关机）两个生理隐喻把"听众放弃理解"写得活灵活现。

**为什么这样写**：这是全章真正的问题所在——不是统计太难，而是"统计 + 法庭"这个组合天然失灵。作者用第一人称的挫败感，点出专家证人的核心困境：她明知概率是唯一诚实的语言，可这门语言一出口，裁决者就"关机"。glazing over / switching off 的比喻极准——陪审团不是听不懂一个词，而是整条认知链路断电。这句为全章所有冤案提供了心理学地基：当 7300 万比 1 砸进一群已"关机"的耳朵，留下来的不是理解，而是"这个数字好大、被告人一定很可疑"的直觉。Meadow 的可怕恰在于他懂得如何用 Grand National 的比喻去"重启"陪审团——只不过重启的是偏见。

---

> **原句 4:** If we forget that, and start mistaking our opinion for fact, we risk beginning to believe in the myth of our own infallibility. We have seen where that can lead with the trouble caused by misidentification of fingerprints.

**中文理解**：如果我们忘了这一点，开始把自己的意见误当成事实，就有滑向"相信自己绝无谬误"这一神话的危险。指纹误认所酿成的麻烦，已经让我们见过这条路通向何处。

**句子结构**：If 条件从句并列两动词（forget that / start mistaking our opinion for fact）+ 主句 we risk beginning to believe in the myth of our own infallibility；第二句 We have seen where that can lead 回指前文他章指纹误认案。

**关键词**：mistaking / opinion / fact / risk / myth / infallibility / misidentification

**表达方式**：opinion→fact→myth→infallibility 的四级滑坡——用一条"自我神化"的下坠链，把统计学焦虑升维成认识论警告。

**为什么这样写**：这是全章从"技术"跃到"心性"的枢纽句。作者真正警惕的从来不是算错数，而是"算错之后还自认不会错"——infallibility（无误）这个神学色彩的词被刻意用来形容专家的心理越界。mistaking opinion for fact 一句精准刺向 Meadow：他把"三死即谋杀"的个人假说（opinion）当作了庭上事实（fact）。而"We have seen where that can lead"是全书的互文钩子——把本章的统计自负，钩回指纹章的"确定性神话"，暗示所有鉴定分支犯的其实是同一个错误：忘记自己站在 0 与 1 之间的概率地带，却装作手握 1。这句因此是第 13 章"永不说 unique"的同一条律令的另一面表述。

---

> **原句 5:** ‘One sudden infant death is a tragedy, two is suspicious and three is murder until proven otherwise.’

**中文理解**：一次婴儿猝死是悲剧、两次可疑、三次在未自证清白之前就是谋杀——这就是所谓的“梅多定律”。

**句子结构**：三段递进排比（One... a tragedy / two... suspicious / three... murder）；until proven otherwise 是法律短语（除非另有证明），此处被嫁接到统计直觉上、制造伪严谨感。

**关键词**：sudden infant death / tragedy / suspicious / murder / until proven otherwise

**表达方式**：格言体的危险——1-2-3 的递进节奏像常识、像箴言，实则把举证责任彻底倒置。

**为什么这样写**：这就是梅多定律的原文，全章最锋利的一把凶器，也是“数据被拷打到招供”的活标本。它的杀伤力不在数字，而在形式：三行排比朗朗上口、貌似符合直觉，让“孩子死得越多越像谋杀”这种朴素恐惧获得了“科学定律”的外衣。until proven otherwise 四字尤为阴险——它把无罪推定反转为“三次死亡即推定谋杀、母亲自证无辜”，恰好与后文 2014 赔偿法“须证明清白”的倒置举证形成跨章回响。作者随后痛批这两句话从科学和统计上看错得太多，简直不知从哪儿纠正起，又指出这条口诀未必是他的原创——但她特意让这句“格言”独立成块，正是要读者亲眼看看：一句修辞优美的伪常识，如何在法庭上把三位母亲送进监狱。

---

> **原句 6:** For the less mathematically minded, the RSS have helpfully likened conflating these two separate issues to thinking that the probability of an animal having four legs if it is a horse is the same as the probability that an animal is a horse if it has four legs.

**中文理解**：为了数学感不强的人，皇家统计学会贴心地把"混淆这两件不同的事"比作：以为"如果一匹动物是马、它有四条腿的概率"，等于"如果一种动物有四条腿、它是马的概率"。

**句子结构**：For the less mathematically minded 受众状语；likened A to B（A=conflating these two separate issues，B=thinking that... 长宾语从句）；B 从句内嵌两个 if 条件对照（four legs if it is a horse vs a horse if it has four legs），靠词序颠倒制造对照。

**关键词**：mathematically minded / likened / conflating / four legs / if it is a horse / probability

**表达方式**：用一个荒诞的"四条腿≠马"类比重锤抽象的"检察官谬误"——把 P(证据|假设) 与 P(假设|证据) 的混淆变得一眼可辨。

**为什么这样写**：这是全章概念高潮的通俗化操作。"检察官谬误"的抽象表述（把证据在有假设下的概率，当成假设有证据下的概率）几乎无法向陪审团讲清，RSS 却用"四腿的动物都是马吗"一句话让它原形毕露——狗、牛、桌腿都四条腿。作者特意标注“for the less mathematically minded”（为了数学感不强的人），正呼应第 3 句陪审员“关机”的困境：她清楚这套东西必须翻译成生活语言才可能在庭上存活。而这个比喻也精确回扣 Sally Clark 案——"两死在同一家庭的概率极低"不等于"这家人杀子的概率极高"，正如"马有四腿"不等于"四腿即马"。这是本章把"数学"交还给"常识裁判"的关键一击。

---

> **原句 7:** The prosecutor’s fallacy was summed up by the RSS as ‘a seductive and widespread mode of reasoning, affecting the general public, the media, lawyers, jurors and judges alike’. It is powerful, it is beguiling and it is dangerous.

**中文理解**：皇家统计学会把"检察官谬误"总结为"一种诱人且普遍的推理方式，从公众、媒体到律师、陪审员、法官无一幸免"。它强大、它迷惑人心、它危险。

**句子结构**：第一句被动（was summed up by the RSS as + 引号同位语，引号内 affecting... 分词 + 五类人群并列）；第二句 It is powerful, it is beguiling and it is dangerous——三个主系表短句排比递进。

**关键词**：prosecutor’s fallacy / seductive / widespread / mode of reasoning / beguiling / dangerous

**表达方式**：三"it is"的渐强三连——powerful（能力）→ beguiling（诱惑）→ dangerous（后果），像给一种病毒写诊断书。

**为什么这样写**：这是全章对"头号反派"的正式判词，三短句的节奏本身就是修辞武器。作者借 RSS 之口点出关键：检察官谬误不是外行的专利，它" affecting... lawyers, jurors and judges alike"——连法律专业人士都中招。beguiling（迷人）一词最要命，呼应题记"逼供数据"：数据之所以能被屈打成招，是因为招来的假口供"太有说服力、太好用了"。这三连排比精确概括了本章三案：Meadow 的 7300 万比 1（powerful）、de Berk 的 3.42 亿比 1（beguiling）、Poggiali 的轮值表（dangerous）。它也解释了为何纠错如此迟缓——要一个人抵抗一种"让他显得更聪明"的推理，比抵抗一个数字难得多。

---

> **原句 8:** An association does not indicate a causation. The statisticians successfully distanced causation from correlation in these cases – a complex matter beyond the expertise of most medical doctors, pathologists or indeed anthropologists.

**中文理解**：相关并不意味着因果。统计学家在这些案子里成功地把"因果"从"相关"中剥离出来——这是一个复杂的课题，超出了大多数医生、病理学家、乃至人类学家的专业边界。

**句子结构**：第一句极简格言（An association does not indicate a causation）；第二句 distanced causation from correlation 用"拉开距离"的空间动词讲概念分离 + 同位语 a complex matter beyond the expertise of...（三类专业人士并列，indeed 递进到"连人类学家=作者自己也不 exempt"）。

**关键词**：association / causation / distanced / correlation / beyond the expertise / anthropologists

**表达方式**：用"把因果从相关里拉开距离"的空间隐喻，讲一个统计学最古老、也最常被违反的区分。

**为什么这样写**：这句是全章三案共同的病理学诊断书。Poggiali 的"总在值班时死亡"、de Berk 的"总在上班时出事"、Clark 的"同一家两死"——全是 association（相关），却被逐一当成了 causation（因果）。作者的高明在句尾自我卷入：beyond the expertise of... indeed anthropologists——她把自己这类专家也划进"会犯此错"的范围，兑现了第 4 章 DNA、本章反复要求的"专家须懂自己专业的边界"。这句也补全了"德州神枪手谬误"的定义：先看到弹孔聚集（相关），再画靶宣称神准（因果）。它把本章从"批判 Meadow 个人"提升为"批判一种人类通用的认知缺陷"。

---

> **原句 9:** There were no witnesses who saw anything happen. No CCTV. No confession. No forensic evidence – actually, no hard evidence at all. Just the opinions of the expert witnesses.

**中文理解**：没有目击者看到任何事发生。没有监控。没有口供。没有法医物证——准确说，什么硬证据都没有。只有专家证人们的意见。

**句子结构**：四句省略式排比（No witnesses... / No CCTV / No confession / No forensic evidence）逐句砍掉主语谓语、只剩 No + 名词，营造清点式的缺失；破折号后 actually 修正升级为 no hard evidence at all；末句 Just the opinions... 用 just 收在唯一的"剩余物"上。

**关键词**：witnesses / CCTV / confession / forensic evidence / hard evidence / opinions

**表达方式**："排除法"清单——把一桩谋杀案"本该有的证据"一件件划掉，直到只剩"意见"，制造强烈的空缺感。

**为什么这样写**：这是全章对 Letby 案最冷峻的一段白描，也是"检察官谬误"能大行其道的结构性前提。作者用四个 No 把现代刑侦的所有锚点（目击、监控、口供、物证）逐一清空，只剩"专家意见"——而这恰恰是统计谬误最容易滋生、最难以反驳的真空地带。它回扣第 13 章"没有可量化错误率的方法不配上庭"：当只剩意见、没有硬证据，任何"3.42 亿比 1"式数字就失去了被物证校验的可能。末句 Just the opinions 的 just（仅仅）是毒针——一个可能被终身监禁的案件，承重墙竟只是"意见"。这段与作者声明"我对其有无罪不持立场"并置，构成了本章"未审先叙"的修辞张力（见可质疑处 1）。

---

> **原句 10:** Juries may find statistics dull, but they are such an important tool for good when harnessed with expertise and accuracy, and such a blunt instrument, leaving misunderstandings and destruction in their wake, when wielded with clumsy inexperience.

**中文理解**：陪审团或许觉得统计学枯燥，但用在正道上，它是一件威力巨大的工具——前提是被专业与精确驾驭；而一旦被笨拙和外行挥舞，它就成了一件钝器，身后只留下误解与毁灭。

**句子结构**：Juries may find statistics dull 让步；but 转折接两个 such... when... 对称结构（such an important tool for good when harnessed with expertise and accuracy / such a blunt instrument... when wielded with clumsy inexperience）；现在分词 harnessed / wielded 分别搭配"驯马"与"挥器"两套工具隐喻。

**关键词**：dull / tool for good / harnessed / blunt instrument / wielded / clumsy inexperience / in their wake

**表达方式**：一件工具的两副面孔——同一把"统计"，harnessed（套上缰绳善用）则造福，wielded clumsily（胡乱挥舞）则酿祸；双隐喻对照收束全章。

**为什么这样写**：这是全章的判词式总结，把整章三案 + 一个活案蒸馏成一句关于"使用方式"的中庸论。作者没有妖魔化统计学本身——她立场一贯：统计是骨架、是"正道利器"（呼应开篇"逃不掉统计"）；真正的恶，来自"clumsy inexperience"（Meadow 越界做统计、荷兰犯罪学者用本科水平算 3.42 亿比 1、Letby 案辩方干脆没请统计学家）。blunt instrument / in their wake（在其身后留下）是全书反复出现的"证据被误用即凶器"意象的又一次兑现。这句为结尾"问一位合格统计学家"的药方铺平了道路：工具无过，过在无缰绳——而 RSS 七条建议、双盲、效应量报告，正是给这匹烈马套上的缰绳。

## 词汇分级

### ⭐⭐⭐ 高级

| 词/短语 | 释义 | 例句 |
|------|------|------|
| infallibility | 无误、绝不出错（常含贬义的自负） | we risk beginning to believe in the myth of our own infallibility |
| quantifiable | 可量化的 | every method we use must have a quantifiable error rate |
| pivotal | 起决定作用的、关键的 | sometimes they will prove pivotal for the opposing legal team |
| cast-iron | 铁板钉钉的、不容置疑的 | since there is very little in forensic investigations that can be a cast-iron certainty |
| infinitesimally | 无穷小地、微乎其微地 | the chance of the coin landing on its edge is infinitesimally small, but it is not zero |
| discriminatory | （此处褒义）具区分力的、可辨异同的 | The loss of a limb is therefore obviously more discriminatory, in terms of identification |
| ambidextrous | 左右手皆灵巧的 | a very small percentage, below 1 per cent, are genuinely ambidextrous |
| aetiologies | （aetiology 复数）成因、病因来源 | the more corresponding anatomical features arising from different aetiologies we can find |
| beguiling | 蛊惑人心的、诱人的 | It is powerful, it is beguiling and it is dangerous |
| exonerated | 被洗清罪名的 | She was fully exonerated, and the case is regarded to this day as one of the biggest miscarriages |
| circumstantial | 间接的、环境证据的 | All the evidence against her was circumstantial |
| relinquish | 放弃、交出（头衔/权利） | Meadow relinquished his registration with the GMC in 2009 |
| cause célèbre | 轰动一时的争议案 | Once a case becomes a cause célèbre and the media start clamouring for justice |
| confounding factor | 混杂因素（干扰因果推断的变量） | Possible confounding factors must be identified, and their effect quantified, before attributing causes |

### ⭐⭐ 进阶

| 词/短语 | 释义 | 例句 |
|------|------|------|
| rearing its ugly head | （坏事）冒头、作祟 | if it doesn’t, it shouldn’t be rearing its ugly head in court |
| crash and burn | 惨败、彻底失手 | I have seen for myself expert witnesses crash and burn when their statistics were based on insufficient data |
| cul-de-sac | 死胡同 | statistics are a favoured bait for luring you down a cul-de-sac |
| flying too close to the sun | 自负越界（伊卡洛斯典故） | we still see overly confident experts flying too close to the sun |
| fall from grace | 失势、身败名裂 | His fall from grace was brought about not by failings in his own specialism |
| cemented | 巩固、坐实（名声） | It was Meadow’s evidence in the Allitt case that cemented his reputation in the courtroom |
| wake-up call | 警钟 | It was a wake-up call for scientists that we needed to be more cautious |
| demonized | 被妖魔化的 | Poggiali was demonized by the press |
| bandwagon | 跟风、一哄而上 | the talk of thirty-eight unexpected deaths launched a convenient bandwagon for everyone to jump on |
| scapegoat | 替罪羊 | preparing the ground for a scapegoat to be identified as the culprit |
| carte blanche | 全权、放行不受限 | It hands any defence KC carte blanche to start shouting about a gun for hire |
| tunnel vision | 管窥、只见一点的偏执 | The police and the CPS were accused of tunnel vision informed by weak science, bad statistics and confirmation bias |
| theorizing on the hoof | 边走边即兴编理论 | it looked as if they might be theorizing on the hoof and then analysing retrospectively |
| constellation of evidence | 证据“星座”（多弱证拼成图案） | Commentators criticized the much-quoted constellation of evidence |
| hypothesis | 假设、待证的解释 | You would have two hypotheses to consider: first, the likelihood of getting heads four times if the coin is fair |
| statistician | 统计学家 | I am most definitely not a statistician, and yet the success of my research depends on statistics |
| GIGO | 垃圾进垃圾出（garbage in, garbage out） | garbage in, garbage out |

### ⭐ 基础

| 词/短语 | 释义 | 例句 |
|------|------|------|
| coin | 硬币 | The example we invariably find ourselves reaching for to illustrate the distinction between probability and likelihood is the tossing of a coin |
| error rate | 错误率 | every method we use must have a quantifiable error rate, and if it doesn’t, it shouldn’t be rearing its ugly head in court |
| evidence | 证据 | The statistical evidence on which the prosecution heavily relied had been provided by a criminologist with no specialism in statistics |
| roster | 值班表、轮值名册 | all the roster really demonstrated was that Letby was probably on duty when she was believed to have been on duty |
| tariff | （无期犯最低服刑年限）量刑基准 | Letby was given a whole life order |

## 一句话总结

这一章把鉴定科学最硬核也最脆弱的神经——统计学——摊开在法庭的灯下：它是专家唯一能诚实言说"确定性"的语言，却也是最容易被权威与修辞"拷打成招"的凶器；从 7300 万比 1 到 3.42 亿比 1，压垮正义的从来不是数字本身，而是"把相关当因果、把证据的概率偷换成有罪的概率"这一人类通用的认知漏洞——因此作者的药方朴素得近乎冒犯：心里没底时，去问一位合格的统计学家。
