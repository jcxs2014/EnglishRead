# EnglishRead — 英文精读库

中文母语者用 The Paris Review / The Atlantic / The New Yorker 等高品质文学/非虚构来源做**逐句英文精读**的个人知识库。
目标是"从看中文翻译过渡到直接读懂英文原文"。

## 目录结构

```
~/Documents/Works/EnglishRead/
├── README.md                ← 本文件（唯一权威项目文档）
├── AGENTS.md                ← 本工作区 agent 操作手册（会话行为 / MiniMax 1027 详细流程）
├── COLLABORATION.md         ← 多 IDE 协作消息板（入库，唯一跨机同步通道）
├── .memory/                 ← 本机工作记忆（不入 git，各机独立维护）
│   ├── AGENTS.md            ← 项目级低频规则
│   └── daily/               ← 当日工作日志
├── index.md                 ← Quartz 首页内容
├── notes/                   ← 所有精读内容（来源 + 精读报告）
│   ├── parisreview/         ← The Paris Review（RSS 带全文）
│   │   └── 2026-08-10 Monday/
│   │       ├── 01 xxx.src.md   原文（不入 git、不上网站）
│   │       └── 01 xxx.md       精读报告
│   ├── atlantic/            ← The Atlantic
│   │   └── 2026-08-25/
│   │       ├── logging in.md   原文（.src.md 格式）
│   │       └── logging in.md   精读报告
│   ├── newyorker/           ← The New Yorker
│   ├── economist/           ← The Economist（按期刊发行日期）
│   │   └── 260822/
│   │       ├── Title.src.md    原文（260822 起，不入 git）
│   │       └── Title.md        精读报告
│   ├── brainpickings/       ← Brain Pickings / The Marginalian
│   ├── lithub/              ← Literary Hub
│   ├── granta/              ← Granta
│   └── books/               ← 整本书/小说精读库
│       ├── a-most-angelic-death/
│       ├── books-that-saved-my-life/   ← 40 篇读书随笔
│       └── if-we-cannot-go-at-the-speed-of-light/
├── scripts/                 ← 抓取与扫描脚本（仅跨源工具）
│   └── scan.py              跨源扫描工具
├── site/                    ← Quartz 项目（配置入 git，public/node_modules 忽略）
│   ├── quartz.config.yaml   package.json  wrangler.jsonc
│   └── public/              构建产物（gitignore）
├── build.sh                 ← CF 构建脚本
└── wrangler.jsonc           ← 部署配置
```

**关键点**：
- Quartz 内容源统一为 `notes/`（`npx quartz build -d ../notes`）：期刊类 + 整本书精读库全部走同一目录
- 原文 `.src.md`（不入 git、不上网站）；精读 `.md`（无后缀）
- `.memory/` 是本机工作记忆（不入 git）；跨机协调走 `COLLABORATION.md`

## 来源

| 来源 | 目录 | RSS 全文 | 说明 |
|------|------|----------|------|
| **The Paris Review** | `parisreview/` | ✅ | 主力来源，文学性最强 |
| **The Atlantic** | `atlantic/` | ❌（付费墙） | 从思源笔记「摘录」笔记本提取 |
| **The New Yorker** | `newyorker/` | ❌（付费墙） | 从思源笔记提取 |
| **The Economist** | `economist/` | ❌ | 按期刊发行日期组织 |
| **Brain Pickings** | `brainpickings/` | ✅ | 思想科学随笔 |
| **Literary Hub** | `lithub/` | ✅ | 文学书评随笔 |
| **Granta** | `granta/` | ✅ | 文学杂志 |

**避开**：政治敏感、涉法轮/宗教极端题材跳过。

## 文件命名规范

### 核心约定（2026-08-25 定稿）
- **唯一分隔符 = 单空格**（禁止 `_` `-` `'` 等特殊字符）
- 原文 = `<标题>.src.md`（gitignore，不入 git）
- 精读 = `<标题>.md`（无后缀）
- Quartz URL slug 由 frontmatter title 生成（不受文件名影响）

### 日期文件夹规范
- Economist：`YYMMDD/`（如 `260822/`）
- Atlantic/其他：`<yyyy-mm-dd>/`（如 `2026-08-25/`）
- 同一目录两种风格按来源区分

### 章节书籍命名
- `ch<NN>_<keyplot>.md`（如 `ch01 rita meets lily.md`）
- 有编号的文档：`01-XX.md`（如 `01-success-of-a-mission.md`）
- 章节书籍/编号文档 frontmatter 必须加 `modified:"YYYY-MM-DD"`（首 commit 日期）

### 脚本位置
- 各源 fetch 脚本收纳于其源文件夹（如 `notes/parisreview/fetch_paris.py`）
- `scan.py` 跨源通用留根目录
- `setup_obsidian.sh` 在工作区根目录

## 每日工作流

> **节奏**：以 UTC 日期为准，目录名用 UTC 日期。用户发出抓取需求 → 抓文 + 自动选 5 + 开精读，一步到位，**不另找用户确认**。

