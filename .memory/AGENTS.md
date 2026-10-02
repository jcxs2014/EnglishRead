---
name: englishread-memory-index
description: EnglishRead 工作区跨会话记忆索引
metadata:
  type: user
---

# EnglishRead 记忆索引

> 本文件 = **记忆索引**（不包含规则内容，规则见根 AGENTS.md 和 docs/新书启动模板.md）。
> 新会话读取顺序：system-reminder → docs/新书启动模板.md → 根 AGENTS.md。

## 架构说明：为什么规则留在根 AGENTS.md 而不是本文件

> **结论先行**：执行规则必须留在根 AGENTS.md。本文件只承担"记忆索引"角色。

**加载机制**：根 AGENTS.md 通过 system-reminder 被注入会话上下文（harness 固定行为，不可配置）——但**只注入到预算上限，不是全文**（实测预算 ≈8,000 字符且随会话浮动，见下条「长度与迁移」）。

⚠️ **2026-09-30 更正（本条此前自相矛盾）**：原句前半写「实测它（`.memory/AGENTS.md`）同样被 system-reminder 注入」、后半又写「不在这个加载路径上，需要主动 Read」——**同一句话里两个相反结论**，读者无从取用。**实测证据**：2026-09-27 的截断轮次里它与根 AGENTS 一同出现过；但 2026-09-30 的两轮会话里**均未见它被注入**。⇒ **注入与否随会话浮动，不可假定**。**处置：一律按「需主动 Read」对待**（与 `docs/新书启动模板.md` 同等），启动指令已把它列入必读清单。

把"精读格式/提交门禁/引语逐字规则"搬到 memory 意味着这些执行规则可能不在上下文里，等于丢失。

**三个文件的分工**：
- **根 AGENTS.md** = 执行规则（"必须怎么做"）—— 格式、门禁、引语规则、git 策略。每次作业都须遵守；⚠️ **但自动注入只覆盖文件前段**（实测预算 4,882–8,009 字符，随会话浮动），**不可假定全文可见**——2026-09-30 已把四条 git 红线前移到文件顶部，即为此
- **docs/新书启动模板.md** = 新书开工入口（执行规则速查 + 历史坑表）—— 通过 system-reminder 摘要或用户指令加载
- **.memory/AGENTS.md** = 记忆索引（本文件，"之前发生过什么"）—— 各书完工记录、经验教训、跨书互证坑位。⚠️ **2026-09-27 更正**：原称本文件承担「工具盲区速查」——**本文件无该节**，已随重构迁至 `docs/实测档案/工具链实测.md`（根 AGENTS 工具表有指针）。跨会话积累，按需主动 Read

**长度与迁移**：去重收口仍是第一手段（已收敛 `00_*.md` 重复、9f/10d 重复）。⚠️ **2026-09-27 更正**：本条原写「**不靠搬走内容**」——但当根 AGENTS 涨到 100,670 B 时，**唯一有效的处置就是把案例性长块逐字迁入 `docs/实测档案/`（12 个文件 / 84 KB）**。只去重不迁移，跨不过注入上限。

⚠️ **2026-09-30 更正（尺子本身错了）**：本条原写「**超出 65,536 B 注入预算**」——**口径错误**。实测注入预算是**约 8,000 字符、且随会话浮动**（三次观测 **4,882 / 7,995 / 8,009 字符**）。`wc -c` 报的字节数在中文下约为字符数的 **1.88 倍**，两个口径混用会把真实上限看**松约 4 倍**——这正是 2026-09-29 重构建成「降到 27 KB、余量 58%」却仍有一半规则进不了上下文的原因。
⇒ **凡涉及「注入体积」，一律用字符数**（`len(open(f, encoding='utf-8').read())`），**禁用 `wc -c` 的字节数当上限**；字节数只在 `wc -c` 用于 git/文件系统层面时才有意义。完整实测与处置见根 `AGENTS.md` 顶部说明与 `docs/规则文档结构调整方案.md` §8。

**引用完整性**：模板、脚本、协作板大量引用"AGENTS.md 第 9/10 条"——迁移会破坏交叉引用链。

**怎么判断一条信息该放哪**：
- 如果删掉它，新会话开工会不知道怎么干活 → 放根 AGENTS.md
- 如果删掉它，只是少了"上次怎么踩坑"的参考 → 放本文件



## 核心规则文档

| 文档 | 位置 | 用途 |
|------|------|------|
| 精读执行规则 | `AGENTS.md`（根目录） | 完整执行规则（格式/门禁/工具链/git 策略） |
| **新书启动模板** | `docs/新书启动模板.md` | **每本新书开工前必读**，含执行规则速查 + 历史坑表 |
| 协作消息板 | `COLLABORATION.md` | 跨 IDE 实时消息（newest first，**按完工时间排**） |
| **发消息规范** | `docs/协作板更新指令.md` | **板与工作日志的硬门禁**，2026-09-28 起取代「自己声明身份」的旧纯规则 |

## 发协作板 / 工作日志消息

**一律走 `scripts/post_collab.py`，不要手写 `### [时间戳] [身份]` 抬头。**
身份查 `scripts/collab_identities.json`、时间查 `date -u`——手写就是「身份混乱 + 捏造时间戳」的入口
（2026-08-31 一次事故两处）。**通用规则见 `COLLABORATION.md` 抬头。**
**入口（复制粘贴用的一句话指令）在 `docs/协作板更新指令.md` 顶部**，六步详版、六条硬约束、阈值与假红说明在同文档下方——**先读那一份，不要在别处找发板步骤**。

一条备忘：**板消息上限按「追加后的整条」算**（完工那条已占掉一半额度），
审查结论撑破时用 `--replace` 把完工+审查合并压缩后整体重写，完工时间不动、两段都要保留。

