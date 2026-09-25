---
状态: 未读
modified: "2026-09-25"
source_text: ch07
---

# 07. 6. Recycling the Garbage（回收垃圾）

## 概览

- **出处**：*Why We Die*，书内第 6 章
- **作者**：Venki Ramakrishnan
- **体裁**：非虚构论述（分子生物学＋阿尔茨海默病研究史）
- **章节定位**：正文第 6 章；第 4、5 章讲 DNA 与染色体的维护，本章转向蛋白质——细胞中真正执行功能的分子——及其质量控制
- **字符数**：约 32,749 字符（去空白）
- **一句话主旨**：细胞用两套回收系统（泛素-蛋白酶体与自噬-溶酶体）处理它自己生产的次品，而阿尔茨海默病等神经退行性疾病正是这两套系统失灵的结果；更棘手的是，应对压力的统一应激反应本身在晚年可能从救命机制变成致病机制。

本章从作者的日常经验起笔——七十岁后忘事、丢手套，随即转向五千万痴呆症患者这一严重问题。蛋白质折叠的原理被先交代清楚：疏水氨基酸躲在内部、亲水氨基酸朝外，这一「折叠规则」是理解后续所有蛋白质质量控制的前提。细胞处理蛋白的方式与家庭处理物品高度相似——扔掉过期的、修好破损的、送去回收；但作者随即指出两处关键差异：制造商不管产品售出后的命运，而细胞既是生产者也是使用者，必须确保数千种蛋白协同工作。缺陷蛋白有四种来源：翻译错误、折叠失败、解链（煮蛋与柠檬奶的演示）、以及糖基化异常（糖化导致白内障与黄斑变性）。细胞的两道防线是伴侣蛋白（chaperones，负责重新折叠）与泛素-蛋白酶体系统（负责切碎降解）。体积更大的残余则交给自噬-溶酶体系统：de Duve 发现溶酶体，Ohsumi 在酵母中筛出十二个自噬必需基因。蛋白质堆积过多时，细胞启动「未折叠蛋白反应」，最终可能导向细胞自杀。当积累速度超过回收能力时，细胞启动「整合应激反应」（ISR）——关停大部分蛋白合成，只保留少数急需的蛋白质。然而本章的核心悖论在此出现：增强 ISR 可治疗某些疾病，抑制 ISR（ISRIB）却能改善阿尔茨海默病的记忆缺陷。作者借「刹车始终踩着」的车比喻解释了这一点：ISR 在晚年可能变成慢性失控。章末以交响乐团作比，并引出 Carleton Gajdusek 与朊病毒病的研究史。

### 结构列表

1. **七十岁的遗忘**：作者自述的健忘与丢三落四，以及随之而来的对神经退行性疾病的恐惧。
2. **痴呆症的数字**：五千万人患痴呆，预计 2050 年达一亿三千万；在英格兰与威尔士已超过心脏病成为首要死因。
3. **阿尔茨海默病的表现**：从记忆与辨认的丧失，到最终失去自我意识与语言能力。
4. **蛋白质折叠的物理原理**：疏水氨基酸藏内、亲水氨基酸朝外，折叠由热力学倾向驱动。
5. **家庭物品的类比**：新买的次品、使用中的损伤、老化过时、季节性需求——蛋白质的问题与此同构。
6. **关键差异**：制造商不关心产品下落，而细胞必须让数千种蛋白协同工作。
7. **翻译错误**：mRNA 错误或核糖体误读导致序列异常。
8. **折叠的协助者**：伴侣蛋白（chaperones），Laskey 的命名与维多利亚时代「陪护」的比喻。
9. **解链的演示**：煮蛋使蛋白展开，柠檬汁使牛奶凝固——疏水氨基酸外露导致聚集。
10. **糖基化与糖化**：正常有序的糖基化与随年龄增加的随机糖化，白内障与黄斑变性是后果。
11. **未折叠蛋白反应**：增加伴侣蛋白、标记降解、减产乃至停止生产、极端时细胞自杀。
12. **泛素-蛋白酶体系统**：泛素的发现与「厨房水槽下的垃圾处理器」比喻。
13. **溶酶体与自噬**：de Duve 的发现与「城中垃圾回收中心」的比喻。
14. **Ohsumi 的酵母筛选**：在液泡中积累细胞残骸的菌株，筛出十二个自噬必需基因。
15. **自噬的四种功能**：正常发育、清除废物、抗击病毒、应对饥饿。
16. **整合应激反应（ISR）**：全局关闭蛋白合成，仅保留应急蛋白质。
17. **ISRIB 的悖论**：抑制 ISR 反而改善记忆，刹车常踩不松的比喻。
18. **行业动向**：Calico Life Sciences 与 Altos Labs 的布局。
19. **交响乐团之喻**：没有指挥的乐团，某个声部失准则整体崩溃。
20. **Gajdusek 与朊病毒**：诺奖得主兼儿童性侵犯者的双重身份，以及一种由蛋白单独致病的疾病。

