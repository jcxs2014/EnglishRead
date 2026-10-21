# 4-verdict.md · 《Don't Leave Her Alone》第 1 章 审查判定

审查员：独立审查员（仅 ch01）｜底稿链：`1-suread.json`（R1 素读）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本文件（R4/R5）
源：`text/ch01_chapter_1.txt`（7 个正文行：6 / 12 / 15 / 18 / 21 / 27 / 30，页码行 1 粘连）｜受审：`ch01 chapter 1.md`
**受审 md 版本指纹**（另一 agent 正在改写导航／一句话总结／句子结构，本表行号只对该指纹有效）：
`md5 = e3cb5bff8e140d30fc6d91a70be5ea12`，mtime `2026-10-21 13:05:45`，133 行。
**R2 原始 verdict `ok`，机器层四类 issue 全空（segment_miss/struct_bad/empty_quote/keyword_bad/cjk_low 均 0）⇒ 本章问题全部落在机器查不了的中文改写层。**

---

## 一、四组计数（先给数）

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **6 / 6 引语相符，0 错** | 机器层 6 块各 1 段 `ok:true`（pos 2 / 712 / 1641 / 3042 / 3558 / 4394）；本审查另以 flat 归一（NFKC + 弯引号/破折号归一 + 空白压缩）对**原始文件**独立取证，6/6 整串命中（len 711@2 / 938@714 / 1407@1653 / 517@3061 / 838@3579 / 1867@4418），**无 `…`、无跨段拼接、无跨章**。词汇表 **22** 条例句（⭐⭐⭐7 / ⭐⭐10 / ⭐5）逐条 flat 命中本章原文，miss=0。 |
| **对应** | **6 块：6 对应，0 不对应，0 密度不足** | 逐块看过：每块「中文理解／句子结构／为什么这样写／读者视角提示」都在讲**本块那句引语**，施事归属与原文一致（Diana 直发器 / Brisa 背诗与罢演 / Carlos 接电话 / 助教评断 / 家长笑脸）。**未见 100G ch86 那种「引语讲 A、分析讲 B」的错位，也未见 Such a Fun Age 那种「引语只截前半句」。** |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# Chapter 1` ✔（与本书 ch02–ch17 `# Chapter N` 形态一致、ch00 `# Prologue`）；导航 **4 项** = 本书众数（bookform.py 众数＝一句话概括/情感弧线位置/人物弧线/叙事手法）✔；子项 **5 项**（中文理解/关键词/句子结构/为什么这样写/读者视角提示）六块一致 ✔；块数 **6** ∈ 中位 6.0、范围 3–9 ✔ ⇒ **无偏离，不需写理由** |
| **断言** | **共核 20 条：阻断 2 / 需人判 3 / 跳过 1 / 提示 14**（提示 14 条中，**9 条属"与原文相符、仅记录"**＝V11/V12/V13/V14/V15/V16/V17/V18/V20；**5 条属"内容成立但措辞/口径待改"**＝V3/V4/V8/V9/V10） | 阻断 2 条 = **V1「粉色脚趾」**、**V2「校庆」**；需人判 3 条 = V5 / V6 / V7；跳过 1 条 = V19（词汇分档与释义未核）；机器层盲区 1 条 = V10（见「三、机器层结果与假红判定」W1）。**假红型 0 条**（机器层未报任何红项）。 |

**阻断型条数 = 2**。R3 三张单合计：**漏 0 条 / 编 2 条 / 错 3 条**（其中 2 条编与错同源，阻断去重后 2 项；第 3 条「错」判为提示型，见 V4）。

---

