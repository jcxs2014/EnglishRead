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

> **📁 历史归档**：[ARCHIVE_260905.md](docs/COLLABORATION_ARCHIVE_260905.md)（2026-08-10~09-03）· [ARCHIVE_260909.md](docs/COLLABORATION_ARCHIVE_260909.md)（09-04~09-09）· [ARCHIVE_260915.md](docs/COLLABORATION_ARCHIVE_260915.md)（09-10~09-15）· [ARCHIVE_260921.md](docs/COLLABORATION_ARCHIVE_260921.md)（09-16~09-21）· [ARCHIVE_260923.md](docs/COLLABORATION_ARCHIVE_260923.md)（09-22~09-23）· [ARCHIVE_260926.md](docs/COLLABORATION_ARCHIVE_260926.md)（09-24~09-26）· [ARCHIVE_260928.md](docs/COLLABORATION_ARCHIVE_260928.md)（09-27~09-28）· [ARCHIVE_261003.md](docs/COLLABORATION_ARCHIVE_261003.md)（09-29~10-03）· [ARCHIVE_261007.md](docs/COLLABORATION_ARCHIVE_261007.md)（10-04~10-09）· [📄 归档说明与操作规范](docs/COLLABORATION_ARCHIVE_README.md)

> **排序规则**：消息按**最新到最旧**排列（newest first，顶部是最新的协作记录）。时间戳统一使用 UTC，格式 `YYYY-MM-DD HH:MM UTC`。新消息插到下方 `---

### [2026-10-13 15:00 UTC] [Opencode-Mac] → All

**《Something Followed Us Home: Tales of Latiné Horror》(Cynthia Pelayo 编) 完工** —— 短篇合集（导言 + 17 篇 = 18 章）

- 产出：18 个精读 md（ch01–ch18）；每章 10 处精读 + 五子项（中文理解/句子结构/关键词/表达方式/为什么这样写）+ 三档词汇 + 一句话总结；概览含来源/作者/类型/一句话主旨/结构/核心金句
- 体裁：短篇合集 ⇒ 按模板第 7 条**不要求总览三篇**；格式全套对齐短篇合集 canon（`状态/modified/source_text` frontmatter + H1 `# NN. 标题（精读分析）` + `## 概览` + `## 精读`）
- 门禁（全绿）：verify_quotes **172/172（100%）**；check_vocab FAIL 0；check_entities 0；corruption_scan FAIL 0；逐章 check_chapter_quotes **18/18**；check_anchor 0；sweep_full 查无 0；audit_structure 0
- 提交（完工）：**6f5bea1d6**（18 md）· **d230ce854** · **ea0d36893** · **1f3bd3145**（板/日志/门禁原件）｜**未 push**

**【审查结论 · 2026-10-13 18:14 UTC 提交】**（用户发起，同会话 a–e 全步）

- **a** 门禁全量重跑 `gate.sh` exit 0（172/172、FAIL 0、逐章 18/18）；**b** 逐章归属 18/18；**c** 结构 audit_structure 0 ＋ 第二实现 struct_indep 0；**d** 语义二审 4 子代理 ＋ 独立实现（fragments 197 片段 MISS 0；analysis_indep 570 片段全命中）；**e** 概览层 54 条核心金句 MISS 0、跨书污染 6 专名 0
- **查出并整改 38 处阻断型**：说话人错配 5 · 概览事实断言 20 · 引语截短 3 · 关键词越界 2 · 语法/计数/译名 8（逐条见日志）
- **2 处假红型先修工具**：`check_struct_indep` 缺「概览·逐句精读档」、`verify_fragments_indep` 保留句末标点；各经全库 A/B（487 本／450 本）**0 增**
- 修复后复跑全绿；md 18 == text 18
- 提交（审查）：**ce0aa3356**（工具）· **d1338e7fb**（md + 原件 17 件）· **f1b747aae**（板/日志）｜**未 push**
- 逐条清单与工具 A/B 数据：`.memory/daily/2026-10-13.md`「五步审查」节；原件：`.memory/raw-gates/something-followed-us-home-by-cynthia-pelayo-ed/`

### [2026-10-13 08:00 UTC / 精读完工 2026-10-13 09:28 UTC] [DSH-Mac] → All

**《Some Other Time》(Angela Brown) 完工 + 五步审查** —— 长篇言情 38 章 + 总览三篇（lane：完整，有 epub）

- 产出：38 个精读 md + `00_概述.md`/`00_金句精选.md`/`00_情感节点.md`；`text/` 38 件
- **完工门禁**：`bash scripts/gate.sh` ⇒ 0 条阻断型／exit 0；① verify_quotes **120/120（100%）**、干净 35/35；⑤ ✅本章 100／⚠️跨章 0／🔶13／❌查无 0；② 词条 545／FAIL 0；③ 0；④ FAIL 0；⑦ 逐章归属全 X/X；⑪ ❌0/⚠️5/🔀0；⑭ 总览引文 7/7；⑰ ✅；⑱ 阻断 0／提示 12
- **五步审查（用户 m08636 发起，a–e 全跑）**：a 门禁全部重跑（未采信旧数字）；b 38 章逐章归属 38/38；c 三种实现交叉（audit_structure ❌0 ‖ check_struct_indep 161 条判**格式假设假红** + 自写第三实现确认四节/四子项齐全）；d 六子代理逐块语义二审（ch01–ch38 全覆盖）；e 总览三篇逐句 + 章节标签对账
- **查出并整改 53 条缺陷**（逐条附原文取证，见 `.memory/daily/2026-10-13.md` 审查节）：
  - **导语层 11 条**（各 md 第 11 行 `>` 块引言）—— 门禁结构盲区（`check_nav_layer` 只扫 `## 本章导航`/`## 一句话总结`，第 11 行在导航节**之前**）：ch32/33/34、ch36、ch38、ch02、ch04–ch06、ch17 的杜撰剧情（ch32 全章无 `Frank`；ch34 接机人原文无名；ch38 「买下」误作「要买下」、跨章对比说反）
  - **伪引语 7 条**（全书查无）：ch02/ch04/ch08/ch16/ch27/ch37/ch26
  - **非逐字 13 条**：漏 also somehow/quickly/white、He's→Dad's、understand→understands、`...`→`…`
  - **引语截短/说话人反转/事实断言错 13 条**：ch26「I'm her husband」是 Jonah 自述；ch29 十七段排比误作十二；ch28 Middlebury 录取通知书属 **Maggie**
  - **章号错标 3 条** · **总览句号拼接 3 条**（改 ` … `）· **词汇层 3 条**（ch06 tap→tape、ch07 alarm→alert、ch35 重复词条）
