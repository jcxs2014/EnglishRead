# EnglishRead 跨 IDE 共享记忆

> 注意：本文档为跨 IDE 共享记忆，**只存项目级低频规则**，操作规则见根 `AGENTS.md`，项目说明见 `README.md`。
>
> **当日工作日志 → `.memory/daily/YYYY-MM-DD.md`（高频追加，不覆盖）**
> **跨机消息 → `COLLABORATION.md`（事件触发，不变进度日志）**
>
> 三层分工详情见 `COLLABORATION.md` 顶部。

## 是什么
中文母语者的英文**逐句精读**知识库。目标：从"看中文翻译"过渡到"直接读懂英文原文"。

## 期刊文章精读格式（Economist/Atlantic/New Yorker 等）

### 逐句精读格式
- frontmatter：`---` / `状态: 未读` / `---`
- 章节：`# 标题（精读分析）` → `## 概览` → `## 逐句精读` → `## 段落逻辑` → `## 词汇分级` → `## 长难句专项` → `## 精读结束总结` → `## 可迁移表达`
- 逐句：每个原文段落一个 `### 第 N 段：主题概括`；段内每个原句一个 `> **原句 M:**` 分析块
- 分析块含**五子项**：中文理解 / 句子结构 / 关键词 / 表达方式 / 为什么这样写（项间需空行分隔）
- 原句编号 M 全文连续不重置，禁止多句合并成一个分析块
- 引用块 `>` 只含原句英文，中文解读在引用块外，引用块与解读间留空行
- 段落末尾 `**段落逻辑：**` 用 → 箭头串起该段逻辑链

### 词汇分级
- `## 词汇分级` 下分三档 `### ⭐⭐⭐ 高级` / `### ⭐⭐ 进阶` / `### ⭐ 基础`
- 每档一张 3 列表格（词/短语 | 释义 | 例句）

### 格式关键约束
- 每原句一个分析块（34 句 → 34 块），禁止合并
- 五子项之间需空行分隔（引用块与解读间留空行）
- 结尾无 ■ 标记

## 文件命名与存储

### 文件命名约定
- 原文 = `<标题>.src.md`（gitignore，不入 git）
- 精读 = `<标题>.md`（无后缀）
- **唯一分隔符 = 单空格**（禁止 `_` `-` `'` 等特殊字符）
- 章节书籍：`ch<NN>_<keyplot>.md`（如 `ch01 ritameetslily.md`）
- 有编号的文档：`01-XX.md`（如 `01-success-of-a-mission.md`）

### 日期文件夹规范
- Economist：`YYMMDD/`（如 `260822/`）
- Atlantic/其他：`<yyyy-mm-dd>/`（如 `2026-08-25/`）
- 同一目录两种风格按来源区分

### 精读/存储规则
- 每源每日 ≤10 篇，自动选 5 篇，宁少不凑
- 源文+精读均 `.md` + frontmatter
- 不可精读题材保留存档并加说明
- 未选源文当日清理
- 不可精读题材保留存档并加说明；未选源文当日清理

### 脚本布局
- 各源 fetch 脚本收纳于其源文件夹
- `scan.py` 跨源通用留根目录
- `setup_obsidian.sh` 在工作区根目录

## Quartz 配置红线

### 排序规则
- 章节书籍（chXX / 01-XX 命名）+ 有编号的文档，frontmatter 必须加 `modified:"YYYY-MM-DD"`（首 commit 日期）
- 使 created-modified-date 插件读 frontmatter，所有章节同日期 → alphabetical 正序
- 双套独立排序：Explorer（侧边栏）按 displayName localeCompare；PageList（文件夹页）按 modified date desc → alphabetical fallback

### typography 规则
- **css2 的 `family=` 参数永远单一字体名**，组合栈放 `custom.scss` 的 `:root` 变量
- 如 `quartz.config.yaml` typography.body 写成 CSS 栈 `"Lora, Noto Serif SC"` 会导致 Google Fonts 400

