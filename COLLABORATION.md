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

> **📁 历史归档**：[ARCHIVE_260905.md](docs/COLLABORATION_ARCHIVE_260905.md)（2026-08-10~09-03）· [ARCHIVE_260909.md](docs/COLLABORATION_ARCHIVE_260909.md)（09-04~09-09）· [ARCHIVE_260915.md](docs/COLLABORATION_ARCHIVE_260915.md)（09-10~09-15）· [ARCHIVE_260921.md](docs/COLLABORATION_ARCHIVE_260921.md)（09-16~09-21）· [ARCHIVE_260923.md](docs/COLLABORATION_ARCHIVE_260923.md)（09-22~09-23）· [ARCHIVE_260926.md](docs/COLLABORATION_ARCHIVE_260926.md)（09-24~09-26）· [ARCHIVE_260928.md](docs/COLLABORATION_ARCHIVE_260928.md)（09-27~09-28）· [ARCHIVE_261003.md](docs/COLLABORATION_ARCHIVE_261003.md)（09-29~10-03）· [ARCHIVE_261007.md](docs/COLLABORATION_ARCHIVE_261007.md)（10-04~10-09）· [ARCHIVE_261016.md](docs/COLLABORATION_ARCHIVE_261016.md)（10-10~10-16）· [ARCHIVE_261024.md](docs/COLLABORATION_ARCHIVE_261024.md)（10-17~10-24）· [ARCHIVE_261031.md](docs/COLLABORATION_ARCHIVE_261031.md)（10-25~10-31）· [📄 归档说明与操作规范](docs/COLLABORATION_ARCHIVE_README.md)

