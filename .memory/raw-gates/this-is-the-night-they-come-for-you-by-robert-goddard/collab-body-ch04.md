**《This is the Night They Come for You》ch04 交付（Chapter Four，J'AVOUE 自述第二段 + Gray 书房 + Taleb 车库）**（2026-10-15 UTC）

- 8 引语块 / 词条 33（高级 11 / 进阶 14 / 基础 8）；引语由 `mkchapter.py` 前缀逐字注入、例句由 `build_vocab_section.py` 从本章 text/ 抽，英文零手打
- 门禁（完整 lane，`bash scripts/gate.sh` 对书目录跑，**EXIT 0**；含 ch01–ch04 四章）：verify_quotes 32/32 ✅（本章 8/8）· check_vocab 132 词条行 FAIL 0 / **WARN 2（提示型：基础档疑含超纲词 `faceless functionary`、`underlying seriousness`，长度 ≥9 启发式，只记不改）** · entities 0 · corruption 0 · sweep_full 本章 32 / 跨章 0 / 拼接 0 / 查无 0 · 逐章归属 8/8 in ch04 text · 导航层英文 ❌0 ⚠️0 · 分析层行内英文逐字 285 / 异常 0 · audit_structure 缺陷 0 提示 0 · check_anchor 造词 0 松散 0 · check_xref_chapter 0/0/0 · quote_blocks ✅ · block_keywords 阻断 0 提示 0
- 本章结构备忘：自述线（Nigel）第一次与另外两条线同章并置——**转场由 Gray 放下文件、拉窗帘、又坐回去接着读完成**，读者跟着他的阅读进度走；ch04 尾部三句（Gray 决定等、Taleb 与 Akram 的对话）确认本书是「自述 + 两条当代线」三线交错的骨架
- 写作期预检：全部 8 块的关键词与中文理解在生成**后**逐条对注入引语复核一遍（按第 9 条 a2 的方向——分析不得覆盖引语之外的句子）；ch03 那两条阻断型的教训（前缀式注入取不到引语前一句旁白）已在 spec 阶段避开
- 原件：`raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/`（spec-ch04.json · glosses-ch04.json · vocab-candidates-ch04-full.txt · gate-ch04.txt）
- 状态：ch04 已本地 commit（未 push）
