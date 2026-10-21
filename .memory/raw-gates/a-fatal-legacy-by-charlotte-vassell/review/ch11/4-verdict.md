# ch11 判定表（R5）

> 审查员：独立审查员｜**只负责第 11 章**
> 原文（唯一权威源）：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch11_11.txt`
> 被审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch11 matt and amy sort digbys papers.md`
> 区间记法：`text/ch11_11.txt:<行号>`（行号即证据）；需要字符偏移时给 `[start,end)`（Python 读全文，0 起算）。
> 取证日志：`5-evidence.txt`（命令 + 输出 + 退出码，R5-补要求）
> 机器层原始输出：`2-machine.json`｜素读底稿：`1-suread.json`｜三张单子：`3-diff.md`｜逐块对应：`4-correspondence.md`

---

## 〇、覆盖声明

- **本次只审 ch11 一章**，人判层（R1 素读 / R3 对账 / R4 逐块 / R5 判定）全部落在 ch11。
- 其余 53 章**未跑人判层**——不得写成「通过」；本章报告中涉及全书语料的 `grep` 仅为取证交叉比对，**不构成对他章的判定**。
- ch11 机器层：`bash scripts/chapter.sh "…/ch11 matt and amy sort digbys papers" --json` → **退出码 0**（`verdict: ok`）。`2-machine.json` 中 `segment_miss:0 / struct_bad:0 / empty_quote:0 / keyword_bad:0 / cjk_low:0`。
- 机器层之外我另做了一次**独立字节级复核**（不经 `bookform.py` 的 `norm()` 归一化，直接在原文里找完整引语串），结果同样是 8/8 命中，含弯引号。

---

## 一、四组数

| 组 | 数 | 说明 |
|---|---|---|
| **逐字** | **37/37 命中，0 不一致** | 8 个引语块（字节级全串比对，含 `‘ ’ “ ”` 弯引号）＋ 29 条词汇例句（`grep -F` 式全串命中）＝37 项。词汇表 32 行中另有 3 行是表头（`词/短语｜释义｜例句`），非例句。 |
| **对应** | **8/8 块主题对应，0 不对应** | 每块的中文都确实在讲自己那句引语；无「讲引语之外的上下文」「讲全书主旨/作者生平」「只复述字面无为什么」三类不对应。但其中 2 块在**归属/结构层**出错（原句 3、原句 6），已计入断言组。 |
| **形态** | **0 偏离** | H1 / 导航项名与项数 / 子项集 / 块数 四项全部落在本书众数内，**无需写偏离理由**（详见 §三）。 |
| **断言** | **共核 18 条：阻断 3、提示 15、假红 0、跳过 0** | 逐条见 §二（A1–A3 阻断、B1–B15 提示）。 |

**阻断型合计 3 条**（A1 主语归属、A2 结构讲反、A3 漏动机线两个数）。

---

