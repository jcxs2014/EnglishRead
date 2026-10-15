**《This is the Night They Come for You》五步审查（a–e 全执行）· 缺陷清单与整改**（2026-10-15 UTC，用户同会话发起；审查方＝执行方 Opencode-Mac）

**a 步（第 3 条门禁全量现场重跑，不采信完工报告数字）**：
```
verify_quotes 246/246（100%）· 干净文件 31/31 · --full 整串取证 0 · 2 条短引语转 check_short_quotes
check_vocab 词条行 1073 · FAIL 0 · WARN 39（全为 [基础] 基础档疑含超纲词＝长度 ≥9 字符启发式）
check_entities 0 · corruption_scan FAIL 0 处 · sweep_full 246 命中/跨章 0/拼接 0/查无 0
check_chapter_quotes 31/31「8/8 in chNN text」· check_short_quotes 2/2
audit_structure 0 · check_anchor 造词 0 / 松散 0 · 空段 0 · check_quote_blocks ✅ · check_xref_chapter 1/0/0
verify_overview_quotes 54/54（100%）· check_overview_full A53/❌0 · B53 对/0 不符 · C1 · E0 · check_overview_labels 28/28
gate.sh 正门结论：0 条阻断型（退出码 0）
```
原件：`review-a-1.txt` / `review-a-2.txt` / `review-a-gate.txt`

**b 步（换实现：`review-bc-indep.py` 第二套代码）**：248 条引语按省略号切片、逐片段 flat 比对**本章** text/，并报「是否只在他章出现」→ **缺陷 0 条**（无跨章搬句）。
**c 步（同一第二实现 + check_struct_indep）**：编号连续 ✅ · 每块四子项齐全 ✅ · 零重复块 ✅ · `check_struct_indep` 31 md 缺陷 0 · 三篇总览 H1 语义 0。

**d 步（语义二审：两批子代理覆盖 248 块 + 主会话逐条回原文复核）→ 28 条阻断型**：
1. ch01 行12/16 导航称理由是「好奇」——ch01 全文无 curio*，原文给的是 `A purpose, a meaning.` ⇒ 改「一个目的，一种意义」
2. ch01 行50 「从局长办公室望出去，景色不错」——`It affords a good view` 主语是那张沙发 ⇒ 重写
3. ch02 行14 「Harriet 在一九八八年失踪」⇒ 一九六五年六月（1988 是最后一次见面的年份）
4. ch04 行10 「两年后跟她去巴黎」⇒ 1964-11 相识 → 1965-03 移居（约四个月）
5. ch04 行56 「在片场扮一个法国人」⇒ 原文只有条纹西装 + 软呢帽、身份是临时演员
6. ch14 行18 「第一次带进 2021 年的时间线」⇒ 2020（ch18 逐字 "Wednesday July twenty-second, 2020"）
7. ch14 行14 「Dalby 死于 1993 年」⇒ 「1993 年那次谈话后不久（实为 1994 年 2 月）」
8. ch16 行10 「Wendy 用倒车的一撞」⇒ 原文 "forward rather than reverse"（挂前进挡）
9. ch16 行68 「本书 2021 年的时间线」⇒ 2020
10. ch16 行110/112 「Olivetti 手提打字机」⇒ 原文 "old manual"（且与 ch02「太重没寄」相抵）⇒ 改「手动」
11. ch17 行10/74/76 Wendy 称 Stephen「哥哥」⇒ 弟弟（ch06 "Wendy was seventeen then, Stephen just ten years old."）
12. ch18 行36 **引语截短（第 9 条 a2）**：引语止于 "Father not identified." 而分析引 "But you were the mother" ⇒ spec 层 Q2 跨度 +3→+5（整段话）＋中文理解/为什么这样写/读者视角提示三子项同步重写
13. ch19 行18/114/174 「妹妹审哥哥」「与哥哥的辩论」「妹妹…哥哥」⇒ 姐姐/弟弟（与同文件行98「你是我弟弟」自相矛盾）
14. ch19 行80 「ch15 里 Bahlouli 说出的『Laloul 就是那个量水人』」⇒ 第 14 章（ch15 只有 "He's made no mention of the water-measurer"）
15. ch19 行80 「记住这五个词」⇒ 「量水的人称金子」是 7 字 ⇒ 改「记住这句话」
16. ch19 行10 「租下那间公寓的旧住户」⇒ 原文是付 "a ridiculously large payment" 给孤僻住户换得进屋搜查
17. ch19 行56 「补上了上一章 Suzette 的推断」⇒ 第 17 章（"Riad Nedjar must have gone along with it."）
18. ch20 行16 「失去…妹妹的信任」⇒ 姐姐（Wendy）
19. ch21 行14 「手机早在 Gray 的怀疑名单上」⇒ Gray 的警示（Laloul 可能窃听）
20. ch23 行10/86 「德高乐」⇒ 戴高乐（全书他处写法）
21. ch25 行100 关键词释义崩坏「原先是八位数的一半——一千万欧元」⇒ 「原先是一千万欧元」
22. ch25 行44 「回应…（下一段『你们俩都给我闭嘴』）」⇒ 原文该句在 Gray 发言之前，回应实为 `a silencing glare`
23. ch29 行14 「最后一次见面在十余年前（见前章回忆）」⇒ 原文只作 "From many years ago."（1993 年问话，相隔 27 年）
24. ch30 行14 「第 27 章的『不交原件』」⇒ 第 26 章（"You don't get the original, Erica."）
25. ch30 行32 「第 20 章第一次出现」（Baudouin）⇒ 第 22 章
26. ch30 行92 「与第 26 章 Ménard 说过的同一句（It's your choice.）对调」⇒ 全书仅 ch30 有此句 ⇒ 重写
27. ch31 行102 「『水计量官』从第 5 章起」⇒ 第 14 章（概念首见）
28. 00_金句精选 ch09 引语点评 **说话人错**：`There's no such thing in Algeria, Stephen…` 说者是 **Suzette**（十五岁离开阿尔及利亚），原写「一个阿尔及利亚人亲口说出」⇒ 改

