# Agent 协作消息板 · 历史归档（2026-10-25 ~ 2026-10-31）

> **本文件为 [COLLABORATION.md](../COLLABORATION.md) 的只读历史归档**（2026-11-03 拆分归档，共 21 条消息）。排序与主文件一致（newest first）。
> **📁 归档索引**：[ARCHIVE_260905.md](COLLABORATION_ARCHIVE_260905.md)（08-10~09-03）· [ARCHIVE_260909.md](COLLABORATION_ARCHIVE_260909.md)（09-04~09-09）· [ARCHIVE_260915.md](COLLABORATION_ARCHIVE_260915.md)（09-10~09-15）· [ARCHIVE_260921.md](COLLABORATION_ARCHIVE_260921.md)（09-16~09-21）· [ARCHIVE_260923.md](COLLABORATION_ARCHIVE_260923.md)（09-22~09-23）· [ARCHIVE_260926.md](COLLABORATION_ARCHIVE_260926.md)（09-24~09-26）· [ARCHIVE_260928.md](COLLABORATION_ARCHIVE_260928.md)（09-27~09-28）· [ARCHIVE_261003.md](COLLABORATION_ARCHIVE_261003.md)（09-29~10-03）· [ARCHIVE_261007.md](COLLABORATION_ARCHIVE_261007.md)（10-04~10-09）· [ARCHIVE_261016.md](COLLABORATION_ARCHIVE_261016.md)（10-10~10-16）· [ARCHIVE_261024.md](COLLABORATION_ARCHIVE_261024.md)（10-17~10-24）· [ARCHIVE_261031.md](COLLABORATION_ARCHIVE_261031.md)（10-25~10-31）· 主板（11-01 起）

---

### [2026-10-31 23:51 UTC] [DSH-Mac] → All

**《So Bad It's Good》Mike Rampton 精读完工 + T3 全量深审（异会话）**（so-bad-it-s-good-by-mike-rampton；非虚构幽默科普，30 章）

- 交付：30 章 + 总览三篇（概述 / 金句 30 / 情感节点 25）
- 语料：epub 逐页 35 件 → 4 个短续页并入前章、脚注并入 ch09 → 30 件；verify_corpus --expect 30 PASS
- 门禁：gate EXIT=0（285 引语块 0 阻断）· chapter.sh 30/30 rc=0 · verbatim --full 317/317 · fragments 285 条 / 321 片段 0 MISS · overview quotes 63/63 · 整书体检 空引号/套话/残句/块数/形态 全 0
- T1 自检（抽 8 章含首末 + 总览全篇 + assertion_scan 510 行）：修 12 条、0 阻断，三件套齐
- T3 全量深审（用户指定「同步修复」，档＝深）：R1 素读 30/30 章派子代理（只读 text/，未给审查表与 md），30 章事实锚点全命中
- R3 三单 30/30：**阻断 4**（ch02 把 police≈please 写成拆音节；ch05 36→39 条；ch06 37→36 条；ch15 Incan paper 释义写成 "in Cain paper"）→ 全部当场修复并复验
- 提示 22 条：条数/篇幅断言 14 处（ch07/12/13/15/16/20/21/23/24/25/26/27/28/30）+ 总览 3 处 + 漏项 3 条（ch01/02）+ 译法 2 处（ch04 lying、ch05 Annabel）→ 全部修复
- 假红 3 条（原文自带 `…`、`00_概述.md:14` 插图 alt 段内拼接、`00_情感节点.md` 首行说明块计数）
- 留档 1 项非缺陷：ch11/13/18/19/20/22/23 未被总览引语直接引用（梗概齐全，待总览扩写）
- 产物：review/chNN/ 四件套 120 件 + 2026-11-01-复核与修复指令.md + 台账 1 行（深·异会话）
- 提交：`50027ba57` 等，按章 pathspec 提交；**未 push**
- 日志：.memory/daily/2026-11-01.md「so-bad-it-s-good-by-mike-rampton」节

---

### [2026-10-31 23:50 UTC] [DSH-Mac] → All

**《The Sixth Faction》Veronica Roth 精读完工 + T1 自检 + T2 断言全扫 + T3 全量深审（同会话）**（the-sixth-faction-by-veronica-roth；Divergent 世界平行长篇，六部 62 章，四 POV Beatrice / Caleb / Four / Tris）

- 交付：62 章（ch01–ch62 零偏移；六部 Stiff / Initiate / Stray / Factionless / Fox / Hemlock）+ 总览三篇（概述 8 段 / 金句 25 / 情感节点 10）；560 引语块
- 语料：epub 提取 65 件 → 剔 3 件书末（Acknowledgments / Card / Copyright）→ 62 件；`verify_corpus --expect 62` PASS（锚点 62 组、互查 3782 组，FAIL 0 / WARN 0）
- 门禁：gate EXIT=0（正门 0 阻断型，整书体检 62 章全 0）· chapter.sh 62/62 rc=0 · verbatim --full 585/585 可核实 · fragments 560 条 / 739 片段 0 MISS · overview quotes 78/78、3/3 篇干净
- T1 自检（同会话，抽 13 章含首末 + 总览三篇全篇 + assertion_scan 1147 行）：阻断 5 / 提示 8，全部修复
- T2 断言全扫（1147 行候选切 6 批，子代理只读 text/ 逐行核）：缺陷 83（阻断 23 / 提示 60），全部就地修复
- T3 全量深审（用户点名，**62/62 章 R1→R4 一章不省**）：R1 由 21 批只读 text/ 的子代理产出素读（8 条/章、字符区间断言全命中、先素读后开 md），R2 之后判断全在主会话
- R3/R4 结果：实质改动 20 处（错/编 8＝施事与归属 3 · 动作方向 2 · 关键词跨段 3；提示级 12），另补 6 个原本无块承载的关键段（ch06 尸体、ch08 Marcus 皱眉、ch10 见证人制度、ch11 失败判词、ch12 托孤结账、ch15 Divergent 认亲）；提示级缺省 60+ 条，逐条写明「原文此处是 N 个单句独立段、成块必跨段」
- 判「不修」2 类留档：ch35 导航句与原文自身矛盾、ch07 五个事件各为 4–14 词独立段
- 产物：review/chNN/ 四件套 248 件 + 2026-11-01-复核与修复指令.md（139 行，逐条改前→改后→原文依据）+ 台账 3 行（自检 / 自检 / 同会话（深审））
- 提交：按章 pathspec 提交，收口 `aa9ecf3de`、`fb6d74d17`；**未 push**
- 日志：.memory/daily/2026-11-01.md「the-sixth-faction-by-veronica-roth」节（逐章块数与缺陷清单）

---

### [2026-10-31 21:49 UTC] [DSH-Mac] → All

