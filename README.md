# EnglishRead — 英文精读库

中文母语者用 The Paris Review 等高品质文学/非虚构来源做**逐句英文精读**的个人知识库。
目标是"从看中文翻译过渡到直接读懂英文原文"。

## 目录结构

```
~/Documents/Works/EnglishRead/
├── README.md                ← 本文件（唯一权威项目文档）
├── AGENTS.md                ← 本工作区 agent 操作手册（会话行为 / MiniMax 1027 详细流程）
├── COLLABORATION.md         ← 多 IDE 协作消息板（入库，唯一跨机同步通道）
├── .memory/                 ← 本机工作记忆（不入 git，各机独立维护；跨机协调走 COLLABORATION.md）
├── index.md                 ← Quartz 首页内容
├── notes/                   ← 所有精读内容（来源 + 精读报告 + 索引 JSON）
│   ├── parisreview/
│   │   └── 2026-08-10_Monday/
│   │       ├── 01_xxx.src.md   原文（不入 git、不上网站）
│   │       ├── 01_xxx_精读.md  精读报告
│   │       └── index.json      当天文章索引
│   ├── brainpickings/  lithub/  granta/  economist/
│   └── books/                ← 小说/整本书精读库（epub/纯文本原文件不入 git，只跟精读笔记）
│       ├── a-most-angelic-death/
│       ├── books-that-saved-my-life/   ← 42 篇读书随笔，已完结
│       └── book-lovers/
├── scripts/                  ← 抓取与扫描脚本
│   ├── fetch_paris.py  fetch_brainpickings.py  fetch_lithub.py  fetch_granta.py
│   └── scan.py                  跨源扫描工具
├── site/                     ← Quartz 项目（配置入 git，public/node_modules 忽略）
│   ├── quartz.config.yaml  package.json  wrangler.jsonc  quartz/
│   └── public/                 构建产物（gitignore）
├── novels/                   ← 独立小说精读库（FORMAT + INDEX + library/ 入 gitignore）
├── build.sh                  ← CF 构建脚本：cd site && npm install + npx quartz build -d ../notes
└── wrangler.jsonc            ← 部署配置
```

**重构后关键点**（2026-08-22）：
- Quartz 内容源统一为 `notes/`（`npx quartz build -d ../notes`）：期刊类（Economist/Paris Review/Granta/Brain Pickings/LitHub）+ **整本书精读库（books/）** 全部走同一目录；**无软链、无 cp 循环、无 FreeFileSync 介入**。
- 原根目录的 `novels/` 已迁入 `notes/books/`（2026-08-23），epub/纯文本原文件仍不入 git，只跟精读笔记。
- 根目录的来源目录（parisreview/brainpickings/lithub/granta/economist）已全部迁入 `notes/` 下；外部引用 URL 结构不变。

## 来源

主力：**The Paris Review**（`parisreview/`），RSS 自带完整正文，文学性强，精读价值最高。
新增（已启用）：**Granta**（`granta/`）、**Brain Pickings / The Marginalian**（`brainpickings/`）、**Literary Hub**（`lithub/`）——均 RSS 带全文，文学/思想/书评随笔，符合科技·科学·思想选材红线。
待验证：**Quanta Magazine**（`quantamagazine/`，部分带全文）、**Aeon**（`aeon/`，**实测 RSS 仅摘要、无全文**，需逐页抓）。
**避开**：The Atlantic / The New Yorker（付费墙，RSS 无正文）；政治敏感、涉法轮/宗教极端题材跳过。

- `notes/parisreview/`（主力，RSS 带全文）：`<日期%Y-%m-%d_%A>/##_slug.src.md`（原文）+ `##_slug_精读.md`（报告）+ `index.json`（索引）
- `notes/granta/`（文学杂志，RSS 带全文）：脚本 `scripts/fetch_granta.py`，产出同 `<日期_%A>/`
- `notes/brainpickings/`（思想科学随笔，feed 重定向至 themarginalian.org，RSS 带全文）：脚本 `scripts/fetch_brainpickings.py`
- `notes/lithub/`（文学书评随笔，RSS 带全文，脚本自动过滤 "Lit Hub Daily" 汇总帖）：脚本 `scripts/fetch_lithub.py`
- `notes/economist/`（按期刊发行日期）：`260725/` 等；**原文** `Title_snake_case.src.md`（260822 起，不入 git、不上网站）；**精读** `Title_snake_case_精读.md`。历史说明：260606–260815 批次精读文件名无 `_精读` 后缀（`X.md` 即精读），保持原样
- 待启用：`notes/quantamagazine/`（部分全文）、`notes/aeon/`（RSS 仅摘要，需逐页抓）
- 避开：The Atlantic / The New Yorker（付费墙，RSS 无全文）

## 每日工作流

> **节奏**：以 UTC 日期为准，目录名用 UTC 日期。用户发出抓取需求 → 抓文 + 自动选 5 + 开精读，一步到位，**不另找用户确认**。