## 二、断言判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | `md:35`「凯厄斯说，**他母亲**写信告诉迪吉」——写信人是凯厄斯的母亲 | 原文 `text/ch11_11.txt:85`「**His mum** wrote to him saying they'd talk about the future of the Institute when she got back,’ Caius said, remembering the postcard sent from Goa on the fridge.」；同句前文 `text:82` 谈的是 `Digby isn’t the only person who has a share of the property`；卡片实物 `text/ch04_4.txt:56`「…Let's talk about the Institute when I get back on 27th. **Mum x.**」（寄自 Goa 的明信片＝芬内拉写给迪吉）；芬内拉在 `text:172` 自述「Digby had written to say that he had a plan for the Institute」 | `His` 指**迪吉**（芬内拉写给迪吉），非凯厄斯。中文里「他母亲」紧跟在「凯厄斯说」之后，按默认指代绑定到凯厄斯，等于凭空造出一段母子关系；md 自己 `md:28` 写的是「迪吉的母亲芬内拉」，`md:11`/`md:123` 也写「母亲芬内拉」，块内自相矛盾。R4 固定追问③「谁的」归属回原文定方向即命中此项 | **阻断** |
| A2 | `md:59`「一摞『机构文件』里混进了死者的私人决定，而『私人信件』里又装着整个馆的处置方案」＋ `md:13` 尾「私人信件与馆藏文件最终被塞进同一个文件夹」——私人信件与馆藏文件分属两摞、互相渗透 | 原文 `text/ch11_11.txt:126`「There was **another letter kept in the same folder**, offering the rest of the collection to the Royal Geographical Society…『Also unsigned and undated.’」——**同一个文件夹里的两封信都是机构信**（一封致部里的遣返函，一封致皇家地理学会的出手函）；**唯一那封私人信件**是 `text:85` 冰箱上的明信片，卡片实物见 `text/ch04_4.txt:56`，它不在任何文件夹里、也不在警局案情室的这摞纸上 | 原文的「模糊点」在**同一文件夹内**：两封机构信都是未署名未署日期的草稿（机构形式、私人决定）；md 却把「私人信件」写成与机构文件分置两摞、并把「整个馆的处置方案」（=致皇家地理学会那封）放进「私人信件」摞。这既与 `text:126` 的 `the same folder` 冲突，也与**同块 `md:58`「被并排塞在一处」自相矛盾**（一句之内两套结构）。本章专属判据问的正是「私人信件与馆藏文件的分界在哪一摞被翻出来时开始模糊」，md 给的答案在原文里不存在 | **阻断** |
| A3 | 本章动机线的两个数（两百万英镑估值、「受托人只剩两人」）**完全未出现在 md 中**，而 `md:13` 导航却承诺了这条线索 | 原文 `text/ch11_11.txt:76`「‘**Two million pounds**. Imagine what it'll be worth once they put electricity in,’ Caius said.」；`text:73-74`「…reading through a glossy booklet…『Digby had the property valued last week.』」；`text:196`「‘**It's just the two of us now.** My aunt had been on the board until she died three years ago.」＋`text:198`「God knows we could've done with the money. I kept telling Digby that he could use his part to go and have adventures of his own.」；md 侧 `md:13`「**房产估值与共有份额（动机）**」 | md 全文零命中：`5-evidence.txt` E1（`两百万\|百万英镑\|million` → 0，退出码 1）、E2（`受托人只剩\|就剩我们\|就剩我们俩` → 0，退出码 1）。**须说清：动机线的引子并未全缺**——`md:114`（`share`）与 `md:115`（`property`）的例句正是 `text:82` Matt 那句「a share of the property」，在词汇表里在场；缺的是把这条线钉死的估值数字（`text:76`）与受托人只剩两人（`text:196`）。这是 ch09 白板「谁继承研究所」的答案（「It's worth a bomb… I wonder who inherits the Institute with Digby gone?」，`text/ch09_9.txt:74-75`），也是全书动机主轴，且 md 自己在导航里认领了这条线——**同一文件内导航与正文不一致**，读者按导航去找会落空 | **阻断** |
| B1 | `md:37`「这封私人信件的证据形态是一张**冰箱贴**」 | 原文 `text/ch11_11.txt:85`「the **postcard** sent from Goa on the fridge」；卡片实物 `text/ch04_4.txt:56`「a **postcard** of a Goan beach clinging to the front of it」；同块 `md:35` 自己写的是「贴在迪吉冰箱上的**明信片**」 | 物件被认错：冰箱磁贴≠明信片，且与同块「明信片」自相矛盾。论证主体（私人信件的物理位置＝家的那一摞）不受影响，属用词级；一字可改 | 提示 |
| B2 | `md:58`「一封要把藏品**整体出手**」 | 原文 `text/ch11_11.txt:126`「offering **the rest of the collection**」；同文件 `md:56`「愿意把**其余**藏品交给皇家地理学会」、`md:13`「把**剩余**藏品交给皇家地理学会」 | 原文是「其余」——七具人头骨那封走的是遣返线（`text:102`），两封信互补而非重叠；「整体」抹掉了这个区分。与 `md:13`/`md:56` 自相矛盾；一处用词 | 提示 |
| B3 | `md:14`「走到**当众**把'harm'改口成'murder'」 | 原文 `text/ch11_11.txt:145-166` 是一对一问询室内的对话（芬内拉与凯厄斯；`text:63` 另有家属联络警员接手，`:145` 之后场景仅二人） | 无公众在场；「当众」把私密问询写成公开场面。同句其余部分（「以为只是个旧宅」亦为 md 转述，见 §四） | 提示 |
| B4 | `md:12`「地点**始终**是警局的案情室」 | 原文 `text/ch11_11.txt:73`「…when Caius **came back into** the incident room」（说明他此前不在案情室）；`text:60-63` 道歉与首轮问询在另一间房 | 「始终」不成立；警局内至少两个房间 | 提示 |
| B5 | 《Our Apologia》在 ch11 内有三种译名（自白书／我们的自辩书／辩白书；自辩） | 原文 `text/ch11_11.txt:190`「He called it "**Our Apologia**"」；md 侧 `md:13`「计划写成的**自白书**」、`md:70`「《Our Apologia》（我们的**自辩书**）」、`md:83`「Apologia｜**辩白书；自辩**」；他章 `ch13 …md:85`「Apologia｜**自辩书**（拟议书名）」 | 一书三名；「自白」与 apologia（为自己申辩/致歉书）语义不合。ch13 用「自辩书」，ch11 应与之统一 | 提示 |
| B6 | `md:82` 词汇条释义「toi moko｜**毛利人对待敌人遗骨的方式**，此处指人头骨」 | 本章原文 `text/ch11_11.txt:99`「the **repatriation of human remains**」、`:102`「seven **toi moko or mokomokai** from New Zealand」——本章只作名词使用，**未给词义**；他章 `text/ch02_2.txt:285` 的说明是「preserved as a way to honour their ancestors by showcasing their **tattoos**」 | 释义属书外补入且描述不准（toi moko 是纹饰人头本身，非「对待遗骨的方式」）。附注：`md:42`「毛利人头骨」与全书口径（`ch38:117`「骸骨之手」、`ch39:75`「缩头与 mokomokai」、`00_概述.md:14`「七具新西兰人头骨」）一致，**不是缺陷**，不必动 | 提示 |
| B7 | `md:51`「和那些**早已办妥**的馆藏文件摞在一起」 | 原文 `text/ch11_11.txt:120`「It hasn't been dated, or signed yet」、`:126`「Also unsigned and undated」 | 本章未说这批文件「早已办妥」；且同一文件夹里那封同样未署名未署日期 | 提示 |
| B8 | `md:72`「把这个家里**几十年**来的遮遮掩掩说成了一次具体的动作」 | 本章原文 `text/ch11_11.txt:178`「My father was curator before Digby took over… I spent far too much time there as a child」、`:180`「Digby had graduated the summer before and was at a loss because of the recession so he took it on」 | 本章未给年代跨度（「几十年」为书外推断） | 提示 |
| B9 | `md:49`「艾米把那封信**翻来覆去**看了看」 | 原文 `text/ch11_11.txt:120`「Amy said, **looking the letter over**」 | 原文是「把信端详一遍」，「翻来覆去」是动作上的添笔 | 提示 |
| B10 | 原句 5 的分析用了**引语外**的下一句（引语边界外扩） | 引语只到 `text/ch11_11.txt:120`；`md:51`「凯厄斯随即判断这封信是在等母亲回来后才发」的判断依据在 `text/ch11_11.txt:123`「‘He was waiting to speak to his mum,’ Caius said.」 | R4 第一档「引语选短」：分析依据落在引语之外。该块分析主体（无日期/无签名的含义）仍在引语内，密度不减 | 提示 |
| B11 | 原句 7 的「警方一开口用的是 harm」依赖**引语外**的 `text:151` | 引语为 `text:154`（`'Harm?' she whispered…`）；警方的 `harm` 在 `text/ch11_11.txt:151`「‘We’re just trying to ascertain why anyone would want to harm Digby.’」 | 同属引语选短信号；块内分析主体（harm→murdered 的升级）在引语内成立 | 提示 |
| B12 | 漏：第三封信（某学者来信，约两周前） | 原文 `text/ch11_11.txt:132`「‘Oh and there was a letter from some academic asking to set up a meeting. That was from two weeks ago.’」 | md 无。取证 `5-evidence.txt` E3（`学者\|学术\|求会面\|约见` → 0，退出码 1）。本章唯一带日期的信、唯一指向外部学术机构的线索，漏掉后「两封未署名未署日期」的对读少一个反差坐标 | 提示 |
| B13 | 漏：迪吉想关停研究所 | 原文 `text/ch11_11.txt:172`「‘Digby had written to say that he had a plan for the Institute. I think he wanted to **wind it down**.』」 | md 无。取证 `5-evidence.txt` E5（`关停\|收掉\|解散\|停掉\|wind it down` → 0，退出码 1）。这是两封信的动机前提 | 提示 |
| B14 | 漏：「没有遗嘱」这个答案 | 原文 `text/ch11_11.txt:199-202`「were you aware whether or not Digby had made a will?’／‘**Not that I know of.** He was young.’」 | md 只在 `md:119` 词汇表引了提问句，答案未写。取证 `5-evidence.txt` E6（`没有遗嘱\|未立遗嘱\|没立遗嘱\|没遗嘱` → 0，退出码 1） | 提示 |
| B15 | 漏：Nathan（迪吉最好的朋友）与「住址簿」这条待查线索 | 原文 `text/ch11_11.txt:214`「No. **Nathan's** a nice boy. Yes, Nathan was his best friend.」、`:220`「I'm sure Digby will have an **address book**.」 | md 无。取证 `5-evidence.txt` E4（`Nathan\|内森\|住址簿\|地址簿` → 0，退出码 1） | 提示 |