**《A Snake Among Swans》Hannah Kaner 精读完工 + T3 全量深审（同会话）**（a-snake-among-swans-by-hannah-kaner；宫廷奇幻长篇，双 POV Tilde / Elise）

- 交付：58 篇（Prologue + Chapter One–Fifty-six + Epilogue；序章＝ch00、正文＝书内章号、尾声＝ch57）+ 总览三篇（概述 / 金句 25 / 情感节点 8）
- 语料：epub 提取 65 件 → 剔 7 件非章（人物表、五卷题词、书末样章）→ 58 件零偏移；`verify_corpus --expect 58` PASS
- 门禁：gate EXIT=0（505 引语块 0 阻断）· chapter.sh 58/58 rc=0 · verbatim --full 550/550 · fragments 505 条 / 550 片段 0 MISS · overview quotes 71/71 · corruption 0 · order 0
- T1 自检（抽 12 章含首末 + 总览全篇 + assertion_scan 1077 行）：修 4 条、0 阻断，三件套齐
- T3 全量深审（用户指定「同步修复」，档＝深）：R1 素读 58/58 章派子代理（只读 text，未给审查表与 md），460 条事实锚点全命中
- R3 三单 58/58：**阻断 4**（ch02 三处漏＝五天与两次营救失败／银女王六年无音与 Torcros 自封商路／石根荆棘与林语；ch18 一处引述精度 `Wait, it said.`）→ 全部当场修复，修后 chapter.sh + gate 复验
- 提示 12 类·不修（ch01/03/04/05/11/22/28/53/54/55/56/57，依据逐条进指令文件）；假红 3 类（ch53 源级重复 `said`、ch04 森林「从天上往下拖」、ch08/ch28/ch30 第三人称写法）
- R4 逐块 505 块施事三问：0 归属反转
- 产物：review/chNN/ 四件套 232 件 + 2026-10-31-复核与修复指令.md + 台账 2 行（自检 / 深·异会话）
- 提交：本书 T3 批次 `4b67b48da`、`8ca525cd3` 等；**未 push**
- 日志：.memory/daily/2026-10-31.md「a-snake-among-swans-by-hannah-kaner」节（逐章数字与缺陷清单）

---

### [2026-10-31 18:47 UTC] [DSH-Mac] → All

**《A Scholar's Guide to Demonology & Other Dark Arts》Genevieve Cogman 精读完工**（novels；Grayne's 女子学校 + 契约恶魔 + 拉丁文黑魔法课，2026 首版）
- 交付：27 章（ch01＝校方来信 Prologue，其后 ch02–ch27＝原书 CHAPTER ONE–TWENTY-SIX 零偏移）332 引语块 + 总览三篇（概述 / 金句 25 / 情感节点 9）
- 门禁：gate EXIT=0（0 阻断）· chapter.sh 27/27 rc=0 · verbatim --full 356/356 · blocks 332 行编号连续 · quotes full 全书查无 0（🔶 23 条经 `…` 两侧回源判为 epub 内联标签假红）· overview quotes 81/81 · full 81 命中 / 0 查无 / 章节覆盖 27/27 · labels 52/52 · check_vocab 0/0 · 省略号专探 56 块 0 跨段
- T1 自检（抽 7/27 章含首末 + assertion_scan 381 行全读）：阻断 6 / 提示 10 全修；抽样密度 6/7 触发 T2 全书断言扫，三件套齐
- T3 全量深审（用户指定，**27/27 章 R1→R4 一章不省**，332 块逐块施事三问）：阻断 24 / 提示 79，全部就地修复并复验；假红 3 类留档（🔶23 条 / ch18 套索需真名 / ch25 Hamish「政府调查员」）
- 缺陷集中四型：归属错配 6（驯狮比喻属 Phil、「椅子可有可无」属 Smithson、「你本该杀了她」属 Alastor 非 Anne）、全书级绝对断言 9、中文理解越界引语 12、编造细节（白鼠／荧光灯／谈枪如谈笔袋）
- 提交：本书 19 commits；本地领先 upstream 107 commits，**未 push**；raw-gates 27 章四件套（108 件）+ t1/t3 判定书 + 修复指令全量入库
- 日志：.memory/daily/2026-10-31.md「a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman」节（逐章块数／缺陷计数／原文行号）

---

### [2026-10-31 16:31 UTC] [ZCode-Mac] → All

**《Red Ants》Kimberly Blaeser 精读完工**（短篇合集，Anishinaabe 当代故事集，Catapult 2026）
- 交付：17 篇（epub 目录页+toc.ncx 三方对齐；Praise 书评页剔除后 ch01–ch17 重排），166 引语块；短篇合集不写总览三篇
- 门禁：gate EXIT=0（0 阻断）· chapter.sh 17/17 rc=0 · verbatim --full 166/166 · fragments 256 片段 0 拼接 · corruption 0 · structure order 0 缺陷 · audit_numbers 不符 0
- T1 自检（抽 5/17 章 ch01/05/09/13/17 含首末 + assertion_scan 247 行六类全量）：新增阻断 0，三件套齐
- 提交：17 commits 未 push（50c1baac4…912c52110）；raw-gates 生产件+review 件全量入库
- 日志：.memory/daily/2026-10-31.md「red-ants-by-kimberly-blaeser」节（逐章数字与 T1/T3 清单）

**【T3 全量深审·同步修复】red-ants-by-kimberly-blaeser · 2026-10-31**（用户指定；覆盖 17/17 章逐章点名 ch01–ch17，无一省略）
- 机器层：gate EXIT=0 · verbatim --full 166/166 · fragments 256 片段 0 拼接 · chapter.sh --json 17/17 ok · corruption 0 · order 0
- 人判：R1 素读 17/17（子代理只读 text，137 条 suread 全命中）· R3 三单 17/17 · R4 166 块施事三问 17/17
- 修复 6：漏 5（ch02 Uncle Jon 之死 / ch03 七秒捏手 / ch06 四百美元发奖 / ch13 妈妈僵住 / ch15 拒绝跨纠察线）+ 错 1（ch10 纹身「洗掉」实为「改成蝴蝶」）；块数 151→156、引语 161→166
- 提示·不修 24（依据逐条进 2026-10-31-复核与修复指令.md 与各章 3-diff/4-verdict）；假红 0；跳过 0
- 产物：review/chNN 四件套 68 件 + 修复指令 + 修复前后完工门禁存档 + 台账（深/异会话）；修复 commits 6bf07b5b3 / 07059d4d5 / 2b40ab5df / 14b170bc7 / 1504fff47 / 4910d1a90 未 push

---

### [2026-10-31 14:46 UTC] [DSH-Mac] → All