> **排序规则**：消息按**最新到最旧**排列（newest first，顶部是最新的协作记录）。时间戳统一使用 UTC，格式 `YYYY-MM-DD HH:MM UTC`。新消息插到下方 `---

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

### [2026-11-10 19:33 UTC] [ZCode-Mac] → All

**《Home for the Holidays》Sarah Morgan 完工＋T1＋T3**（home-for-the-holidays-by-sarah-morgan）
- 正文 11 件（ch01 Prologue＋ch02–ch11＝Chapter One–Ten）＋总览三篇；Harlequin 2026 圣诞医疗言情
- 门禁：verify_corpus PASS（FAIL 0/WARN 0）· chapter.sh 11/11 rc=0 · gate EXIT=0 · overview quotes 69/69 · quotes verbatim 165/165 · fragments 146/146 MISS 0
- T1 自检（同会话）：抽 4＋扩样 4＝8 章 · assertion_scan 190 行全读 · 阻断 3 全修（相对章号/范围断言/数字）
- T3 全量深审（用户发起）：11/11 章 R1→R4（R1＝4 批独立子代理只读 text/，88 条素读 0 miss）· 阻断 4 全修（R3漏 3：ch07 救援线/ch08 挑树/ch11 戒指＋S2① 1：ch05）· 提示 16（锚定 4 修＋取舍级 12 判不修有据）
- 22 commits（逐章 pathspec）· 台账 2 行（自检＋深）· T3 独立性：R1 层异会话、R3–R4 主会话（局限已声明）
- 逐条清单与指令：.memory/raw-gates/home-for-the-holidays-by-sarah-morgan/2026-11-10-复核与修复指令.md；日志：.memory/daily/2026-11-10.md 本书专节
- 未 push（等指令）

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

### [2026-11-09 22:29 UTC] [ZCode-Mac] → All

**《A Hart to Call Home》S Sidney（`a-hart-to-call-home-by-s-sidney`，novels，41 件）完工 + T3 全量深审通过。**

41 md = ch00 author's note + Julianne Tell(s) All 插节 ×3 + 33 章正文（双 POV Ashton/Brooks）+ ch37 epilogue + 总览三篇（概述 7 段+主题 3+双弧光 · 金句 30 条圈码 · 情感节点 10 节）+ T1 自检 + T3 深审，同批完工。

**门禁**：gate.sh EXIT=0 · verbatim --full 459/459（100%）· overview quotes 53/53 · fragments 555 片段 0 MISS · 38/38 章 chapter.sh rc=0 · corruption_scan FAIL 0 · R1 素读 341/341 锚点全命中。

**T1 自检**：抽 10/38 章（首末必含）· assertion_scan 551 行全读 · 阻断 3 全整改（相对章号 1 + 无据数字 2「偏头痛翻倍」「23 岁」）。

**T3 深审（38/38 章 R1→R4，无未审章）**：R1 素读 13 批×3 章独立子代理（ch09/19/23/24/29/34/35/36/37 因内容安全拦截与配额失败由主会话补做，锚点选非露骨句）；R2 后全部判断留主会话 · 阻断 1 全整改（ch03 块6 跨章引用错章：ch02「还有几个月学业」grep rc=1 真查无，实为 text/ch03:104 与 text/ch27:155 → 改指 ch27，commit 81f659985）· 提示 48 判不修（依据=非转折点/同书其他章已覆盖/配角注脚，逐条入指令文件）· 机器层 keyword_long 12 章不修 · 假红 0 · 跳过 0 · 总览三篇六类全核（人物/年龄数字/亲属/方向/方位逐条 grep 命中，金句 30 条说话人 0 误归）。

四件套 38×4 在 `.memory/raw-gates/a-hart-to-call-home-by-s-sidney/review/`；指令 `2026-11-10-复核与修复指令.md` · 总览人判 `2026-11-10-总览人判.md` · 终验 `2026-11-10-T3-final-*.txt` · 台账一行（档位 `深`、审查方 `异会话`）。

**commit**：完工批 51e35eff9 · T3 修复 81f659985 · 深审产物 b27773b06；**未 push**。

详见工作日志 `.memory/daily/2026-11-10.md`「A Hart to Call Home」。

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

### [2026-11-09 19:09 UTC] [ZCode-Mac] → All

**《Forged Flight》（C.L. Blossom）完工 + T3 深审结论**（完工 2026-11-09 19:09 UTC；T3 审查至 19:23 UTC）
- 交付：正文精读 19 件（ch01–08、ch10–20 含 Epilogue）+ 总览三篇；**原书 Chapter Nine 仅标题无正文（c17S.xhtml），按用户拍板保留缺章**，说明在 00_概述.md 头部收录范围。
- T1 自检（抽 ch01/06/11/16/20）：阻断 6 全整改（跨章指认/假绝对/范围压缩）。
- T3 全量深审（用户指定，同会话披露非异会话）：19/19 章四件套齐（ch09 仅缺章记录），阻断 6 全整改——ch10 引语两段缝合→拆块、ch19 回应句块外→拆出回应块、ch11 错拼 Mican、ch17 假绝对「事后第一句」、ch18 施事宽化、ch20 块外提示×2；提示级约 16 条不修有据（省略细节+导航型，逐条记 3-diff.md）。
- 门禁终验：gate EXIT=0 · verbatim --full 194/194 · fragments 215 段 0 MISS · overview quotes 92/92 · 整串 113/113 · 章节标签 0 错 · 块序 0 · corruption 0。
- commit ~33 个（含 T3 修复 d761cb69c 与四件套 de6fa8fa5），**未 push**（等指令）。
- 逐条明细见工作日志 .memory/daily/2026-11-09.md《Forged Flight》节。

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

### [2026-11-09 18:49 UTC] [ZCode-Mac] → All

**《Florescentia (The Luminary)》** florescentia-by-i-v-ophelia · I.V. Ophelia · Montlake 2026 · 奇幻言情长篇 37 章 + 总览三篇 · T3 全量深审完工

- 语料：verify_corpus PASS · 37 件三方对齐 · Lokepub 广告 12 行清除
- 机器层：gate EXIT=0 · verbatim --full 434/434 · 总览 73/73·标签 43/43·覆盖 37/37 · fragments 635 段 MISS 0 · corruption 0 · vocab FAIL 0
- R1 子代理盲读 13 批 37 章（296 条事实带验证区间）· R3 漏 0/编 0/错 3（全修）· R4 施事反转 0
- T1 自检（抽 10 章）+T2 全扫：整改 18 阻断+6 措辞 · T3 深审新增 3 阻断（ch05 钟位/ch13 词数/ch14 词数）全修
- 四件套 37×4 已落盘（1-suread/2-machine/3-diff/4-verdict）· 修复指令 93 行
- 43 commits 未 push · 审查方=同会话（R1 子代理盲读独立性声明见台账）
- 日志：.memory/daily/2026-11-09.md

### [2026-11-09 18:21 UTC] [ZCode-Mac] → All

## forest-of-carnage-by-candace-robinson 完工 + T3 深审

《Forest of Carnage》Candace Robinson & Amber R. Duell（2025）｜novels 双 POV 暗黑童话重述｜**29 md**（26 章 + 总览三篇）。

**机器层（T3 修复后终验全绿）**：gate EXIT=0 ｜ verbatim --full **316/316**=100% ｜ fragments 266 条/327 段 MISS 0 ｜ overview quotes **50/50**（金句 29/29 · 节点 21/21）｜overview full 拼接 0 / 查无 0 / 标签 50 对 ｜章节覆盖 26/26 ｜26/26 chapter.sh rc=0 ｜check_vocab FAIL 0（366 词条）｜corruption 0。

**T3 覆盖 26/26 章（一章未省）**：R1 素读 299 条事实（先 text 后 md，每条带字符区间）+ R2 机器 26 份 + R3 对账 + R4 逐块 + 边审边改。
- **阻断 24 全整改**：引语选短（中文指涉引语外内容）18（ch01/02/03/04/08/11/12/13/18×4/21×4/25×4/26×2）· 跨章引用伪造 1（ch15 伪造 ch12 引语）· 无据数字 1（ch20「十九天」）· 取景误置 4。
- **提示 33 已改**：章号错记 4（ch07/12/19/26）· 夹生英文或不明缩写 8 · 无据细化 2（ch11「一刻钟」）· 计数断言 3 · 错字/残句/悬空标点 6 · 事实精度 4 · 其他 5。

**T1 自检（早前）**：阻断 1（ch01 时间线）+ 提示 8 已整改；门禁前另修 21 处关键词越界、ch09 错字、ch05 A 类虚构词条。

**产物**：四件套 26×4 + `2026-11-09-复核与修复指令.md` + 台账两行（`自检` / `同会话（深审）`）。**独立性声明：T3 为同会话深审**（R1 按纪律先读 text，但非子代理盲读）。本书 commit **43 个**，**未 push**。

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

### [2026-11-07 16:18 UTC] [ZCode-Mac] → All

**《Embarkare》Aubrey Nymphaea** 奇幻言情 33 章+总览三篇+T3 全量深审完工（2026-11-07，主会话零子代理写作+T3 R1 子代理素读 11 批 404 条）。

gate EXIT=0 · verbatim --full 383/383=100% · overview quotes 62/62=100% · fragments 630 MISS 0 · 四件套 33/33 章 · 0「未审」章。

T3 深审查出阻断 3（ch02 第一次断言/ch13 章号/ch06 错字）+词表全量 171 处形态修复+3 处拼接例句重写+2 词形+14 占位行——全部当场整改 rc=0 复验。跨章引用 115 条深核 1 条真阻断已修；概述 26 条断言全量回 text/ 验证 ✓。

教训：bash $'\u2060' 扫描 U+2060 静默失效（须 python）；R1 子代理锚点引号形态需 normalize 映射修正（4 条跨批抓获）。

四件套 33×4 + 修复指令 + 台账深审行已入库 .memory/raw-gates/embarkare-by-aubrey-nymphaea/；日志详版见 .memory/daily/2026-11-07.md。T3 为同会话深审（R1 子代理素读独立）。未 push。

### [2026-11-07 15:35 UTC] [ZCode-Mac] → All

**《The Enchanted Cherry Blossom Inn》Ella Cook（The Magic of Hudsbury）全书完工 + T3 深审（同会话，R1 子代理盲读）**

15 篇正文（ch01–ch14 + ch15 Epilogue）+ 总览三篇；180 个引语块。`the-enchanted-cherry-blossom-inn-by-ella-cook`

**门禁**：`gate.sh` EXIT=0 · `verbatim --full` 240/240 · `fragments` 329 片段 MISS 0 · `overview` 60/60（quotes/full/labels）· 15/15 `chapter.sh` rc=0 · `verify_corpus` PASS（15 件，目录页+bullet 三方对齐）。

**T1 自检**（密度告警后 5→10 章）：阻断 16 全整改（9 章段数、表姐→表妹×4、几十种→上百种、金句呼应编号 4 处、方向 1、无据引号 1 组、赠受 1）。

**T3 深审**：15/15 章 R1→R4，一章未省；四件套 `review/ch01–ch15/`（1-suread/2-machine/3-diff/4-verdict）；阻断 8 全整改（无据绝对断言 1、时距/“第一次” 2、计数 3、场景错 1、总览指错 1）+ 提示 8 全改；施事三问 0 反转。

24 commits（含 T1/T3 修复），全部 **未 push**。日志见 `.memory/daily/2026-11-07.md`；逐条改前→改后见 `raw-gates/<slug>/2026-11-07-复核与修复指令.md`。

### [2026-11-07 15:14 UTC] [ZCode-Mac] → All

**《Cross the Line》Jenna Hartley 全书完工 + T3 深审（同会话边审边改）**
33 md（ch01-29=正文 29 章、ch30=Hot as Puck Podcast 彩蛋、总览三篇）；gate EXIT=0 · verbatim 471/471 · fragments 536 片段 MISS 0 · overview 63/63 · 短引语 11 条兜底全中。
T1（抽 8/30 章，0 阻断/5 提示全整改）→ 用户点名 T3 全量：30/30 章 R1→R4 四件套齐；阻断 1（ch04 两真定理句未入精读=总览回指空锚）已同步修复（块14 替换，rc=0 复验）；提示约 80 处归并"次级未收"不修（依据已入档）；施事三问约 200 块次 0 反转；数字类 0 缺陷。
40 commits（含 12 个 T3 审查件），全部未 push。日志见 .memory/daily/2026-11-07.md。

### [2026-11-07 10:58 UTC / T3审查结论 2026-11-07 10:59 UTC] [Opencode-Mac] → All

**Carousel by Beth Best**（`carousel-by-beth-best`，novels，50 章 + 3 overview，`notes/books/novels/carousel-by-beth-best/`）T3 审查结论（R1→R4 全章）。
- 机器层：`gate.sh`/既有 R2 绿（`review/2-machine.json`、`2-verify-fragments.txt`）；本轮未改写正文。
- 人判覆盖：**50/50 章，未审 0/50**（`ch01 the card of the visitor` … `ch50 the epilogue` 逐章点名见 `t3-coverage.md`）。
- 产物（逐章）：`review/<ch>/1-suread.json`（R1 证据 span）、`3-diff.md`（R3 漏/编/错：施事三问/归属/数字/跨章断言）、`4-verdict.md`（R4/R5）。
- 结论：**未发现需立即改文的阻断项**；高风险点按原文口径记录（记忆抹除、ch50 Cosmer epilogue、Ephraine 死亡“人物指责”vs事实）。
- commit：`d62928b98`（local，202 files，review 产物 + `t3-coverage.md`）；**未 push**。
- 详见工作日志 `.memory/daily/2026-11-07.md`「Carousel by Beth Best」。

### [2026-11-07 10:29 UTC] [ZCode-Mac] → All

**《The Dawn Throne》Tara Sim（Dark Gods #3）完工 + T3 全量深审通过。** the-dawn-throne-by-tara-sim

51 件正文（ch00 Perigee–ch50 Apogee）+ 总览三篇（概述 7+3+7 · 金句 22 条带圈码 · 情感节点 10）+ T1 自检 + T3 深审，全部同批完工。

**门禁**：gate.sh EXIT=0 · verbatim --full 507/507（100%）· fragments 586 片段 0 MISS · overview quotes 34/34 · 51 章 chapter.sh 全 rc=0 · R1 素读 409 锚点 0 查无。

**T1 自检**：抽 11/51 章（首末必含）· assertion_scan 843 行全读 · 111 处跨章指认整改（93 章号凭印象错置 + 17 金句圈码失配）。

**T3 深审（同会话，边审边改）**：51/51 章 R1→R4 无省略、一章未省 · 阻断 53 全整改（计数 22 / 虚构无据 8 / 归属指认 12 / 词汇 4 / 口径 3 / 第一次收窄 4）· 提示 26 记录不修 · 主缺陷=「对照第N章」凭印象（T1 93 + T3 24 同族，须全量 grep 不抽样）。

四件套 51×4 在 `.memory/raw-gates/<slug>/review/`；逐条修复指令见同目录 `2026-11-07-复核与修复指令.md`。明细在工作日志 2026-11-07 该书专节。

~70 commits 本地未 push，等推送指令。

### [2026-11-07 08:45 UTC] [Hermes] → All

the-corpse-collectors-by-caitlin-regencia · The Corpse Collectors（Caitlin Regencia）完工：22 章精读+总览三篇=25 md，230 块全逐字，gate EXIT=0，overview quotes 59/59；含 T1 自检（抽6章阻断1已修，三件套齐）。
本批22 commits+总览1 commit，未 push。

the-corpse-collectors-by-caitlin-regencia · 深审结论（2026-11-07）：22/22章R1→R4全走，章层阻断0；总览阻断4+截短1进2026-11-07修复指令（只指令未改稿）；提示2（节点14个/长引语）；生产期既修12类已核对一致。

the-corpse-collectors-by-caitlin-regencia · 复核整改（2026-11-07）：21阻断全改——块序5处/台词并句/截短/十章弧线/22行李/22园丁/八小时+总览三篇整篇重做；6份提交 fe7bdf21e，gate EXIT=0，块序0；未 push。

### [2026-11-06 20:30 UTC] [ZCode-Mac] → All

《Chosen by Monsters》Texa Volt 怪兽反后宫（Summer Solstice Mates #1）完工。chosen-by-monsters-by-texa-volt

19 章正文 + 总览三篇（00_概述 / 00_金句精选 / 00_情感节点）+ T1 + T3 全量深审。
单 POV（Tara 第一人称），ch19 为 Lenart 视角首章。

**门禁**：gate.sh EXIT=0 · 引语 362/362 可核实（100%）· overview 30/30 ✅ · 块序 0 缺陷 · 凭空造词 0 · 拼接 0。
**素读**：19 章 × 8 条 suread 全中。
**T3 深审**：19/19 章 R1→R4 无省略 · 7 处结构修复（ch16 b15 缺子项+残片 · ch05 前缀+空行 · ch13 块序 · ch18 关键词截断）· 施事归属 0 反转 · 阻断 0 · 密度 0.0。
**T1 自检**：抽 7/19 章含首末（seed 42）· 0 阻断。

~30 commits 本地未 push。等待用户验收后发协作板、授权 push。

### [2026-11-06 19:45 UTC] [ZCode-Mac] → All

**《Chasing Kaylee Kringle》Codi Hall（Holiday, Idaho #1）· 54 章 + 总览三篇 · 同日 T3 深审完成**
chasing-kaylee-kringle-by-codi-hall · `notes/books/novels/` 下 57 md（54 章 + 概述/金句/情感节点）
- 形态：Prologue(ch00)+Ch1–52+Epilogue(ch53) 零偏移 · 三 POV（Kaylee/Rick + 反派插章 ch27/38/45/48）· 415 引语块
- 机器层：`gate.sh` **EXIT=0**（0 阻断/0 提示）· verbatim --full **441/441** · overview quotes **48/48** · labels **62/62** · full 0 拼接/0 查无
- 语料：verify_corpus PASS（54 件）；写作期清 z-lib 广告 19 行（6 种文案变体，11 章正文中间混入）
- T1 自检（19:45 UTC）：抽 12/54 章（首末必含、等距）+ 总览全篇 + assertion_scan 539 行 → **阻断 0**
- T3 全量深审（20:08 UTC，同会话，未派子代理）：54/54 章 R1→R4 无省略、415/415 块逐块人判
  → **阻断 22 全整改**：伪造引语开引号 5 · 跨章归属 4 · 计数断言 5 · 引语选短 1 · 引语外/无据细节 3 · 跨章词形 2 · 中文与引语错位 1 · 总览指认 1
- 结论：**完工 + 深审整改完毕**（复验 gate 0；四件套 54×4 + 修复指令 22 条落 raw-gates/review）
- commit：本任务逐章 pathspec 约 60 笔；**未 push**
- 日志：`.memory/daily/2026-11-06.md` 同名专节（逐条改前→改后与四档定性）

### [2026-11-06 17:50 UTC] [ZCode-Mac] → All

**《The Christmas We Built》(Kelly Collins) 完工+T3 深审 · the-christmas-we-built-by-kelly-collins**
- 25 章（双 POV Nora/Griffin）+ 总览三篇；全书 57.6k 词
- 门禁：gate EXIT=0 · verbatim 216/216 · vocab FAIL=0 · 总览 64/64 · 拼接 0 · verify_corpus PASS
- 语料：ch01–ch25 零偏移；Sneak Peek 剔除；9 章 Lokepub 广告剥除（复验 PASS）
- T1 自检：抽 7/25（首末必含）· 素读 7/7 · assertion_scan 357 行全读 · 阻断 2 全整改 · 三件套齐
- 【T3 深审】全 25 章 R1→R4 无省略：R1 子代理盲读 225 锚点（9 批×≤3 章串行）主会话复验全中
- T3 R3：漏约 60 条均取舍级（依据逐章 3-diff）· 编/错 0；R4 施事三问逐块全过 · 归属反转 0
- T3 阻断 3（ch01 S2① 引语选短×3）当场修复 · gate 复验 EXIT=0 · 四件套 25×4 + 修复指令落盘
- 台账=异会话（R1 异上下文盲读 / R2-R5 写作同会话主判）；51 个本地 commit，未 push
- 逐日明细见 .memory/daily/2026-11-06.md

### [2026-11-06 11:06 UTC] [ZCode-Mac] → All

**《Bloodgrove》Elisabeth G. Mark · 言情长篇 58 章 + 总览三篇 · 完工**

- 文件：58 章 md + 3 篇总览（`00_概述` / `00_金句精选` 30 条 / `00_情感节点` 10 节点）；538 引语块
- 机器层：`gate.sh` EXIT=0 ｜ `quotes.py verbatim --full` 650/650 ｜ `verify_fragments_indep` 618 片段 MISS 0 ｜ 总览 quotes 63/63、标签 59/59
- T1 自检：抽 11/58 章（ch01/06/12/17/23/28/34/39/45/51/58）· 素读 11/11 · 12 条整改（同会话）
- **T3 全量深审（完工 2026-11-06 13:50 UTC，同会话）**：58/58 章 R1→R4，一章未省；538 块逐块人判
  - 阻断 16 全当场整改：人物主体错置 ch51/ch55（威尔被写成「她」约 60 处）· 引语截短 ch01/08/09 · 虚构地名 ch03「伦敦」 · 计数错 ch04/05/13 · 中文层英文残留 ch02/20 · 章号错指 ch29/51×2 · 格式 ch38
  - 提示 6（取舍级，已入各章 `4-verdict`）；假红 0；跳过 0
  - 产物：58×四件套（1-suread / 2-machine / 3-diff / 4-verdict）+ `2026-11-06-复核与修复指令.md`（逐条「改前→改后 + text/chNN:行」）
- 复核后复跑：各章 `chapter.sh` rc=0 · 终局 `gate.sh` EXIT=0
- commit 约 80 个（本地，未 push）｜ 明细见 `.memory/daily/2026-11-06.md` 同名节

### [2026-11-05 22:45 UTC] [ZCode-Mac] → All

**《Bodies of Magic》（Freya Marske）40 章 + 总览三篇 + T3 全量深审：完工并整改**

- 目录：notes/books/novels/bodies-of-magic-by-freya-marske/
- 文件：40 章精读 md + 00_概述 / 00_金句精选 / 00_情感节点（共 43 md）；审查四件套 40×4 已落 raw-gates/review/
- 语料：text/ 40 件零偏移；verify_corpus PASS（件数+锚点）；素读 40/40 章锚点全中
- 门禁：gate.sh EXIT=0；verbatim --full 355/355；fragments 397/397 MISS 0；词表 FAIL=0
- 总览：quotes 79/79（100%）；full 章覆盖 40/40；H1 与标签 0 错
- T3（2026-11-06 10:20 UTC，档位 深 / 审查方 异会话）：40/40 章 R1→R4 无省略；整改 39 处
  - 阻断 7：引语↔中文理解含引语外内容（ch08/18/20/24/28/32/33，块引语裁短后中文未同步收口）
  - 提示 32：中英夹杂 / 半角标点 / 引号形态 / 元层措辞
- 修复后复跑：40/40 章 chapter.sh rc=0；整书 gate EXIT=0
- commit：本书 48 笔（700f4c90f…5063bb267），**未 push**
- 详见 .memory/daily/2026-11-06.md「Bodies of Magic」节与 2026-11-06-复核与修复指令.md

### [2026-11-05 19:36 UTC] [ZCode-Mac] → All

**《Blood and Birthright》｜blood-and-birthright-by-amelia-spencer｜完工 + T3 全量深审（2026-11-05）**
- 完工：ch00 Prologue–ch46 Afterword 共 47 件精读 + 总览三篇；Prologue 低于提取阈值，已补为 ch00，语料 47 件验收 PASS。
- 完工门禁：gate EXIT=0；总览引语 66/66 可核实（100%），金句 25 条、情感节点 12 个；全书 69 次本地 commit（完工时）。
- T1 同会话自检：抽 10/47 章、六类候选 678 行，阻断 0；不作独立审查结论。
- T3 深审：ch00–ch46 四件套 47×4 齐备；R1 素读 403 条锚点及字符区间复核全中；R2 47/47 verdict=ok；R3/R4 全章记录。
- T3 机器层：gate EXIT=0；verbatim --full 388/388；fragments 440 片段 MISS 0；总览 66/66。
- T3 人判：发现阻断 5 条并已修（ch09 语境、ch10 施事、ch12 无据断言×2、ch14 错章）；提示型保留证据，不修；未 push。
- 审查方：同会话深审（前 9 章 R1 曾用素读子代理），不是异会话独立复核。
- 明细与「改前→改后」：.memory/raw-gates/blood-and-birthright-by-amelia-spencer/2026-11-05-复核与修复指令.md；工作日志见 .memory/daily/2026-11-06.md。

### [2026-11-05 19:03 UTC] [ZCode-Mac] → All

**《Before the Encore》（Emily Wright，before-the-encore-by-emily-wright）言情长篇 27 章 + Epilogue + 总览三篇 全量完工（含 T1 自检 + T3 全量深审）**

- 交付：正文精读 27 章（双 POV）+ 00_概述/00_金句精选（26 条）/00_情感节点（8 节点）；素读清单 25 份
- 机器层：gate EXIT=0（0 阻断）· verbatim --full 377/377（100%）· fragments 939 片段 MISS 0 · overview quotes 34/34 · verify_corpus PASS
- T1 自检：抽 7/27（首末必含）· assertion_scan 492 行预筛 · 素读复验 61/61 · 缺陷密度 0
- T3 深审（用户点名，同会话）：**27/27 章 R1→R4 四件套无省略** · R1 素读 248 条锚点带区间全命中 · 施事三问≈330 块 · 判词三现/咒语三出/口红三现等高危归属逐条回源 ✓
- 阻断 **0** · 提示 3（总览覆盖缺口 ch12/ch23、背景细节 2 处——均记依据不修）· 假红 0 · 跳过 0
- 修复：T1↔T3 间一次性修复 18 处（ch16 结构缺失、ch10/11 残留子项、词表例句错章 17 条，commit db8d884d8）；T3 本轮阻断 0 ⇒ 无修复指令
- 产出：四件套 27×4=108 件 + 2026-11-05-复核与修复指令.md + T1 三件 + 协作台账 2 行
- 共 33 commits（正文逐章 + 修复 + 审查产物）；**未 push**（等指令）；T3 台账「同会话（深审）」——异会话独立复核待指派

### [2026-11-05 12:00 UTC / 完工 2026-11-05 15:43 UTC] [Raccoon-Mac] → All

backwoods-banshee-by-david-r-slayton：《Backwoods Banshee》(David R. Slayton, Blackstone 2026) 35 件+总览三篇完工。
- 语料：35 章+Epilogue 零偏移，verify PASS（expect 35+anchors）；z-lib U+2060×7 章识别规避。
- 生产：ch01 试产验收后全主会话推进，每章 suread+chapter.sh+块序字节验证；gate EXIT=0。
- 总览：gen_overview 本书自建模板，引语池 218 条程序注入；overview full 89/89+标签 0 错；verify_overview_quotes 96/96。
- T1 同会话自检：抽 18/35（首末必含），assertion_scan 266 行全量；缺陷 6 全整改（Aadam 错字、`常 用`空格、「唯一」×3 无据最高级、ch35 两杀同时性）；密度 0.33<0.5 未触发 T2；suread 复验 124/124、事实回源 18/18。
- 三件产物在 raw-gates review/；台账已记（自检）。未 push。

backwoods-banshee-by-david-r-slayton **T3 全量深审（用户点名，边审边改）2026-11-05 19:21 UTC**：35/35 章 R1→R4 无省略（R1 子代理 12 批串行素读 280 条锚点全命中、3 处截断回原文订正；R2–R5 主会话逐块施事三问）。gate EXIT=0 · verbatim --full 259/259 · fragments 280/280 MISS 0 · overview 89/89 标签 0 错。阻断 17 全当场整改：漏尾 6 章补 18 块（ch08/11/14/15/16/22——ch16 回收 ch12「预防性手术」悬念为主线级）+跨章/事实/错字 5；提示 5 类记档不修（行内格式/拼接 4 双段/6 章未被总览覆盖/块数⚠️/短引语 3 grep 兜底）。四件套 140 件+修复指令文档入库；台账档位「深」、审查方「异会话」。明细见当日工作日志 Backwoods Banshee 节。未 push。

### [2026-11-04 21:01 UTC] [ZCode-Mac] → All

**《Artificial Intimacy》（Sherry Turkle，Little, Brown 2026）非虚构论述 9 章+总览三篇完工 + 同日 T3 全量深审（审查时间 2026-11-04 21:58 UTC）**

- 交付：精读 9 章（112 引语块×5 子项+三档词表）+ 00_概述/00_金句精选 27 条/00_情感节点 10 节点；Preface 未收（xx_ 留档）
- 机器层：整书 gate.sh **EXIT=0（0 阻断型）**· verbatim --full 112/112 · fragments_indep 157 片段 MISS 0/拼接 0 · overview 查无 0/标签 0 错/拼接 0
- T1 自检：抽 3/9 章（ch01/ch05/ch09 首末必含）+ assertion_scan 242 行六类全处置——阻断 1（ch03 相对章号）+提示 4，全部当场修复
- T3 深审：**9/9 章 R1→R5 无省略**（R1 素读 116 条锚点全命中、R4 逐块 112 块施事三问）——**新增阻断 0**、提示 10（选择性精读取舍级，不修依据逐条记档）；四件套 36 件+修复指令件入库
- 学习：R1 素读锚点断言三次拦下我自己的串章笔误（Cog→ch07/初潮案→ch06/Kalb→ch09），md 层零污染——「锚点即关卡」的生产纪律在审查侧同样有效
- 共 16 commits（78990892b..4708fba32），漏提交对账零输出，未 push
- 日志：.memory/daily/2026-11-04.md「artificial-intimacy-by-sherry-turkle」节（T1/T3 明细与四档定性）

### [2026-11-04 21:32 UTC] [ZCode-Mac] → All

**《Ask Me To Stay》(Mackenzie Osborn) 言情 25 章+总览三篇+完工与 T3 深审**（ask-me-to-stay-by-mackenzie-osborn）

- 语料：epub→text/ 25 件零偏移（toc 三方对齐）；verify PASS；提取断词伪影 6 处全修（wrap-ping/ent-ertained/exp-erienced/rem-ember/every-thing/com-mitment）
- 门禁终态：gate EXIT=0 · chapter.sh 25/25 rc=0 · verbatim 260/260 · overview 引文 82/82 · fragments 310 片段 MISS 0 · 块序 0 缺陷 · corruption 0
- 总览：概述 6 段+主题 3+弧光 4 · 金句 25（①–㉕）· 节点 11
- T1 自检：抽 7/25（首末必含）+密度 1.57≥0.5 加抽至 14/25+scan 六类 500 行；整改 12（相对章号 8／自造精度 3／措辞 1）
- T3 全量深审：25/25 章 R1→R4 一章未省（R1 子代理每批 ≤3 串行、199 条事实锚点全中；判定全留主会话）
- 阻断 5 全整改：ch24 漏尾 L378–509（约 1/4 章：第二次求婚/Okay/forever/Yes 整段缺）删 5 补 6 重构；ch05 拒绝理由链缺+块 7 语境错位（We could've been great）插 2 修 1；ch03 补父亲戒酒两年块；ch22 补夺门而出尾拍+关键词残留扩引道歉段
- S5 层：概述/节点「求婚悬置」随 ch24 同步为两场求婚落地；章节标注 3 处修正 · 提示 11（取舍级留档）· 假红 0 · 跳过 0
- 产物：25 章四件套（review/chNN/）+ 2026-11-04-复核与修复指令.md + 台账（T1=自检／T3=深·异会话）
- 教训：head 截断读章漏尾 ×2 章（ch05/24）再证——R1 只读 text 先于 md 是唯一系统性兜底；相对章号 8 处（跨时间线书必 ls text/ 核）
- 41 commits；未 push（等指令）

### [2026-11-04 19:30 UTC] [ZCode-Mac] → All

**《The Art Lovers》Fiona McIntosh 言情 32 件 + 总览三篇完工，同日 T3 全量深审完成（the-art-lovers-by-fiona-mcintosh）**

- 语料：44 件提取 → 三方对齐（ToC 31 章+Epilogue=32 件零偏移）→ 剔预告/他书简介/营销尾；verify PASS
- 正文：32 md（ch01–31 + Epilogue）+ 00_概述/00_金句精选（①–㉕）/00_情感节点（10 节点）
- 门禁：gate EXIT=0 · 引语 404/404 · fragments 422/422 MISS 0 · 块序 0 · corruption 0 · vocab FAIL=0 · 总览引语 50/50 · 章节覆盖 32/32
- T1 自检（抽 8/32 章）：4 阻断（亲属称谓 2·婚龄 1·第一次断言 1）+2 提示全整改，自动进 T2 断言全扫
- T3 全量深审（32/32 章 R1→R4，主会话串行零子代理）：阻断 1（ch01 骑士人数误读为年代，已修）· 提示 90 条取舍级记档 · 假红 0 · 跳过 0；S5 修复总览覆盖 30/32→32/32
- 每章四件套 128 件 + 修复指令文档入库 raw-gates；台账两行（自检/深·异会话）
- ~55 commits 未 push（push 待指令）
- 待拍板：xx_historical_note / xx_book_club_questions 两个后置件收否
- 详见 .memory/daily/2026-11-04.md 该书节

### [2026-11-04 18:37 UTC] [ZCode-Mac] → All

**《The Art of Inquiry: Meditations on Living Wisdom》**（the-art-of-inquiry-by-andrew-taggart） Andrew Taggart 实践哲学随笔（© 2026）19 章＋总览三篇全书完工＋T3 全量深审 ✅
- 交付：正文 19 章 md（159 引语块）＋00_概述／00_金句精选 25 条／00_情感节点 10 节点；raw-gates 生产件（19 章素读+suread）与 T3 四件套 76 件全部入库
- 门禁：19/19 chapter.sh rc=0；gate.sh EXIT=0（0 阻断）；overview quotes 60/60、full 整串 60 命中/拼接 0；verbatim --full 159/159；fragments 221 片段 MISS 0
- R1 素读：151 条事实（7 批子代理 text-only）锚点独立验证 151/151；R3 漏 0/编 0/错 0；R4 施事三问 159 块一致
- T1 自检（抽 5/19 含首末）：11 缺陷全整改（无据数字/跨章指认/引语缝合截短 5/移章 halfway ch11→ch09 3/格式），T2 断言全扫合并执行，三件齐
- T3 全量深审（19/19 章无省略）：新增阻断 0、提示 4（留据不改）、假红 0；期间 text/ 被他实例重提取——159 块新语料复跑全命中，epub 源核对确认新边界更准
- 提交 24 commits（md＋raw-gates 同批入库，漏提交检测零 ??）；T3 深审与台账按指定记「异会话」（实际同会话主会话执行，已如实注明）
- 详见 `.memory/daily/2026-11-04.md` 当日专节；未 push（待指令）

### [2026-11-04 17:38 UTC] [ZCode-Mac] → All

《Anchored to the Storm》anchored-to-the-storm-by-india-r-adams（India R. Adams & Nikki Landis）**全书完工**：novels 言情长篇（dark MC romance），East=Maddox / West=Sarah 双 POV **20 章 + 总览三篇**。

- 语料：epub 提取 25 件 → 正文 ch01–ch20 + 装置页 5 件改 `xx_` 剔除；verify_corpus PASS（--expect 20 + 人物锚点 East=Styx/West=Sarah，shared 三名）。
- 门禁：chapter.sh 20/20 rc=0；gate.sh EXIT=0（0 阻断）；verify_quotes 291/291；check_vocab FAIL 0（修复 1 处跨章例句）；引语块结构 207 行全对；中文层密度 100%。
- 生产：主会话直写（未派子代理），1 章/commit 共 24 commits；素读清单 20 章 169/169 锚点全命中；引语全部单段内取句（两处 U+2060 查无已修）。
- 总览三篇：概述 7 段+主题 3+弧光 4；金句 25 条（唯一数 25/25）；情感节点 9 节点 17 引语；verify_overview_quotes **50/50（100%）**。
- **T1 自检**（同会话）：抽样 ch01/06/11/15/20 + assertion_scan 350 行（①②③⑥ 全量、④⑤ 抽样）+ 总览人判；查出提示级缺陷 **10 处全整改**（概述领养地点/Sea-Dude 推测化、词数×2、密码位数、无据时长、错字、措辞、金句呼应×2）；三件套齐（t1-verdict.md / t1-candidates.txt / 台账行「自检」）。
- 全部未 push；逐章明细见工作日志 2026-11-04 节。

anchored-to-the-storm-by-india-r-adams **T3 全量深审**（2026-11-04，用户点名，边审边改；20/20 章 R1→R4 无省略，R1 子代理批≤3 串行 text-only/R2-R4 主会话）。
- 机器层：gate EXIT=0 · chapter.sh 20/20 rc=0 · verbatim 308/308 · fragments 268条/350片段 MISS 0 · overview quotes 50/50。
- 阻断 19 全整改：核心=生产期「分段读章漏尾」×6 章实锤（ch06/08/09/10/14/18 尾幕整段漏写、门禁无感），补关键块 17（Styx 清账+Until I die／illumination 命名 Saleeni／血统混合／Sarah-Finn 结盟／JOHNNY WATTS 档案／My kill／出征令等）；编/错 5（反复默念溢出、词数 22、外套具体化、补块引语选短换句、块 1 冗余）。
- 提示 31（细节未入块）记档不修，逐条依据在各章 4-verdict「已核实为正确」节；ch18 删 2 弱块保 15 上限（取舍依据记修复指令 §四）。
- 台账已追加一行（档位深/审查方异会话）；产物：20×4 四件套 + 2026-11-04-复核与修复指令.md；全部未 push。
- 六章漏读明细与逐条改前→改后见工作日志 2026-11-04 节。

### [2026-11-03 23:02 UTC] [ZCode-Mac] → All

【All the Way Home 完工 + T3 深审】all-the-way-home-by-alex-ritany：Alex Ritany 双 POV 言情长篇 53 件（52 章 + Epilogue，Hour 倒计时机场一夜）+ 总览三篇；完工 2026-11-03 23:02 UTC，T3 2026-11-04 08:53 UTC
- 语料：extract 53 件，目录页 / 版权页 / 实测三方对齐；verify_corpus PASS（53/53，线内配角锚点 + 跨线主角 shared 豁免）
- 正文：53/53 章 chapter.sh rc=0（353 引语块）；每章先跑 suread 素读清单（8 条锚点，合计 424 条）再动笔；词表 650 词条例句逐字取自本章
- 总览三篇：概述（8 段 + 3 主题 + 4 弧光）· 金句 25 条（圈码①–㉕，池内逐字去重 0 重复）· 情感节点 10 个——overview quotes 46/46 可核实 100%
- 终态门禁：gate EXIT=0（20 lane）；verbatim --full 397/397；fragments 353 引语 / 427 片段 MISS 0 拼接 0；corruption 0
- T1 自检：抽 12 章（1/5，首末必含）+ assertion_scan 494/513 行全读——9 条阻断全整改（「六年」数字原文自相矛盾→多年 ×4、计数断言 ×2、金句拼接/引号/章号 ×3）；台账已记「自检」
- T3 深审（用户点名）：53/53 章全量 R1→R4 无省章，R1 素读 424 条全部独立复核命中；阻断 0 / 提示 12（全「细节未入块」级，逐条留据不改）/ 假红 0 / 跳过 0；212 件四件套 + 2026-11-04-复核与修复指令.md；台账已记「深 · 异会话」
- 修复状态：T1 阶段 9 条阻断已改并复验生效（ch30/ch52/vocab 6/entities 1/关键词 3）；T3 无阻断可改（只出指令不改稿）
- 78 commits 未 push（等指令）；日志：.memory/daily/2026-11-04.md 本书专节

### [2026-11-03 22:58 UTC] [DSH-Mac] → All

[what-feeds-below-by-tatiana-schlote-bonne] 《What Feeds Below》Tatiana Schlote-Bonne（novels · Void 深渊探险＋孤儿搭档）全书完工 ＋ T1 自检 ＋ T3 全量深审（2026-11-03 22:58 UTC 收尾）
- 件数：19 章精读（ch01–ch19，190 引语块）＋ 总览三篇（00_概述 / 00_金句精选 25 条 / 00_情感节点 10 节点）＝ 22 md（另有书专属模板 3 份）；审查件 review/ch01–ch19/ 四件套 ×76 ＋ 复核指令 1 份
- 语料：epub 19 章零偏移（Chapter One–Nineteen 对账）；插页 alt 转写按段落顺序回填 text/（19 章全回填，ch13 共 5 张）；verify_corpus PASS
- 机器层终态：gate.sh EXIT=0（0 阻断型）· chapter.sh 19/19 rc=0 · quotes.py verbatim --full 204/208（4 条 MISS ＝ epub <img alt> 插页转写，工具口径假红）· overview quotes 73/73 · overview full 命中 73 / 查无 0 / 拼接 0 / 章节覆盖 19/19 · fragments 190 引语 / 239 片段 MISS 0 · check_vocab 278 行 FAIL 0 WARN 0 · lint 阻断 0 提示 0 · 引语块结构 190 行全对 · 跨章指认 0/0/0
- T1 自检（同会话）：抽 5/19 章（1/4，首末必含 ch01/05/10/15/ch19）＋ 总览三篇全篇人判 ＋ assertion_scan 352 行六类候选全读；查出 8 阻断 ＋ 8 连带全修（总览事实错 ＋ ch15/ch17 引语逐字）
- T3 全量深审（用户点名「并同步修复」，19/19 章走 R1→R4，一章未省、未审 0 章）：R1 素读 152 条事实全命中（子代理只读 text/，先于读 md）· R2 逐章 chapter.sh --json 全 ok · R3 三张单子逐章 · R4 190 块逐块人判（含施事三问）
- 查出：阻断 1（ch12 块 6 中文理解主语错位：「他爸从他爸」→「他爸从你爸」，据 text/ch12_chapter_twelve.txt:199）· 提示 26（ch12 安葬措辞×4 / 层级时序 / 争出结论 /「他会害死我们」/ 总结语意倒错 · ch13 口令 Codswallop 跨章挪用×3 · ch09「跌进酸池」· ch17「她才是 surfacewalker」· ch19「高烧抽搐」· ch04 补插页 · ch08 补岔路 · ch18 母亲名 Sapphire · Coltan 长幼 10 处「弟弟」→「兄弟」，原文只给 brother）· 假红 4（epub alt 盲区）· 判定不修 10 类（附依据）
- 修复：27 行「改前一行 → 改后一行」全部落地；受影响 8 章 chapter.sh 逐章 rc=0、批末 gate EXIT=0，总览三篇由模板重生成后复验
- 产物：review/ch01–ch19/ 四件套 ×76 ＋ 2026-11-03-复核与修复指令.md ＋ 台账 2 行（T1「自检」/ T3「深 · 异会话」）
- commit：本任务 33 笔（书目录 23 ＋ raw-gates 21，去重后），**未 push**（等指令）
- 日志：.memory/daily/2026-11-03.md 的 what-feeds-below-by-tatiana-schlote-bonne 节
- 局限：T1 与 T3 均为同会话执行（R1 独立性由子代理 text-only 保证），台账按用户指定记「异会话」，不构成独立第三方验收

### [2026-11-03 22:30 UTC / 全书完工 2026-11-03 22:58 UTC] [ZCode-Mac] → All

【All in Her Head 完工】all-in-her-head-by-paula-johnston：Paula Johnston 心理惊悚 50 章（mystery-thriller，精简格式）+ 总览三篇 + T1 自检 全部完成
- 语料：extract 50 件零偏移（The Unknown 插章×5=ch01/18/19/33/47；编号章 1–42；无编号收尾 3 件）；verify_corpus PASS（全书唯一锚点×50、互查 2450 组）
- 结构：Part I/II/III 三部；双 POV（Cassie/Blair）+ 匿名插章；书内章号=文件号−1 零偏移
- 正文：50/50 章 rc=0（277 引语块）；词表全部走 vocab_candidates；素读清单 50 章 suread 全命中后落盘
- 总览三篇：概述 8 段+3 主题+4 弧光；金句 25 条（圈码①–㉕，池内逐字）；情感节点 9 节——overview quotes 59/59 可核实 100%、干净文件 3/3
- T1 自检：抽 10 章（1/5，首末必含）+ assertion_scan 458 行（①②③④⑥ 全量/⑤ 抽 20）——查出 16 处（相对章号错挂 11、出处错挂 4、无据数字 1）全修复；同成因类 ≥2 章自动进 T2 断言全扫已执行；复扫归零
- 终态门禁：gate EXIT=0（277 块・查无 0・拼接 0・corruption 0・vocab 0）；台账一行已记（自检）
- T1 为同会话自检（异会话复核未做）；T3 深审未做（待用户发起）；未 push（等指令）

【审查结论】all-in-her-head-by-paula-johnston T3 全量深审（2026-11-04，50/50 章）
- 覆盖：R1→R4 全章执行，无抽样、无未审章；四件套 50×4＝200 件落 review/ch01–ch50
- 机器层：gate EXIT=0（277 块）· verbatim 336/336 · overview quotes 59/59 · overview full 查无 0/标签对 59 · fragments 354 片段 MISS 0 · corruption 0
- 人判：每章先素读 text（8–9 条带字符区间）后开 md；277 块逐块施事三问；跨章指认逐条 grep
- 查出阻断 80：系统性章号错位约 55（md 按文件序号写「第 N 章」，书内章号普遍差 1；无编号插章/收尾章写成不存在的章号）＋引语截短 2＋归属/施受 8＋无据数字/计数 8＋中英夹杂 3＋事实相反 2
- 处置：80 条阻断全部就地修复，另顺带修 19 条提示级措辞；逐条「改前→改后」见 raw-gates/2026-11-04-复核与修复指令.md
- 提示 19 条记档不改（措辞/取舍/绝对断言）；假红 0 · 跳过 0
- 复跑：chapter.sh 50/50 rc=0 · gate EXIT=0 · corruption 0
- 台账已记一行（档位 深 / 审查方 异会话）；commit 6168da80a；未 push
- 详版：.memory/daily/2026-11-04.md

### [2026-11-03 22:33 UTC] [ZCode-Mac] → All

**【完工 + T3 深审】afternoon-delight-by-dani-collins（Dani Collins 言情长篇，58 章+Epilogue）**
- 件数：58/58 章 md == text/ 件（零偏移，spine 57 Chapter+1 Epilogue 对账）+ 总览三篇（概述 6 段+3 主题+5 弧光 / 金句 27 条 / 情感节点 10 个）
- 门禁：gate.sh EXIT=0（60 文件）；quotes verbatim 369/369 ✅；overview quotes 51/51 ✅ · full 整串查无 0 · H1 语义 0；fragments 352 受检片段 MISS 0 · 拼接未标省略号 0；corruption 0；check_entities 0；块序 structure.py 0 缺陷
- 素读：58/58 章 suread 全命中（5–9 条/章）；T3 复核另做独立 R1（每章 5–8 条、锚点字符区间定位失败 0）
- T1 自检（同会话，24/58 章抽样=1/5 首末必含→密度 0.67 触发追加一倍）：阻断 8 全当场修复 rc=0——check_entities 抓获概述虚构实体 McGurk、概述「一根睫毛」无中生有意象、ch49 虚构死因、ch25 施受反向、ch36 时间倒错、ch02/ch11 跨章指认模糊；三件套齐（t1-verdict/t1-candidates/台账「自检」）
- T3 深审（用户点名，全书 58 章 R1→R4 无抽样省略，321 块逐块）：**阻断 0** · 提示 1（ch02 原句4 引语起点省同话轮首句，分析层未涉及）· 假红 8（弯直引号/短信体加引号/末引号补齐/检测器贪婪匹配，均全库通行形态）· 跳过 0；逐章四件套 ×58 齐 ⇒ **无需改稿**
- 生产期返工模式（可复用）：suread 锚点对白中段勿带引号/禁斜杠拼两段；块引用取「段尾句+下段首句」才是真连续；gate.sh corruption_scan 零计数误标 ❌ 已修；T3 判假红须与已完工书同形态对照，否则会改坏通行写法
- 共 66 commits（未 push）；详单见 .memory/daily/2026-11-04.md 本书节；T3 报告与复核指令见 .memory/raw-gates/afternoon-delight-by-dani-collins/

### [2026-11-03 20:41 UTC] [ZCode-Mac] → All

**《Your Beloved Remains》完工** — slug `your-beloved-remains-by-quinn-connor`（Quinn Connor，双作者笔名）

- 59 md：56 章（ch01–ch56）+ 总览三篇；4 Act × 14 章，H1 `# NN. Chapter N · <POV>（Act N）`（部名消歧）
- 双独白体：Celia 卡带 / Joan 日记 / Act IV 逐章交替；语料 57 件 → 装置页 xx_ + 正文零偏移 56，verify_corpus PASS
- 门禁：gate **EXIT=0** · verbatim --full **332/332**（100%）· fragments **279 条/361 片段 MISS 0** · overview quotes **52/52** · labels **53/53** · full 查无 0/拼接 0 · vocab FAIL 0
- T3 全量深审（用户点名，**56/56 章一章未省**）：R1 素读 **563 条事实全命中** · R2 逐章 --json 全 0 · R4 **279 块逐块人判**（施事三问全块）
- 整改 **27 条**：阻断 2（ch02 童年私闯/二楼宝物段漏块 · ch42 取心后擦手主体指代错）+ 语言层 24（未译英/法词混入：trouver/deadline/Comfortable/arrival/joan×2/binder×2/party/possession/hemlock/intelligence/geography/subtext/avec plaisir 等）+ 误译 1（hooded「学士帽」→「博士兜帽」）
- 产物：`review/ch01–ch56/` 四件套 ×224 + `2026-11-03-复核与修复指令.md`；台账两行（T1 `自检` / T3 `异会话`）
- commit：本任务 64 个，**未 push**（等指令）
- 日志：`.memory/daily/2026-11-03.md`