## tracked 门禁脚本索引

> 权威用法与**已知盲区**以根 `AGENTS.md` 的「配套工具链」与「工具已知盲区速查」
> 两表为准；此处只作跨会话记忆的快速定位。`scripts/attic/` 是 gitignored 的
> 一次性脚本区，**不在门禁内**，不要引用其结论。

| 脚本 | 一句话职责 | 关键前提 / 盲区速记 |
|------|-----------|------------------|
| `verify_corpus.py` | **语料层验收**（P0-0）：件数对账 / 人物锚点双向 / 首末句抽印 / 转义符与页码 bleed | 在所有以 `text/` 为真值的门禁**之前**跑；不传 `--anchors` 则 ② 整项跳过 |
| `check_vocab.py` | 词汇表真实性 / 例句逐字 / 分档合理性 / 必备章节 / 空文件 | v3 起只扫 `## 词汇` 节；v4 起必备章节按「该书 ≥50% 文件都有」判定 |
| `verify_quotes.py` | 引语逐字（对 epub 全文）；`--full` 关闭 52 字符指纹盲区 | **必须有 `library/*.epub`**；「0 提取」按文件名四类分派 |
| `check_chapter_quotes.py` | 引语**逐章归属**（对 `text/`），防跨章搬句 | 不需 epub；P0-5 吞词检测**只报不判红**（md 吞词 / text 粘连无法分辨） |
| `verify_overview_quotes.py` | 总览三篇引语门禁（`verify_quotes` 不覆盖总览） | 概述行内英文引语不在口径内，须逐条人工 grep |
| `check_entities.py` | 梗概实体一致性（未知人名地名 = 情节虚构信号） | — |
| `check_crossref.py` | 分析层 `chNN "引语"` 跨章引用是否指对章 | **只认英文模式**，中文「第X章」写法不在口径 |
| `extract_chapters.py` | epub → 逐章 `text/` | dropcap 修连正则有已知误伤；提取后必跑 `verify_corpus` |
| `audit_book.py` | 一键总账（A 库存 / B 引文 / C 格式 / D 词汇实体） | **不含 crossref**（由 `check_crossref` 承担） |
| `corruption_scan.py` | **编辑损坏扫描**：U+FFFD / 双句号 / 占位崩坏 | **进提交门禁**——这类损坏对六道门禁全部不可见；中文重复片段**只报不判红**（约 50% 假阳） |
| `check_anchor.py` | 关键词锚定：关键词英文词须落在本块引语或分析正文 | 词全书查无 = ❌ FAIL；只在块外 = ⚠️ **不判红**（本库通行写法）；0 关键词行时**报「无法判定」**不算通过 |
| `sweep_analysis_inline.py` | 分析层行内英文逐字核查（反引号/双引号片段） | 七档按优先级；**B 类（语料缺）最先判**，**partial 必须排在 stem 之前**，frontmatter 必跳过 |
| `audit_numbers.py` | 计数断言核查（`N 个词` / `N 次` / `N 段`） | 只有「分隔线切为 N 段」与「N 次 token」有客观真值；「N 个词/分句/字符数」**一律列未判** |
| `audit_structure.py` | 结构扫描：子项齐备 / 编号连续 / 孤儿块 / 重复块 / 配额 | **按书内主流子项集自校准**，不套外部模板；`RE_ANY_LABEL` **必须 `re.M`**（否则子项检查空跑） |
| `check_short_quotes.py` | 短引语兜底（<20 flat 字符 `verify_quotes` 跳过的那批） | 复用 `verify_quotes` 口径；**跨标签拼接兜底不可省**（否则真引语被报成凭空造词） |
| `sweep_full.py` ⚠️ | 引语**整串** flat 比对（52 字符指纹盲区的克星） | **条件性工具**（需 epub，epub 将来会清理）；四档含**跨标签拼接 🔶**——flat 查无 ≠ 凭空造词 |
| `check_overview_full.py` ⚠️ | 总览三篇整串核查 + 章节标签对账 + H1 语义校验 | **条件性工具**；章节标签**只报不判红**（分不清「错标」与「有意引相关章」）；实现须与 `sweep_full` 同口径 |
| `check_overview_labels.py` | 总览 `（chNN）` 标注层核对：引语**逐字** + **章号归属**（`✅ 标注章逐字`／`⚠️ 标注与实章不符`／`❌ 全书查无`） | 补 `verify_overview_quotes.py`（不解析 `> ` 形态）与 `check_overview_full.py`（章节标签「只报不判红」）两个盲区；**只收带 `（chNN）` 的行**（裸引语归前者）；⚠️ **行首 `①` 必须在 flat 前剥掉**，NFKD 会把圈码归一成 `1` 留在指纹头部，**每条必然查无**；退出码 1 = 有 ⚠️/❌，**未接入 gate.sh**；另见 `check_overview_full.py` 行 |
| `vocab_candidates.py` | **生产工具**（非检测）：从 `text/` 打出可粘贴的三档表格行 | **写词表的默认入口**——它替代的动作是「凭印象写词条」；敢输出「本章 0 条高级」，**某档不足就留空，不许为凑满从记忆里补** |


> **本节即脚本表的唯一权威来源**（2026-09-27：原「## 工具链」节是本节的**严格子集**（8/22、无独有项），已删——两份清单记同一件事必然漂移）；完整用法与盲区见根 AGENTS「配套工具链」表与 `docs/实测档案/工具链实测.md`。

## 记忆归档分层（`.memory/` 下）