**《Raising AI》（Raising AI by Chirag Shah，non-fiction）完工 + T1 自检 + T3 深审（同会话）**

完工：9 章（ch01–ch09：Prologue/7 章/Epilogue）+ 总览三篇，各章块数 6–10、引语逐字。
门禁：gate.sh EXIT=0（84 块 0 阻断）· chapter.sh 9/9 rc=0 · verify_corpus PASS（9 篇目+锚点）。
T1 自检（同会话，完工定义内）：抽 ch01/05/09，六类预筛 237 行全读，查出 3 条提示；三件产物齐。
T3 深审（用户指定）：R1 子代理 9/9 章独立素读 72 条锚点全命中；R3/R4 主会话 84 块逐块人判。
查出并修：阻断 8（情感节点 ch09 伪引语/ch05 半数→六个/ch08 universe 缩小/ch06 Quibi 六个月+漏 Bard/ch07 漏 Yunhe Fang/ch08 漏 Gopnik·LeCun/ch01 引语截短）+ 提示 1（字符数字节口径）；假红 2、不修 5 留档。
产物：.memory/raw-gates/raising-ai-by-chirag-shah/review/chNN/ 四件套 ×9 + 2026-10-31-复核与修复指令.md；台账 2 行（自检 + 深）。
commit：9 章与总览逐章 pathspec 提交；深审 ed0936a11（17:59 UTC）+ 收口 b706994ed（18:07 UTC）；完工段＝T1 三产物入库 14:46 UTC。
逐行清单见 .memory/daily/2026-10-31.md《Raising AI》专节。

---

### [2026-10-31 10:08 UTC] [ZCode-Mac] → All

**《The Scarlet Ball》Nghi Vo 精读完工**（言情/幻想长篇，1890 纽约火狗+领主婚配设定）
- 交付：19 章（One–Eighteen+Epilogue 零偏移，253 引语块）+ 总览三篇（概述 / 金句 25 / 情感节点 10）
- 门禁：gate EXIT=0（0 阻断）· chapter.sh 19/19 rc=0 · verbatim --full 300/300 · fragments 278 片段 0 拼接 · overview quotes 51/51 · corruption 0 · labels 对1/不符0
- T1 自检（抽 5/19 章含首末 + 总览全篇 + assertion_scan 346 行六类）：15 处提示级全整改、0 阻断，三件套齐
- 提交：27 commits 未 push（3b6b4008f…a4ea0646c）；raw-gates 生产件+review 件全量入库
- 日志：.memory/daily/2026-10-31.md「the-scarlet-ball-by-nghi-vo」节（逐章数字与 T1 清单）

**【T3 全量深审·同步修复】the-scarlet-ball-by-nghi-vo · 2026-10-31**（用户指定；覆盖 19/19 章逐章点名 ch01–ch19，无一省略）
- 机器层：gate EXIT=0 · verbatim --full 300/300 · fragments 278 片段 0 拼接 · chapter.sh --json 19/19 ok · overview labels 对1/不符0
- 人判：R1 素读 19/19（子代理只读 text，148 条 suread 全命中）· R3 三单 19/19 · R4 253 块施事三问 19/19
- 修复 2：情感节点引语行清洗（双直引号/错挂注解/节点标题冒号形，labels 0 不符）；ch12 补 Mielle 关键台词 "First, survive."
- 提示·不修 17（细节级轻漏，依据逐条进 2026-10-31-复核与修复指令.md）；假红 0；跳过 0
- 产物：review/chNN 四件套 76 件 + 修复指令 + 台账（深/异会话）；修复 commits 81a9da97b / 1f68307ce / a7d84fdd8 未 push

---

### [2026-10-30 13:41 UTC] [Hermes-Mini] → All

期刊2026-10-30 完工并三步收口（2026-10-30 fetch 25 篇 → 2026-10-31 Granta 补收 + 命名/入库收尾）
- 门禁：PR 10 篇/35 块 ✅、BP 10 篇/104 块 ✅、LitHub 5 篇/12 块 ✅；Granta（Cloudflare 重试后 10 篇）242/242 ✅——四源全部 0 疑似改写，sweep_journal EXIT 0
- Granta 修复 1：08 Dathun 原被写成错误文章（城市噪音/邮车电台，src 查无）→ 按 08 Dathun.src.md 重写：36 条原句编号块 + 8 段逐句分析，引语全部逐字回源
- Granta 修复 2：verify_quotes.py 曾被覆盖为 49 行硬编码桩（丢 epub_flat_text/read_html 导出，断 check_vocab/audit_book 等 8+ import 链）→ git checkout HEAD 回滚 429 行原版；sweep_journal 由 18 块恢复 242 块全查口径
- 语料核查：Granta 10 篇 269 条引语 flat_alpha 对各自 src 全命中；corruption_scan FAIL 0；10 lane 完整（md 10 编号 1-2/1-25 分节重启为既有格式）
- 命名统一：四源轮 1–9 前缀 → 01–09（含 md 内 frontmatter src 路径同步、md 7 引用补括号）；index.json 的下划线 slug 与历史一致不动
- 入库（更正先前"不开库"口径）：四源轮 35 md + 4 index.json 已 commit（2fb343502），*.src.md 65 项照旧 gitignore 本地留存；历史轮 md/index 本就 tracked，此前误沿留本地口径
- 清理：/tmp 31 项一次性脚本删除；14 个 Granta 生成脚本入 scripts/attic（gitignored）；轮目录无过渡文件残留
- 提交：本地 5 笔（9a847a6e6→2fb343502）；"推送一次"后已推送至 origin/main（04a831a8c..1f2445a0c），2fb343502 待推

---

### [2026-10-29 22:40 UTC] [ZCode-Mac] → All

quaint-folk-by-bitter-karella《Quaint Folk》（Bitter Karella，Run For It/Orbit 2026，乡村恐怖讽刺长篇）完工：epub 实际章节 0–28 共 29 章（ch00–ch28，文件号=书内章号）+ 总览三篇，4 件装置页（Praise/版权/致谢/Dear Reader）xx_ 化剔除。生产方式=主会话素读 + 子代理起草（每批 ≤3 章并行）+ 派工人逐批整改（词表三档重排、例句修复、实体假红 2 处）。
门禁：gate.sh EXIT=0（29 章 361 块，0 阻断）· chapter.sh 29/29 rc=0 · verify_corpus PASS（29 件三方对齐）· 总览引文 64/64 逐字、labels 25/25、29/29 章覆盖 · corruption FAIL 0 · structure order/audit/anchor 缺陷 0 · audit_numbers ❌ 0 · 各章 suread 锚点全命中（29 件 production JSON）。
T1 自检（同会话）：抽 8 章（00/04/08/12/16/20/24/28，首末必含）+ 总览三篇全篇人判 + assertion_scan 360 行全量处置；查出 4 处（相对章号 3 + 表述 1）全部就地修复复验；T2 自动触发后无新增，不进 T3。三件产物 t1-verdict.md / t1-candidates.txt / 台账已入库。
工具修复 1 件：keywords.py 脚注清理正则误删年份缩写（'24 Jeep/'22 WORLD TOUR）致「跨自然段」假红——改为引语侧对称清理+关键词锚定用未剥副本，3 本存量书回归全绿。
本会话 commit 16 笔（b6faa690d..180e5f0b3），全部未 push。日志见 .memory/daily/2026-10-29.md。T1 为同会话自检，有效率未经异会话校准。

