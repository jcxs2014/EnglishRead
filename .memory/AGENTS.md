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

## 现状（2026-08-10）
- **本批（2026-08-10_Monday）已精读 19 篇 + 2 篇仅存档**，全部编号连续、源文/精读/selected.json/index.json 四套对齐：
  - `granta/` 6 篇（精读 4：01 Wake / 02 骨头里的尘土 / 05 另一种挪威语 / 06 信仰的维度；仅存档 2：03 未成年性剥削、04 成人情色，顶部已加说明）
  - `brainpickings/` 5 篇（精读 5：斯多葛解药 / 阿伦特论爱与丧失 / 游泳与生命意义 / O'Donohue 论"开始" / 多迷走神经理论）
  - `lithub/` 5 篇（精读 5：戳破硅谷神话 / Salinger 与二战 / 大揭秘的毒性 / 石油公司 50 年否认史 / 看封面判断书）
  - `parisreview/` 5 篇（精读 5：纽约下水道 / 运动的剧场 / 配角·Steve Zissou / 间隙组织 / 城市写作；重编号 01–05）
- **精读/存储规则（README 固化）**：每源每日 ≤10 篇，自动选 5 篇，宁少不凑；源文+精读均 `.md`+frontmatter；不可精读题材（未成年性剥削/成人情色）保留存档并在源文顶部加说明，不产出精读；未选源文当日清理。
- **脚本布局（已整理）**：各源 fetch 脚本收纳于其源文件夹内（`parisreview/fetch_paris.py` / `granta/fetch_granta.py` / `brainpickings/fetch_brainpickings.py` / `lithub/fetch_lithub.py`）；`scan.py` 跨源通用，留根目录；一次性 RSS 探测脚本 `feed_check.py`/`feed_check2.py` 已删，`__pycache__/` 已清。README 引用已同步。
- `economist/` 已读期：260606–260801（本工作区**不主动**扫描其内部；如需针对具体问题，可应要求扫描）
- **260627 期回炉（2026-08-10）**：首轮精读格式不达标，Burnham/Global/University 三篇重写，Alan P55 插入，末尾段落修复；Commit `9f8ff5f`