1. **抓文**（脚本自动，每源每日上限 **10 篇**）
   ```bash
   cd ~/Documents/Works/EnglishRead
   python3 notes/parisreview/fetch_paris.py  # 或对应源文件夹的 fetch 脚本
   ```
   自动建 `notes/<source>/<今日日期_星期>/`，存当天 RSS 全文为 `<标题>.src.md`（≤10 篇），生成 `index.json`。**硬过滤**：正文 <500 字、纯汇总帖、当日已抓的重复 URL。

2. **自动选 5 篇**（AI 完成）
   - **长度适中**：约 800–3500 词
   - **题材多样**：避免 5 篇撞主题
   - **敏感剔除**：政治/宗教极端/暴力/领土争议/法轮相关 → 直接排除
   - **不可精读的题材**：涉及未成年人性剥削、大量直白性描写等 → 保留存档但不精读，在源文 `.src.md` 顶部加 `> ⚠️ 仅存档不精读` 说明
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

### 期刊文章逐句精读格式
- frontmatter：`---` / `状态: 未读` / `---`
- 章节顺序：`## 概览` → `## 逐句精读` → `## 段落逻辑` → `## 词汇分级` → `## 长难句专项` → `## 精读结束总结` → `## 可迁移表达`
- 每个原文段落一个 `### 第 N 段：主题概括`；段内每个原句一个 `> **原句 M:**` 分析块
- 分析块含**五子项**：中文理解 / 句子结构 / 关键词 / 表达方式 / 为什么这样写（项间需空行分隔）
- 原句编号 M 全文连续不重置，禁止多句合并
- 引用块 `>` 只含原句英文，中文解读在引用块外，引用块与解读间留空行
- 段落末尾 `**段落逻辑：**` 用 → 箭头串起逻辑链

### 词汇分级
- `## 词汇分级` 下分三档 `### ⭐⭐⭐ 高级` / `### ⭐⭐ 进阶` / `### ⭐ 基础`
- 每档一张 3 列表格（词/短语 | 释义 | 例句）

### 小说精读格式（三档体裁对应）
- **言情/情感小说**：3 篇（概述 + 金句精选 + 情感节点），不逐句
- **推理/悬疑/奇幻小说**：逐章精读（精简格式），每引语块 ≤4 行
- **随笔集/书评集**：逐篇精读（每篇 1 H1 + 4 H2）

## Quartz 配置红线

- **typography**：css2 的 `family=` 参数永远**单一字体名**，组合栈放 `custom.scss` 的 `:root` 变量
- **排序**：章节书籍/编号文档 frontmatter 必须加 `modified:"YYYY-MM-DD"`（首 commit 日期），使 alphabetical 正序
- **前端定制**：不模拟原生行为，变量层组合字体，砍无引用装饰系统
- **YAML 炸弹**：frontmatter title 含 `: `（冒号空格）或斜杠时需加引号

## 项目基础设施

### 网页部署
- Cloudflare Workers（https://englishread.jcxs2014.workers.dev/）
- push 到 main 由 CF Git 集成自动构建
- CF Build command = `bash build.sh`（cd site && npm install --legacy-peer-deps + npx quartz build -d ../notes）
- Quartz `ignorePatterns` 排除 `*.src.md`

### 记忆系统（三层分工）

| 层 | 文件 | 内容 | 变动频率 |
|---|---|---|---|
| 项目级 | `.memory/AGENTS.md` | 协作协议、格式规则、配置约定 | 低 |
| 当日 | `.memory/daily/YYYY-MM-DD.md` | 当日工作日志 | 高 |
| 消息板 | `COLLABORATION.md` | 跨机消息、重要状态 | 事件触发 |

### 两机 git 状态
- Mac mini：`.git` 为 0 字节空壳（文件同步软件忽略 `.git`）
- MacBook：有真仓库
- 两边 git 各自独立、互不干涉

### 推送节奏（规则 #1784）
- commit 自由
- push 仅限批次定稿/重大交付/明确指令
- 本地 commit 累积，不触发 CF 构建

### 当前字体栈（8/25 定稿）
- `--headerFont/--bodyFont` = `Lora, "Noto Serif SC"`
- `--codeFont` = `IBM Plex Mono, system`

### 小屏横溢修复
- `site/quartz/styles/custom.scss` 给 `.nav-file-title` / `.page-title` / `.article-title` 加 `overflow-wrap: anywhere; word-break: break-word`

## 注意事项

- 本目录是**独立个人资产**，与 HermesAgent 工作区（`~/Sites/HermesAgent`）解耦，可单独备份/迁移。
- 加新来源：在 `notes/<source>/` 文件夹下放抓取产出，写对应 `fetch_<source>.py`
- 本文档为**唯一权威项目说明**；agent 操作规则见根 `AGENTS.md`，本机工作记忆见 `.memory/AGENTS.md`
- **跨机同步**：两台机器各自维护 git 仓库，跨机只靠 git push/pull，`.src.md` 与 `.memory/` 不同步属预期
- 本工作区在 macOS 26.5 上验证
