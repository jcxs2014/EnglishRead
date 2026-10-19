《Maybe Next Time》（Cesca Major）slug: maybe-next-time-by-cesca-major 全书精读 + 五步审查 + 中文层整层重写完工

- 产出：59 章逐章精读 + 总览三篇（概述/金句精选/情感节点）= 62 md；text/ 59 件（1:1 对账）
- 门禁（2026-10-19 中文层整改后全量重跑）：gate.sh 退出码 **0**（0 条阻断型）｜ verify_quotes 368/368（100%，62/62 干净）｜ check_chapter_quotes 逐章 59 章 0 MISS ｜ corruption_scan FAIL 0 ｜ check_block_coverage 59/59（每块都进 verify_quotes）｜ check_block_keywords 阻断型 0（提示型 14：语境延伸词，第 9 条 b 允许）｜ check_chinese_layer 阻断型 0（合格分析密度 100%、整层夹杂率 5%）｜ verify_overview_quotes 22/22（100%，3/3 干净）｜ check_overview_full A 27 命中 / B 20 对 / 0 不符 / H1 错配 0 ｜ check_nav_layer 0 ｜ audit_structure 结构缺陷 0 ｜ check_anchor 凭空造词 0 ｜ check_xref_chapter 伪造 0 ｜ sweep_analysis_inline 零命中 0 ｜ check_vocab FAIL 147（**预存**，改前改后同数；词表属禁改层，本轮未动）

**中文层整层重写**（2026-10-19，新增 lane ⑲ `check_chinese_layer` 首次进门禁后本书被扫出整层退化）
- 类级对账：合格分析密度 13% → **100%**；阻断型 551 → **0**；英文理解 210 → 0；英文为什么 303 → 0；缺中文理解 29 → 0；英文读者提示 → 0；形式性规避 4 → 0
- 改写方式：三个字段（`中文理解` / `为什么这样写` / `读者视角提示`）**整段重写**为中文散文分析；引用证据用中文弯引号 `「…」` 包住（英文证据保留原文），术语保留英文
- 证据纪律：逐块回读 `text/chNN_chapter_<N>.txt`（AGENTS 8.1 证据先行），不凭记忆
- 提示型 19 条（5%）的定性（AGENTS 第 3 条量级条款要求抽样 20 条）：抽 6 条实读（ch20:23 / ch21:17 / ch23:29 / ch40:29 / ch42:17 / ch43:35）全部是**引语行本身**含中英夹杂（`For fuck . . .` 等），`check_chinese_layer` 把引语行误算进「夹杂」统计 ⇒ 假红型（工具口径），不阻塞不整改

**顺带整改的内容级缺陷（22 处，非中文层）**
- 导航/总结层引语改回原文逐字 22 处：截短 8（`I can't really believe it` → 原文 `I still can't really believe it`）／改写 8（`You are on a committee` → `You're on a committee`）／跨章误标 4（`dragging herself back…` 实为 ch01 `you're dragging yourself back…`）／拼接未标省略号 2（`You didn't do this to us. I let you down.` 中间漏 `I know you saw us as a team.`）／改写＋改标 2
- 关键词行改引语逐字词 9 处（AGENTS 第 9 条 b）：ch07/ch08/ch09/ch18/ch21/ch22×2/ch34/ch36；另 6 处系分析层改中文后失去英文回显而暴露（ch13×2 / ch32 / ch34×3）
- 重复块（AGENTS 第 9 条 c）：**ch03 原句 4 与原句 8 是同一句 `No loo roll.`**，epub 全书仅 `Chapter_3.xhtml` 一处 ⇒ 原句 4 换回原文真实句 **“I really don—Ow.”**（Emma 撞上床柱，句子被打断），原句 8 的分析改为不再声称「本章出现两次」（那是事实错误）；块数保 17
- 总览层（AGENTS 第 9 条 d2）：`00_概述.md` 2 处行内英文引语改独立成行引用块 ⇒ `verify_overview_quotes` 覆盖 20 → **22 条（100%）**，`00_概述.md` 从「无引语行」→ 2/2 ✅
- U+FFFD 1 处（`ch35 nine years.md:42`）＝本轮 spec 手打时引入，已修 ⇒ corruption_scan FAIL 1 → 0

**工具 bug（修共享脚本，附全库行为对照）**
- `check_nav_layer.py` ① 直撇号 `'` 被当引号 ⇒ 区分「单词内部所有格撇号」与「成对包住英文段的引号」（**不能整体移除 `'`**——本库 md 里 `'` 成对包住英文段有 11,263 处，整体移除会丢 11k 处校验＝假阴性）；② 节边界只认 `## ` 标题 ⇒ 把 `**中文理解**：` 等精读字段行也当边界（`## 本章导航` 之下直接接精读块的写法，under-the-same-stars 全书 34 章）
- 全库行为对照（496 本，旧版与工作树版并列跑）：旧 ❌ 970 → 新 ❌ **476**；有差异 67 本；**新增 8 本经逐条抽样确认是真缺陷被揭出**（the-man / diana-in-love / seven-husbands / hello-beautiful / martyr / rookie-season / falling-into-place / meet-me-at-midnight）⇒ 按 AGENTS 第 3 条「工具失准必须重跑并留档」：留档，**不自动改那 8 本的内容**
- `check_analysis_quotes.py` ① 引号错配（`"`开`"`闭都算）⇒ 同类配对扫描；② 引号内中文译文被当英文原句 ⇒ 含汉字即非英文原句
- `check_cross_chapter_misattr.py` 跨章引用区分「已标注合规回指」与「真误标」；标注判定用 `(?<![A-Za-z0-9])chNN(?![A-Za-z0-9])` 替代 `\bchNN\b`（**Python 的 `\b` 在汉字紧邻时不匹配**，`在ch16 里` 判不出 ⇒ 「已标注」判定全失效）
- `rewrite_zh_fields.py` `_tail_` 支持顶层键与列表两种形态

- commits：c361244ee · be511f9e1 · d126c1359 · be0cb19f6 · 59330f2cd = 5，全部未 push
- 留待主会话裁定：① ch08 引语编号跳号（1,2,3,4,**6**,7,8），改前 HEAD 即如此，重编号会动引语行（禁改层）；② ch50 文件名 slug `the tiktok day` 与正文不对位（epub TOC 只有「Chapter N」）；③ `.memory/raw-gates/…/batches/` 1.3 MB / 58 文件属中间产物，本轮只提交规格与台账
- 明细：.memory/raw-gates/maybe-next-time-by-cesca-major/（2026-10-19-中文层整层重写-台账与门禁.md）
- 日志指引：.memory/daily/2026-10-19.md 本书专节
