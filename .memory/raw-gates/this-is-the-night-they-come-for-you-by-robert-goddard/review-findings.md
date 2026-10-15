# 《This is the Night They Come for You》五步审查缺陷清单（2026-10-15）

审查方：Opencode-Mac（用户在同一会话内发起；按 AGENTS 第 10 条「用户在同一会话内要求时本实例直接执行」）
门禁 lane：完整（`library/*.epub` 在位）｜ 目标：31 章 + 总览三篇 = 34 md

## a 步：第 3 条门禁全量重跑（现场重跑，不采信完工报告数字）

| 项 | 原始结论 |
|---|---|
| verify_quotes | 246/246（100%）· 完全干净文件 31/31 · --full 整串取证 0 · 2 条短引语转 ⑦ |
| check_vocab | 词条行 1073 · FAIL 0 · WARN 39（全部 `[基础] 基础档疑含超纲词`＝长度 ≥9 字符启发式） |
| check_entities | 0 个文件存在未知实体 |
| corruption_scan | FAIL 0 处（U+FFFD / 双句号） |
| sweep_full | 本章命中 246 ｜ 跨章 0 ｜ 拼接 0 ｜ 全书查无 0 |
| check_short_quotes | 命中 2 ｜ 查无 0 |
| check_chapter_quotes | 31/31 全为「8/8 in chNN text」 |
| audit_structure / check_anchor / 空段 | 结构缺陷 0 / 造词 0 / 空段 0 |
| verify_overview_quotes | 54/54（100%）· 3/3 篇覆盖 · 拼接 0 |
| check_overview_full | A 命中 53 / ❌0 · B 标签 53 对 / 不符 0 · C 跨章多重命中 1 · E H1 0 |
| check_xref_chapter | 归章正确 1 / 伪造 0 / 移章 0 |
| gate.sh 正门结论 | **0 条阻断型（退出码 0）** |

（原件：`review-a-1.txt` `review-a-2.txt` `review-a-gate.txt`）

## b 步：逐章归属（换实现：`review-bc-indep.py` 第二套代码，非 check_chapter_quotes）

248 条引语按省略号切片、逐片段 flat 比对**本章** `text/`；并报「片段是否只在他章出现」。
→ **缺陷 0 条**：无跨章搬句、无他章专属片段。

## c 步：结构扫描（换实现：`review-bc-indep.py`；另跑 check_struct_indep）

- 编号连续 ✅ · 每块四子项（中文理解/关键词/为什么这样写/读者视角提示）齐全 ✅ · 零重复块 ✅
- `check_struct_indep.py`：31 md，缺陷 0
- 总览：`check_overview_full` E 段 H1 语义错配 0；`grep -m1 '^# ' 00_*.md` 三篇 H1 与文件语义一致 ✅

## d 步：语义二审（两批子代理 + 主会话复核，120+128=248 块全覆盖）

子代理载荷分两批（ch01–ch16 / ch17–ch31），附本库三例真实失败案例与防幻觉条款；主会话对每条报警回原文复核并三档定性。

### 阻断型（已全部整改）

