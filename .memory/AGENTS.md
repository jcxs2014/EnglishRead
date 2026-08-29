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
> 实战样本：Traitors' Nest（4 项外围修复）、Natural Selection（10+ 处总览层整改）、Room in the Ground（章节层 5 跨章 + 总览层 13 虚假）；多书在 verify_quotes 主门禁全绿下仍漏网的事实级缺陷，均由本 SOP 兜底。

#### 完成报告硬要求（执行方交付审查时必填，2026-08-29 立）

> 与根 `AGENTS.md` 第 10 条"完成报告硬要求"段呼应；本节为详细操作规范。

| 项 | 操作 | 不达标处理 |
|---|---|---|
| 三件套原始输出 | `verify_quotes` / `check_vocab` / `check_chapter_quotes` 三份原始逐行结果贴 commit message 或 COLLABORATION.md | 只贴"X/X ✅"和数字 → 审查方拒收 |
| 总览层引语 grep | 概述/金句集/情感节点的每条英文引语附 `grep -c "<关键词>" text/ch*.txt` 结果，MISS=0 | MISS > 0 → 退回执行方 |
| 总览层人物身份/关系/结局 grep | "做了什么"陈述附 grep 人名/地名 + 原文行号支撑 | 无支撑行号 → 退回执行方 |
| 跨书污染自检 | 不熟悉的人名/地名先 `grep -rl "<name>" notes/books/` | 在他书命中且本任务未识别 → 退回执行方 |

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

**1a. 说话人反转**（SOP 第 1 类子项，2026-08-29 Room 实战新增）——总览层 grep 命中后必须二次确认说话人：
- 同一英文逐字命中 ≠ 说话人正确。Room 实证 8 处金句说话人错位：
  - **㉒ "What I did to you"**：标 Kim→实为 **Rudbeck** 对 Kim 的悔罪台词（ch12）
  - **㉓ cuckoo clock**：标 Jonny 描述 Kim→实为 **Irma** 对 Julia（ch09）
  - **㉗ "I'm calling an ambulance"**：标 Astrid 改口→实为 **车主**（ch21）
  - **㉑ cockfight**：标 Animal Action→实为 ch08 葬礼巴士上的 Astrid
  - **㉙ "So much life"**：标 Kim→实为 Rudbeck 对 Kim "Just you"
  - **㉚ "I knew exactly what I was doing"**：标 Rudbeck rationalize→实为 Rudbeck 用链条勒住 Kim 时的 snarl
  - **⑰ "despicable but anything but stupid"**：标 Rudbeck→实为 ch24 Julia 看 **Claes-Göran 宣传视频** 的评价
  - **⑭ "escaped slaughter"**：标 Astrid 躲在柜子里→原文无此细节，实为葬礼现场
- **预防**：总览引语 grep 命中后必 grep 前后 ~200 字符窗口确认说话人，并把说话人名与原始章节精读文件的说话人核对一致
- **子代理委派必附**：本类失败案例 + 防幻觉条款（见根 `AGENTS.md` 第 9 条 f）

**1b. cliffhanger 跨章场景**（2026-08-29 Room 实战新增）——前一章以悬念收尾、对话在后一章展开时，禁止把整场戏的引语放进前一章：
- Room 实证：㉑ cockfight 误归前一章（ch08 末葬礼 + Animal Action 在 ch71 跨 67 章）+ ㉒ What I did to you 误归前一章
- **预防**：遇到两章边界的引语必须同时读前后章 text/ 各 ~100 行确认引语实际发生章节（不是尾段所在章节）

**1c. 复合引语/拼接句**（2026-08-29 Room 实战新增）——总览引语长度 >40 字符且含 `…` 或 `. . .` 中段省略的，verify_quotes 靠 flat 前缀匹配会让尾段非逐字漏网：
- Room 实证：ch09 把 Irma 的"...cuckoo clock..."与 Julia 的 "It was a comic touch!" 拼成一句；ch74 "Jolifanto" 单词在本章但完整 chant "Jolifanto bambla ô falli bambla!" 在前两章
- **预防**：必须单独 grep 前后两段确认各自落在原文何处；拼接句要按所属说话人分别核实

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

**5. 章节标题/文件名系统性偏移**（2026-08-29 Room 实战新增）——审计阶段必须全库比对：
- **操作**：自写脚本对每文件 `filename-chapter` vs `H1-chapter` vs `text-suffix`（book-chapter）三者交叉，发现 >2 个连续偏移即判块状命名坑
- **Room 实证**：19 文件名 + 3 个 H1 比真实书章号偏高 1，集中在 **ch05–ch13 / ch20–ch28 / ch58** 三段（块状聚集），非随机散布；副作用："Chapter 13" 双文件标题重复 + "Chapter 4" 标题缺失
- **预防**：审查第一步上 `audit_book.py` 后必补此三向比对