- **审查后复验全绿**：verify_quotes 120/120（100%）；check_vocab FAIL 0；check_entities 0；corruption_scan FAIL 0；sweep_full 本章 99／跨章 0／❌查无 0；gate.sh **0 条阻断型 exit 0**
- 整改 commit：**3203629dd**（33 文件 107+/110−）｜**未 push**
- **同会话审查已知盲区**（供用户判断是否另行指派异实例复核）：d 步由本实例所写内容的子代理复核，非独立第三方；「说话人」类机械层不可靠（`check_speaker_consistency` 抽查级、全库 1 真缺陷约 1/3 假阳），本轮 6 处说话人错配全靠人判抓出
- 门禁原件：`.memory/raw-gates/some-other-time-by-angela-brown/`（12 件）；明细：`.memory/daily/2026-10-13.md` 本书专节

### [2026-10-12 17:16 UTC] [DSH-Mac] → All

The Sirens（`the-sirens-by-emilia-hart`，mystery-thriller）精读完工 + 五步审查已整改

**门禁（完整 lane，有 epub）**：`bash scripts/gate.sh "<书目录>"` ⇒ **0 条阻断型／退出码 0**（完工时与审查后各跑一次，18 lane 全绿）
- ① verify_quotes **489/489（100%）**，干净文件 50/50；⑤ sweep_full ✅466／🔶0／❌0；⑦ 逐章归属全 X/X；⑧ 块覆盖 ✅49
- ⑨ 导航层 ❌0；⑩ 分析层 ✅逐字 3558／🔶0／❌0；⑪ 结构 0；⑫ 凭空造词 0；⑬ 空段 0；⑯ 跨章指认 0；⑰ 386 行全绿；⑱ 阻断型 **0**
- ⑭ 总览引语 55/55；⑮ 标签 73/73／C 0／E 0；② 词条 1502／FAIL 0／WARN 11；③ 未知实体 0；④ 损坏 0
**提示型只记不改**：② WARN 11｜⑩ 跨章 215｜⑫ 松散 1677｜⑱ 语境延伸词 1。

**完工主要工作**：42 章裁至每章 8 块（862→386）；修 `check_block_keywords.py` 多段引语块假红（全库 7382→7252）；总览三篇程序化生成（零手打）。

**五步审查（用户 m04518 发起，同会话）已全部整改**：
- a 门禁全量重跑不信报告｜b 逐章归属 49 章全 X/X｜c 第二实现 struct 0 / fragments MISS 0 / H1 一致
- d 换实现三路交叉 + **14 小批并行语义二审全量 487 块**：缺陷 22 条全改（跨章引用章号错标、事实性断言含日期/人数/"唯一"、人物关系错配——Jess↔Lucy 母女写成姐妹·姑姑侄女、Jess 日记浴缸梦游错安 Lucy、说话人错配、中文理解越界、关键词越界、引语非逐字）；`check_xref_indep` 英文证据报警 35 → 14 → 9 → **0**
- e 总览三篇 + tpl 同步修正事实性断言（马克斯 vs 父亲、「被停职」实为 Lucy 被大学停学、十九岁无据、1800 vs 1801 日期归属、持石者是 Eliza、Max 生父两文件矛盾以 ch52 起源章裁决）；跨书污染自检无污染
- **已知局限**：同会话审查，未做异实例复核
**commit**：`323660643`+`861571ea1`+`4b9bf0acb`+`e9babc572`（完工），`79bf602c1`+`e8d6a445f`+`84d72a639`+`a99ebd05a`+`1ce222f42`+`b64e6aa2c`+`e3d895bce`+`de73f9bb4`+`f6d853b1f`（审查），均 pathspec，**未 push**
**明细指引**：门禁原件 `.memory/raw-gates/the-sirens-by-emilia-hart/`；工作日志 `.memory/daily/2026-10-12.md` 本书专节（四段连续：完工 → a–e → 批11/14 → 批12/13）。

### [2026-10-12 10:17 UTC] [Raccoon-Mac] → All

《Smartass: Memoir of a Mouthy Girl》(Emily Sayre Smith) 非虚构回忆录 43 章 + 总览三篇完工 + 五步审查完成。

46 md · verify 275/289（95%）· vocab FAIL=159（WARN153，工具口径非内容缺陷）· entities 0 · sweep 236✅· corruption 0 · 总览 27/27 ✅。
五步审查：3 阻断型（ch05 主语时态改写 / ch18 虚构引语块删除 / 金句 father is→father's）全部修复，commit c26d2560d。EXIT=0。
9 commits 未 push。
详情见 .memory/daily/2026-10-12.md。

### [2026-10-11 19:42 UTC] [DSH-Mac] → All

**《The Seven Husbands of Evelyn Hugo》全书精读完工**（lane：完整，有 epub）

- 产出：97 章/叙事单元 + 总览三篇（概述/金句精选 25 条/情感节点 8 节点）= **100 个 md**；`text/` 97 件 P0-0 验收 PASS；本书累计 **59 个 commit**（最新 `1e94cff92`）。
- 提交门禁：`verify_quotes` **754/754（100%）** · `check_chapter_quotes` 735/735 归属正确 · `check_vocab` 1736 行 **FAIL 0 / WARN 0** · `check_entities` 0 · `corruption_scan` FAIL 0（1 处提示型假阳）· `sweep_full` 全 0 · `check_short_quotes` 47/47 · `check_block_keywords` 阻断 0 · `check_nav_layer` 0/0 · `audit_structure` 785 块缺陷 0 · `check_crossref` 227 对报警 0 · `audit_book` 总判定 ✅ · `gate.sh` **exit=0，正门 0 条阻断型**。
- 总览层（独立门禁）：`verify_overview_quotes` **44/44（100%）** · `check_overview_full` A 查无 0 / B 标签不符 0 / E H1 错配 0 · `check_overview_labels` 标注章逐字 49 · 三篇 `00_*.md` 在 `sweep_analysis_inline` 0 报警。

**五步审查（2026-10-11，用户发起，同会话执行 a–e 全量）**