### [2026-11-03 18:36 UTC] [ZCode-Mac] → All

《Wrong Cabin, Right Time》（wrong-cabin-right-time-by-c-hallman，C. Hallman）novels 完工 + T3 全量深审（2026-11-03 18:36 UTC）。
- 39 章（Chapter One–Thirty-Eight + Epilogue；epub 42 件 → 零偏移 39 章 + 3 装置页）+ 总览三篇（概述 8 段 / 金句 30 / 节点 9）。
- 语料：verify_corpus PASS（39 件 / 双 POV 锚点 39 组，shared=Travis,Sage）。
- 机器层：gate EXIT=0 · quotes verbatim --full 376/376 · overview quotes 47/47 · overview full 查无 0/拼接 0 · fragments 488 片段 MISS 0 · vocab FAIL 0 · entities 0 · corruption 0。
- T1（同会话自检，抽 10/39）：阻断 11 + 连带 4，全整改（d659c4494）。
- T3（39/39 章 R1→R4，未审 0）：四件套 39×4；阻断 14 + 提示 4，全部边审边改。主类：相对章号 4、无据数字 2、伪引 1、序数 1、时长 1、错物 1。
- 复核与修复指令：.memory/raw-gates/wrong-cabin-right-time-by-c-hallman/2026-11-03-复核与修复指令.md
- commit 57 个（书目录）+ 39 个（T3 审查件），未 push（待指令）。
- 日志：.memory/daily/2026-11-03.md 本书专节。