## 二、判定表（# | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位）

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| V1 | md 导航「叙事手法」：`用粉色脚趾被新靴子磨破这类细节，把焦虑具象化`（md:16） | `text/ch01_chapter_1.txt:15` 逐字结尾：`her too-tight new boots destroying her pinkie toes.`；`text/ch01_chapter_1.txt:27` 逐字：`Diana arrived at the Christmas play late, her pinkie toes raw.` | 原文只写 `pinkie toes`（**小趾**），**从未写脚趾是粉色**；本章颜色词只有 `white`(:6) / `golden`(:6,:30) / `beige`(:6)。md 自己却在 :52「与后文 "pinkie toes raw" 呼应」、:88「"toes soft and perfect" 与 "pinkie toes raw" 的对照」引的是 `pinkie toes raw` ⇒ **md 自述与 :16 冲突**。属凭空添加的修饰，且让「焦虑具象化」这一分析落在一个原文不存在的细节上。 | **阻断** |
| V2 | md:34「错过**校庆**演出」、md:38「错过**校庆**演出」、md:58「比她先到**校庆**」（3 处） | `text/ch01_chapter_1.txt:12` 逐字：`She couldn’t remember a Christmas when she hadn’t put off her shopping, slipped out of a family dinner, or missed a school play just to hole up and finish reviewing some absurd movie, or rush off to interview a barely relevant public figure.`；`text/ch01_chapter_1.txt:18` 逐字：`…would seemingly still beat her to the school play.`；`text/ch01_chapter_1.txt:27` 逐字：`Diana arrived at the Christmas play late, her pinkie toes raw.` | 原文事件名是 `school play` 与 `Christmas play`（学校/圣诞演出），**全书 18 章 `anniversary` 零命中**，不存在「周年庆」语义。md 自身在 :34 前半写「女儿的**圣诞演出**」、:82 写「Diana 迟到抵达**圣诞演出**」、:133 写「圣诞演出」⇒ **同一章内三处自相矛盾**；且 `校庆` 在**全书 18 个 md 中只出现在 ch01 的这 3 行**，是孤例术语。属误译 + 自述冲突。 | **阻断** |
| V3 | md:66 读者视角提示：`显示她的焦虑 partly 是社会性焦虑（fear of judgment）`（英文残留）；md:54 读者视角提示：`后文 likely 复现`；md:10 导航：`onstage 的女儿 Brisa`；md:46 中文理解：`她哭着、羞愧地 hurried 回 Balmes` | 用工具自带 `mix_ratio()` 口径实测：`md:66` **50.0%**、`md:54` 34.9%、`md:10` 21.2%、`md:46` 6.4%（`MIX_WARN = 0.35`）。`text/ch01_chapter_1.txt:15` 逐字：`So she hurried back up Balmes, teary-eyed, embarrassed.`（原文是动词 `hurried`，md 在中文句中直接留英文）；`text/ch01_chapter_1.txt:30` 逐字：`She saw the kids on stage, and the exact same shot in miniature, multiplied by one hundred, on their parents’ and grandparents’ phone screens…`（原文是 `on stage` 分写） | 属**中文层未中文化残留**，不是引语层问题（引语 6/6 逐字无误）。`md:66` 的夹杂率按工具自身口径已超 35% 阈值，但 `check_chinese_layer.py` **只对「中文理解／为什么这样写」跑 `mix_ratio`**，对「读者视角提示／表达方式」只查「整段是否英文」⇒ 工具对 :66 无报警（详见「三、机器层结果与假红判定」W1）。**内容层面**：:66 的 `partly`/`fear of judgment`、:54 的 `likely`、:46 的 `hurried` 均应中文化；:10 的 `onstage` 是把原文 `on stage` 合并拼写，**属英文书写不规范**（原文写 `on stage`），非事实错误。 | **提示** |
| V4 | md:66 读者视角提示：`是本章唯一一次 Diana 表达对他人反应的恐惧` | `text/ch01_chapter_1.txt:18` 逐字：`She pretended she was texting to avoid eye contact—she couldn’t stand when smiling parents pointed out that she was going the wrong way, though she herself had made that joke, too, when she saw someone rushing home to grab a swim bag or whatever else.`；`text/ch01_chapter_1.txt:30` 逐字：`When she walked through the school doors, she could feel the teacher’s aide—lost in thought, counting the minutes until she could leave—judge her for being late.` | 本章 `fear` 零命中（原文只写 `embarrassed`(:15)、`judge`(:30)）。`couldn't stand`＝「受不了／难堪」，作「社会性不适」解读可辩护，**不与原文直接矛盾，故不判阻断**。但同一块内 **md:64 写着「作者把 Diana 的痛苦写成"羞辱"**而非"恐惧"**」**（:64 与 :66 属同一引语块「原句 4」，中间隔一空行，位于同一 md 文件），与 :66 的「恐惧」**标签互斥**；且「唯一一次」在 :30 助教评断处被 md:82 自己记录（「感到助教……在评断她的迟到」）⇒ **:64 与 :66 必须择一改齐**，否则同一块自相矛盾。 | **提示** |
| V5 | md:88 为什么这样写：`她不是被怪物追杀`（与 md:12「在序章的恐怖之后…恐怖不来自外力」呼应） | `text/ch01_chapter_1.txt` 与 `text/ch00_prologue.txt` 均**无** monster/creature 字样（`grep -cE 'monster\|monstru\|creature'` 两者皆 0）；`text/ch05_chapter_5.txt:441` 逐字：`she saw a monster… Alba looked like a creature from another dimension`；`text/ch13_chapter_13.txt:18` 命中 `a creature like the others` | 「怪物」是**全书恐怖线**的实体（ch02/ch05/ch06/ch13 都有），本章把它用作对照修辞并非凭空捏造；但**在本章范围内**没有怪物可供「追杀」⇒ 读者若只读 ch01 会觉得是空对照。**属跨章修辞，不是本章编造**，故不判阻断，改词与否由作者定。 | **需人判** |
| V6 | md:88 为什么这样写：`母亲缺席刺痛了她，是本章唯一一次直接写出 Brisa 的感受，此前都是外在行为` | `text/ch01_chapter_1.txt:30` 逐字：`Stung by her mother’s absence, she had sunk into the choir.`；`text/ch01_chapter_1.txt:6` 逐字结尾：`Failing to see her mom in the crowd, she decided to stop looking.` | :30 确为唯一一处**明写 Brisa 情绪**（`Stung`）处；但 :6 的 `she decided to stop looking` 是 Brisa 的**内心决定**（非纯外在动作），md:30 自己称它是「本章第一个主动选择」⇒「此前都是外在行为」在**全章范围**不成立，在**原句 6 块内**成立。属断言作用域不清，需作者定「唯一」的边界。 | **需人判** |
| V7 | md:10 导航 / md:14 人物弧线 / md:133 一句话总结：`Brisa 因母亲缺席而罢演` / `用罢演表达被遗弃感` / `Brisa 以罢演与皇冠面具回应母亲的缺席`（3 处） | `text/ch01_chapter_1.txt:30` 逐字：`Not just because she could have picked her daughter out even in darkness, but because Brisa was acting in a way that drew attention. In a way, her acting out had made her the star of the Christmas play: The only child not singing, she had crossed her arms and made a mask of the golden crown her classmates wore on their heads.` | 原文写 `acting out`（原文自带的词）＋ `The only child not singing`，**没有**「拒绝/罢演」字样；md:82 自己的译法较克制（「唯一不唱的孩子」「她的"表演"」）。「罢演」是原文可以支撑的合理概括，但语气比原文强（原文的 `acting out` 更偏「用反常举止引人注目」，且叙述者明说 `her acting out had made her the star`＝反而成了明星）。**不判错**，但三处「罢演」与 :82 的克制译法不统一，建议统一。 | **需人判** |
| V8 | md:16 导航：`第三人称限制视角先贴着台上的 Brisa，再切到赶路的 Diana` | `text/ch01_chapter_1.txt:6`（Brisa 段）→ `text/ch01_chapter_1.txt:12`（Diana 段）→ `:15`（Diana 段）→ `:30`（Diana 段，末段内又回切 Brisa） | 视角切换顺序与原文**段落顺序**一致（Brisa 段在 :6，DIANA 段从 :12 起），表述成立。末段 :30 在 Diana 视角内写 Brisa 的 `Stung by her mother's absence`（叙述者转述 Brisa 内心），md 未误标施事。 | **提示** |
| V9 | md:12 导航：`用 Diana 的焦虑症与母女关系建立本书的"家庭惊悚"基调` | `text/ch05_chapter_5.txt:543` 逐字：`In fact, it wasn’t that long ago that Diana herself had come to realize how serious it was… when Tomás was born and her fears began to multiply.`；`text/ch02_chapter_2.txt:132` 逐字：`All the women in the family, without exception, were compulsive and superstitious.` | 「焦虑症」是**全书层**结论（ch05 才坐实），本章只有行为描写、无诊断词。md 把它写在「情感弧线位置」（定位性判断）而非「本章发生了什么」，属跨章视角的合理概括，**不判错**。同理 md:76「这是强迫性思维的核心」、md:78「暗示她早有强迫性检查习惯，本章不是孤例」均有 ch02/ch05 支撑。 | **提示** |
| V10 | md:66 等处的英文残留，机器层**未报警** | `scripts/check_chinese_layer.py` 实测：ch01 不在阻断/提示名单（全书阻断 2 条在 ch11:10 / ch11:156，提示 2 条在 ch10:10 / ch10:164）。但用该脚本**自带**的 `mix_ratio()` 测 md:66 得 **50.0% > MIX_WARN 0.35**。 | 工具口径盲区：`check_chinese_layer.py` 对「中文理解／为什么这样写」跑 `mix_ratio`，对「**读者视角提示／表达方式」只查「整段是否无汉字」**（源码 :556-565），**不查单条夹杂率** ⇒ :66 的 50% 夹杂在工具口径里是绿的。内容该改（见 V3），**工具口径也该补**。按「成片同类报警先假定工具口径错了」的反向纪律：此处是**漏检**，须补口径。 | **提示**（工具口径待修，见「三」W1） |
| V11 | md:42 读者视角提示：`本章第一次出现 "Balmes"——与序章的儿童用品店、后文的 Splau/El Prat 共同构成巴塞罗那地理坐标` | `grep -rln 'Balmes' text/` → **仅** `text/ch01_chapter_1.txt`（原文 :12 `Diana walked down Balmes looking radiant`）；`text/ch00_prologue.txt:12` 逐字：`soon the whole store was lit up`、`:15` `the last time she’d been here, with Brigitte, trying on plastic tiaras`（儿童用品店成立）；`text/ch05_chapter_5.txt:609` 命中 `Splau`、`text/ch10_chapter_10.txt:6` 命中 `El Prat` | 全部成立，且「第一次出现」经全库 grep 核实。 | **提示**（成立，记录） |
| V12 | md:30 读者视角提示：`"nougat's my treat" 是西班牙圣诞糖果 turrón 的译写` | `text/ch01_chapter_1.txt:6` 逐字：`I’m the queen of the house and nougat’s my treat, at Christmas I send you kisses so sweet!`；`text/ch17_chapter_17.txt:123` 逐字：`Maybe something light before bed. Dried fruit and turrón?` | nougat 与 turrón 的对应有 ch17 实据，成立。 | **提示**（成立，记录） |
| V13 | md:54 读者视角提示：`Carlos 是 Diana 的伴侣` | `text/ch01_chapter_1.txt:12` 逐字：`Her partner was going to be in Madrid all day, so a classmate’s mom was picking up her son.`；`text/ch10_chapter_10.txt:9` 逐字：`While Carlos paid the driver and helped the kids out of the car…`（与 Diana 同车、育有一双孩子的伴侣） | 成立。⚠️ 用户已明示**「伴侣整天在马德里」此点已核实正确，不得去"修"它** ⇒ 本条记为**护栏**，任何人不得据此改动 :10/:34/:38。 | **提示**（成立，护栏） |
| V14 | md:54 读者视角提示：`"straightener" 的焦虑…后文 likely 复现` | `text/ch04_chapter_4.txt:150` 逐字：`“I should have known better. Fucking straightener. Why does this happen to me?”`；`text/ch08_chapter_8.txt:93` 逐字：`she confirmed that the heat wasn't on, the straightener was safely cooling` | 复现成立（直发器在 ch04、ch08 再现）。 | **提示**（成立，记录） |
| V15 | md:78 读者视角提示：`"Everything had been checked, and checked again, an hour earlier" 暗示她早有强迫性检查习惯，本章不是孤例` | `text/ch01_chapter_1.txt:21` 逐字：`Everything was in order. Everything had been checked, and checked again, an hour earlier.` | 原文逐字支持；「不是孤例」由 ch02:132 / ch05:543 支撑（见 V9）。 | **提示**（成立，记录） |
| V16 | md:88 为什么这样写：`"toes soft and perfect" 与 "pinkie toes raw" 的对照` | `text/ch01_chapter_1.txt:30` 逐字：`Moms who had shown up on time, serene and impeccable, toes soft and perfect.`；`:27` 逐字：`Diana arrived at the Christmas play late, her pinkie toes raw.` | 对照成立且用词逐字（md 未在这里写「粉色」；「粉色」只在 :16，见 V1）。 | **提示**（成立，记录） |
| V17 | md:50 句子结构：原句 3 全段共**二十**句；md:26/:38/:62/:74/:86 分别声称原句 1/2/4/5/6 为 6/8/2/9/19 句 | 独立切分实测：**6 / 8 / 20 / 2 / 9 / 19**，六项**全部吻合** | 句数断言全部成立（`docs/rules/20-gate.md` 的计数断言需客观真值，此项有）。 | **提示**（成立，记录） |
| V18 | md:86 句子结构：`他们按班依次上场`（原句 6「他们 went class by class, in order」） | `text/ch01_chapter_1.txt:30` 逐字：`But no. They went class by class, in order.` | 成立。 | **提示**（成立，记录） |
| V19 | md 词汇分级（⭐⭐⭐ 7 条 / ⭐⭐ 10 条 / ⭐ 5 条 = 22 条）例句 | 22 条例句经 flat 归一后**逐条命中本章原文**（miss=0）；`check_vocab.py` 全书 FAIL 0、ch01 无 WARN | 例句真实性成立。**分档合理性与释义准确性本审查未核**（见「四、未核清单」）。 | **跳过**（分档与释义未核） |
| V20 | 词汇表例句中的「 She mentally reconstructed the moments」（md:99） | `text/ch01_chapter_1.txt:15` 逐字：`She mentally reconstructed the moments before she left the house…` | 例句逐字成立。⚠️ 注意：**md:46 中文理解里同一处已被改写为「她在脑中重建」**（用户所述的 `mentally` 残留已修，git diff 可见 `-…She mentally 重建…` → `+…她在脑中重建…`），但**词汇表例句里的 `mentally` 是原文逐字，必须保留** ⇒ 修复时**不要**把 md:99 一起"中文化"，否则例句变非逐字。 | **提示**（护栏） |