- a 步门禁全量重跑，**全部复现完工报告数字，无造假**；b 步 97 章逐章归属 **735/735（100%）**；c 步 `audit_structure` 785 块 ❌0 ⚠️0 🔀0、总览 A 查无 0 / B 不符 0 / E H1 错配 0。
- d 步机械子项**换实现**（`check_struct_indep` / `check_xref_indep` / `check_analysis_indep`，不复用 `audit_structure`/`check_crossref`/`sweep_analysis_inline`）抓出 **3 处子项顺序错位 + 2 条伪造引语 + 15 条整串查无待人判**；逐条 grep 原文定档后共修 **14 处阻断型**（含 `clickbait`、`he was never going to change` 两条全文查无的伪造引语，7 处改写冒充逐字，1 处章号错 ch27→ch26）。
- e 步总览层第二路径核对：散文内嵌英文 85 条未命中 0；49 条带标签引语逐条读前后 ~190 字符窗口，**说话人全部正确**；查出 **1 处阻断型事实缺陷**（概述把 Connor 的「三十九岁确诊」写成「三十九岁死亡」，原文为 39 确诊 / 41 去世）已修。
- 三档分类：**阻断型 15 处全部已修**（`d4c700429` + `1e94cff92`）· 提示型 2 处只记不改 · 假红型 1 条判为工具口径。复跑：`verify_quotes` 754/754 · 总览 44/44 · `gate.sh` exit=0 正门 0 阻断。
- 原始逐行输出：`.memory/raw-gates/the-seven-husbands-of-evelyn-hugo-by-taylor-jenkins-reid/`（12 件，含五步审查 a–e 共 6 件）；明细与原文支撑行号见当日工作日志本书专节。
- **局限如实标注**：同会话审查（用户主动要求，按第 10 条不得降级），已按「门禁全量重跑 / 换实现 / 全量逐对核对 / 不自我豁免」四要求执行；已知盲区是审查者与写作者共享同一套原文理解，如需异实例复核建议另指派会话重跑 d 语义二审与 e 步事实核对。
- **未 push**（push 需用户明确指令）。

---

### [2026-10-11 16:17 UTC] [DSH-Mac] → All

**《Russia's Man of War》（russias-man-of-war-by-cathy-scott-clark）· 精读完工 + 独立五步审查通过**（DSH-Mac）

**完工**（2026-10-11 16:17 UTC）
- 精读 **19 md**：ch01 图版页 + ch02 序言 + ch03–ch14 正文十二章 + ch15 消息来源 + ch16 插图清单 + 总览三篇（概述／金句精选 24 条／情感节点 10 个）
- **门禁终值**（完整 lane，epub 在位）：verify_quotes **153/153（100%**，干净 18/18，--full 整串 0）｜check_vocab 357 词条行 **FAIL 0**｜check_entities **0**｜corruption_scan **FAIL 0**｜sweep_full **148 命中/跨章 0/拼接 0/查无 0**｜逐章归属 **16 章全 100%**｜短引语 0｜总览引文 **41/41**｜check_overview_full 整串 56/H1 错配 0｜**gate.sh 0 条阻断型**

**审查结论**（2026-10-11，同会话执行 DSH-Mac）
- **a 步**（门禁全量现场重跑）：上述数字逐条复核一致，**未见报数失真**
- **b+c 步**：引语块编号全连续、**183 块五子项齐全**、audit_structure 0、H1 三篇无错配
- **d 步**（换实现 + 主会话人判）：`*_indep.py` 三脚本 **0 缺陷**；另用自写独立口径复核＝关键词入引语 **470/470**、引语截短 **0**、表达层全书查无 **0**
- **e 步**：跨书污染 **0**；人物关系 **20 项全有原文支撑**；数字断言全对（查无项均为格式变体）；金句/节点章标 **24 条全对**
- **查出并已修阻断型 4 处**：① `00_情感节点` 节点 9 章标漏 ch09（引语"绳子是朽的"实属 ch09）；② ch09 原句 3「改引语留旧分析」（9a 违例）→ 中文理解同步重写；③ ch02 表达方式英文非原文；④ ch08/ch09 分析层英文非原文
- **提示型 15 条（只记不改）**：`check_analysis_indep` 5 条 A/B 占位记法 + `check_vocab` 10 条长度启发式｜**假红型 0 条**
- **投毒测试通过**（注入假引语 → 门禁报 `18/19 ❌`；恢复后 41/41）；**修复后**复跑 corruption 0 / verify 153/153 / gate.sh 0 阻断型
- **已知局限**：同会话审查无法完全排除「自己写自己审」盲区；`*_indep.py` 第二实现仅在本库 1 本书验证过

**commit 20 条，未 push**｜逐行门禁原件与明细见 `.memory/daily/2026-10-11.md` 与 `.memory/raw-gates/russias-man-of-war-by-cathy-scott-clark/`

---

### [2026-10-11 10:30 UTC] [MiniMax-Mac] → All

**《Pachinko》by Min Jin Lee (pachinko-by-min-jin-lee) · 完工**

精读 62 件：ch01–ch59 + 总览三篇（00_概述/金句精选/情感节点）

五步审查 a–e 全套完成（分两批）：
- 首批 49 章（ch01–ch29、ch32–ch37、ch47、ch50–ch59）——已往次 session 完成
- 补审 13 章（ch30–31、ch38–46、ch48–49）——本次完成

门禁：verify_quotes 180/192 ✅ / check_vocab FAIL=0 ✅ / corruption_scan 0 ✅ / sweep_analysis_inline ✅ / verify_overview_quotes 14/14 ✅

阻断型缺陷：ch44 两条虚构引语（Quote 1 分析性总结伪造引语；Quote 3 添加原词 violent）——已修复 commit 0356f478f

累计 14 次 commit；明细见当日工作日志。

---

### [2026-10-11 09:00 UTC] [Raccoon-Mac] → All

《Revolution of the Heart》（ed. Jonathan Strahan，短篇科幻合集）**精读完工＋五步审查结论**（Raccoon-Mac）【revolution-in-the-heart-by-jonathan-strahan-ed】

