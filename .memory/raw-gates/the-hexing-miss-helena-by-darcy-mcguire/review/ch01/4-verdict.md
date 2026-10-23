# 4-verdict.md · 《The Hexing Miss Helena》第 1 章 审查判定

审查员：主会话自审（**同会话盲区见文末**）｜章型：**首章**｜抽样理由：快审 `ceil(N/8)` = 4 章，首末必含，等距 1·10·18·27
底稿：`1-suread.json`（R1 先素读，16 条事实／7 组关系／5 处数字）→ `2-machine.json`（R2）→ `3-diff.md`（R3）
源：`text/ch01_chapter_1.txt`（273 行）｜受审：`ch01 a dead husband.md`（6 块 / 21 条词表）
**R2 退出码 0，verdict `ok`；R2 之外本轮另跑全书级机器层（gate.sh / overview.py / verify_fragments_indep.py），见 `review/00_概述/4-verdict.md`。**

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 6 / 6 相符，0 错** | `2-machine.json`：6 段全部 `ok:true`，字符位 344 / 2909 / 5516 / 6796 / 10154 / 11572（递增），**无 `…`、无跨段拼接、无省略号缝**；另 `verify_fragments_indep.py` 全书 312 片段 0 MISS；词表 **21 / 21** 例句逐字回源命中（行号见 `3-diff.md` C9） |
| **对应** | **6 块：6 对应，0 不对应，0 密度不足** | 逐块 R4 三问（动词主语／受事／归属方向）全部与原文一致；引语未截短：块 1 覆盖 `:38` 全句、块 5 覆盖 `:236` 全句、块 6 覆盖 `:266` 全句 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 01. Chapter One` ✓｜导航 **5 项** = profile ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 6 块一致 ✓｜块数 **6** ∈ profile 4–6 ✓（`2-machine.json` `block_target:[4,6]`）；**但与本书众数 13 有差**（`structure.py audit` 报提示）。**偏离理由**：ch01 全章 2,061 词，为全书最短章之一，块数按「一段一个可分析场景」切得 6 块；本书众数 13 来自 2,700–4,000 词的长章。形态不算错，按规则在此写明理由 |
| **断言** | **共核 21 条：相符 17 ／ 提示 4 ／ 阻断 0 ／ 跳过 0** | 阻断 0；提示 4 条见下表 V1–V4 |

**阻断型条数 = 0。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch01_chapter_1.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| V1 | 导航「一句话概括」：`她刚承认自己感到的是解脱` | `:224` `Relief? Well. That’s hardly something one would admit.`；`:230` `She was free.`；`:236` `If she did feel a breath of liberation at his demise, it was only because she no longer had to pretend her society marriage was whole and happy.` | 源文三层并存：对外「不是会承认的东西」／内心已认「She was free」／随即用 `If she did feel` 对冲。md 写「承认」在「内心承认」层成立，但与 `:224` 相冲，且与本章正文（`:58-66` 原句 5 中文理解写「**如果**她真的感到一丝自由」）口径不一致 | **提示**（措辞；建议「她心里那点解脱刚冒头」） |
| V2 | 导航「叙事手法」：`结尾用问句收束，把悬念交给下一章` | `:266` `‘Lady Burrows, it gives me no pleasure to ask, but I must. Is there any reason you might want your husband dead?’`；其后仍有 `:269` `Oh dear.`、`:272` `Because she could think of hundreds of reasons.` | 问句在倒数第 3 段，章末落点是内心独白，不是问句 | **提示**（措辞） |
| V3 | 原句 6「读者视角提示」：`问题落下，章节就断了，她连否认的时间都没有` | 同 V2（章节未在问句处断） | 与 V2 同源，同一处改即可 | **提示**（措辞） |
| V4 | 原句 1「中文理解」：`十年的忍耐被压成三个连续的"十年"：闭嘴、做丈夫要求的尽职妻子` | `:38` `building up steam for the tirade that had been brewing for ten years. Ten years of keeping her mouth shut. Ten years of being the dutiful wife her husband required.` | 三个「十年」中只列了后两项（第三项由「为什么这样写」的「一次具体的冒犯」承担）；枚举不全，不算错 | **提示**（措辞） |

### 与原文相符的 17 条断言（避免「只报问题」的不完整交代）

- 十年：`text/ch01_chapter_1.txt:38` `building up steam for the tirade that had been brewing for ten years` ✓
- 丈夫姓 Burrows／名 Hubert：`:77` `He was sprawled face down…`、`:92` `took one look at Lord Hubert Burrows` ✓
- Thomas 是哥哥：`:131` `Her brother stood in front of her, his black hair askew, his green eyes flashing…` ✓
- MacDougal 是苏格兰场警司：`:137` `Superintendent Lachlan MacDougal` ✓
- MacDougal 是哥哥的挚友：「十多年前」扛过他过战场：`:140` `the man who had carried poor Thomas across battlefields littered with dead men so that he could be patched up and sent home to her over a decade ago` ✓
- 辛西娅与丈夫彼此都不爱：`:233` `Cynthia didn’t love her husband. Nor did Hubert ever love Cynthia.` ✓
- 死因非自然死亡：`:260` `‘It’s clear he didn’t die from natural causes.’` ✓
- 五个月前结识 Clio / Thomas 是 Clio 的调查搭档：`:191` ✓（本章 md 未取用，见 `3-diff.md` L1）
- 住 Mayfair：`:50` `their Mayfair home` ✓
- 希金斯太太是 housekeeper、今晨由她告知 Lily 被辞退：`:56` ✓（md 仅在词表例句出现，见 `3-diff.md` L4）
- 辛西娅偏爱咖啡、觉得那是「有失体统的承认」：`:203` `She preferred coffee, a scandalous admission.` ✓
- 客厅七月中生炉火、她在发抖：`:263` ✓（md 仅在词表例句出现，见 `3-diff.md` L2）

### 机器层（本轮另跑，结论入 `review/00_概述/4-verdict.md`）

- `chapter.sh --json`：退出码 0，verdict `ok`，`segment_miss=0`、`cjk_low=0`、`keyword_bad=0`、`struct_bad=0`、`quote_long=0`、`template=0`、`hole=0`、`block_count=0`。
- 本章相关的全书级提示：`check_vocab` 报 `ch01 a dead husband.md [基础] 基础档疑含超纲词「constable」`（词长 9 触发 `check_vocab.py` 的 ≥9 字启发式；`constable` 是本章原词 `:104` `A constable whose moustache twitched…`，属**假红型**，不修）。

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「她骂的是丈夫，但句子里的"my maid"才是她真正能支配的一小块领地」**（原句 1 读者视角提示）——依据 `text/ch01_chapter_1.txt:44` `Hubert taking control of household decisions, the one domain where she held a smidge of autonomy, was beyond the pale.`：自主权域正是家务决定，女仆正属该域。**成立**。
2. **「一个横陈、一个汇聚」（原句 2 为什么这样写）**——依据 `:77` `He was sprawled face down on the thick Aubusson rug. Blood pooled around him like a large crimson lake.`：`sprawled`＝摊开横陈、`pooled`＝积聚。**成立**。
3. **「同一面墙先作为她的选择出现，再作为困住她的东西出现」（原句 4 为什么这样写）**——依据 `:161` `She remembered choosing the wallpaper because it felt wild and free. But now, the vines were wrapping around her chest, tightening…`。**成立**。
4. **「第二个男人进入她的视线」（原句 3 中文理解）**——依据 `:131` 哥哥 Thomas 先现身、`:137` `Another man stepped into her line of vision`；MacDougal 确为第二个出现的男性。**成立**。
5. **「他手里的茶…本身就说明她已经被人接管了」（原句 3 读者视角提示）**——依据 `:137` `He held a cup of tea in his hands. Which was very strange indeed. She had never seen the superintendent drink tea.` 与 `:140` `She hadn’t invited anyone over this afternoon.`。**成立**。
6. **「从"准备第一次当面反抗"走到"对手已经不再回答"」（导航 人物弧线）**——依据 `:38` `Ten years of keeping her mouth shut.` 与 `:44` `She was going to confront him this time.`；十年闭嘴＋「this time」支持「第一次」。**成立**。
7. **词表 21 条例句全部逐字取自本章**——依据 `3-diff.md` C9 列出的行号（`:62 :50 :86 :251 :263 :239 :74 :170 :35 :44 :59 :104 :155 :53 :203 :89 :38 :158 :104 :104 :86 :104`）。**成立，不得改成别的句子**。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读 → R2 机器层 → R3 三张单子 → R4 逐块 6/6 → R5 判定表，**全流程走完**。
- **全书覆盖**：机器层 27/27 章；人判 **ch01 / ch10 / ch18 / ch27 = 4 / 27 章**（快审 `ceil(27/8)`=4，首末必含，等距 1·10·18·27）；**其余 23 章「仅机器层」**，未做人判。**总览三篇全篇人判**（另见 `review/00_概述/`、`review/00_金句精选/`、`review/00_情感节点/`）。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章又是**写作期已读过**的章之一（写作期为核对总览事实读过 ch01/ch05/ch09/ch12/ch16/ch17/ch18/ch22/ch25/ch26/ch27 的 `text/`）。本次仍按「先素读、写完 `1-suread.json` 才开 md」执行，但**不能视为完全盲态**；ch10 是本轮唯一此前**未读**过 `text/` 的抽样章，其结论独立性最高。
- **未做**：五步审查（深审 R0–R5 全章）**未执行**；快审升级条件（§0 四条）**未命中**（阻断 0 条 / 书写期用了 `bookform.py --contract` 与 `suread.py` / 机器层无异常信号 / 用户未点名），**未提请升级**。