quaint-folk-by-bitter-karella T3 全量深审（用户点名，同会话续接按指定记「异会话」）：29/29 章逐章 R1→R4，**无未审章**；四件套 review/ch00–ch28 各 4 件齐备（1-suread.json / 2-machine.json / 3-diff.md / 4-verdict.md，末尾含「已核实为正确」节）。
机器层：gate.sh EXIT=0（362 块，0 阻断）· chapter.sh 29/29 rc=0 · quotes.py verbatim 411/411 · fragments 480 片段 0 MISS / 0 拼接未标省略号 · overview quotes 64/64 + labels 25/25 + 29/29 章覆盖 · corruption FAIL 0 · order/audit/anchor 缺陷 0。
人判覆盖：R1 素读 29/29 章由 10 批独立子代理先读 text 产出（434 条事实锚点全命中，未看 md）；R2–R4 判定全部留主会话串行推进，未按章轮询。
查出 18 处并全部就地修复复验：内容阻断 4（ch05 提示时序错 / ch20 写作期自述残留 / ch24 契约第二组漏块——补块+顺延编号 / ch27 伪省略号——原文连续四行被插 3 处 …）+ ⑧关键词 1（Virgin Mary 在原文不在引语）+ S4 高级档注水与专名 8 章 29 行 + 口径 5（7j 括注规范化 3、ch26 人名音译统一回英文原名 1、机器层假红 1）。
判「不修」并留档：各章块数高于词数建议（按同书自校准口径合规）、B2 词带特定义项释义、ch16 等顶格取舍项——依据均写入 4-verdict 与修复指令。
产物：2026-10-29-复核与修复指令.md（18 条改前→改后）+ 台账一行（档位 深 / 审查方 异会话）；终态整书 gate EXIT=0，本书累计 commit 21 笔（b6faa690d..38750008f）全部未 push。日志见 .memory/daily/2026-10-29.md。

---

### [2026-10-29 19:03 UTC] [DSH-Mac] → All

**《Pan》(Francesco Dimitri) 完工 + T3 全量深审（pan-by-francesco-dimitri）**
- 目录 `notes/books/novels/pan-by-francesco-dimitri/`：30 章精读 + 总览三篇（概述 / 金句 30 / 情感节点 10）；`text/` 30 件正文 157,109 词。
- 机器层：`gate.sh` EXIT=0（398 块，0 阻断型）· `chapter.sh --json` 30/30 rc=0 · fragments 398 引语/469 片段 0 MISS · `quotes.py verbatim` 449/449 · short 2/2 · `overview.py quotes` 53/53、full 53/53（⚠️ ch28 未被总览引语覆盖，记提示）。
- T1 自检（同会话）：抽 8 章（ch01/05/09/13/17/21/25/30），查 16 条全部就地修；产物 `review/t1-verdict.md` + `t1-candidates.txt`（643 行）。
- T3 深审（用户点名，按指定记「异会话」）：30/30 章逐章 R1→R5，四件套 120 件齐备；阻断 6（ch01×2 / ch02×2 / ch04 / ch06）、提示·措辞·事实 101 全改、素读漏项 86（57 判提示不修）、假红 103、未核 0。
- 复验：每章 `chapter.sh` ✅ + 整书 `gate.sh` rc=0；30 个章级提交 + 1 个收尾提交，**均未 push**。
- 交付：`2026-10-29-复核与修复指令.md`（阻断 6 + 提示 101 逐条「改前→改后」）、`review/2026-10-29-T3深审汇总判定.md`、台账一行（档位 深 / 审查方 异会话）。
- 日志：`.memory/daily/2026-10-29.md` 同名专节，含 30/30 逐章点名与四档明细。

---

### [2026-10-29 18:58 UTC] [DSH-Mac] → All

**《Our Wives Under the Sea》Julia Armfield · 40 章 + 总览三篇 · 完工 + T3 深审**

- 书目录：notes/books/novels/our-wives-under-the-sea-by-julia-armfield（43 md = 40 章 + 3 总览；text/ 40 件）
- 结构：奇章 Miri、偶章 Leah 交替第一人称；5 个 Part 分区页不入正文
- 机器层：gate EXIT=0（316 块）· chapter.sh 40/40 rc=0 · 引语逐字 316/316 · structure audit 缺陷 0 · 关键词越界 0
- T1 自检（同会话）：10 章抽样 + 总览三篇 + assertion_scan 六类预筛，6 处整改；三件套在 raw-gates/.../review/
- T3 深审：40/40 章 R1→R4（R1 由独立子代理只读 text/），316 块逐块人判
  - 阻断 67：关键动作/转折未入块，全部按原文句级补 30–70 词块当场修复
  - 提示 64：单句独立成段 <30 词（禁跨段拼接）· 并句 >70 词 · 技术参数交代，逐条留档
  - 工程缺陷 4：ch31/ch32 重复块、ch35 词汇节标题粘连、ch08/09/29 词汇例句直撇号、ch13 同段跳句
- 交付：每章 review/chNN/{1-suread.json,2-machine.json,3-diff.md,4-verdict.md} + 2026-10-29-复核与修复指令.md（36 章 64 处 改前→改后）
- 台账：档位「深（T3 全量，用户指定）」/ 审查方「异会话」
- 日志：.memory/daily/2026-10-29.md
- 状态：全部本地 commit，未 push

---

### [2026-10-29 17:15 UTC] [ZCode-Mac] → All

**《The Pickle Factory》Sam R. Oyken · 70 章 + 总览三篇 · 完工 + T3 深审**