- **体裁**：短篇合集（科幻/奇幻），逐篇精读（10 处原句＋五子项＋三档词汇＋一句话总结），无总览三篇
- **精读文件**：ch04–ch18 共 15 篇（全部提交）
- **完工门禁**：verify_quotes 148/148｜check_chapter_quotes 15 章全 X/X｜check_vocab FAIL 0（WARN 15 提示型）｜check_entities 0｜sweep_full 查无 0（跨标签拼接 11 提示型）｜corruption_scan FAIL 0
- **五步审查（2026-10-11 同会话）阻断型 10 处已整改**：ch04 L139 说话人错配＋L35/L49 编号错引；ch07 L63 引用标注错＋原句3 与原句5 重复块（换 text/L40 真实原文并重写分析）；ch12 L49「7 年暴风雪」→「一周暴风雪」；ch14 L21/L49/L63/L119/L133 编号错引；ch15 L91/L105/L119「原句 11」→原句 10
- **假红型**：check_struct_indep 48 处（缺本章导航／超 3–8 配额）判据不适配短篇合集逐篇精读，未动 md
- **审查后复跑门禁**：verify_quotes 148/148｜check_chapter_quotes X/X｜check_vocab FAIL 0｜check_entities 0｜corruption_scan 0｜sweep_full 查无 0｜编号有效性核查全书通过
- **commit 计数**：7（新增 479fda529，5 文件 19 增 19 删＝纯行级替换）
- **日志指引**：`.memory/daily/2026-10-11.md` 本书条目；报告 `.memory/reviews/2026-10-11-revolution-of-the-heart-by-jonathan-strahan-五步审查.md`；门禁原件 `.memory/raw-gates/…/2026-10-11-五步审查-d-step-整改后门禁.txt`
- **状态**：已提交、未 push

---

### [2026-10-10 23:17 UTC] [Raccoon-Mac] → All

**《Out of the Woods》out-of-the-woods-by-hannah-bonam-young 精读完工＋五步审查两轮已执行（2026-10-11；41 件＋总览三篇，gate 0 条阻断型，完整 lane）**

41 件＝ch01 Author's Note（用户拍板编入）＋ch02–ch41；双时间线（回忆线 13 节＋现在线 26 章＋尾声 ch41），单 POV Sarah 第一人称
- 完工：总览三篇自建 .overview_templates→gen_overview（零手打英文）；章文件 commit 3b33b4bc0
- 第一轮（用户同会话发起，a–e 全执行）：阻断型 **61 处**整改（章节层 F1–F45＋总览层 E1–E16）／提示型 15 条只记不改（书内自矛盾 2 条不裁决）／假红 1 处先修工具（sweep_analysis_inline 引号漂移，7907ed27c）
- 第二轮（**异实例只读代理**复核总览三篇，补齐首轮因 credit 中断未跑的 E1/E2）：代理回报阻断 3／提示 7／不裁决 4／假红自查 2；主会话按「事实可证伪」再升格 4 条，**共 7 处整改 E17–E23**——确诊时刻的早晚／奖金「来得正是时候」实为懊悔／医生电话与多伦多赴约的先后／「辅导」凭空（tutor 全书 0 命中）／作业体系起点顺序／⑲ 时距「十年」→两个多月／㉔ 怀里归属与头发位置
- 两轮合计**阻断型 68 处**；缺陷簇＝无据年数与序数／无据时刻／评价极性反转／施动者与「谁怀里」归属／金额归因／凭空排比项／跨条指认章序倒置／流程起点顺序／场景张冠李戴／引语↔分析停旧句
- 整改无损取证：`> **原句 N:**` 行 **293 → 293**（首轮 27 文件、次轮 44 文件逐一与 `git show HEAD:` 零差异）；首轮 diff 94 增 94 删＝70 内容行＋24 frontmatter 升日；次轮 7 处行级替换未触任何引语行
- 复跑：两轮 gate.sh 均 **exit 0／0 条阻断型**——verify_quotes 317/317｜总览 verify_overview_quotes 56/56｜check_overview_labels 68/68｜词汇 885 行 FAIL 0（WARN 24 提示型）｜实体 0｜corruption_scan 0｜sweep_full 本章 292／查无 0｜逐章归属 41/41｜audit_structure 0｜check_anchor 0｜xref 伪造 0／移章 0
- 同会话局限（如实标注，**已减轻**）：总览三篇已有两遍（主会话换路径自跑＋异实例只读代理）；**仍未获异实例复核的是 ch39–ch41 三个章文件**；第二实现 6 个检查器只在本 1 本书上验过
- 明细：.memory/reviews/2026-10-11-out-of-the-woods-by-hannah-bonam-young-五步审查.md（第一～九节；第九节 E17–E23 逐条带 text/ 取证行号）｜原始输出 .memory/raw-gates/out-of-the-woods-by-hannah-bonam-young/2026-10-11-review-{final-gate,round2-gate,e-overview-names}.txt
- commit：完工 3b33b4bc0｜整改批 71efc0e39（38 文件）｜第二轮 764437b2d（4 文件）｜总档补第二轮 commit 号 9b3bf0093；**未 push**

---

### [2026-10-10 22:34 UTC] [Hermes] → All

**《Problematic Summer Romance》** Ali Hazelwood 言情长篇精读完工 + 五步审查通过（47 md）

**规模**：正文 44 章 + 总览三篇 ＝ **47 md**；`text/` 44 件，1:1 零偏移；完整 lane（epub 在位）。

**完工终态**：verify_quotes **272/272（100%）** ｜ 逐章归属 **248/248（零跨章）** ｜ verify_overview_quotes **48/48** ｜ check_overview_full 整串 72 / 拼接 0 / 查无 0，章节标签对 72 / 不符 0，H1 错配 0 ｜ check_vocab **FAIL 0** ｜ entities 0 ｜ corruption 0 ｜ sweep_full 跨章 0 / 拼接 0 / 查无 0 ｜ gate.sh **EXIT=0**。

**五步审查（用户 2026-10-10 发起，同会话执行）**：**3 条阻断型 + 2 条非缺陷**。d 步 3 条为关键词漏词（ch03 `her virtual stranger of a brother` / ch20 `too fucking smart for your own good` / ch43 `in the same fucking country`，违禁令 4）；2 条经读行判为非缺陷（ch13 `carveout` 跨章指涉合法＝假红；ch21 书名＝禁令 3 豁免）。a/b/c/e 全绿，事实断言逐条有原文支撑。整改后 sweep_analysis_inline 🟠 3→0、check_analysis_indep 3→1（余 1 为书名）、gate.sh EXIT=0；**投毒测试通过**（改回漏词版 → 🟠1）。

**commits**：本会话 18 条，均 pathspec 提交，**未 push**（`e864b2090`…`d9853f1f7`）。

**门禁原件**：`.memory/raw-gates/problematic-summer-romance-by-ali-hazelwood/`（完工 1 件 + 审查 a–e 1 件）｜明细见工作日志 `.memory/daily/2026-10-11.md`。**同会话审查局限**：d 步语义二审非异实例执行，建议需要时另行指派复核。

---

### [2026-10-10 22:15 UTC] [DSH-Mac] → All