| 目录 | 放什么 | 谁写 |
|------|--------|------|
| `daily/` | 协作板配套的**当日工作日志**（`## <书名>` 一节一书） | 只走 `scripts/post_collab.py daily` |
| `raw-gates/` | 门禁的**原始逐行输出**存档（`<书 slug>/` 一目录） | 各次门禁跑完即落盘 |
| `metro-specs/` | metro 系列的规格 JSON | metro 流程 |
| `reviews/` | **独立五步审查的完整缺陷清单**（一审一文件 `YYYY-MM-DD-<书 slug>-五步审查.md`） | 第 10 条审查收尾时成文 |

> ⚠️ 审查清单**不要**放书目录——书目录的 `*.md` 会被 `gate.sh` lane ⑦/⑧ glob，
> 几千行带英文引语的 md 进去会污染逐章归属与块覆盖对账。
> ⚠️ 也不要用 `.tmp_spot/`：该目录已于 2026-10-01 删除并进 `.gitignore`；
> 规范承认的一次性脚本区是 `scripts/attic/`（本身 gitignored），能复用的正式工具提升到 `scripts/`。

## 重要记忆（按时间倒序）

### 2026-10-02 新增

- **Black Is the Body（Emily Bernard）非虚构随笔集**：13 章 + 总览三篇 = **16 md** + text/ 13 件（对账相符）。DSH-Mac 执行，15 commits 未 push（`31239fcd2`…`52b319f74`）。终值：verify_quotes --full **166/166 干净 15/15** · vocab **839 词条 FAIL0 WARN0** · entities 0 · corruption 0 · sweep_full 128/跨章 0 · 短引语 10 · 逐章归属 13×10/10 · 总览 **38/38** · audit_structure 0 · check_anchor 0 · gate.sh **EXIT=0**。
  - 结构：非虚构论述格式（概览 → 论证结构[核心论点/证据链/论证脉络/可质疑处] → 选择性精读 10 处五子项 → 词汇三档 → 一句话总结）。四条主题＝身体是处境 · 讲述不等于治愈 · 跨种族关系的不对称是常态 · 归家找不到终点。人物弧光六条（作者 / 母亲克拉拉·琼 / 外婆多西 / 曾外婆坦皮妈妈 / 两个女儿 / 父亲）。
  - **关键教训**：①**证据链表格第一格与第三格必须纯中文**（人名用中文音译 Karen→卡伦 / Loree→洛莉 / Estelle→埃丝黛尔）——`check_vocab` 会把任何「三列、第一格含 `[A-Za-z]{2,}`」的表格当词条形表格报 WARN，本书触发 3 次；②**短语词头必须用原书出现的词形**（`reeling off` / `butted heads`），词典原形（reel off / butt heads）会让 `sweep_analysis_inline` 复现 🟠；③中文计数词（"一个""第一个"）紧邻英文串会被 `audit_numbers` 当计数断言解析 → 删计数词或改"前者/后者"；④释义里禁夹无出处英文（写"巧劲、 inventive 的本领"→ 改纯中文）；⑤**大文件 write 后必须 `wc -c` 实测落盘**——ch09 首写时输出退化，工具回 "Created file" 但文件实际未落盘；⑥非虚构书**不给** `verify_corpus` 传 `--anchors`（小说人物消歧口径，报假红，见 2026-09-15 教训⑩）；⑦`check_overview_labels.py` 报"总览无（chNN）标注引语，跳过 N 行——不是通过"是口径而非缺陷（本书引语为裸 `> "…"` 格式）。
  - **gate.sh ⑱ `check_block_keywords` 的三条定性（工具口径备忘）**：`is_nonfic` 判据＝文件含 `^## 选择性精读`；配额非虚构 3–10（模板:1144 规定 10 处 ①-⑩）、言情 3–8。`KW_RE = r'^[ \t]*(?:[-*+][ \t]+)?\*\*关键词(?:\*\*：|：\*\*)[ \t]*(.*)$'` ⇒ **写成 `- **关键词**:`（冒号在 `**` 外）会漏计、报"关键词行 N ≠ 引语块 M"**（本书 ch06 真缺陷，改回 `**：` 即配平）。`not only... but also...` 一类**语法术语记法**被报"关键词不在本块引语内"属**假红**（模板:133 禁令 3 明列豁免），与 `sweep_analysis_inline` 全书固定那条 🔶拼接 1 同源。

### 2026-09-18 新增

- **She's a Doll（Barbara Truelove）死后成长推理长篇**：38 章精读（ch01 Content Warning + ch02–ch38 Chapter 1–37）+ 总览三篇（概述/金句精选25句/情感节点10节点）= **41 md** + text/ 41 件。Opencode-Mac 执行，独立五步审查通过。终值：verify **378/378（100%）** 干净 38/38 · vocab **331 词条 FAIL0 WARN0** · entities **0** · chapter **378/378 本章归属（零跨章）** · 8 条短引语人工 grep 命中。**关键教训**：①死后成长叙事（Posthumous Coming-of-Age）格式=精简格式（导航 5 项 + 四子项 + 三档词汇 + 一句话总结）；②verify_overview_quotes 对 00_*.md 报"未提取到编号引语"属工具盲区，须人工 grep 兜底；③概述/总览层事实错误（遗体描述/DNA归属/虚构引语）是 verify 全绿下的最大盲区，必须逐条回原文 grep 核实。**14 commits 未 push**。
  - 结构：幽灵叙述者（Lucy May McQuinn），死后第七天在破碎 doll 身体中苏醒，能控制时间（内部时间无限延长那几分钟）；复仇对象 Kyle Lawson（Krissy 的双胞胎哥哥）；Nicola 是唯一能看到 Lucy 的人；Ghost Lore Facts 系列（5 条）
  - 核心主题：死后成长（接受 ace lesbian 身份）· 有毒的女性友谊与救赎（Krissy 掩盖 Kyle 罪行）· 复仇的空虚与继续的意义（"you decide when you're ready to go, no one else"）

