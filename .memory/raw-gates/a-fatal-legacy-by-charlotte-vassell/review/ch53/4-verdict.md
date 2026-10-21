# ch53 · R5 判定表

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch53 callie is finally sick.md`
> 唯一权威源：`text/ch53_53.txt`（78 行 / 2786 字符）
> 交叉源（仅用于核分部名，epub 内 `OPS/`）：`library/A Fatal Legacy (Charlotte Vassell) ….epub`
> 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch53/`
> 本次**未改动书目录任何 md，未 git add/commit**（只写本落盘目录）。

## 0. 覆盖声明

- 本次只审 **第 53 章**（委托指定单章）。R1–R5 全跑：素读（`1-suread.json`）→ 机器层（`2-machine.json`）→ 三张单子（`3-diff.md`）→ 逐块对应（`4-correspondence.md`）→ 判定表（本文件）。
- **其余 53 章：只有书级机器层**（`check_vocab.py` 全书 exit 0、`corruption_scan.py` 全书 FAIL 0、`verify_corpus.py` ch53 PASS、`bookform.py` 形态统计），**未做单章 R1 素读 / R4 人判**，**不写成「通过」**。
- 机器层覆盖限制：`chapter.sh` 对 ch53 退出码 **0（ok）**、5/5 引语逐字命中、中文层无低密度、形态无偏离——但它**不检查说话人、关系状态、分部名、计数措辞**，故「机器全绿」**不能**推出本章无缺陷；本表的 3 条阻断型全部落在机器读不到的那一层。

## 1. 四组数（只报这四组）

| 组 | 数 | 说明 |
|---|---|---|
| **逐字** | **5/5 命中（0 阻断）** | 5 个引语块整段逐字命中 `text/ch53_53.txt`（`2-machine.json`：`ok=true`，pos 196 / 1241 / 1606 / 2251 / 2407），人工按字符区间复核一致；无省略号拼接、无跨话轮缝合。词汇表 26 条例句全部锚定本章（`check_vocab.py` exit 0）。 |
| **对应** | **5/5 对应**（**1 块引语选短**；0 不对应；0 密度不足） | 每块中文都在讲本块引语本身；无「讲全书主旨/作者生平」块；每块均有「为什么这样写」＋「读者视角提示」两层。原句 4 的分析依赖引语外 `:65` ⇒ 引语选短（提示型，见 3-diff 漏-2）。 |
| **形态** | **1/1 章符合**（**1 条提示**） | H1 `# 53. Caius and Callie’s Flat` ✔（本书 H1 众数「N.」54/54）；导航 **5 项**、项名 `一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法` 与本书众数**完全一致** ✔；子项集 `中文理解 / 关键词 / 为什么这样写 / 读者视角提示` 4 项 ✔（与 profile 一致）；块数 **5**＝本书下沿（众数 7、范围 5–10、profile 3–10；全书 54 章中 5 章为 5 块），**在范围内但未写理由** ⇒ 提示 1 条。 |
| **断言** | **12 条**（**阻断 3 / 提示 8 / 假红 0 / 跳过 1**） | 见下表。 |

> **阻断型条数：3**（均为「与原文/原书不符」，不是措辞问题）。

## 2. 判定表