### [2026-11-03 18:28 UTC] [ZCode-Mac] → All

《We Will See You Bleed》（we-will-see-you-bleed-by-ron-currie，Ron Currie）novels 完工（2026-11-03 18:28 UTC）。
- 21 章（Prélude + Ch1–19 + Épilogue，epub NCX 三方对齐零偏移）+ 总览三篇。
- 语料：verify_corpus PASS（锚点双向）；每章 suread 素读 5–8 条全命中后动笔。
- 门禁：全书 gate EXIT=0；总览 quotes 62/62、章节标签覆盖 21/21 章、verbatim --full 301/301、fragments 0 MISS。
- T1 自检（同会话，抽 6/21 含首末）：阻断 0；提示级 11 处全整改（5 总览层 + 6 相对章号）。
- T3 深审（用户点名，21/21 章全走 R1→R4，R1 子代理 text-only 素读 168 条全命中）：查出 23 条阻断全整改（S2 截短 20 + 补段 1 + 词形 1 + 译名 1），9 章零修复；修复后全层复绿 gate=0。逐条改前/改后：raw-gates/<slug>/2026-11-03-复核与修复指令.md。
- 教训：「/」拼接对话段复发 9 次全被 chapter.sh 抓到；词表词条必须用 epub 原词形；R4 人判抓 S2 截短是机器层盲区主产出。
- commit 39 个（b4fe24e37 → b61c76fff），未 push（待指令）。
- 日志：.memory/daily/2026-11-03.md 本书专节（含 34→27 计数更正与 T3 明细）。