---

## 三、形态组（逐项对照本书众数）

| 形态项 | 本章实测 | 本书众数/profile | 偏离 |
|---|---|---|---|
| H1 | `# 11. The Police Station` | 原文 `text/ch11_11.txt:17` 小标题即 `The Police Station`；本书 54 章一律 `# NN. <本章节标题>` | 无 |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 全书 54 章**逐章一致**为这 5 项、5 项（`2-machine.json`：`nav_count:5`、`nav_counts:[5]`、`nav_missing:[]`） | 无 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | profile `mystery-thriller` 的 `profile_subitems` 完全相同（可选 `句子结构` 未用） | 无 |
| 块数 | 8 块 | 全书中位 7.0、区间 [5,10]（54 章分布：6×19、7×10、9×8、10×7、8×5、5×5） | 无（8 落在 [5,10] 内） |

→ **形态组 0 偏离**，无需写偏离理由。
→ 附注（非偏离）：ch11 导航未标分部「A MONDAY IN MAY」；全书 54 章中 26 章标了、28 章没标，相邻的 ch09/ch10/ch12 也没标，属非强制项，不计入偏离。

---

## 四、R5.5 已核实为正确（防误修，固定一节）

以下写法**看起来像错、回原文核对后成立**，后续任何人不得以「读着不对」为由改动：