**6. 章节编号改动联动 cross-ref 失效**（2026-08-29 Room 实战新增）——执行阶段凡改任何章节标题/H1/文件名：
- **必须全库 grep** `"Chapter N"` 引用（N ∈ [改前值, 改后值]）逐条核对落点
- **Room 实证**：ch13 改"Chapter 12"后 4 处"Midsummer Eve 在 Chapter 4"引用实际全在书 7 章；批量整改 TV4 审片（ch03 vs ch04）、Animal Action（ch24 vs ch06）等 7 处 cross-ref
- **预防**：所有 cross-ref 改动必须附 grep 实证行号

**7. 跨实例并发纯改名 commit**（2026-08-29 Room 实战新增）——审计之外的并发安全条款：
- **场景**：会话期间另一实例可能顺带做了与本任务相同的纯文件名改名（0 内容变更），本轮修改干净叠加
- **预防**：审查期间若 `git pull` 后发现 `git log` 出现新 commit 涉及本任务文件，立即 `git show <新commit> --stat` 与自己未提交修改比对；冲突时按"内容优先于文件名"裁定取舍

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

#### Room in the Ground 实战补强（2026-08-29，71d909c SOP 增补）

> 五步审查 SOP 落地时撞出的额外条款，与上节"经验性条款"互补但侧重**结构性 + 跨章 + 并发**。

- **章节标题/文件名系统性偏移——必须全库 audit，不能只查首尾**：本轮发现 19 个文件名 + 3 个 H1 比真实书章号偏高 1，集中在 ch05–ch13 / ch20–ch28 / ch58 三段（块状聚集），非随机散布。**预防**：审查第一步上 `audit_book.py` 后，必须补一次自写脚本对每文件 filename-chapter vs H1-chapter vs text-suffix（book-chapter）三者交叉比对，发现 >2 个连续偏移即可判定有块状命名坑
- **说话人反转是总览层高发坑（SOP 第 1 类仅列"角色身份"虚构，未含"同一句被转引为不同说话人"）**：金句 ㉒ "What I did to you" 原作者以为是 Kim 对 Julia 的 confession，实为 ch12 **Rudbeck** 对 Kim 的悔罪台词——同一英文逐字命中，但总览层说话人完全反转。**预防**：总览引语 grep 命中后必 grep 前后 ~200 字符窗口确认说话人，并把说话人名与原始章节精读的说话人核对一致
- **cliffhanger 跨章场景——前一章以悬念收尾、对话在后一章展开时，禁止把整场戏的引语放进前一章**：金句 ㉑ cockfight 误标为 Animal Action（实为葬礼巴士）、㉒ What I did to you 误归 Kim——都是把"前一章末尾铺垫 + 后一章展开"对话压缩归在前章。**预防**：总览层核对时，遇到两章边界的引语必须同时读前后章 text/ 各 ~100 行确认引语实际发生章节
- **复合引语/拼接句按所属说话人分别核实**：ch09 把 Irma 的 "...cuckoo clock..." 与 Julia 的 "It was a comic touch!" 拼成一句（拼接两句）；ch74 "Jolifanto" 单词在本章但完整 chant "Jolifanto bambla ô falli bambla!" 在前两章（半句归本句）；verify_quotes 靠 flat 前缀匹配会让尾段非逐字漏网。**预防**：引语长度 >40 字符且含 `…` 或 `. . .` 中段省略的，必须单独 grep 前后两段确认各自落在原文何处
- **跨实例并发纯改名 commit——验证"修改干净叠加无内容冲突"是审计之外的并发安全条款**：会话期间另一实例提交 `b5db591`（Yellow Pine ch06-08）顺带做了与我相同的 ch05-ch13 纯改名（0 内容变更），本轮修改干净叠加。**预防**：审查期间若 `git pull` 后发现 `git log` 出现新 commit 涉及本任务文件，立即 `git show <新commit> --stat` 与自己未提交修改比对；冲突时按"内容优先于文件名"裁定取舍
- **check_chapter_quotes 对长篇同样必要——非短篇合集专属**：71d909c SOP 第 2 步已要求但 Room 这轮实证出长篇 5 章跨章错植（ch05/ch32/ch33/ch74/ch09），均为前次 commit 漏网。**预防**：长篇审查时尤其要跑 check_chapter_quotes，特别是 `--out-dir` 必须指向本书 text/（脚本默认是 100 Great 路径，否则会全量误报）
- **章节编号错位会联动 cross-ref 失效**：ch13 改"Chapter 12"后，4 处写于旧编号期的"Midsummer Eve 在 Chapter 4"引用实际全在书 7 章；批量整改 TV4 审片（ch03 vs ch04）、Animal Action（ch24 vs ch06）等 7 处 cross-ref。**预防**：执行阶段凡改任何章节标题/H1/文件名，必须全库 grep "Chapter N" 引用（N∈[改前值,改后值]）逐条核对落点