### 与原文相符的断言（一并列明，避免「只报阻断」的不完整交代）
- **「伴侣整天在马德里，所以由一位同学的妈妈去接自己儿子」**（md:10/:34/:38）＝ `text/ch01_chapter_1.txt:12` `Her partner was going to be in Madrid all day, so a classmate’s mom was picking up her son.` ✔（用户明示已核实，**不得改动**）
- **Diana 提前出门、假期前交稿、做完下周的活、转自由职业以来第一次**（md:34）＝ :12 `She’d even finished the following week’s assignments, something she hadn’t managed since she’d gone freelance all those years ago.` ✔
- **一切井然有序／出门前一小时已检查又检查**（md:70/:78）＝ :21 `Everything was in order. Everything had been checked, and checked again, an hour earlier.` ✔
- **没有保姆，只有早到的家人、多是母亲；无视"请勿录像"指示**（md:82）＝ :30 `She saw none of the nannies she knew from school pickup… they’d ignored the instruction not to take videos.` ✔
- **唯一不唱歌的孩子、抱臂把金冠做成面具、像列队照里的小罪犯被闪粉纸带蒙眼**（md:82/:88）＝ :30 `The only child not singing, she had crossed her arms and made a mask of the golden crown… She looked like a tiny felon in a lineup, blindfolded with a band of sparkly paper.` ✔
- **直发器当然没有温控、插头拔掉线圈好、离其他东西半米远**（md:70）＝ :21 `The straightener, which of course had no thermostat, was turned off with the cord coiled up, set half a meter from everything else in the bathroom.` ✔
- **她希望某样东西（毛巾、发圈）在进门瞬间起火，烧出无害小火证明自己不荒唐**（md:70/:78）＝ :21 `hoping she had, in fact, left the straightener on and that something—a towel, a scrunchie—would catch fire…` ✔
- **「她只能通过电话出现」的 Carlos**（md:54）＝ :15 `She called Carlos… But he didn’t pick up.`（本章 Carlos 仅此一次出场）✔
- **「她曾是背诗的小天使」**（md:14）＝ :6 `The preschoolers had dressed up as angels… From the stage, Brisa scanned the room for her mother while she recited the Christmas poem…` ✔

