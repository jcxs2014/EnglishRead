# 4-verdict · ch39《A Fatal Legacy》独立审查判定

> 审查方：独立审查员（第二轮，接手上一位卡死的 R1/R2）
> 被审对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch39 the institute is to be sold.md`
> 语料：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch39_39.txt`（6030 字符，129 行）
> 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch39/`（1-suread.json / 2-machine.json / 3-diff.md / 4-correspondence.md / 4-verdict.md）
> **本次审查只写落盘目录，未改书目录任何 md，未 git add/commit。**

## 0. 覆盖声明

- 本章 ch39 **全章审**（R1–R5 全部走完，非抽样）：R1 素读 → R2 机器层 → R3 对账 → R4 逐块 6/6 → R5 判定。
- 六块引语**逐块人判**（三问：讲的是不是这句引语 / 说话人 / 有没有讲到引语之外）。
- 另核：分部名（epub `OPS/toc.ncx`）、跨章术语（mokomokai 在 ch02／ch11 的既有写法）、词汇表例句、导航与总结的断言。
- 机器层（`scripts/chapter.sh --json`）退出码 0、四道探针全绿；**本轮阻断型 10 处全部落在机器层结构上查不到的那一层**（施事／受事／归属／词条释义），与「四绿 ≠ 没缺陷」一致。

## 1. 四组数

| 组 | 数 | 说明 |
|---|---|---|
| **逐字** | **6/6 命中，0 缺陷** | 6 段引语全部逐字（`2-machine.json`：`segments 6`、`segment_miss 0`、`empty_quote 0`）；另 `python3 scripts/check_vocab.py` 全书 FAIL 0，ch39 词表 30 条例句抽验全部命中本章 text。 |
| **对应** | **6/6 块对应，0 块讲引语之外的话** | 六块中文都在讲各自引语；**但 3 块（2/3/4）内含内容／归属错**，另 2 块（5/6）有归属含混提示。对应数与内容对错分开记。 |
| **形态** | **偏离 0** | H1 / 导航项名与项数 / 子项集 / 块数四项全部落在本书众数上（详见 §3）。 |
| **断言** | **27 条：阻断 10 · 提示 7 · 成立 10** | 10 处阻断 = 6 个根因（见 §2）。 |

**阻断型条数：10 处（6 个根因）。**

## 2. 断言表

| # | 断言（md 逐字） | 证据（章:区间／原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md:28 `使他没法把 mokomokai（毛利战鼓）归还` | ch39:75 `‘That was what was holding Digby back from returning the mokomokai…’`；ch39:129 `He talks about returning the shrunken heads here too.`（同一批藏品＝缩头）；ch11:102 `the Institute is in possession of seven toi moko or mokomokai from New Zealand`；ch02:285 `the mokomokai were preserved as a way to honour their ancestors by showcasing their tattoos` | mokomokai 是**风干毛利人头骨**，不是战鼓 | **阻断** |
| 2 | md:67 `\| mokomokai \| 毛利战鼓；此处指霍雷肖带回的毛利编年史木刻 \|` | 同上（ch39:75／ch39:129／ch11:102／ch02:285）；本书 ch02:125 已写「风干缩头」、ch11:82 已写「人头骨」 | 词条释义两处皆错，且与本书既有写法冲突 | **阻断** |
| 3 | md:15 `压在底下的是缩头、战鼓、人骨和一桩还没定价的谋杀` | ch39:129 `the shrunken heads`；ch02:285／ch11:102（同上） | 「战鼓」是错译；缩头＝mokomokai，非两物 | **阻断** |
| 4 | md:11 `归还缩头与 mokomokai 的打算` | ch39:129 `He talks about returning the shrunken heads here too.` + ch39:75（mokomokai）＝同物 | 一物当两物 | **阻断** |
| 5 | md:11 `他去研究所找那本失踪的日记` | ch39:41 `‘The missing journal is really bugging me. I’m going to go back to the Institute and see if I can find it first…’`（说话人 **Amy**）；ch39:44 `‘Try Digby’s house too.’ Matt knew well enough to go with Amy’s instincts.` | **施事写反**：回研究所的是 Amy，Matt 去的方向是 Digby 家 | **阻断** |
| 6 | md:11 `Amy 继续挖「假 Isolde」` | ch39:32 `‘You said you’d look into real Isolde again, right?… We need to work out how “fake Isolde” knew that much about her.’` | **受事写反**：要查的是**真实** Isolde，「假 Isolde」是被解释的对象 | **阻断** |
| 7 | md:110 `Matt 一边在警局接着查那本失踪的日记和「假 Isolde」` | ch39:41／ch39:32／ch39:44（同上） | 施事＋受事双错 | **阻断** |
| 8 | md:38 `注意这句里的降神会数量：它不是修辞，是账面` | ch39:90 `Although the sheer number of orgies seemed to point in the opposite direction.` | 引语里的计数是**群交**次数，不是降神会次数；md:37「为什么这样写」自己写对了（「群交的次数太多」），md 自相矛盾 | **阻断** |
| 9 | md:42 `尽管博物馆一直坚持那样塑造他` | ch39:99 `I don’t think Horatio was a great man, despite how he insisted we portray him, merely a well-travelled egotist with a grim collection.` | `insisted` 的施事是 **Horatio 本人**（他生前要求后裔那样写他），不是博物馆；md:44 整段论证建立在这个写反的前提上 | **阻断** |
| 10 | md:42 `她祖父小时候不是在上学就是住在母亲的亲戚家` | ch39:99 `My great-grandfather was either away at school or staying with his mother’s relatives while Horatio was off galivanting across the globe.` 与同句 `Horatio died while Aloysius, my great-grandfather, was in his last year at school, I think.` | 是**曾祖父**（Aloysius），md 同段末尾却写「她的曾祖父阿洛伊修斯」——md 内部自相矛盾 | **阻断** |
| 11 | md:106 `\| instincts \| 直觉 \|`（基础档） | 机器 WARN：`ch39 … [基础] 基础档疑含超纲词「instincts」` | 档位偏松（进阶词入基础档） | 提示 |
| 12 | md:49 `而她此前的许多封信都已经扔进了回收箱` | ch39:123 `I’d put so many of his letters in the recycling already.` | 归属含混：原文是**迪吉的**许多封信；中文省略物主后易读成「她的信」 | 提示 |
| 13 | md:51 `就顺手把成堆旧信扔进回收箱——销毁证据的动作和上交证据的动作同时发生` | ch39:123 `I’d put so many of his letters in the recycling already.` | 「顺手」「销毁证据」是分析加的定性，原文只是既成事实（过去时），且从未把这批信称作证据 | 提示 |
| 14 | md:51 `「karma」一词` | ch39:123 `But then that feels rather karmic, doesn’t it?` | 原文用词是 `karmic`（形容词） | 提示 |
| 15 | md:56 `迪吉想约她吃午饭` | ch39:129 `He wanted to arrange to go for lunch to discuss an offer for the Institute he’d received, which he also enclosed.` | 原文未指明午餐对象（语境是报价方），「她」易误读为芬内拉 | 提示 |
| 16 | md:35 `那只断手会不会是她太太的？` | ch39:90 `Matt wondered if the hand could be hers.` | **所指正确**（Horatio 之妻＝Fenella 的曾曾祖母，见 ch39:87／69／99），只是「她」应作「他」 | 提示 |
| 17 | md:45 `她说到曾祖父阿洛伊修斯的名字时语气不确定` | ch39:99 `Horatio died while Aloysius, my great-grandfather, was in his last year at school, I think.` | `I think` 修饰的是学年份，不是名字 | 提示 |
| 18 | md:11 `在分部「FRIDAY」里` | epub `OPS/toc.ncx` 第八分部 `FRIDAY`（`s050-Part-008.xhtml`），ch39 在其中 | 用的正是书里真实分部标题（未误用 `A FRIDAY IN MAY`） | 成立 |
| 19 | md:110 `迪吉死后的第一个星期五` | epub spine：Part-001 `A FRIDAY IN MAY` → Chapter-001（Digby 死）→ … → Part-008 `FRIDAY`（+7 天） | 成立 | 成立 |
| 20 | md:11 `信里那笔被嫌压价的收购报价` | 全章无金额（grep 取证见 3-diff.md：命中仅 line 20／129，退出码 0） | md 未虚构任何金额 | 成立 |
| 21 | md:11 `迪吉死前寄出的最后一封信` | ch39:123 `He sent it while I was away.`／`It was the last thing he wrote to me, you see.` | 成立 | 成立 |
| 22 | md:14 `她强作镇定是因为孩子已经死了` | ch39:111 `Her only child was already dead.` | 成立 | 成立 |
| 23 | md:13 `Horatio 遗嘱明写房屋「不得以任何方式改动」、信托从无外人介入、地下室自他那一代起就被封上` | ch39:69 `the conditions of my great-great-grandfather’s will clearly state that the house is not to be altered in any way`；ch39:72 `‘Right, Horatio’s will.’`；ch39:81 `We’ve never had any outsiders involved with the trust`；ch39:78–81（Fenella 答 `‘Yes.’` 地下室是 Horatio 封的） | 成立 | 成立 |
| 24 | md:28 `正是霍雷肖遗嘱的条款一直拖住迪吉…看能不能把这些东西送回新西兰` | ch39:75（逐项对上）／ch39:69–72 | 成立 | 成立 |
| 25 | md:42 `父亲说两人关系并不亲近；霍雷肖去世时，她的曾祖父阿洛伊修斯正读最后一年学` | ch39:99 `My father said they didn’t have much of a relationship.`／`Horatio died while Aloysius, my great-grandfather, was in his last year at school, I think.` | 成立（唯亲属称谓那句见 #10） | 成立 |
| 26 | md:56 `信里还提到要把那些缩头归还到新西兰` | ch39:129 `returning the shrunken heads here too`（here＝新西兰，与 ch39:75 `send them back to New Zealand` 一致） | 成立 | 成立 |
| 27 | md:21–24 块 1 全项 | ch39:26（candlesticks／markings／creepy time capsule／Fascinating stuff／communing with the dead／Being Chinese／ancestor worship／Grave robbing／Highgate Cemetery） | 逐项对应，说话人 Matt ✓ | 成立 |

## 3. 形态组（逐项）

| 形态项 | 本章实测 | 本书众数／profile | 偏离 |
|---|---|---|---|
| H1 | `39. The Police Station` | 原文小标题 `The Police Station`（ch39:17）；本书 54/54 章一律 `NN. <场景小标题>` | 无 |
| 导航项名与项数 | 5 项：一句话概括／视角／线索结构／人物弧线／叙事手法 | 全书 **54/54** 章均为这 5 项、顺序相同（脚本遍历 `ch*.md` 得 Counter 唯一元组） | 无 |
| 子项集 | 中文理解／关键词／为什么这样写／读者视角提示 | profile（mystery-thriller）`profile_subitems` 同 4 项；子项众数同 4 项 | 无 |
| 块数 | 6 | 全书中位数 7，区间 5–10 → 6 落在区间内 | 无（无需理由） |
| 机器形态探针 | `h1_shape_ok true`、`nav_count 5 / nav_count_ok true`、`nav_missing []`、`struct_bad 0` | — | 无 |

**形态组结论：偏离 0。**

## 4. 已核实为正确（防误修，勿以「读着不对」为由改动）

1. **md:11 `在分部「FRIDAY」里`** —— epub `OPS/toc.ncx` 第八分部标题逐字为 `FRIDAY`（`s050-Part-008.xhtml`），ch39 确在该分部内。**不要**改成 `A FRIDAY IN MAY`（那是第一部，ch01–ch02）。
2. **md:110 `迪吉死后的第一个星期五`** —— Digby 死于第一部 `A FRIDAY IN MAY`（epub spine：Part-001 → Chapter-001），ch39 属再下一个 `FRIDAY`（中间 SATURDAY→SUNDAY→MONDAY→TUESDAY→WEDNESDAY→THURSDAY→FRIDAY，+7 天），正是死后的第一个星期五。
3. **md:11／md:110 没有写任何金额** —— 本章原文全章无金额（取证：`/usr/bin/grep -niE 'million|£|\$|offer|valuation|valu|price|money|lowball' text/ch39_39.txt` → 仅命中 line 20 与 line 129，退出码 0）。**不要**补任何估值数字。
4. **md:35 `那只断手会不会是…太太的？`** —— 原文 `the hand could be hers` 的所指 = Horatio 的亡妻 = Fenella 的曾曾祖母（谱系：ch39:87 `my father was his great-grandson`、ch39:69 `my great-great-grandfather’s will`＝Horatio 的遗嘱（ch39:72）、ch39:99 `Aloysius, my great-grandfather`）＝ 同一句里的 `his late, much-loved wife`。**内容正确**，只需把「她太太」改成「他太太」。
5. **md:28 `霍雷肖遗嘱的条款一直拖住迪吉`** —— ch39:69–75（`Right, Horatio’s will.` + `holding Digby back`）✓，方向未反。
6. **md:56 `缩头归还到新西兰`** —— ch39:129 `here` ＝ Fenella 的新西兰，与块 2 的 `send them back to New Zealand` 一致 ✓。
7. **md:14 `孩子已经死了`** —— ch39:111 `Her only child was already dead.` ✓。
8. **六段引语本身** —— 机器逐字 6/6；人工复看三处易混点：块 2 头 `‘That was what…New Zealand.’`、块 6 尾 `It was glorious. He was going to really live.`、块 5 中 `karmic` 均为原文形态。

## 5. 最要紧的一条

**#5＋#7（施事写反）：导航与一句话总结把「回研究所找失踪日记」和「查 Isolde」两件事都安到 Matt 身上；原文这两件都是 Amy 的活（ch39:41 `I’m going to go back to the Institute and see if I can find it first`、ch39:32 `look into real Isolde again`），Matt 只说「也去 Digby 家找」（ch39:44）。** 这类错误四道机器探针全绿（引语逐字、中文是中文、关键词成立、形态正常），只有 R4 的三问能看见；且它出现在导航与总结两处，是读者对本章行动力的第一手摘要，误导面最大。

**附：修复建议（按根因）**
- 根因 A（施事）：md:11、md:110 改为「**Amy** 回研究所找失踪日记并继续挖 Isolde，**Matt** 留局里通知芬内拉、并顺道去 Digby 家」。
- 根因 B（受事）：「假 Isolde」改「**真实 Isolde**（为了弄清『假 Isolde』怎么知道那么多）」。
- 根因 C（mokomokai）：md:28、md:67、md:15、md:11 统一改为「**风干的毛利人头骨（toi moko / mokomokai）**」，删掉「战鼓」「编年史木刻」，并把 md:11 的「缩头与 mokomokai」合并为一项。
- 根因 D（计数）：md:38「降神会数量」改「**群交（orgies）次数**」。
- 根因 E（坚持者）：md:42「尽管博物馆一直坚持那样塑造他」改「**尽管霍雷肖本人坚持让后裔那样描写他**」；md:44 的论证前提同步改。
- 根因 F（亲属层级）：md:42「她祖父小时候」改「**她曾祖父（Aloysius）小时候**」。
- 提示级：md:35「她太太」→「他太太」；md:49「她此前的许多封信」→「迪吉的许多封信」；md:51 去掉「顺手／销毁证据」，`karma`→`karmic`；md:56「约她吃午饭」→「约**对方**吃午饭」；md:45 的 `I think` 归属改到「学年份」；md:106 `instincts` 移出基础档（机器 WARN）。

**复跑要求**：修完重跑 `bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch39 the institute is to be sold" --json`（期望仍 0/0/0），并人工复查上述 6 个根因是否**每一处**都改到（只报「现在 0」不算交代）。
