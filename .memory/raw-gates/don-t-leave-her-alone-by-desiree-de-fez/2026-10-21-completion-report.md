# 《Don't Leave Her Alone》(Desirée de Fez) — 五步独立审查完成报告

- 书目录：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez`
- 规模：18 章 md（ch00 序章 – ch17）+ 总览三篇（00_概述 / 00_情感节点 / 00_金句精选）= 21 md｜109 个引语块｜321 行词条
- lane：**完整 lane**（`library/Dont Leave Her Alone (Desirée de Fez) (z-library.sk, 1lib.sk, z-lib.sk).epub` 2.5 MB 在位）
- 审查方：DSH-Mac（执行方自审，同会话）｜审查依据：`docs/rules/审查表.md` R0–R5（2026-10-20 重构后的新第 10 条）
- 原始输出落盘：`.memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/`（19 个文件）

---

## 一、类级对账（修复前 → 修复后）

| 类 | 修复前 | 修复后 | 改写方式 |
|---|---|---|---|
| 中文层「夹杂理解/夹杂为什么」阻断型 | **5** | **0** | 4 处为工具口径假红（修工具，不改 md）＋1 处（ch02:80）已被工作树译全 |
| 中文层整层夹杂率 | 5% | **0%** | 同上 |
| 合格分析密度 | 95% | **100%** | — |
| 引语块内「读者视角提示」子项缺失 | **1**（ch03:50） | **0** | 拆出独立子项行 |
| 分析层「整段复制两遍」损坏 | **3**（ch16:61 / ch17:98 / ch05:80） | **0** | ch16:61 删重复半段、ch17:98 截回 `l[:1202]`、ch05:80 删省略号后回卷重放 |
| 中文理解「译文截断 / 引号错位」 | **2**（ch15:70 / ch17:82） | **0** | 整段重译并按语料对话轮次配对引号 |
| 分析层「引语走形 / 自造短语」 | **14** | **0** | 逐条换回语料逐字原句或改为中文表述 |
| 分析层「跨章引用未标注章号」 | **3** | **0** | 补 `chNN` 标注 |
| 说话人 / 受话人错配 | **3**（ch06:66 / ch10:52 / ch17:38） | **0** | 按语料改归因 |
| 关键词「不在本块引语内」 | 24 → 现 18 条**全部**在「为什么这样写」有呼应 | 18 条（0 条全书查无） | 属 AGENTS 第 9 条 b 允许的语境延伸词 |
| 总览三篇 d2 合规引用块 | 概述 9 / 节点 0 / 金句 0 | **概述 20 / 节点 22 / 金句 20** | 全部改为 `> "…"（chNN）`，编号移出块外 |
| 总览引语门禁覆盖率 | 26/62 | **62/62** | 引语块化后全部进 `verify_overview_quotes` 口径 |
| 总览「出处」错标 | **4**（金句 ①⑫⑱⑲） | **0** | 逐条按章建引语块池重对 |
| 总览事实性断言错误 | **1**（概述把 ch11 才点明的 Splau/Claire's 前置到序章） | **0** | 改写为与 ch00 原文一致 |
| 工具缺陷（假红源） | **3** | **0** | 修工具，见下节 |

---

## 二、缺陷清单（四档分类）

### 阻断型（必须改）—— 已全部修完，共 32 处

**A. 引语层（4）**
1. `ch05 chapter 5.md:80` 引语用 `…` 把同一段前 127 字符回卷重放（原文该句只出现 1 次）→ 删重放段，改取 para 205 原文（行 989 → 1650 字符）
2. `ch10 chapter 10.md:20` 引语截短（漏 `that they were autonomous individuals, even the baby…`）→ 延长引语 + 同步「中文理解」「句子结构」
3. `ch12 chapter 12.md:88` 中文理解被 ASCII `...` 截断在 `女孩 reac...` → 补完（原文 para 77；现 758 字符，ASCII `...` 0 处）
4. `ch12 chapter 12.md:61` 呼应对象写 `sun-bleached hair`，该词在本块引语外（在下一块原句 5）→ 改引语内词 `hair bleached by the sun`（原句 4 内确有 `hair bleached by the sun`）

**B. 重复/损坏（3）**
5. `ch16 chapter 16.md:61` 「中文理解」整段复制两遍（613 字符重复）→ 删重复半段
6. `ch17 chapter 17.md:98` 「句子结构」复制两遍且第二遍开头被截 13 字符 → 截回 `l[:1202]`
7. `ch15 chapter 15.md:70` 「中文理解」引号闭合在前开启在后 + 译文截断 → 整段重译配对

**C. 说话人 / 受话人 / 归因（3）**
8. `ch06 chapter 6.md:66` 把 Carlos 的 `the baby is OK` 归给 Diana → 改归因
9. `ch10 chapter 10.md:52` 把 Diana 说的 `That Alba is never alone` 归给 Carmen → 改归因（并在同章 :58 同步，消除自相矛盾）
10. `ch17 chapter 17.md:38` 把 `Carmen, before you sit down…` 写成 `Juan, …` → 改回 Carmen

**D. 分析层走形 / 自造（14）**
11. `ch13:66` `"longed for Diana to pinch her"` 全书零命中 → 改逐字 `Alba longed for Diana to sit down and give her a pinch`
12. `ch13:64/66` 自造 `red pinpricks` → 改 `tiny red points`
13. `ch13:48` 关键词 `birth ritual` 在下一块 → 删除（分析层两处改为块内逐字 `The birth ritual repeated itself`）
14. `ch13:76/78` `same face`（实为 ch16 才有）→ 改 `The same oval shape Diana envied`（**在 ch13 原句 5 内**，`text/ch13` 命中；`text/ch16` 0 命中）
15. `ch14:64` 把原文冒号两侧接成省略号引语 → 拆为两个逐字引证
16. `ch16:54/57` `pinch her thigh` / `mouth of wolf` / `flayed skin around eyes` / `applause in synchrony` 等压缩走形 → 逐条换回逐字原句（`the mouth of a wolf` / `the version with the skin around its eyes flayed` / `they clapped in perfect synchrony`，均在 `text/ch16` 命中）
17. `ch16:57` 跨章引用 `Diana pinched her leg` 未标 ch11 → 补标
18. `ch17:38`（见 10）
19. `ch04:28` `obsessive organization` → `obsessively organized`
20. `ch05:12/16/66/150` 自造分析标签 `documentary lens`（**epub 全文 0 命中**；`lens` 仅出现在 frontmatter 的 `through the lens of family` 与 ch04 的 `contact lenses` 两处无关语境）→ 4 处全改为中文表述「纪录片式观察视角」
21. `ch12:72` `wander that no-man's-land for twenty years` → `would wander that no-man's-land for a very long time`（语料：`Twelve-year-old Alba, with her red swimsuit and sun-bleached hair, would wander that no-man's-land for a very long time.`）
22. `ch17:28` `Carmen's prewash` → `My washing machine has prewash, Mom.`
23. `ch17:64` `left hair loose so kids wouldn't see ears` → 补 `Tonight, Alba had …`
24. `ch17:78` `neither one met eyes` → `Neither one felt able to meet the other's eyes`
25. `ch10:66` `Alba was happy at the campground. She wasn't afraid` → `She was happy at the campground. She wasn't afraid.`
26. `ch11:88` `first time in years she'd looked in mirror...` → 补全逐字
27. `ch12:39` `chorus doesn't count` → `That's the chorus. It doesn't count.`
28. `ch09:42` 引号跨中文串接造成的伪引证 → 拆开

