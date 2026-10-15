《This is the Night They Come for You》（Robert Goddard）· 推理长篇 · 30 章 + epilogue + 总览三篇 = 34 md（this-is-the-night-they-come-for-you-by-robert-goddard）
- 完工：ch01–ch30 + ch31 epilogue 正文 + 总览三篇（概述/金句精选/情感节点）全部本地提交；text/ 31 件 = 30 章 + 尾声，1:1 零偏移（ch31 的 Epilogue 出现两次＝部分标题页 + 章首页的正常重复）
- 门禁（完整 lane；`bash scripts/gate.sh <书目录>` EXIT 0，正门结论 0 条阻断型）：verify_quotes 246/246（100%）· --full 整串取证 0 · check_chapter_quotes 31/31「8/8 in 本章 text」· check_vocab FAIL 0（WARN 4 条提示型＝基础档长度启发式）· check_entities 0 · corruption_scan FAIL 0 · sweep_full 246 命中 / 跨章 0 / 拼接 0 / 全书查无 0 · check_short_quotes 2/2 · audit_structure 0 · check_anchor 造词 0 · check_quote_blocks ✅ 前缀/编号/孤儿/泄漏 · block_keywords 阻断 0
- 总览门禁：verify_overview_quotes 54/54（100%，3/3 篇全覆盖）· check_overview_full A 53 命中 / ❌0、B 章节标签 53 对 / 不符 0、C 跨章多重命中 1（提示型）、E H1 语义 0 · check_overview_labels 28/28 逐字 · 三篇英文引语全部写成独立引用块（AGENTS 第 9 条 d2），引语由 gen_overview 从章节 md 逐字取，英文零手打
- 写作期拦下并整块重写 3 处阻断型（全部回到 spec 层重生成，未在 md 上打补丁）：① ch11 Q8 关键词落在引语之外；② ch18 Q3 中文理解只覆盖后半句；③ ch31 Q1 关键词不在本块引语内。另记 2 条工具口径（新入记忆）：build_vocab_section 的候选集口径＝vocab_candidates --max-sent 400；glosses 键大小写须与候选行行首一致
- commits：正文 31 批 + 总览/取证 1 批，均本地 commit 未 push
- 五步审查未做（待用户发起）
- 明细见 .memory/daily/2026-10-15.md；门禁原件 .memory/raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/