**提示型（只记不改 6 类）**：check_vocab WARN 39（长度启发式）· check_overview_full C 段 1 条（图尼耶录音在 ch23/ch26 各播一次，标注 ch23 取自本章 text，成立）· sweep_analysis_inline 6 条（ch17:68 为**显式**第 15 章引用＝正确被误报；5 条省略号两侧均为同句原词）· ch22:168 `Suzette holds her nerve.` 为 ch22:567 逐字原句（报警源于释义格英文搭配 `hold one's nerve`）· ch25 块序与原文时序相反但引语与内容均正确 · ch29 枪手身份原文留白。
**工具盲区（不计三档）**：check_anchor 的「或本块分析正文」豁免与 check_analysis_indep 的「全书 text 命中」口径，**结构上抓不到「引语截短」**（ch18 即此例）——这一类只能靠 d 步人判。

**e 步（总览层）**：verify_overview_quotes 54/54 · check_overview_labels 28/28（口径外 0、待人判 0）· 说话人逐条回原文窗口复核（抓到并修正上表 #28）；**33 项事实断言逐条 grep 出支撑行号，0 未命中**（Taleb=Superintendent ch06:61 · Bouras=Director ch01:76 · Hidouchi=DSS ch01:190 · Ménard=DGSE ch26:16 · Zarbi→SM ch13:31 · Laloul→Sonatrach ch13:31 · Dalby=Le Chélifère 英国老板 ch12:340 · Kermadec=beau-père ch25:133 / 替 Zarbi 办事 ch25:270 · Gray=Harriet 的弟弟 ch13:67 · 1965 年 Wendy 17/Stephen 10 ch06:398 · Harriet 23 岁死 ch02:313 · Nedjar 伦敦开店 ch17:97 · Zakaria=Zarbi 之子 ch18:156 · 图尼耶被杀 1965-06-02 ch12:364 · Dalby 死 1994-02-21 ch16:340 · Laloul 1999 外逃 ch11:106 · Zarbi 二十年刑期 ch27:19 · 六名死者含 Storza ch29:309 · 磁带=图尼耶录音 ch26:178 · 镀金保险 ch31:49 · 指控撤销 ch31:67 · Gray 在 Annecy ch31:130 · 阿尔及利亚包裹 ch31:157 · hizb fransa ch31:327 · 书名出处 ch30:337 · 疫情封控 ch31:195 · 现在时 2020-07-22 ch18:78 · Bouteflika 去年下台 ch01:88 · Sidi Ferdj ch01:172 · 1993 年问话 ch12:91）。
**材料三样**：① 门禁原始输出（本目录 review-a-*.txt / review-fix-*.txt）② 总览自检声明（上段行号 + MISS=0）③ 跨书污染自检——28 个专名全部有本书 text/ 支撑，唯一他书同名 `Taleb` 出自 `365-days-with-self-discipline`（Nassim Nicholas Taleb，同形异指）。

**修复后复验（全部现场重跑）**：gate.sh **EXIT 0 / 正门 0 阻断型** · verify_quotes 246/246 · check_chapter_quotes 31/31 · sweep_full 0 异常 · check_entities 0 · corruption_scan **FAIL 0**（修复后必跑）· check_short_quotes 2/2 · review-bc-indep（第二实现）248 引语 0 缺陷 · check_struct_indep 0 · check_analysis_indep 617 片段全逐字 · check_xref_indep 英文报警 0 · verify_overview_quotes 54/54 · check_overview_full A53/B53 对/C1/E0 · **check_block_keywords 提示型 1→0**（ch18 截短修复后自动消失）。
**整改纪律**：全部 20 个文件的 40 处改动用 `review-fix.py` 行级替换（每条 old 必须唯一匹配、写盘用 tempfile+os.replace、写后断言行数不变），先 `--dry` 打印待改行人工确认后再 apply；ch18 引语跨度走 spec 层重生成（不在 md 上打补丁）。
**同会话审查的已知盲区**：d 步人判由子代理批跑 + 主会话复核完成（ch22–ch31 用 ±320 字窗口取证，未通读全文）；史学层面未核；建议如需第三重核验另指派异实例专查「说话人」与「引语截短」两类。
**状态**：本地 commit `07fb6ae40`（未 push）；逐条清单 `.memory/raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/review-findings.md`