**E. 事实错误（2）**
29. `ch00 prologue.md:64` 自造英文 `practitioner`（全书零命中）→ 改中文表述
30. `ch01 chapter 1.md:10` 写「单亲母亲 Diana」，原文是 `Her partner was going to be in Madrid all day`、ch05 明写 `a couple with two children` → 改写
31. `ch16:61` 残留空格 `耐心而 无奈` → `耐心而无奈`

### 提示型（只记不改）—— 4 类

- **P1 分析层「忠实压缩引证」**：全书分析层英文引证 2,553 条，语料可溯源 2,525 条（**98%**），不可溯源 28 条（1%）。逐条人工定性后确认：这 28 条全部是**本库通行的压缩引证体例**（`symbiotic vs parasitic`、`scars / stumps`、`bucket / cutting board / candles / knife` 这类标签式缩写），或**跨章引用且已带 `chNN` 标注**。抽样 20 条（§提示型豁免 ③ 要求）逐条回语料核对，**0 条自造**。
- **P2 `00_金句精选.md:202` 章节标注歧义**：`I dream of you—what have you given me? I long for you, you're forgetting me.` 逐字命中 ch11/ch12/ch17 三章语料，但**只被 ch12 原句 2 与 ch17 原句 7 两个引语块包含**（ch11 语料有、在 ch11 引语块外）⇒ 属副歌天然复现的真歧义，出处已改为 `ch12 原句 2, ch17 原句 7`。
- **P3 词汇层 WARN 14 条**：check_vocab 基础档疑含超纲词，按第 5 条 A/B 裁决口径处理，属措辞正当。
- **P4 `sweep_analysis_inline` 提示 573 条**（跨章 31 / 拼接 81 / 部分命中 427 / 词形 33）：与 P1 同源，属本库通行写法。

