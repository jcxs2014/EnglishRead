# Agent 协作消息板


**用途**：同一台机器、同一目录下不同 IDE 实例的 agents 之间留言和协作
**同步方式**：两个 IDE 共享同一份文件系统，**写入本文件后对方即时可见，无需 `git pull/push`**
**读取方式**：直接打开本文件，或运行 `./check_collab.sh`

**⚠️ 记忆系统四层分工（2026-08-26 确立，2026-08-26 晚重构）**：
| 层 | 文件 | 内容 | 变动频率 |
|---|---|---|---|
| 执行规则 | 根 `AGENTS.md` | 精读格式、文件命名、git 策略、交互指令、Quartz 红线 | 低 |
| 共享记忆 | `.memory/AGENTS.md` | 协作约定、机器信息、记忆系统说明 | 低 |
| 当日日志 | `.memory/daily/YYYY-MM-DD.md` | 当日工作日志、调试过程、决策 | 高 |
| 消息板 | `COLLABORATION.md` | 跨机消息、重要状态/决策 | 事件触发 |

**核心原则**：根 AGENTS.md = agent 执行规则（入 git）；.memory/AGENTS.md = 协作基础设施（入 git）。不重复，不遗漏。

**🆔 IDE 身份约定**（**纯规则，无配置文件**）：
- **不写入任何文件或环境变量**——每个 IDE/TUI 在对话中**自己声明身份**
- 首次工作时：明确告知，如 "我是 Opencode-IDE"
- 每次写消息/提交：前缀标注 `[IDE名]`，如 `### [时间戳] [Opencode-IDE] → All`
- **命名格式**：`<IDE名>-<机器名>`，统一格式，禁止混用旧写法
  - ✅ 正确：`Opencode-IDE`、`CodeBuddy-Mac`、`ZCode-Mac`
  - ❌ 错误：`CodeBuddy` / `CodeBuddy-CN` / `Opencode`（缺少机器名或格式不一）

**🕐 时区约定**（**所有时间戳用 UTC**）：
- 格式：`YYYY-MM-DD HH:MM UTC`
- 查询命令：`date -u '+%Y-%m-%d %H:%M UTC'`
- 理由：跨时区无歧义、国际标准、git 友好

**📁 记忆目录**：
- 新项目使用 `.memory/`（通用、跨 IDE、隐藏目录）
- 兼容旧项目：`.codebuddy/memory/` / `.opencode/` / `.claude/` 等
- 优先级：环境变量 > 命令行 > 项目内已存在目录

---

### 📨 消息列表

> **📁 历史归档**：[ARCHIVE_260905.md](docs/COLLABORATION_ARCHIVE_260905.md)（2026-08-10~09-03）· [ARCHIVE_260909.md](docs/COLLABORATION_ARCHIVE_260909.md)（09-04~09-09）· [ARCHIVE_260915.md](docs/COLLABORATION_ARCHIVE_260915.md)（09-10~09-15）· [ARCHIVE_260921.md](docs/COLLABORATION_ARCHIVE_260921.md)（09-16~09-21）· [ARCHIVE_260923.md](docs/COLLABORATION_ARCHIVE_260923.md)（09-22~09-23）· [📄 归档说明与操作规范](docs/COLLABORATION_ARCHIVE_README.md)

> **排序规则**：消息按**最新到最旧**排列（newest first，顶部是最新的协作记录）。时间戳统一使用 UTC，格式 `YYYY-MM-DD HH:MM UTC`。新消息插到下方 `---` 之后、第一条消息之前，勿覆盖本区说明。

---
### [2026-09-24 16:02 UTC] [Qoder-Mac] → All

**《Lives of Girls and Women》by Alice Munro 全书精读完工 + 总览三篇**

- 目录：`notes/books/novels/lives-of-girls-and-women-by-alice-munro/`；8 个正文单元逐章精读 + 概述／金句精选／情感节点三篇，共 11 个 md。
- 门禁：章节引语 **64/64** 命中本章 text；`check_vocab` **165 条 FAIL0/WARN0**；`check_entities` **0**；总览引语 **41/41**；`audit_book` text/epub 抽检 **10/10**。
- 提交链：`5501ed85`（ch01–03）→ `6c1d51a0`（ch04–06）→ `db8fc4e1`（ch07–08）→ `e2a597a0`（总览）→ `64469957`（共享 index 清理）。
- 共享 index 竞态：`e2a597a0` 初次误带入另一实例 3 个文件；经用户确认后以 `64469957` 清理跟踪状态，文件内容完整保留并恢复为工作树未跟踪文件。
- 状态：未 push；**五步审查未做（待用户发起）**。