### 2026-09-16 新增

- **Strange Is the Light（Sarah Maria Griffin）文学思辨／科幻·恐怖长篇**：**25 md**（ch01–ch22 正文 + 00_概述 / 00_金句精选25句 / 00_情感节点10节点）+ text/ 22 件（1:1 零偏移）。DSH-Mac 执行，主会话五步审查修正 27 处后放行。终值：verify **203/203（100%）** 干净 23/23 · vocab **656 词条 FAIL0 WARN0** · entities **0** · chapter **178/178 in 本章 text** · overview 金句 **25/25** · crossref **0 对 0 报警** · 结构 **178 块 0 问题** · 总览全量英文片段 **47/47 MISS=0** · **分析层英文片段 867 条 MISSS=0** · 0 条短引语。**12 commits 未 push**（`a07ba702`…`7e34a8a5`）。
  - 结构：19 编号章 + 3 个 "Wonder Wonder" 插叙节（Ch.8a/10a/15a）+ 6 个无编号诗性插叙节 "Strange is the Light"（Ch.3/9/11/13/15/16，NCX 目录刻意隐去）；**ch01 与 ch21 是同一趟回岛**（Malachy 葬礼），ch02–ch20 为回溯；ch08 单章 12 万字符按用户指示单文件单独一批。
- **本批次关键教训（DSH-Mac）**：
  ① **新增终验标准件：分析层英文片段全量 flat sweep**——把非引语行的英文短语（≥3 词 ≥20 flat 字符）对 epub flat 比对：本书 867 条一次扫出 6 处非逐字/虚构短语（含 1 条完全凭空的 `this is not metaphorical for her`）。verify_quotes 只看引语行，分析层内联英文是纯盲区，成本极低（一个脚本扫完全书）。
  ② **数字断言必须当场数**——本次 5 处失准（「念过七次」实 8 次、「五个词的独立段落」实 6 词、「这三个词」×2 实 4 词、「this time 三个词」实 2 词、「三句递进陈述句」实 2 句）。凡写「N 个词 / N 次 / 唯一一次」都要回原文数。
  ③ **四子项顺序是成片发生的结构缺陷**——ch02/06/11/13/14/15/17/18/20/21/22 累计 60+ 块把「关键词」写在「为什么这样写」之后（批量生成时的注意力漂移）。对策=`scripts/attic/fix_strange_block_order.py` 行级修复（**禁 re.S**）+ 每章写完即跑自建结构扫描，别等收尾。
  ④ **总览层 blockquote 与概述行内短语是 verify_overview_quotes 的口径外**——`00_情感节点.md` 的 `> 引语` 与概述行内英文均不被抽取（工具对这两文件报「未提取到编号引语」）。自建 `verify_strange_overview.py` 做全量 flat 比对（47/47）兜底。
  ⑤ **同体裁双时空书的结构勘定**——NCX 目录可能刻意不给某些插叙节标签（本书 6 个 "Strange is the Light" 节无 label → 提取器 fallback 出 `ch03_chap3` 型文件名），须用精确 old→new 映射表重命名，并对齐「书内章号 vs 文件号」后写入导航。
  ⑥ **词汇分档注水检测靠人工**——check_vocab 只用 ~200 高频词表判 WARN，`elastic`/`metallic`/`realm`/`threshold` 等 B1/B2 常见词混入 ⭐⭐⭐ 全绿；本次降档 12 条（自建 `tier_demote_strange.py`）。

- **Pictures of You（Josh Malerman）恐怖/悬疑长篇**：40 章（ch01–ch40 = Chapter 1–40，1:1 零偏移）+ 总览三篇（概述/金句精选30句/情感节点10节点）= **43 md** + text/ 40 件。恐怖长篇精简格式（导航5项 + 编号引语块四子项 + 三档词汇 + 一句话总结）。Opencode-Mac 执行，独立五步审查**通过（0 遗留）**。终值：verify **356/356**（42/42 干净；10 短引语人工 grep 命中本章 text）/ vocab **872 词条 FAIL0 WARN0** / entities 0 / chapter **318/318 in 本章 text** / overview **58/58** / crossref 0 报警 / 结构 40/40 零异常 + **filename=H1=text 首行章号三方零偏移**。**19 commits 未 push**（`e602cf18`…`5dd7160f`）。
- **本批次关键教训**：
  ① **extract_chapters dropcap 修连正则误伤正文**——`\b([A-Z])\s+([A-Z][a-z]+|[A-Z]{2,})\b` 把 "A Wainscott"→"AWainscott"、"A TV"→"ATv"、"I HAVEN'T DECIDED"→"IHaven'TDecided"；无 dropcap 结构的 epub 用 `scripts/attic/extract_pictures_of_you_text.py`（复用 extract_chapters 逻辑、仅关该正则）重提，提取后 grep `\b[A-Z][A-Z][a-z][a-z]+\b` 自查。
  ② **check_crossref 只认 `chNN "引语"`，不管中文式「第 N 章」**——两轮共 **60 处**章号错引（语义二审 22 + 独立审查 18 确认，另 10 存疑）全在该盲区。逐章自检须额外 grep `第 [0-9]+ 章` 并对每条回查 text/chNN 原文。另有 **6 处"上一章/下一章"实指本章**（相对表述单独折算后再核）。
  ③ **说话人核验不能只看"窗口内是否有 she said"**——须看前后文施动关系（谁刚被扇、谁在 stare）。实证：情感节点 ⑫ `"You're no artist," she said.` 标为 Helen，实为 **Emily**（ch23 两记巴掌后 Emily 开口，紧接 The woman…only stared）；我自建的窗口检查器因只匹配标签而漏报，独立审查才抓出。
  ④ **check_vocab 不抓"抽词拼接式改写例句"**——ch16 rearview/mirror 例句脱漏原句的 "smiled and"，WARN 全绿；独立核验须对全部例句做"逐字 substring（含 … 分段）"扫描（872 条一轮可扫完）。
  ⑤ **audit_book.py C 节对精简格式全量误报**——`**中文理解：**`（冒号在粗体内）不被其正则识别，40/40 全报"五子项块数 0"；属 SOP 第 24 条豁免，勿误判缺陷。
  ⑥ **总览层细节不实**——概述把"拳头与肘砸开假墙"写成"掌刀割墙"（实为 ch19）、"咬刀爬回椅子"（ch30）写成"反手掷出飞镖"（无此事件）；总览叙事细节同样须回原文核（不只核引语）。