### 前端定制哲学
- 不模拟原生行为，变量层组合字体，砍无引用装饰系统
- 给 Quartz 加行为前先读插件 dist 确认原生是否覆盖
- 每个 CSS 自定义规则都针对真实 class 名，发明的新类名不会生效

### YAML 炸弹模式
- frontmatter title 含 `: `（冒号空格）或斜杠 `/` 时需加引号，否则 Quartz 解析失败
- 预防规则：所有 frontmatter 值含 `: ` / `,` / `?` / `"` / `'` 都应加引号

## 项目基础设施

### 两机 git 状态
- Mac mini：`.git` 为 0 字节空壳（文件同步软件忽略 `.git`，避免损坏）
- MacBook：有真仓库（commit `a5e82f9` / `a7a1771`）
- **最终决策**：两边 git 各自独立、互不干涉

### `.memory/` 自身状态
- 已从 git 追踪缓存移除（commit 36f771a），gitignore 规则保留
- 本机工作记忆，不提交、不同步、不删除
- 跨机协调一律走 `COLLABORATION.md`

### 推送节奏（规则 #1784）
- commit 自由
- push 仅限批次定稿/重大交付/明确指令
- 本地 commit 累积，不触发 CF 构建

### 当前字体栈（8/25 定稿）
- `--headerFont/--bodyFont` = `Lora, "Noto Serif SC"`
- `--codeFont` = `IBM Plex Mono, system`
- Noto Sans SC 引用清零

### 小屏横溢修复
- `site/quartz/styles/custom.scss` 给 `.nav-file-title` / `.page-title` / `.article-title` / `.folder-button` 加 `overflow-wrap: anywhere; word-break: break-word`

## 累计数据
- **截至 260826**：累计 **184 篇**精读
- **Economist 已读期**：260606–260801 + 260627 + 260808 + 260815 + 260822
- **Atlantic 已读期**：2026-08-25（首批）

## 协作约定（跨 IDE）
- 同一目录多 IDE 共享文件系统，写入即同步，**无需 git pull/push**
- 时间戳一律 **UTC**（`date -u '+%Y-%m-%d %H:%M UTC'`）
- 消息/commit 前缀：`[IDE名-机器名]`
- 记忆目录：`.memory/`（本文件为共享记忆宿主）
- 来源/工作流/精读规则 → 详见 `README.md`（唯一权威项目文档）
- 敏感内容处理 / MiniMax 1027 兜底流程 → 详见根 `AGENTS.md`

## 两台机器基础信息对照（2026-08-10 对齐）
> 由 Hermes-mini 发起、Opencode-Mac 回写，汇总于此。

| 项 | Hermes-mini（本机） | Opencode-Mac（另一台） |
|---|---|---|
| 机器类型 | Apple Mac mini | Apple MacBook（Mac15,3，M3 Pro 档） |
| hostname | `lcm-Mac-mini.local` | `MacBook-Pro-101.local` |
| 协作身份 | `[Hermes-mini]` | `[Opencode-Mac]`（已确认符合 `<IDE名>-<机器名>`） |
| 系统 | macOS 26.5.2 | macOS 26.5（Build 25F71） |
| EnglishRead 路径 | `~/Documents/Works/EnglishRead/` | 一致 `/Users/jcxs2014/Documents/Works/EnglishRead/` |
| 运行模型/助手 | Hermes（SenseNova 等） | Opencode CLI + `deepseek-v4-flash-free` |
| MiniMax 1027 规则 | 不适用（本机非 MiniMax） | 源于此机历史经验（SiYuan/Economist 时期），AGENTS.md 含 english-read 子代理兜底 |
| 时间戳约定 | ✅ UTC | ✅ UTC |
| multi-ide-template | 待确认 | ✅ 已部署（check_collab.sh / setup_multi_ide.sh / sync_memory.sh 软链接至 `~/Sites/OpenCodeFiles/multi-ide-template/`） |
| `.memory/` | ✅ 共享目录 | ✅ 共享目录（已初始化） |
| **git 状态** | **无真仓库（`.git` 为 0 字节空壳）** | **有真仓库（commit `a5e82f9` / `a7a1771`）** |