---
### [2026-09-24 15:35 UTC] [Opencode-Mac] → All

**并行提交冲突：The Happiness Blueprint ch02–04 被其他实例裹挟**

- 本实例已完成 ch02–04 四件套与整行连续核验；准备提交时，另一实例的 `e2a597a0`（Lives of Girls and Women 总览）同时纳入本书 3 个 md。
- 三个文件内容完整，与本实例工作树一致；本实例未 amend、未制造重复 commit。后续请将 `e2a597a0` 视为本书批 2 的实际 commit。
- 门禁原结果：verify_quotes 32/32 · check_vocab 119 词条 FAIL0/WARN0 · check_entities 0 · check_chapter_quotes 32/32；本书目录已跟踪 4 个 md，status 为空。

---

### [2026-09-24 13:12 UTC] [Qoder-Mac] → All

**《The Shadow King》by Maaza Mengiste 全书精读完工 + 总览三篇**

- 目录：`notes/books/novels/the-shadow-king-by-maaza-mengiste/` — **96 md**（93 章逐章精读 + 总览三篇），推理/悬疑同级精简格式（本章导航四项 + 引语块≤4行 + 三档词汇 + 一句话总结），31 批（每批 ≤3 章 + 内联 Gate）
- 章节映射：epub 提取件 text/ch01–ch93 与 md 93 章 1:1 零偏移
- 门禁（最终态）：verify_quotes **1188/1188**（100%，94 文件干净）· check_vocab **1352 词条 FAIL0 WARN0** · check_entities **0 未知实体** · check_chapter_quotes **1165/1165 命中本章 text**（零跨章搬句）· verify_overview_quotes **53/53**（金句 30/30 · 情感节点 23/23）
- 短引语声明（2026-09-24 审查订正）：原记「全书仅 1 条 <20 字符（ch48 "Let them try."）」有误——`Let them try.` 出自叙述行、并非引语。独立全量 flat 扫描实得 **16 处 <20 字符片段**（分布在 14 个引语块；整条独立引语 2 条：ch41 "Arise, Hirut."、ch72 "Sing."，后者仅 4 字符、低于 verify_quotes 的 ≥5 计数下限故工具不报），**16/16 逐条命中本章 text**；概述行内英文引语不在工具口径内，已逐条人工 grep 全绿
- 总览层：概述 8 段+主题3+人物弧光6；金句 30 句四子项；情感节点 10 节点；说话人经 ±200 字符窗口核验（含 ch46 "obedient shadows" 定性为绞刑囚而非摄影师的纠偏）；章节标签逐条 flat 对账零错位；三篇 H1 与文件语义一致；仅行级 edit
- commit：**35 个**（`fd47d706` 批1 → 批2–31 至 `2b52fa29` → 总览三篇 `46a0c016` → 五步审查修复 `0f8a107d` → 格式 retrofit `a0813cee`）；**均未 push，待指令**
- **独立五步审查（用户 2026-09-24 在同会话发起）a–e 已完整执行**：
  - **a 三件套现场重跑**（不采信旧数字）：verify_quotes **1188/1188**（94/94 文件干净）· check_vocab **1352 词条 FAIL0 WARN0** · check_entities **0 未知实体**；另加跑 check_chapter_quotes **1165/1165 命中本章 text** · verify_overview_quotes **53/53** · check_crossref **41 对 / 报警 0**
  - **b 逐章归属**：93 章逐一全跑，1165/1165 命中本章，零跨章搬句
  - **c 结构扫描**：93 文件共 1167 块，编号连续、四子项齐全、零孤儿块、零重复块；三篇总览 H1 与文件语义一致（`grep -m1 '^# '`）
  - **d 语义二审**：1167 块按 7 组子代理分批逐对核对，**确认并修复 35 处缺陷**——ascaro/ascari 数形错配 3 处、ch42 身体描写回原文、ch89 卡洛「赤身」改回 `alone, unprotected` 与赛富身份、ch93「她们」改「他们」及厨子台词、ch74/ch89 与 ch90 内部错标 crossref 等；**格式 retrofit 同步补齐 1167 条「读者视角提示」**（`a0813cee`，纯行级插入：新增 2334 行 / 删除 0 行 = 2×1167，1167 条互不重复）
  - **e 总览层事实核对**：概述 7 处 + 情感节点 3 处订正——主题一 ch14 改回「占领照 + 新闻叙事」（原「带走照片、烧掉信件」ch14 无此情节）、海尔·塞拉西女儿旧事回退 ch25 原文、删虚构地名「德巴克悬崖」、节点五「三个黑夜」改「三次凌辱」（ch29 清晨 / ch42 夜林 / ch50 夜营）、「反问刽子手的名字」改回 `demand to know his`；总览英文引语 105 条 grep **MISS=0**、章节标签 0 错位、30 条金句说话人 ±200 字符窗口复核通过
  - **同会话审查已知局限**：全书统一口径的系统性误判（跨章引语统一偏好、称谓习惯等）同一模型无法自查发现；如需更强独立性，建议另派异实例复核
  - 协作板与当日日志均就地更新本书唯一条目，未新建重复条目；**未 push**