### 2026-09-14 新增

- **Asmodeus（Rita Indiana，Achy Obejas 译）文学小说（多米尼加）**：33 章（ch01–ch33，ch34 为 Graywolf Press 样板页已删除），精简格式（导航 5 项 + 3-6 处四子项精读 + 三档词汇 + 一句话总结），无总览三篇。ZCode-Mac 执行。独立五步审查通过。verify 178/182 (98%) / vocab 796 词条 FAIL=0 / entities 0 / check_chapter 178/182 (97%) / 结构 183 块零缺陷 / 关键词锚定 0 真违规。**4 条 MISS 全为多行诗歌工具盲区**（Icosiel 韵文 ch18/ch28、Manca 韵文 ch26），grep 确认存在。**关键教训**：①多行诗歌（Icosiel/Manca 韵文）verify_quotes/check_chapter_quotes 系统性 MISS——必须逐篇 grep 人工兜底；②精简格式词汇 FAIL 高频来自例句错章（例句来自 ch11 但词条在 ch22）；③"单词 A 类虚构"需先查 epub 全文——部分工具只查提取件。16 commits 未 push。

### 2026-09-11/12 新增

- **Everything Is Fine Here（Iryn Tushabe）当代成长小说（乌干达）**：18 章（ch01–ch18，无 Prologue/Epilogue），无总览三篇。**格式 = 精简格式（4 子项：中文理解/关键词/为什么这样写/读者视角提示）**——与 Favorite Daughter、Wild Dark Shore、Ligotti、How to Tell a True Story 同款。Opencode-Mac 执行。独立五步审查通过，发现并修复 5 处语义错位（verify 100/100 ✅ 全绿下漏网）：①ch06 原句5「男女同分」原文 Mama 自问自答（"The boy," Mama answered her own rhetorical question），Aine 真实回应是自贬的"Sorry I'm not as smart as Dr. Mbabazi Kamara"——分析误归为 Aine 的女权质问；②ch12 原句6「Petrichor」记住童年词汇的是老同学 Dan（"Petri who?" Paulo 当时反问），Paulo 系现学现用在吻别时归还——分析把两人合并为"一个游戏管理员"；③ch13 原句3「reset button」掌掴在 ch11 line 201 而非 ch09；④ch17 原句5「理想宣言」Elia 问 Aine（"问他"→"问她"）；⑤ch12 原句1「deviated septum」Paulo 点单宣言发生在派对当晚（早于夜谈），且为"替她点单"非"点酒"。终值：verify 100/100 ✅ / vocab 208 词条 FAIL=0 / entities 0 / check_chapter 105/105 ✅ / crossref 0 / 关键词锚定 0 违规 / 跨书污染 0。commits（未 push）：`c25c2a6e` ch01-03（首章试产）→ `6e663d98` ch04-06 → `d35d5c6b` ch07-09 → `79109e64` ch10-12 → `787fcee4` ch13-15 → `7c98608e` ch16-18 → `bdea0d27` 关键词锚定修复（ch05 brain scan/ch18 a new path → 引语逐字词）→ `aba55315` 完工公告 → `facbbba3` 五步审查修复 → `043cb41d` 审查修复公告。**本批次关键教训**：①精简格式审计 C 节五子项误报是 SOP 第 24 条豁免项，**勿误判缺陷**；②子代理委派语义审查必须附防幻觉条款（"报警前须先确认引语行与中文理解行真实存在于同一 md 文件且相邻"——避免拿 text/ 句子与无关分析行拼装错位）；③本批次关键词锚定检查器初版有 `**` 闭合符捕获 bug（误报 7 处假阳性），修正后真违规仅 2 处（脑扫描/路径未在引语中）；④fa<5 短引语（如 ch16 "Mama!"）工具完全跳过不计数，非结构缺陷——手动确认即可；⑤Episode 偏差根因：当分析层/总览层涉及多人物互动时（如"谁记住词""谁问话"），凭印象填充是 verify 全绿下的最大盲区，必须逐字回原文 grep + 说话人窗口核验（±200 字符）。

### 2026-09-10 新增