1. `md:28`「迪吉的母亲芬内拉在楼下」——与 `text/ch11_11.txt:38`「'Digby's mother Fenella is downstairs'」逐字相符。**（与 A1 同一章内两处不同写法：A1 的错在 `md:35`。）**
2. `md:63` 原句 7 的说话人归属「芬内拉…冲凯厄斯喊了出来」「他们不是在胳膊上捏一把」——`text:154`「'Harm?' she whispered… somehow found herself **shouting at Caius**… They didn't **pinch him on the arm**. They murdered him!'」全部对上，无误。
3. `md:70` 原句 8 的说话人与指代：「母亲说…」——`text:189-190` 是芬内拉回答「And what was his idea?」；「**他**开始对馆里的藏品感到不安，**她**也一样」对应 `text:190`「He had begun to feel uncomfortable with the collection. **We both did.**」——`We`＝迪吉＋芬内拉，md 归属正确，未误派给他人。
4. `md:56` 原句 6 的说话人「艾米扫着另一封信说」——`text:126`「Amy said, **scanning the other letter**」逐字相符。
5. `md:38`「这一封已经寄出、**署名**」——明信片署名 `Mum x.` 见 `text/ch04_4.txt:56`；本章 `text:85` 亦有 `sent from Goa`。为真（依据在他章，本章未给），**不必改**。
6. `md:42`「七具来自新西兰的毛利人头骨」——与 `text:102`「seven toi moko or mokomokai from New Zealand」相符；与 `ch38:117`「骸骨之手」、`ch39:75`「缩头与 mokomokai」、`00_概述.md:14`「七具新西兰人头骨」口径一致，**全书统一，不必改**。
7. `md:14` 人物弧线「芬内拉从『以为只是个旧宅』走到…」——前半可回 `text:178`「It's a **mausoleum**. My father was curator before Digby took over… Hated it. Utterly hated it.」＋`text:180`「he took it on」（她本就把这地方当负担、想脱手）＋`md:89` 已收录 `mausoleum｜陵墓；阴森森的旧宅`——**该转述成立**，勿改；同句的「当众」见 B3（措辞级）。
8. `md:66` 原句 7 读者视角提示「谁在说'harm'，谁在说'murdered'」——原文确为二人分说：`text:151` 警方「…why anyone would want to **harm** Digby」、`text:154` 芬内拉「They **murdered** him!」。成立。
9. `md:11`「两封未署名、未署日期的信」——`text:120`「It hasn't been dated, or signed yet」＋`text:126`「Also unsigned and undated」，**逐字属实**（第三封信另有日期，见 B10，两者不矛盾）。
10. `md:44` 原句 4 的「两次 et cetera」——`text:102` 结尾「…proper channels et cetera, et cetera.」确为两次，成立。

