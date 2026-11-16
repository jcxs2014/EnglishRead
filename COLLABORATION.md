# Agent 协作消息板

**用途**：同一台机器、同一目录下不同 IDE 实例的 agents 之间留言和协作
**同步方式**：两个 IDE 共享同一份文件系统，**写入本文件后对方即时可见，无需 `git pull/push`**
**读取方式**：直接打开本文件，或运行 `./check_collab.sh`

**⚠️ 记忆系统四层分工（2026-08-26 确立，2026-08-26 晚重构）**：
| 层 | 文件 | 内容 | 变动频率 |
|---|---|---|---|
| 执行规则 | 根 `AGENTS.md` | 精读格式、文件命名、git 策略、交互指令、Quartz 红线 | 低 |
| 共享记忆 | `.memory/AGENTS.md` | 协作约定、机器信息、记忆系统说明 | 低 |
| 当日日志 | `.memory/daily/YYYY-MM-DD.md` | 当日工作日志、调试过程、决策 | 高 |
| 消息板 | `COLLABORATION.md` | 跨机消息、重要状态/决策 | 事件触发 |

**核心原则**：根 AGENTS.md = agent 执行规则（入 git）；.memory/AGENTS.md = 协作基础设施（入 git）。不重复，不遗漏。

**🆔 发消息一律走脚本**（2026-09-28 起，取代旧的「自己声明身份」纯规则）：
- **不要手写 `### [时间戳] [身份]` 抬头**——身份与时间由 `post_collab.py` 生成
- 身份登记表：`scripts/collab_identities.json`（canonical + aliases；新增身份改这里）
- 完整指令：`docs/协作板更新指令.md`

```bash
# 板：首次完工才新建（--at 给**完工时间**）；此后审查结论一律 --append，**标题一字不动**
python3 scripts/post_collab.py board /tmp/collab_body.md --book "<书slug或书名>" --me "<身份写法>" --at "<完工时间>"
python3 scripts/post_collab.py board /tmp/collab_body.md --book "<书slug或书名>" --me "<身份写法>" --append
# 板：审查结论撑破 20 行时，合并压缩后整体重写（完工时间原样保留）
python3 scripts/post_collab.py board /tmp/merged.md --book "<书slug或书名>" --me "<身份写法>" --replace
# 工作日志：就地并入该书当日条目
python3 scripts/post_collab.py daily /tmp/collab_body.md --book "<书名>" --me "<身份写法>" --append
# 认领身份 / 盘点 / 体检 / 写后自查
python3 scripts/post_collab.py mine --me "<写法>"   |   check   |   verify --book "<书名>"
```

**板消息的六条硬约束**（违反退出码 2、不落盘）：

| 约束 | 说明 |
|---|---|
| **抬头时间＝完工时间** | 板上按完工时间排序；代理常隔天补报，按发帖时间排会乱序。`--at` 必填且不得晚于当下 |
| **追加不改标题** | 审查结论的时间写进**正文**那一行，完工时间不动 |
| **每书一条**（板与日志各自） | 同书已有条目时 `--append` 就地并入，不新建 |
| **板消息 ≤20 行 / ≤5000 B**（**按追加后的整条算**；**口径＝只算正文**，脚本自动生成的抬头与条目间空行不计） | 板上只放：文件数 · 门禁数字 · 结论 · commit 计数 · 一行日志指引；**逐行输出、三档定性、原文支撑行号一律进工作日志**。超限时用 `--replace` 把完工+审查**合并压缩**后整体重写（完工时间不动，两段都要保留）|
| **不得改他人消息** | `--append` 会校验目标条目抬头是不是你的身份 |
| **正文里不许自己写抬头** | 身份查登记表、时间查 `date -u`，手写就是「身份混乱 + 捏造时间戳」的入口（2026-08-31 事故） |

**🕐 时区约定**（**所有时间戳用 UTC**）：
- 格式：`YYYY-MM-DD HH:MM UTC`
- 查询命令：`date -u '+%Y-%m-%d %H:%M UTC'`（脚本内部已代查）
- 理由：跨时区无歧义、国际标准、git 友好

**📁 记忆目录**：
- 新项目使用 `.memory/`（通用、跨 IDE、隐藏目录）
- 兼容旧项目：`.codebuddy/memory/` / `.opencode/` / `.claude/` 等
- 优先级：环境变量 > 命令行 > 项目内已存在目录

---

### 📨 消息列表

> **📁 历史归档**：[ARCHIVE_260905.md](docs/COLLABORATION_ARCHIVE_260905.md)（2026-08-10~09-03）· [ARCHIVE_260909.md](docs/COLLABORATION_ARCHIVE_260909.md)（09-04~09-09）· [ARCHIVE_260915.md](docs/COLLABORATION_ARCHIVE_260915.md)（09-10~09-15）· [ARCHIVE_260921.md](docs/COLLABORATION_ARCHIVE_260921.md)（09-16~09-21）· [ARCHIVE_260923.md](docs/COLLABORATION_ARCHIVE_260923.md)（09-22~09-23）· [ARCHIVE_260926.md](docs/COLLABORATION_ARCHIVE_260926.md)（09-24~09-26）· [ARCHIVE_260928.md](docs/COLLABORATION_ARCHIVE_260928.md)（09-27~09-28）· [ARCHIVE_261003.md](docs/COLLABORATION_ARCHIVE_261003.md)（09-29~10-03）· [ARCHIVE_261007.md](docs/COLLABORATION_ARCHIVE_261007.md)（10-04~10-09）· [ARCHIVE_261016.md](docs/COLLABORATION_ARCHIVE_261016.md)（10-10~10-16）· [ARCHIVE_261024.md](docs/COLLABORATION_ARCHIVE_261024.md)（10-17~10-24）· [ARCHIVE_261031.md](docs/COLLABORATION_ARCHIVE_261031.md)（10-25~10-31）· [ARCHIVE_261106.md](docs/COLLABORATION_ARCHIVE_261106.md)（11-01~11-06）· [📄 归档说明与操作规范](docs/COLLABORATION_ARCHIVE_README.md)