- **Don't Make Me Laugh（Julia Raeside）非虚构 #MeToo 幽默回忆录**：42 章（ch01-41 + Epilogue）+ 总览三篇（概述/金句精选28句/情感节点9节点）。**体裁提示：用户拍板用非虚构论述格式写小说**（与 it-comes-from-the-river 同类已知偏差，永久保留）。verify_quotes 388/388 ✅ / vocab 1058 词条 FAIL=0 WARN=0 / entities 0 / 逐章 388/388（100%）。**关键经验**：①论证结构证据链表格第三列含 ≥8 拉丁字符即被当例句判 FAIL（证据链单元格必须纯中文）；②总览候选句凭记忆 short-hand 多次 MISS（必须从已验证的章节文件原文复制）；③说话人窗口核验抓到 ch40 "I don't know" 命中 usher 台词；④生成期混入西里尔/越语/法语等珍稀语料（已全清）。16 commits 未 push。
- **Cabin Fever（Riley Parker）言情中篇 established couple**：7 章 + 概述一篇（含10 金句+7 节点+6 表达）。独立五步审查零缺陷。短篇结构，9 commits 未 push。
- **Burn for You（Bridie Charles）言情长篇 enemies-to-lovers**：43 章 + Epilogue + 总览三篇（概述/金句精选30句/情感节点10节点）。独立五步审查通过。
- **Adrift（Ellie Pond）言情长篇**：47 章 + 总览三篇。独立五步审查通过。文本/提取件零偏移。
- **How to Tell a True Story（Tricia Springstubb）middle-grade 当代小说**：58 章 + 总览三篇（概述/金句精选25句/情感节点10节点）。独立五步审查通过。LoC Cataloguing "LCGPT: Novels" 是体裁判断的权威信号。
- **Lady of The Lake（C.N. Crawford & Alex Rivers）奇幻言情**：61 章正文（ch02-ch62 = Chapter 1-61）+ 总览三篇。ch01=A Recap / ch63=Timeline / ch64=Sample 不精读。独立五步审查通过（22 commits 未 push）。总览引语跨叙述标签（如 "I understand why you lied," he says softly.）须逐字含标签文本，否则 flat 匹配失败。
- **Meet Me at Midnight（Brianna Bourne）YA contemporary romance + magical realism**：48 章（Chapter One → Chapter Forty-Eight）+ 总览三篇（概述/金句精选25句/情感节点12节点）。独立五步审查通过。
- **Pretty Bossy（Arini Vlotman）言情长篇 enemies-to-lovers + fake relationship**：22 章（ch01-ch22 = Chapter 1-21 + Epilogue）+ 总览三篇（概述/金句精选25句/情感节点10节点）。独立五步审查通过（11 commits 未 push）。**教训**：词汇表例句必须逐章 grep 验证，不可凭印象编写；总览引语格式（**关键引语：**）不在 verify_overview_quotes 口径内，须人工 grep 兜底。
- **The Bucket List（Ali Parker）言情长篇 contemporary romance**：43 章 + 总览三篇（Opencode-Mac 等多 IDE 接力）。25 commits 未 push。
- **The Sweet Chef and the Corporate Queen（Susanne Ash）言情长篇（age gap, forced proximity）**：13 章（ch01-ch12 + Epilogue）+ 总览三篇（概述/金句精选25句/情感节点9节点）。独立五步审查通过（9 commits 未 push）。**教训**：导航栏英文 trope 名称（Grumpy/Sunshine/Forced Proximity/Truth-Teller）须改中文，否则触发 check_entities 误报。
- **根目录 10 本新 epub 归档（260908 第二批）**：用户拍板"抽检内容后再分类"，按 OPF spine 取首章正文（混淆文件名 fallback 到扫 HTML 找 >800 字符非 boilerplate 页）。最终格局：**novels 61 / mystery-thriller 21 / non-fiction 18 / short-story-anthologies 20 = 120 本**。**关键判断**：①不要凭书名/作者印象分类；②Praise/营销文案含修辞夸张（Don't Make Me Laugh 标 "thriller" 是修辞非体裁）；③opus epub 用混淆文件名（c9.xhtml/cM.xhtml 等），须扫 HTML fallback。

### 2026-09-07 新增

- **The Wrong Sister（Claire Douglas）心理悬疑惊悚**：53 章（ch00 Prologue + ch01-51 + ch12b Interlude）+ 总览三篇（CommandCode-Mac）。独立五步审查放行。verify 272/274 ✅ / vocab 460 词条 FAIL=6（ch12b 工具盲区）/ entities 0 / 结构扫描 53/53。核心揭示：Bonnie=Holly（30 年前被绑架婴儿）/ Alice 是 chimera（嵌合体两套 DNA）/ Alice 杀害 Kyle（轮胎扳手）/ Tasha 选择沉默（"turning a blind eye"）。19 commits 未 push。
- **Falling into Place（Allison Ashley）言情长篇 contemporary romance**：34 章（Carly/Brooks 交替 + ch33 短信体 + ch34 Epilogue）+ 3 篇总览（Opencode-Mac）。独立五步审查两轮放行。verify 258/258 ✅ / vocab 732 词条 0/0 / entities 0 / overview 21/21。核心主题：稳定 vs 心动、说 vs 躲、翻篇 vs 传承。15 commits 未 push。
- **⚠️ Read 输出异物混入（本轮头号教训）**：ch23 Read 中段混入办公室/frames/centerfold/pizza 整段、ch33 Read 混入 ch31 pitch 段（franchise/Nashville/Riza），文件 grep 实测查无——Read 输出≠文件实况，凡写必先 grep，记忆与单次读取皆不可信。ch19 "bailed"/"fluke"亦为记忆漂移虚构。
- **verify fail-closed**：epub 路径拼错时报全 0/X——先查路径，不怀疑文件。
- **分析层数字断言**：年龄（三十三岁×4）、时长（九个月）、章数（九章/十九章）凡无原文支撑一律 soften/删除；推算的不写。
- **gag 计数链**：跨章"见下/下章见/over/哈哈"计数梗后期失控（三文件约 40 处），行级正则批量清理（禁 re.S 跨块）。

### 2026-09-06 新增