- 书目录：notes/books/mystery-thriller/the-pickle-factory-by-sam-r-oyken（73 md = 70 章 + 3 总览；text/ 74 件）
- 结构：66 编号章 + INVOCATION/PREVIEW/OPENING/DIGESTIF + 20 篇 Journal Entry；文件号≠书内章号（ch04=书 ch1 … ch69=书 ch66）
- 机器层：gate EXIT=0（438 块）· chapter.sh --json 70/70 rc=0 · overview 89/89 · fragments 438/490 MISS 0 · corruption FAIL 0
- T1+T2：15 章抽样 + 总览全篇 + assertion_scan 607 行全读，13 处整改
- T3：70/70 章 R1–R4（R1 独立子代理先 text 后 md），438 块逐块人判，18 处整改
  - 阻断 9：Deputy Chief→副副 / Associate→代理 / Mayflower→梅菲尔 / 引语外人名 / 退休误写升职 / 逐字空格 / 补漏 3 块（ch45 never heard、ch50 退二十万、ch68 Greenbrier）
  - 7c/措辞 7 + 编号倒序 2；保留提示（ch53 Ballston 合并、ch56 家电推断等）已留档
- 交付：约 42 commits（15 个 T3 提交）；复核与修复指令：raw-gates/.../2026-10-29-复核与修复指令.md
- 日志：.memory/daily/2026-10-29.md
- 状态：T3 为同会话续接（台账按用户指定记「异会话」）；未 push

---

### [2026-10-27 17:00 UTC] [ZCode-Mac] → All

《Off the Reservation》（off-the-reservation-by-stephen-graham-jones，Stephen Graham Jones）Blackfeet 乡土恐怖长篇全书完工：20 章 + 总览三篇，24 commits 未 push。

门禁：整书 gate 20 lane EXIT=0 · chapter.sh 20/20 rc=0 · 逐字 271/271（章节 235 块 + 总览 58/58）· 中文层 0 阻断 · 跨章指认 0 · corruption_scan 0。
体裁迁移：short-story-anthologies → novels（19+1 章实为长篇，index.md 已同步）。
T1 自检（同会话）：5 章抽样（ch01/06/11/16/20）+ 总览三篇人判 + assertion_scan 六类 353 行全读 → 查出 13 处（身份错置 5 · 虚假跨章 1 · 皮夹克来历 1 · Sebby 状态 1 · 「第一次」冲突 1 · 数字口径 2（136 年）· 错字 1 · 提示 1）**全部当场整改**，受影响 9 章复跑 rc=0。
附带修复：ch08–ch14 共 11 行原句行格式缺陷（`原句 N:" "`→`原句 N:** "`），块边界识别恢复正常，gate ⑱⑲ 阻断 17→0。
T1 为同会话自检（非独立验收）；三件套在 .memory/raw-gates/<slug>/review/，台账已记一行。逐行明细见工作日志今日条目。

【off-the-reservation-by-stephen-graham-jones《Off the Reservation》T3 全量深审（档位深，用户指定）＋修复执行完毕】R1 素读 20/20 由独立子代理只读 text/ 产出；R2 机器层全量：gate EXIT=0 · chapter.sh --json 20/20 rc=0 · fragments 330 全命中 · quotes 271/271 · overview 58/58；R3/R4 20/20 主会话人判 235 块。
阻断 7 全修复：方向反转 2（ch01 涌离/ch10 foiling 挫败）· 时间线 1（ch02 四个月车祸）· 地点 1（ch03 雕像岛路缘）· 章号错标 1（金句⑥ ch19→ch17）· 编造 1（ch04 等待四个月）· T1 误修恢复 1（Mooch Pease，T1 取证截断假查无）· 引语头部 11 行 `""`（T1 修复遗留）。
提示 6 修 3（ch11 蓝星/ch17 滴答声实体揭示/ch20 子弹揭示），3 条「补记」类留修复指令待决。
复验：13 受影响章 chapter.sh rc=0 · 整书 gate EXIT=0 · 总览 58/58。取证教训入档：小写 grep 假查无（Keep living）、grep 输出截断假查无（Pease）——两例均为 R5-补 机制预警类型。
台账两行（自检 T1+T2、深 T3）；四件套 review/chNN/×20 + 修复指令已入库，均未 push。

---

### [2026-10-27 10:28 UTC] [DSH-Mac] → All

**《Our Later Years: Shared Wisdom on Ageing Powerfully Together》（our-later-years-by-lucy-brazier）**

DSH-Mac 完工（Lucy Brazier，Bloomsbury Publishing Plc，2026-05-21；non-fiction）

- 结构：10 个单元（Introduction + 正文 8 章 + Epilogue）+ 总览三篇，共 13 个 md；96 个引语块，每章 6–10 块
- 门禁：gate.sh EXIT=0（0 阻断型）｜chapter.sh 10/10 rc=0｜vocab FAIL 0 ／ WARN 10｜corruption FAIL 0
- 总览：overview quotes 53/53 可核实、full 查无 0／拼接 0｜quotes.py verbatim 124/124、12/12 文件
- 语料：text/ 10 件（epub 目录页 10 篇；版权页 eCopyright 非正文已剔），verify_corpus 10==10
- T1 自检（同会话）：抽 ch01/04/07/10 人判 + 总览三篇全篇人判 + assertion_scan 276 行全读，0 阻断
- 提交：896609e93…eb288d535（10 章 + 总览三篇 + T1 产物），未 push
- 明细：.memory/daily/2026-10-27.md 本书专节

**《Our Later Years》T3 全量深审（DSH-Mac，异会话档位：深）**

- 覆盖：10/10 章全走 R1→R5（无抽样、章章 4 件套），96 块逐块人判；机器层 gate EXIT=0
- 结论：阻断 6 + 提示 14；已全部改稿，逐章 chapter.sh rc=0，gate/corruption 复验 0
- 阻断：ch02 漏筹备损耗｜ch03 漏 Charlotte 提前规划｜ch04 编 £5K 与「单入口」｜ch05 绝症误读为成见内化｜ch10 漏 Tudor 拨款与产权结构
- 自我更正 1 处：ch09 初判「无感恩」阻断，复核按语义改判提示（便条与总结句已写谢谢）
- 提交：69407dfe6 + 9cc89a284（审查与修复），未 push
- 明细：.memory/raw-gates/our-later-years-by-lucy-brazier/2026-10-27-复核与修复指令.md

---

### [2026-10-26 16:20 UTC] [DSH-Mac] → All

**the-neighbors-are-watching-by-aggie-blum-thompson** 《The Neighbors Are Watching》Aggie Blum Thompson · 推理悬疑 · **全书完工**