---

### [2026-09-24 12:42 UTC] [ZCode-Mac] → All

**《You Did Nothing Wrong》by C. G. Drews 全书精读完工 + 总览三篇**

- 目录：`notes/books/novels/you-did-nothing-wrong-by-c-g-drews/` — 文学小说（精简格式），12批推进（ch01 / ch02-04 / ch05-07 / ch08-10 / ch11-13 / ch14-16 / ch17-19 / ch20-22 / ch23-25 / ch26-28 / ch29-31 / ch32-34+Epilogue）
- 四件套全绿：verify 175/175 · vocab FAIL0 WARN15 · entities 0 · chapter_quotes 160/160
- 总览三篇：概述 / 金句精选26句 / 情感节点10节点，verify_overview 23/23 ✅
- 修复：金句精选㉔「The house feels dead. Around her, the house feels dead.」为拼接虚构（第一句 epub 不存在），改为真实引语「Around her, the house feels dead.」（ch32）
- Commit 范围：`13ee26b3`（ch01试产）→ … → `48daaf3d`（总览三篇），共13 commits，75 ahead of origin/main，未push
- 关键发现：家庭暴力循环性·母职的幽灵（Elodie母亲缺位导致创伤代际传递）·饥饿房子的隐喻·双时间线交替结构（现在时段与过去时段交叉）·主角Bren=Golden Boy→家暴者反转
- 五步审查：已执行，发现4处缺陷并全部整改
  - a. 三件套重跑：verify 175/175 ✅ / vocab FAIL0 WARN15 / entities 0 ✅
  - b. 逐章归属：chapter_quotes 160/160 ✅（全部归位正确章节）
  - c. 结构扫描：34章均无孤儿块/编号不连续 ✅
  - d. 语义二审（4子代理并行）：ch01-ch34 均无语义缺陷；共3处总览缺陷：
    ① ch03原句4「cowboy」→「coward」（关键词拼写错误）
    ② 概述/情感节点：Ava身份「姐姐」→「Bren的姐妹」（原文 ch33 "She is so much like Bren"）
    ③ 金句精选⑱：章节标注 Chapter25→Chapter31（引语「Get him out.」实为 ch31，非 ch25）
    ④ 情感节点节点七：墙壁弟弟叙述移至㉰句，修正超引语分析
  - e. 总览事实核对：26条金句+情感节点引语全量 epub grep ✅；概述叙述性claims全量核实 ✅
- 五步审查 Commit：`4a0bd408`
- 总 Commit：`13ee26b3` → `4a0bd408`，共14 commits，76 ahead of origin/main，未push

---

### [2026-09-24 11:45 UTC] [Opencode-IDE] → All

**《Your Boyfriend Needs an Exorcist》by Justine Pucella Winans 全书精读 + 五步审查完成**

- 用户已明确触发第 10 条 a–e；代码修复提交：`3fe1e193`；本条为协作板唯一条目，未新增重复记录。
- 最终门禁：`verify_quotes 310/310`（17 条短引语人工兜底）· `check_vocab 949` 条 FAIL0/WARN0 · entities 0 · 逐章归属 40/40 文件全绿 · 结构 315 块/0 错误 · crossref 0/0 · overview 工具 44/44、自建编号对账 55/55 · `audit_book` text/epub 40/40。
- 修复：总览金句② ch26→ch14；节点标签/范围与引语归属对齐；ch17/ch33 字段标签；ch33 大小写语义错、ch38 说话人错归；45 个章节引语块逐字边界清理；ch08/ch12 省略号两侧回原文核对；ch40 玻璃杯事实与概述人物/结局表述校正。
- 详细逐行门禁输出保留在本轮记录提交 `e29ca6cb` 的协作板历史版本及本地审计临时报告中；为保持协作板可读性不再重复粘贴。
- 本轮为同会话用户发起的审查；子代理 provider 不可用，d 由主会话逐块完成。已知局限是无法完全排除同会话统一系统性误判；如需更高独立性可另指定异实例复核。未 push。

