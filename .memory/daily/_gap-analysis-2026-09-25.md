# 2026-09-25 工作日志 → AGENTS.md 规则缺口审计

> 审计对象：`.memory/daily/2026-09-25.md`（1578 行，21 个实例 / 19 本书）
> 基准：`AGENTS.md`（691 行，全文通读）
> 方法：先 grep 标记词（建议/缺漏/盲区/根因/教训/复发/事故/假红/归档/清理）定位叙事区，再逐条回原文核；
> 每条 AGENTS 判定均以行号 + 原文短引为证。门禁原始逐行 dump 已跳过。

---

## 一、总表

| # | Gap（短） | Log 行 | 书 / 实例 | 复发 | AGENTS.md 状态 + 证据 |
|---|---|---|---|---|---|
| 1 | `check_vocab` 词头只做**全书级**匹配，词在别章出现即放过 → 跨章搬运词条可 FAIL=0 全绿 | 11（Lace）；966（AOY）；1145（What Grows）；1029（Why We Die）；1406（One Way Back）；638（Exhausted） | Lace / AOY / What Grows / Why We Die / One Way Back / Exhausted | **6 本 / ~29 处** | **PARTIAL**。AGENTS:612 只规定「**例句**是否命中本章」是逐章权威判定；「**词条头**是否在本章」**全文无一条**。Lace 自建 `check_vocab_head.py` 一行命令，AGENTS 无对应工具也无对应禁令 |
| 2 | 中文回指「**第 N 章**」用 md 文件号还是**书内章号**，无口径 → 大面积跨章引用错位 | 30（Lace，**明写「下一本书开工前应在 AGENTS.md 明确『中文回指一律用书内章号』」**）；896（Forgotten Sisters 42 处）；868/872（CWV）；1093（Floating Hotel）；1040（Why We Die） | Lace / Forgotten Sisters / China's World View / Floating Hotel / Why We Die | **5 本 / ~55 处** | **NOT-COVERED**。AGENTS:499 只把「`check_crossref` 只认英文模式、中文不在口径」列为**工具盲区**，没有正面规定回指该用哪套号；AGENTS:574 的三元比对只覆盖**文件名/H1/text 标题**偏移，不含正文里的中文回指 |
| 3 | 分析层 / 中文句中**未译英文碎片 + 繁体字 + 句体破损**（最大单一缺陷类） | 840（CWV 整改分类第 1 类 **57 条**）；868；855/859/860（各章明细） | China's World View | 1 本 / **57+ 条** | **NOT-COVERED**。禁令 1（AGENTS:318）管的是「分析层里**作证据的**英文」，管不到中文句子里混进来的无标记英文碎片与繁体残留 |
| 4 | `AGENTS.md` **自相矛盾**：命名约定「禁止 `_`」vs 工具链全篇用 `00_*.md` → 脚本硬编码下划线名，94 本单空格命名书**一律假红** | 1578（One Way Back 补录） | One Way Back | 1 实例 / **全库 94 本受影响** | **NOT-COVERED（实为规则内部矛盾）**。AGENTS:32「**唯一分隔符**：单空格（**禁止**使用 `_`）」，但 AGENTS:476/550/554/586/596/607/628 共 7 处引用 `00_*.md`；AGENTS:584 又写 `00 金句精选.md`。AGENTS:34 自身的例子 `ch<NN>_<keyplot>.md` 也与「禁 `_`」冲突 |
| 5 | 归档：slug 撞名**无消歧规则**（`title-by-author` kebab 不够用） | 603（Real Life 短篇集 2002 用 `-2002-anthology`）；620（Lost Village 建 `-zlibrary` 后删除） | 归档 Batch B / Batch D | 2 批 / 2 例 | **NOT-COVERED**。AGENTS:137 只写「slug = `title-by-author` kebab」，AGENTS:128 的处置表四条里没有「同名不同书如何加后缀」这一行 |
| 6 | 归档：`index.md` **批量插入的 sort 错位**（单点插入 vs 整节重排） | 592（Batch A「手工修正 4 处 sort」）；628（收官「批量节内 sort 须用全节重排而非单点插入」） | ZCode-Mac 归档批次 | 1 实例 / **4 处** | **PARTIAL**。AGENTS:138 只写「按字母位插入」+「顺手查历史**缺行**（并行 edit 覆盖丢行）」；**排序错位**（行插进来了但位置不对）不在其中，而对账口径只查「零缺零幽灵」也不查顺序 |
| 7 | 归档：NFD **分解字符**文件名（Téa / García）匹配不到，须 NFC 归一 | 628（归档收官坑位沉淀） | ZCode-Mac 归档 | 1 实例 | **PARTIAL**。AGENTS 归档流程 step 1/4（128/138）无 Unicode 归一要求。`docs/新书启动模板.md:593` 有**相邻但更窄**的一条（长音符 `Tōkyō` grep 假阴），只管 grep、不管归档对账 |
| 8 | 段落结构断言（「独立成段 / 三行 / 单独成句」）**必须解包 epub `<p>` 标签**才查得出，`text/` 提取件已把同段多句并成一行 | 987（AOY 审查 8 处断言**全部不成立**） | All Our Yesterdays | 1 本 / 8 处 | **NOT-COVERED**。`verify_corpus` ④ 查的是转义符/页码 bleed；`audit_numbers` 明写「`N 个字符/分句` 一律不判，只列未判」（AGENTS:585）；**没有任何一处说明 `text/` 不保段落边界、段落断言须回 epub** |
| 9 | 委派**子代理写作**章节（写作侧，非审查侧）的规则完全空白 | 816（China's World View 4 个子代理写 ch12–ch18，「一次通过 0 FAIL」，**明写「这条经验值得固化」**） | China's World View（Qoder-Mac） | 1 本 | **NOT-COVERED**。AGENTS 9f（474）与 10d（552）管的是**审查委派**（附反例 + 防幻觉条款 + 载荷上限）；写作委派的任务书要求、复核口径、机械可判定性**一条没有** |
| 10 | 短章 / 特殊章**合法规格下调**（Epilogue 仅一条词典释义、3 篇短章）无规则 | 8（Lace ch65「显式标注不适用 3–8 处常规配额」）；950（AOY ch01/ch14/ch21）；1083（Floating Hotel 4 个无标题节）；1408（One Way Back 小章只写 8 块） | Lace / AOY / Floating Hotel / One Way Back | **4 本** | **PARTIAL**。AGENTS:457 只规定「删块后低于 3–8 下限必须回填」——那是**缺陷处置**，没有「本章客观不足 3 处」时的合法下调路径。AGENTS:613 有同 spirit 的先例（「缺概览只是体裁差异」，按 CORE/OPTIONAL 拆分），可照抄 |
| 11 | 计数断言里的「**X 个字母 / X 个词**」是不可迁移修辞套语，批量造假 | 18（Lace 五步审查扫出 **67 处假计数**：`available` 9 个、四个 `And` 实为三个…） | Lace | 1 本 / **67 处** | **PARTIAL**。禁令 2（AGENTS:321）列的是「`N 个词`/`N 个分句`/`N 个字符` 一律不写」——**「N 个字母」「N 个词组/次」未列入**，而 67 处假计数里绝大多数是这类 |
| 12 | **否定 / 极性翻转**是独立缺陷类（否定读成肯定、方向标反） | 1092（Floating Hotel `hairless`→「毛茸茸」、`lunar eclipse`→「日全食」）；901（Forgotten Sisters「非法抛尸」读成合法）；840（CWV「The answer is no」→肯定）；29（Lace ch63「父母都死了」原文父母活着）；1040（Why We Die SIR2 突变方向反）；1433（One Way Back 方向/位置标反 4 处） | 6 本 | **6 本 / ~14 处** | **PARTIAL**。禁令 1 的「为什么」列了「多插否定词」（AGENTS:318）但只当**引语复制失真**讲；没有一条把「**中文理解/总结把原文的否定、方向、极性读反**」立为独立缺陷类与专项回查动作 |
| 13 | 引语**首尾吞词**：flat 子串判定天然失明；词边界须在**原文层**判定，且**破折号不可归入词字符集** | 930–934（Forgotten Sisters 新工具 `audit_bounds.py`，一启用再抓 2 处） | Forgotten Sisters | 1 本 / 3 处 | **PARTIAL**。AGENTS:615 有 `check_chapter_quotes` 的「首/尾词吞词**只报不判红**」+ 裁决①改 md ②走 verify_corpus；但**「判定必须在原文层做词边界、破折号不可算词字符」**这条实现判据只在 `sweep_full`（AGENTS:587）里以 `suffix_match` 出现过，未上升为通则 |
| 14 | `verify_quotes` 对 `, I thought.` 类**尾注行整行跳过**（m2 正则要求闭引号后接字母/行尾） | 1405 / 1419（One Way Back ch27 金句） | One Way Back | 1 本 | **NOT-COVERED**。AGENTS:607 的跳过清单是「<20 flat 字符短引语」与「P0-1 只认三种引语格式」；`check_short_quotes`（AGENTS:584）也只捡 `<20` 的。**尾注导致整行不提取**是第三条独立的提取盲区 |
| 15 | 金句精选**复用**精读块引语 → 章节↔总览**跨文件**重复块，现有门禁只查 within-file | 1404（One Way Back 8 处，**明写「工具不查重复——建议纳入常用流程」**） | One Way Back | 1 本 / 8 处 | **PARTIAL**。AGENTS:457 把「重复块（同引语出现两次）」定为缺陷，`audit_structure`（550/586）查的是**单文件内**重复；**跨文件（总览 vs 章节）去重**无任何门禁 |
| 16 | **同句共现**词条导致例句重复（11 组），只能完工前统一扫才看得全 | 828（China's World View 11 组）；971（AOY 重复词条行 2 处）；1025/1031（Why We Die 占位行 ~40 行） | CWV / AOY / Why We Die | **3 本** | **NOT-COVERED**。AGENTS 无「同一例句被两个词条共用」的任何检查或禁令 |
| 17 | 草稿标记（`X? no — Y`）与反引号残留的**提交前 grep 自查** | 640（Exhausted 5 处 `? no` + 4 处反引号残留，给出 grep 式）；1407（One Way Back 3 处占位行）；1155（What Grows `—— 本章无此搭配` 空壳行） | 3 本 | **NOT-COVERED**。AGENTS:586 有 `audit_structure` 的「占位行」、AGENTS:612 有「grep 行尾 `\| *$`」；但**草稿问答式标记 `? no` / 思考残留 / 反引号未闭合**这三类没有对应的 grep 或门禁项 |
| 18 | 完工前「**漏提交核对**」（tracked=N / 未提交=0）无强制规则 | 6（Lace 接手时前实例留下 ch17–ch25 **9 个 md 未提交**，明写「**漏提交盲区**」）；103/826/963 至少 5 本自行执行了这项 | Lace（+5 本自发执行） | **1 本报坑 / 6 本在用** | **NOT-COVERED**。AGENTS git 策略（623–630）覆盖 add 范围、index.lock、amend、GIT_INDEX_FILE，**没有「完工/接手先核对 tracked 与未提交」这一步** |
| 19 | 源文本**自身**的拼写错误不要沿用（`grapefuit` vs `grapefruit`） | 16（Lace ch53） | Lace | 1 本 | **NOT-COVERED**。第 5 条 A/B 裁决管的是「词在不在原文」，没有「原文自己错、词条取哪个」的裁决口径 |
| 20 | `check_entities` 把「**一句话总结**的标签」当未知实体 | 1060 / 1072（That First Flight ch49「Happy Beginning」） | That First Flight | 1 本 | **PARTIAL**。AGENTS:594 给了两类豁免路径（作者姓 → `whitelist.txt`；系列名不在书内），没有「总结/导航层的**体裁标签**」这一类 |
| 21 | 证据链**表格第一格**禁放专名 / 外语词（会被 `check_vocab` 当词条判 A 类虚构） | 13（Lace「三列表格第一格是中文即报 A 类虚构」，改 `·` 分列）；639（Exhausted ch04 德语词拼错 + 第一格被当词条）；1093（Floating Hotel 结构表改列表格式） | Lace / Exhausted / Floating Hotel | **3 本** | **PARTIAL**。AGENTS:612 有「**概述/导航层**用 `\|` 会误判为词汇表行 → 改用 `·`」，但**精读节内的 `## 论证结构` 证据链表格**（AGENTS:115 规定的 `\| 证据 \| 类型 \| 支撑什么 \|`）恰恰**就是**用 `\|` 的，规则没覆盖到它自己定义的表格 |
| 22 | 导航 / **格式说明**层出现英文专名（`Part III`、trope 名）→ `check_entities` 误报 + `> ` 前缀被 `check_chapter_quotes` 当引语去比对 | 972/974（AOY，「**值得写进盲区表**」）；1000（5 处导航层英文分部名） | All Our Yesterdays | 1 本 / 10 处 | **PARTIAL**。AGENTS:308–310 有相邻的一条（`>` 只有引语能用，汇总性说明改 `**粗体标签**：`），但框定在「母题计数/形式记录/章节统计」；**格式说明行里的英文专名**与 `check_entities` 的实体误报这一半，AGENTS 无 |
| 23 | `verify_quotes` **弯撇号截断** → Clear 全书 `0/467` 假阴性（全靠 `check_chapter_quotes` 兜住） | 350（Clear） | Clear | 1 本 | **PARTIAL**。AGENTS:615 只给了 `check_chapter_quotes` 的弯撇号假 MISS；AGENTS:458 说「弯/直引号差异视为正常」。**`verify_quotes` 因此整本 0 提取**这一失效模式没写进 AGENTS:607 的「0 提取」四类分派 |
| 24 | 批量重编号脚本 `replace` **丢 `### ` 前缀**致锚点失配 | 1409（One Way Back ch32） | One Way Back | 1 本 | **PARTIAL**。AGENTS:475（9g）禁 `re.S` 跨块、AGENTS:562 要 dry-run；「重编号类脚本必须保留 heading 前缀」是第三条，且它不同于内容批改（它动的是结构标记） |
| 25 | 「用户拍板保留 epub」清单（USER_KEEP）**无机制** | 582/586（清理已完工 epub，`exhausted` 在制 + `open-secrets` 6/8 在制 → 列入 USER_KEEP 免删） | ZCode-Mac 清理实例 | 1 实例 | **PARTIAL**。AGENTS:139 写「存量已精读书可按**用户指令**删除 epub」——当次指令是覆盖的；但**在制书**（章节未完工、epub 仍需回拷）没有「按在制状态自动豁免」的判定口径，USER_KEEP 是临时手搓的 |
| 26 | 清理 epub 本身（删 59 本、−160MB）**未暴露规则缺口** | 578–586 | ZCode-Mac | 1 实例 | **COVERED**。按 AGENTS:130「library 空 + 精读已完成 → 不留 epub」执行，判定口径（md 齐 + 总览三篇齐 + text 1:1）写在 AGENTS:130 括注里。后续「降级 lane」概念（AGENTS:179–194）是这次清理的**下游后果**，已被 09-26 单独固化 |
| 27 | 归档 Lost Village：同名不同版本 | 620（Batch D） | 归档 Batch D | 1 例 | **COVERED**。AGENTS:132「同名不同书/版本存疑：先 `grep -rl` 全库排除跨书同名，拿不准问用户」 |
| 28 | 归档 kebab 对账 / index 零缺零幽灵 | 234/593/602/611/619/626（6 批） | 归档 7 本 + Batch A–D | 6 批 | **COVERED**。AGENTS:138 |
| 29 | 总览引语**章节标签对账**是独立盲区 | 14/1094（**明写「建议进 AGENTS.md 盲区表」**）；716；824；956；962；1066/1070；1169；1262；1335；1379；1417；895 | 15 本 | **~15 本** | **COVERED**。AGENTS:554「总览引语的章节标注（chNN）是独立工具盲区」+ AGENTS:588 `check_overview_full` B 项章节标签对账 |
| 30 | 52 字符指纹盲区 | 15/718/644/985/1091/1192/1427 | 8 本 | **8 本** | **COVERED**。AGENTS:165（`--full`）、552（`sweep_full` 终验标准件）、587、607 |
| 31 | 导航 / 一句话总结 / 概览层是**全库最大共同盲区** | 805（11 处缺陷 9 处落导航层）；842（132 项零落引语层）；1044（62 处 61 处在门禁盲区）；6；986；1092；1198 | 8 本 | **8 本 / ~220 处** | **COVERED**。AGENTS:282–290（2026-09-27 从提示级上调为实质约束）+ AGENTS:608 三书互证条目 |
| 32 | 分析层伪造 / 改写引语**无低成本机检** | 986（2 处伪造 + 4 处改写）；987（段落断言 8 处） | AOY | 1 本 | **COVERED**。AGENTS:329–338（禁令 3 附注，「只能靠写作期粘贴」）+ `sweep_analysis_inline`（AGENTS:583） |
| 33 | heredoc `r'\*'` 假阴性；**报告为 0 时先怀疑脚本坏了**；批量脚本 dry-run | 26（Lace「差点照着『124 处』去改」） | Lace | 1 本 | **COVERED**。AGENTS:562 审查过程纪律 3 |
| 34 | 脚本化批量改写分析层产生**重复从句 / `。。`** | 28（Lace ch64 2 处自造损坏） | Lace | 1 本 | **COVERED**。AGENTS:171–177 + 235 + 581（`corruption_scan` 进第 3 条门禁，理由即此） |
| 35 | 假红型先修工具、不许改 md | 26/718/1005/1089/1547/1578 | 6 本 | **6 本** | **COVERED**。AGENTS:204（三档判据）+ 214–215 报告纪律 |
| 36 | 大面积同类报警先读行再改 | 718（Until August：先在已知良好的书上跑对照再判定） | Until August | 1 本 | **COVERED**。AGENTS:217–222 + 563 |
| 37 | 裁引语必须**同步裁分析**（「改引语留旧分析」的变体） | 21（Lace 锚定漂移 6 处） | Lace | 1 本 | **COVERED**。AGENTS:453（第 9 条 a 修复即同步） |
| 38 | 引语**合并**（相邻两独立行被并成一句） | 1065/1069（That First Flight ch30）；1302（Night Circus ch70/71/72）；1192（What Grows ch25 虚构桥接） | 3 本 | **3 本** | **COVERED**。禁令 5（AGENTS:324）「引语只取一个说话轮次」 |
| 39 | `check_vocab` 基础档 ≥9 字符启发式误杀常见词 | 12（Lace 10 词）；207（Living on Paper 7 词）；703（Until August 17 WARN）；1151（What Grows 18 处） | 4 本 | **4 本** | **COVERED**。AGENTS:203 三档表「提示型」明列该启发式 |
| 40 | `audit_book` C 节把总览按正文章节格式误报 | 115（Pax）；195（Red Memory）；207（Living on Paper）；567（Wolf at the Table） | 4 本 | **4 本** | **COVERED**。AGENTS:617 |
| 41 | `verify_overview_quotes` 对本库格式 **0/0 静默空转**（不是满分） | 207/641/707/956/1131/1295/1536 | 7 本 | **7 本** | **COVERED**。AGENTS:610 + 607「0 提取」四类分派 |
| 42 | 提取器 min-len 600 误滤短章（451 / 423 字符） | 1108（What Grows Interlude_2009）；1083（Floating Hotel Walking away） | 2 本 | **2 本** | **COVERED**。AGENTS:590「短章可能被 min-len 滤掉」+ 591 `verify_corpus` ① 件数对账 |
| 43 | TOC 一项 = 多个文件 / 同名文件内容不同 | 1109/1110（What Grows） | What Grows | 1 本 | **COVERED**。AGENTS:155「预期篇目数必须写来源（目录页/bullet 实测）」+ 591 ① |
| 44 | 页码 bleed 粘连（Profile Books epub） | 637（Exhausted 40+ 处）；645 | Exhausted | 1 本 | **COVERED**。AGENTS:156/611（`verify_corpus` ④ 页码 bleed → 选句避开粘连点） |
| 45 | 引语中段脚注号粘连致整句 flat 假阴 | 207（Living on Paper 9 例） | Living on Paper | 1 本 | **COVERED**。AGENTS:156 同上 |
| 46 | Read 工具输出损坏 / 记忆漂移，须以 shell grep 为准 | 1435（One Way Back ch30⑥「whah 少一个」实为 Read 输出损坏） | One Way Back | 1 本 | **COVERED**。AGENTS:377–381（「不信 Read 工具输出与上一次读取的记忆」） |
| 47 | 子代理额度耗尽 / provider 报错时**主会话自执行不可省** | 318（Dolphin 5 个子代理批次全未执行，主会话完成 120/120 + 51/51） | The Dolphin in the Mirror | 1 本 | **COVERED**。AGENTS:552「子代理额度耗尽时主会话自执行不可省」 |
| 48 | 审查任务书须附本库失败案例 + 防幻觉条款 | 111/212/573/747/837/888/981/1089/1177/1429 | **10 本** | **10 本** | **COVERED**。AGENTS:474（第 9 条 f） |
| 49 | 同会话审查「全书统一口径系统性误判」须如实标注 | 31/41/116/196/227/336/410/575/677/742/807/872/938/1009/1046/1074/1096/1226/1307/1344/1392/1442 | **21 本全部** | **21 本** | **COVERED**。AGENTS:491（「局限」指结论写作要求，不是减少步骤的依据） |
| 50 | 完工/修复报告数字不可信，须现场重跑 | 834/918/1036/1086/1270/1340/1383/1426/1444 | 9 本 | **9 本** | **COVERED**。AGENTS:546 |
| 51 | 第 10 条两处「三件套」名单漂移 | AGENTS:516–517 自述（NS/TN/Levels of Life） | — | — | **COVERED**。AGENTS:512–520 |
| 52 | 内联 Gate（写前 grep 预验）拦下凭印象词条 | 828（CWV **约 55 处**）；715（Until August ch06/ch07）；640（Exhausted）；716 | 4 本 | **4 本 / ~65 处** | **COVERED**。AGENTS:250 直接把 `.memory/daily/2026-09-25.md:828` 引为「提取·对照」证据行 |