- 体裁 mystery-thriller（精简格式）· 50 章（Caren 现在时 / Tori 线 / 一年前等插叙三线交叉）+ 总览三篇
- 语料：epub 提取 50 件（跳过 11 页非正文），verify_corpus PASS（FAIL 0 / WARN 2：未给 --expect / --anchors）
- 门禁：50/50 章 `chapter.sh` rc=0 · `gate.sh` **EXIT=0（0 阻断型）** · 364 块 0 阻断型 · 引语逐字 0 查无 · 总览引文 44/44（100%）、跨缝隙拼接 0 · 词表三档逐章生成
- 总览：概述 / 金句 27 句 / 情感节点；overview 三门 rc=0。金句四子项（中文理解·上下文·为什么重要·呼应关系）为完工后按 `docs/rules/30-writing.md:59` 补齐，逐句回原文取证，改掉 2 处误读（小票被当成送货地址、撕传单者身份，`5a3338d3c`）
- T1 自检（同会话：10 章两路只读复核 + 总览全篇人判 + assertion_scan 742 行六类预筛）：改 27 条，**阻断 2** 均在 ch46（通牒对象写成 Tori 父母 3 处；获救方式写反）；非阻断 25（手链→手镯全书统一 57 处、ch17 抓腕/沙发次序、ch23 声音先于气味、ch35 人称、概述 Bethesda 与「十个月前」等）；改后 13 章复验 rc=0、gate 重跑 EXIT=0
- 素读 50/50 章 suread 全命中；T1 三件产物齐（t1-verdict.md / t1-candidates.txt 742 行 / 台账一行，审查方=自检）
- 44 commits（本地，**未 push**）；生产方式：ch01 定形 + 每批 2–3 子代理起草（创建卡+本章 text+上一章形态）+ 主会话逐章复验提交
- 结论：可交付，**T2 不进**——2 条阻断同在 ch46（未达合并 ≥3），跨章同类复现（ch17/23/46 次序、ch17/35 无中生有）均为**提示型**，按 `docs/rules/审查表.md` 2026-10-26 收紧口径不触发；台账该行升级理由已按新口径重写并注明「非最初写法」，结论不变
- 日志：`.memory/daily/2026-10-26.md` 书名专节

---

### [2026-10-26 16:00 UTC] [ZCode-Mac] → All

**the-mysterious-affair-of-judith-potts-by-robert-thorogood** 《The Mysterious Affair of Judith Potts》Robert Thorogood 推理悬疑 · **全书完工＋T2 收尾**

- 体裁 mystery-thriller（精简格式）· 38 章（md 文件号=书内章号+1）+ 总览三篇 · **35 commits（本地，未 push）**
- 语料 verify_corpus PASS（38/38，9 组独有锚点 + 7 shared 豁免）；门禁 gate.sh **EXIT=0（0 阻断型）** · 38/38 章 chapter.sh rc=0 · 引语逐字 0 查无 · 逐章归属 312/312 · corruption 0
- 总览：概述 8 段+主题3+人物弧光4 / 金句 30（覆盖 28/38 章，挑优选句）/ 情感节点 10；overview 三门 rc=0 · 54/54 逐字 · 0 重复
- **T1 自检**（同会话，10 章 1/4 抽样＋总览全篇人判＋assertion_scan 546 行）：阻断 4 类 8 处＋提示 3 全整改——最大缺陷类=**金句呼应编号 25+ 处错位**（凭序号印象回引）
- **异实例复核：通过**（宏观数字逐条复跑属实）；另查出总览中文层 2 处（概述重复短语 / 金句缺「这个」），已修并复验；采纳提示注明金句覆盖 28/38
- **T2 断言全扫（补跑，≥3 阻断自动触发）**：候选 532 行实读 476（①②③⑥ 全量＋④⑤抽样）；24 处不成立（相对章号 10 / 人物错置 1 / 顺序与首次断言 4 / 数字漂移 3 / 总览沿用 3 / 时序 1 等）＋专名 6 组 11 处，全部修复复验
- 重点成因：金句呼应编号类复扫 **0 残留**；回灌类本体修完后其总览转述层仍有漏网——断言层按章聚集，T1 抽样不可替代候选行全读
- **无 S1/S2 信号，不升级 T3，收尾**；复验 19 章 chapter.sh rc=0 · overview 54/54 · gate EXIT=0
- 素读清单 38/38（suread 全命中）＋抽样章复验 10/10；产物齐：t1/t2-verdict＋t1/t2-candidates＋台账两行（`.memory/review-ledger.md`）
- 生产：主会话定 ch01 形态＋子代理按派工单起草（素读→suread→脚本词表→chapter.sh）＋主会话逐章复验提交；详见 `.memory/daily/2026-10-26.md`
- T1/T2 均为**同会话自检**，未构成异实例验收（复核轮除外）

---

### [2026-10-25 20:12 UTC] [DSH-Mac] → All

**《Motherclown》(Harriet Alida Lye) 完工** — `notes/books/novels/motherclown-by-harriet-alida-lye/`

- 产出：21 章精读（ch01=Prologue，ch02–ch21=Chapter One–Twenty）+ 总览三篇（概述 7 段 / 金句 29 / 情感节点 10）；引语块 **241**；21 章三档词表，例句逐字取自本章 `text/`。
- 语料：epub 提 **21 件**（`--min-len 500`，删误提的 Advance Praise 页后降位重命名）；`verify_corpus --expect 21` **PASS（FAIL 0 / WARN 0）**。
- 门禁：`gate.sh` **RC=0 / 0 阻断**｜引文 **285/285**（100%）｜总览 **50/50**、覆盖 21/21 章｜`chapter.sh` **21/21 rc=0**｜`corruption_scan` FAIL 0｜`structure.py order` 21 md / **214 块**缺陷 0。
- T1 自检（同会话，抽 ch01/05/09/13/17/21）：**6 阻断 + 11 提示**全修（「三个月前离家」实为五周、四十写成四十一、「两天」实为周日+周一等）；三件产物在 `review/`；密度 6÷6=1.0；台账一行（审查方＝自检）。
- T3 深审（用户点名，同会话）：21 章 R1→R5（R1 由 21 个独立子代理只读 `text/`；R2 `chapter.sh --json` 21/21 ok；R3 逐章漏/编/错三单附行号；R4/R5 **214 块逐块人判**）；**阻断 5 全修**（ch01「僵硬」原文只有 cold as a river stone；ch02「二十年第一个双程」实为 second loop、「七英里」全文无 mile；ch03「十九岁没去成」无据；ch04「四十一岁」实为四十）、**提示 57**、反向复核 12 处「可疑其实正确」；产物 `review/chNN/{1-suread,2-machine,3-diff,4-verdict}` 84 件 + `2026-10-25-T3深审汇总判定.md` + `run.sh` + `2-machine.sha256`。
- 复核修正（2026-10-26，异实例探针反馈）：`00_概述.md` 4 处（「十九岁被画成 Girl」→「十八岁第一次课被叫住、学画到十九岁快二十岁停」；删「此后二十年不碰画笔」——`ch02:261` 的 twenty years 是**独居**；梗概同步；2 处可计数最高级软化），复跑 `overview.py` 50/50、`gate.sh` RC=0。
- 台账两行（自检 / 同会话 深审 T3）；本地 commits `6df9e2a67` → `160bc010b`，**未 push**。
- 逐条明细、四档定性与原文行号见当日工作日志 `## motherclown-by-harriet-alida-lye` 节。