- **⚠️ 工具口径盲区速查（2026-09-05/06 十余本书交叉固化，详见 docs/新书启动模板.md 坑表新增节）**：
  1. verify_quotes/check_chapter_quotes 对无编号言情格式（`> "..."`）抽到 0/0——言情书须自备 flat 分段脚本
  2. <20 flat 字符短引语被工具静默跳过（Perfection/Forest of Scars/Rookie Season 三书互证）——grep 行数 vs 提取数不一致即信号
  3. check_vocab 撇号缩写词条（I've/he'd）误报 A类虚构；例句起点避开页码污染点；词条头必须本章原词形（torn≠tore）
  4. 跨标签拼接是 7 本书互证的最高频引语缺陷——多段台词严禁 `...` 连接
  5. verify_overview_quotes 只认行首圈数字且 CIRCLED 止于㉕——金句 ≤25 条/文件，其余人工脚本兜底
  6. 分析层 cross-ref 章号/数字断言/说话人是三道门禁的共同盲区——写前当场 grep 所指章
- **Up in Molten Lights（E.B. Golden）奇幻言情双 POV**：79 章 + 总览三篇（2026-09-06，ZCode-Mac）。流程=质量评估→修复不重做（尾部 ch49-54 词汇崩坏重写+引语 3 处）→续写 25 章 8 批→五步审查 12 处整改→词汇表全库清理（跨篇 59 处+移档+去重 68 行，FAIL=0 WARN=0）。终态引语 1006/1006（引号分段口径）。新工具盲区：check_vocab 撇号词条误报 A类、verify_quotes 对无编号言情格式抽不到、verify_overview 只认行首圈数字。约 35 commits 未 push。
- **The Last Thing（Bethany Monaco Smith）言情长篇 contemporary romance**：32 章（Chapter 1-31 + Epilogue），双 POV（Hallie/Deck 交替），逐章精读格式 + 3 篇总览。核心主题：命运 vs 选择、爱的勇气、家庭的多样性。Hallie 从"反爱情"到"说出我爱你"，Deck 从"控制狂"到"fun partner"。独立五步审查零缺陷。verify 355/355 ✅ / vocab FAIL=0 / entities 0。
- **No Take Backs（Taylor Wilson-West）逆后宫超自然言情**：29 章 + Epilogue，4 POV（Moraine/Soren/Rhea/Benny），逐章精读精简格式 + 3 篇总览。独立五步审查零缺陷。verify 219/219 ✅ / vocab FAIL=0 / entities 0。
- **Taken by Sinistre Ange（Sinistre Ange）言情长篇 erotic romance**：14 章 + 3 篇总览，含绑架/性支配/斯德哥尔摩综合征题材。独立五步审查修复 7 处缺陷。verify 133/133 ✅ / vocab FAIL=0 / entities 0。
- **Memories Like Fangs（Chelsey J. León）奇幻言情**：44 章 + 3 篇总览，双时间线（1960s/1990s），Rina/Emilio 跨种族恋爱。独立五步审查整改 27 处。verify 248/248 ✅ / vocab FAIL=0 / entities 0。

### 2026-09-05 新增
- **Wild Dark Shore（Charlotte McConaghy）言情长篇小说**：75 章（6 POV：Rowan/Fen/Dominic/Orly/Raff/Alex），逐章精读精简格式 + 3 篇总览。核心主题：爱与牺牲、家庭与血缘、自然与文明。Rowan 为寻夫来到 Shearwater 岛，融入 Salt 一家，最终为保护 Orly 淹死在竖井中。独立审查修复 31 个 FAIL + 5 处实体误判。verify 386/386 ✅ / vocab FAIL=0 / entities 0。
- **The Lack of Light（Nino Haratischwili）文学小说**：25 章，逐章精读精简格式 + 3 篇总览。四人友谊与创伤叙事（Dina/Keti/Ira/Nene），横跨第比利斯 1987 至布鲁塞尔 2019。独立审查修复 30 处词汇例句未命中 + ch09 重复引语块。verify 191/191 ✅ / vocab FAIL=0 / entities 0。
- **A Sea of Unspoken Things（Adrienne Young）推理悬疑奇幻**：32 章（含 ch18 "Twenty Years Ago" 闪回章节），逐章精读 + 3 篇总览。格式为推理/悬疑/奇幻精简格式（frontmatter + 本章导航 + 3-8 处精读 + 三档词汇 + 一句话总结）。独立审查发现并修复 5 处问题（ch01 编号、ch23 跨章错植、01_quotes 3 处 A 类虚构引语）。
- **Ten Bridges I've Burnt（Brontë Purnell）诗歌回忆录**：31 首自由诗，逐章精读 + 诗歌技法专项。格式按"随笔集逐篇精读"框架适配，新增"诗歌技法专项"章节分析跨行连续/括号自反/通感联觉/自造词等。
- **Addie LaRue 词汇精简**：ch098-108 词汇表从 ~1638 WARN 精简至 87 WARN（每章 25-30 词条）
- **Getaway Girl 双 POV**：Addison/Elijah 交替视角，需注意引语归属和人物弧线的对称性
- **Butcher of the Forest 场景节分章**：无章节号的中篇可按 `* * *` 场景分隔分章
- **文件命名修正**：Ten Bridges 初版用 `NN Title.md`（缺 ch 前缀），后统一重命名为 `chNN Title.md` 对齐其他书规范

### 2026-08-31 新增
- **Ligotti 第四次复查整改**（commit ba9b2e0）：
  - check_vocab全书词频口径盲区——A类虚构（如ch33 nullify/ch52占位符/ch73 night）在别章出现即通过check_vocab FAIL=0，但verify_quotes仍100%
  - check_chapter_quotes按flat文本匹配，省略号/标点差异导致误报（如ch22 PLACE引语"the diseased waters await his embrace"因无whose匹配失败）
  - 旧格式章节（①编号→`> **原句 N:**`）转换时缺冒号后空格导致引语提取失败
  - 49章旧格式转换后仍残留全部标为"原句1"（ch22/27/28/29）——圈数字映射bug
  - 详见 `docs/新书启动模板.md` 第9条规则说明