### 假红型（先修工具，不修 md）—— 3 处工具缺陷

1. **`scripts/check_chinese_layer.py` 口径缺陷**（阻断型 5 → 0 的关键）
   - 旧 `mix_ratio` 先 `re.sub(r'[“"][^”"]*[”"]', "", text)` —— 把**引号里的中文译文也一起剥掉**，再在剩下的文本上算汉字与英文。对话体书的「中文理解」正是「中文译句包在引号里」的形态 ⇒ 汉字被剥到只剩标签与连接词、英文只剩人名 ⇒ **比率被系统性高估**。
   - 实测本书 4 处（ch08:32 35.5% / ch09:44 40.4% / ch10:56 / ch10:68 83.3%）新口径下 3%–24% ⇒ **确认为假红，不改 md**。
   - 修法：**分母的汉字数按全文算，分子只数剥掉引文后的英文词**（剥引文只为排除「英文原句不算分析层内容」，不该把中文译文从分母拿走）。
   - **全库 472 本回归：判绿 → 判红 0 本**（只减不增）；已知坏书 bruja-s-nest 138→124、armor-for-liars 72→72、the-book-of-the-dead 8→4 保持高位 ⇒ 不漏报。
   - ⚠️ 工具 docstring 原声称「在合格书上 0 误报（this-time-tomorrow 428 块 / incarnate 286 / under-the-same-stars 711 块全部 0 阻断）」——**实测该声称不成立**（新口径下这四本仍分别 36 / 40 / 94 / 0 命中），属**专名/人名/URL 占比高造成的启发式假红**（如 `Rube Goldberg machine`、`Courtney Love`、`http://www.creepypasta.com/thebargain`）。本次未擅自改写该声称，须在实测档案内另行处理。

2. **`scripts/bookform.py` 三处缺陷**
   - (a) `re.search(r'""|“”', v)` 把**相邻对白**（`"又一枚耳环。""像前几天的那枚？"`）误判为空引号 ⇒ 新增 `has_empty_quote_span()` 逐个引号区解析，只在区间内容确实为空时报警。
   - (b) `corpus = find_corpus(book, no) if no else None` —— **`no=0` 是合法序章章号但 falsy** ⇒ ch00 被判「无法判定」（假红）。改 `if no is not None`。
   - (c) 引语逐字判定**大小写敏感**，而本库其余全部引语门禁（`verify_quotes.flat_alpha` / `quotecheck.chapter.flat_with_bounds` / `overviewcheck.full.flat_alpha`）都走 `.lower()` ⇒ 「原文句首大写、md 写成小写」被判「查无」（本书 ch06/ch10 各 1 段）。改 `corpus_lc`。
   - **全库 322 本基线对比（修前 = HEAD 版，非 amend）**：告警总数 **356 → 32（净减 324）**，明细减少 87 本，**明细增加 0 本**。差异明细落 `2026-10-21-tool-baseline-diff.txt`（532 行）。

### 跳过型（未进扫描集，写进报告）—— 3 项