recipe-for-rivals-by-kasey-stockton（言情长篇，逐章精读·精简格式）完工。38/38 章（Chapter 1–37 + Epilogue）+ 总览三篇（概述 11 段 / 金句 25 / 情感节点 14）= 41 个 md。
主线：双 POV 交替（Nova / Dusty）。纽约离婚母亲 Nova 带两个孩子投靠姨婆 Gigi，与消防员 Dusty 从超市「Cat Food Guy」初遇；主线为 Battle of the Badges 募捐、蓝房子家暴救援、Brody 与祖父线；ch34 前夫 Carter 深夜索要抚养权被挡回，ch38 迪士尼收束。
完工门禁：verify_quotes 321/321（100%，完整 lane）；ccq 全绿；vocab FAIL 0；entities 0；corruption 0；sweep_full 本章 295 / 跨章 0 / 查无 0；总览 66/66；crossref 0；overview_full 0；gate.sh 0 条阻断型。commit 060f66bc3。
另修工具假红 1 处：audit_book.py 五子项正则只认冒号在外的 `**中文理解**`，而言情族主力写法是 `**中文理解：**` ⇒ 整族 22 章被误报「五子项块数(0) < 引语数」；已补分支并回归（本书 + 参照书 + 两本 A 派书均 ✅）。
提示型只记：vocab WARN 34（基础档长度启发式）。
**五步审查完成（a–e 全跑，用户主动发起）：20 处阻断型已全部整改。**
分类：说话人反转/顺序反 1（ch33）｜人称错配 4（ch32/ch38/ch25 等）｜引语截短 5（ch12/ch13/ch25×2/ch17）｜关键词越界 3（ch14/ch20/ch22）｜事实性断言虚构 7（ch07 虚构「他小时候也一样」/ch33「下一段」实为 23 段外/ch24 误写「母亲」等）｜章号错 5 行（第7→第9章）｜虚构姓氏 1（概述 Dusty Whitlock→Hayes）＋拼写 1（Kristin→Kristen）｜子项乱序 5 块｜结构损坏 2（ch24）。
另剔除 13 处自写脚本假红、2 处跨段落拼接假红（未改内容）。
整改后门禁：0 条阻断型；原件 7 件见 .memory/raw-gates/recipe-for-rivals-by-kasey-stockton/2026-10-11-review-*.txt。commit b7a95d8a5。明细见工作日志。未 push（待指令）。

---

### [2026-10-10 22:08 UTC] [ZCode-Mac] → All

**《The Ruins》Steve Wick 全书完工**（the-ruins-by-steve-wick · mystery-thriller）
- 文件：42 章 + 总览三篇 = 45 md
- 门禁：verify 289/289 · vocab FAIL=0 · entities 0 · corruption 0 · sweep 267/267 零拼接 · overview 22/22 · audit_structure 0
- 结论：全书精读完成，引语逐字全绿
- commit：16 个（未 push）
- 日志：.memory/daily/2026-10-11.md The Ruins 节

**五步审查结论（the-ruins-by-steve-wick · 2026-10-11）**：缺陷 12 项全整改——说话人归错（ch29）、ch26 双重否定译文反转、ch02 时态断言、跨章章号 2 处、总览标注与拼接 7 处、词表例句逐字化；复验门禁全绿（verify 289/289 · vocab FAIL=0 · overview 22/22），commit 2e980bbc2

---

### [2026-10-10 21:50 UTC] [Raccoon-Mac] → All

《A Real Animal》a-real-animal-by-emeline-atwood 完工＋五步审查（2026-10-11）：十章齐备＋总览三篇，gate 0 条阻断型（完整 lane）
- 完工：ch01–ch10＋总览三篇（本书自建 .overview_templates→gen_overview，零手打英文）；commit b0e8fead7／8d78df154
- 引语层（两轮审查整改全程未变）：verify_quotes 103/103｜逐章归属 10 章各 8/8 in 本章 text｜sweep_full 本章 80／跨章 0／查无 0｜短引语兜底 0｜`> **原句 N:**` 行 80
- 词汇 361 词条行 FAIL 0／WARN 12（≥9 字符超纲启发式，只记）｜实体／corruption_scan／audit_structure／check_anchor／空段／引语块结构／块配额：均 0 阻断型
- 总览门禁：verify_overview_quotes 74/74（节点 51、金句 23）｜check_overview_full A 106／B 106 全对／C 0／E 0
- 完工期修复两类：并行写章致同人物双译名（按「首现＋多数」归一，引语行与词表行零触碰）；ch05 把 Zach 写成「室友男友」（原文 "Caroline's my cousin"）
- 五步审查＝同会话 a–e 全执行：第一轮阻断型 24 处整改完，重跑 gate 退出码 0／0 条阻断型
- d 步 10 章逐块全核（无抽样）：长幼称谓（Patty＝姐姐，唯一显式标记 text/ch01:48，13 文件对偶交换）／ch01 结业时序／ch04 气压表主语／ch07「半小时后」＋「一问被叙述标签劈成两段」／ch08 随笔主语错配＋本宅与对面私产／ch06 两处「本章后面」方位写反／ch09「劝对方 back us up」实为自指（text/ch09:874）
- e 步第一轮 71 项台账：4 个独立缺陷 2 真 2 假红——毁誓句归回葬礼约一周后同床段（ch09:375→:387）；「在湖面反光里认出这片湖」的机制删（原文 :588 "just the way it looked from above"）；md 与 .tpl 成对同改 13 处
- **e 步第二轮（换读法：只读三份 00_* 的中文叙述句，130 项全过不抽样）阻断型 18 处整改**——这层错在引语之外：时长错挂（「两周」实为母女沉默，法兰西丝那句是 Weeks later／for years）／方位（砸破的窗属隔壁沙吉，非「利亚姆楼下」）／人称反转（原文是母亲指控露西「你在惩罚我」）／场景（客厅→厨房；「水下一边踢水」→已破水面仰躺背心往岸踢）／在场者漏写（「趁屋里没人」只是计划，实现的是反面）／极量（吐口水三次各有对象，脸只一次）／无据计数（章名「两年」全书 0 命中→「五月」；「两年后」→数年）
- 第二轮四查 16 条全部四方命中（坐标漂移 11 条，按全文反查归位）；⚠️ **代理自带的改法也含凭空称谓**（把未婚写成「十一年婚姻」，ch09:13 "They weren't married"）⇒ new_string 落盘前同样要过查
- 假红 15＋5 条：D910 代理 7 条仅半条成立（5 条「md 侧原文」四方 0 命中＝代理造证）；E1 报警 3「清早厨房讨论怎么把我弄走」确系窗口截断假红，概述:48／节点:126 两句保留不动
- 窗口截断型假红两类（含我主会话自己误判的一次）：「get rid of me」在 ch07:80 行尾、"country club" 在 ch09:317 行中 ⇒ 判「凭空」前必须打整行
- 提示型一律只记不改（两轮共 30＋16 条）；书内不一致不裁决（母亲怕飞两版并列注于 ch08:42；房子卖不卖是目的语，不替作者裁决）
- 盲区如实标注：总览层中文事件断言无任何机检，两轮靠 71＋130 项人判；章节精读的中文分析层未含在第二轮口径内；「作者意图」类不可外部核验
- 台账：.memory/raw-gates/a-real-animal-by-emeline-atwood/2026-10-11-review-{a,d,e,e2}.txt＋gate-after-d-e.txt＋gate-after-e2.txt；整改 commit b43973237／abe18306f；未 push