#### Wolftamer 实战补强（2026-08-29，9b2ab04 整改新增）

> 本轮独立审查发现执行方完工声明通过后、总览层仍含传播性虚构引语；修复期间又挖出"完工覆盖缺口"和"工具调用陷阱"，与 Room 款经验互补。

- **完工消息"章数"必须用 md 数 vs text 章数对账**：执行方声称"ch02–ch64 逐章精读（62 章）"，但 md 文件实为 ch03–ch64（62 个文件），第一章（Chapter One，约 1900 词 Faolan 视角）无精读文件——"62 章"是文件数非覆盖数。**预防**：验收方收到完工报告后，第一件事 `ls text/*.txt | wc -l` 对比 `ls ch*.md | wc -l`，有缺口立即报。
- **交叉引用引语（呼应关系/前瞻/回扣 里的英文片段）与主句一样要过 epub 裁决**："I've made you a pirate" 在金句㉑ 上下文里被标为 ch41 回扣，但全书 epub 查无（真句是 ch14 "I'm a pirate"）；verify_quotes 只检主句不检呼应收引语，导致这条虚构片段随"回扣/前瞻"句式扩散到 7 处 × 3 文件才被发现。**预防**：审查总览层时，用 epub flat 指纹对金句/情感节点/概述里所有英文引语片段（不只是加粗主句）做逐字 grep，包括弯引号包裹的短片段。
- **Brona/Tavin/Lorcan 说话人错植是章级高频坑**：ch51 精读把"Get your fecking hands off my friend!"归给 Tavin，原文"another knife in her hand"自证首刀也是 Brona 掷的（Tavin/Lorcan 是拽人掩护者）。**预防**：语义抽查时，对"喊话/掷刀/弑敌"类动作句的说话人必须 grep text/chNN.txt 前后 5 行实证，不能凭分析文本的描述归因。
- **check_chapter_quotes 必须显式传 `--out-dir`（脚本默认值是 100 Great 路径）**：本轮首轮误报 302 MISS 是因为跨书调用漏传 `--out-dir`，校验器拿 100 Great 的 text/ 比对 Wolftamer 产生全量假 MISS。正确用法：`python3 scripts/check_chapter_quotes.py <NN> "<md>" --out-dir <书目录>/text`。
- **完工报告的 commit message 或 COLLABORATION.md 留言要贴三件套原始逐行输出**：不能只贴"X/X ✅"，要贴 verify_quotes / check_vocab / check_chapter_quotes 的原始逐行，便于审查方复验和追踪（NS/Traitors' Nest 两轮实证：数字干净≠内容干净）。
- **总览层自查三项（审查方和执行方自查都适用）**：①概述/金句集/情感节点的英文引语逐句 `grep` epub 展平全文；②人物身份/关系/结局的"做了什么"陈述须 grep 实体（人名/地名）并核对原文支撑；③任何不熟悉的人名/地名先 `grep -rl "<name>" notes/books/` 排除跨书污染（NS 的 Jo/Shayne 即《A Real Paige Turner》人物）。

### git 与协作规则
- `git add` 只加本任务明确路径（禁 `-A` / `.`），commit 前检查 `git status` 防混入他实例修改
- COLLABORATION.md 看板更新：**追加到表格末尾**（用最后一行作锚点 patch），禁止中间插入
- 重复填充修复：**必须一篇一篇手动修**，拒绝脚本批量处理
- push 前先拉取远程（`git pull`），避免分叉；批次进行中不自动 push
- `.src.md` 原文文件被 `.gitignore` 忽略，勿强行 add
- **跨机同步**：FreeFileSync 已取消（2026-08-25），完全靠 git 仓库沟通；`.memory/` 入 git 两机都能 pull；跨机决策走 COLLABORATION.md，本机工作规则写 `.memory/AGENTS.md`
