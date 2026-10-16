**Twisted Lies（Ana Huang）完工** —— 57 章正文（ch01–ch56 + Epilogue）+ 总览三篇

**【lane】** 完整 lane（有 epub）

**【第 3 条门禁】**
① verify_quotes 340/340 ✅（100%）｜完全干净 60/60
② check_vocab FAIL 0 ｜ WARN 232（基础档疑似超纲词，长度≥9 启发式＝提示型，只记不改）
③ check_entities 0 未知实体
④ corruption_scan FAIL 0（U+FFFD／双句号）
⑤ sweep_full 本章命中 202 ｜跨章 0 ｜跨标签拼接 84（提示）｜全书查无 0
⑥ check_short_quotes 无短引语
⑦ check_chapter_quotes 57/57 全部「X/X in 本章 text」
⑧ 块覆盖对账 ✅

**【总览门禁】**
⑭ verify_overview_quotes 54/54 ✅（概述 13／金句 24／情感节点 17）
⑮ check_overview_full：A 整串命中 60、查无 0 ｜B 章节标签对 60、不符 0 ｜C 跨章多重命中 3（提示）｜E H1 语义错配 0

**【gate.sh 正门】** 18 步全过，**0 条阻断型，退出码 0**

**【本轮修掉的真实缺陷（门禁初跑时存在）】**
· 引语 4 处：ch48「Brady→Brock」人名错；ch19 跨句拼接（把两句拼成一句）；ch03 漏词 that；ch11 标点+大小写
· 词汇表跨档重复 40 文件（同一批词填入三档＝注水）→ 按长度重分为互斥三档（10/10/5），跨档重复归零
· 关键词锚定 284 块越界（块级关键词误填章级候选）→ 改为只取本块引语内真实词
· 跨自然段引语 12 处 → 收为单段并同步重写四子项

**【假红型（已如实记录，不改内容）】**
· verify_fragments_indep 余 9 条 MISS：来源 epub「标点前空格」排版瑕疵（Stop .／Tonight ?／cup !／fucked .），去空格归一后全部逐字命中
· check_overview_full B 段 ch40 引语被判「跨标签拼接」：实为来源弯撇号 ’ vs md 直撇号 '，5 个片段逐条 flat 命中

**【门禁原始输出】** .memory/raw-gates/twisted-lies-by-ana-huang/（2026-10-16-门禁-首跑含279缺陷.txt / 2026-10-16-门禁-终验.txt）

**【五步审查】** 未做（待用户发起）