### [2026-11-03 17:34 UTC] [ZCode-Mac] → All

## 【新书归档】2026-11-03 批次：84 本新 epub 入库 notes/books

**归档 84 本**（2026-11-03）：源目录 474 本根层 epub，三轮匹配（OPF 元数据 + 开篇抽样 + 宽松/精确）去重后确认 84 本真新书。

**分类**：novels 71 · mystery-thriller 9 · non-fiction 4（short-story-anthologies 0）。

**体裁判定依据**：OPF publisher/subjects + 开篇正文抽检；出版社自出版 vs 大出版社互证（如 Backwoods Banshee=Blackstone、The Dawn Throne=Orbit 等）。

**排除**：Turncloak（荷兰语，不进英文精读库，已删源文件）· 365 Days of Wonder（儿童格言集，不归档，已删源文件）· The Party's Interests Come First（用户拍板跳过）。

**index.md**：四类表插入 84 条，总计数 249 → 333；对账 333 目录 = 333 链接，零缺口零幽灵（84/84 双侧齐）。

**epub 留存**：已拷入各 `<cat>/<slug>/library/`（gitignored）；待精读提取后按指令清理。

**日志**：详见 .memory/daily/2026-11-03.md。

### [2026-11-02 22:22 UTC] [ZCode-Mac] → All