1. **抓文**（脚本自动，每源每日上限 **10 篇**）
   ```bash
   cd ~/Documents/Works/EnglishRead
   python3 scripts/fetch_paris.py   # 或 scripts/fetch_granta.py 等（所有 fetch 脚本在 scripts/ 下）
   ```
   自动建 `notes/<source>/<今日日期_星期>/`，存当天 RSS 全文为 `##_slug.src.md`（≤10 篇，按 `pubDate` 取最新），生成 `index.json`。**硬过滤（脚本层自动排除）**：正文 <500 字、纯汇总帖（如 Lit Hub Daily）、当日已抓的重复 URL。

2. **自动选 5 篇**（AI 完成，不另找用户确认）
   对 ≤10 篇候选自动挑 5，依据：
   - **长度适中**：约 800–3500 词
   - **题材多样**：避免 5 篇撞主题
   - **敏感剔除**：政治/宗教极端/暴力/领土争议/法轮相关 → 直接排除
   - **非 fiction**：granta 含小说，**长篇小说剔除**；**篇幅不长（≤18k 字符）的小说/虚构可保留**，但需逐篇通读判性质
   - **不可精读的题材**：涉及**未成年人性剥削**、**大量直白性描写（成人情色向）**等 → **保留存档但不精读**，在源文 `.src.md` 顶部（标题下）加一段 `> ⚠️ 仅存档不精读` 的简要说明（题材性质 + 为何不精读），仍不产出 `_精读.md`
   - **语言密度**：长难句多、可读性高者优先
   - **宁少不凑**：剔除后凑不齐 5 篇就只精读能过的，**不放宽阈值硬凑**
   - 产出 `selected.json`（记录的 5 篇 idx + 理由）

3. **精读**（交给 AI 助手）
   - 逐句：原句 / 自然中文 / 句子结构 / 关键词 / 地道表达 / "为什么这样写"
   - 段落逻辑分析；长难句专项（找主干→修饰→从句→恢复逻辑→整体理解）
   - 文末总结：核心词汇 / 表达 / 语法 / 长难句 / 写作技巧 / 可迁移表达
   - 报告存为 `<idx>_<slug>_精读.md`，与原文同目录

4. **清理**
   - 当日**未入选且无精读**的源文 → 直接删除，保持目录整洁
   - **保留**：入选源文 + 精读 `_精读.md` + `index.json` + `selected.json` + 脚本
   - **不可精读但已保留的存档篇**：在源文顶部加说明即可，无需再删除（属"有标记保留"）

5. **交互指令**：继续 / 详细解释这个句子 / 只讲语法 / 只讲词汇 / 测试我 / 不要翻译

## 精读核心原则

- 以理解英文原文为核心，**不做逐词翻译**。
- 用具体物件承载情感（show, don't tell），重视克制与留白。
- 重点放在长难句、易误解句、高级词汇、地道/学术表达、论证衔接词。
- 英文表达用简单英文解释英文时，用"不要翻译"指令。
- 报告要素：原句 / 自然中文 / 句子结构 / 关键词 / 地道表达 / "为什么这样写"；长难句专项：找主干→修饰→从句→恢复逻辑→整体理解。
- 交互指令：继续 / 详细解释这个句子 / 只讲语法 / 只讲词汇 / 测试我 / 不要翻译。

## 注意事项

- 本目录是**独立个人资产**，与 HermesAgent 工作区（`~/Sites/HermesAgent`）解耦，可单独备份/迁移。
- 加新来源：在 `notes/<source>/` 文件夹下放抓取产出，在 `scripts/` 写对应 `fetch_<source>.py`（逻辑同 `scripts/fetch_paris.py`，改 FEED + 解析；脚本 BASE 已指向 `notes/<source>/`，CWD 无影响）。
- `scripts/scan.py` 的 flags 字典需随来源扩充更新；路径已迁移至 `notes/` 下。
- 本文档为**唯一权威项目说明**；agent 操作规则见根 `AGENTS.md`，本机工作记忆见 `.memory/AGENTS.md`（各机独立，不入 git）。
- **跨机同步**：两台机器各自维护 git 仓库（origin = `github.com:jcxs2014/EnglishRead`），Syncthing 已排除本目录；跨机只靠 git push/pull，`.src.md` 与 `.memory/` 不同步属预期。
- 本工作区在 macOS 26.5 上验证。
- **源文与精读命名**：所有源目录位于 `notes/` 下。源文 `<idx>_<slug>.src.md`（不入 git、不上网站）；精读 `<idx>_<slug>_精读.md`。Economist 命名规则与历史断层见上方来源节。
- **网页部署**：Cloudflare Workers（https://englishread.jcxs2014.workers.dev/），push 到 main 由 CF Git 集成自动构建。CF Dashboard Build command = `bash build.sh`（运行根 `build.sh`：cd site && npm install --legacy-peer-deps + npx quartz build -d ../notes）；Quartz `ignorePatterns` 排除 `*.src.md`，原文不上网。
- **抓取三边界（用户定）**：宁少不凑（敏感剔除后凑不齐 5 篇则少精读，不放宽阈值）；未入选源文直接删除；备份用户自理，AI 不处理。
- **git 提交纪律**：精读批次进行中只 commit 不 push；定稿或用户指令后统一推送（详见 AGENTS.md）。