## 论证结构

- **核心论点**：蛋白质的功能依赖其形状，而形状依赖于正确制造、正确折叠与及时回收。细胞为此投入了巨大的质量管理 machinery——伴侣蛋白、泛素-蛋白酶体、自噬-溶酶体——而衰老的直接后果之一就是这套系统效率下降。神经退行性疾病则是这一失败的极端表现：异常折叠的蛋白聚集体杀死神经元，而本该清理它们的系统已经无力工作。
- **证据链**：

  | 证据 | 类型（案例/研究/数据/类比） | 支撑什么 |
  |------|------|------|
  | 疏水氨基酸藏于内部、亲水氨基酸朝外 | 机制 | 蛋白折叠由热力学驱动，而非随机 |
  | 煮蛋、柠檬奶使蛋白解链并凝固 | 演示 | 解链后的疏水残基外露导致聚集 |
  | 随年龄增加的糖化导致白内障与黄斑变性 | 病理 | 翻译后修饰的失控是衰老的具体表现 |
  | 伴侣蛋白协助折叠，源自「Victorian chaperones」 | 命名／类比 | 分子机制与日常经验的对应 |
  | 泛素的名称源自其无处不在 | 命名史 | 科学命名的偶然性 |
  | 蛋白酶体是「厨房水槽下的垃圾处理器」 | 类比 | 泛素-蛋白酶体系统一次只处理一件 |
  | 溶酶体是「城中垃圾回收中心」 | 类比 | 自噬系统处理大体积残余 |
  | de Duve 发现溶酶体与自噬 | 发现史 | 细胞自我消解机制的发现 |
  | Ohsumi 在酵母中筛出十二个自噬必需基因 | 实验 | 自噬是可被遗传学解析的主动过程 |
  | 猪尾蛔虫幼虫可进入 dauer 状态存活数月 | 案例 | 细胞可在极低代谢下维持功能 |
  | ISR 增强改善小鼠病理，ISR 抑制改善阿尔茨海默记忆 | 双向实验 | 同一机制在不同状态下作用相反 |
  | ISRIB 在脑损伤一个月后给药仍有效 | 实验 | 记忆恢复的时序观察 |
  | 神经退行性疾病随年龄升高且由自身蛋白功能障碍引起 | 分类 | 蛋白质错误折叠是共同病理机制 |
  | Gajdusek 发现朊病毒病 | 医学史 | 一种仅由蛋白单独致病的疾病，确证「蛋白可致病」 |