---

## 三、机器层结果与「假红」判定

| 探针 | 结果 | 判定 |
|---|---|---|
| `bash scripts/chapter.sh "ch01 chapter 1.md"`（书目录内跑） | 退出码 **0**；「引语块 6，片段 6，查无 0／空引号 0｜子项缺 0｜关键词不成立 0｜中文过薄 0｜H1 ✅ Chapter 1｜导航 4 项 ✅｜块数 6（本书中位 6.0，范围 3–9）｜结论：✅ 机器层无阻断」 | 全绿，**无假红**（机器未报任何红项，故本表无一条「假红」档） |
| `2-machine.json`（R2 存档） | `verdict: ok`；6 块各 1 段 `ok:true`（pos 2/712/1641/3042/3558/4394）；`segment_miss/struct_bad/empty_quote/keyword_bad/cjk_low` 全 0；`form`：h1 `Chapter 1` ok、nav_count 4、subitems_modal 五项、blocks 6、profile novels | 与本审查独立取证一致，**互相印证** |
| 本审查自建 flat 取证（原始文件、非归一化） | 6/6 引语**整串**命中（len 711@2 / 938@714 / 1407@1653 / 517@3061 / 838@3579 / 1867@4418）；无省略号、无拼接、无跨段；本章 6 个正文行**全部被引语覆盖**（唯一"未覆盖"是页码 `1` 与首句粘连的切分伪影） | 与机器一致 |
| `python3 scripts/check_vocab.py <书目录>` | FAIL **0**；14 条 WARN 全在 ch05/ch11/ch12/ch13/ch14/ch16/ch17，**ch01 无 WARN**；本审查另验：22 条例句 flat 命中本章原文 miss=0 | ch01 通过 |
| `python3 scripts/quotes.py blocks "ch01 chapter 1.md"` | 前缀完整・编号连续无撞车・无孤儿分析・无自查泄漏 E/F，EXIT 0 | 通过 |
| `python3 scripts/structure.py anchor .` | 「扫 21 个 md，109 个引语块｜❌ 凭空造词 0 处｜⚠️ 松散关键词 0 处」——ch01 的 26 个关键词全部落在本块引语或分析正文内 | 通过 |
| `python3 scripts/structure.py order .` | 「18 个 md / 51 块，顺序或编号缺陷 0 章／不可判定 9 章」；**ch01 不在不可判定名单**（ch02/ch04/ch05/ch06/ch08/ch10/ch11/ch14/ch15） | ch01 块序合格 |
| `python3 scripts/analysis.py inline .` | ✅逐字 2202｜⚠️跨章 27｜🔶拼接 24｜🟠部分命中 359｜🟡词形 24｜❌零命中 0｜跳过 657；**ch01 无任何报警行** | 通过 |
| `python3 scripts/check_chinese_layer.py <书目录>` | 阻断 2（ch11:10 导航非中文、ch11:156 总结非中文）｜提示 2（ch10:10、ch10:164）｜109 块、合格分析密度 100%、整层夹杂率 0%；**ch01 不在任一名单** | 见下 W1 |
| `python3 scripts/bookform.py .` | 导航众数 4 项、子项众数 5 项；ch01 与众数**完全一致** | 通过 |