---

## 二、优先处理清单（NOT-COVERED / PARTIAL）

### P0 — 复发面最大、规则真空

**1. `check_vocab` 缺「词条头逐章核对」（表 #1，6 本 / ~29 处）**
AGENTS:612 明确把判定权分成两半：例句**是否命中本章**是逐章权威判定，词条**是否 A 类虚构**是全书判定。但 6 本书独立报告的恰恰是判定权的**中间地带**——词头在别章出现 → 全书口径放行 → 本章其实没有这个词。Lace 记「795 行一次扫出 3 处」，What Grows 记 14 处。AGENTS 既无禁令（`词条头必须在本章 text/`）也无工具条目（`scripts/attic/check_vocab_head.py` 未入库），是最典型的「规则有洞、不是脚本不够用」。

**2. 中文回指章号口径（表 #2，5 本 / ~55 处，日志里唯一一条明写「应在 AGENTS.md 明确」的）**
Lace:30 是全日志唯一直接向 AGENTS 提要求的句子，而它至今没有被写进去。Forgotten Sisters 单项 42 处「书内章号与 md 文件号混用」。现在的 AGENTS 只有两处相关：AGENTS:499 把它记成 `check_crossref` 的工具盲区（被动）、AGENTS:574 的三元比对只查 filename/H1/text 标题（不含正文回指）。需要一条**正面口径**：中文「第 N 章」一律用书内章号，且偏移书在 frontmatter `source_text` 旁记 `book_chapter` 映射。

