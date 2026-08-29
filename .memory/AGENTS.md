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
- **截至 260828**：累计 **344 篇**精读（+36，Things We Fake）
- **Economist 已读期**：260606–260801 + 260627 + 260808 + 260815 + 260822
- **Atlantic 已读期**：2026-08-25（首批）

### 书籍阅读进度追踪（迁移自系统记忆，2026-08-29 起统一存放于此文件）

| 书 | 状态 | 进度 | 备注 |
|---|---|---|---|
| The Room in the Ground (John Ajvide Lindqvist) | ✅ 全部完成+审查整改 | ch01-95 / 235 引文 / 0 FAIL vocab / 94/94 干净 / 49 commits / 总览3篇 | HEAD `5954892` fix: 总览层13处虚假修复；章节层审查+整改 `969be42`：19文件名对齐(ch05-13/ch20-28/ch58) + 5章跨章错植引语修复 + 11文件词汇分档 + 7处cross-ref更正；verify 235/235 ✅ |
| Golden Boy (A. J. Symon) | ✅ ch01-19 | 69/69 引文全绿 / 0 FAIL vocab | ch20-21 + 总览待完成 |
| Things We Fake | ✅ 完成 | 36 章 / 238/238 引文 | |
| The Eleventh Hour | ✅ 完成 | 25 章 / 175/175 引文 | |

**verify_quotes 失败主因**：引文含 speech tag 打断 fingerprint（须保留 tag 如 `said Christof`）；check_vocab FAIL=虚构词不在语料（换原文有词如 help/sure/chase/crowd/time/night/office/wordless/carry/patronizing）。

**Room 章节映射**：text 文件编号 = epub 章节号 + 1（ch47_46.txt = Chapter 46 内容）；.md 文件编号 = text 文件编号。epub 章节映射补充：`index_split_070.html`=Chapter 64（ch65.md）、`index_split_073.html`=Chapter 68（ch69.md）、`index_split_077.html`=Chapter 73（ch74.md）、`index_split_080.html`=Chapter 76（ch77.md）、`index_split_096.html`=Chapter 89（ch90.md）、`index_split_099.html`=Chapter 92（ch93.md）、`index_split_101.html`=Chapter 94（ch95.md，epilogue）。

### 书籍库质量整顿（260827 启动，Opencode-Mac 主导）
- **根因**：部分书籍批次生成时未把原书文本放入上下文 → 引文凭记忆脑补。新规：书籍精读前必须先按章提取原文放上下文；commit 前跑 `scripts/verify_quotes.py` 门禁，逐篇 10/10 ✅ 方可入库。
- **已完成**：
  - Nabokov's Dozen ✅ 13 篇（130/130）
  - Best British Short Stories 2023 ✅ 20 篇（188/188）
  - Collected Stories (Peter Carey) ✅ 27 篇（182/182）
  - Good and Evil ✅ 8 篇（53/53）
  - The Isolationist ✅ 7 篇（66/66）
  - Book Lovers ✅ 42 篇（214/214）
  - If You See Me Don't Say Hi ✅ 11 篇（46/46）
  - O Henry Best Short Stories 2024 ✅ 20 篇（105/105）
  - Empty Bottles Full of Stories ✅ 93 篇（292/292）
  - My Husband's Wife ✅ 71 章（336/336）
- Things We Fake ✅ 36 章（238/238）
  - The Eleventh Hour ✅ 25 章（175/175）
- **进行中**：100 Great Short Stories 返工（Hermes-Mac）
- **Best British Short Stories 2023**：✅ 20篇精读完成，引文整改收尾（commit `de149ab` 修复 ch14/ch16/ch17 三条真实伪造，verify 188/188 全绿）；词汇表6词（breach/lingerie/grunt/fauna/barefoot/loci）确认 epub 不存在，需人工从 epub 重建（待处理）。
- **scripts 目录（2026-08-27 commit `b5416ab`）**：5个 untracked 脚本入库（chapter_text.py / pick_cands.py⭐ / check_one.py / check_chapter_quotes.py⭐⭐ / check_candidate.py）。整合路线：①合并 check_chapter_quotes 入 verify_quotes（--per-chapter）；②pick_cands 纳入正式选句流程；③解绑硬编码路径；④统一从 verify_quotes 导入 extract_quotes/flat_alpha。
- **100 Great Short Stories**：全量实测 174/838=21%，干净仅 15/99；已下发任务书 `docs/REWORK_INSTRUCTION_100GREAT.md` 指派 [Hermes-Mac] 返工约 84 篇（🔄 进行中）。
- **The Love Hypothesis**：抽查真实可信，暂保留；词汇分档待优化。