**W1 · 工具口径盲区（须补口径，不改 md 判红）**
`check_chinese_layer.py` 源码 :526/:550 对「中文理解／为什么这样写」跑 `mix_ratio`，:556-565 对「读者视角提示／表达方式」**只查「整段是否无汉字」**，不查单条夹杂率。
实测（用该脚本自带的 `mix_ratio`）：`md:66` = **50.0%**、`md:54` = 34.9%、`md:10` = 21.2%、`md:46` = 6.4%，阈值 `MIX_WARN = 0.35`。
⇒ :66 的读者视角提示若按同口径判，会**超阈值**；工具却报绿。**这是漏检，不是假红。** 建议在 :556-565 的循环里对「读者视角提示／表达方式」补 `mix_ratio > MIX_WARN` 判据（与前两个字段同档）。
（按「成片同类报警先假定工具口径错了」纪律的反向应用：此处无报警，但盲区成立，先修工具口径再动 md 措辞。）

---

## 四、修复优先级（交派工人；本审查员按纪律**未改任何书目录 md、未 git add/commit**）

1. **V1（阻断）· md:16**：`用粉色脚趾被新靴子磨破` → 改为「**小趾**」（与原文 `pinkie toes` 一致，与 md:52/:88 已引的 `pinkie toes raw` 一致）。改后必须重跑 `chapter.sh`。
2. **V2（阻断）· md:34 / md:38 / md:58**：`校庆演出` → `圣诞演出`（与 md 自身 :34 前半、:82、:133 一致，且与原文 `Christmas play` / `school play` 相容）；`比她先到校庆` → `比她先到学校/圣诞演出`。三处必须同改（`grep -rn '校庆' --include='*.md' .` 复核应归零）。
3. **V3（提示）· md:66 / md:54 / md:46 / md:10**：`fear of judgment`→`害怕被人评判`、`partly`→`部分`、`likely`→`很可能会`、`hurried`→`快步`、导航 `onstage`→`在舞台上的`（原文写 `on stage` 分写）。
4. **V4（提示）· md:64 与 md:66 择一改齐**：:64 写「"羞辱"**而非"恐惧"**」而 :66 写「表达对他人反应的**恐惧**」——同一块内标签互斥；建议 :66 改「唯一一次 Diana 因他人反应而感到难堪」。
5. **V5 / V6 / V7（需人判）· md:88 / md:10 / md:14 / md:133**：① 「她不是被怪物追杀」是否保留跨章对照；② 「唯一一次直接写出 Brisa 的感受」是否限定为「原句 6 块内」；③ 三处「罢演」是否统一为 :82 的克制译法（「唯一不唱的孩子」）。**这三项属作者裁量，本审查不代决。**
6. **W1（工具）· `scripts/check_chinese_layer.py`**：为「读者视角提示／表达方式」补单条夹杂率判据（见「三」W1）。