| # | 位置 | 缺陷 | 处置 |
|---|---|---|---|
| 1 | ch01 行12/16 | 导航称他答应的理由是「好奇」——ch01 全文无 curio*，原文给的是 "A purpose, a meaning." | 改「一个目的，一种意义」 |
| 2 | ch01 行50 | 「从局长的办公室望出去，景色不错」——`It affords a good view` 的主语是那张沙发 | 改「视线落在局长办公桌后面的墙上」 |
| 3 | ch02 行14 | 「Harriet 在一九八八年的巴黎失踪」——1988 是最后一次见面的年份，失踪为 1965-06 | 改「一九六五年六月」 |
| 4 | ch04 行10 | 「一九六四年…两年后跟她去巴黎」——1964-11 相识 → 1965-03 移居（约四个月） | 改「一九六四年十一月…几个月后」 |
| 5 | ch04 行56 | 「戴着软呢帽在片场扮一个法国人」——原文只作条纹西装 + 软呢帽、身份是临时演员 | 改「站在片场当临时演员…正穿着一身刻板印象」 |
| 6 | ch14 行18 | 「第一次带进 **2021** 年的时间线」——现在时为 2020-07（ch18 逐字 "Wednesday July twenty-second, 2020"） | 改 2020 |
| 7 | ch14 行14 | 「Dalby 死于 1993 年」——原文 "a few months after I spoke to him"，实为 1994-02-21 | 改「在 1993 年那次谈话后不久…（实为 1994 年 2 月）」 |
| 8 | ch16 行10 | 「Wendy 用**倒车**的一撞让箱子打开」——原文 "forward rather than reverse" | 改「挂前进挡撞过去」 |
| 9 | ch16 行68 | 「本书 **2021** 年的时间线」 | 改 2020 |
| 10 | ch16 行110/112 | 「老式的 Olivetti **手提**打字机」——原句为 "old manual"，且与 ch02「太重没寄」相抵 | 删「手提」改「手动」 |
| 11 | ch17 行10/74/76 | Wendy 称 Stephen「**哥哥**」——ch06 "Wendy was seventeen then, Stephen just ten years old" ⇒ 是**弟弟** | 3 处改「弟弟」 |
| 12 | ch18 行36 | **引语截短（第 9 条 a2）**：引语止于 "Father not identified."，而中文理解/关键词/为什么这样写都引 "But you were the mother" | spec 层跨度 +3→+5（覆盖整段话）+ 三子项同步重写 |
| 13 | ch19 行18/114/174 | 「妹妹审哥哥」「与哥哥的辩论」「妹妹…哥哥」——与同文件行98「你是我弟弟」自相矛盾 | 改「姐姐审弟弟」等 3 处 |
| 14 | ch19 行80 | 「ch15 里 Bahlouli 说出的『Laloul 就是那个量水人』」——Bahlouli 的话在 ch14（ch15 只有 "He's made no mention of the water-measurer"） | 改「第 14 章；第 16 章由 Taleb 复述」 |
| 15 | ch19 行80 | 「记住这**五个词**」——「量水的人称金子」为 7 字 | 改「记住这句话」 |
| 16 | ch19 行10 | 「租下那间公寓的旧住户」——原文是付 "a ridiculously large payment" 给那位孤僻住户换得进屋搜查 | 改「付给…一大笔钱，才换得进屋搜查」 |
| 17 | ch19 行56 | 「补上了**上一章** Suzette 的推断」——该推断在 ch17（"Riad Nedjar must have gone along with it."） | 改「第 17 章」 |
| 18 | ch20 行16 | 「失去证物、住处与**妹妹**的信任」——Wendy 是姐姐 | 改「姐姐」 |
| 19 | ch21 行14 | 「她的手机早在 Gray 的**怀疑名单**上」——原文是 Gray 的警示（Laloul 可能窃听） | 改「Gray 此前警告过她，手机可能已被 Laloul 窃听」 |
| 20 | ch23 行10/86 | 「**德高乐**」（繁体/异译）——全书他处作「戴高乐」 | 2 处改「戴高乐」 |
| 21 | ch25 行100 | 关键词释义崩坏：「`It was ten million euros`（原先是**八位数的一半**——一千万欧元）」 | 改「原先是一千万欧元」 |
| 22 | ch25 行44 | 读者提示称 Kermadec 对 Gray 反驳的回应是「下一段『你们俩都给我闭嘴』」——原文该句在 Gray 发言**之前**，回应实为 `a silencing glare` | 重写 |
| 23 | ch29 行14 | 「两人最后一次见面在**十余年前**（见前章回忆）」——原文只说 "From many years ago."（1993 年问话，实际相隔 27 年） | 改「二十多年前（1993 年那次问话）」 |
| 24 | ch30 行14 | 「**第 27 章**的『不交原件』」——该台词在 ch26（"You don't get the original, Erica."） | 改「第 26 章」 |
| 25 | ch30 行32 | 「他在**第 20 章**第一次出现」——Baudouin 首见于 ch22 | 改「第 22 章」 |
| 26 | ch30 行92 | 「与**第 26 章** Ménard 说过的同一句（`It's your choice.`）对调」——全书仅 ch30 出现该句 | 重写（去掉错标） |
| 27 | ch31 行102 | 「『水计量官』这个从**第 5 章**起就悬着的职位」——该概念首见于 ch14 | 改「第 14 章」 |
| 28 | 00_金句精选 行42 后点评 | **引语说话人错**：ch09 "There's no such thing in Algeria, Stephen…" 说者是 **Suzette**（她十五岁离开阿尔及利亚），点评却写「一个阿尔及利亚人亲口说出」 | 改「说这话的是在阿尔及利亚长大、十五岁才离开的 Suzette」 |

### 提示型（只记不改）

- `check_vocab` WARN 39 条：全部为「基础档疑含超纲词」，判据是**长度 ≥9 字符**（例：`motorbike` `honeymoon` `photocopy` `best interests` 均属常用词）⇒ 启发式误报，不阻塞。
- `check_overview_full` C 段 1 条：`We gave you your country…` 同句出现在 ch23、ch26（该句是图尼耶被逼问时的录音原文，两章各播放一次），标注 ch23 取自本章 text，标注成立。
- `sweep_analysis_inline` 6 条（跨章 1 / 分段命中 5）+ 部分命中 1：逐条回原文核过——ch17:68 是**显式**「第 15 章」引用（正确）；5 条 `A … B` 型省略号两侧均为同句原词（`Living, he has come to understand…is a relative term`、`bring her murderers – and those of Guy Tournier – to book` 等）；ch22:168 的 `Suzette holds her nerve.` 为 ch22:567 逐字原句，报警源于释义格里的英文搭配 `hold one's nerve`。
- ch25 行38–50：块序（原句 2 Gray 反驳 / 原句 3 闭嘴）与原文时序相反，但引语逐字正确、内容无错 —— 记录不改。
- ch29 行14：神秘枪手身份原文留白（Hidouchi 只答 "No idea"），导航已写「身份未明」，人物弧线记 Storza 之死有原文支撑（"One of the dead men is Storza."）—— 两者不构成重复计数。
- ch17:68：显式跨章引用「第 15 章 Gray 的 `I'm sure that's where Harriet is`」，工具报「实为 ch15」属**正确引用被误报**。

