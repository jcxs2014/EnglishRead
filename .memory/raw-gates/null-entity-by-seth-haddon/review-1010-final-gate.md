# 《Null Entity》五步审查整改后 gate.sh 原始逐行输出

- 时间：2026-10-10（整改批 785f1298f / bccc7c4b3 / a607215a9 之后）
- 命令：`bash scripts/gate.sh "notes/books/novels/null-entity-by-seth-haddon"`
- lane：完整 lane（epub）
- 结论：0 条阻断型，EXIT=0

```
=== lane ===
完整 lane（有 epub）

=== ① verify_quotes（引语逐字，对 epub；--full 关闭 52 字符指纹盲区）===
○ 总览三篇 1 个文件 0 提取——**本工具不判红**（总览引语主管门禁是 verify_overview_quotes）
    · 00_情感节点.md  → 须由 verify_overview_quotes 覆盖；若它也 0 提取则该文件引语确实无人核实

=== 总计 188/188 引文可核实（100%）；完全干净文件 24/24；正文章节 0 提取 0；总览 0 提取转交 1；--full 整串取证 0 ===

=== ② check_vocab（词汇真实性/例句/分档）===
词条行合计: 591
--- FAIL (0) ---
--- WARN (25) ---

=== ③ check_entities（梗概实体一致性）===
=== 实体一致性检测：0 个文件存在未知实体 ===

=== ④ corruption_scan（编辑损坏，进门禁）===
  ❌ FAIL 0 处（U+FFFD / 双句号）
  报告 0 处（中文重复片段 / 句中插入 / 占位崩坏）——**不判红，需人工判**

=== ⑤ sweep_full（引语整串 flat）===
  ✅ 本章命中 164 ｜ ⚠️ 跨章 0 ｜ 🔶 跨标签拼接 0 ｜ ❌ 全书查无 0

=== ⑥ check_short_quotes（<20 字符短引语兜底）===
  ✅ 命中 8 ｜ ⚠️ 在别的章 0 ｜ 🔶 跨标签拼接 0 ｜ 🔧 B类语料缺 0 ｜ ❌ 全书查无 0
  口径：正文章节按本章核；总览文件（00_*）按全书核

=== ⑦ 逐章归属 check_chapter_quotes（不降级）===
ch01 the game begins.md                        ch01 the game begins.md: 8/8 in ch01 text（另有 1 条短引语未校验）
ch02 desire outweighed the risk.md             ch02 desire outweighed the risk.md: 16/16 in ch02 text（另有 5 条短引语未校验）
ch03 i woke to fire.md                         ch03 i woke to fire.md: 20/20 in ch03 text（另有 6 条短引语未校验）
ch04 part of the subsidiary was in your head.md ch04 part of the subsidiary was in your head.md: 11/11 in ch04 text（另有 2 条短引语未校验）
ch05 we revolted together.md                   ch05 we revolted together.md: 8/8 in ch05 text（另有 1 条短引语未校验）
ch06 i feel sick.md                            ch06 i feel sick.md: 11/11 in ch06 text（另有 1 条短引语未校验）
ch07 welcome to the thorned root.md            ch07 welcome to the thorned root.md: 7/7 in ch07 text
ch08 a feast just out of reach.md              ch08 a feast just out of reach.md: 18/18 in ch08 text（另有 2 条短引语未校验）
ch09 ten thousand masks.md                     ch09 ten thousand masks.md: 11/11 in ch09 text（另有 2 条短引语未校验）
ch10 the cargo wing.md                         ch10 the cargo wing.md: 10/10 in ch10 text
ch11 cheap echoes of me.md                     ch11 cheap echoes of me.md: 18/18 in ch11 text（另有 1 条短引语未校验）
ch12 like knows like.md                        ch12 like knows like.md: 30/30 in ch12 text（另有 8 条短引语未校验）
ch13 hostile fusion.md                         ch13 hostile fusion.md: 30/30 in ch13 text（另有 4 条短引语未校验）
ch14 a wife turned extremist.md                ch14 a wife turned extremist.md: 13/13 in ch14 text
ch15 i am lyrebird.md                          ch15 i am lyrebird.md: 11/11 in ch15 text（另有 1 条短引语未校验）
ch16 infinity mirror.md                        ch16 infinity mirror.md: 8/8 in ch16 text
ch17 welcome home.md                           ch17 welcome home.md: 9/9 in ch17 text
ch18 have you been compromised.md              ch18 have you been compromised.md: 14/14 in ch18 text（另有 3 条短引语未校验）
ch19 the parliamentary coup.md                 ch19 the parliamentary coup.md: 25/25 in ch19 text（另有 2 条短引语未校验）
ch20 the world went white.md                   ch20 the world went white.md: 17/17 in ch20 text（另有 1 条短引语未校验）
ch21 watch us.md                               ch21 watch us.md: 28/28 in ch21 text（另有 8 条短引语未校验）
ch22 the last coherent thing.md                ch22 the last coherent thing.md: 53/53 in ch22 text（另有 4 条短引语未校验）
ch23 hello wylla.md                            ch23 hello wylla.md: 20/20 in ch23 text（另有 2 条短引语未校验）
（逐章归属：全部 X/X in 本章 text）

=== ⑧ 块覆盖对账（每块都进 verify_quotes）===
✅ 块覆盖对账：23 个文件，每块都进了 verify_quotes 校验

=== ⑨ 导航/总结层英文核对（六道门禁盲区）===
  
  === 导航/总结层英文核对：❌ 0 ｜ ⚠️ 0 ===

=== ⑩ sweep_analysis_inline（分析层行内英文）===
=== 分析层行内英文逐字核查（null-entity-by-seth-haddon）===
  ✅ 逐字 1319 ｜ ⚠️ 跨章 121 ｜ 🔶 拼接 3 ｜ 🟠 部分命中 1 ｜ 🟡 词形 0 ｜ ⚪ 术语 0 ｜ 🔧B类语料缺 0 ｜ ❌ 零命中 0 ｜ 跳过 418

=== ⑪ audit_structure（结构；子项检查是假阴性高发点，0 不等于齐）===
  本书主流子项（自推断，不套外部模板）：中文理解、为什么这样写、关键词、读者视角提示 ｜ 引语众数 8
  ❌ 结构缺陷 0 ｜ ⚠️ 提示 0 ｜ 🔀 映射不一致 0

=== ⑫ check_anchor（关键词锚定）===
  ❌ 凭空造词 0 处（词全书查无）
  ⚠️ 松散关键词 345 处（词在全书内、只是不在本引语块——多半是中译英或章内他处）
  ── 松散关键词明细 ──

=== ⑬ 空段扫描（必备章节标题在 ≠ 内容在）===
=== 空段扫描：0 处 ===

=== ⑭ verify_overview_quotes（总览三篇引语；有 00_* 才跑）===
=== lane：完整 lane（epub） ===
00_情感节点.md: 29/29 ✅
00_概述.md: ➖ 无引语行（正常，非门禁项）
00_金句精选.md: 24/24 ✅

=== 总览引文 53/53 可核实（100%）；完全干净文件 2/2；已核覆盖 2/3 篇（无引语 1 · 口径外 0）；🔶 跨缝隙拼接 0 条（提示，不判红）===

=== ⑮ check_overview_full（章节标签对账 + H1 语义；条件性）===
  C 跨章多重命中：0 ｜ E H1 语义错配：0

=== ⑯ check_xref_chapter（分析层跨章指认；❌阻断 / ⚠️须人工读行）===
=== 分析层跨章指认核对（null-entity-by-seth-haddon）===
  参照集：text/（24 个提取件） + epub 交叉验证 ；只认「chNN 后 20 字符内、且不跨中文分句标点」的反引号片段
  ✅ 归章正确 0 ｜ ❌ 伪造（全书查无）0 ｜ ⚠️ 移章（不在被引章）0

=== ⑰ check_quote_blocks（引语块结构：前缀/编号/孤儿/泄漏）===
=== 引语块结构对账（null-entity-by-seth-haddon）===
  带前缀的 `> **原句 N:**` 行：23 个文件共 171 行
  ✅ 前缀完整 · 编号连续无撞车 · 无孤儿分析 · 无自查泄漏

=== ⑱ check_block_keywords（块数配额 3–8 处 / 关键词锚定 / 拼接红线）===
=== 引语块覆盖度：23 个 md，阻断型 0 处 ／ 提示型 0 处 ===
══ 正门结论：0 条阻断型（⚠️/❓ 不阻塞；退出码 0）══
```