**3. AGENTS 自身矛盾：`_` 分隔符（表 #4，影响 94 本）**
AGENTS:32 禁 `_`，而 7 处工具链规则用 `00_*.md`、AGENTS:584 又用 `00 金句精选.md`、AGENTS:34 的例子本身就是 `ch<NN>_<keyplot>.md`。One Way Back 实例据此判「假红型、先修工具」并给了 322/94 的库内分布实测。这不是缺一条规则，而是**要消一处矛盾**——否则任何按 AGENTS 写的新脚本都会再犯。

**4. 未译英文碎片 / 繁体 / 句体破损（表 #3，1 本 57 条 = 单一最大缺陷类）**
China World View 的 132 项整改里「未翻译英文碎片」占 57 条，超过引语保真、语法误判的总和。禁令 1 管的是「分析层里作证据的英文」，而这 57 条是**中文句子里混进来的无标记碎片**（`清华 students`、`adopts / venture / formidable`、`動員→动员`）。四道门禁对这一类全部无感，需要一条独立禁令 + 一个 grep 自查。

### P1 — 单本但机制价值高

**5. 委派子代理**写作**的规则空白（表 #9）**
China's World View 用 4 个子代理写完 ch12–ch18，一次通过 0 FAIL，主会话机械复核 + 数字溯源后全绿，日志明写「这条经验值得固化」。AGENTS 关于子代理的规则（9f / 10d）**全部是审查侧**的。缺的是：写作委派的任务书必备条款（先 grep 再写词表、词头原词形、例句不重复、引语写前 flat 预验——这四条 instance 自己写在任务书里了）、以及主会话复核的机械可判定性要求。