### 精读格式规范（2026-08-26 定稿）

| 体裁 | 格式 |
|------|------|
| 言情/情感小说（长篇） | 逐章精读 + 3 篇总览（概述/金句/情感节点） |
| 推理/悬疑/奇幻小说（长篇） | 逐章精读（精简格式，引语块 ≤4 行） |
| 言情/恐怖短篇合集 | 逐篇精读（10块 + 五子项 + 三档词汇 + 一句话总结） |
| 随笔/书评集 | 逐篇精读（1 H1 + 4 H2） |
| 非虚构论述 | 逐章精读 + 论证结构分析 |

**文件名唯一分隔符**：单空格（禁止 `_` `-` `'` 等特殊字符）；标点全部去除。

### 独立审查 SOP（独立审查员专节，2026-08-29 立）

> 场景：本机/他机另一实例（或过去自己）完成某本书的精读并交付，本节为审查方的标准流程。
> 与根 `AGENTS.md` 第 10 条呼应，本节为详细 checklist。
> 实战样本：Traitors' Nest（4 项外围修复）、Natural Selection（10+ 处总览层整改）；两书在 verify_quotes 主门禁全绿下仍漏网的事实级缺陷，均由本 SOP 兜底。

#### 五步审查法

| 步骤 | 工具/口径 | 必跑项 | 失败处理 |
|---|---|---|---|
| 1. 三件套重跑 | `verify_quotes` / `check_vocab` / `check_entities` | 全部从本机重跑；**不信报告数字** | 任一 FAIL → 退回执行方 |
| 2. 逐章归属 | `check_chapter_quotes.py <NN> <md> --out-dir text/` | 每章必须"X/X in chNN text" | MISS → 标记跨章错植，定位原属章节后从执行方拿正确引语 |
| 3. 结构扫描 | 行首引语块正则扫 | 编号连续 / 四件套齐全 / 零孤儿块 / 零重复块 | 编号跳序、缺字段、重复行 → 列出章节清单交回 |
| 4. 语义二审 | 子代理或主会话逐对核对 | "引语↔中文理解"逐对；子代理委派必附反例+防幻觉条款（见根 `AGENTS.md` 第 9 条 f） | 引语换新句但分析停旧句 → 触发规则 9 修复即同步 |
| 5. 总览事实核对 | 人工 grep 实体+引语 | 概述/金句/情感节点逐句校验 | 见下方"四类高发坑位" |

#### 四类高发坑位（NS / TN 实证）

**1. 总览层情节虚构**——`verify_quotes` 主口径不解析 `00_金句精选.md` / `00_情感节点.md` / `概述.md`，必须人工 grep：
- **角色身份**（"主角是侦探/演员"等）→ grep 人名 + 读章节文件交叉核对。NS 实锤：概述把 Megan 写成"被 Kevin 强奸"——实为 Bee
- **人物关系**（"A 是 B 的母亲/父亲"等）→ 在关键章 grep 实词。NS 实锤：概述完全没提 **Bob = Megan 父亲**这一全书终局冲突的轴心
- **结局走向**（"他被绳之以法"等）→ 在最后两章 grep 结局动词
- **叙事结构**（"双时间线""POV 切换"等）→ 数章节标题/段首 POV 标记

**2. 跨书污染**——从其他书的设定串入本批：
- **NS 实证**：概述/金句/情感节点 3 处写"Jo 愤怒驱赶 Shayne"——这两人是《A Real Paige Turner》人物，NS 全文 `grep -rl "Jo\|Shayne" text/` 查无
- **Room in the Ground 实证**：Schöneberg 实为他书角色
- **预防**：任何不熟悉的人名/地名先 `grep -rl "<name>" notes/books/` 排除其他书同名人物