### 2026-08-30 新增
- **Barron's 批次 928 条 A 类虚构**：`check_vocab` 工具盲区——"（未出现在原文）"标注绕过工具检测，52篇全部存在。修复后 FAIL=0 ✅，WARN=72（B类）。详见 `docs/新书启动模板.md` 第5条。
- **check_vocab 标注盲区**：工具只检词频/例句前20字符/分档，不识别中文单元格。独立审查时必须 grep "（未出现在原文）"全文，有输出即 A 类虚构。

### 2026-08-29 新增
- **Room in the Ground 审查整改**：19 文件名偏移 + 5 跨章错植 + 7 cross-ref 联动修复 + 总览 8 处说话人反转。verify 235/235 ✅，FAIL=0。
- **AGENTS.md 第 10 条固化**：独立审查 SOP 五步法 + 完成报告硬要求 + 七类高发坑位。

### 历史教训
- Book Lovers 言情用逐句格式写到 35 篇崩坏重做
- 100 Great 两次大量生成后期衰减实证
- ~20 处"引语换新句、分析停旧句"在 verify_quotes 全绿下漏网
- NS 报告"101/101 ✅"重跑实为 108/109 含 1 FAIL
- 多 IDE 并行：git add -A 裹挟 / COLLABORATION.md 覆写 / amend 改写他实例 commit

## 推送策略

> ⚠️ **2026-09-30 起**：权威副本是根 `AGENTS.md` 顶部的 **「🚦 git 与推送红线」**节（2026-09-30 由原第 4 条前移，为的是落进任何实测注入预算之内）。以下三条是**索引级摘要**，冲突时以根 AGENTS 为准，**勿在此扩写**。

- commit 自由；push 仅限批次定稿/重大交付/明确指令
- **默认不推送，等用户指令统一 push**
- 多 IDE 并行时禁止 `git add -A` / `git add .`

- **You Were Never Not Mine（Monica Murphy）言情长篇**：57 章（ch01 Prologue + ch02-ch55 + ch56 Epilogue + ch57 Epilogue Part 2）+ 总览三篇（概述/情感节点10/金句26）= 60 md + text/ 57 件。Muse Spark 执行，22 commits 未 push。终值：verify 323/323 ✅ / vocab 507 词条 FAIL=0 / entities 2 误报 / check_chapter 311/311 ✅ / crossref 0 / 总览 45 引语全绿。**关键教训**：①短引语全量 sweep 自建法（flat<20 全提取 + grep 本章 text）抓 3 真缺陷（ch21 漏 n't 致反义、ch31/ch45 合并独立引语）——工具静默跳过 + 人工抽查都会漏，必须全量脚本化；②格式 retrofit 先例：37 文件三子项→四子项（补 254 行读者视角）由三子代理并行完成，附反例+防幻觉条款，语义零错位；③子代理备案须独立复核证据：B 批报 ch33 短句虚构实为其 grep 引号风格错（原文 line 89 实有），报警数字≠证据；④总览中文文件名不在 verify_overview_quotes 口径内（Fox 改 00 名，本书手工等效：长句指纹 0 MISS + 短句 9/9），命名是否统一待定；⑤多实例下 `git add` 只加明确路径（一次 -A 误收他书文件，reset 回退）。

### 2026-09-15 新增

- **工具链盲区固化**（topic: `tool-blinds-202609`）：verify_quotes 弯引号截断/不覆盖总览文件/跨块引语只取第一段；extract_chapters dropcap 正则制造虚构连字；check_vocab 撇号词条误报/概述层`|`分隔符误判；双绿≠语义干净（第 3 条门禁全绿仍有引语↔分析错位、说话人反转、cliffhanger跨章、总览层虚构）；整行sweep≥3次应列入终验标准件。**2026-10-01 Nexus 五步审查追加 ④ 条**：⑨分析层**语法级改字**（`that was` vs 原文 `that were`、`a extremely` vs `an`）是六道门禁共同盲区——投毒测试证明 sweep_analysis_inline/verify_quotes/check_vocab 三把主力尺子全漏，**仅 `check_analysis_indep` 可抓，建议其进常规门禁清单**（当前仅 d 步跑）；⑩`verify_corpus --anchors` 是**小说人物消歧**口径，非虚构论述书误用报 82 条假红，且 ①④ 不验章节归属须另用「逐章首行标题 vs epub 目录页」独立验；⑪子代理的**阻断型定性与行号都需复核**（23 条→实 19 条：2 假红+1 幻觉+2 升级+1 部分成立），⚠️有 Prologue 的书两套章号差 1，判跨章引用前先确认对方用哪套；⑫「引语截短」在脚本化生产下为 0（判据=中文理解里的英文词是否全在引语内 + 理解/引语字数比）。⚠️**另记一条审查期教训**：投毒测试的 `git checkout` 回滚**会把既存缺陷一起还原**——本轮 ch05:106（that was/were）即因此被误还原，**注入前必须先 `git diff` 确认工作树干净、并把备份与原文逐字比对**（Nexus 完整实例见 `docs/实测档案/N_Nexus五步审查_缺陷清单.md`）
- **子代理幻觉根因**（topic: `subagent-hallucination`）：根因=分析子项未锚定原文仅靠泛化指令生成；缓解=引语先行（每块附英文原句逐字粘贴）+ ≥20章自建关键词锚定检查器；实证=100G ch86引语与分析完全错位/NS 137块主会话逐对核对可补救
- **关键词锚定检查器**（topic: `keyword-anchor-checker`）：≥20章推荐；原理=分析块关键词英文词须命中该块引语或"为什么这样写"文本；Memories Like Fangs实战=237块扫出59+处违规（说明问题在大批次中普遍，需系统性扫描而非人工抽检）
