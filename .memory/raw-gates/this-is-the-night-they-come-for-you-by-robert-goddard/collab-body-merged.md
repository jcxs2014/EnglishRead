《This is the Night They Come for You》（Robert Goddard）· 推理长篇 · 30 章 + epilogue + 总览三篇 = 34 md（this-is-the-night-they-come-for-you-by-robert-goddard）
- 完工：ch01–ch30 + ch31 epilogue 正文 + 总览三篇（概述/金句精选/情感节点）全部本地提交；text/ 31 件 = 30 章 + 尾声，1:1 零偏移（ch31 的 Epilogue 出现两次＝部分标题页 + 章首页的正常重复）
- 门禁（完整 lane；`bash scripts/gate.sh <书目录>` EXIT 0，正门结论 0 条阻断型）：verify_quotes 246/246（100%）· --full 整串取证 0 · check_chapter_quotes 31/31「8/8 in 本章 text」· check_vocab 词条行 1073 / FAIL 0（WARN 39 条，全部同一类 `[基础] 基础档疑含超纲词`＝长度 ≥9 字符启发式，提示型）· check_entities 0 · corruption_scan FAIL 0 · sweep_full 246 命中 / 跨章 0 / 拼接 0 / 全书查无 0 · check_short_quotes 2/2 · audit_structure 0 · check_anchor 造词 0 · check_quote_blocks ✅ 前缀/编号/孤儿/泄漏 · block_keywords 阻断 0
- 总览门禁：verify_overview_quotes 54/54（100%，3/3 篇全覆盖）· check_overview_full A 53 命中 / ❌0、B 章节标签 53 对 / 不符 0、C 跨章多重命中 1（提示型）、E H1 语义 0 · check_overview_labels 28/28 逐字 · 三篇英文引语全部写成独立引用块（AGENTS 第 9 条 d2），引语由 gen_overview 从章节 md 逐字取，英文零手打
- 写作期拦下并整块重写 3 处阻断型（全部回到 spec 层重生成，未在 md 上打补丁）：① ch11 Q8 关键词落在引语之外；② ch18 Q3 中文理解只覆盖后半句；③ ch31 Q1 关键词不在本块引语内。另记 2 条工具口径（新入记忆）：build_vocab_section 的候选集口径＝vocab_candidates --max-sent 400；glosses 键大小写须与候选行行首一致
- commits：正文 31 批 + 总览/取证 1 批，均本地 commit 未 push
- 五步审查未做（待用户发起）
- 明细见 .memory/daily/2026-10-15.md；门禁原件 .memory/raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/

**五步审查（2026-10-15 19:18 UTC，同会话，用户发起）**：a–e 全执行（31 章 + 总览三篇）。
- a 门禁全量现场重跑：gate.sh EXIT 0 · 正门 0 阻断型 · verify_quotes 246/246 · --full 0 · check_vocab FAIL 0（WARN 39 全为「基础档长度 ≥9 字符」启发式）· entities 0 · corruption_scan 0 · sweep_full 0 异常 · 逐章归属 31/31 · 短引语 2/2 · 总览 54/54
- b/c 步换实现复核（第二套代码，248 引语）：跨章搬句 0 · 编号连续/四子项齐全/重复块 0 · H1 语义 0
- d 步语义二审两批子代理覆盖 248 块 + 主会话逐条回原文复核 ⇒ **28 条阻断型全部整改**：年份 2 处（2021→2020、1988→1965）· 亲属称谓 6 处（Wendy 是姐姐、Stephen 是弟弟）· 跨章引用指错 6 处（ch15→ch14、第 20 章→第 22 章、第 26/27 章、第 5 章→第 14 章、上一章→第 17 章）· **ch18 引语截短**（spec 层 +3→+5 并同步三条分析）· 释义崩坏 1 处、病句 1 处、繁体字 1 处、体例 2 处
- e 步总览：54/54 逐字 · 章节标签 28/28 · 33 项事实断言逐条 grep 出**支撑行号**；修正 1 处引语说话人错（ch09 "There's no such thing in Algeria" 说者是 Suzette，原写「一个阿尔及利亚人」）
- 提示型 6 类只记不改（含 check_overview_full C 段同句跨两章＝录音在两章各播一次，标注成立）；工具盲区 1 条：check_anchor / check_analysis_indep 结构上抓不到「引语截短」，只能靠人判
- 修复后复验：gate.sh EXIT 0 · verify_quotes 246/246 · corruption_scan FAIL 0 · check_block_keywords 提示型 1→0 · 总览门禁全绿 · 独立 b/c 与三个 *_indep 脚本全 0
- 状态：本地 commit 07fb6ae40（未 push）；逐条清单与原始输出 `.memory/raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/review-findings.md`