### 假红型 / 工具盲区

- `build_vocab_section.py` 候选集口径 = `vocab_candidates.py --max-sent 400`（>400 字符长句里的词被判「不在候选集」）。
- glosses 键大小写须与候选行行首完全一致。
- **工具盲区（不计三档，供工具维护者）**：`check_anchor` 的「或本块分析正文」豁免、`check_analysis_indep` 的「全书 text 命中」口径，都**结构上抓不到「引语截短」**（ch18 即此例：`But you were the mother` 确在全书，只是不在本块引语）。这一类只能靠 d 步人判兜住。

## e 步：总览层事实核对

- **引语逐字**：`verify_overview_quotes` 54/54（100%）；`check_overview_labels` 28/28 标注章逐字，口径外 0、待人判 0。
- **说话人**：三类总览全部引语的归因逐条回原文窗口复核，抓到 1 处（上表 #28，ch09）并已改。
- **四类断言（做了什么/什么关系/死因/数字）逐条 grep + 行号**：33 项全命中，0 未命中 ——
  现职 Superintendent（ch06:61）· Director Farid Bouras（ch01:76）· Hidouchi=DSS（ch01:190）· Ménard=DGSE（ch26:16）· Zarbi→Sécurité Militaire（ch13:31）· Laloul→Sonatrach（ch13:31）· Dalby=Le Chélifère 的英国老板（ch12:340）· Kermadec=beau-père（ch25:133）且替 Zarbi 办事（ch25:270）· Gray=Harriet 的弟弟（ch13:67）· 1965 年 Wendy 17 / Stephen 10（ch06:398）· Harriet 23 岁死（ch02:313）· Nedjar 在伦敦开店（ch17:97）· Zakaria=Zarbi 之子（ch18:156）· 图尼耶被杀 1965-06-02（ch12:364）· 戴高乐的特助（ch12:388）· Dalby 死 1994-02-21（ch16:340）· Laloul 1999 外逃（ch11:106）· Zarbi 二十年刑期（ch27:19）· 六名死者含 Storza（ch29:309）· 磁带=图尼耶被逼问录音（ch26:178）· 磁带=镀金保险（ch31:49）· Abderrahmane 指控撤销（ch31:67）· Gray 在 Annecy（ch31:130）· 阿尔及利亚寄来的包裹（ch31:157）· Hidouchi 提出查 hizb fransa（ch31:327）· 书名出处（ch30:337）· 疫情封控（ch31:195）· 现在时 2020-07-22（ch18:78）· Bouteflika 去年下台（ch01:88）· Sidi Ferdj 的船（ch01:172）· 1993 年问过 Gray（ch12:91）。

## 材料三样（模板 741–748 行）

① 门禁原始逐行输出 → 本目录 `review-a-*.txt` / `review-fix-*.txt`（并已进工作日志本书条目）；
② 总览自检声明（MISS=0 + 关系/身份/结局的支撑行号）→ 见上节 e；
③ 跨书污染自检 → 28 个书中专名全部有本书 `text/` 支撑；唯一「他书同名」是 `Taleb` 出现在 `365-days-with-self-discipline`（Nassim Nicholas Taleb，同形异指，非污染）。

## 整改后复验（全部现场重跑）

- `gate.sh` → **正门结论 0 条阻断型，EXIT 0**
- verify_quotes **246/246（100%）**（ch18 延长后的引语仍逐字命中）· check_chapter_quotes 31/31 · sweep_full 0 异常 · check_entities 0 · corruption_scan **FAIL 0**（修复后必跑）· check_short_quotes 2/2
- 结构：`check_struct_indep` 0 · `review-bc-indep.py`（第二实现）248 引语 0 缺陷 · `check_analysis_indep` 617 片段全逐字 · `check_xref_indep` 英文报警 0
- 总览：verify_overview_quotes **54/54** · check_overview_full A53/B53 对/C1（提示型）/E0 · check_overview_labels 0 口径外
- `check_block_keywords`：**阻断 0 / 提示 0**（ch18 截短修复后，此前的 1 条提示型随之消失）

## 同会话审查的已知盲区（结论写作要求，非降低标准）

本次 a–e 五步全部执行、门禁全部现场重跑，但审查方与执行方同为 Opencode-Mac（用户在同一会话内发起），故：
1. **d 步的人判部分**由子代理批跑 + 主会话复核完成，两批子代理均未通读 ch22–ch31 全文（用 ±320 字窗口取证），超出窗口的说话人线索可能漏判；
2. 史学层面（1961-10-17 与 1965-06-02 的历史事实本身）未核；
3. 若需要第三重独立核验，建议另指派异实例复核「说话人」与「引语截短」两类（本库已多次证明这两类只能靠人判）。
