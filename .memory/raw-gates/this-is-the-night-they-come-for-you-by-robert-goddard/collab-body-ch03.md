**《This is the Night They Come for You》ch03 交付（Chapter Three，Suzette 线与 J'AVOUE 自述合流）**（2026-10-15 UTC）

- 8 引语块 / 词条 33（高级 11 / 进阶 14 / 基础 8）；引语由 `mkchapter.py` 前缀逐字注入、例句由 `build_vocab_section.py` 从本章 text/ 抽，英文零手打
- 门禁（完整 lane，`bash scripts/gate.sh` 对书目录跑，**EXIT 0**；含 ch01–ch03 三章）：verify_quotes 24/24 ✅（本章 8/8，干净 3/3）· check_vocab 99 词条行 FAIL 0 WARN 0 · entities 0 · corruption 0 · sweep_full 本章 24 / 跨章 0 / 拼接 0 / 查无 0 · 短引语 0 条 · 逐章归属 8/8 in ch03 text · 块覆盖 ✅ 每块都进 verify_quotes · 导航层英文 ❌0 ⚠️0 · 分析层行内英文逐字 214 / 异常 0（跳过 3）· audit_structure 缺陷 0 提示 0 · check_anchor 造词 0 松散 0 · 空段 0 · check_xref_chapter 0/0/0 · quote_blocks ✅ 24 行前缀完整·编号连续·无孤儿·无泄漏 · block_keywords 阻断 0 提示 0
- 首跑 2 条阻断型（`check_block_keywords` ⑱），已修：① Q2 关键词 `the exact note of exasperation mixed with insistence` 落在引语**之前**的旁白句里（前缀式引语取不到）⇒ 换成引语内的 `It is not important why Saidi wants you to agree the document is a forgery`；② Q6 引语原为 +2 句（只到 `An overdue clean-up.`），而关键词与中文理解都提到后面的 `A little necessary housekeeping` ⇒ 跨度改为 +6 句，引语与分析同步。两处均按第 9 条 a/a2 在 spec 层改后整章重生成（不在 md 上打补丁）
- 工具口径备忘：**引语前缀式注入的天然边界**——按钮式「前缀 + N 句」取不到引语前的旁白，凡分析想引用引语**前方**那句话（如「她听得出恼火与坚持」），要么改关键词、要么把引语起点前移；本章属前者
- 原件：`raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/`（spec-ch03.json · glosses-ch03.json · vocab-candidates-ch03-full.txt · gate-ch03.txt）
- 状态：ch03 已本地 commit（未 push）