| # | 断言 | 证据（章:区间／文件:行） | 结论 | 档位 |
|---|---|---|---|---|
| B1 | 导航写「分部『A Tuesday in May』把这一切处理得很轻」 | `ch53 …md:15`；原文 `text/ch53_53.txt` 全章无 "Tuesday"/"May"/任何分部标题（唯一分部标题 `:17` `Caius and Callie’s Flat`）；epub：本章 `OPS/s071-Chapter-053.xhtml`（`<h2>Caius and Callie’s Flat</h2>`，正文与 text/ 逐字一致）所属分部 `OPS/s069-Part-011.xhtml` = `<h1>TUESDAY</h1>`；全书唯一的「A … IN MAY」是 `OPS/s008-Part-001.xhtml` = 「A FRIDAY IN MAY」（第一部，与本章无关） | 分部名系拼错：把 FRIDAY IN MAY 与 TUESDAY 拼成「A Tuesday in May」，全书不存在，且用书名号当事实陈述 | **阻断** |
| B2 | 分析称 Caius 为 Callie 的「丈夫」（`:44`、`:51` 两处） | `ch53 …md:44`「她的**丈夫**刚数出三样她的享乐」、`:51`「她先夸了**丈夫**一句」；`text/ch53_53.txt:20–77` 无 husband/wife/married 任何婚姻表述；`text/ch40_40.txt:59–61`「'You can have the wedding here,' Marcus said.」「'If we pull our finger out you could have it in August. …'」→ 婚礼在未来；`text/ch52_52.txt:41`「'I found out about the engagement rings, by the way.'」→ 订婚；`text/ch27_27.txt:101`「'I refer to him as my "paramour" and he refers to me as his "missus". It's an equal partnership.'」 | 二人是**未婚夫/伴侣**，全书到 ch53 未婚；「丈夫」凭空升级婚姻关系 | **阻断** |
| B3 | 分析称「**三个「No」**连着一句「Yes」」，中文理解写作「连着说了三句「不。对。不」」 | `ch53 …md:30`、`:28`；原文 `text/ch53_53.txt:44`「'No. Yes. No.' Callie reached for the fabric on the table.」→ 三词＝**2×No + 1×Yes**（Yes 在中间），不是 3×No + 1×Yes（那是四词） | 对引语本身的计数错误；且 `Yes` 译作「对」读作「正确」而非「好／想」。（同 md `:11`、`:29` 写对了 `No. Yes. No.`，属章内自相矛盾） | **阻断** |
| P1 | 导航「给人梳头」 | `ch53 …md:12`；`text/ch53_53.txt:35`「Callie fell into his lap and **he stroked her hair**.」 | 原文是抚摸/顺头发，非梳头 | 提示 |
| P2 | 导航「把手机递过去」 | `ch53 …md:12`；`text/ch53_53.txt:47`「Caius **took his phone out and showed Callie some of the stills** from the footage of the little robot's second journey.」 | 掏出手机给她看剧照 ≠ 把手机交给她（主语方向未反，但动作错） | 提示 |
| P3 | 「她嘴上推掉，手上却在搓那块碎布」 | `ch53 …md:44`；`text/ch53_53.txt:44`「Callie reached for the fabric on the table. **She rubbed it between her fingers.**」（前一场）；到 `:68` 她的动作只有「Callie stuck her tongue out.」 | 搓布是前一场动作，此刻仍在搓无原文依据（时序外移） | 提示 |
| P4 | 「信是从茶几上拿起来的，**不是当场拆开的**，说明她早就知道内容」 | `ch53 …md:51`；`text/ch53_53.txt:74`「Callie picked a letter up off the coffee table. 'We've had the date for the twelve-week scan come through.'」 | 原文没写「不是当场拆开的」——无逐字依据的否定推断 | 提示 |
| P5 | 骷髅 / “dead nun” / “earthly” 一节（6 个话轮）未进任何引语块，也未进导航 | 原文 `text/ch53_53.txt:50`「'Were there any skeletons in the end?'」、`:53`「'Yeah, hundreds of them. I've never heard the words "dead nun" spoken so many times.'」、`:56`「'I really would've been a terrible nun.'」、`:59`「'You're too earthly.'」、`:62`「'Earthly?'」、`:65`「'You like pleasure too much. Pinot Grigio, pistachio croissants and getting railed.'」；md 全文只在词汇表 `:76` 出现一次 | 漏；属可取舍范围（本章主动作已覆盖），但 md 未写取舍理由，且这是「新房子下有人骨」暗线唯一一次露头 | 提示 |
| P6 | 原句 4 的引语选短 | `ch53 …md:26`（引语止于 `:68`）；分析 `:44` 依赖引语外 `text/ch53_53.txt:65`「'You like pleasure too much. Pinot Grigio, pistachio croissants and getting railed.'」 | S2「分析覆盖的原文比引语长」同类；建议把引语扩到 `:65`，或在分析里点明「上一句他刚数出三样」 | 提示 |
| P7 | 字词与格式 5 处小瑕 | `:99`「底下那点**不安全**靠生活细节垫着」（按语义应为「不安」）；`:31`「而不是**Jen** 那边的进展」（缺空格，且原文她谈的是 Venetia 带来的消息，未谈 Jen 那边）；`:44`「床上那点事」对 `getting railed`（语域降级）；`:21`/`:44`「碎布」与词汇表 `:66`「swatches｜布样；色卡」用词不一；`:95` 词汇例句 `| hundreds | 数百个 | 'Yeah, hundreds of them. |` 右引号缺失 | 措辞与排版，不影响事实 | 提示 |
| P8 | 形态：块数 5 = 本书下沿，md 未写理由 | `ch53 …md` 全文 5 块；`bookform.py`：「每章块数：中位 7.0，范围 5–10」「profile mystery-thriller…块数 3–10」；实测全书 54 章中 5 章为 5 块（含本章） | 在本书范围内、且有同例，不判错；但按体裁纪律应补一行理由（本章对话密集、块数偏少） | 提示 |
| S1 | 汇总层（`00_概述.md` / `00_金句精选.md` / `00_情感节点.md`）对本章的引用与断言 | 不在本次委托范围 | **未查**（如实标注，不写成「通过」） | 跳过 |