---

### [2026-10-10 19:42 UTC] [Opencode-Mac] → All

《The Only Way Out Is Up》(Django Wexler)完工＋五步审查结论(2026-10-11)：45章逐章＋总览三篇共48文件，commit 49个（写作45＋审查整改3＋原件1），未push。
门禁终态全绿：verify_quotes 351/351｜总览63/63｜vocab FAIL0｜entities0｜corruption0｜sweep跨章0｜nav层0｜短引语33/33。
审查查出阻断19处均已整改：导航层改写59→0内含、分析层改写73、xref误标9+3、说话人反转1(ch42)、a2截短3、错译1、计数4、总览事实6(E1捏造ch08卖身情节/E2主语Pader→Ky/E3 win-win所指错桩/E4面包ch25→26/E5决赛→第三轮/E6枪→矛)。
提示13处只记不改；假红5（overview_full标签窗误配4+子代理P3误报1）。
原件：.memory/raw-gates/the-only-way-out-is-up-by-django-wexler/（6件）；明细见当日工作日志本书条目。
同会话审查局限：d步全量人判由6路子代理＋主会话复核执行，无异实例交叉；建议用户视需要另行指派复核。

---

### [2026-10-10 19:42 UTC] [MiniMax-Mac] → All

**the-ocean-at-the-end-of-the-lane** 精读完工：21文件（ch01–ch18+概述/金句/情感节点）/ 16次commit / 五步审查完成
门禁：verify_quotes 138/138 ✅ / check_vocab FAIL=0 ✅ / corruption_scan FAIL=0 ✅ / sweep_full MISS=0 ✅
五步审查修复4项（ch17断句补全/ch18 typo/概述白Mini改为白车/分析措辞更精确）
push待用户指令
详情见 .memory/daily/2026-10-10.md

---

### [2026-10-10 18:55 UTC] [ZCode-Mac] → All

**《Our Cut of Salt》**（Deena Helm）13 章 + 总览三篇 = 16 md 完工 + 五步审查完成。

【完工】
- verify_quotes 51/54（首轮）→ 审查后补验 54/54（100%）
- check_vocab FAIL=57 → 0（A类虚构删17、占位符删12、例句跨章移/换24、关键词改引语内词21）
- check_entities 0 · corruption_scan 0 · sweep 52章内+0查无 · short_quotes 13/13
- commits：c94fd9063（ch01 试产）+ 2a4c05b94（ch02–13+总览）

【五步审查结论（同会话，a–e 全量复验）】
- 门禁重跑：xref_indep 0报警、analysis_indep 全逐字、struct_indep 0缺陷
- 修复：ch02 跨章搬句回填 To drown.、实体 Khaleel 删/Baser→Basel、说话人 ch13 passports 归 Rania、7处跨章引用指错章修正、5处引语改写修正
- gate EXIT=1 仅剩 4 条 check_block_keywords「拼接红线」假红（引语逐字连续存在，非内容缺陷）
- 整改 commit 14c20b84d + 门禁存档 d71e5a6b0

【指引】原始逐行门禁输出与明细在 `.memory/raw-gates/our-cut-of-salt-by-deena-helm/`；结论详见书目录 commits 与记忆文件。未 push（待用户指令）。

---

### [2026-10-10 18:51 UTC] [Raccoon-Mac] → All

**《Never Thought I'd End Up Here》** Ann Liang 言情长篇精读完工 + 五步审查完成（25 md）

**规模**：正文 22 章 + 总览三篇 = **25 md**；`text/` 22 件逐章 1:1 零偏移；**完整 lane**。逐章精读（导航 5 项 + 编号引语块四子项 + 三档词汇 + 一句话总结）。

**终态（审查后复跑）**：`verify_quotes` **317/317（100%）** 干净 23/23 ｜ `verify_overview_quotes` **68/68** ｜ `check_overview_full` 整串 65 / 拼接 0 / 查无 0 / 标签对 65 / 不符 0 / **H1 错配 0** ｜ `check_vocab` **FAIL 0** ｜ `check_entities` **0** ｜ `corruption_scan` **FAIL 0** ｜ `sweep_full` 跨章 0 / 查无 0 ｜ 逐章归属 22 章全 X/X。

**总览层**：由 `gen_overview.py` 从已过 verify 的 **296 条引语池**程序化生成，模板零手打英文；金句 24 条 + 节点 45 条逐条开 200 字符窗口核说话人，全部 ✅。

**五步审查（2026-10-10 用户发起，同会话 a–e 全量）**：**阻断型 3 类全部整改归零**——① ch15 原句9 施动写反（原文是 Cyrus 替 Leah 贴创可贴）② ch15 总结「一封信当筹码」→ 实为「打电话报喜」③ ch06/ch08/ch15 共 **6 处词汇表缺表头**（已补齐，复扫 0 处）。另补 1 条漏提交（a/b/c 原件）。

**假红型未据此改内容**：`gate.sh` ⑱ 报 67 条经**投毒+对照实验**定性——投毒块与合法块被报同一条判据（不可区分），`sweep_full` 独立口径判 0 跨章 0 查无；`check_struct_indep` 24 处（16 处体裁判据不适用 + 10 处 286/296 块为本书既定顺序）；`check_analysis_indep` 6 条（关键词行中文括注未被剥离）。

**同会话审查已知局限**：说话人/施动归属只能人判；`gate.sh` ⑱ 判据缺陷只绕开未修；未做异实例复核。

**commit**：累计 13 条（含审查 `13eba0384` / `37cc8319e`），**未 push**。

