# 五步审查：Marilyn and Her Books（Gail Crowther）

- 审查方：Raccoon-Mac（用户 2026-10-08 发起）；执行方：同会话前段（本会话）
- 整改 commit：`c5bff7712`（d 步）——此前批次 commit `68b6654d2`…`3d31e7849` 共 12 条
- 复跑终值：verify_quotes 183/183（100%，干净 19/19）· vocab FAIL 0 / WARN 86 · entities 0 · corruption 0 · sweep_full 161 命中/跨章 0/拼接 0/查无 0 · 逐章归属 161/161（--book-dir 换口径）· check_analysis_indep 320 片段全命中 · 总览 47/47 + 整串 97 命中/标签不符 0/H1 0 · check_anchor 凭空造词 0 · **gate.sh EXIT=0（0 条阻断型）**

## a. 第 3 条门禁全量重跑（不信报告数字）

逐条从本机重跑，全部复现：verify_quotes 183/183（含 `--full`，EXIT 0）、check_vocab FAIL 0 / WARN 86（逐条看过：≥9 字符长度启发式 + 论证结构表格固有提示，全部提示型，接受）、check_entities 0、corruption_scan FAIL 0、sweep_full 161 命中/0/0/0、check_short_quotes 4 命中 0 查无。**0 阻断 / 86 提示（接受） / 0 假红。**

## b. 逐章归属（换路径：--book-dir 全书模式，非写作期的单章模式）

161 块全部 X/X in 本章 text；短引语 1 条（"Fuck off"）由 check_short_quotes 兜底命中本章。**0 缺陷。**

## c. 结构扫描（第二实现 check_struct_indep + audit_structure 双跑）

check_struct_indep：18 md 缺陷 0 / 提示 0。audit_structure：结构缺陷 0 / 提示 0 / 🔀 映射不一致 15。**映射不一致定性为提示型（结构成因非缺陷）**：本书 ch01=Introduction、ch02=Prologue 占提取件号，正文编号章从 ch03 起（ch03=第 1 章）——H1「第 N 章」跟随书内形态（AGENTS 8.1 第 6 步），文件号是提取件号，两侧按章号映射合法。总览三篇 H1 一行 grep 全部与文件语义一致。

## d. 语义二审（子代理 ch01–09 / ch10–18 两路并行 + 第二实现机械子项）

**子代理两路：检查 162 块 / 阻断 0 / 提示 1 / 假红 0**（报告：`.memory/reviews/2026-10-08-marilyn-d-step-A.md`、`-B.md`）。唯一提示：ch02 原句 2 中文理解写「对来访的黑白照片记者说」，text 无对话归属，属推断性措辞——引语逐字正确，存疑不改（措辞有依据："It's small," she said 的 said 记者来自 ch01 语境；记为提示接受）。

**第二实现机械子项 + 人工定性（发现 3 条阻断型，全部改完并回查原文）**：
1. **阻断** ch01:125「escape and its opposite」——Ephron 引语的同位结构被改写（原文 "Reading is escape, and the opposite of escape"）→ 改为逐字引用+同位结构标注（`ch01_chap1.txt:87`）。
2. **阻断** ch13:36「requires more analysis」——漏 "a little"（原文 "requires a little more analysis"）→ 补全逐字（`ch13_chap13.txt:38`）。
3. **阻断** ch09:165 词表例句「he does not share…」——漏 "Dean certainly"（原文 "Dean certainly does not share the ditzy reputation…"）→ 补全逐字（`ch09_chap9.txt:50`）。

**余 🟠 2 条定性为提示型（正当措辞/豁免类，不改）**：ch01:89「take A to B」= 句式记法（禁令 3 豁免类）；ch02:81「Cast back / stumble bedward」= 两个独立引语片段同句、各自逐字命中。

check_xref_indep：英文证据 0 报警；中文式 101 处待人判由 check_xref_zh 覆盖（0 错）。check_xref_zh：0 错。audit_numbers：年龄/百分比类 5 条列待人核——逐条回原文核对全部有据（二十岁=ch06 Grushenka、七十三岁=ch10 Dinesen、十一岁=ch11 Miller 年长、102 岁=ch14 Devi、十六岁=ch15 结婚未毕业）。check_anchor：凭空造词 0 / 松散 0。

## e. 总览层事实核对（说话人窗口 + 数字断言逐条回源）

- **说话人窗口抽查 8 条**（Cursum Perficio/Mankiewicz 场景/I am alone/病床信/迪恩/1957 访谈/安娜题赠/RECORD 日记）：全部「看到说话人标签」，**0 错配**。
- **数字断言回源**：$13,405,785、around $600,000、forty-nine、thirty-seven years、29 years、208 performances 全部在 text/ 逐字有据。
- **章节标签**：check_overview_full B 段 95 对 / 0 不符（审查期修复 3 处错标：⑰ ch7→ch9、⑳ ch10→ch11×2）；check_overview_labels 0 待人判。
- **金句 25 / 节点 22 条引语**全部来自已核实引语池（gen_overview 程序化生成，模板零手打英文）。

## 缺陷清单（汇总）

| # | 档 | 位置 | 缺陷 | 修法 |
|---|---|---|---|---|
| 1 | 阻断 | ch01:125 | 分析层改写引语同位结构 | 逐字引用 + 标注 |
| 2 | 阻断 | ch13:36 | 漏 "a little" | 补全逐字 |
| 3 | 阻断 | ch09:165 | 词表例句漏 "Dean certainly" | 补全逐字 |
| 4 | 提示 | ch02:48 | 「对记者说」推断性措辞 | 存疑不改（有依据） |
| 5 | 提示 | audit_structure | 🔀 映射不一致 15 | 结构性偏移（front/back matter 占号），合法 |
| 6 | 提示 | check_vocab WARN 86 | 启发式/格式固有提示 | 逐条看过，接受 |

审查过程自身教训 2 条：① 子代理委派带 write_scope 时须显式声明 write_file（第一次 INVALID_DELEGATION_SPEC，重复调用被 REPEATED_FRAMEWORK_FAILURE 拒绝，retry_limit=1 只许修一次）；② 一次 bash 会话的输出出现与文件不符的内容（显示损坏），从工作区根目录重跑干净验证后才采信。

## 结论

**五步审查通过**：3 条阻断型全部改完并回查原文，复跑 14 项全绿（gate.sh EXIT=0）。**同会话审查已知盲区**（供用户判断是否另行指派异实例复核）：① 审查方与执行方同会话，对「写作时为何这样写」的语境记忆共享；② 说话人核对为窗口抽查（8 条）而非全量 47+161 条逐条开窗；③ 子代理为独立上下文（无写作记忆），其「提示型 ch02:48」的存疑定性未经第二意见复核。