---

## 五、跨文件观察（**不属本章 md 的缺陷**，仅提示别处复核）

- 全书语料中 `Two million/two million` **只出现在** `text/ch11_11.txt:76`，`two of us` **只出现在** `text/ch11_11.txt:196`（取证 `5-evidence.txt` E9/E10）。
- 但 `00_概述.md:14`、`00_情感节点.md:46`、`00_金句精选.md:82` 把「上周刚估过两百万英镑」「就剩我们俩了」记在**白板章（ch09）**名下。ch09 原文（`text/ch09_9.txt:65,74-75`）只有「I doubt he had a couple of million **in the bank**」（且是否定式，指迪吉个人存款）与「It's worth a bomb… who inherits the Institute with Digby gone?」——**这两个答案在语料里属于 ch11**。这三条总览文件把 ch11 的答案安到了 ch09 的场景上，**建议由总览章的审查员复核**（本章不判其对错）。

---

## 六、复核者指引（三行摘要）

1. **最要紧的一条：A2**——`md:59` 与 `md:58` 对同一组文件给出两套互斥结构（一个说「同一个文件夹」，一个说「两摞互相渗透」），原文 `text:126` 只有一种结构；本章专属判据问的正是这个分界点，md 在此处答反了。
2. **A1 是本库最典型的机器查不出的错**：引语逐字 ✓、中文是中文 ✓、关键词 ✓、形态 ✓ 四道探针全绿，只有 R4 的「谁的/谁的」归属追问能抓住它（`md:35` 的「他母亲」绑错了人）。
3. **A3 的修法最省事**：把 `text:73-82`（两百万估值＋共有份额动机）与 `text:196-198`（受托人只剩两人＋姨母三年前去世＋「本可以用那笔钱」）立成 1–2 个块即可，导航 `md:13` 的承诺就兑现了。
4. **修 A2 时不要动 `md:58`**：`md:58` 的「被并排塞在一处」与原文 `the same folder` 一致，是本章写得最准的一句；`md:59` 才是写反的那一句。
