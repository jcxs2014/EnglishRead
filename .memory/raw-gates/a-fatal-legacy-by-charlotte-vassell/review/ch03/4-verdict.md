# R5 判定表 · ch03《The Police Station》

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch03 willow bell is questioned.md`
- 原文（唯一权威源）：`text/ch03_3.txt`（8225 字符 / 173 行）
- 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch03/`
- 覆盖声明：**本次是 ch03 的定向审查（用户指定），不是抽样**；本文件内所有结论只覆盖 ch03。其余 53 章**只有机器层**（复核时以全书口径跑过 `verify_fragments_indep` / `check_chinese_layer` / `check_vocab` / `check_speaker_consistency`），**未做人判，不写成「通过」**。
- 铁律执行：R1 素读（`1-suread.json`）**先落盘**，之后才开 md。

---

## 一、四组数

| 组 | 数 | 依据 |
|---|---|---|
| **逐字** | **7/7 通过** | `2-machine.json`（`chapter.sh --json` → `scripts/bookform.py`，退出码 0，verdict ok，`segment_miss` 0）。机器判定用的是**整段**（`scripts/bookform.py:323-324`：`ok = ns.lower() in corpus_lc`；JSON 里 `segments[].text` 的 `seg[:120]` 只是**显示截断**，不是判定口径）。**两点补充复核**：① 机器判定**大小写不敏感**（`scripts/bookform.py:315` `corpus_lc = corpus_n.lower()`）⇒ 另做一次**大小写敏感**的整串连续子串比对 → 7/7 仍通过（md 引语与原文大小写一致）；② `split_segments`（`scripts/lib/text.py:67`）只按省略号切段，ch03 七条引语**无省略号**，故每条即一段整查 → 7 条均为**单一连续子串**，无缝合、无虚构尾巴。**第三条独立路径**：`python3 scripts/verify_fragments_indep.py`（逐片段、按章参照）全书 776 条 / 844 片段 **MISS 0、拼接未标省略号 0**。 |
| **对应** | **7/7 块对应成立**（0 块"不对应"、0 块"密度不足"） | `4-correspondence.md` 逐块人判：每块的中文都在讲这句引语，且每块都有"为什么这样写"。**但对应层的缺陷全部落在跨层/跨块**：阻断 2 条（C1/A1）、提示 8 条（B1–B6、C2、C3 中的对应侧）。 |
| **形态** | **0 偏离** | H1 `3. The Police Station`＝本书众数 `# NN. 标题`（**54/54** 章一致），且与原文小标题 `text/ch03_3.txt:17`「The Police Station」一致；导航 **5 项**（一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法）＝本书众数项名与项数；子项集 **4 项**（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）＝本书众数＝profile `mystery-thriller`；块数 **7** ＝本书中位 **7.0**（范围 5–10），落在 profile 允许的 3–10 内。**无偏离 ⇒ 无需写理由行。**<br>副形态（非众数项，不判偏离）：ch03 的导航**未写分部名**，而全书 17/54 章在导航散文里写「分部「A X IN MAY」」（ch13/21/25/27/28/29/30/31/33/34/36/38/39/42/44/47/49/50/51）。理由：分部名是散文里的提法、不是 H1/导航项/子项集/块数四要素，且 37/54 章同样不写。 |
| **断言** | **15 条**（漏 5 + 编 6 + 错 4）＝ **阻断 2 / 提示 12 / 已核实为正确 1** | 逐条见下表。**假红 0**（机器层 exit 0、`2-machine.json` issues 全空；`check_vocab` 全书 26 条 WARN **无一条属于 ch03**）。**跳过 1**（词汇表"是否 A 类虚构/是否超纲"的 epub 权威判定——本书无 `library/*.epub`，`check_vocab.py` 明确降级不判红，故该项**未核**，不计入通过）。 |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md 导航「**到场时间**（手机基站打卡反推出 3.15 p.m.）」与一句话总结「复述**那个早晨**：…手机倒推出的三点一刻」把 3.15/3.24 p.m. 挂在**发现尸体的当天早上** | md `ch03 …md:13`、`:138`；原文 `text/ch03_3.txt:47`「‘When was the last time you saw Digby alive?’」、`:50`「‘**Yesterday, actually.** I popped in in the early afternoon.』、`:59`「‘**What time was this?**’」、`:62`「‘My phone says I tapped back into Chalk Farm at 3.24 p.m. It’s ten minutes’ walk so 3.15 p.m., I guess.’」、对照 `:26`「‘I turned up at the Institute at **8.45 a.m.**…’」 | 3.15/3.24 p.m. 属**前一天下午**那次探访（问答对象明确是 yesterday 那次），与发现当天上午无关。md 把前一天的时间说成发现当天的时间 ⇒ 时序错 | **阻断** |
| 2 | md 全篇**没有**「发现当天早上 8.45 a.m.」这一项（`8.45` 检索 0 命中），时间线上「发现现场」那一格空缺 | md 全文（`/usr/bin/grep -n "8.45…" → 无输出，退出码 1）；原文 `text/ch03_3.txt:26`「‘I turned up at the Institute at **8.45 a.m.** like I normally do. The door was left open, which was a bit odd, and I just walked in.’」 | 本章判据是「她能提供什么」；到场时刻是这份证词最基本的一项，且是读者复盘时间线的唯一依据。md 用 3.15 p.m. 顶替了它 | **阻断** |
| 3 | 「刷进了 Chalk Farm 的**基站范围**」／「**手机基站打卡**」 | md `ch03 …md:51`、`:13`；原文 `text/ch03_3.txt:62`「My phone says I **tapped back into Chalk Farm** at 3.24 p.m.」；他章口径 `ch15 …md:113`「tapping his card on the reader」（中文作「刷卡机」）、`ch12 …md:68`「Only my Oyster card」；`/usr/bin/grep -rn "基站" --include="*.md" .` → 仅 ch03 两处 | 原文是**车站闸机刷卡**，非蜂窝基站定位。**时间/地点/倒推方向三项事实全对**，错的只是记录机制名 ⇒ 按「措辞正当但不准」判提示（升格为阻断的判断权交回执行方，见 `3-diff.md` B1 的口径声明） | 提示 |
| 4 | 原句 2 为什么这样写：「目击者于是从一进门起就背着「我本不该进去」的**自责**」 | md `ch03 …md:35`；原文 `text/ch03_3.txt:26`「The door was left open, which was a bit odd, and I just walked in.」与 `:32`「Then I noticed it was slightly ajar anyway so I walked in.」 | 原文对走进去是中性的，无任何愧色；「自责」是 md 补出的心理断言 | 提示 |
| 5 | 原句 6 为什么这样写：「连细节都**不自觉地补齐**」 | md `ch03 …md:75`；原文 `text/ch03_3.txt:125`「**I transcribed a diary entry last month** where he blithely described chiselling a bit of a Roman villa off in Pompei…」 | 那些细节出自**她誊抄的日记**，不是她替空白补上的证词细节；在「事后补写的记忆」这一母题下易被误读 | 提示 |
| 6 | 原句 7 为什么这样写：「这是**全章第一次**出现关于这批藏品的分歧」 | md `ch03 …md:85`；同文件导航 `ch03 …md:13`「她**两次**提起馆藏时的语气」；第 6 块自己的引语 `text/ch03_3.txt:125`「Horatio Combe would be in prison for vandalism…He wasn’t a good person by any stretch」 | 与本章导航自相矛盾（第 6 块已是第一次对藏品的批判性表述）；若「分歧」专指两人对立则成立，措辞须收紧 | 提示 |
| 7 | 原句 7 为什么这样写：「与**死者把藏品当作全部生命的立场**正面冲突」 | md `ch03 …md:85`；原文本章仅 `text/ch03_3.txt:173`「I don’t get why Digby, Mr Combe-Watson, still kept them」与 `:137`「Being surrounded by all that stuff all the time had seeped into him and made him part of the past」 | 本章无「全部生命」这一强度的依据，属跨章解读被写成既成事实 | 提示 |
| 8 | 原句 5 为什么这样写引「Caius 紧接着的观察（现在没人能核实她那份 LinkedIn 档案了）」 | md `ch03 …md:65`；原文 `text/ch03_3.txt:107`「Caius could see her changing her LinkedIn profile in her head now there was no one to verify that with.」（在引语**之外**） | 创建卡 §0.2：分析里的人名/动作须在该段引语内，否则引语选短。主旨仍在引语内，判引语选短（提示） | 提示 |
| 9 | 原句 6 为什么这样写引「the damn things」「讲得又快」 | md `ch03 …md:75`；原文 `text/ch03_3.txt:125`「She started talking quickly. ‘There are all these volumes of **the damn things**.」（在引语**起点之前**） | 同上，引语选短（提示）；建议扩引语至含 "There are all these volumes of the damn things…"，**保持连续、勿用 `…` 缝合叙述** | 提示 |
| 10 | 原句 2 中文理解：「等**主人**来开门」 | md `ch03 …md:31`；原文 `text/ch03_3.txt:32`「I usually had to ring the bell and **wait to be let in**」（被动，施事未明说），本章未称其为「主人」 | 施事归属：md 补出了原文没有的执行者（R4 固定追问 ①） | 提示 |
| 11 | 原句 7 中文理解：「**归还本来能换来好名声**」 | md `ch03 …md:81`；原文 `text/ch03_3.txt:173`「**He could’ve got some good PR by returning them**」 | 主语由「他（Digby）」滑成「归还这件事」，且同句后半又写回「他还能卖上几张明信片」，前后不一 | 提示 |
| 12 | 导航承诺「再把**死者的性格、孤独**与藏品一件件评过来」／「看得出她既喜欢又烦躁迪吉」 | md `ch03 …md:14`、`:12`；原文 `text/ch03_3.txt:137`（tight / fussy / pernickety / antiquated / 1980s / 妈妈让她投简历 / 全靠通信）、`:143`（从没见他有手机 / Private Eye, The Cutter, London Review of Books）、`:155`（「I guess he was lonely. Lonely and trapped.」） | 7 个块里**性格 0 处、孤独 0 处**（藏品 2 处）。导航承诺与精读实有不对齐；非关键转折，判提示 | 提示 |
| 13 | 「He was a historian」未进 md | 原文 `text/ch03_3.txt:80`「Mr Combe-Watson was a very studious man. **He was a historian.** Quite a serious “chap”.」 | 可选补充：她知道死者是历史学家，却拒绝说研究所研究什么（`text/ch03_3.txt:98`「I’m not supposed to call it a museum…」），本可构成一组反讽 | 提示 |
| 14 | 「Because I was asked to.」未进 md | 原文 `text/ch03_3.txt:128`–`131`「‘Why were you typing it up?’ … ‘**Because I was asked to.**’ She shrugged.」 | 她与藏品的距离是**被派活**而非好奇；第 6 块读者视角提示说「她是真的逐字读过那些手稿的」，缺这条读者会问"她为什么要读" | 提示 |
| 15 | 研究所自我描述与日常工作未进 md | 原文 `text/ch03_3.txt:98`「an institute for the further study of something or another」、`:119`「The filing. He did everything on paper…」 | 非关键事件，可选覆盖 | 提示 |
| 16 | 「**侦探** Caius」（导航、总结各一处） | 本章原文只写 `text/ch03_3.txt:20`「Caius stated their names for the recording.」；全书口径 `text/xx_characters.txt:20`「An Irish-Jamaican **detective** in the Met, CAIUS…」、`text/ch06_6.txt:152`「You should be a detective.」、`text/ch24_24.txt:41`「‘Oh, a DI.’」 | **成立，不判缺陷**（见「已核实为正确」） | 提示（=已核实为正确） |
| 17 | 词汇表 30 条例句是否本章原句 | md `ch03 …md:93`–`134`；`text/ch03_3.txt` 全文 | 逐条 `grep -F` 式判定：**30/30 例句在 `text/ch03_3.txt` 中各命中 1 次**（机器层 `check_vocab.py` 本书 FAIL 0，26 条 WARN 无一条属 ch03） | 提示（=已核实为正确） |
| 18 | 词汇表"词是否 A 类虚构 / 是否超纲"的 epub 权威判定 | `check_vocab.py` 自述：「本书无 epub → 该判定**不出结论**（列入「无法判定」，不判红）」 | **未核**，不计入通过 | 跳过 |

---

## 三、假红（机器报了、判为工具口径错的）

- 本章**无假红**：`chapter.sh` 退出码 0、`2-machine.json` 的 `issues` 四段全空、`counts` 全 0。
- 全书层面 `check_vocab.py` 的 26 条「基础档疑含超纲词」WARN **无一条属 ch03**（清单见 3-diff 取证节的同源命令）。
- `check_speaker_consistency.py`（抽查级）报「归因与原文不一致 **0**」——按其自述「**报 0 不等于「说话人都对」**」，故说话人一项在报告里仍按**人判**结论记（对应层第 10、11 条即人判发现的施事偏移，机器层查不到）。

---

## 四、已核实为正确（防误修，固定一节）

> 以下条目**读着像错、回原文核对后成立**。后续任何人不得以「读着不对」为由改动，除非能给出反证。

1. **「侦探 Caius」**（`ch03 …md:12`、`:45`、`:138`）——本章只写他在录口供，但全书口径确为侦探：`text/xx_characters.txt:20`「An Irish-Jamaican detective in the Met, CAIUS is a foodie with a mortal fear of scurvy…」；`text/ch06_6.txt:152`「‘You should be a detective. I’m sure Caius could get you on a fast track scheme or something.’」；`text/ch24_24.txt:41`「‘Oh, a DI.’」。**不要因为"本章没说他是侦探"就改。**
2. **原句 6 的主语是 Horatio Combe、不是 Willow**（`ch03 …md:71`）——原文 `text/ch03_3.txt:125`「**Horatio Combe** would be in prison for vandalism if he was alive today. He was a womaniser too. I transcribed a diary entry last month where he blithely described chiselling a bit of a Roman villa off in Pompei…」主语确为 Horatio Combe，md 写对了（这是施事归属最容易写反的一处）。
3. **原句 4 的倒推方向**（`ch03 …md:51`、`:57`）——原文 `text/ch03_3.txt:62`「My phone says I tapped back into Chalk Farm at 3.24 p.m. It’s ten minutes’ walk so 3.15 p.m., I guess.」是从**回程进站时刻倒推**她在研究所的时刻；md 的「她到那栋房子时大约是 3.15 p.m.」「从回来的时间往前推」方向正确，**不要把方向改正过来**（错的只是把它挂到"那个早晨"，见阻断 #1）。
4. **原句 5 的因果方向**（`ch03 …md:61`）——原文 `text/ch03_3.txt:92`「because it’ll sound better on my CV when I graduate in July」是"为了简历好看 → 自称实习生"，md 未写反。
5. **7 条引语全部逐字**（`ch03 …md:19/29/39/49/59/69/79`）——全串连续子串命中 `text/ch03_3.txt`（第 1 条 552 字符、第 7 条 319 字符均整串命中），无省略号缝合、无拼接尾巴。
6. **章号重复不是语料错**——`text/ch03_3.txt:1` 与 `:12` 各有一个 "3"，`:17` 为小标题「The Police Station」；md 的 H1「3. The Police Station」与之相符。

---

## 五、给执行方的处置顺序（只列必须改的）

1. **先修时间线**（阻断 #1 + #2 一并修）：把 8.45 a.m.（`text/ch03_3.txt:26`）补进导航「线索结构」与「一句话总结」；把 3.15/3.24 p.m. 一律标为「**前一天下午**」。
2. **改「基站」**（提示 #3，建议一并改）：`ch03 …md:13`、`:51` → 「手机进站记录（闸机刷卡）」。
3. **一处自相矛盾**（提示 #6）：`ch03 …md:85`「全章第一次」→ 改「全章第一次出现**针对死者本人立场**的分歧」。
4. 其余提示项按 `3-diff.md` 的建议逐条处理（自责 / 补齐 / 主人 / 好名声主语 / 两处引语选短 / 导航承诺的「性格、孤独」）。
5. 改完重跑 `bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch03 willow bell is questioned" --json`（**「现在 0」不等于每处都改过**，请给修前→修后对照）。
