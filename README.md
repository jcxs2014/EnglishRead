# EnglishRead — 英文精读库

中文母语者用 The Paris Review / The Atlantic / The New Yorker 等高品质文学/非虚构来源做**逐句英文精读**的个人知识库。
目标是"从看中文翻译过渡到直接读懂英文原文"。

> **本文件是「项目地图」**——目录、文档索引、部署、协作入口。
> **执行规则的权威是根 `AGENTS.md`**（规范源）。规则正文不在本文件重复：
> 本仓库已多次实证「两份清单记同一件事必然漂移」，重复处一律改为指针。

## 目录结构

```
~/Documents/Works/EnglishRead/
├── README.md                ← 本文件（项目地图）
├── AGENTS.md                ← 【规范源】执行规则（入 git，所有 IDE 共享）
├── COLLABORATION.md         ← 多 IDE 协作消息板（入 git，最新消息在**最前**）
├── .memory/                 ← 跨 IDE 共享记忆（入 git）
│   ├── AGENTS.md            ← 记忆索引：架构说明 / 核心规则文档 / 发板入口 / 脚本索引
│   └── daily/YYYY-MM-DD.md  ← 当日工作日志（入 git；板与日志均「每书一条」）
├── docs/                    ← 规则文档与实测档案（入 git）★ 见下方「文档地图」
│   ├── 新书启动模板.md        ← 书籍精读开工前必读（本库体量最大的执行文档）
│   ├── 期刊精读模板.md        ← 期刊精读前必读（与书籍侧是两档，勿串）
│   ├── 协作板更新指令.md      ← 发板 / 写日志（含一句话指令）
│   ├── 新书归档指令.md        ← epub 归档任务启动
│   ├── 实测档案/             ← 16 份案例档案（规则句留 AGENTS/模板，案例迁此处）
│   ├── 规则文档结构调整方案.md · 规则文档安全处置手册.md
│   └── COLLABORATION_ARCHIVE_*.md ← 板归档（只读历史，勿改）
├── notes/                   ← 所有精读内容（Quartz 内容源）
│   ├── index.md             ← Quartz 首页内容
│   ├── parisreview/ atlantic/ newyorker/ economist/
│   │   brainpickings/ lithub/ granta/          ← 七个期刊来源
│   │   └── <日期>/（Economist 用 YYMMDD，其余 yyyy-mm-dd）
│   │       ├── 标题.src.md   原文（gitignore：不入 git、不上站）
│   │       └── 标题.md       精读报告
│   └── books/               ← 整本书 / 短篇合集
│       ├── novels/ · mystery-thriller/ · non-fiction/ · short-story-anthologies/
│       └── <book-slug>/
│           ├── library/     ← epub（gitignore）
│           ├── text/        ← 逐章原文（gitignore；**用 `_`**：ch01_xxx.txt）
│           ├── ch01 xxx.md  ← 逐章精读（**用空格，禁 `_`**）
│           ├── 00_概述.md · 00_金句精选.md · 00_情感节点.md   ← 总览三篇（**用 `_`**）
│           └── （短篇合集豁免总览三篇；其余体裁完工必须齐三篇）
├── scripts/                 ← 工具脚本（45 个 .py + gate.sh，实际数以 ls 为准）
│   ├── gate.sh                ★ 一键跑本书全部门禁：bash scripts/gate.sh "<书目录>"
│   ├── verify_corpus.py       语料层验收（开工第 1 步，先于一切以 text/ 为真值的门禁）
│   ├── extract_chapters.py    epub → 逐章 text/
│   ├── verify_quotes.py       引语逐字（对 epub）· check_chapter_quotes.py 逐章归属
│   ├── check_vocab / check_entities / corruption_scan / sweep_full / audit_book …
│   ├── post_collab.py         发板 / 写日志（唯一入口，**勿手写抬头**）
│   ├── fetch_*.py             四个 RSS 源的抓文脚本（在 scripts/，不在来源目录）
│   └── attic/                 一次性脚本区（gitignore，**不在门禁内**）
├── site/                    ← Quartz 项目（配置入 git；public / node_modules 忽略）
├── build.sh                 ← CF 构建脚本（NODE_OPTIONS 调堆 + contentIndex 瘦身）
└── wrangler.jsonc           ← 部署配置
```

**关键点**
- Quartz 内容源统一为 `notes/`（`npx quartz build -d ../notes`）：期刊类 + 整本书精读库走同一目录
- 原文 `.src.md`（不入 git、不上站）；精读 `.md`（无后缀）
- **命名两侧不同，勿按文件名比对**：精读 md 用**单空格**（`ch01 rita meets lily.md`），
  `text/` 提取件与总览三篇用 **`_`**（`ch01_rita_meets_lily.txt`、`00_概述.md`）——
  一律**按章号映射**。全库曾因这条自相矛盾产生 94 本假红（详见 `AGENTS.md`「文件命名约定」）

## 文档地图（规则与编排在哪）