**3. 总览引语虚构**——主门禁通过不代表总览层全过。NS 实证：
- ⑯ "Bob, you're hunting girls. Not bears." **全书查无**（属改写台词）
- ⑮ "We ate them. When we kill men." 改写自原文 "how the men feel when we eat them. When we kill them."
- ⑱ 重复引号错误
- **预防**：总览引语必须逐句 grep 验证（见下方 grep 模板）

```bash
python3 -c "
import re,glob,sys
sys.path.insert(0,'scripts')
from check_chapter_quotes import flat
q='<引语原文>'
corpus=flat(''.join(open(f).read() for f in glob.glob('text/ch*.txt')))
print('OK' if flat(q) in corpus else 'MISS')
"
```

**4. A 类词汇虚构**——分档注水/常见词进 ⭐⭐⭐ / 例句改写：
- **写入/审查前**：`grep -i "word" text/chNN.txt` 验证
- **分档注水**：常见词混 ⭐⭐⭐ 高级档视为不合格（NS ch09 "afternoon"、ch11 "prisoners"/"breakfast"、ch18 "flashlight"、ch19 "scratches" 等被检出）
- **A/B 裁决**（规则 5）：epub 也查无 = A 类真虚构（换文中真实词）；epub 有而 text/ 缺 = B 类语料缺失（重跑 `extract_chapters.py` 修复或换真实词形）

#### 经验性条款（必读）

- **先重跑，不信报告数字**：执行方报告"73/73 ✅"时审查方必须复跑——NS 报告 101/101 实为 108/109 含 1 FAIL；TN 报告 44/44 包含 1 处错植未被报
- **短引语人工核验不可省**：verify_quotes 指纹阈值 ≥20 alnum 字符外的引语（NS 8 章出现）必须人工逐条 grep 文本+核验分析对应
- **金句集/总览层必须逐字 grep 复验**：主口径不解析 `00_*.md`，主脚本通过不代表总览层全过
- **子代理额度耗尽时主会话自执行不可省**：语义二审发现问题但子代理被 Token Plan 拦下时（NS 137 块三件代理被拦），主会话逐对核对仍可完成全部——发现配额不足前先评估"主会话能不能做"
- **用户授权"直接修"=默认分工例外**：独立审查 SOP 默认只审不改；用户明确授权后可批量执行（如 NS 总览层整改 `b3caa7e`）
- **COLLABORATION.md 必留**：审查完成后必写一条带 commit 引用的审查报告，按"主题/五步结果/整改清单/状态"四段式

#### 工具链现状

- `scripts/audit_book.py` 是单书一键总账（4 节 + 退出码），可作 push 前巡检；含 text/ vs epub 一致性抽检（防语料污染）
- 但**全库语义对应审计必须人工**（无自动化方案）：子代理委派 + 防幻觉条款 + 文本实证三件套
- 配套工具链全部用法见根 `AGENTS.md` 配套工具链小节

#### 已知失效样本（审查员"防幻觉"训练数据）

- 100G ch86 ⑧"引语讲遮盖、分析讲没有叔叔"——引语换新句但分析停旧句
- Angelic Death 概述 Sam 写成侦探、假结局
- Alfred Hitchcock 10 ⑥ 引语讲 A 场景、分析讲 B 场景
- A Real Paige Turner 概述虚构 POV、戒指来源；情感节点 3 处假引语
- Golden Boy / In a Heartbeat / Paige Turner 三本书累计 6 处审查代理幻觉报警——报警前须先确认引语行与中文理解行真实存在于同一 md 且相邻

### git 与协作规则
- `git add` 只加本任务明确路径（禁 `-A` / `.`），commit 前检查 `git status` 防混入他实例修改
- COLLABORATION.md 看板更新：**追加到表格末尾**（用最后一行作锚点 patch），禁止中间插入
- 重复填充修复：**必须一篇一篇手动修**，拒绝脚本批量处理
- push 前先拉取远程（`git pull`），避免分叉；批次进行中不自动 push
- `.src.md` 原文文件被 `.gitignore` 忽略，勿强行 add
- **跨机同步**：FreeFileSync 已取消（2026-08-25），完全靠 git 仓库沟通；`.memory/` 入 git 两机都能 pull；跨机决策走 COLLABORATION.md，本机工作规则写 `.memory/AGENTS.md`
