# EnglishRead 跨 IDE 共享记忆（拓扑 + 协作日志）

> 注意：本文档为跨 IDE 共享记忆，非操作规则；操作规则见根 `AGENTS.md`，项目说明见 `README.md`。

## 是什么
中文母语者的英文**逐句精读**知识库。目标：从"看中文翻译"过渡到"直接读懂英文原文"。

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

## 现状（2026-08-19）
- **Economist 260815 批次**已精读 9 篇（主线程2 + 子代理7），全部 `状态: 未读` frontmatter，逐句精读完整：
  - 主线程：In_praise_designer_ish_babies（42句）、Nirmal_Purja_obituary（71句）
  - 子代理：Punishing_Putin / Venezuela_democracy / China_oil_OPEC / China_safety_theatre / China_mental_health / Taliban_engage / Zhu_Rongji
- **精读格式标准已定稿**（AGENTS.md + 项目记忆）：概览 → 逐句精读（`### 第 N 段` + `> **原句 M:**` 五子项分析块）→ 段落逻辑 → 词汇分级 → 长难句专项 → 总结 → 可迁移表达。核心：每原句一块，禁止合并。
- **Obsidian vault 配置**：`setup_obsidian.sh` 链接 ObsFile plugins/themes，properties 插件已启用，"状态"属性可点击切换
- **Marjane Satrapi 讣告**拼接异常已修复（原句1-50连续，9段标题完整）
- **本批（2026-08-19_Wednesday）非 Economist 精读 13 篇**已完成（Hermes-mini 主导）：
  - parisreview 4 / brainpickings 5 / lithub 4 / granta 0
- **上一批（2026-08-10_Monday）非 Economist 精读 19 篇 + 2 篇仅存档**
- **累计**：260606–260815 期 Economist 99 篇 + 非 Economist 34 篇 = 133 篇精读
- **Economist 已读期**：260606–260801（历史）+ 260627（回炉）+ 260808 + 260815
- **精读/存储规则（README 固化）**：每源每日 ≤10 篇，自动选 5 篇，宁少不凑；源文+精读均 `.md`+frontmatter；不可精读题材保留存档并加说明；未选源文当日清理
- **脚本布局**：各源 fetch 脚本收纳于其源文件夹；`scan.py` 跨源通用留根目录；`setup_obsidian.sh` 在工作区根目录
