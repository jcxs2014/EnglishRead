**五步审查（2026-10-15，同会话，用户发起）**：a–e 全执行（31 章 + 总览三篇）。
- a 门禁全量现场重跑：gate.sh EXIT 0 · 正门 0 阻断型 · verify_quotes 246/246 · --full 0 · check_vocab FAIL 0（WARN 39 全为「基础档长度 ≥9 字符」启发式）· entities 0 · corruption_scan 0 · sweep_full 0 异常 · 逐章归属 31/31 · 短引语 2/2 · 总览 54/54
- b/c 步换实现复核（第二套代码，248 引语）：跨章搬句 0 · 编号连续/四子项齐全/重复块 0 · H1 语义 0
- d 步语义二审两批子代理覆盖 248 块 + 主会话逐条回原文复核 ⇒ **28 条阻断型全部整改**：年份 2 处（2021→2020、1988→1965）· 亲属称谓 6 处（Wendy 是姐姐、Stephen 是弟弟）· 跨章引用指错 6 处（ch15→ch14、第 20 章→第 22 章、第 26/27 章、第 5 章→第 14 章、上一章→第 17 章）· **ch18 引语截短**（spec 层 +3→+5 并同步三条分析）· 释义崩坏 1 处、病句 1 处、繁体字 1 处、体例 2 处
- e 步总览：54/54 逐字 · 章节标签 28/28 · 33 项事实断言逐条 grep 出**支撑行号**；修正 1 处引语说话人错（ch09 "There's no such thing in Algeria" 说者是 Suzette，原写「一个阿尔及利亚人」）
- 提示型 6 类只记不改（含 check_overview_full C 段同句跨两章＝录音在两章各播一次，标注成立）；工具盲区 1 条：check_anchor / check_analysis_indep 结构上抓不到「引语截短」，只能靠人判
- 修复后复验：gate.sh EXIT 0 · verify_quotes 246/246 · corruption_scan FAIL 0 · check_block_keywords 提示型 1→0 · 总览门禁全绿 · 独立 b/c 与三个 *_indep 脚本全 0
- 状态：本地 commit 07fb6ae40（未 push）；逐条清单与原始输出 `.memory/raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/review-findings.md`