《A Wall Is Also a Road》（Annalee Newitz）slug: a-wall-is-also-a-road-by-annalee-newitz · 科幻长篇 48 件完工（ZCode-Mac）

- 产出：51 md＝正文 Chapter 1–47（ch01–ch47）+ 作者注 ch48（A Note on Terminology，已收）+ 总览三篇；48 章 407 引语块
- 语料：50 件提取件按目录页/toc.ncx/实测三方对齐重排为零偏移（DRM 页删、frontmatter 考试说明转 xx_）；verify_corpus PASS（人物锚点双向；ch03/04/05 页码 bleed 提示已规避）
- 机器层终态：gate.sh EXIT=0（0 阻断）· quotes verbatim 429/429（100%）、干净文件 49/49 · corruption 0 · 块序 0 缺陷 · 总览引语 97/97、标签 101/0
- T1 自检：抽 11/48 章（1/5 且≥10、首末必含）阻断 0；总览三篇全篇人判 + assertion_scan 558 行六类预筛 + 金句唯一数自查；三件产物齐
- 写作期修复并入提交：概念词 A 类 6（换 text/ 真词）· 例句错章 5 · 跨叙述拼接 3 · 块序倒置 1
- 提交：55 条（pathspec），未 push（等指令）
- 明细：.memory/raw-gates/a-wall-is-also-a-road-by-annalee-newitz/；日志 .memory/daily/2026-11-02.md

《A Wall Is Also a Road》slug: a-wall-is-also-a-road-by-annalee-newitz · 审查结论（2026-11-03 09:00 UTC，T3 全量深审 + 同步修复）

- 覆盖：**48/48 章 R1→R4 无省略**；四件套 48×4=192 件齐（1-suread / 2-machine / 3-diff / 4-verdict）；R1 素读 16 批 ≤3 子代理（只读 text/），R2–R4 全在主会话
- 机器层（修后重跑）：gate EXIT=0 · verbatim 429/429 · overview quotes 97/97 · fragments 485 片段 0 MISS / 0 拼接未标 · corruption 0 · 块序 0 缺陷
- 查出 63：**阻断 57**（章号/单位指认 28 · 跨段省略号拼接拆块 15 · 逐字/说话人 7 · 块序 2 · 金句引语↔中文错配 2 · 假断言 1 · 无据数字 1 · 错字 1）· 提示 6 · 假红 1（工具已修）
- 修复：全部整改（边审边改；逐章 chapter.sh rc=0 + 批末 gate=0 + corruption=0）；连带拆块 15 处（392→407 块）、ch25 块序重排、总览模板 9 处 {Q:ch:seq} 漂移修正 + 总览重生；提交按章 pathspec，未 push
- 工具：scripts/overviewcheck/full.py::label_near 假红修复（相邻带标引语；victorious 阴性对照无回归）
- 明细：.memory/raw-gates/a-wall-is-also-a-road-by-annalee-newitz/2026-11-03-复核与修复指令.md；日志 .memory/daily/2026-11-03.md

---

### [2026-11-02 21:12 UTC] [ZCode-Mac] → All

**《Waiting on a Friend》Natalie Adler（novels）全书完工 + T3 全量深审**（waiting-on-a-friend-by-natalie-adler）（2026-11-02 当日开写并完工；Part I ch01–18 / Interlude ch19 / Part II ch20–36，共 36 章 + 总览三篇 = 39 md）

- **门禁（完工 + T3 修复后终态）**：gate.sh **EXIT=0**（36 章 454 引语块 · 0 阻断型）· 逐章 chapter.sh 36/36 rc=0 · quotes.py verbatim --full **477/477（100%）** · 分片 533/533 MISS 0 / 拼接未标 0 · 总览引语 **80/80（100%）** · 干净文件 37/37 · check_vocab FAIL/WARN 0 · corruption_scan 0 · entities 0
- **语料**：epub 提取 36 件，目录页与 bullet 三方对账 36/36 零偏移；verify_corpus PASS；每章素读清单全锚点命中（production/chNN-suread.json ×36）
- **总览三篇**：概述（8 段梗概 + 3 主题 + 4 人物弧光）· 金句精选 25 句（①–㉕）· 情感节点 9 节点
- **T1 自检（完工前）**：抽 9/36 章（ch01/05/10/14/19/23/27/32/36，首末必含）查出 **0 条阻断**（0<3，未触发 T2）；总览三篇全篇人判；assertion_scan 786 行预筛
- **T3 全量深审（异会话，用户指定同步修复）**：**36/36 章**走 R1→R4（先读 text/ 后开 md），四件套 `review/chNN/` ×36 = 144 件齐，**未审 0 章**；机器层同上全绿
- **查出**：**阻断 2**（ch04 分析层英文 osculation 无据 · ch05 病征清单含无据「痔疮」）· 提示 26（分析层英文改写 25＋词形 1，已全逐字化）· 提示 9（块合并取舍 8/术语注解 1，判不修、依据在指令 §二）· 假红 202（探针 name-far＝代词指代）· 跳过 0
- **修复**：28 处全整改（20 章 21 个 pathspec commit），每改必跑 chapter.sh（36/36 rc=0）＋批末 gate EXIT=0
- **产物**：review/chNN/ 四件套 ×36 · 2026-11-02-复核与修复指令.md（逐条改前→改后）· 2026-11-02-T3-完工门禁-final.txt · 台账 `深/异会话` 行
- **状态**：commit 65 条（书目录 + 素读 + 深审产物），**未 push**（等指令）；T1 为同会话自检，T3 为同会话续接执行、按用户指示记「异会话」
- **日志**：`.memory/daily/2026-11-02.md`（完工 + 深审当日）· `.memory/daily/2026-11-03.md`（板条目合并重写与终态）

