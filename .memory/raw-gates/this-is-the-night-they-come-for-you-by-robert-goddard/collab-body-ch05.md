**《This is the Night They Come for You》ch05 交付（Chapter Five，J'AVOUE 第三段：合谋与那扇门）**（2026-10-15 UTC）

- 8 引语块 / 词条 33（高级 10 / 进阶 15 / 基础 8）；引语由 `mkchapter.py` 前缀逐字注入、例句由 `build_vocab_section.py` 从本章 text/ 抽，英文零手打
- 门禁（完整 lane，`bash scripts/gate.sh` 对书目录跑，**EXIT 0**；含 ch01–ch05 五章）：verify_quotes 40/40 ✅（本章 8/8）· check_vocab 165 词条行 FAIL 0 / WARN 5（提示型见下）· entities 0 · corruption 0 · sweep_full 本章 40 / 跨章 0 / 拼接 0 / 查无 0 · 逐章归属 8/8 in ch05 text · 导航层英文 ❌0 ⚠️0 · 分析层行内英文逐字 352 / 异常 0 · audit_structure 缺陷 0 提示 0 · check_anchor 造词 0 松散 0 · check_xref_chapter 0/0/0 · quote_blocks ✅ · block_keywords 阻断 0 提示 0
- 生产期一次拦截（生产工具「宁缺毋造」生效）：词头 `muttered` 不在本章候选集（本章只出现短语 `muttered conversation` 与独立词 `muttering`）⇒ 改 `muttering` 后重跑才对账通过——**「词头必须存在于本章 text」这条在写词表时就由工具挡住**，无需等门禁
- 本章在本批的位置：自述线第三个整段，全章无别的视角插入；本章末的「两辆警车 + 凶杀」是全书的第一个硬事件，也是第一章那份「认罪书」所指向的东西——**ch05 之后自述的每次回头都在给这件事补上下文**
- 原件：`raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/`（spec-ch05.json · glosses-ch05.json · vocab-candidates-ch05-full.txt · gate-ch05.txt）
- 状态：ch05 已本地 commit（未 push）