- **论证脉络：以作者的衰老焦虑与痴呆症数据建立问题的重要性 → 交代蛋白质折叠的物理基础 → 用家庭物品的类比引入「质量管理」的概念 → 指出细胞与家庭的关键差异（协同工作要求）→ 逐一列举蛋白质缺陷的四种来源（错译、折叠失败、解链、糖化）→ 介绍第一道防线（伴侣蛋白）与第二道防线（泛素-蛋白酶体）→ 转向大体积残余的自噬-溶酶体系统 → 由 de Duve 与 Ohsumi 的发现补完机制 → 说明自噬的正常发育功能（房屋翻新的比喻）→ 描述 ISR 的作用机制（交通堵塞的比喻）→ 提出 ISR 效果的方向性依赖（增益与抑制各有实验支持）→ 用刹车比喻解释其双重性 → 交代产业动向 → 以交响乐团总结蛋白质协同的要求 → 引出朊病毒病研究史。
- **可质疑处**：
  1. 本章对「蛋白质错误折叠导致神经退行性疾病」的叙述在总体上被学界接受，但作者将阿尔茨海默病与帕金森病、Pick 病的共同病因归结为「我们自身蛋白的功能障碍」，这一表述较研究现状更强——就阿尔茨海默病而言，tau 与 β-淀粉样蛋白的确切致病机制至今仍有争议。
  2. 作者指出 ISRIB 改善小鼠记忆后，对结果的解释完全依赖于 Sonenberg 的「刹车常踩」这一比喻（ISR 慢性失控）。这一解释本身合理，但目前尚无直接证据表明老年人的 ISR 确实处于慢性失控状态。
  3. 关于 ISR 的双向效应，作者承认「可能有些情况适合增强、有些适合抑制」，但并未给出区分两者的判据。这使得本章的结论停在「需要更多研究」，读者若期待一个可操作的判断，会落空。
  4. 本章以 Gajdusek 的生平收尾，作者特意点出其「诺奖得主兼儿童性侵犯者」的双重身份。此类插入在作者的其他章节中亦有先例（如 Muller、Carrel），它们有助于呈现科学史的复杂性，但叙述重心偏向个人品行而非科学内容，可能使读者对相关发现的评价产生不应有的偏向。

## 选择性精读

> **原句 1:** "As we age, the quality control and recycling machinery of the cell deteriorates, leading not only to neurodegenerative but also many other diseases of old age, including inflammation, osteoarthritis, and cancer."

**中文理解**：随着我们衰老，细胞的质量控制与回收机制逐渐劣化，这不仅导致神经退行性疾病，也导致许多其他老年疾病，包括炎症、骨关节炎与癌症。

**句子结构**：主句 As we age 为时间状语从句；the quality control and recycling machinery of the cell 为并列主语；deteriorates 为谓语；leading not only to...but also... 为现在分词短语作结果状语，其中 including 为插入语。

**关键词**：`quality control and recycling machinery`、`deteriorates`、`not only to...but also many other diseases`、`inflammation, osteoarthritis, and cancer`

**表达方式**：以 quality control（质量控制）这一制造业术语描述细胞的蛋白管理，立即把本章确立为一篇关于「细胞内质检」的论述；deteriorates 一词涵盖渐进恶化而非突然故障；not only...but also 把神经退行性疾病与炎症、骨关节炎、癌症并列为同一原因的不同表现。

**为什么这样写**：这句话承接前面长篇的机制描述，为整章收束到一句可被记住的结论。它同时完成一次范围的扩大——读者可能以为蛋白质量问题只与大脑相关，而「炎症、骨关节炎、癌症」的出现说明这一机制关乎整个衰老过程。这一并置也预告了全书的一个主题：衰老不是单一过程，而是多个器官的共同退化。

> **原句 2:** "humorously named these proteins chaperones."

**中文理解**：他诙谐地把这些蛋白质命名为「陪伴者」（chaperones）。

**句子结构**：省略主语的过去分词结构作插入语，修饰前面的动词（named）；these proteins 为宾语；chaperones 为宾语补足语（宾语与补足语之间有逗号隔开，构成「命名……为……」结构）。

**关键词**：`humorously named`、`these proteins`、`chaperones`

**表达方式**：以 humorously 点出命名的随意性质，把「陪伴者」这一维多利亚时代的社交用语借用到分子生物学；these proteins 的指示代词强化了这些蛋白质作为一类共同体的存在。

**为什么这样写**：作者在此处借用了自己在剑桥同事 Ron Laskey 的说法，把一群功能严谨的蛋白质叫作「陪伴者」。这一命名把「监督折叠过程以防错误互动」这一机制日常化，同时也给读者留下了一个可复述的图像——正如维多利亚时代有陪护陪同年轻女子在舞会上避免不当接触，这些蛋白质陪伴着新生肽链，阻止其与不该接触的分子相触。

> **原句 3:** "Like Victorian chaperones during courtship, these proteins prevent improper interactions between different parts of the chain or between chains."

**中文理解**：就像维多利亚时代 courtship 期间的陪护人一样，这些蛋白质阻止肽链不同部分之间、以及肽链彼此之间的不当接触。