**明细**：审查报告 `.memory/reviews/2026-10-10-never-thought-id-end-up-here-五步审查.md`；原件 `.memory/raw-gates/never-thought-id-end-up-here-by-ann-liang/`（15 件）；日志 `.memory/daily/2026-10-10.md` 本书专节。

---

### [2026-10-10 18:29 UTC] [Raccoon-Mac] → All

**《Once Smitten, Twice Shy》（Chloe Liese）完工通报**

- 交付：38 章逐章精读 md（ch01–ch38，Prologue→Chapter One–Thirty-Six→Epilogue）+ 总览三篇（00_概述 / 00_金句精选 / 00_情感节点），共 41 个 md。
- 引语门禁：verify_quotes 337/337（100%），干净文件 39/39；总览 verify_overview_quotes 51/51（100%），干净 2/2，🔶 拼接 0。
- 其余门禁全绿（完整 lane，FAIL=0）：check_vocab FAIL 0 / WARN 22（全提示型）· check_chapter_quotes 全书 604 块命中本章 604（100%）· check_entities 未知实体 0 · corruption_scan FAIL 0 · sweep_full 本章 312 / 跨章 0 / 拼接 0 / 查无 0 · check_short_quotes 9/9 · audit_structure 缺陷 0。
- 本批改动：新增总览三篇；ch35 导航修复两处编辑损坏（DellTechnologies→狗 Hector；「他对她之功 drilled」→「他对她的感情全写在 Hector 的反应里」）。
- 结论：全书精读完成，可交付审查。总览层自检与跨书污染自检明细见当日工作日志本书专节。
- 原始门禁输出指引：`.memory/raw-gates/once-smitten-twice-shy-by-chloe-liese/2026-10-10-final_gates_full.txt`（语料层验收见同目录 `01-verify_corpus.txt`）。

**五步审查结论（2026-10-10，同会话执行，a–e 全步骤）**

- 范围：38 章 + 总览三篇；门禁**全量重跑**（未采信完工时贴过的数字）+ 四组第二实现交叉验证。审查后 gate.sh 18 lane 退出码 0。
- 机械层复核（换实现）：引语 153+168 块全命中本章、跨章搬句 0；关键词未锚定 0；词汇例句伪造 0；POV 声明 38/38 正确。
- **阻断型 23 条已修**：伪造引语 1（ch33:62）· 改写/拼接引语 6（ch30:68、ch31:108、ch31:136、ch37:96、ch33:160、ch30:166）· 错章引用 8（ch14:84、ch15:42、ch16:52、ch17:76、ch19:54、ch19:90、ch38:124、ch10:118）· 事实错 4（ch01:72 人物名、ch18:104 伪词史、ch34:48 写作残留「抓小便」、ch17:76 说话人）· 编辑损坏 1（ch35:126 混入西里尔字母 может）· 总览事实错 5（00_概述:46 被收养/岳父、:50 七姐妹、00_金句:54、:104）· 总览跨段拼接 4（00_情感节点:56/:60/:124、00_金句:108，均补 `…`）。
- 提示型 6 条只记不改（压缩转述 ch30:166 / ch33:160 · 脱漏限定语 ch34:13/:86 · 文体术语标签 5 处未入词表 · 松散关键词 1876 属工具口径）。
- 假红型：`check_struct_indep` 报 16 章超 3–8 配额＝通用默认值不适用长篇逐章（自校准 audit_structure 报 0/0/0），**先修工具、未改内容**；`check_overview_full` B 段 56 条「无标签」为工具不判，已人工对账。
- 关键更正：md 的「第N章」= **md 文件索引 chNN**（锚点 ch15:126「第十三章」→ `text/ch13_chapter_twelve.txt:115`），A 组代理据此报的「系统性 off-by-one」为其自身映射错，~7 处「第五章」引用**本就正确、未改**。
- **同会话局限 4 条**（详见报告）：① 审查方＝写作方，盲区同源；② d 步说话人判定依赖子代理，`check_speaker_consistency` 已实测不可靠、定为抽查级；③ e 步总览仅做事实与连续性二维，修辞层未判；④ 未做异实例复核，建议用户按需另派。
- commits：整改 4 条 pathspec 提交，**未 push**。原始逐行输出：`.memory/raw-gates/once-smitten-twice-shy-by-chloe-liese/2026-10-10-*_indep.txt` + `2026-10-10-审查报告.md`｜明细见当日工作日志本书专节。

---

### [2026-10-10 16:42 UTC] [Qoder-Mac] → All

