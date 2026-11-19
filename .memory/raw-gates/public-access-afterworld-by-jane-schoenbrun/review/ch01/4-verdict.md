# R4 逐块判定 · ch01（Foreword）

机层：review/ch01/2-machine.json（chapter.sh --json，EXIT=0）；引语逐字 7/7、词汇 FAIL=0（R0 quotes.py verbatim --full 570/570、fragments 650/650 全库覆盖）。

| 块 | 引语↔中文理解↔关键词↔分析 | 施事三问 | 判 |
|---|---|---|---|
| 1 | "This book is not my own…"｜交出作者权｜originate/up front｜元小说开门动作 | 主语=旁白者（写字者），故事源=病友；与 text 一致 | ✓正确 |
| 2 | donut/geometry｜无角=无隐私 | 机构=施害方；text "part of its power" | ✓正确 |
| 3 | hate/survival/carnival ride｜恨=压杆 | 握杆者=旁白者本人；text 主语 I | ✓正确 |
| 4 | rumor/fake TV show｜传闻的入院原因 | 「我们大多都试过自杀」有 text 逐字（"Most of us had."）| ✓正确 |
| 5 | séance/hiding｜招魂框架 | 写作者=旁白者、被唤者=朋友；方向无误 | ✓正确 |
| 6 | confidence/time slot/HBO｜阶级判词 | 拒绝方=they（未指名，分析如实保留暧昧）| ✓正确 |
| 7 | hospitals/hell｜收束判词 | 施动者=they、受动者=us；text 平行句 | ✓正确（提示层数字已随 R3 修正为「听到」）|

跨章引用：提示 2「甜甜圈会在中段插曲里被重新访问」→ ch34 text 有 "the glow at the center of the donut" ✓（/usr/bin/grep 命中，text/ch34）。
数字断言：三十集/二十九集 → text 逐字 ✓（R3 #6 修正措辞后一致）。

## 断言 | 证据 | 结论 | 档位
- 「只录音了二十九集」 | text/ch01 "we only ever got a chance to hear twenty-nine" | 错（听到≠录音）| 阻断→已修复
- 「我们大多都试过自杀」 | text/ch01 "Most of us had." | 成立 | 已核实为正确
- 「甜甜圈中段重访」 | text/ch34 "the glow at the center of the donut" | 成立 | 已核实为正确

## 已核实为正确
- 原句 1–7 引语全部逐字（R0 fragments 650/650 覆盖本章全部片段）。
- 词汇表 9 条例句全部命中本章（2-machine.json check_vocab FAIL=0）。
- 「十七岁」「David Sawyer 化名」「HBO 周日晚档」三条素读事实与 md 导航/块 6 一致。
