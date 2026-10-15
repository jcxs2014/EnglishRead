**《This is the Night They Come for You》ch02 交付（Chapter Two，Hampshire 线开篇）**（2026-10-15 UTC）

- 8 引语块 / 词条 34（高级 11 / 进阶 15 / 基础 8）；引语由 `mkchapter.py` 前缀逐字注入、例句由 `build_vocab_section.py` 从本章 text/ 抽，英文零手打
- 门禁（完整 lane，`bash scripts/gate.sh` 对书目录跑，EXIT 0；含 ch01+ch02 两章）：verify_quotes 16/16 ✅（本章 8/8）· check_vocab 66 词条行 FAIL 0 WARN 0 · entities 0 · corruption 0 · sweep_full 本章 16 / 跨章 0 / 拼接 0 / 查无 0 · 逐章归属 8/8 in ch02 text · 导航层英文 ❌0 ⚠️0 · 分析层行内英文逐字 135 / 异常 0 · audit_structure 缺陷 0 提示 0 · check_anchor 造词 0 / 松散 0 · 空段 0 · check_xref_chapter 0/0/0 · quote_blocks ✅ 16 行前缀完整·编号连续·无孤儿·无泄漏 · block_keywords 阻断 0 提示 0
- 写作期自查 1 处（第 9 条 a2）：Q4 引语由工具取整句（含前置叙述 "She closes her eyes for a moment."），中文理解初稿只覆盖台词 ⇒ 补「她闭了一下眼睛才开口」，避免引语长于它所支撑的分析
- 工具口径备忘：`build_vocab_section.py` 的**档位不由 glosses JSON 的分组决定**——高级＝`len(词头) ≥ 10` 且不在常见词表，进阶＝`len < 10` 的生词，基础＝候选集里的短语/短词。首跑把 25 条全塞进高级（我挑的词几乎都 ≥10 字符），补入 8–9 字符词（savouring / tranquil / solitary / paralysis / obscured / disarming / unaltered / dolefully / intently / shrubbery / watchful / glimpses / hesitates / foreseen / prompted）后才成 11/15/8
- 原件：`raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/`（spec-ch02.json · glosses-ch02.json · vocab-candidates-ch02-full.txt · gate-ch02.txt）
- 状态：ch02 已本地 commit（未 push）