---

## 五、R5-补 · 零命中类断言的自证（全部附原命令、输出、退出码）

> 纪律：BSD grep 在本机是 GNU-compatible 版，但 `text/` 被 `.gitignore` 排除 ⇒ `git grep` 与默认尊重 ignore 的 rg 系永远「查无」且退出码 1 与「真查无」不可区分。
> ⇒ 本节一律用**显式文件路径** + `/usr/bin/grep -E`（交替匹配用 `-E`、查单词用 `-w`），并单列退出码。

```
# V2「校庆」零命中（全书）
$ cd notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text
$ /usr/bin/grep -cE 'anniversary|anniversar' *.txt > /tmp/q1 2>&1; echo "exit=$?"; cat /tmp/q1
exit=1
ch00_prologue.txt:0   ch01_chapter_1.txt:0   ch02_chapter_2.txt:0   ch03_chapter_3.txt:0
ch04_chapter_4.txt:0   ch05_chapter_5.txt:0   ch06_chapter_6.txt:0   ch07_chapter_7.txt:0
ch08_chapter_8.txt:0   ch09_chapter_9.txt:0   ch10_chapter_10.txt:0  ch11_chapter_11.txt:0
ch12_chapter_12.txt:0  ch13_chapter_13.txt:0  ch14_chapter_14.txt:0  ch15_chapter_15.txt:0
ch16_chapter_16.txt:0  ch17_chapter_17.txt:0
→ 命中 0（18 章全 0）；退出码 1（真查无）

# V2 阳性对照：原文确有 school play / Christmas play
$ /usr/bin/grep -noE 'school play|Christmas play' ch01_chapter_1.txt > /tmp/o6 2>&1; echo "exit=$?"; cat /tmp/o6
exit=0
12:Christmas play
12:school play
18:school play
27:Christmas play
30:Christmas play
→ 命中 5；退出码 0（探针有效，不是口径错）

# V1「粉色」零命中（本章无颜色词 pink）
$ /usr/bin/grep -noE '\bpink[a-z]*\b' ch01_chapter_1.txt > /tmp/o2 2>&1; echo "exit=$?"; cat /tmp/o2
exit=0
15:pinkie
27:pinkie
→ 命中 2，均为 pinkie（小趾），无 pink；退出码 0
$ /usr/bin/grep -noiE '\b(pink|red|blue|green|black|white|gold|golden|beige)\b' ch01_chapter_1.txt
→ 仅 white(:6)、golden(:6)、beige(:6)、golden(:30)，无 pink

# V4「fear」零命中（本章）
$ /usr/bin/grep -cE 'fear[a-z]*' ch01_chapter_1.txt > /tmp/o3 2>&1; echo "exit=$?"; cat /tmp/o3
exit=1
0
→ 命中 0；退出码 1
# 阴性对照（探针有效性）：同一模式在别章有命中
$ /usr/bin/grep -cE 'fear[a-z]*' *.txt
exit=0
ch02_chapter_2.txt:1  ch05_chapter_5.txt:2  ch06_chapter_6.txt:3  ch10_chapter_10.txt:1
ch11_chapter_11.txt:1  ch15_chapter_15.txt:1  ch16_chapter_16.txt:1  （其余 0）
→ 探针有效，ch01 的 0 是真的 0

# V5「monster」零命中（本章与序章）
$ /usr/bin/grep -cE 'monster|monstru|creature' ch01_chapter_1.txt > /tmp/o4 2>&1; echo "exit=$?"; cat /tmp/o4
exit=1
0
$ /usr/bin/grep -cE 'monster|monstru|creature' ch00_prologue.txt > /tmp/o5 2>&1; echo "exit=$?"; cat /tmp/o5
exit=1
0
# 阴性对照：全书有命中（证明探针有效）
$ /usr/bin/grep -cE 'monster|monstru|creature' *.txt
exit=0
ch02_chapter_2.txt:1  ch05_chapter_5.txt:1  ch06_chapter_6.txt:1  ch13_chapter_13.txt:4  （其余 0）

# 「校庆」「粉色」在全书 md 的分布（证明是 ch01 孤例）
$ cd .. && /usr/bin/grep -rn '校庆' --include='*.md' . > /tmp/q4 2>&1; echo "exit=$?"; cat /tmp/q4
exit=0
./ch01 chapter 1.md:34:…没为了窝着写完某部荒诞电影的评论或冲去采访某个无足轻重的公众人物而错过校庆演出。…
./ch01 chapter 1.md:38:…没为窝着写评论或赶去采访而错过校庆演出，…
./ch01 chapter 1.md:58:…他们都"刚刚好"出门，却似乎仍会比她先到校庆。…
→ 命中 3，全部在 ch01；其余 17 章 0

$ /usr/bin/grep -rn '粉色' --include='*.md' . > /tmp/q6 2>&1; echo "exit=$?"; cat /tmp/q6
exit=0
./ch01 chapter 1.md:16:…用粉色脚趾被新靴子磨破这类细节，把焦虑具象化。
./ch10 chapter 10.md:138:| pink light | 粉色光 | "A deep pink, almost purple" |
./ch14 chapter 14.md:10:…说天上出现了粉色的灯；Juan 叫来…
./ch14 chapter 14.md:82:…子们。"一些粉色的灯光，在天…
./ch14 chapter 14.md:86:…齐声说天上有粉色的灯，第 60 句…
./ch14 chapter 14.md:109:| pink lights | 粉色灯光 | "Some pink lights, in the sky" |
./ch14 chapter 14.md:121:…们说天上看见粉色的灯，Juan 叫来…
./ch16 chapter 16.md:74:…了一个巨大的粉色和紫色星星投…
./ch16 chapter 16.md:87:…群，一切都被粉色的光、然后紫…
→ 命中 9；其中「粉色**脚趾**」仅 ch01:16 一处，其余 8 处均指粉色灯光/光/星（ch10/ch14/ch16）⇒ 「粉色脚趾」是全书孤例且无原文依据

# 「pinkie」在全书 md 的分布（证明 md 其余各处与原文一致，别误改）
$ /usr/bin/grep -rn 'pinkie' --include='*.md' . > /tmp/q5 2>&1; echo "exit=$?"; cat /tmp/q5
exit=0
./ch01 chapter 1.md:44 / :52 / :80 / :88 / :129
→ 命中 5，全在 ch01，且全部与原文 pinkie toes 一致 ✔
```