| 文档 | 何时读 | 定位 |
|---|---|---|
| `AGENTS.md`（根） | 每会话（自动注入，**但只注入开头一小段**） | **规范源**：执行规则唯一权威 |
| `.memory/AGENTS.md` | 查协作约定 / 脚本索引 / 历史记忆时 | 记忆索引（**规则正文不在此**） |
| `docs/新书启动模板.md` | **精读 `notes/books/` 任一本书之前** | 书籍侧执行编排（含本库不重复存放的展开内容） |
| `docs/期刊精读模板.md` | **精读 `notes/` 七源任一篇之前** | 期刊侧执行编排 |
| `docs/协作板更新指令.md` | 要发协作板 / 写工作日志时 | 板与日志的**唯一入口**（一句话指令 + 六步 + 六条硬约束） |
| `docs/新书归档指令.md` | 有新 epub 投到 `notes/books/` 根目录时 | 归档任务启动 |
| `docs/实测档案/`（16 份） | 查某条规则的实证案例时 | 案例层：**规则句留 AGENTS/模板，案例迁此处** |
| `docs/规则文档结构调整方案.md` · `docs/规则文档安全处置手册.md` | 要改规则文档本身时 | 重构方案与处置规程（锚点 / 分级 / 一键回滚） |
| `docs/COLLABORATION_ARCHIVE_*.md` | 极少 | 板归档，**只读历史，勿改** |

⚠️ **自动注入 ≠ 读到全文**：会话对 `AGENTS.md` 的注入只覆盖**开头一小段**，且**预算浮动**
（2026-09-30 三次实测 **4,882 / 7,995 / 8,009 字符**，同一份文件不同会话各不同）。
**第 2–10 条规则、git 与推送策略、会话交互指令、编辑纪律全在注入区外** ⇒ 必须**主动 Read**，
不能等它自己出现。git/push 红线已因此**前移到 `AGENTS.md` 文件顶部**。

## 两个 AGENTS.md 分工

| 文件 | 入 git | 定位 | 内容 |
|------|--------|------|------|
| 根 `AGENTS.md` | ✅ | **执行规则（规范源）** | 开工前必读触发 · 🚦 git 与推送红线 · 来源清单 · 会话流程 · 文件命名 · 日期规范 · 精读格式路由 · epub 归档 · 原文核验门禁 · 第 5–10 条（写作期防缺陷 / 引语修复同步 / 独立审查 SOP） |
| `.memory/AGENTS.md` | ✅ | **协作基础设施 + 记忆索引** | 架构说明 · 核心规则文档表 · 发板入口 · 门禁脚本索引 · 按时间倒序的重要记忆 |

**核心原则**：根 = agent 执行时的行为规则；`.memory` = 跨 IDE 协作的基础设施事实与历史记忆。
**不重复、不遗漏**——两边都不得各存一份规则正文。

## 来源

| 来源 | 目录 | RSS 全文 | 说明 |
|------|------|----------|------|
| **The Paris Review** | `notes/parisreview/` | ✅ | 主力来源，文学性最强 |
| **The Atlantic** | `notes/atlantic/` | ❌（付费墙） | 从思源笔记「摘录」笔记本提取 |
| **The New Yorker** | `notes/newyorker/` | ❌（付费墙） | 从思源笔记提取 |
| **The Economist** | `notes/economist/` | ❌ | 按期刊发行日期组织 |
| **Brain Pickings** | `notes/brainpickings/` | ✅ | 思想科学随笔 |
| **Literary Hub** | `notes/lithub/` | ✅ | 文学书评随笔 |
| **Granta** | `notes/granta/` | ✅ | 文学杂志 |

**避开**：政治敏感、涉法轮/宗教极端题材跳过。加新来源见文末「注意事项」。

## 每日工作流（期刊侧）

> **节奏**：以 UTC 日期为准，目录名用 UTC 日期。用户发出抓取需求 → 抓文 + 自动选 5 + 开精读，
> 一步到位，**不另找用户确认**。期刊侧的格式与门禁见 `docs/期刊精读模板.md`。

1. **抓文**（脚本自动，每源每日上限 **10 篇**）
   ```bash
   cd ~/Documents/Works/EnglishRead
   python3 scripts/fetch_paris.py    # 或 fetch_lithub / fetch_granta / fetch_brainpickings
   ```
   自动建 `notes/<source>/<今日日期_星期>/`，存当天 RSS 全文为 `<标题>.src.md`（≤10 篇），生成 `index.json`。
   **硬过滤**：正文 <500 字、纯汇总帖、当日已抓的重复 URL。

2. **自动选 5 篇**（AI 完成）
   - **长度适中**：约 800–3500 词
   - **题材多样**：避免 5 篇撞主题
   - **敏感剔除**：政治/宗教极端/暴力/领土争议/法轮相关 → 直接排除
   - **不可精读的题材**：涉及未成年人性剥削、大量直白性描写等 → 保留存档但不精读，
     在源文 `.src.md` 顶部加 `> ⚠️ 仅存档不精读` 说明
   - **语言密度**：长难句多、可读性高者优先
   - **宁少不凑**：剔除后凑不齐 5 篇就只精读能过的