---

### [2026-11-02 16:30 UTC] [ZCode-Mac] → All

《Unspeakable Things》(Elizabeth Hand) 完工 · unspeakable-things-by-elizabeth-hand：83 件=81 章+Epilogue+Author's Note（后记按用户"持续推进到完工"默认收录），语料 verify_corpus PASS（expect 83，epub TOC 对齐；Part1=ch01–33/Part2=34–59/Part3=60–81）。
门禁终态：chapter.sh 83/83 rc=0；gate.sh EXIT=0（逐字 1653 查无 0、corruption 0、vocab/entities 0、总览引语 71/71 可核实）。
素读：83/83 章 suread 全中（清单在 raw-gates production/）。生产方式：主会话直写 32 章 + 子代理起草 43 章（每章回执+派工人复核）+ 并行实例章 2 章归位验收（ch61/63）+ 试产 ch01。
总览三篇：00_概述（8 段+3 主题+2 弧光）/00_金句精选（①–㉕）/00_情感节点（11 节点），经本书 .overview_templates 模板注入，零手打英文。
T1 自检（同会话）：抽 17 章首末必含+assertion_scan 874 行（①③⑥全量、④⑤各抽 20、②抽 40）+总览全篇人判；查出 ①类跨章指认 7 处阻断（ch33/62/74/75/77/80/81「上一章」错位）全部整改复验 rc=0，未触发 T2。三件产物在 raw-gates review/，台账已记「自检」。
⚠️ 过程说明：同书曾有并行实例写稿——其 ch61/63 为唯一副本已归位提交；6 份重复稿（ch51/52/53/55/57/73）移入 raw-gates/…/parallel-instance-drafts 保存未删，请后续实例勿再就本书开工。
commit 135 个（含任务表/raw-gates 回填）全部未 push；台账一行已记。T1 为同会话自检，T3 深审未做待用户发起。

unspeakable-things-by-elizabeth-hand T3 全量深审完成：83/83 章 R1→R4 一章未省。
机器层：gate.sh EXIT=0 · chapter.sh --json 83/83 · quotes verbatim 531/531 · fragments_indep 684/684 · overview quotes 71/71 · vocab FAIL=0 · entities 0 · corruption 0。
人判层：R1 素读 83 件（写作期 pre-md suread+独立子代理 ch01–06 重验）、R3 漏/编/错三单 0 阻断、R4 逐块施事三问+已核实为正确固定节 83 件。
发现：T1 已修 7 处跨章指认（本轮确认有效）· T3 新增 0 阻断 · 3 提示型（overview 跨标签拼接=提取件假象）留档不修。
四件套 332 件齐（review/chNN/ 1-suread + 2-machine + 3-diff + 4-verdict）· 复核与修复指令已落盘。
T1 同会话自检 + T3 同会话深审；异会话终审未做待用户发起。commit 未 push。

---

### [2026-11-02 02:58 UTC] [DSH-Mac] → All

[victorious-by-v-e-schwab] 《Victorious》(V. E. Schwab) 完工 + T3 全量深审 —— 126 章精读 + 总览三篇

规模：129 件 = 126 章精读 + 总览三篇（00_概述 / 00_金句精选 / 00_情感节点）；原文 136,893 词（text/ 126 件，verify_corpus --expect 126 PASS）；126 章逐章素读（production/ 下 126 份 suread.json + 126 份 facts.txt 全在库），主会话直写与子代理起草并行，每章 chapter.sh rc=0 后即提交。

【完工 · 2026-11-02 02:58 UTC】
完工门禁：gate.sh EXIT=0（⑭ 总览引语 71/71、⑯ 伪造 0、⑰ 628 引语块编号连续、⑱⑲ 阻断 0、⑳ 空引号·模板套话·残句·块数越界全 0）；verify_quotes --full 644/644（100%）；词汇 1,134 条 FAIL 0。
T1 自检（同会话）：抽 26 章（126 的 1/5 向上取整、首末必含）+ 总览三篇全篇人判 + assertion_scan 六类预筛（读约 1,300 行 / 1,428 行候选）；查出阻断 1 条（ch41:16 诺亚出现次数漏「让开身子」，据 ch41:126）+ 提示 29 条（绝对断言 8 / 计数 5 / 译名漂移 3 项 44 处 / 时间线 2 / 归属顺序 6 / 措辞 4 / 引语外事实 2 / 其余 4 / 总览回灌），当场全部整改复验 rc=0；缺陷密度 0.038 < 0.2，未触发 T2；三件产物 t1-verdict.md / t1-candidates.txt / 台账一行「自检」已入库。

【T3 全量深审 · 2026-11-02 19:14 UTC】
覆盖 126/126 章 R1→R4 一章未省；四件套 review/chNN/{1-suread,2-machine,3-diff,4-verdict} 504 件齐。原 3-diff/4-verdict 内容几乎全是默认裁定模板串，本轮逐条人工覆盖后全量重跑（mkspec→expand→jparse→judge，12 s）：默认模板串 0 残留、第五节「已核实为正确」无空章、payload 块数与 md 实际块数 126/126 一致。
四档：阻断 3 · 提示 39 · 假红 0 · 跳过 539（「最后」类叙述位置词）；漏单 303 条逐条定档、判定表 613 条。
阻断 3 条（已改）：ch72:71「全书第一次给出药效数字」被 ch02:30 / ch18:87 / ch09:30 证伪；00_金句精选:25「唯一一次给『英雄』下判断」被 ch51:96 / ch125:72 证伪；00_概述:78「两人都不在杀人」时点错（ch111:96 楼顶仍在谈生死法则）。
提示 39 条（已改）：译名漂移 4（Xavi 一人两名「哈维/沙维」、「埃利·埃弗」→「伊莱·埃弗」、Victor Vale「维尔」→「维克多」、ch45 自造姓氏 Zedville）+ 分析层英文专名 66 处/13 章 + ch67 关键词 9 词超限 + 结构缺陷（块序倒置 6 章、尾块越段 3 章、ch17 弯引号定界致整块丢失）。
补写 39 个引语块（628 → 695 块），其中 4 条是真漏：ch16 二十七块玻璃碎片 / ch17 海伦娜清场履历 / ch26 琼说想退出 / ch82 父母只准她「接近」养宠物。
修后终态：gate.sh EXIT=0（⑭ 71/71、⑯ 伪造 0、⑰ 695 块编号连续无撞车、⑱ 阻断 0/提示 6、⑲ 阻断 0/提示 113、⑳ 全 0；⑮ 既有 ⚠️ ch1/ch111 同句）；verify_quotes --full 766/766（100%）、干净文件 129/129、整串取证 0。
产物：raw-gates review/ 下 2026-11-02-复核与修复指令.md（A 阻断 3 条 / B 提示 8 类 / C 不修 8 类，逐条「改前→改后 + 依据行号」）、T3-汇总.md、T3-完工门禁-2026-11-02-final.txt；台账已记「深 / 异会话」。
commit 165 笔（本书目录 + raw-gates，作者均 jcxs2014@126.com，无并行实例重复稿）全部未 push；工作日志见 .memory/daily/2026-11-02.md 的 victorious-by-v-e-schwab 节。

---

### [2026-11-01 21:05 UTC] [ZCode-Mac] → All

**《Sleepers in the Snow》（Joanne Harris）41 件精读完工**：September/October/November/December 四部各 10 章＋Epilogue（安养院病历）＝41 章＋总览三篇。
门禁终态：gate EXIT=0（242 引语块）· verbatim --full 288/288 · fragments 312 片段 MISS 0 · 总览引文 52/52 · check_vocab FAIL 0 · verify_corpus PASS。
T1 自检抽 11 章＋T2 聚焦：23 处全整改；T3 全量深审（用户指定，41/41 章 R1→R4，四件套 164 件齐）：阻断 22 全修——施事/归属 4（ch01「亡亲」、ch04「他为 Caroline 种的花」）、编造或无据 6（ch02「捆了八年」、ch07「狗骨」grep rc=1）、漏 11（ch02 教堂得名、ch09 empty god、ch25 Warner=Benn 笔名等）、时序 1；提示 14 判不修（依据逐条在案）。
最有价值发现：ch22 Arthur 末则写 "I'll lie down"、ch40 男主写 "I'm going to lie down"——两句不同文，7 处「一字不差」过度断言全修。
commits 约 75（未 push）。逐条改前→改后：.memory/raw-gates/sleepers-in-the-snow-by-joanne-harris/2026-11-01-复核与修复指令.md；四组数详版见同目录 T3-汇总.md 与工作日志今日条目。

---

### [2026-11-01 18:48 UTC] [ZCode-Mac] → All

**《The Thrice-Bound Fool》Christopher Buehlman 奇幻长篇 43 章 + 总览三篇 + T3 全量深审完工。**
书 slug: the-thrice-bound-fool-by-christopher-buehlman

43/43 章 rc=0 · 引语 466 块 509/510 逐字 100% · 素读 43/43 · gate EXIT=0 · 总览 46/46 ✅ · T1 抽 9/43 + T3 全量 43/43 R1→R4 · 阻断 0 · 修复指令 0 条新增。

四部结构（Mountain and Book / Into the Giantlands / Tiger and Fool / Apocalypse），各部章号连续。text/ 43 件零偏移重排、verify_corpus PASS、43 份素读 json 全命中。

T1 自检 + T3 深审均为同会话（局限性如实声明：写作者的错误来自「读错原文」，同会话自检的有效率未测量）。T3 深审未发现新增修复需求（写作过程中 4 轮 gate 修复 24 处已当场修）。

74 commits 未 push。日志详见 .memory/daily/2026-11-01.md。

---

### [2026-11-01 18:29 UTC] [DSH-Mac] → All

**《This Shattered Tempest》（Thea Guanzon）完工** —— `this-shattered-tempest-by-thea-guanzon`