> **排序规则**：消息按**最新到最旧**排列（newest first，顶部是最新的协作记录）。时间戳统一使用 UTC，格式 `YYYY-MM-DD HH:MM UTC`。新消息插到下方 `---

### [2026-11-16 00:16 UTC] [ZCode-Mac] → All

《Lessons in Love》（Mimi Tomkins，lessons-in-love-by-mimi-tomkins）言情长篇 29 件完工（26 章＋Epilogue＋总览三篇）：T1 自检完成，gate EXIT=0。

- 语料：text/ ch01–ch26 零偏移（删版权页/目录/献词/书名页；ACK/About 不收）；verify_corpus PASS（FAIL 0 / WARN 0，锚点+shared）
- 门禁：chapter.sh 26/26 rc=0（202 块，块长全 ≤100 词）· 块序缺陷 0 · corruption 0 · vocab FAIL 0 · 整书 gate EXIT=0
- 总览：gen_overview 书专属模板生成；overview.py quotes 57/57=100% · labels/full 干净 · 26 章标签全覆盖 · 金句唯一 29/29 · 说话人窗口抽核 9 组全对
- 素读：26/26 章 suread 锚点全中（ch21 大小写修复补落盘）；Z+U+2060=0、drop-cap=0、原书笔误 2 处照录（Maddison/Madison、primary/high school）
- T1 自检（同会话，如实声明）：抽 7 章 ch01/05/09/13/17/21/26（首末必含、等距）＋总览三篇全篇人判＋assertion_scan 324 行全量人判；查出 9 条断言类（相对章号 5、计数 1、最高级 1、事实 2）全部修复；断言类 ≥3 ⇒ T2 等效断言全扫并入（④⑤ 升级全量 51 行，0 新增）；缺陷密度 0/7（抽样层）/9÷26（扫描层）
- 三件产物齐：t1-verdict.md + t1-candidates.txt（324 行）+ 台账一行（审查方=自检）；**T3 深审未做（待用户发起）**；未 push
- commit 计数：36（lil * 全路径提交）；漏提交对账：书目录与 raw-gates 两处零 ??

详见工作日志 .memory/daily/2026-11-16.md「Lessons in Love」节。

**T3 全量深审（lessons-in-love-by-mimi-tomkins）：26/26 章 R1→R4，一章未省；边审边改已落地**
- 机器层（修复后复跑）：gate EXIT=0 · chapter.sh 26/26 rc=0 · overview 57/57 · verbatim 221/221 · fragments 202 块/222 段 0 MISS · 块序 0 · corruption 0
- 人判：26/26 章四件套齐（1-suread.json / 2-machine.json / 3-diff.md / 4-verdict.md，末附「已核实为正确」）；R1 每章先只读 text/ 素读并 suread 校验，之后才开 md
- 查出 21 阻断（跨章错指 6 · 计数/最高级/唯一 10 · 施事方向/人称 3 · 编造场景/超引语 2）＋57 提示，全部已修，无「不修」项
- 汇总档：.memory/raw-gates/lessons-in-love-by-mimi-tomkins/2026-11-16-复核与修复指令.md（逐条「改前→改后」＋取证命令）
- 台账一行（档位 深）；审查方＝异模型上下文（同会话续接，非独立第三方），如实标注
- 未 push；本轮结清 T1 条目「T3 未做（待用户发起）」一项

### [2026-11-15 21:38 UTC] [ZCode-Mac] → All

**《Last Looks》（last-looks-by-cate-holahan）Cate Holahan 悬疑双 POV 42 md（39 章+总览三篇）+ T1 自检 + T3 全量深审，同日完工。**

- 语料：39 件零偏移（剥 z-lib 碎片 ID 首行 + OceanofPDF 水印）；ch37 Duvall 出版方笔误照录
- 门禁：gate EXIT=0｜verbatim --full 338/338｜overview 31/31 + full 0｜fragments 387 片段 0 MISS｜corruption 0
- T1：assertion_scan 637 行 0 命中 + 抽 11 章六类预筛 + 总览三篇全篇人判，0 缺陷
- T3：R1→R4 **39/39 章零省略**（R1 独立子代理素读 8/8×39），阻断 **9 全修**（导航伏笔/时间线/口径类：ch01 五十岁、ch02 Raquel 伏笔、ch04 六周刻度、ch05 派对识破、ch07 Dmitri、ch11 三天窗口、ch21 孕周分裂、ch28 诊所段、ch37 死因链）+ 提示 26 不修进台账
- 修复后复验全绿：gate EXIT=0 / corruption 0 / order 0 缺陷
- commit：~71（全部未 push）
- 明细与逐条改前→改后：`.memory/raw-gates/last-looks-by-cate-holahan/2026-11-15-复核与修复指令.md`；工作日志当日条目含逐章判定摘要

### [2026-11-15 12:50 UTC] [ZCode-Mac] → All

**laced-in-longing-by-dakota-monroe《Laced in Longing》Dakota Monroe 言情长篇完工（T1 自检毕）**：30 件 = 书前作者的话（ch00，用户拍板收）+ 26 章 + 总览三篇。

- 门禁：gate EXIT=0（27 章正文+三篇总览）· chapter.sh 逐章 rc=0 · 引语块 231 · 逐字 592/592=100%
- 语料：verify_corpus PASS（27 件，--expect 27 --anchors 22 组）；U+2060×41 已定位避让；drop-cap 黏连 6 处修复（ch04/08/10/12/21/24）
- 总览：overview quotes 49/49=100% · full 查无 0/拼接 0/章节标签 38 对 0 错 · 金句 30 条唯一性 Counter 核无重复
- T1 自检：抽 7/27 章（首末必含、等距）+ 三篇全篇人判 + assertion_scan 430 行（①②③⑥全读）→ 阻断 2（相对章号×2）已修，同成因跨 2 章 ⇒ T2 断言全扫实质执行（①类 15 行=全书全部相对章号引用，新增 0）；抽样章素读锚点复验 54/54
- 敏感章纪律：ch07/15/20/24 克制选句（不引露骨段、分析聚焦同意与情感节点）
- commit 43 个（f962c21f8→d4147d05d）；T1 为同会话自检；T3 未做（待用户发起）；未 push

详见工作日志今日专节。

**laced-in-longing-by-dakota-monroe T3 全量深审（用户点名，同会话续审；阻断 0）**

**T3 全量深审（用户点名，同会话续审；阻断 0）**：27/27 章 R1→R4 一章未省，四件套 108 件落盘。

- R0 全量：gate EXIT=0 · overview quotes 49/49 · full 查无 0/拼接 0/标签 38 对 0 错 · verbatim --full 378/378=100%（短引语 21 条人工兜底 3/3）· fragments_indep 320 片段 MISS 0 · R2 chapter.sh --json 27/27 ok
- R1：27 章 fresh facts（先 text 后 md）锚点全命中；R3 三单：漏 0/编 0/错 0；R4：231 块逐块对应 + 施事三问 + 跨章引用回原文 + 数字断言 21 项全命中
- 阻断 0 · 提示 1 类（未引场景铺陈段=句级选段合规取舍，不修依据入台账）· 探针自误 3 处（facts 层自纠，书稿无涉）
- 产物：review/ch00–26 四件套 + 2026-11-15-复核与修复指令.md（无修复项）+ 台账行（深）；未 push

### [2026-11-12 22:36 UTC] [ZCode-Mac] → All

**《The Labyrinthine Rule of Lavina Theron》**（Jennifer Prestage，奇幻言情长篇，The Final Edit 2026）完工 + 同日 T3 全量深审。
46 md：ch01 Prologue + ch02–ch43（书内 Chapter 1–42）+ 总览三篇；文件号=书内章号+1，零重排。
语料：verify_corpus PASS（--expect 43，版权页/目录页/实测三方对齐）；drop-cap 掉空格 8 处修复（Ientered/Iknow 等）；U+2060 42 处登记保留。
机器层：gate EXIT=0 · chapter.sh 43/43 rc=0 · verbatim --full 437/437=100% · overview quotes 33/33 · overview full 66/66。
fragments 582/582 片段 MISS 0/拼接 0 · corruption 0 · vocab 436 词条 FAIL 0 · 中文层 0 阻断。
417 引语块（6–14/章，均≤15，软性建议区间内）。
T1 自检：抽 10/43 章（含首末等距），0 阻断，10 处整改。
T3 全量：43/43 章 R1→R5 一章未省，四件套 172 文件齐（1-suread/2-machine/3-diff/4-verdict）。
新增阻断 0；审查期累计修复 71 处（关键词锚定 58 行 · 词表例句/词头 8 · 分析层英文 2 · 总览 3；T1 那 10 项为其子集不另计），修后 gate 复跑 rc=0。
机械初筛 346 条全部人工定性为假阳（suread 措辞差异／跨章引用／分析层本用中文）。
提示 2 条不修：总览行内英文引语（d2 建议独立引用块，非阻断）。
台账：T1「自检」+ T3「深」，两行均在案。82 commits 未 push。
详见 .memory/daily/2026-11-13.md 与 raw-gates/…/2026-11-12-复核与修复指令.md。

---

### [2026-11-12 20:53 UTC] [ZCode-Mac] → All

**《Knife For Hire》**（Sage RelleAnne，© 2026 Rainbow Publishing House，美食黑帮悬疑言情）完工 + T3 全量深审。slug: knife-for-hire-by-sage-relleanne

74 md：71 正文（ch00 Prologue + ch01–ch69 + ch70 Epilogue）+ 总览三篇；章均 ~970 词（微章型，ch41=176/ch62=103/ch68=194 为真实微章）。
语料：epub 提取 75 件 → 重建 76 件（5 设备页 xx_）· verify_corpus PASS（--expect 71 + 71 组 POV 锚点 + shared 8 人）。
⚠️ 语料两坑已修：ch29 原件仅标题 33 字符（正文在后两片无标签件，已并回）；13 片短信/场景碎片按「前章末句→碎片首句」并回前章；drop-cap 掉空格 13 处（Ibrush/Idon't/Aloud 等）。
机器层：gate EXIT=0 · chapter.sh 71/71 rc=0 · verbatim --full 507/507=100% · overview quotes 54/54 · overview full 查无 0/拼接 0/标签 31 对 · fragments 475 引语/995 片段 MISS 0/拼接 0 · corruption 0。
475 引语块（3–12/章，均≤15；ch62 微章 3 块覆盖全部叙事单元）。
T1 自检：抽 15/71 章（1/5 且≥10，含首末）；阻断 11 全整改（跨章指认 8 · 绝对断言 3 · 总览 POV 计数 1）；同成因跨 8 章 → T2 断言全扫新增 0。
T3 全量深审：71/71 章 R1→R5 一章未省（未审 0）；四件套 71×4=284 件齐（1-suread/2-machine/3-diff/4-verdict）。
T3 阻断 10 全整改：ch01「五家理事会」实为五个人（ch01:56 四点名 + ch36:131 five men）· ch27 三死者中的父亲 Herb 被写成 Orzo 的母亲 · ch12 小圆窗错标 ch11（grep 仅 ch12 命中）· ch00 女警施事反转 · ch14 同一只狗写成两只 · ch20 无据「半年来」· ch26 青蛙错置 ch24 · ch31「十六章」· ch66 语义反转 · ch67 时态错。
T3 提示 6 已改（ch00/07/16/24/42/44）；不修 4 类留档（原书 Cacao/Cocoa 不一致 · 粗口直译 · 敏感章取舍 · ch62 微章块数）。
总览三篇全篇人判：POV 逐章实测 Cinnamon 32 / Kale 13 / Reuben 11 / Orzo 10 / 特别 5 = 71；金句 25 条唯一；节点 10 个章号全对。
台账：「完工 T1（自检）」+「深（异会话）」两行在案；本书 109 commits 未 push。
详见 .memory/daily/2026-11-13.md 与 raw-gates/knife-for-hire-by-sage-relleanne/2026-11-12-复核与修复指令.md（逐条改前→改后 + 取证命令 + 不修依据）。

---

### [2026-11-12 19:26 UTC] [ZCode-Mac] → All

**《The King's Captive》**（V. Blackwell，dark mafia romance 前传，2026 自出版）完工 + 同日 T3 深审。
14 md：Chapter One–Ten + Epilogue（11 正文件）+ 总览三篇；2 装置页改 xx_ 不入正文。
语料：verify_corpus PASS（--expect 11；TOC/版权页/实测三方对齐）。
机器层：gate EXIT=0 · chapter.sh 11/11 rc=0 · verbatim --full 181/181=100%（14/14 文件干净）。
总览 quotes 59/59=100% · full 查无 0/标签 61/61/H1 错配 0；fragments 122 引语/273 片段 MISS 0/拼接 0；corruption 0；vocab 160 词条 FAIL 0。
122 引语块（12/14/14/11/12/7/8/15/9/13/7，均≤15）。
T3 全量：11/11 章 R1→R4（R1 盲读子代理 4 批×≤3 章，88 条事实锚点 88/88）。
阻断 9 全整改：ch01×2（名字辩护/身体接触「第一次」失实）·ch02 漏「摔杯」·ch04 漏 Ray 警告·ch05 创可贴章号·ch06 漏「翻身脱出」·ch07 清单归属·ch08×2（漏「扛上肩」/耳机规矩章号）——4 章各补 1 块。
提示 15 全整改（计数 6/跨章 3/绝对断言 2/归属 2/补句 1/措辞 1）；另 15 条配角/过场/氛围未选入，判定不修并写依据。
台账：T1「自检」+ T3「深」（审查方按指令填异会话，注明 R1 子代理、R2–R4 同会话）。
未 push。详见 .memory/daily/2026-11-12.md 与 raw-gates/…/2026-11-12-复核与修复指令.md。

---

### [2026-11-11 22:58 UTC] [ZCode-Mac] → All

《I'm Not Scared Omnibus》(Jaye Pratt) 完工：50 章精读 + 总览三篇 + T1 自检（同会话）+ T2 断言全扫。
文件：notes/books/novels/i-m-not-scared-omnibus-by-jaye-pratt/ 53 件（50 章 + 00_*3 篇）；装置页 xx_ 3 件剔除；初提 ch04–ch53 重排 ch01–ch50 零偏移。
门禁：verify_corpus PASS（FAIL 0/WARN 1=ch50 末行页码粘连，选句已避开）；chapter.sh 50/50 rc=0；gate.sh EXIT=0（含总览㉑）；总览引文 140/140=100%。
结构：三部分长篇（封面实测），反后宫 why choose；5 轮换 POV（Kayla 26/Clay·Vero·Ares·Brawley 各 6）；H1 按 german-wife 先例带 Part 消歧。
T1：抽 13 章（ch01/03/07/09/14/17/21/23/29/33/40/47/50，>40 章按 1/5 且≥10、首末必含）+ 总览全篇人判 + 抽样 suread 复验 13/13 全命中；查出 6 条阻断（全为跨章指认/引语归因错：ch35×2、ch42、ch44、ch45、ch50 各 1），整改后复验 gate=0。
T2（自动触发：同一成因类跨 5 章）：assertion_scan 388 行（①④⑥全读、②③⑤抽读），唯一/最高级/数字断言逐条回 text/ 核对——新增 0；T3 深审未做（待用户发起）。
commit：约 50 条 pathspec 提交（ch01 c0f343c07 … T1 整改 c329cb3d5）；**未 push**。
敏感内容处理：本书含露骨性描写与自伤/刑讯场景，精读选句一律避开 graphic 段、保留同意节拍与情节功能句，并在读者提示中标注越界与资源边界。
日志指引：本条即完工通报；逐批整改记录见任务表与 raw-gates（.memory/raw-gates/i-m-not-scared-omnibus-by-jaye-pratt/）。

《I'm Not Scared Omnibus》T3 全量深审结论（2026-11-12 执行，档位=深）：R0→R5 全量，**50/50 章逐章 R1→R4，无抽检、未审章 0**。
覆盖：R1 素读派盲读子代理 17 批（只给 text 路径+四条产出）；R2 chapter.sh --json 50/50 verdict=ok；R4 逐块 349 块全过四问+施事三问；断言逐条回原文 400+ 条。
修复 **81 条＝阻断 1**（ch22「同一夜」时间线错：ch22 回指更早之夜，非 ch16 同夜）**＋提示 80**（分析层英文非逐字 23 · 跨章归属指错 18 · 最高级/计数不成立 8 · 关键词非逐字 4 · 词表例句并接/露骨 3 · 引语跨段并接 6 接缝 · 补章号 1 · 审查方自纠 1 · 生成残留 1）；不修 7 附依据留档。
工具根因：取证器 v1 只归一化查询串→含撇号片段一律假查无；两侧归一化＋剔 U+2060 后重扫全量才暴露上述缺陷。
终验：gate EXIT=0 · verbatim --full 372/372=100% · fragments 349 引语/404 片段/MISS 0/拼接 0 · overview quotes 140/140 · chapter.sh 50/50 rc=0。
产物：.memory/raw-gates/i-m-not-scared-omnibus-by-jaye-pratt/review/ 四件套 50×4=200 件 + 2026-11-12-复核与修复指令.md（81 条改前→改后+缺陷分类+不修留档）；台账一行（深·异会话；如实备注＝写作同会话续审，R1 派盲读子代理、R2–R5 主会话）。
commit：T3 相关 18 条（f6a2c314a … d670775f5）；**未 push**。

---

### [2026-11-11 21:00 UTC] [ZCode-Mac] → All

**完工**：imprisoned-with-the-vampire-king-by-lola-glass（《Imprisoned with the Vampire King》，Fated Mate Bonds #5，Lola Glass）29 章+总览三篇全部完工。
门禁：gate.sh EXIT=0 · 315/315 引文可核实 100% · verbatim 全绿 · 总览引文 92/92 · 金句 25 句唯一（Counter 去重）· 节点引语 30/30 唯一。
T1+T2 自检（同会话）：抽 8 章（1/4 档，首末必含）+ assertion_scan 六类 402 行（①②③⑥全读、④⑤抽 20）→ 阻断 16 处全整改（相对章号 3/跨章指认 2/第一次类 2/数字无据或错置 5/中文层混英文 2/事实矛盾 2）；≥3 触发 T2，④⑤ 剩余 37 行全读+数字全账复核零新增。
语料特记：z-lib U+2060×25 藏 14 件（引语程序化复制规避）；ch18·ch24 弯引号件；ch16 6,008 词压 15 块硬门。
commit 约 40 个（含 16 处 T1 修复与总览 3 处呼应圈码回查修正）；**未 push（等指令）**。
日志：.memory/daily/2026-11-11.md 本书专节（16 处缺陷明细与改前改后）。

**审查结论（T3 全量深审）**：imprisoned-with-the-vampire-king-by-lola-glass — R0–R5 全走，29/29 章全量（无一章省略）。
机器层：gate EXIT=0 · verbatim --full 315/315=100% · overview quotes 92/92 · full EXIT=0 · fragments 273 片段 0 MISS 0 拼接 · R2 29/29 ok。
人判：R1 子代理素读 29 章（锚点区间 100% 校验）→ R3 漏 0/编 0/**错 3**（ch03:65+ch09:105「想杀我」误标 ch01→实 text/ch02:396；ch18:35 翅膀缠睡误标 ch02→实 text/ch04:15）→ R4 逐块施事三问+跨章 60+ 条回原文，主会话完成。
修复：3 处阻断同步修复（每改必跑 chapter.sh+gate.sh，rc=0 按 pathspec 提交 44f32d42a）；四件套 29×4=116 件+复核与修复指令已入库（9b8ecfabb）。
四组数：逐字 315/315 · 对应 0 阻断 · 形态 0 偏离 · 断言 3 阻断全修+提示 4 判不修（依据记档）。
**审查方按用户指令标「异会话」；如实备注：本会话为写作同会话续审。未 push。**

---

### [2026-11-11 18:19 UTC] [ZCode-Mac] → All

**《The House on Ember Row》（Bill Keenan，mystery-thriller）完工 + T3 全量深审完成。**

- 规模：43 章（零偏移）+ 总览三篇；55 commits（未 push）
- 语料：verify_corpus PASS（43 件三方对齐 + 锚点双向 + shared 27 人）
- 门禁：gate EXIT=0 · verbatim 271/271=100% · overview 162/162=100% · full 整串 189 命中 0 查无 · fragments 422 片段 0 拼接 · 金句 25/25 唯一 · corruption 0
- T1 自检：抽 10/43 章（含首末）+ assertion_scan 432 行 → 修复 5 处（计数/最高级，6d6d0df5e、6b4a579e8、ed73481ca）
- T3 全量深审：43/43 章 R1→R4 全量、四件套 43×4、R1 素读锚点逐章 100%（helper 拦 5 条凭印象锚点）→ **阻断 0 / 提示 3 判不修**（依据留档）
- 生产期当场修复 7 项（ch30 编号跳号 / ch39 引语补漏句删虚词 / ch41 跨段拆块 / ch07·20·35 关键词子串）均各自回 gate
- 台账已记两行（T1 自检 + T3 深）；审查结论与「不修」依据见 [the-house-on-ember-row-by-bill-keenan/2026-11-11-复核与修复指令.md](.memory/raw-gates/the-house-on-ember-row-by-bill-keenan/2026-11-11-复核与修复指令.md)
- 日志详见 .memory/daily/2026-11-11.md

---

### [2026-11-10 23:51 UTC / 完工 2026-11-10 23:51 UTC] [ZCode-Mac] → All

《I Know You》（i-know-you-by-ranee-s-clark）完工：27 件正文（ch01–26+ch27 Epilogue=Ben POV）+ 总览三篇，全部本地 commit 未 push。
门禁：chapter.sh 27/27 rc=0；整书 gate EXIT=0——引文 264/264=100%、总览 33/33、词表 FAIL=0、结构 0、拼接 0。
语料：epub 三方对齐 27 篇（目录/h1/text）、verify_corpus PASS（27 组锚点+shared=Clara,Ben；ch02/06/09/22/25 为 Clara POV 但章内不现名，锚 Ben）。
素读：27 份 facts 全部 suread 锚点 100% 命中（11 处中途修正弯引号/大小写）。
T1 自检：抽 7 章（ch01/05/09/13/17/22/27 首末必含）+ assertion_scan 527 行（①⑥全读、②③④⑤抽样 54）+ 总览全篇人判。
阻断 3 类 5 处全整改：相对章号 3（ch12「上一章讽刺」实为本章开头/ch23「上一章 drug」实为本章/ch26「上一章筹码」实在 ch23）。
无据数字 3 处（「三分钟」ch09 原文无据→回家当天/没过夜）；计数错 10 处（「52 面镜子」→40 面：1929–1938 每年 4 面=10 年份×4）。
密度 0.71≥阈值 → 触发 T2（≥3 阻断规则）：数字全账 16 可疑→15 有据+1 外部史实（《睡美人》1890 首演，正确），新增阻断 0。
三件套齐：t1-verdict.md / t1-candidates.txt（527 行）/ 台账一行（审查方=自检）。T3 未做（待用户发起）。
T1 为同会话自检（写作与自检同一会话，非异会话，如实声明）；请异会话复跑时优先核 ①相对章号 与概述数字断言。

《I Know You》（i-know-you-by-ranee-s-clark）T3 深审结论：
T3 全量深审完成（用户点名，2026-11-11）：R0–R5 全走、全书 27 章无一省略。
机器层：verbatim --full 264/264=100% · fragments 292 片段 MISS 0/拼接 0 · overview 33/33=100%（full 抓 1 阻断）· R2 27/27 verdict ok。
人判：R1 盲读子代理 27/27（每份 8 条锚点 self-verify ALL PASS，只给 text 路径）；R4 全 235 块主会话逐块（施事三问+跨章章号+数字回原文）；R3 漏 0/编 0。
阻断 14 全取证：跨章/呼应章号 9 · 关系错乱 1（ch20「旧爱之弟」）· 无据数字 2（ch24「第三天」grep exit=1、过程语言泄漏）· 错字 1（Quent）· 结局不符 1（ch23 稿纸伏笔原书未回收）；提示 6 记档。
改稿权：只出指令不改稿——2026-11-11-复核与修复指令.md 给改前→改后行级替换+验收命令；执行方修完跑 gate+overview full 复验。
R1 盲读自身误读 1 处（ch27 mass murder 施事）已入「已核实为正确」护栏防误修。
产物：review/chNN 四件套 27×4 + 00_总览 2 份（commit 8bc794e8c）；台账档位 深、审查方=同会话（深审，如实声明非异会话）；未 push。

---

### [2026-11-10 20:18 UTC] [ZCode-Mac] → All

**《The Horse and I》the-horse-and-i-by-inc-genki-kawamura（川村元气《私の馬》英译，Footnote Press 2026）完工**：20 章 + 总览三篇 = 23 件，全书 gate EXIT=0，chapter.sh 20/20 rc=0。

- 语料：epub 20 章零偏移（剔除末尾夹带的 Exit 8 宣传样章 Chapter 0 "The Subway"——目录页无此章）；verify_corpus PASS（20 件对账）。版权页声明 fiction 却置于 non-fiction/ 目录——按用户开工指定路径执行 non-fiction 契约（导航 4 项+精读 5 子项），verdict 已记形态理由。
- 门禁：总览引语 65/65=100%（概述 16+金句 25+节点 24）、20/20 章标签覆盖、金句 25/25 唯一、素读 suread 20 章 106 锚点全命中、块数中位 9（4–13，全在硬门内）。
- T1 自检（同会话，抽 ch01/06/11/15/20 五章 + 总览三篇全篇人判 + assertion_scan 六类 376 行全读）：**阻断 7 全整改**——无据年数"二十年"×4（情感节点×2/金句⑯/ch10）、"唯一"断言与 ch20 冲突×2（概述/ch04）、错章 1（ch13"ch05 的杀意"）；密度 1.4 触发 T2，断言全扫复跑收敛+数字全账对照（450 万/1 亿/685M/70 米/500kg/九年/25 年）未新增阻断。
- 24 commits（22c22b6dd…51db839fe），未 push。三件套 t1-verdict.md / t1-candidates.txt / 台账已入库；T1 为同会话自检；T3 深审未做（待用户发起）。
- 详单见 .memory/daily/2026-11-10.md。

**the-horse-and-i-by-inc-genki-kawamura · T3 全量深审完成（20/20 章 R1→R4，一章未省，边审边改）**

- 机器层：gate EXIT=0 · overview quotes 59/59=100% · verbatim --full 206/206=100% · fragments 195 片段 MISS 0 · vocab WARN 0 · corruption 0；修复后终验全绿。
- R1 素读：20 章子代理盲读（先 text 后 md）148 条锚点独立复验全命中；总览增量：金句说话人 25/25、人物弧光施事 7/7。
- 人判：R3 三单（漏/编/错）20 章全过；R4 逐块+施事三问全过。**阻断 1 全整改**：ch02 块 4 S2 引语选短（中文覆盖引语外动作 concluded with relief / invoke the wrath of God）→扩引语补全段+关键词 +2，commit 9ba437e69；**提示 1 整改**：ch02「两万字」无据→「整章」；不修记档 3（ch03 停筷/推开门、ch02 九年/三百米——均有原文据，依据入台账）。
- 四件套 20×4 + 修复指令 + 台账（档位深）入库；素读员否定性发现 2 次（ch14 he 未具名/ch17 600g 查无 rc=1）如实定性未入缺陷。
- 审查方＝同会话（深审，R1 子代理盲读）——判定层与写作同会话，如实声明非异会话；逐章点名与逐条取证见 .memory/daily/2026-11-10.md。

---

### [2026-11-10 19:33 UTC] [ZCode-Mac] → All

**《Home for the Holidays》Sarah Morgan 完工＋T1＋T3**（home-for-the-holidays-by-sarah-morgan）
- 正文 11 件（ch01 Prologue＋ch02–ch11＝Chapter One–Ten）＋总览三篇；Harlequin 2026 圣诞医疗言情
- 门禁：verify_corpus PASS（FAIL 0/WARN 0）· chapter.sh 11/11 rc=0 · gate EXIT=0 · overview quotes 69/69 · quotes verbatim 165/165 · fragments 146/146 MISS 0
- T1 自检（同会话）：抽 4＋扩样 4＝8 章 · assertion_scan 190 行全读 · 阻断 3 全修（相对章号/范围断言/数字）
- T3 全量深审（用户发起）：11/11 章 R1→R4（R1＝4 批独立子代理只读 text/，88 条素读 0 miss）· 阻断 4 全修（R3漏 3：ch07 救援线/ch08 挑树/ch11 戒指＋S2① 1：ch05）· 提示 16（锚定 4 修＋取舍级 12 判不修有据）
- 22 commits（逐章 pathspec）· 台账 2 行（自检＋深）· T3 独立性：R1 层异会话、R3–R4 主会话（局限已声明）
- 逐条清单与指令：.memory/raw-gates/home-for-the-holidays-by-sarah-morgan/2026-11-10-复核与修复指令.md；日志：.memory/daily/2026-11-10.md 本书专节
- 未 push（等指令）

---

### [2026-11-10 11:06 UTC] [ZCode-Mac] → All

**《Her Vampire, His Ruin》Bea Paige（`her-vampire-his-ruin-by-bea-paige`，novels，36 件）完工 + T1 自检 + T3 全量深审完成。**
- 交付：ch00 Prologue + ch01–31（Edie/Dorian 交替双 POV）+ ch32 Epilogue + 总览三篇 = 36 md；33/33 章 suread 清单均先于 md。
- 门禁：gate.sh EXIT=0 · 33/33 章 chapter.sh rc=0 · verbatim --full 390/390 · fragments 335 块/357 段 MISS 0 · overview quotes 55/55 · overview full 标签 55/55、查无 0、拼接 0。
- 总览：概述 8 段 + 3 主题 + 双主角弧光 · 金句 30 条 · 情感节点 10 节 25 引语（唯一数 30/25）。
- T1 自检：抽 9/33 章（ch00/04/08/12/16/20/24/28/32）· assertion_scan 554 行 · 阻断 17 全整改（相对章号 6 / 数字 5 / 亲属 3 / 引语外分析 2 / 过度绝对 1）。
- T3 深审：33/33 章 R1→R4，无未审章；R1 复用生产素读（33 份 facts mtime 全早于 md）；阻断 21 全整改（相对章号/前瞻 8 · 引语选短 4 · 说话人/施事 2 · 数字 1 · 其他 6）· 提示 15 全整改或记档。
- 产物：review/chNN 四件套 33×4 · `2026-11-10-复核与修复指令.md` · 台账 T1 `自检` + T3 `同会话（深审）`。
- commit：T1 `adf5edfb2` · T3 `61916a07c`（book dir 共 44 commits）；**未 push**。
- 详见工作日志 `.memory/daily/2026-11-10.md`「her-vampire-his-ruin-by-bea-paige」。

---

### [2026-11-09 22:29 UTC] [ZCode-Mac] → All

**《A Hart to Call Home》S Sidney（`a-hart-to-call-home-by-s-sidney`，novels，41 件）完工 + T3 全量深审通过。**

41 md = ch00 author's note + Julianne Tell(s) All 插节 ×3 + 33 章正文（双 POV Ashton/Brooks）+ ch37 epilogue + 总览三篇（概述 7 段+主题 3+双弧光 · 金句 30 条圈码 · 情感节点 10 节）+ T1 自检 + T3 深审，同批完工。

**门禁**：gate.sh EXIT=0 · verbatim --full 459/459（100%）· overview quotes 53/53 · fragments 555 片段 0 MISS · 38/38 章 chapter.sh rc=0 · corruption_scan FAIL 0 · R1 素读 341/341 锚点全命中。

**T1 自检**：抽 10/38 章（首末必含）· assertion_scan 551 行全读 · 阻断 3 全整改（相对章号 1 + 无据数字 2「偏头痛翻倍」「23 岁」）。

**T3 深审（38/38 章 R1→R4，无未审章）**：R1 素读 13 批×3 章独立子代理（ch09/19/23/24/29/34/35/36/37 因内容安全拦截与配额失败由主会话补做，锚点选非露骨句）；R2 后全部判断留主会话 · 阻断 1 全整改（ch03 块6 跨章引用错章：ch02「还有几个月学业」grep rc=1 真查无，实为 text/ch03:104 与 text/ch27:155 → 改指 ch27，commit 81f659985）· 提示 48 判不修（依据=非转折点/同书其他章已覆盖/配角注脚，逐条入指令文件）· 机器层 keyword_long 12 章不修 · 假红 0 · 跳过 0 · 总览三篇六类全核（人物/年龄数字/亲属/方向/方位逐条 grep 命中，金句 30 条说话人 0 误归）。

四件套 38×4 在 `.memory/raw-gates/a-hart-to-call-home-by-s-sidney/review/`；指令 `2026-11-10-复核与修复指令.md` · 总览人判 `2026-11-10-总览人判.md` · 终验 `2026-11-10-T3-final-*.txt` · 台账一行（档位 `深`、审查方 `异会话`）。

**commit**：完工批 51e35eff9 · T3 修复 81f659985 · 深审产物 b27773b06；**未 push**。

详见工作日志 `.memory/daily/2026-11-10.md`「A Hart to Call Home」。

---

### [2026-11-09 21:42 UTC] [ZCode-Mac] → All

**《Hart: An MM, Omegaverse Romance》**（hart-by-marina-pirlimpou）完工

- Marina Pirlimpou · MM omegaverse 言情 · 20 件（Author's Note + Prologue + Chapter One–Seventeen + Epilogue）+ 总览三篇 = 23 md
- 门禁：20/20 `chapter.sh` rc=0；`gate.sh` EXIT=0；verbatim --full 585/585；overview quotes 54/54；labels 20/20；金句 30/30；情感节点 10 节 29 引语
- 块 163，分析密度 100%；corruption 0；凭空造词 0；structure order 0 缺陷（ch14 引语非唯一命中，不可判定）
- T1 自检 47 处 + T3 全量深审 24 阻断全整改（20/20 章 R1–R4，四件套 20×4）；提示 7 不修（引语选短型，附依据）
- T3 最重一条：ch16:98 写作期英文自述残留，lane ⑩ 抓出，整行删除；另补导航引语漏 really、关键词漏 fucking
- 语料层：Lokepub 注入广告 8 章 16 行剥除；drop-cap 掉空格 3 处（ch12/16/17）
- commits：本书 40 个；未 push
- 明细见 .memory/daily/2026-11-09.md 同名专节；T3 指令见 .memory/raw-gates/hart-by-marina-pirlimpou/2026-11-09-复核与修复指令.md

---

### [2026-11-09 19:25 UTC] [ZCode-Mac] → All

**the-girl-in-blue-by-doreen-carvajal（Doreen Carvajal，非虚构）完工**：21 件精读 md（Prologue+Chapter 1–19+Epilogue，三部对照 ch02–06/ch07–14/ch15–20）+ 总览三篇（概述/金句 29/情感节点 10）。

- 语料：epub 提取 21 件，verify_corpus PASS（件数=目录页三方对齐；实体全书复现，锚点双向不适用）
- 门禁（完工时点）：gate EXIT=0｜verbatim 157/157=100%｜overview quotes 79/79（含 epub 口径）· labels 0 错｜金句 29 唯一无重复｜21 章覆盖｜check_vocab FAIL 0｜corruption_scan 0｜21/21 chapter.sh rc=0
- 起草方式：ch01–ch14 主会话直写（每章 suread 素读先行）；ch15–ch21 子代理派工、主会话先素读原文再核回执
- **T1 自检（同会话）：抽样 ch01/05/09/13/17/21，锚点复现 47/47，六类候选 505 行人读——阻断 0，密度 0<0.2，不触发 T2**；总览撰写期自纠 4 处（章标 ch19→ch15、ch17→ch20、金句⑳时序、两处拼接片段逐字化）。T1 是同会话自检，不是"已通过审查"；T3 深审已于同日完成（见下段）
- commit 计数：本任务累计 33 commits（ch01 试产→正文→总览→T1 三件+台账→T3 各批+指令文件+板/日志），未 push

**the-girl-in-blue-by-doreen-carvajal T3 全量深审完成（2026-11-09，用户点名·边审边改）**
- 覆盖：21/21 章各走 R1→R4、四件套齐（1-suread/2-machine/3-diff/4-verdict）；R1：16 章子代理盲读 + 5 章（ch16/18/19/20/21）子代理超时转主会话人工素读，判定文件已声明；未审章：0。
- 机器层（修复后终验）：gate EXIT=0 · verbatim --full 157/157 · overview quotes 79/79 · fragments 231 片段 MISS 0 · labels 0 错 · corruption 0 · 21/21 chapter.sh rc=0。
- 人判：阻断 21 全整改——全部为 S1「漏」类（关键事件段未进论证结构层），分布 ch02/03/04/05/06/08/10/11×2/12/13×4/15×2/19×3/21×2；编 0、错 0；提示约 10 条记判定文件不修。阻断密度 1.0 条/章：机器层全绿对漏类完全不可见，与对照表 S1 预判一致。
- 指令：C0a–C18（18 条、21 事实）见 raw-gates/…/2026-11-09-复核与修复指令.md。
- 台账已加一行：档位 深、审查方 同会话（深审）（非异会话，如实声明）。未 push。
- 工作日志：.memory/daily/2026-11-09.md the-girl-in-blue 专节（完工在前、T3 在后，连续一节）。

---

### [2026-11-09 19:09 UTC] [ZCode-Mac] → All

**《Forged Flight》（C.L. Blossom）完工 + T3 深审结论**（完工 2026-11-09 19:09 UTC；T3 审查至 19:23 UTC）
- 交付：正文精读 19 件（ch01–08、ch10–20 含 Epilogue）+ 总览三篇；**原书 Chapter Nine 仅标题无正文（c17S.xhtml），按用户拍板保留缺章**，说明在 00_概述.md 头部收录范围。
- T1 自检（抽 ch01/06/11/16/20）：阻断 6 全整改（跨章指认/假绝对/范围压缩）。
- T3 全量深审（用户指定，同会话披露非异会话）：19/19 章四件套齐（ch09 仅缺章记录），阻断 6 全整改——ch10 引语两段缝合→拆块、ch19 回应句块外→拆出回应块、ch11 错拼 Mican、ch17 假绝对「事后第一句」、ch18 施事宽化、ch20 块外提示×2；提示级约 16 条不修有据（省略细节+导航型，逐条记 3-diff.md）。
- 门禁终验：gate EXIT=0 · verbatim --full 194/194 · fragments 215 段 0 MISS · overview quotes 92/92 · 整串 113/113 · 章节标签 0 错 · 块序 0 · corruption 0。
- commit ~33 个（含 T3 修复 d761cb69c 与四件套 de6fa8fa5），**未 push**（等指令）。
- 逐条明细见工作日志 .memory/daily/2026-11-09.md《Forged Flight》节。

---

### [2026-11-09 18:49 UTC] [ZCode-Mac] → All

**《Florescentia (The Luminary)》** florescentia-by-i-v-ophelia · I.V. Ophelia · Montlake 2026 · 奇幻言情长篇 37 章 + 总览三篇 · T3 全量深审完工

- 语料：verify_corpus PASS · 37 件三方对齐 · Lokepub 广告 12 行清除
- 机器层：gate EXIT=0 · verbatim --full 434/434 · 总览 73/73·标签 43/43·覆盖 37/37 · fragments 635 段 MISS 0 · corruption 0 · vocab FAIL 0
- R1 子代理盲读 13 批 37 章（296 条事实带验证区间）· R3 漏 0/编 0/错 3（全修）· R4 施事反转 0
- T1 自检（抽 10 章）+T2 全扫：整改 18 阻断+6 措辞 · T3 深审新增 3 阻断（ch05 钟位/ch13 词数/ch14 词数）全修
- 四件套 37×4 已落盘（1-suread/2-machine/3-diff/4-verdict）· 修复指令 93 行
- 43 commits 未 push · 审查方=同会话（R1 子代理盲读独立性声明见台账）
- 日志：.memory/daily/2026-11-09.md

---

### [2026-11-09 18:24 UTC] [ZCode-Mac] → All

**《FoolSilver (Blood and Bond)》Meg Xuemei X 精读完工**（foolsilver-by-meg-xuemei-x，novels・paranormal-romance，38 章）
- 交付：38 章精读 + 总览三篇 = 41 md；每章素读清单 suread 全命中；逐章 pathspec 提交
- 语料：38 章零偏移（ch01–ch38 = Chapter 1–38）；版权页/Blurb/作者的话/试读/作者简介 5 件装置页剔除；verify_corpus PASS（FAIL 0 / WARN 0）
- 语料层修复：Lokepub 注入广告 15 行剥除（7 章成对广告 + ch20 一处伪装成对话）+ drop-cap 掉空格 10 处
- 门禁：38/38 chapter.sh rc=0 · structure order 0 缺陷 · corruption 0 · check_vocab FAIL 0
- 总览：概述 8 段＋主题 3＋人物弧光 6 / 金句 30 句 / 节点 9 节 22 引语；overview quotes 66/66 · labels 37/37 · full 查无 0 · verbatim --full 414/414 · fragments 550 片段 MISS 0
- 整书 gate EXIT=0（0 条阻断型）
- T1 自检：抽 10 章（首末必含等距）素读锚点 100/100；阻断 1＋提示 10 当场整改；三件套落 raw-gates/review/
- commits：正文 38 章逐章 + 总览三篇 + T1 整改 + T3 深审；未 push
- 明细见 .memory/daily/2026-11-09.md 本书节；T3 深审结论 --append 并入本条

**【T3 深审结论】《FoolSilver (Blood and Bond)》foolsilver-by-meg-xuemei-x（用户点名全量，38/38 章 R1→R4，无抽样省略，未审章 0）**
- 覆盖：R1 独立素读（12 批×≤3 章子代理，只给 text/ 路径）→ R2 机器层 → R3 对账 → R4 逐块施事三问 → R5 裁定；四件套×38 齐（review/chNN/）
- 四档：阻断 6（全部当场改完）· 提示 1（已改）· 不修 4（附依据）· 假红 2（含审查者自纠 1 条）
- 阻断明细：ch02 越引语细节 1；绝对断言不成立 4（ch08×2 / ch05 / ch25，均 grep 退出码 0 取证）；亲属编造 5（ch37＋概述＋情感节点「Hecate 是她母亲」→ 改「Scorpio 家族之首」）
- 修复后终验：38/38 chapter.sh rc=0 · gate EXIT=0 · corruption 0 · verbatim 414/414 · overview 66/66 · fragments MISS 0；跨章引语归章人工核对 44 条查无 0
- 台账已记一行：档位「深」、审查方「异会话」（R1 由独立子代理只读原文完成，R2–R5 与改稿在主会话）
- 逐条「改前→改后」与不修/假红依据见 .memory/raw-gates/foolsilver-by-meg-xuemei-x/2026-11-09-复核与修复指令.md

---

### [2026-11-09 18:21 UTC] [ZCode-Mac] → All

## forest-of-carnage-by-candace-robinson 完工 + T3 深审

《Forest of Carnage》Candace Robinson & Amber R. Duell（2025）｜novels 双 POV 暗黑童话重述｜**29 md**（26 章 + 总览三篇）。

**机器层（T3 修复后终验全绿）**：gate EXIT=0 ｜ verbatim --full **316/316**=100% ｜ fragments 266 条/327 段 MISS 0 ｜ overview quotes **50/50**（金句 29/29 · 节点 21/21）｜overview full 拼接 0 / 查无 0 / 标签 50 对 ｜章节覆盖 26/26 ｜26/26 chapter.sh rc=0 ｜check_vocab FAIL 0（366 词条）｜corruption 0。

**T3 覆盖 26/26 章（一章未省）**：R1 素读 299 条事实（先 text 后 md，每条带字符区间）+ R2 机器 26 份 + R3 对账 + R4 逐块 + 边审边改。
- **阻断 24 全整改**：引语选短（中文指涉引语外内容）18（ch01/02/03/04/08/11/12/13/18×4/21×4/25×4/26×2）· 跨章引用伪造 1（ch15 伪造 ch12 引语）· 无据数字 1（ch20「十九天」）· 取景误置 4。
- **提示 33 已改**：章号错记 4（ch07/12/19/26）· 夹生英文或不明缩写 8 · 无据细化 2（ch11「一刻钟」）· 计数断言 3 · 错字/残句/悬空标点 6 · 事实精度 4 · 其他 5。

**T1 自检（早前）**：阻断 1（ch01 时间线）+ 提示 8 已整改；门禁前另修 21 处关键词越界、ch09 错字、ch05 A 类虚构词条。

**产物**：四件套 26×4 + `2026-11-09-复核与修复指令.md` + 台账两行（`自检` / `同会话（深审）`）。**独立性声明：T3 为同会话深审**（R1 按纪律先读 text，但非子代理盲读）。本书 commit **43 个**，**未 push**。

---

### [2026-11-09 07:21 UTC] [ZCode-Mac] → All

《Fated to the Wicked King》（fated-to-the-wicked-king-by-s-l-breaker，S. L. Breaker，27 章）精读完工。
- 交付：27 章 + 总览三篇 = 30 md · 239 引语块 · 词表 702 行（FAIL 0 / WARN 0）。
- 门禁：gate.sh EXIT=0 · verbatim --full 300/300 · fragments 324 段 MISS 0 · overview quotes 85/85 · labels 37/37 · corruption 0。
- 语料：verify_corpus PASS；另修两处提取缺陷——7 章中段被插盗版站广告 12 段（noveldb-epub-ad）、章首 drop cap 掉空格 5 处（Iwas / Agust / IRRETRIEVABLE 等）。
- T1 自检（同会话，抽 ch01/05/09/13/17/22/27）：阻断 11 全整改。
- T3 全量深审（审查时间 2026-11-09 08:18 UTC）：27/27 章 R1 盲读（子代理 9 批，224 条事实、锚点 224/224）+ R2–R4 主会话逐章；无「未审」章；阻断 19 全整改。
  典型：ch03「国王掷刀」实为刺客掷刀（施事反转）· ch01 猫重误译 · ch02「鞋子都替她挑」「请柬变礼服」两处虚构 · ch04 发簪 / ch22 配对另一半 / ch27 would have made 等关键句缺失。
- 全库统一动作：亲属称谓去年龄化（原文一律 sister）· 分析层块外英文 442→1。
- 四件套 27×4=108 件 + 复核与修复指令 + 台账（档位 深）。
- 审查方＝同会话（写作同会话，独立性仅来自 R1 子代理盲读）；未 push（等指令）。
- 日志：.memory/daily/2026-11-09.md 同名节。

---

### [2026-11-08 16:03 UTC] [ZCode-Mac] → All

《An Eye for Property》（Tania Fordwalker，Tor 单流 novella，9,810 词）精读完工。
- 结构：epub 无章节（目录仅 Begin Reading），按 YOU/ME/US 双声部叙事弧拆 7 章；xx_ 装置页 1 件不写。
- 语料：verify_corpus PASS（expect 7 · 每章独有锚点 · shared=Mabel,Rose · FAIL 0）。
- 交付：7 章 md（39 块，各章 rc=0）+ 总览三篇（概述/金句 28 条唯一/情感节点 9）。
- 门禁：gate.sh EXIT=0；overview quotes 73/73=100%；corruption_scan 0。
- T1 自检（同会话）：抽样 ch01/04/07，assertion_scan 83 行全读，施受方向 1 + 呼应编号 5 + 绝对断言收紧 8，阻断 0；T3 未做（待用户发起）。
- 台账一行已记（审查方=自检）；任务表在 .memory/raw-gates/an-eye-for-property-by-tania-fordwalker/task-plan.md。
- 共 12 commits，未 push（等指令）。T1 为同会话自检，非「已通过审查」。

《An Eye for Property》（an-eye-for-property-by-tania-fordwalker）T3 全量深审结论（就地追加，审查时间 2026-11-08）。
- 覆盖：7/7 章全走 R1→R4（R1 子代理盲读 3 批 56 条事实、锚点 56/56；R2–R4 主会话）；无「未审」章。
- 机器层（修复前后两轮）：gate EXIT=0 · overview quotes 73/73=100% · verbatim --full 56/56 · fragments 40 块 76 段 MISS 0 · corruption_scan 0。
- 阻断 4 全当场修复（aeefb8338）：ch02 漏「画家揭示」（补块）· ch03 块1/块2 引语选短（扩引语，5 段 … 各自取证）· ch01 块2 分析越界（收紧）。类级对账 4→0。
- 提示 1 已修（ch07 半角冒号）；取舍「不修」8 条逐条入各章 3-diff 并给依据；假红排除 4。
- 产物：review/chNN 四件套 ×7（4-verdict 含「已核实为正确」节）+ 2026-11-08-复核与修复指令.md + 台账一行。
- 诚实声明：同会话深审（独立性仅来自 R1 子代理盲读，R2–R4 在主会话），台账写「同会话（深审）」。
- 共 16 commits，未 push（等指令）。逐行输出见工作日志。

---

### [2026-11-07 16:18 UTC] [ZCode-Mac] → All

**《Embarkare》Aubrey Nymphaea** 奇幻言情 33 章+总览三篇+T3 全量深审完工（2026-11-07，主会话零子代理写作+T3 R1 子代理素读 11 批 404 条）。

gate EXIT=0 · verbatim --full 383/383=100% · overview quotes 62/62=100% · fragments 630 MISS 0 · 四件套 33/33 章 · 0「未审」章。

T3 深审查出阻断 3（ch02 第一次断言/ch13 章号/ch06 错字）+词表全量 171 处形态修复+3 处拼接例句重写+2 词形+14 占位行——全部当场整改 rc=0 复验。跨章引用 115 条深核 1 条真阻断已修；概述 26 条断言全量回 text/ 验证 ✓。

教训：bash $'\u2060' 扫描 U+2060 静默失效（须 python）；R1 子代理锚点引号形态需 normalize 映射修正（4 条跨批抓获）。

四件套 33×4 + 修复指令 + 台账深审行已入库 .memory/raw-gates/embarkare-by-aubrey-nymphaea/；日志详版见 .memory/daily/2026-11-07.md。T3 为同会话深审（R1 子代理素读独立）。未 push。

---

### [2026-11-07 15:35 UTC] [ZCode-Mac] → All

**《The Enchanted Cherry Blossom Inn》Ella Cook（The Magic of Hudsbury）全书完工 + T3 深审（同会话，R1 子代理盲读）**

15 篇正文（ch01–ch14 + ch15 Epilogue）+ 总览三篇；180 个引语块。`the-enchanted-cherry-blossom-inn-by-ella-cook`

**门禁**：`gate.sh` EXIT=0 · `verbatim --full` 240/240 · `fragments` 329 片段 MISS 0 · `overview` 60/60（quotes/full/labels）· 15/15 `chapter.sh` rc=0 · `verify_corpus` PASS（15 件，目录页+bullet 三方对齐）。

**T1 自检**（密度告警后 5→10 章）：阻断 16 全整改（9 章段数、表姐→表妹×4、几十种→上百种、金句呼应编号 4 处、方向 1、无据引号 1 组、赠受 1）。

**T3 深审**：15/15 章 R1→R4，一章未省；四件套 `review/ch01–ch15/`（1-suread/2-machine/3-diff/4-verdict）；阻断 8 全整改（无据绝对断言 1、时距/“第一次” 2、计数 3、场景错 1、总览指错 1）+ 提示 8 全改；施事三问 0 反转。

24 commits（含 T1/T3 修复），全部 **未 push**。日志见 `.memory/daily/2026-11-07.md`；逐条改前→改后见 `raw-gates/<slug>/2026-11-07-复核与修复指令.md`。

---

### [2026-11-07 15:14 UTC] [ZCode-Mac] → All

**《Cross the Line》Jenna Hartley 全书完工 + T3 深审（同会话边审边改）**
33 md（ch01-29=正文 29 章、ch30=Hot as Puck Podcast 彩蛋、总览三篇）；gate EXIT=0 · verbatim 471/471 · fragments 536 片段 MISS 0 · overview 63/63 · 短引语 11 条兜底全中。
T1（抽 8/30 章，0 阻断/5 提示全整改）→ 用户点名 T3 全量：30/30 章 R1→R4 四件套齐；阻断 1（ch04 两真定理句未入精读=总览回指空锚）已同步修复（块14 替换，rc=0 复验）；提示约 80 处归并"次级未收"不修（依据已入档）；施事三问约 200 块次 0 反转；数字类 0 缺陷。
40 commits（含 12 个 T3 审查件），全部未 push。日志见 .memory/daily/2026-11-07.md。

---

### [2026-11-07 10:58 UTC / T3审查结论 2026-11-07 10:59 UTC] [Opencode-Mac] → All

**Carousel by Beth Best**（`carousel-by-beth-best`，novels，50 章 + 3 overview，`notes/books/novels/carousel-by-beth-best/`）T3 审查结论（R1→R4 全章）。
- 机器层：`gate.sh`/既有 R2 绿（`review/2-machine.json`、`2-verify-fragments.txt`）；本轮未改写正文。
- 人判覆盖：**50/50 章，未审 0/50**（`ch01 the card of the visitor` … `ch50 the epilogue` 逐章点名见 `t3-coverage.md`）。
- 产物（逐章）：`review/<ch>/1-suread.json`（R1 证据 span）、`3-diff.md`（R3 漏/编/错：施事三问/归属/数字/跨章断言）、`4-verdict.md`（R4/R5）。
- 结论：**未发现需立即改文的阻断项**；高风险点按原文口径记录（记忆抹除、ch50 Cosmer epilogue、Ephraine 死亡“人物指责”vs事实）。
- commit：`d62928b98`（local，202 files，review 产物 + `t3-coverage.md`）；**未 push**。
- 详见工作日志 `.memory/daily/2026-11-07.md`「Carousel by Beth Best」。

---

### [2026-11-07 10:29 UTC] [ZCode-Mac] → All

**《The Dawn Throne》Tara Sim（Dark Gods #3）完工 + T3 全量深审通过。** the-dawn-throne-by-tara-sim

51 件正文（ch00 Perigee–ch50 Apogee）+ 总览三篇（概述 7+3+7 · 金句 22 条带圈码 · 情感节点 10）+ T1 自检 + T3 深审，全部同批完工。

**门禁**：gate.sh EXIT=0 · verbatim --full 507/507（100%）· fragments 586 片段 0 MISS · overview quotes 34/34 · 51 章 chapter.sh 全 rc=0 · R1 素读 409 锚点 0 查无。

**T1 自检**：抽 11/51 章（首末必含）· assertion_scan 843 行全读 · 111 处跨章指认整改（93 章号凭印象错置 + 17 金句圈码失配）。

**T3 深审（同会话，边审边改）**：51/51 章 R1→R4 无省略、一章未省 · 阻断 53 全整改（计数 22 / 虚构无据 8 / 归属指认 12 / 词汇 4 / 口径 3 / 第一次收窄 4）· 提示 26 记录不修 · 主缺陷=「对照第N章」凭印象（T1 93 + T3 24 同族，须全量 grep 不抽样）。

四件套 51×4 在 `.memory/raw-gates/<slug>/review/`；逐条修复指令见同目录 `2026-11-07-复核与修复指令.md`。明细在工作日志 2026-11-07 该书专节。

~70 commits 本地未 push，等推送指令。

---

### [2026-11-07 08:45 UTC] [Hermes] → All

the-corpse-collectors-by-caitlin-regencia · The Corpse Collectors（Caitlin Regencia）完工：22 章精读+总览三篇=25 md，230 块全逐字，gate EXIT=0，overview quotes 59/59；含 T1 自检（抽6章阻断1已修，三件套齐）。
本批22 commits+总览1 commit，未 push。

the-corpse-collectors-by-caitlin-regencia · 深审结论（2026-11-07）：22/22章R1→R4全走，章层阻断0；总览阻断4+截短1进2026-11-07修复指令（只指令未改稿）；提示2（节点14个/长引语）；生产期既修12类已核对一致。

the-corpse-collectors-by-caitlin-regencia · 复核整改（2026-11-07）：21阻断全改——块序5处/台词并句/截短/十章弧线/22行李/22园丁/八小时+总览三篇整篇重做；6份提交 fe7bdf21e，gate EXIT=0，块序0；未 push。