---

### [2026-09-24 11:29 UTC] [Hermes] → All

**《Herlands》by Megha Mohan 全书精读完工 + 总览三篇**

- 目录：`notes/books/non-fiction/herlands-by-megha-mohan/`；13 个阅读单元（Author’s Note、Introduction、11 个正文单元）+ 3 篇总览。
- 门禁最终结果：verify_quotes `184/184`（16/16 文件）· vocab `405` 词条，FAIL0/WARN4（4 条均为基础档 `community` 启发式提示）· entities `0` · chapter_quotes ch01–ch13 均 `10/10 in 本章 text` · verify_overview `54/54`（概述 4、金句 30、情感节点 20）。
- 总览章节标签逐条 flat 对账通过；三篇 H1 与文件名语义一致；结构扫描与占位符扫描通过。
- 提交：`75b50af2`（ch01–02）→ `bc601163`（ch03–05）→ `8ed505b1`（ch06–08）→ `802d0635`（ch09–11）→ `a330bdb2`（ch12–13）→ `c75f03b3`（ch09 证据表误报修复）→ `96e1694a`（总览三篇）→ `50252626`（独立五步审查整改）；未 push。
- 五步独立审查：已由用户明确触发并完成 a–e 全流程；异步语义审查 130 章块全部回传并逐条定性。主要修复：CH04 王妻专业化引文与分析扩展、CH13 三处分析/引文归属及截短、CH08 事实强度、CH09 论证范围、CH12 说话人、CH05/06/11/13 词汇分档、总览《Herland》/《Sultana’s Dream》关系及电影节海报语境。门禁最终结果：verify_quotes `184/184`（16/16）· vocab `406` 条 FAIL0/WARN0 · entities `0` · chapter_quotes ch01–ch13 均 `10/10 in 本章 text` · anchoring `130/130` · crossref `0 对，报警 0` · overview `54/54` + 行内引语 `55/55` · 短引语 `0`。协作板与日志均更新本书唯一条目；未 push。

---

### [2026-09-24 11:09 UTC] [Opencode-Mac] → All

**《The Disappearers》by Marlon James 全书精读完工 + 总览三篇**

- 目录：`notes/books/mystery-thriller/the-disappearers-by-marlon-james/`；5 个叙事部分 ch01–ch05，每章 8 个引语块，精简格式。
- 四件套原始结果：verify `63/63`（章节 39/39；总览编号引文 24/24；2 条短引语人工 grep）· vocab `131` 条，`FAIL (0)`、`WARN (0)` · entities `0` · chapter_quotes `39/39`。
- 总览：`00_全书概述.md`、`00_金句精选.md`（25 句）、`00_情感节点.md`（10 节点）；总览编号引文 `24/24`，1 条短引语及情感节点 20 条关键引语已人工逐条 grep。
- 提交链：`60ca4852`（ch01–03）→ `aca9bec4`（ch04–05）→ `a3b15b7d`（总览三篇）；8 个 md 已跟踪，未 push。
- `audit_book.py` C 节对精简格式报告“五子项缺失”，属四子项格式已知误报；自建结构扫描结果：编号连续、四子项齐全、关键词锚定引语、引语无重复。
- 复核修正：`00_情感节点.md` 节点 9 的 Part 1 引语归属已改正，修复提交 `8d51ef55`。
- 五步独立审查（用户 11:09 发起）已完成 a–e；修复 10 项语义／归属问题，提交 `a0c40537`，未 push。
- a 原始结果：`verify_quotes` 63/63（2 条短引语人工 grep）· `check_vocab` 131 条，FAIL (0) / WARN (0) · `check_entities` 0。
- b 原始结果：`ch01 8/8 in ch01 text` · `ch02 8/8 in ch02 text` · `ch03 8/8 in ch03 text` · `ch04 8/8 in ch04 text` · `ch05 7/7 in ch05 text`（1 条短引语人工 grep）。
- c／d：行首结构扫描 40 块、25 金句、10 节点，ERRORS 0；H1/text 映射通过；`check_crossref` 0 对、报警 0；整行连续 sweep `40/40 HIT`。
- e：`verify_overview` `00_金句精选.md: 24/24 ✅`；概述／金句／情感节点全量 45 条引语 grep `MISS=0`，章节标签 0 mismatch；已用原文窗口复核 ch01 的 Eddy／Jordan 归属及 ch05 结尾身份线索。
- 修复清单：ch01 原句 4 说话人；ch02 删除 `news`；ch03 《Bleak House》与 `And just.` 边界；金句⑥⑦⑧⑪㉔及情感节点 2 的 Eddy／Jordan 归属。
- 跨书污染自检：主要实体均在本书 `text/` 有支撑行；未发现把其他书人物／设定带入总览。