---

## 六、R5.5 已核实为正确（防误修，固定一节）

**凡写进这一节的，后续任何人不得以「读着不对」为由改动，除非能给出反证。**

1. **md:10 / md:34 / md:38「伴侣整天在马德里，所以同学的母亲代接儿子」** — `text/ch01_chapter_1.txt:12` 逐字：`Her partner was going to be in Madrid all day, so a classmate’s mom was picking up her son.` ⇒ **用户已明示此点核实正确；原文就是 "going to be in Madrid all day"（整天在马德里），不得改成「当天不在马德里」**。
2. **md:54「Carlos 是 Diana 的伴侣」** — 同上 :12 的 `Her partner` ＋ `text/ch10_chapter_10.txt:9` `While Carlos paid the driver and helped the kids out of the car`（与 Diana 同车、育有一双孩子的伴侣）⇒ 成立。
3. **md:44 / md:52 / md:80 / md:88 / md:129 的 `pinkie toes raw` 类表述** — `text/ch01_chapter_1.txt:27` 逐字：`her pinkie toes raw.`；:15 逐字：`her too-tight new boots destroying her pinkie toes.` ⇒ 成立，**要改的只有 md:16 的「粉色」二字**（`grep -n 'pinkie' "ch01 chapter 1.md"` → :44 / :52 / :80 / :88 / :129 五处，全部与原文一致）。
4. **md:99 词汇例句 `"She mentally reconstructed the moments"`** — `text/ch01_chapter_1.txt:15` 逐字：`She mentally reconstructed the moments before she left the house` ⇒ **例句必须保留英文 `mentally`（逐字要求）**；md:46 中文理解里的「她在脑中重建」是中文化，**两处形式不同都正确，不要互相"对齐"**。
5. **md:42「本章第一次出现 "Balmes"」** — `grep -rln 'Balmes' text/` → 仅 `text/ch01_chapter_1.txt` ⇒ 成立。
6. **md:42「序章的儿童用品店」** — `text/ch00_prologue.txt:12` `soon the whole store was lit up`、`:15` `the last time she’d been here, with Brigitte, trying on plastic tiaras` ⇒ 成立（序章是儿童用品店，不是别的地方）。
7. **md:30「nougat 是西班牙圣诞糖果 turrón 的译写」** — `text/ch01_chapter_1.txt:6` `nougat’s my treat` ＋ `text/ch17_chapter_17.txt:123` `Dried fruit and turrón?` ⇒ 成立。
8. **md:90「Brisa 的 "acting out" 是本章主题词」** — `text/ch01_chapter_1.txt:30` 逐字：`her acting out had made her the star of the Christmas play` ⇒ 成立（原文自带该词）。
9. **md:82「唯一不唱的孩子、把金色皇冠做成面具、小罪犯、闪亮纸带蒙眼」** — `text/ch01_chapter_1.txt:30` 逐字：`The only child not singing, she had crossed her arms and made a mask of the golden crown her classmates wore on their heads. … She looked like a tiny felon in a lineup, blindfolded with a band of sparkly paper.` ⇒ 成立（用户所述「末段 Diana 独自坐最后一排、Brisa 是唯一不唱、拿金冠当面具的孩子」全部命中）。
10. **md:26/:38/:50/:62/:74/:86 的句数（六/八/二十/二/九/十九）** — 独立切分实测 6/8/20/2/9/19，**六项全部吻合** ⇒ 成立。
11. **md:42「后文的 Splau/El Prat」** — `text/ch05_chapter_5.txt:609` 命中 `Splau`、`text/ch10_chapter_10.txt:6` 命中 `El Prat` ⇒ 成立。