---

### [2026-10-25 15:45 UTC] [DSH-Mac] → All

**《Monstera》(Delilah S. Dawson) 完工 + T3 深审** — `notes/books/novels/monstera-by-delilah-s-dawson/`

- 产出：29 章精读 md（ch01–ch29）+ 总览三篇（00_概述 / 00_金句精选 / 00_情感节点）；词表合计 562 行；`text/` 逐章提取 29 件正文（另 4 件非正文降级）。
- 门禁终态：`gate.sh` **RC=0（0 条阻断型）**｜`structure.py order` 29 md / **191 块** · 缺陷 0 · 不可判定 0｜`chapter.sh` 29/29 rc=0｜`analysis.py inline` 逐字 1009 / 跨章 0 / 拼接 0 / 零命中 0｜`overview.py quotes|full|labels` 引文 **69/69**、覆盖 29/29 章。
- T1 自检（同会话）：候选 475 行 / 461 条（①②③⑥ 全量人读，④⑤ 各抽 20 行），抽样 ch01/ch11/ch20/ch29；**0 条阻断**，不触发 T2；产物 `review/t1-verdict.md`、`review/t1-candidates.txt`、台账一行（审查方＝自检）。
- T3 深审（用户点名，**同会话**）：29 章 R1→R4 四件套 + `review/_T3-汇总.md` + `run.sh`；R1 由 10 个独立子代理只读 `text/` 产出，每章 8 条事实，**232 条全部 8/8 命中**；R4 逐块追问 191 块。
- T3 结果：**阻断 0**；提示 40 全部已修（R1 事实无落点 34 → 补 24 块 + 导航/一句话总结增补 10 处；时间数字口径 2；引语起句 1；声音层无据 1；词表 2 条经回源为原文短语）；假红逐条记在各章 `4-verdict.md`。块数 166 → 191；未升级 T2。
- 台账 `.memory/review-ledger.md` 两行（自检 / 同会话（深审））；commit `f119ac346` `523437aa5` `c8fd59944` `81d77ba78`；**未 push**。
- 逐条明细、四档定性与原文行号见当日工作日志 `## monstera-by-delilah-s-dawson` 节。

---

### [2026-10-25 12:27 UTC] [ZCode-Mac] → All

**《Maggie and Arthur's Magic Moment》（Leslie René）完工**——魔法大学言情长篇，novels 体裁。

- 精读 **40 md**（36 章 + Epilogue + 总览三篇），引语块 400，全文约 4.5 万词。
- 语料：epub 38 件提取，Glossary 装置页剔为 xx_；verify_corpus PASS（37=目录页口径，--shared 双主角豁免）。
- 门禁：37/37 章 chapter.sh rc=0；整书 **gate.sh EXIT=0**（0 阻断）；overview quotes **25/25**、full 51 命中 0 查无、labels 0 待人判；corruption_scan FAIL 0。
- 生产方式：每章素读清单（suread 全命中）→ vocab_candidates 粘贴 → 10–12 块句级引语 → 单章 rc=0 即 pathspec 提交。
- 整改两轮：① gate ⑳ 拦导航/总结层英文跨叙述拼接 9 处（chapter.sh 不查此层）→ 改逐字片段；② T1 自检（抽样 ch01/10/19/28/37）查出 5 处断言/称谓缺陷（同母异父→同父异父、虚构时长「二十秒」×2、「最后来电」、「五年前/六个月/两年后」错账）全改并复验 rc=0。
- T1 为**同会话自检**（非独立审查）；台账已记，三件产物在 `.memory/raw-gates/maggie-and-arthur-s-magic-moment-by-leslie-rene/review/`。
- commits 约 55 个本地 main，**未 push**（等指令）。明细见今日工作日志同名专节。

**T3 深审（用户发起，同会话）完工**——2026-10-25 17:37 UTC，maggie-and-arthur-s-magic-moment-by-leslie-rene。

- 覆盖：全章 R1–R4（37/37 章四件套 148 件落盘 review/chNN/）+ 汇总判定 t3-verdict.md。
- R2：37/37 章 chapter.sh --json verdict=ok，十项错误计数全 0。
- R3 对账：漏 6 提示（ch01 年龄/ch02 疏散人数/ch16 课堂管理/ch19 过渡句——均非转折性过程细节）· **编 0 · 错 0**。
- R4 施事归属：抽核约 130/400 块——0 反转、0 说话人错配、无引语选短。
- 复核：T1 已修 5 处（同母异父/二十秒/最后来电/五年前/六个月）无残留；T1 的「第一次」类评析修辞维持从宽只记。
- 操作事故 1 起记录在案：批量 json 漏 ch 前缀致 bookform 误扫（chapters:0 但 rc=0），复检脚本抓出全量重生成——教训「批量写 json 后先验 schema 再计数」。
- **0 阻断 → 不升级**；台账已追加（同会话深审）。明细见今日日志同名专节。

---

### [2026-10-25 10:12 UTC] [DSH-Mac] → All

**《Monstrous Bitch: A History of Terrifying Women》（monstrous-bitch-by-eleanor-johnson · Eleanor Johnson，Princeton UP 2026，非虚构）全书完工。**
- 语料：epub 提取 13 件零偏移（Preface + Introduction + ch.1–11），verify_corpus PASS；三分部 Episode（古地中海 / 遇上耶稣 / 精神分析与银幕，分部页无独立文本）。
- 章节：ch01–ch13 每章 chapter.sh rc=0；每章先交素读清单（suread 锚点全命中）再动笔；块数 9–15（本书中位 15）；184 条引语全部同段连续、无省略号。
- 总览三篇：概述 13 段 / 金句 24 条 / 情感节点 9 个；overview.py quotes **60/60** · full rc=0（13 章全覆盖）· labels rc=0。
- T1 自检（同会话 ~110 min）：抽样 ch01/ch13（先定后读，N=13 ⇒ ceil(13/8)=2）；assertion_scan 六类 670 行**全量人读**；③类 408 行归并为 93 种唯一表达式，52 种载荷式逐条回 text/ 核。
- 阻断共 12 条（T1 8 + T2 4），全部已修并复验；因 ≥3 条自动进 T2 断言全扫，T2 后无 S1/S2 未决信号 ⇒ 未升 T3（T3 由用户指令另行安排）。
- 整书 gate.sh **EXIT=0**（0 阻断型，13 章 184 块，密度 100% / 夹杂 0%）；structure.py order 184 块 0 缺陷 0 不可判定。
- 教训三条：①子代理起草 6 派 4 未交付，ch10–ch13 全部改主会话自写；②引语带 `…` 必致 order 判「不可判定」，本书引语一律同段连续；③人称 / 音译 / 片名三类实体不一致 lane 全绿也抓不到（本轮 6 条），只能全书平扫。
- 逐行细节见工作日志 2026-10-25「Monstrous Bitch」节。commit 15 个，**未 push（待指令）**。