**6. 段落结构断言必须回 epub 解包 `<p>`（表 #8）**
AOY 的 8 处「独立成段 / 三行 / 单独成句」断言**全部不成立**。`text/` 提取件把同段多句并成一行，所以 `audit_numbers` 的「字符数/分句」判据天然失效（AGENTS:585 已把它降为「只列未判」，但没说为什么、以及该回哪里核）。缺一句：`text/` 不保段落边界，凡段落级断言须解包 epub。

**7. 合法规格下调的路径（表 #10，4 本）**
四本书遇到 Epilogue / 短章客观不足 3–8 处的情况，处理方式各不相同（Lace 在格式说明里显式标注、AOY 三章标注下调、One Way Back 事后补回填）。AGENTS:457 的「低于下限必须回填」是缺陷处置，缺少合法下调的判据。AGENTS:613 的 CORE/OPTIONAL 拆分是现成的写法可抄。

**8. `check_vocab` 例句去重（表 #16，3 本）与跨文件重复块（表 #15，1 本 8 处）**
CWV 的 11 组「同句共现」例句重复、AOY 的 2 处重复词条行；One Way Back 8 处金句复用精读引语——`audit_structure` 只查单文件内重复。两条都便宜（`flat[:60]` Counter 即可），但 AGENTS 都没有。

### P2 — 单例、低成本

表 #5（slug 撞名消歧，2 例）、#6（index sort 错位，4 处）、#7（NFC 归一）、#14（`, I thought.` 尾注致整行跳过）、#17（草稿标记 grep）、#18（漏提交核对）、#19（源文本自身拼写错误）、#24（重编号丢 heading 前缀）、#25（USER_KEEP / 在制书豁免口径）——每条都是一次事故换一条规则，成本一行到一段文字。

**归档批次 A–D 的整体判断**：99 本 6 批归档，主体流程（体裁判定、kebab 对账、零缺零幽灵、Lost Village 处置表）**AGENTS 全部已覆盖**，未暴露流程性缺口；新坑集中在**机械细节**（Unicode 归一、sort 错位、slug 撞名）三条，全部属于「归档流程 step 1/3/4 各加半句」的量级。
**清理已完工 epub**：按 AGENTS:130 执行，未报缺口；它造成的下游状态（大量完工书无 epub → 降级 lane）已在 09-26 单独固化为 AGENTS:179–194，不重复记账。