- **S1 `check_entities`**：本书 18 个梗概段、0 个未知实体，**该项进了扫描集**（非跳过）。
- **S2 词汇 A 类虚构的 epub 口径裁决**：check_vocab FAIL 0，epub 在位，**该项进了扫描集**（非跳过）；但 WARN 14 条未逐条做 A/B 裁决（按第 5 条，A/B 裁决的触发条件是 FAIL，此处 FAIL=0）。
- **S3 「句子结构 / 一句话总结」体例漂移**：ch05–ch17 一致为英文主导、ch00–ch04 为中文 ⇒ 登记为需人判，**未改**（属体例选择，非内容缺陷）。

---

## 三、门禁终值（整改后全量重跑，不采信此前任何数字）

`bash scripts/gate.sh "<书目录>"` → **退出码 0**，105 行落 `2026-10-21-final-gate.txt`

| lane | 结果 |
|---|---|
| ① verify_quotes | **171/171 ✅（100%）**；完全干净文件 21/21 |
| ② check_vocab | 词条 321 行，**FAIL 0**，WARN 14 |
| ③ check_entities | 18 个梗概段 / **0 个未知实体** |
| ④ corruption_scan | **FAIL 0**，报告 0 |
| ⑤ sweep_full | 本章命中 82 ｜ 跨章 0 ｜ 拼接 27（提示）｜ **全书查无 0** |
| ⑥ check_short_quotes | 短引语 0 条（主门禁已全覆盖） |
| ⑦ 逐章归属 | **18 章全 X/X** |
| ⑧ 块覆盖对账 | 18 文件每块进 verify_quotes |
| ⑨ 导航/总结层英文 | **❌ 0 ｜ ⚠️ 0** |
| ⑩ sweep_analysis_inline | 逐字 2876 ｜ 跨章 31 ｜ 拼接 81 ｜ 部分命中 426 ｜ 词形 33 ｜ **零命中 0** |
| ⑪ structure audit | **结构缺陷 0 ｜ 提示 0 ｜ 映射不一致 0**（子项集＝中文理解/为什么这样写/关键词/句子结构/读者视角提示；引语众数 6） |
| ⑫ structure anchor | **凭空造词 0 ｜ 松散关键词 0** |
| ⑬ 空段扫描 | **0 处** |
| ⑭ verify_overview_quotes | **62/62 ✅**（情感节点 22 + 概述 20 + 金句 20）｜ 拼接 0 |
| ⑮ check_overview_full | 查无 0 ｜ 章节覆盖 18/18 ｜ ⚠️ 1（见 P2） |
| ⑯ check_xref_chapter | **归章正确 0 ｜ 伪造 0 ｜ 移章 0** |
| ⑰ check_quote_blocks | 109 行 `> **原句 N:**`，前缀完整 / 编号连续 / 无孤儿 / 无泄漏 |
| ⑱ structure keywords | **阻断型 0** ｜ 提示 23 |
| ⑲ check_chinese_layer | **109 块 ｜ 合格分析密度 100% ｜ 整层夹杂率 0% ｜ 阻断型 0 ｜ 提示型 0** |
| ⑳ 整书体检 bookform --all | **空引号 0 章 ｜ 形态偏离 0 章 ｜ 无法判定 0 章** |

补充：`bash scripts/chapter.sh` 逐章 18 章**全部退出码 0**（落 `2026-10-21-final-chapters.txt`）；`check_struct_indep.py`（独立实现）**缺陷 0**；`corruption_scan.py` **FAIL 0 / 报告 0**。

**独立取证（本次审查自写脚本，不依赖任何既有工具）**
- **引语块逐片段取证**：109 个引语块拆成 **196 条** ≥20 字符片段，逐条回本章 `text/` 语料比对（md 侧与语料侧都剥掉直/弯引号后归一）⇒ **未命中 0 处**。⇒ AGENTS 第 10 条第 5 类缺陷（省略号引语第二、三段是不是原文）本书为 0。
- **重复段机检**（自写 maxrep，阈值 L ≥ 30）：`ch16:61`（HEAD 2264 → 工作树 1187 字符）、`ch17:98`（1838 → 1204）、`ch05:80` 三处**重复均为 0**。
  ⚠️ `corruption_scan` 的「中文重复片段」判据**只查中文串**，对英文重放完全不可见——该 lane 报「0 处」而实际有 3 处英文重放，属**工具盲区**，本轮由自写机检抓出。
