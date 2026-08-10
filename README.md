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
├── fetch_paris.py         ← 抓取 The Paris Review RSS
├── scan.py                ← 抓取后扫描题材/敏感度/字数，供筛选
└── feed_check.py / feed_check2.py   ← 探测 RSS 是否带全文
```

## 来源

主力：**The Paris Review**（`parisreview/`），RSS 自带完整正文，文学性强，精读价值最高。
备选（待启用）：Quanta Magazine（`quantamagazine/`）、Aeon（`aeon/`）——全文免费，科学/思想题材。
**避开**：The Atlantic / The New Yorker（付费墙，RSS 无正文）；政治敏感、涉法轮/宗教极端题材跳过。

- `parisreview/`（主力，RSS 带全文）：`<日期%Y-%m-%d_%A>/##_slug.txt`（原文）+ `##_slug_精读.md`（报告）+ `index.json`（索引）
- `economist/`（按期刊发行日期）：`260725/` 等；报告 `Title_snake_case.md`
- 待启用：`quantamagazine/`、`aeon/`
- 避开：The Atlantic / The New Yorker（付费墙，RSS 无全文）

## 每日工作流

1. **抓文**
   ```bash
   cd ~/Documents/Works/EnglishRead
   python3 fetch_paris.py
   ```
   自动建 `<source>/<今日日期_星期>/` 子目录，存当天 RSS 全文 + `index.json`。

2. **筛选**
   ```bash
   python3 scan.py
   ```
   打印每篇的题材、敏感度、字数，人工挑 3–5 篇（题材多样、安全、语言密度高）。

3. **精读**（交给 AI 助手）
   - 逐句：原句 / 自然中文 / 句子结构 / 关键词 / 地道表达 / "为什么这样写"
   - 段落逻辑分析；长难句专项（找主干→修饰→从句→恢复逻辑→整体理解）
   - 文末总结：核心词汇 / 表达 / 语法 / 长难句 / 写作技巧 / 可迁移表达
   - 报告存为 `<编号>_..._精读.md`，与原文同目录

4. **交互指令**：继续 / 详细解释这个句子 / 只讲语法 / 只讲词汇 / 测试我 / 不要翻译

## 精读核心原则

- 以理解英文原文为核心，**不做逐词翻译**。
- 用具体物件承载情感（show, don't tell），重视克制与留白。
- 重点放在长难句、易误解句、高级词汇、地道/学术表达、论证衔接词。
- 英文表达用简单英文解释英文时，用"不要翻译"指令。
- 报告要素：原句 / 自然中文 / 句子结构 / 关键词 / 地道表达 / "为什么这样写"；长难句专项：找主干→修饰→从句→恢复逻辑→整体理解。
- 交互指令：继续 / 详细解释这个句子 / 只讲语法 / 只讲词汇 / 测试我 / 不要翻译。

## 注意事项

- 本目录是**独立个人资产**，与 HermesAgent 工作区（`~/Sites/HermesAgent`）解耦，可单独备份/迁移。
- 加新来源：新建 `<source>/` 文件夹，写对应 `fetch_<source>.py`（逻辑同 fetch_paris.py，改 FEED + 解析）。
- `scan.py` 的 flags 字典需随来源扩充更新。
- 本文档为**唯一权威项目说明**；agent 操作规则见根 `AGENTS.md`，跨 IDE 拓扑与协作日志见 `.memory/AGENTS.md`。
- 本工作区在 macOS 26.5 上验证；跨机器同步用文件系统直读，git 仅在 MacBook 侧做版本记录。

## 今日（2026-08-10）已完成

parisreview/2026-08-10_Monday/ 下 5 篇精读：
- 02 Last Days at the Aqueduct（城市散文）
- 05 The Theater of Sport（Buford 访谈）
- 06 The Bit Player（家庭回忆，最催泪）
- 07 Interstitium（医学哲学，思辨最深）
- 10 In Paris, in Tokyo…（城市拼贴诗，最实验）