**句子结构**：主句为 There be 结构的隐含主语 these proteins（这些蛋白）；谓语 prevent；宾语 improper interactions；between...and... 介词短语说明「不当接触」发生的位置。

**关键词**：`Like Victorian chaperones`、`prevent improper interactions`、`between different parts of the chain`

**表达方式**：以 Like 引导的比况明喻（明喻 = 明喻）直接把分子机制映射到十九世纪的社会习俗；courtship 一词（求偶／求爱）赋予这一比喻以性别的具体性；两个 between 介词短语并列，说明「不当接触」的两种形态（链内与链间）。

**为什么这样写**：这个比喻的精确之处在于，它同时解释了「监督者」与「被监督者」的关系：chaperone 的职责不是替代被陪伴者，而是限制其与他人的接触。蛋白质折叠正是如此——链内的疏水片段互相排斥，而伴侣蛋白确保它们不会在折叠完成前错误结合。这一比喻让「蛋白质质量控制」这一抽象概念变得具体可感。

> **原句 4:** "Like the garbage disposal in your kitchen sink, it can handle only one scrap at a time."

**中文理解**：就像你家水槽下的垃圾处理器，它一次只能处理一小块垃圾。

**句子结构**：独立句；主句 it can handle only one scrap at a time；at a time 为强调短语；Like the garbage disposal in your kitchen sink 为介词短语作比较状语（置于句首）。

**关键词**：`Like the garbage disposal in your kitchen sink`、`can handle only one scrap`、`at a time`

**表达方式**：以 Like 引出明喻并前置，使比喻先行、结论在后，形成「先见其物、后知其量」的阅读顺序；only one...at a time 以数量限制的方式点出局限性。

**为什么这样写**：此句解释了泛素-蛋白酶体系统的运作瓶颈：一次只能处理一条蛋白链上的一个降解段。作者把这一生化限制转译为读者厨房中的熟悉经验，从而为下一句的转折（「但如果需要处理的是一整张旧沙发呢？」）埋下伏笔——量变引出了系统性的方案（自噬）。

> **原句 5:** "the lysosome is the huge garbage recycling center in your city."

**中文理解**：溶酶体就是你所在城市的巨型垃圾回收中心。

**句子结构**：这是一个省略结构，前面有 If the proteasome is akin to the garbage disposal in your kitchen sink 的条件从句；主句 the lysosome is the huge garbage recycling center in your city；in your city 为后置修饰。

**关键词**：`the huge garbage recycling center in your city`

**表达方式**：以 the huge（巨大的）对应前文水槽处理器的小规模，以 in your city（在你城中）把尺度从家庭扩展到城市；中心一词暗示它是汇总各处垃圾的中转枢纽。

**为什么这样写**：把溶酶体比作「垃圾回收中心」而非「垃圾填埋场」，关键在于前者会「回收」——它把废料分解为可再使用的氨基酸。这正是细胞回收机制的核心特点：销毁不是目的，回收才是。理解这一点，读者才能理解为什么细胞要如此大费周章地拆解自己的零件。

> **原句 6:** "a bit like turning off the main water supply when you have a flood in the bathroom."

**中文理解**：有点像在浴室发生洪水时关闭总供水阀门。

**句子结构**：这是一个不完整的名词性短语（无主谓），作 a bit like 的宾语，由动词 turning off 充当动名词；when you have a flood in the bathroom 为时间状语从句。

**关键词**：`a bit like turning off`、`the main water supply`、`a flood in the bathroom`

**表达方式**：以 a bit like（有点像）降低比喻的强度，避免断言等同；turning off the main water supply 以动名词短语构成动作；a flood in the bathroom（浴室的水灾）以小场景类比细胞内蛋白质过量堆积的危机。

**为什么这样写**：在蛋白质质量失控的时刻，细胞停止蛋白质合成的策略——主动「关水」——被翻译为读者生活中最接近的应急反应。这个比喻的精妙在于它同时包含了「减少供给」与「控制事态」两层含义，与 ISR 关闭蛋白合成的双重作用（减产 + 保留应急蛋白）一致。

> **原句 7:** "It's like driving a car in which the brake is activated all the time instead of only in response to a signal to slow down or an accident ahead."

**中文理解**：这就像驾驶一辆刹车始终处于制动状态的车，而不是只在收到减速信号或前方有事故时才制动。

