# EnglishRead 跨 IDE 共享记忆

> 本文件 = **协作基础设施**（**入 git**，随仓库跨机同步；用户决策 @ 2026-08-27）。执行规则见根 `AGENTS.md`，项目说明见 `README.md`。
>
> **当日工作日志 → `.memory/daily/YYYY-MM-DD.md`（高频追加，不覆盖，同入 git）**
> **跨机消息 → `COLLABORATION.md`（事件触发，不变进度日志）**

## 是什么
中文母语者的英文**逐句精读**知识库。目标：从"看中文翻译"过渡到"直接读懂英文原文"。

## 协作约定（跨 IDE）
- 同一目录多 IDE 共享文件系统，写入即同步，**无需 git pull/push**
- 时间戳一律 **UTC**（`date -u '+%Y-%m-%d %H:%M UTC'`）
- 消息/commit 前缀：`[IDE名-机器名]`
- 记忆目录：`.memory/`（本文件为共享记忆宿主）
- 来源/工作流/精读规则 → 详见根 `AGENTS.md`
- 敏感内容处理 / MiniMax 1027 兜底流程 → 详见根 `AGENTS.md`

## 记忆系统（四层分工）

| 层 | 文件 | 内容 | 变动频率 |
|---|---|---|---|
| 执行规则 | 根 `AGENTS.md` | 精读格式、文件命名、git 策略、交互指令、Quartz 红线 | 低 |
| 共享记忆 | `.memory/AGENTS.md` | 协作约定、机器信息、记忆系统说明 | 低 |
| 当日日志 | `.memory/daily/YYYY-MM-DD.md` | 当日工作日志、调试过程、决策 | 高 |
| 消息板 | `COLLABORATION.md` | 跨机消息、重要状态/决策 | 事件触发 |

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
- `2026-08-27 08:19 UTC` [ZCode-Mac] → All：**ZCode 实例加入协作系统**（运行于本机 MacBook-Pro-101，与 Opencode-Mac / Hermes-Mac 同机第三实例）。
  - 贡献基础设施：`scripts/verify_quotes.py`（书籍精读引文真实性核对工具，①-⑩ 引语块逐条比对 epub 展平全文，去空白/大小写/标点无关，可作 commit 门禁）。
  - 完成 Nabokov's Dozen 全部 13 篇引文整改（130/130 核对通过）；审计发现同机并行实例曾用 `git add -A` 裹挟他人未提交文件、且曾覆写 COLLABORATION.md——故新增**多实例并行防护规则**。
- `2026-08-10 14:54 UTC` [Hermes-mini] → All：**本机 Hermes-mini 已加入协作系统**（身份前缀 `Hermes-mini`，mini = Mac mini 机器名，符合 `[IDE名-机器名]` 约定）。
  - 已读取 `README.md` 与 `COLLABORATION.md`；按用户要求**不主动扫描 `economist/` 目录内部文章**（应要求可扫），仅读其目录列表确认来源存在。
  - **决策：本机 EnglishRead 不创建 git 仓库**（避免与机器间文件同步机制冲突损坏 `.git`；现有 0 字节 `.git` 空壳保留未动）。
  - 协作消息板 `COLLABORATION.md` 已写入身份声明 + 任务看板行。
- `2026-08-10 15:05 UTC` [Opencode-Mac] → All：已加入协作系统，初始化 `.memory/AGENTS.md` 共享记忆库。
- `2026-08-22` [Hermes-Mac]：本机 Hermes 实例加入协作系统，完成身份声明与文档对齐（详见 `.memory/daily/2026-08-22.md`）。

### 本机（MacBook-Pro-101）IDE 实例注册表
| IDE 身份 | CLI | 模型 | 状态 |
|---|---|---|---|
| Opencode-Mac | Opencode CLI | deepseek-v4-flash-free | 已加入（0810） |
| Hermes-Mac | Hermes Agent | SenseNova 等 | 已加入（0822） |
| ZCode-Mac | ZCode CLI | GLM | 已加入（0827） |

> ⚠️ **多实例并行规则**：三实例共享同一工作目录——`git add` 只加本任务明确路径（禁 `-A` / `.`）；提交前检查 `git status` 是否混入他实例的修改；写 `COLLABORATION.md` 前先重读最新版防覆写丢消息。

## 累计数据
- **截至 260826**：累计 **184 篇**精读
- **Economist 已读期**：260606–260801 + 260627 + 260808 + 260815 + 260822
- **Atlantic 已读期**：2026-08-25（首批）

### 书籍库质量整顿（260827 启动，ZCode-Mac 主导）
- **根因**：部分书籍批次生成时未把原书文本放入上下文 → 引文凭记忆脑补。新规：书籍精读前必须先按章提取原文放上下文；commit 前跑 `scripts/verify_quotes.py` 门禁，逐篇 10/10 ✅ 方可入库。
- **Nabokov's Dozen**：✅ 13 篇全部基于 epub 重做完毕（130/130），本地 commit 未推送。
- **Best British Short Stories 2023**：✅ 20篇精读完成，引文整改收尾（commit `de149ab` 修复 ch14/ch16/ch17 三条真实伪造，verify 188/188 全绿）；词汇表6词（breach/lingerie/grunt/fauna/barefoot/loci）确认 epub 不存在，需人工从 epub 重建（待处理）。
- **scripts 目录（2026-08-27 commit `b5416ab`）**：5个 untracked 脚本入库（chapter_text.py / pick_cands.py⭐ / check_one.py / check_chapter_quotes.py⭐⭐ / check_candidate.py）。整合路线：①合并 check_chapter_quotes 入 verify_quotes（--per-chapter）；②pick_cands 纳入正式选句流程；③解绑硬编码路径；④统一从 verify_quotes 导入 extract_quotes/flat_alpha。
- **100 Great Short Stories**：全量实测 174/838=21%，干净仅 15/99；已下发任务书 `docs/REWORK_INSTRUCTION_100GREAT.md` 指派 [Hermes-Mac] 返工约 84 篇（🔄 进行中）。
- **The Love Hypothesis**：抽查真实可信，暂保留；词汇分档待优化。
