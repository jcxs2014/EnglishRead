# 任务表 · Bodies of Magic（Freya Marske）· novels 言情长篇

- 语料：`text/ch01–ch40`，40 件零偏移（TOC 对齐：Contents 页 40 章目录；Part 分隔页 Day One–Five + 装置件 15 件已剔除）
- verify_corpus：PASS（--expect 40 --expect-source epub bullet 实测 --anchors ch01=Jehan/ch06=Estiene/ch21=Estiene/ch35=Clement/ch40=Jehan,Clement,Estiene --shared）
- 总词数 ~135.7k；章词数 925–7,062；主线人物 Jehan（ healer）/Clement/Estiene，跨章共享
- 形态：H1 `# NN. One`（text/ 章首行＝拼写数词 ONE，照 the-unsolvable-case 先例）；导航 5 项；子项 4 项；新书块数 2–15
- 批次节奏：约 1 章/次（长篇）；每章 rc=0 立刻 commit（pathspec）；每批 gate.sh 后回填 hash
- 完工定义：全书 + 总览三篇 + T1 自检三件套（t1-verdict.md / t1-candidates.txt / 台账一行）

| 章 | 词数 | 状态 | commit |
|---|---|---|---|
| ch01–ch40 | 925–7,062 | 全部完工，逐章 rc=0、素读 100% | 700f4c90f…07ca53d28 |
| 门禁整改 | — | 词表 8 处 + 关键词 9 处 + ch34 补块，gate EXIT=0 | a875100f9 |
| 总览三篇 | — | 79/79 引语、40/40 章覆盖 | 见下一 commit |
| T1 自检 | — | 抽 10/40 章，整改 17 处，三件产物齐 | 见下一 commit |
