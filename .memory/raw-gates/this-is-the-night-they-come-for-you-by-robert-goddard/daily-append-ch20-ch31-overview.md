**《This is the Night They Come for You》完工（ch20–ch31 + 总览三篇）**（2026-10-15 UTC）

- 本批交付：ch20–ch31 共 12 章（每章 8 引语块 + 35 词条：高级 12 / 进阶 15 / 基础 8）+ 总览三篇（概述 6152 字 / 金句精选 8048 字 / 情感节点 5501 字）；全书 30 章 + 尾声 + 3 篇总览 = 34 md 全部本地 commit（未 push）
- 语料层（第 1 条 1a）：`verify_corpus.py --expect 31` FAIL 0 / WARN 0；text/ 31 件与目录 31 项 1:1，每件恰 1 个章首标题、序列严格递增 ⇒ 无合并/拆分
- **全书门禁原始输出**（完整 lane；`bash scripts/gate.sh <书目录>` → **正门结论：0 条阻断型（⚠️/❓ 不阻塞；退出码 0）**，EXIT 0）：
```
① verify_quotes 31 章：ch01 8/8 … ch31 8/8 ✅；总计 246/246 引文可核实（100%）；完全干净文件 31/31；--full 整串取证 0
② check_vocab：FAIL 0 ｜ WARN 4（ch29/ch30/ch31 基础档疑含超纲词——长度 ≥9 字符启发式，提示型）
③ check_entities：0 个文件存在未知实体
④ corruption_scan：FAIL 0 处（U+FFFD / 双句号）；报告 0 处
⑤ sweep_full：✅ 本章命中 246 ｜ ⚠️ 跨章 0 ｜ 🔶 跨标签拼接 0 ｜ ❌ 全书查无 0
⑥ check_chapter_quotes：31/31 全为「8/8 in chNN text」（0 MISS）
⑦ check_short_quotes：verify_quotes 跳过的 2 条短引语 → ✅ 命中 2 / ❌ 0
⑧ audit_structure 0 ｜ check_anchor 造词 0 ｜ check_xref_chapter 归章正确 1 / 伪造 0 / 移章 0 ｜ quote_blocks 前缀·编号·孤儿·泄漏 ✅ ｜ block_keywords 阻断 0
⑨ 总览：verify_overview_quotes 54/54（100%，已核覆盖 3/3 篇、口径外 0、拼接 0）｜check_overview_full A 命中 53 / ❌ 0、B 标签 53 对 / 不符 0、C 跨章多重命中 1、E H1 语义错配 0 ｜check_overview_labels 28/28 逐字 ｜H1 三篇与文件语义一致
```
- **三档分类**：阻断型 0；提示型 5（check_vocab 4 条基础档长度启发式 + check_overview_full C 段 1 条「同一句在 ch23/ch26 出现」——已人工读行：该句是图尼耶被逼问时的录音原文，ch23 与 ch26 各播放一次，概述标注 ch23 取自本章 text，标注成立）；假红型 3 例（均为工具口径造成，按「先修口径、不动内容」处置：build_vocab_section 内部用 `vocab_candidates.py --max-sent 400`，故只出现在 >400 字符长句里的词被判「不在候选集」——ch13 `dread`、ch29 `three-point turn` 两例换同章真实词通过；glosses 键大小写须与候选行行首一致——ch16 `Ballistic` 一例改键名通过）
- 写作期拦下的阻断型 3 处（全部回 spec 层重生成，未在 md 上打补丁）：① ch11 Q8 中文理解写了引语之外的情节（"I understand." 一段）⇒ 整块按真实引语重写并改引语跨度；② ch18 Q3 中文理解只覆盖引语后半句（"A child is a woman's greatest strength. And also her greatest weakness."）⇒ 补全「最大的力量，也是最大的软肋」；③ ch31 Q1 关键词 `permanent disadvantage`/`bargaining power` 不在本块引语内（前者是旁白、后者在另一段）⇒ 改引语跨度至 `‘And now we have the DGSE at a permanent disadvantage…+4`
- 总览（第 9 条 d + d2）：三篇由 `.memory/raw-gates/<slug>/gen_overview.py` 生成——**所有英文引语由脚本从章节 md 的 `> **原句 N:**` 行逐字取出**（一句话引语另用 QS() 从 `text/ch13_thirteen.txt` 正则取原句），英文零手打；全部写成 `> “…”（chNN）` 独立引用块、编号在块外。落地前按 9d 逐条 grep 核对四类断言（做了什么/什么关系/死因/数字）：1965-06-02 图尼耶被杀、1994-02-21 Dalby 阳台中弹身亡、Laloul 1999 外逃、Zarbi 二十年刑期、六个死者含 Laloul/Zarbi/Storza、Hidouchi＝DSS 特工、Suzette＝英国书店主 Nigel Dalby 之女、Kermadec＝继父、Zakaria＝Zarbi 之子且母为 Abderrahmane、Le Chélifère＝书店名、Nedjar 现居伦敦——**这一步在动笔前改掉 3 处身份错判**（Hidouchi 一度按 DGSE、Suzette 一度按「法国书商之女」、Kermadec 一度按 Suzette 丈夫，均为他人笔记/直觉易混处，逐条回 text/ 后纠正）；写完另做一轮同文件交叉一致性通读，改掉 6 处措辞与 1 处顺序（金句第三辑重排为 ch11→12→13→13→16）
- 本轮新增工具：`gen_overview.py` 的 `QS()`（按正则从 `text/` 取整句，供总览交代原文时引用，避免手打）
- 原件：`.memory/raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/`（gate-full-book.txt · gate-full-book-2.txt · gate-chapter-quotes-all.txt · gate-overview-final.txt · gate-overview-full.txt · gen_overview.py · 每章 spec/glosses/vocab-candidates/gate）
- 状态：ch01–ch31 + 总览三篇全部本地 commit（正文 31 批 + 总览 1 批，均未 push）；**五步审查未做（待用户发起）**