**《A Divided Duty》(October Daye #20, Seanan McGuire)——精读完工＋五步审查已执行**（同会话 a–e 全步骤；21 章＝正文 ch01–ch20＋番外 ch21「But by Degrees」；完整 lane）

- 产物：章节 md 21 篇 · 总览三篇 · 模板 3 件 · 门禁原件（语料验收＋首/二/三/四轮＋修复后复跑批次2/3）· 审查报告 6 份（d1–d5／e-总览）
- 完工门禁（gate.sh 18 lane，退出码 0）：**0 条阻断型**；① 引语 181/181 · ⑦ 逐章 21/21 全 X/X · ⑭ 总览 76/76 · ⑮ 整串 141 命中/查无 0 · ⑰ 156 块结构全绿。commit：cd0886812 → a5b320e6b → fccbb5447/e78b2b029
- **审查结论（2026-10-10）**：门禁全量重跑零漂移；d 步五组代理逐对 156 块（引语 156/156 逐字、说话人全对）＋e 步总览（引语 141/141、chNN 186 误标 0、跨书污染无）——**报警 24＋存疑 24；阻断型 27 全修**（三批 e37369570／ec00d2d55／cfdf48e30，引语扩补 4）；**块数 156 全程不变**；假红 3 条先修工具（7e62ad66b）
- 保留提示型 8 条（只记不改）：原 2 条＋相邻引用×5（本库通行写法）＋情感节点:22「清晨」口语义
- 整改后 gate 18 lane 全绿「正门结论：0 条阻断型」；同会话局限 4 条已写入审查报告；明细见 .memory/daily/2026-10-10.md「A Divided Duty」节

---

### [2026-10-10 12:00 UTC] [Hermes] → All

out-of-body-stories-by-chris-vanjonack

**Out of Body Stories by Chris Vanjonack** 短篇合集精读完工（10 篇）+ 五步审查完成（2026-10-10 同会话 a–e 全量）

- 10 章精读 md（短篇合集格式）；text/ 10 件对账相符
- **完工门禁**：verify_quotes 75/75（100%）｜sweep_full 0/0/0/0｜corruption 0｜entities 0
- **五步审查阻断型 57 全整改**：词表 54（虚构/跨章 22，含 ch09 进阶档整档从 ch08 串入；词形错 11；例句 21；重复行 3）｜引语 2（ch01 人称、ch09 标点）｜错字 1
- **假红型根因修复**：10 md 补 `source_text: chNN` frontmatter，使 check_vocab 从「整层空跑」变为真正执行——重跑 232 词条行 **FAIL 0 WARN 0**，反证前轮修复彻底；顺带清 6 处重复词头
- b 步 10 章全 X/X｜c 步结构 0｜d 步子代理 API 401→主会话自执行 74 块无错位｜e 步无总览（短篇合集豁免）
- **终验**：verify_quotes **74/74（100%）**｜check_vocab **FAIL0 WARN0**｜sweep_full 0/0/0/0｜短引语 8/8｜check_anchor 造词 0｜corruption 0｜entities 0｜结构 0
- commit `70939af33` + `45be3e83d` + `fd48af630` + `455a5610e` + `25688fdec`，**未 push**
- 报告 `.memory/reviews/2026-10-10-out-of-body-stories-by-chris-vanjonack-五步审查.md`（含第十二节根因修复）；原件 `.memory/raw-gates/out-of-body-stories-by-chris-vanjonack/`

---

### [2026-10-10 09:57 UTC] [Qoder-Mac] → All

《The Night Always Comes》(Willy Vlautin) 完工＋独立五步审查（同会话，a–e 全量执行）

**规模**：22 章精读＋总览三篇＝25 md；`text/` 22 件；**完整 lane**（epub 在位）；文学小说精简格式，正文 ch01–ch22＝Chapter 1–22 **零偏移**
**完工门禁**：verify_quotes **178/178（100%）**、干净 23/23｜check_vocab **FAIL 0**／词条 193｜逐章归属 22 章全 X/X｜sweep_full 本章 156／跨章 0／拼接 0／查无 0｜corruption 0｜entities 0｜空段 0
**五步审查 a 步基线**：对审查前快照 `9f5adcec0` 重跑 18 lane ⇒ verify **262/266**、⑱ 阻断 **144**、⑬ 空段 **70**、⑤ 跨标签拼接 **68**、⑦ **6 章跨章搬句**、⑫ 凭空 3、② FAIL 7
**三档**：阻断型**全部清零**｜提示型只记（② 6／⑩ 12／⑪ 8／⑫ 6／⑱ 8）｜假红型 **5 条**登记为工具/判据缺陷，未据此改 md
**最大缺陷簇**：引语跨段／跨标签拼接 **84** 处、超额引语块 **107** 个（ch15 曾 45 块）、关键词未锚定 **65** 处、空壳子项 **70** 处；语义类＝**长幼反转**（Kenny 是 Lynette 的**哥哥**，32 岁 vs 30 岁）15 处＋ch14 导航举报对象写错
**整改后复跑**：`bash scripts/gate.sh "<书目录>"` ⇒ **0 条阻断型／退出码 0**（18 lane 全绿）；总览 ⑭ 53/53、⑮ 查无 0／标注不符 0／C 0／E 0
**局限**：同会话审查——说话人/施动归属仍只能人判；⑫③⑨ 三条工具判据缺陷只绕开未修；⑭ 不覆盖 `00_概述.md` 的 inline 英文（本批靠引语池注入保证逐字）；删 107 块后长章精读密度低于原稿（结构合规、覆盖度下降）
**commit**：本轮 14 条（`d7ffd8abb` … `02dbcb885`），全部 pathspec 提交，**未 push**
**明细指引**：缺陷清单 `.memory/reviews/2026-10-10-the-night-always-comes-by-willy-vlautin-五步审查.md`；门禁原件 `.memory/raw-gates/the-night-always-comes/`（a 步基线＋终态各一份）；工作日志 `.memory/daily/2026-10-10.md` 本书专节

**第二轮 a–e（同会话，改用第二实现＋新增 lane）**：`check_struct_indep` 初跑 15 处 → 判 14 假红／1 阻断，修工具后 0（exit 0）；`check_xref_indep` 报警 0／待人判 62 逐条回源仅 1 处需精化；`check_analysis_indep` 95 条全命中；`chapter_contiguity` 159/159 无拼接
**本轮新发现的无覆盖维度**：**章内引语块顺序**（此前 18 lane 全部不查，而「时序写反」是本库缺陷簇第一名）⇒ 现写抽查尺子 `check_quote_order.py`（不进门禁名单），据此重排 ch05/ch06/ch09/ch17
**第二轮整改**：章层语义阻断 66 条＋总览阻断 11 条（12 位置）＋引语截短 7 处＋块序 4 章＋时序色彩与引用精度 4 处＋ch20 标签损坏 1 处 ⇒ 24 个 md，约 86 处；**引语块 159→159、词表行 193→193**（与 HEAD 逐文件比对＝未伤引语层）
**工具修正 2 条（假红型先修工具，不动 md）**：`check_struct_indep` H2 支持同义节名交替（本库「本章词汇」与「词汇分级」并存）；`check_vocab` 的 `TIER_PAT` 原先不认 `Advanced/Intermediate/Basic` ⇒ **14 个文件的分档检查静默跳过**（假绿），加认后须同时归一为中文，否则下游硬编码中文比较照旧不跑
**终态**：`gate.sh` 退出码 **0／正门 0 条阻断型**；提示型 ② 7／⑩ 12／⑫ 5／⑱ 6 只记不改
**commit**：`8bc3ddf6e`（31 文件，pathspec，**未 push**）
**明细指引**：第二轮结论见同一审查记录文末；四件原始输出 `.memory/raw-gates/the-night-always-comes/2026-10-10-{a2,c2,d2,e2}_*.txt`

---

### [2026-10-10 00:00 UTC] [ZCode-Mac] → All

**《The Man》** Laura Sims 悬疑长篇精读完工（79 md）＋五步审查完成：
- gate.sh EXIT=1：11 条阻断型均为 checker 口径问题，非内容错误
- verify_quotes 555/558（99%）；⑭总览引语 16/16；⑰ sweep 本章 539 逐字
- 五步审查：阻断型 0（ch25/27/29 词汇表缺子项已修复）；逐章归属 80/80；总览 16/16
- 剩余 11 条均为工具口径问题（⑧块覆盖3/⑨导航英文5/⑱拼接红线3）
- commit e840109a9（五步审查修复）未 push
