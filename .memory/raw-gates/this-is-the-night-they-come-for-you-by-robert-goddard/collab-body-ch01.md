**《This is the Night They Come for You》（Robert Goddard）· 推理长篇 · 开工 + 首章试产**（this-is-the-night-they-come-for-you-by-robert-goddard）

- 语料层 PASS：`extract_chapters.py` 产出 text/ 31 件（ch01–ch30 + ch31 epilogue）；件数对 epub 目录 31 项；**每件恰好 1 个章首标题、序列严格递增 ⇒ 无合并/拆分**（ch31 的 Epilogue 出现 2 次，是部分标题页 + 章首页的正常重复）；`verify_corpus --expect 31 --anchors`（用「大写形态出现且小写形态全库零出现」筛出的逐章独有专名）FAIL 0 / WARN 0
- 体裁：推理长篇，**多 POV / 多线**——Taleb（阿尔及尔，第三人称现在时）· Suzette Fontaine（Hampshire / 巴黎）· Stephen Gray，另有一份第一人称回忆录（ch04/ch05/ch07…，即后文 J'avoue）分章插入；后续各章「叙事手法」按实际出场线标注
- ch01 试产：8 引语块（配额 3–8 内）；引语由 `mkchapter.py` 从 text/ 前缀逐字注入（零手打）；词汇 32 条由 `build_vocab_section.py` 生成（高级 9 / 进阶 15 / 基础 8，例句全部取自本章 text/）
- 门禁（完整 lane，`bash scripts/gate.sh` EXIT 0）：verify_quotes 8/8 ✅ · check_vocab FAIL 0 WARN 0 · check_entities 0 · corruption 0 · sweep_full 本章命中 8 / 异常 0 · 逐章归属 8/8 · 分析层行内英文 65 逐字 / 0 异常 · audit_structure 0 · check_anchor 0（凭空造词 0）· 块覆盖 ✅ · quote_blocks 前缀/编号/孤儿/泄漏 ✅
- 写作期自查并整块重写 1 处：第 7 块初稿的中文理解写成了他章情节（「不是责任，不是报复」），关键词 `Not duty. Not revenge. Not even redemption.` 也不在本块引语内 ⇒ 按第 9 条 a 把中文理解 / 关键词 / 为什么这样写 / 读者视角提示 四项同步重写为引语的真实内容（Kudos? Redemption? Excitement? … A purpose, a meaning.）
- 原件：`.memory/raw-gates/this-is-the-night-they-come-for-you-by-robert-goddard/`（spec-ch01.json · glosses-ch01.json · vocab-candidates-ch01-full.txt · gate-ch01.txt · verify-corpus-ch01-batch.txt）
- 状态：ch01 交付验收格式；用户通过后按批次推进 ch02+；本地 commit，未 push