3. **精读**（交给 AI 助手）
   - 逐句：原句 / 自然中文 / 句子结构 / 关键词 / 地道表达 / "为什么这样写"
   - 段落逻辑分析；长难句专项
   - 报告存为 `<标题>.md`，与原文同目录

4. **清理**
   - 当日**未入选且无精读**的源文 → 直接删除
   - **不可精读但已保留的存档篇**：在源文顶部加说明即可，无需删除

5. **交互指令**：继续 / 详细解释这个句子 / 只讲语法 / 只讲词汇 / 测试我 / 不要翻译

## 精读格式

格式正文**不在本文件**（避免第三份副本）：

- **期刊**（`notes/` 七源）→ `docs/期刊精读模板.md`
- **书籍 / 短篇合集**（`notes/books/`）→ `docs/新书启动模板.md`（含体裁对应格式表、逐章格式全文）
- 段落顺序、五子项、引用块规则的权威表述在 `AGENTS.md`「精读格式」节

**书籍门禁**：一次跑完用 `bash scripts/gate.sh "<书目录>"`（15 项汇总）；
单跑见 `AGENTS.md` 第 3 条（lane 判定 → 完整/降级两档，结论必须分三档：阻断型 / 提示型 / 假红型）。
期刊侧另有 `python3 scripts/sweep_journal.py`。

## 项目基础设施

### 网页部署
- Cloudflare Workers：https://englishread.jcxs2014.workers.dev/
- push 到 main 由 CF Git 集成自动构建；CF Build command = `bash build.sh`
  （`cd site && npm install --legacy-peer-deps` + `npx quartz build -d ../notes` +
  `NODE_OPTIONS=--max-old-space-size=6144` + contentIndex 去 content 字段瘦身）
- Quartz `ignorePatterns` 排除 `*.src.md`
- **push 会触发真金白银的构建** ⇒ 推送纪律见 `AGENTS.md`「🚦 git 与推送红线」节

### 记忆系统
| 层 | 文件 | 内容 | 变动频率 |
|---|---|---|---|
| 执行规则（规范源） | 根 `AGENTS.md` | 精读格式、命名、git 策略、门禁、审查 SOP | 低 |
| 协作基础设施 + 记忆索引 | `.memory/AGENTS.md` | 架构说明、脚本索引、发板入口、历史记忆 | 低 |
| 当日工作日志 | `.memory/daily/YYYY-MM-DD.md` | 当日工作、调试过程、决策（**入 git**） | 高 |
| 跨机消息板 | `COLLABORATION.md` | 跨机消息、完工/审查通报（**最新在最前**） | 事件触发 |
| 本机会话记忆 | `.workbuddy/memory/`（**gitignore**） | WorkBuddy 侧的当日审计/决策记录 | 高 |

### 两机 git 状态
- Mac mini：`.git` 为 0 字节空壳（文件同步软件忽略 `.git`）
- MacBook：有真仓库
- 两边 git 各自独立、互不干涉

### 当前字体栈（8/25 定稿）
- `--headerFont/--bodyFont` = `Lora, "Noto Serif SC"`；`--codeFont` = `IBM Plex Mono, system`

### 小屏横溢修复
- `site/quartz/styles/custom.scss` 给 `.nav-file-title` / `.page-title` / `.article-title`
  加 `overflow-wrap: anywhere; word-break: break-word`
- **Quartz 站点 / CSS / frontmatter 配置红线**见 `docs/实测档案/I_Quartz配置红线.md`（改站点时才读）

## 协作（发板 · 写日志 · 提交推送）

- **发协作板 / 写工作日志**：唯一入口 `docs/协作板更新指令.md`（内含**一句话指令**可直接复制）。
  一律走 `python3 scripts/post_collab.py`，**勿手写 `### [时间戳] [身份]` 抬头**；
  写完**必跑** `python3 scripts/check_collab_guard.py`（退出码 0 才算写成功）。
- **提交与推送**：`git add` 只加本任务明确路径（**禁止 `git add -A` / `git add .`**）；
  **push 必须获用户明确指令**。四条红线全文在 `AGENTS.md`「🚦 git 与推送红线」节。
- **多实例并行**：精读文件由指派的负责人修改；发现问题**只输出核对报告 + 留板**，不改他人文件。

## 注意事项

- 本目录是**独立个人资产**，与 HermesAgent 工作区（`~/Sites/HermesAgent`）解耦，可单独备份/迁移。
- 加新来源：在 `notes/<source>/` 放抓取产出，并在 `scripts/` 写对应 `fetch_<source>.py`（脚本与产出分开放）。
- **跨机同步**：两台机器各自维护 git 仓库，跨机只靠 git push/pull；
  `.src.md` 与 `library/` `text/` 不同步属预期（均 gitignore），**`.memory/` 与 `docs/` 是入 git 的，要同步**。
- 本工作区在 macOS 26.5 上验证。