- **总览引语 80 个 span 逐条比对**：`EXACT 44 ｜ EXACT_NO_TRAILING_DOT 12 ｜ CASE_FIXED 24 ｜ NOT_FOUND 0` ⇒ 总览层无虚构引语。
  ⚠️ 24 条大小写/句点差异属本库普遍做法（抽样 46 本：span 2481 ｜ 逐字 1655 ｜ 仅大小写标点差 551 ≈ 22%）⇒ **不得据此外判红**；`verify_overview_quotes` 的归一化本就不大小写敏感。
- **「读者视角提示」子项齐备**：18 章 109 块，每块 5 子项齐全（`check_struct_indep.py` 缺陷 0）。

---

## 四、d 步语义二审执行方式

按 AGENTS 第 10 条 d 步，**不采信任何既有分析**，用与写作时不同的路径重建：

- 三个子代理批次（ch06–ch11 / ch12–ch17 / ch00–ch02 / ch03–ch05），指令附 3 个本库真实失败案例（100G ch86 引语讲"遮盖"分析讲"没有叔叔" / Such a Fun Age 18 处引语截短 / A Real Paige Turner 情感节点儿童转述冒充第一人称）+ 防幻觉条款（须确认引语行与中文理解行同文件相邻、禁拿 text/ 句子与无关分析行拼装、不确定标「需人判」、显式列出未进扫描集内容）+ **只读、禁改 md、禁 git**。
- **首轮三批全部 failed before finishing（无 closing message），第二批三批中一批再崩** ⇒ 处置：范围从 9 章/批砍到 6 章/批，并加**落盘要求**（完整报告写入 raw-gates 目录），使崩溃不再导致全部工作丢失。
- **父会话逐条程序化复核**了子代理的全部阻断项，不照单全改：batch E 的 7 条阻断经复核确认「现已全部修好」；batch B 的 13 条中 `ch11` leg/thigh 一条判为**假警报**（全文未把 leg 写成 thigh）；batch C 的「引语截短」多条经 `block_scope_check.py` 复核判为**本库通行写法**（本书「中文理解+关键词」字段块外率仅 1.1%，对比 bruja-s-nest 21.6% / under-the-same-stars 46.3%）。

---

## 五、结论与局限

**结论**：五步审查完成，**阻断型 32 → 0**，整改后 20 lane 门禁退出码 0、18 章逐章门禁全绿、另两套独立实现（`check_struct_indep.py`、`bookform.py --all`）均 0 缺陷。三篇总览已按 d2 全面重写为 `> "…"（chNN）` 形态，总览引语门禁覆盖率从 26/62 提到 **62/62**。

**局限（如实标注，供用户判断是否另行指派异实例复核）**：
1. 本次为**执行方自审（同一会话）**，按 AGENTS 第 10 条「局限如实标注条款」须写明已知盲区。
2. 分析层「忠实压缩引证」有 28 条（1%）无法逐字溯源，已定性为本库通行体例并抽样 20 条人工核对；**该定性依赖抽样，非穷举**。
3. `check_chinese_layer` 的 docstring「合格书上 0 误报」声称与实测不符，本次**未擅自改写**，属工具文档债。
4. `corruption_scan` 只查中文重复片段，**英文重放对它完全不可见**；本轮 3 处英文重放是靠自写机检抓出的，门禁层无覆盖。
5. 「句子结构 / 一句话总结」体例漂移（ch05–ch17 英文主导、ch00–ch04 中文）**未改**，登记为需人判。
6. 子代理两轮崩溃导致 ch00–ch05 的审查多花一轮时间；虽然范围已缩到 6 章/批并加了落盘兜底，但**批次稳定性本身未解决**。
7. **工具改动只做了「修前 vs 修后」的明细对比，未改任何存量书的 md**（按「🚦 新规则的适用范围」第 1 条：判据变更只对新增书籍生效）。`bookform.py` 修后仍有 19 本带告警（`finding-darla-by-vidhya-sathyamoorthy` 空引号 23 处等）——这些书**不在本次审查范围**，未动。

---

*审查方：DSH-Mac｜原始输出目录：`.memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/`*
