**《This is the Night They Come for You》ch06–ch19 交付（本批 14 章，多线推进）**（2026-10-15 UTC）

- 每章 8 引语块 + 33–35 词条（高级 10–12 / 进阶 14–15 / 基础 8）；引语由 `mkchapter.py` 从 `text/chNN_*.txt` 前缀逐字注入，例句由 `build_vocab_section.py` 从本章 text 抽，英文零手打
- 门禁（完整 lane；每章交付即对书目录跑 `bash scripts/gate.sh`，**EXIT 0**）：verify_quotes 每章 8/8、无 ❌ · check_vocab FAIL 0 · entities 0 · corruption 0 · sweep_full 跨章 0 / 拼接 0 / 查无 0 · 逐章归属每章 8/8 in 本章 text · 导航层英文 0 · 分析层行内英文异常 0 · audit_structure 0 · check_anchor 造词 0 · 空段 0 · quote_blocks 前缀/编号/孤儿/泄漏 ✅ · block_keywords 阻断 0
- 逐章结构：ch06–ch07 Suzette 线（档案与父亲身份线索）· ch08–ch11 Taleb 线（夹带文件 / Haddad 实为 Laloul / Nedjar 交出复写副本与流沙警告）· ch12–ch14 三线交汇（J'AVOUE 自述推进 + Suzette 与 Gray 的旧账）· ch15–ch19 Gray 与 Wendy 的清算线（ch18 审 Abderrahmane：Zakaria 身份击穿防线、ch19 Gray 交出篡改与暗语「量水的人称金子」）
- 写作期按第 9 条 a/a2 处理 4 处「引语与分析不同步」（全部在 spec 层改后整章重生成，不在 md 上打补丁）：① Q3 关键词落在引语前的旁白句（前缀式注入取不到）⇒ 换成引语内的词；② 引语跨度少一句致关键词不可达 ⇒ 修句数；③ ch18 Q3 中文理解只覆盖后半句（"A child is a woman's greatest strength. And also her greatest weakness."）⇒ 补全「最大的力量，也是最大的软肋」；④ ch19 Q3 跨度 +2 取不到 "Hidden in your old apartment in Algiers." ⇒ 改 +3
- 工具口径备忘（新增记忆）：`build_vocab_section.py` 的**候选集口径 = `vocab_candidates.py --max-sent 400`**，故「只出现在 >400 字符长句里」的词会被判「不在本章候选集（自造？）」；ch13 `dread` 即此例，换同章 `faintly` 通过。另：glosses 键的大小写必须与候选行行首一致
- 原件：`raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/`（每章 spec-chNN.json · glosses-chNN.json · vocab-candidates-chNN-full.txt · gate-chNN.txt）
- 状态：ch06–ch19 全部已本地 commit（每章一条，未 push）；进度 19/31 章