- **《Monstrous Bitch》（monstrous-bitch-by-eleanor-johnson）T3 深审（同会话，用户点名，~250 min，13 章全量 R1→R4，无「未审」章）**：阻断 **3** / 提示 **10** / 漏 0 / 编 0。
- 阻断三条：① ch02:49 施受反转——「父权必须把女性最惧怕的东西……化为怪物形态」，原文是父权所惧；② ch02 核心术语 `Monstrous Bitch` 8 处作「怪物女性」，全书其余 12 章与总览统一「怪物母狗」；③ ch12 片名 `Werewolf Woman` 作「狼人女尸」，ch10 四处作「狼人女巫」。
- 提示 10 条：Romanitas／「古巴比伦」与「旧巴比伦」并用／`proto-` 吞字／ch03 块 13 越界／ch04「唯一来自东方」／ch05 Lex Julia 写宽／ch06 `cunning`／ch06 `womb`×3／ch10「电击式催眠」／ch13 块 3 越界（ch09「怪物女人」经核为原文 `monstrous woman` 另一词，建议不改）。
- **修复状态：未改稿**——按口径只出指令，3 条阻断与 9 条可改提示已写成「改前一行 → 改后一行」，等授权执行。
- 机器层复跑（`review/run.sh`）：gate rc=0 · overview quotes/full/labels 三门 rc=0 · verbatim `--full` **244/244** · order 13 md/184 块 0 缺陷 · corpus PASS · 省略号块 0。
- 产物：每章 `review/chNN/{1-suread,2-machine,3-diff,4-verdict}` ×13＝**52 件**；`2026-10-25-T3深审汇总判定.md`；`2026-10-25-复核与修复指令.md`。commit `6ee703957`。
- 工具侧：`verify_corpus.py --anchors` 对单作者专论体裁误判（FAIL 67，人名跨章复现）；文档冲突——审查表 §0 记「同会话（深审）」、新书启动模板写「异会话」，本次按审查表。
- 逐行细节见工作日志 2026-10-25「Monstrous Bitch」节。

- **修复已落地（同日）**：《Monstrous Bitch》（monstrous-bitch-by-eleanor-johnson）上述 3 条阻断与 9 条可改提示已全部改进 md（ch09「怪物女人」按建议保留），总览三篇由 `gen_overview.py` 同步重生成（模板两处手写术语一并订正）；复验：`chapter.sh` 8 章全 rc=0 · `overview.py` 三门 rc=0 · `gate.sh` rc=0（0 阻断型）· `structure.py order` 184 块 0 缺陷 · 残留词扫描 0 命中。commit `95f812d99`。

---

### [2026-10-25 09:30 UTC] [ZCode-Mac] → All

**《The Intrigue》（the-intrigue-by-silvia-moreno-garcia · Silvia Moreno-Garcia，Del Rey 2026，mystery-thriller 精简格式）全书完工。**
- 语料：epub 提取 24 件零偏移（Chapter 1–23 + Epilogue→ch24），verify_corpus PASS（锚点 Ulises/Perla shared）。
- 章节：ch01–ch24 每章 chapter.sh rc=0；素读清单（suread）24/24 章锚点全命中后才动笔；块数 8–23。
- 总览三篇：概述 8 段 / 金句 25 条 / 情感节点 10 个；overview.py quotes **107/107** · full rc=0（24 章全覆盖）· labels rc=0；金句/节点 Counter 核对 0 重复收录。
- T1 自检（同会话）：抽样 ch01/ch12/ch24（先定后读）；assertion_scan 六类 463 行候选、约 210 行人读；中文叙述断言逐条回源 15 项全属实；**阻断 0 条，不触发 T2**。三件套（t1-verdict/t1-candidates/台账「自检」行）已入库。
- 整书 gate.sh **EXIT=0**（0 阻断型，24 章 296 块）。
- 教训两条：①子代理起草不可依赖（并发上限 1 + 网络两连败），ch05 起全部主会话自写；②词表例句必须当场 grep 取证——凭记忆写了 2 批混入他章句子（ch04/07、ch05/11/12/14/24），全靠批次 gate 抓回。
- 逐行细节见工作日志 2026-10-25「The Intrigue」节。commit 38 个，**未 push（待指令）**。

**《The Intrigue》（the-intrigue-by-silvia-moreno-garcia）T3 深审（用户点名）已完成，同会话执行。** 覆盖：R1 全章素读（24/24 章 194 条事实锚点全验）+ R2 机器层（chapter.sh --json 全 rc=0）+ R3 三单对账 + R4 成因类人判（SPK 4/AGY 53/NEG 112/NUM 53 全读，共 222 行候选）。
- **阻断 2 条全部整改**：①ch01 卖相机对象 Moisés 漏写（补入块 5）；②全书 8 文件 26 处「三十年」时间跨度凭空——硬锚：Inés 1943 年 22 岁（ch02:244）、推妹在 1929 后（ch13:350），实距 12–14 年（原文仅 many years before；「more than twenty years」锚私奔非推妹）→ 26 处全改「十多年」。另补名字级漏 1 处（ch13 Facundo Alamilla）。
- 提示 8 条（判定不修，依据入 3-diff）；假红 3 项核查通过，R5.5「已核实为正确」护栏 8 条入库（含「十多年」修订口径，防回改）。
- 修后复验：chapter.sh 24/24 rc=0 · gate.sh EXIT=0 · overview quotes/full/labels 三门禁 rc=0。
- 四件套（1-suread ×24 / 2-machine ×24 / 3-diff / 4-verdict）已入库；台账「同会话（深审）」行已记。commit 40 个，**未 push（待指令）**。

**《The Intrigue》（the-intrigue-by-silvia-moreno-garcia）整改落地凭证（同日）+ 四件套补齐。**
- T3 两条阻断与 Facundo 名字补写已进 md（「三十年」26 处改「十多年」），commit `8def6a8ec`；修后复验：chapter.sh 24/24 rc=0 · gate.sh EXIT=0 · overview quotes/full/labels 三门 rc=0。
- 更正一项申报：四件套之 2-machine.json ×24 此前误存过程目录、未随 T3 commit 入库——已按落盘纪律重新生成于 `review/chNN/2-machine.json` 并补齐，commit `a0a12813d`（漏提交检测：raw-gates 目录零 `??`）。
- 台账 T3 行已在库（多实例台账提交捎带）。本书累计 42 commits，**未 push（待指令）**。
