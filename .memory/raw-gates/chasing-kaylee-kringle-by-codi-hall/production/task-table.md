# 任务表 · Chasing Kaylee Kringle（Codi Hall）· novels 言情长篇（Holiday, Idaho #1）

- 语料：`text/ch00–ch53`，54 件零偏移（TOC 对齐：Prologue + Chapter One–Fifty-Two + Epilogue = 54；装置件 2 件剔除：Also-by / Author's Note）
- verify_corpus PASS（FAIL 0 / WARN 0）：件数 54 对账 + POV 锚点全中（Kaylee/Rick/Ansel 三 POV，Ansel 插章 ch27/38/45/48）
- 总词数 ~83.5k；章词数 168–4,200；ch53 尾部 rating 宣传行已剥离
- epub 真值照录：ch39 章头全大写 `RICK`（原书误植）；ch50 首句 `Ahalf dozen` 缺空格（原书误植）
- 形态：H1 `# NN. Chapter N`（书内章名拼写式，如 `# 01. Chapter One`；ch00 `# 00. Prologue`；ch53 `# 53. Epilogue`）；导航 5 项；子项 4 项；新书块数 2–15
- 批次节奏：约 1 章/次（长篇）；每章 rc=0 立刻 commit（pathspec）；每批 gate.sh 后回填 hash
- 完工定义：全书 54 章 + 总览三篇 + T1 自检三件套（t1-verdict.md / t1-candidates.txt / 台账一行）

| 章 | POV | 词数 | 状态 | commit |
|---|---|---|---|---|
| ch00 | Rick | 168 | 试产 rc=0 | 70f6c2c72 |
| ch01 | Kaylee | 2364 | 试产 rc=0 | 70f6c2c72 |
| ch02 | Rick | 278 | rc=0 | 批次1（97a551036 收口） |
| ch03 | Kaylee | 1513 | rc=0 | 批次1（97a551036 收口） |
| ch04 | Kaylee | 2557 | rc=0 | 批次1（97a551036 收口） |
| ch05 | Rick | 1217 | rc=0 | 批次1（97a551036 收口） |
| ch06 | Kaylee | 3049 | rc=0 | 批次1（97a551036 收口） |
| ch07 | Rick | 1394 | rc=0 | 批次1（97a551036 收口） |
| ch08 | Kaylee | 1362 | rc=0 | 批次1（97a551036 收口） |
| ch09 | Rick | 1384 | rc=0 | 批次1（97a551036 收口） |
| ch10 | Kaylee | 2729 | rc=0 | 批次1（97a551036 收口） |
| ch11 | Kaylee | 1219 | rc=0 | 批次1（97a551036 收口） |
| ch12 | Kaylee | 2359 | rc=0 | 批次1（97a551036 收口） |
| ch13 | Rick | 1474 | rc=0 | 批次2（收口） |
| ch14 | Kaylee | 1321 | rc=0 | 批次2（收口） |
| ch15 | Kaylee | 1261 | rc=0 | 批次2（收口） |
| ch16 | Rick | 1611 | rc=0 | 批次2（收口） |
| ch17 | Kaylee | 1901 | rc=0 | 批次2（收口） |
| ch18 | Rick | 1068 | rc=0 | 批次2（收口） |
| ch19 | Rick | 1888 | rc=0 | 批次2（收口） |
| ch20 | Kaylee | 1449 | rc=0 | 批次2（收口） |
| ch21 | Kaylee | 2459 | rc=0 | 批次2（收口） |
| ch22 | Rick | 1457 | | |
| ch23 | Kaylee | 1532 | | |
| ch24 | Rick | 1396 | | |
| ch25 | Kaylee | 1346 | | |
| ch26 | Rick | 1149 | | |
| ch27 | Ansel | 822 | | |
| ch28 | Kaylee | 2254 | | |
| ch29 | Rick | 2269 | | |
| ch30 | Rick | 1735 | | |
| ch31 | Kaylee | 2467 | | |
| ch32 | Rick | 1266 | | |
| ch33 | Kaylee | 1506 | | |
| ch34 | Rick | 1007 | | |
| ch35 | Kaylee | 1783 | | |
| ch36 | Kaylee | 820 | | |
| ch37 | Rick | 1470 | | |
| ch38 | Ansel | 422 | | |
| ch39 | Rick | 1166 | | |
| ch40 | Kaylee | 2133 | | |
| ch41 | Rick | 2664 | | |
| ch42 | Kaylee | 1060 | | |
| ch43 | Kaylee | 4200 | | |
| ch44 | Rick | 911 | | |
| ch45 | Ansel | 408 | | |
| ch46 | Rick | 1187 | | |
| ch47 | Kaylee | 1317 | | |
| ch48 | Ansel | 874 | | |
| ch49 | Rick | 1696 | | |
| ch50 | Rick | 1203 | | |
| ch51 | Kaylee | 1531 | | |
| ch52 | Kaylee | 1676 | | |
| ch53 | Kaylee | 749 | | |