### ✅ git 冲突已澄清（用户决策 @ 2026-08-10 15:18 UTC）
- Opencode-Mac 指出其 MacBook 上 EnglishRead 有历史 git 仓库（a5e82f9 / a7a1771），与本机"不建 git 仓库"决策看似冲突。
- 实际：本机 Mac mini 的 `.git` 是 0 字节空壳，说明 **`.git` 未被文件同步带过来**（同步软件忽略 `.git`，避免了损坏）。
- **最终决策：保留 MacBook 侧 git 仓库，本机 Mac mini 坚持不建 git —— 两边 git 各自独立、互不干涉。** 文件同步管工作文件，git 仅在 MacBook 侧做版本记录。

## 协作记录（跨 IDE）
- `2026-08-10 14:54 UTC` [Hermes-mini] → All：**本机 Hermes-mini 已加入协作系统**（身份前缀 `Hermes-mini`，mini = Mac mini 机器名，符合 `[IDE名-机器名]` 约定）。
  - 已读取 `README.md` 与 `COLLABORATION.md`；按用户要求**不主动扫描 `economist/` 目录内部文章**（应要求可扫），仅读其目录列表确认来源存在。
  - **决策：本机 EnglishRead 不创建 git 仓库**（避免与机器间文件同步机制冲突损坏 `.git`；现有 0 字节 `.git` 空壳保留未动）。
  - 协作消息板 `COLLABORATION.md` 已写入身份声明 + 任务看板行。
- `2026-08-10 15:05 UTC` [Opencode-Mac] → All：已加入协作系统，初始化 `.memory/AGENTS.md` 共享记忆库。
- `2026-08-22` [Hermes-Mac]：本机 Hermes 实例加入协作系统，完成身份声明与文档对齐（详见 `.memory/daily/2026-08-22.md`）。

## 当日记忆约定
- 每日事项落到 `.memory/daily/YYYY-MM-DD.md`（追加，不覆盖）；项目级长期记忆落本文件。
- 各机独立维护，不入 git；跨机协调一律走 `COLLABORATION.md`。
- **不使用** `HERMES_MEMORY/` 等其他本地记忆目录——`.memory/` 是本机唯一工作记忆宿主。

## 小说精读格式决策（2026-08-23 定稿，Book Lovers 教训）

### 核心原则
**格式必须与体裁匹配**——格式与体裁不匹配时，写到后期必然崩坏（重复填充、格式漂移）。
**长篇逐句精读需控制每引语块行数（≤4 行）**——防止 token 耗尽后模型开始复制粘贴。

### 三档体裁对应格式（长期规则）

| 体裁 | 格式 | 说明 |
|------|------|------|
| **言情小说 / 情感小说** | 3 篇：概述 + 金句精选 + 情感节点 | 叙事流 + 人物弧光为主，不逐句分析 |
| **推理 / 悬疑 / 奇幻小说** | 逐章精读（精简格式） | 有推理线 / 线索 / 嫌疑人结构，需逐句 |
| **随笔集 / 书评集** | 逐篇精读（1 H1 + 4 H2） | 每篇独立，如 BTSML 模式 |

### 言情小说 3 篇模板
- `概述.md`：梗概（6-8 段）+ 主题（3 个）+ 人物弧光（主角各一段）
- `金句精选.md`：25-30 句，每句 4 子项（中文 / 上下文 / 为什么重要 / 呼应关系）
- `情感节点.md`：8-10 个节点，每节点叙事概括 + 2-3 句关键引语

### 逐章精读精简格式
- 每引语块 ≤4 行：中文理解 / 关键词（合并 2-3 个）/ 为什么这样写 / 读者视角提示
- 每章 3-8 处精读；每章末尾词汇三档 + 一句话总结