**假红：0 条。** 机器层 `chapter.sh` 对本章退出码 0、`issues` 四类全空——它没有误报，也没有覆盖到 B1–B3 这层（关系状态／分部名／引语计数措辞），这是**覆盖面限制**而非假红。

## 3. 已核实为正确（防误修，不得以「读着不对」为由改动）

1. **PCQV 与唱片公司未被混同**（`:11`「转而说起 PCQV 的合约黄了、唱片公司人心惶惶」；`:28`「跟 PCQV 的合约显然已经作废；唱片公司上下都在慌」；`:99`「把话头岔到 PCQV 合约作废与唱片公司的惊慌上」）。原文 `text/ch53_53.txt:44`「The deal's off with PCQV, obviously. Everyone at the record label is panicking because they're not sure how much they knew, if that makes sense.」PCQV＝法国奢侈集团（彩妆/香氛线，见 ch36 md `:11`「法国奢侈集团 PCQV」「欧拉莉亚自己的唱片公司是另一方」），与唱片公司是两个主体；md 三处分列，**正确**。
2. **扫描日期是「通知到了」，不是「已经做完了」**（`:49`「说十二周扫描的日期已经通知下来了」；`:11`「十二周扫描的日期定下来了」；`:99`「那封通知信里十二周扫描的日期」）。原文 `text/ch53_53.txt:74`「We've had the date for the twelve-week scan come through.」＝日期通知到位；md 全篇无「扫描已完成」的意思，**正确**。
3. **本章没有「电话那头」**：原文全章无任何电话对话（手机只用于展示剧照，`:47`）；md 全文亦无「电话那头」字样，**没有凭空造出电话内容**。（ch18 md 的「电话那头」指 Venetia 那通电话 `text/ch18_18.txt:44`，与本章无关。）
4. **「六个开心果可颂」数字逐字一致**：原文 `:20`「bought **six more** pistachio croissants」；md `:11`「六个开心果可颂」、`:99`「六个可颂」——数字正确。
5. **导航「Callie 吐过之后」成立**：`:26`「Callie came out of the bathroom and flopped onto the sofa. 'I was finally sick.'」先吐后说。
6. **块 3 的「他们」指唱片公司、未错配到 PCQV**：`:47`「'They're definitely morally culpable if not legally.'」的 `They` 承 the record label，md `:35` 表述未错。
7. **词汇表 26 条例句全部锚定本章**（`check_vocab.py` 全书 exit 0，ch53 无 FAIL/WARN）。

## 4. 取证记录（R5-补：命令 + 输出 + 退出码）

```
$ bash scripts/chapter.sh "notes/books/.../ch53 callie is finally sick.md" --json > 2-machine.json
  → verdict "ok"；quotes 5/5 ok=true；counts: segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0；退出码 0

$ python3 scripts/verify_corpus.py "<书目录>"
  → ch53 (52 句) 首| 53  末| He got up off the sofa and went to peg the washing out on the line.
  → P0-0 语料验收: PASS（FAIL 0 / WARN 3，WARN 为全书级）；退出码 0

$ python3 scripts/check_vocab.py "<书目录>"
  → 退出码 0；输出无 ch53 行（ch53 无 FAIL/WARN）

$ python3 scripts/corruption_scan.py "<书目录>"
  → FAIL 0 处（U+FFFD / 双句号）；报告 0 处；退出码 0

$ python3 scripts/bookform.py "<书目录>"
  → H1 {'N.': 54}；导航项（众数 5 项）：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法
    子项集（众数 4 项）：中文理解 / 关键词 / 为什么这样写 / 读者视角提示
    每章块数：中位 7.0，范围 5–10；profile mystery-thriller（块数 3–10）；退出码 0

$ /usr/bin/grep -ril "tuesday" .        # 书目录内全量（text/ + 全部 md）
  → ./ch53 callie is finally sick.md      （仅此一处，即被编造的那行）；退出码 0
$ /usr/bin/grep -n -i -E "monday|tuesday|wednesday|thursday|friday|saturday|sunday" text/*.txt
  → 37 行命中，全部为正文用词，无任何分部标题；退出码 0
$ /usr/bin/grep -n -i -E "husband|wedding|married|wife|fiancé" text/*.txt
  → 命中均在他人婚事/婚礼与 ch40（本章当事人的婚礼尚在未来）；退出码 0
```

**epub 内部核对**（`OPS/` 解包后直接读，未修改）：`s071-Chapter-053.xhtml` 的 `<h2 id="h253">Caius and Callie’s Flat</h2>` 与正文首尾均与 `text/ch53_53.txt` 一致；其前一分部文件 `s069-Part-011.xhtml` 标题为 `<h1 id="h167">TUESDAY</h1>`；`s008-Part-001.xhtml` 标题为 `<h1 id="h16">A FRIDAY IN MAY</h1>`。