---

## 七、未核清单（❓ 无法判定，不是「正常」）

1. 引语**字符级**一致性（标点、大小写、弯引号/破折号逐字符比对）——我只做 flat 归一比对，flat 会掩盖标点级差异 ⇒ ❓
2. 词汇表 22 条的**释义准确性**与 **⭐/⭐⭐/⭐⭐⭐ 分档合理性**（只验了例句逐字）⇒ ❓
3. 全文 **16 个其他章**与 ch01 的人物/时间线/称呼一致性（只抽查了 Carlos 关系、straightener 复现、Splau/El Prat、monster 主题线、ch03 对 ch01 的引用）⇒ ❓
4. `scripts/corruption_scan.py`（编辑损坏扫描）本次**未跑** ⇒ ❓
5. `scripts/verify_corpus.py`（语料层验收）本次**未跑**（本章 `text/` 为既有语料）⇒ ❓
6. **md 的未提交改动**：另一 agent 正在改写导航／一句话总结／句子结构；本报告行号只对 md5 `e3cb5bff8e140d30fc6d91a70be5ea12`（mtime 13:05:45）有效，对方再提交后行号会漂移 ⇒ ❓
7. 「校庆」最终改译为「圣诞演出」还是「学校演出」——属作者用词裁量 ⇒ ⚠️ 需人判（已在本报告 V2 给出首选「圣诞演出」，因与 md 自身 :34/:82/:133 一致）
8. **总览三篇**（`00_概述.md` 等）是否含本章的同款错误（如「校庆」「粉色脚趾」）——本次**未查** ⇒ ❓

---

机器层：2-machine.json（verdict ok，6/6 引语命中）
