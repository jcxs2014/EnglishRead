# EnglishRead — 英文精读库

中文母语者用 The Paris Review 等高品质文学/非虚构来源做**逐句英文精读**的个人知识库。
目标是"从看中文翻译过渡到直接读懂英文原文"。

## 目录结构

```
~/Documents/Works/EnglishRead/
├── README.md              ← 本文件（唯一权威项目文档）
├── AGENTS.md              ← 本工作区 agent 操作手册（会话行为 / MiniMax 1027 详细流程）
├── .memory/               ← 跨 IDE 共享记忆（拓扑 + 协作日志，见 .memory/AGENTS.md）
├── <source>/              ← 一个来源一个文件夹（小写）
│   └── 2026-08-10_Monday/ ← 按抓取日期建子目录
│       ├── 01_xxx.txt          原文
│       ├── 01_xxx_精读.md       精读报告
│       └── index.json           当天文章索引（含标题/字数/预览）
├── parisreview/fetch_paris.py  ← 抓取 The Paris Review RSS
└── scan.py                      ← 抓取后扫描题材/敏感度/字数，供筛选
```

## 来源

主力：**The Paris Review**（`parisreview/`），RSS 自带完整正文，文学性强，精读价值最高。
新增（已启用）：**Granta**（`granta/`）、**Brain Pickings / The Marginalian**（`brainpickings/`）、**Literary Hub**（`lithub/`）——均 RSS 带全文，文学/思想/书评随笔，符合科技·科学·思想选材红线。
待验证：**Quanta Magazine**（`quantamagazine/`，部分带全文）、**Aeon**（`aeon/`，**实测 RSS 仅摘要、无全文**，需逐页抓）。
**避开**：The Atlantic / The New Yorker（付费墙，RSS 无正文）；政治敏感、涉法轮/宗教极端题材跳过。

- `parisreview/`（主力，RSS 带全文）：`<日期%Y-%m-%d_%A>/##_slug.txt`（原文）+ `##_slug_精读.md`（报告）+ `index.json`（索引）
- `granta/`（文学杂志，RSS 带全文）：脚本 `granta/fetch_granta.py`，产出同 `<日期_%A>/`
- `brainpickings/`（思想科学随笔，feed 重定向至 themarginalian.org，RSS 带全文）：脚本 `brainpickings/fetch_brainpickings.py`
- `lithub/`（文学书评随笔，RSS 带全文，脚本自动过滤 "Lit Hub Daily" 汇总帖）：脚本 `lithub/fetch_lithub.py`
- `economist/`（按期刊发行日期）：`260725/` 等；报告 `Title_snake_case.md`
- 待启用：`quantamagazine/`（部分全文）、`aeon/`（RSS 仅摘要，需逐页抓）
- 避开：The Atlantic / The New Yorker（付费墙，RSS 无全文）

## 每日工作流

> **节奏**：以 UTC 日期为准，目录名用 UTC 日期。用户发出抓取需求 → 抓文 + 自动选 5 + 开精读，一步到位，**不另找用户确认**。

1. **抓文**（脚本自动，每源每日上限 **10 篇**）
   ```bash
   cd ~/Documents/Works/EnglishRead
   python3 parisreview/fetch_paris.py   # 或 granta/fetch_granta.py 等（各源 fetch 脚本都在其源文件夹内）
   ```
   自动建 `<source>/<今日日期_星期>/`，存当天 RSS 全文（≤10 篇，按 `pubDate` 取最新），生成 `index.json`。**硬过滤（脚本层自动排除）**：正文 <500 字、纯汇总帖（如 Lit Hub Daily）、当日已抓的重复 URL。

2. **自动选 5 篇**（AI 完成，不另找用户确认）
   对 ≤10 篇候选自动挑 5，依据：
   - **长度适中**：约 800–3500 词
   - **题材多样**：避免 5 篇撞主题
   - **敏感剔除**：政治/宗教极端/暴力/领土争议/法轮相关 → 直接排除
   - **非 fiction**：granta 含小说，**长篇小说剔除**；**篇幅不长（≤18k 字符）的小说/虚构可保留**，但需逐篇通读判性质
   - **不可精读的题材**：涉及**未成年人性剥削**、**大量直白性描写（成人情色向）**等 → **保留存档但不精读**，在源文 `.md` 顶部（标题下）加一段 `> ⚠️ 仅存档不精读` 的简要说明（题材性质 + 为何不精读），仍不产出 `_精读.md`
   - **语言密度**：长难句多、可读性高者优先
   - **宁少不凑**：剔除后凑不齐 5 篇就只精读能过的，**不放宽阈值硬凑**
   - 产出 `selected.json`（记录的 5 篇 idx + 理由）

3. **精读**（交给 AI 助手）
   - 逐句：原句 / 自然中文 / 句子结构 / 关键词 / 地道表达 / "为什么这样写"
   - 段落逻辑分析；长难句专项（找主干→修饰→从句→恢复逻辑→整体理解）
   - 文末总结：核心词汇 / 表达 / 语法 / 长难句 / 写作技巧 / 可迁移表达
   - 报告存为 `<idx>_<slug>_精读.md`，与原文同目录

4. **清理（谨慎，本机无 git 不可逆）**
   - 当日**未入选且无精读**的源文 → 直接删除，保持目录整洁
   - **保留**：入选源文 + 精读 `_精读.md` + `index.json` + `selected.json` + 脚本
   - **不可精读但已保留的存档篇**：在源文顶部加说明即可，无需再删除（属"有标记保留"）
   - 清理动作在**单一机器**执行，避免跨机器同步竞态

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
- 加新来源：新建 `<source>/` 文件夹，写对应 `fetch_<source>.py`（逻辑同 parisreview/fetch_paris.py，改 FEED + 解析）。
- `scan.py` 的 flags 字典需随来源扩充更新。
- 本文档为**唯一权威项目说明**；agent 操作规则见根 `AGENTS.md`，跨 IDE 拓扑与协作日志见 `.memory/AGENTS.md`。
- 本工作区在 macOS 26.5 上验证；跨机器同步用文件系统直读，git 仅在 MacBook 侧做版本记录。
- **源文与精读均存 `.md`**：源文带 frontmatter（title/source/url/published/chars），命名 `<idx>_<slug>.md`；精读 `<idx>_<slug>_精读.md`。
- **抓取三边界（用户定）**：宁少不凑（敏感剔除后凑不齐 5 篇则少精读，不放宽阈值）；未入选源文直接删除（本机无 git，操作在单一机器执行防同步竞态）；备份用户自理，AI 不处理。
- **指定唯一抓取机**（建议）：`Opencode-Mac` 执行抓取脚本，避免两台机器同写一个目录引发同步竞态；Hermes-mini 负责精读。

## 今日（2026-08-10）已完成

parisreview/2026-08-10_Monday/ 下 5 篇精读：
- 02 Last Days at the Aqueduct（城市散文）
- 05 The Theater of Sport（Buford 访谈）
- 06 The Bit Player（家庭回忆，最催泪）
- 07 Interstitium（医学哲学，思辨最深）
- 10 In Paris, in Tokyo…（城市拼贴诗，最实验）