**句子结构**：主句 It's like driving a car in which...；in which 引导定语从句修饰 a car；从句中 the brake is activated all the time 与 only in response to a signal to slow down or an accident ahead 由 instead of 连接，形成对比。

**关键词**：`the brake is activated all the time`、`instead of only in response to a signal`、`an accident ahead`

**表达方式**：以 instead of 连接「常态」与「应然」，把 ISR 的功能从「应急机制」重新定义为「被误触发的应急机制」；all the time 与 only in response to 构成时间频率上的对立；an accident ahead 保留了该机制原本应有的触发场景。

**为什么这样写**：本章的核心悖论在此被一个比喻彻底说清：ISR 本身是好的（在应激时保护细胞），但如果它在平时也持续激活，就从救命机制变成了负担。作者并不否认 ISR 的价值，而是指出其**剂量与时机**才是关键——这为「需要判断何时增强、何时抑制」这一实际困境提供了思考框架。

> **原句 8:** "It is not unlike all the instruments in a symphony orchestra that all have to play their parts together."

**中文理解**：这与交响乐团中必须各自演奏好自己声部、协同演奏的处境并无不同。

**句子结构**：主句 It is not unlike...；all the instruments in a symphony orchestra 为名词短语作介词宾语；that all have to play their parts together 为定语从句修饰 instruments。

**关键词**：`It is not unlike`、`all the instruments in a symphony orchestra`、`have to play their parts together`

**表达方式**：以 It is not unlike（这与……并无不同）作弱化否定，避免过于肯定的类比；a symphony orchestra（交响乐团）作为全章的总结意象，指向协调与协作；all the instruments 与 all have to（双重 all）强调无一例外。

**为什么这样写**：交响乐团是作者全书的标志性比喻（他还将在后续章节中用它来对照细胞内部的无指挥状态）。这个比喻的最终功能是把本章的机制描述升华为一个整体论断：蛋白质并非各自独立工作，而是像乐团一样必须同步；任何一部分失准，整个演出就崩塌。衰老因而不是某个蛋白的故障，而是乐团整体的走调。

## 词汇分级

### ⭐⭐⭐ 高级

| 词/短语 | 释义 | 原文例句 |
|---|---|---|
| the quality control and recycling machinery of the cell deteriorates | 细胞的质量控制与回收机制逐渐劣化 | "As we age, the quality control and recycling machinery of the cell deteriorates, leading not only to neurodegenerative but also many other diseases of old age, including inflammation, osteoarthritis, and cancer." |
| humorously named | 诙谐地命名为 | "Ron Laskey, one of my fellow scientists in Cambridge, humorously named these proteins chaperones." |
| Like Victorian chaperones during courtship | 就像维多利亚时代求偶期的陪护人 | "Like Victorian chaperones during courtship, these proteins prevent improper interactions between different parts of the chain or between chains." |
| prevent improper interactions | 阻止不当的相互作用 | "Like Victorian chaperones during courtship, these proteins prevent improper interactions between different parts of the chain or between chains." |
| can handle only one scrap at a time | 一次只能处理一块残余 | "Like the garbage disposal in your kitchen sink, it can handle only one scrap at a time." |
| the huge garbage recycling center in your city | 你所在城市的巨型垃圾回收中心 | "If the proteasome is akin to the garbage disposal in your kitchen sink, the lysosome is the huge garbage recycling center in your city." |
| the brake is activated all the time | 刹车始终处于制动状态 | "It's like driving a car in which the brake is activated all the time instead of only in response to a signal to slow down or an accident ahead." |
| play their parts together | 各尽其职地协同演奏 | "It is not unlike all the instruments in a symphony orchestra that all have to play their parts together." |
| the unfolded protein response | 未折叠蛋白反应 | "Cells have an elaborate sensor to detect the buildup of unfolded proteins. The unfolded protein response, as this is known, is multipronged" |
| the integrated stress response (ISR) | 整合应激反应 | "Since it is a unified response to many kinds of stress, it is called the integrated stress response, or ISR." |
| the buildup of unfolded proteins | 未折叠蛋白的堆积 | "Cells have an elaborate sensor to detect the buildup of unfolded proteins." |