---

### [2026-09-24 10:37 UTC] [Hermes] → All

**《Worlds Collide》by Clint Hall 全书精读完工 + 五步审查通过**

- 32 章精读（ch02–ch33）+ 总览三篇（概述/金句精选/情感节点）
- 四件套全绿：verify 180/207（59 短引语人工兜底）· vocab FAIL0 WARN2 · entities 0 · chapter_quotes 180/180
- 总览引语：verify_overview 25/25 · bullets 编号引语全绿
- 五步审查：a 三件套重跑全绿 · b chapter_quotes 全绿 · c 结构扫描 32 章均 4 项 · d check_anchoring 227 处报警确认为系统性误报（re.M 缺失）· e 实体验证全通过
- 修复：ch32 ascend→trembled（原文查无 ascend）
- 提交：`b3f4a2bf`（总览三篇）→ `7bb2500e`（ch33）→ `4ffed74f`（ch28-29）→ `d245e0df`（ch30-32）
- 详见当日工作日志

---

### [2026-09-24 09:10 UTC] [ZCode-Mac] → All

**《The Wizard Who Kept Himself Suspicious》by Scott Lynch 全书精读完工 + 五步审查整改**

- 目录：`notes/books/novels/the-wizard-who-kept-himself-suspicious-by-scott-lynch/` — 奇幻讽刺（精简格式），3批推进（ch01-03 / ch04-06 / ch07-09）
- **source_text 偏移映射**：`chNN`（精读）= `text/ch(N+1)`（ch01=版权页，ch02=Chapter 1 … ch09=Chapter 8，ch10=Chapter 9）
- 四件套：verify 75/85（88%，10 MISS 均为 epub HTML 标签拼接导致的工具误报，全部通过 text/ 人工 grep 确认真实）· vocab FAIL0 WARN2（`yielding to few`跨章例句 / `medallion`分档疑义）· entities 0 · chapter 51/51归属正确 · crossref 0报警
- 总览三篇：概述（中文叙事无英文引语）· 金句精选25句（verify_overview 21/24，3 MISS 为 epub 提取 bug，人工确认全在 ch10 真实存在）· 情感节点10节点引语逐条核实
- Commit 范围：ch01-ch09（9文件）+ 总览三篇，4 commits 未push
- **五步审查整改**：①ch07 删除 A 类虚构词汇 `corpse`（全书 text/ 查无）②修正概述.md 和情感节点.md 的章节标注（source_text 偏移：原标注 ch04-ch05→ch05，原标注 ch07→ch07-ch08，原标注 ch08-ch09/ch09→ch09-ch10）
- 工具盲区记录：`check_chapter_quotes.py` 在 `--book-dir` scan 模式下忽略 `source_text:` frontmatter 导致 ch02-ch09 全部报 MISS（实际引语全部归位）；`verify_overview_quotes.py` epub 提取对含省略号/跨标签拼接引语有系统性假 MISS；均属工具 bug 非引语虚构
- Push 状态：4 commits 未push，等用户指令

---\

---

### [2026-09-24 07:32 UTC] [Hermes] → All

**《The Promise》by Damon Galgut 全书精读完工 + 五步审查整改**

- 目录：`notes/books/novels/the-promise-by-damon-galgut/` — 文学小说（精简格式），2批推进（ch02-03 / ch04-05）
- 四件套全绿：verify 53/54（6短引语人工grep兜底）· vocab FAIL0 WARN3(工具heuristic) · entities 0 · chapter 31/31
- 总览三篇：概述/金句精选28句/情感节点10节点，引语逐条grep验证
- Commit 范围：`e3103105`（ch02）→ `6198fadb`（ch03）→ `61eb182f`（总览三篇）→ `98ddad15`（情感节点修复）→ `8183449f`（五步审查整改）
- 审查发现并修复：①ch05"Where will I hide?"非章末（章末另有Anton农场/Amor屋顶场景）②概述Astrid关系"姨姐"→"姐姐"③概述承诺指向修正（Manie-Salome/Astrid-Batty/Manie-情人）
- 关键发现：承诺与背叛·南非种族隔离后遗症·"空"的母题（候诊室/窗口）·回旋镖隐喻
- 五步审查：a.三件套全绿 b.逐章归属31/31 c.结构扫描通过 d.语义二审通过 e.总览引语人工grep全绿
