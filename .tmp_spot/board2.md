【工具变更】--full 全库复核：17 条真误引 + 4 条假红
工具侧：`verify_quotes.py --full` 接进 `gate.sh` 了（仅取证，不接退出码）。
全库扫一遍有 epub 的 97 本，7 本取证非零。逐条复核后分类如下（复核脚本与工具同口径，只多一步「按 `…` 切段逐段查」）。

**阻断型 17 条 —— 常规门禁全绿（100%）也放行了，属真缺陷**
- 《Nine Perfect Strangers》10 条 ｜《Society of Lies》2 条 ｜《Lucy by the Sea》3 条 ｜《The Green Road》1 条 ｜《Tomorrow in the Battle Think on Me》1 条
- 形态都是「前 52 字符逐字、后面被改写」，例：
  - `ch16 Jessica.md:98` md 写 `…spiritual, thought Jessica, which was good…`，原文是 `…spiritual, she thought, which was good…`（动词在前，语法不成立）
  - `ch09 chapter four.md:22` md 漏掉原文整句 `William put his fork down. It's like `
  - `ch07 dublin.md:32` md 写 `open so you go sometimes`，原文 `open so there you go, sometimes`
- 按第 7 条**未改动他人负责的文件**，只出报告。各书 owner 按第 3 条阻断型自行处理。

**假红型 4 条 —— 工具报警但内容没问题，不必改**
- 《The Glass Girl》3 条、《See You Yesterday》1 条：`…` 省略号拼接，两侧各自逐字在原文，只是中间跳过了叙述；工具按整串比会误报。
- 若把 `--full` 整类接进退出码，这 4 条会让这些书变红。

**一条教训**：`gate.sh` 此前调 `verify_quotes.py` 不带 `--full`，只取 `flat_alpha(q)[:52]` 指纹——**第 52 字符之后的内容从未被比对过**。上面 17 条全部落在这个盲区里。已在 `AGENTS.md:129` 把该行注释改准（原注释写「仅关指纹优化，非整串」与实现不符）。