### ⭐⭐ 进阶

| 词/短语 | 释义 | 原文例句 |
|---|---|---|
| neurodegenerative | 神经退行性的 | "We all face the prospect of suffering from neurodegenerative diseases that cause us not just to forget but also to completely lose our sense of who we are." |
| unhinged | 失控的；精神错乱的 | "His patients, he wrote, would oscillate from periods of calm and lucidity to being unable to identify common objects, feeling increasingly disoriented, forgetful, agitated, and even unhinged." |
| hydrophobic | 疏水的 | "The reason that they fold up is that some amino acids, like oils, are hydrophobic, meaning that they do not like to be exposed to water." |
| hydrophilic | 亲水的 | "Hydrophilic amino acids, on the other hand, are happy to interact with water molecules." |
| misfold | 错误折叠 | "We can thus have proteins that are incorrectly made to begin with, or proteins that misfold later." |
| glycation | 糖化（非酶促糖基化） | "But as we age, sugar molecules are added randomly to proteins, a process called glycation, to distinguish it from the normal and orderly process of glycosylation." |
| glycosylation | 糖基化 | "Many proteins have extra sugar molecules added to specific points on their surface after they are made. This process, called glycosylation, is essential for their work." |
| cataracts | 白内障 | "For instance, eye diseases such as cataracts and macular degeneration result from proteins in the lens or retina of our eye being modified by sugar molecules" |
| macular degeneration | 黄斑变性 | "For instance, eye diseases such as cataracts and macular degeneration result from proteins in the lens or retina of our eye being modified by sugar molecules" |
| osteoarthritis | 骨关节炎 | "leading not only to neurodegenerative but also many other diseases of old age, including inflammation, osteoarthritis, and cancer." |
| the ubiquitin-proteasome system | 泛素-蛋白酶体系统 | "Any defect in the proteasome or the ubiquitin tagging system means that unwanted proteins hang around the cell and cause problems." |
| autophagosome | 自噬体 | "In the cell, membranous structures called autophagosomes form and grow in size, gradually engulfing everything the cell targets for disposal." |
| vacuole | 液泡 | "Ohsumi turned to that favorite of molecular biologists, baker’s yeast, in which the equivalent of the lysosome is called a vacuole." |
| autophagy | 自噬 | "De Duve coined the term autophagy, from the Greek for “self-eating,” because the cell was digesting away parts of itself." |
| molecular machine | 分子机器 | "The birth of a protein chain takes place on the ribosome, the large molecular machine that I have studied for the last forty-five years." |
| multipronged | 多管齐下的 | "The unfolded protein response, as this is known, is multipronged" |
| misfolded | 错误折叠的（过去分词） | "induces each normal prion protein it encounters to switch to the misfolded version." |
| aberrant | 异常的 | "First, more chaperones are synthesized to aid in folding these aberrant proteins." |

### ⭐ 基础

| 词/短语 | 释义 | 原文例句 |
|---|---|---|
| neurodegenerative diseases | 神经退行性疾病 | "We all face the prospect of suffering from neurodegenerative diseases that cause us not just to forget but also to completely lose our sense of who we are." |
| accumulation | 积累 | "Cells have an elaborate sensor to detect the buildup of unfolded proteins." |
| a prion | 一种朊病毒 | "misfolded, scrapie version of the protein acts as a mold, or template, and induces each normal prion protein it encounters to switch to the misfolded version." |
| autophagy | 细胞自噬 | "De Duve coined the term autophagy, from the Greek for “self-eating,” because the cell was digesting away parts of itself." |
| digest | 消化；分解 | "He and his Leuven colleagues found they were full of digestive enzymes that would break down any of the major constituents of living matter." |
| commit suicide | 自我毁灭（细胞凋亡） | "In extreme cases, where these measures are inadequate, the unfolded protein response can simply direct the cell to commit suicide." |
| disposal | 处置；处理 | "All kinds of unwanted structures were taken to lysosomes for disposal." |

## 一句话总结

**本章的真正问题是：细胞不是被外力摧毁的，而是被自己的废物淹没的——当回收系统追不上生产速度，那些本该被拆解回收的蛋白碎片便堆积成块，而其中最致命的一种聚集物，恰好就叫阿尔茨海默。**