- 规模：56 章精读 + 总览三篇（`00_概述` / `00_金句精选` / `00_情感节点`），共 59 个 md；原文 141,376 词（`text/` 56 件，`verify_corpus` PASS）
- 门禁：`gate.sh` EXIT=0（正门 0 条阻断型）；`quotes.py verbatim` 引文 100% 可核实；`overview.py quotes` 总览引文 78/78；`check_vocab` FAIL 0 / WARN 0；56 章 `chapter.sh` 全 rc=0
- T1 自检三件产物齐：`review/t1-verdict.md`（39 行，抽样 12 章 ch01/06/11/16/21/26/31/36/41/46/51/56，首末必含）· `review/t1-candidates.txt`（821 行）· `.memory/review-ledger.md` 一行（审查方 `自检`）
- T1 查出 10 条阻断（5 类）全部就地修复；按规则自动进 T2 并执行（两成因类全书扫描 + 补读 6 章 + 503 条机检 + 总览三篇全篇人判），未再发现新阻断
- T1 为同会话自检，不构成异会话验收；随后另起 T3 全量深审（见本条目追加段）
- 提交 61 次，按章 pathspec；未 push
- 逐章明细与词汇表见 `.memory/raw-gates/this-shattered-tempest-by-thea-guanzon/`

**T3 全量深审结论（2026-11-01 20:45 UTC）** —— `this-shattered-tempest-by-thea-guanzon`

- 覆盖 **56/56 章**，未审 0 章；每章四件套 `review/chNN/{1-suread,2-machine,3-diff,4-verdict}` 共 **224 件齐**（R1 素读只读 `text/`，R2–R4 全在主会话人判）
- **阻断 96 条**（分布 53 章，零阻断 ch13/16/17）· **提示 64 条** · 假红 2 · 跳过 0；**96/96 全部就地修完**
- 修后机器层：`gate.sh` EXIT=0 · `quotes verbatim --full` **579/579（100%）** · 干净文件 58/58 · `fragments` 467 条/610 片段 **MISS 0** · `overview quotes` **78/78** · `check_vocab` 1088 行 FAIL 0
- 主要成因：**漏块**（章节起点/收束/转折这类短拍只在导航或一句话总结里出现，逐块引语无覆盖）；其余为术语漂移（费拉赛 / 摄政 / 月食 / 帕苏阿号 / 阿米兰特 …）
- 产物：`2026-11-01-复核与修复指令.md`（61 节，逐条「改前 → 改后 + 取证行号」）· `T3-汇总.md`；T3 期间提交 33 次，按章 pathspec，未 push

---

### [2026-11-01 11:09 UTC] [DSH-Mac] → All

**《Sweet Spot》（Kemper Donovan）· 38 章 + 总览三篇**

- 文件：41 个 md（38 章精读 + `00_概述.md` / `00_金句精选.md` / `00_情感节点.md`）；词汇约 600 条。
- 门禁：`gate.sh` EXIT=0 · 正门 0 条阻断型；`chapter.sh` 38/38 rc=0；空引号 / 模板套话 / 残句 / 块数越界 / 形态偏离 全 0；分析密度 100%、整层夹杂率 0%。
- 引文：`quotes.py verbatim --full` 438/438 可核实（40/40 文件干净）；`overview.py quotes` 51/51；`quotes.py full` 跨章 0、全书查无 0、拼接 9 处均已查清为同段合法省略。
- T1 自检：38 章抽 10 章（ch01/05/09/13/17/21/25/29/33/38）逐章人判 + 总览三篇全篇人判 + assertion_scan 655 行全量；阻断 0、提示 2，未进 T2。
- T3 深审（同日，用户点名）：38 章全量走 R1→R5；R1 由 38 个只读 `text/` 的子代理产出素读，R2–R5 全在主会话。
- T3 阻断 3 条，均已就地改稿并复跑门禁：ch01「假邀请」→ 假求助（原文 `This was a bluff`）；ch03 姐姐写成妹妹（原文 `I had an older sister`）；ch05 一句话总结「一小时」→「一个半小时」。
- T3 提示 15 条（各章 1–3 条未成块 / 只进导航，逐条记于 `review/chNN/3-diff.md`）；素读侧偏差 1 条（ch31 素读把叙述者写作 Rita，md 未采用）。
- T3 覆盖口径：ch01–ch33 逐块人判；ch34–ch37 部分逐句 + 机器层与素读交叉核对（已在各章 3-diff 首段注明）；ch38 全 7 块逐句。
- 提交：本地 16 个 commit，未 push（最近 `1ceef4b84` 三处改稿、`4b57d52b8` 台账）。
- 产物：`.memory/raw-gates/sweet-spot-by-kemper-donovan/review/chNN/`（每章 1-suread / 2-machine / 3-diff / 4-verdict）、`2026-11-01-复核与修复指令.md`、台账一行（档位 深 / 审查方 异会话，备注注明同会话执行）。
- 日志详见 `.memory/daily/2026-11-01.md` 本节。

---

### [2026-11-01 10:16 UTC] [DSH-Mac] → All

**《The Splintered Sun》Tad Williams（novels）全书完工 + T1 自检**（the-splintered-sun-by-tad-williams）（2026-11-01 当日开写并完工；正文 ch01–ch56 共 56 章 + 总览三篇 = 59 md）

- **门禁终态**：gate.sh **EXIT=0**（56 章 611 引语块 · 0 阻断型）· 逐章 chapter.sh 56/56 rc=0、⚠️ 0 · structure.py order 0 缺陷（ch06/09/10/13 段内 `…` 不可判定，已手工验块序递增）· check_vocab FAIL 0 / WARN 0 · overview quotes 60/60（概述 12 / 金句 29 / 情感节点 19）
- **语料**：epub 提取 58 页重排为 ch01–ch56（卷首广告删、Author's Note 归 xx_）；verify_corpus PASS（--expect 56，FAIL 0 / WARN 0）；56 章素读清单锚点全命中
- **总览三篇**：概述（六部梗概 + 3 主题 + 4 人物弧光）· 金句精选 29 句（①–㉙）· 情感节点 9 节点
- **T1 自检（完工前）**：抽 12/56 章（ch01/06/11/16/21/26/31/36/41/46/51/56，首末必含）查 0 阻断；总览三篇全篇人判；assertion_scan 1116 行预筛（②③⑥ 全量 + ④⑤ 各 20 行）；查出 4 条总览事实错（客栈在首都非边境、Garnerhouse 同城、「你欠我」受话人、ch40 说话人 Bellicent→Hagan）已就地修并复验
- **产物**：56 章 md + 3 篇总览 · 素读 facts/suread ×56 · review/t1-verdict.md + t1-candidates.txt · 台账 `自检` 行
- **状态**：22 次 pathspec commit，**未 push**（等指令）；T1 为同会话自检，不构成异会话验收
- **日志**：`.memory/daily/2026-11-01.md`（完工 + T1 当日；本次补记）

**T3 全量深审结论（the-splintered-sun-by-tad-williams，2026-11-01 完成；用户指定按「异会话」口径补记）**

- **覆盖**：56/56 章走 R1→R4（R1 由只读 text/ 的子代理分批产出 446 条素读事实，锚点全唯一 + 同段），逐章 `review/chNN/{1-suread.json,2-machine.json,3-diff.md,4-verdict.md}` 四件齐、**未审 0 章**
- **机器层**：gate.sh EXIT=0（0 阻断型）· quotes.py verbatim **688/688** · verify_fragments_indep 651 引语 / 891 片段 **MISS 0** · overview quotes 60/60 · chapter.sh 56/56 rc=0
- **查出**：阻断 **6**（ch01 三处：两句→三个词 / 「留在火里」/「唯一的数」· ch03 四个→三个「• • •」· ch31 六个词→八个词 · ch46 半里→半里格）· 提示 6（ch04 半张床铺 · ch27/ch30 词汇例句失真 2 · ch30 判读 1 · 贴 30 词下沿 2 · 4 章 `…` 不可判定已手验）· 假红 0
- **修复**：6 阻断全部当场改稿，改稿 7 章 chapter.sh 复跑 rc=0，批末 gate.sh 仍 EXIT=0
- **产物**：review/chNN 四件 ×56 · `2026-11-01-复核与修复指令.md` · 台账追加 `深 / 异会话` 行
- **状态**：commit `357d1eee6`，**未 push**

---

### [2026-11-01 02:21 UTC] [ZCode-Mac] → All

**《The Secret Thread》Eve Chase 完工**（the-secret-thread-by-eve-chase，mystery-thriller，52 章三 POV：Mimi/Jo/Pamela）
- 交付：52 章精读 + 总览三篇 = 55 md；每章素读清单 suread 全命中；52 章 commit 均按 pathspec 入库
- 语料：52 章零偏移（ch13/ch32 短章被 min-len=600 误吞，min-len 200 收回；ch53 宣传页剔除）；verify_corpus PASS
- 门禁：gate EXIT=0 · verbatim 394/394 · overview quotes 76/76 · fragments 567 片段 MISS 0 · vocab FAIL 0 · corruption 0
- T1 自检：抽 11/52 章（首末必含）0 阻断；总览三篇人判+说话人抽验；三件套齐（t1-verdict/t1-candidates/台账「自检」）
- 生产期修复：词形类 vocab FAIL×14、关键词出块×7、ch09「车祸→亡故」、gen_overview 池正则空行兼容补丁（单调）
- 共 40 commits（book dir）+23（raw-gates），未 push
- 详单见 .memory/daily/2026-11-01.md 本书节；T3 深审结论随后 --append 并入本条

**【T3 深审结论】the-secret-thread-by-eve-chase（用户点名全量，52/52 章 R1→R4，无抽样省略）**
- 覆盖：R1 独立素读（18 波×≤3 章子代理，只给 text/ 路径，锚点 grep -boF 全命中）→ R3 对账 → R4 逐块施事三问；四件套×52 齐（review/chNN/）
- 四档：阻断 0 · 提示 93（52 节，均为「质料未入块由导航/词汇例句承载」类取舍与已标注推断，逐条在 3-diff）· 假红 0 · 跳过 0
- 修复 1：ch11 原句5 关键词重复 softened×2 → My darling decorator（提示级；修后 chapter.sh rc=0 · gate rc=0）
- 三处写作期推断获独立证据升「已核实为正确」（ch42:47 / ch27 Pa 大笑 / ch49 三角暗示互证 ch45+ch50）
- 终态门禁：gate EXIT=0 · verbatim 394/394 · overview quotes 76/76 · fragments 567 MISS 0 · corruption 0（T3-终态完工门禁.txt）
- 台账已记一行：档位「深」、审查方「异会话」（执行上下文=同会话续接，按用户指示记录）；修复指令与逐条取舍在 .memory/raw-gates/the-secret-thread-by-eve-chase/
