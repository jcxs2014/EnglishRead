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
| ch22 | Rick | 1457 | rc=0 | 见 git log |
| ch23 | Kaylee | 1532 | rc=0 | 见 git log |
| ch24 | Rick | 1396 | rc=0 | 见 git log |
| ch25 | Kaylee | 1346 | rc=0 | 见 git log |
| ch26 | Rick | 1149 | rc=0 | 见 git log |
| ch27 | Ansel | 822 | rc=0 | 见 git log |
| ch28 | Kaylee | 2254 | rc=0 | 见 git log |
| ch29 | Rick | 2269 | rc=0 | 见 git log |
| ch30 | Rick | 1735 | rc=0 | 见 git log |
| ch31 | Kaylee | 2467 | rc=0 | 见 git log |
| ch32 | Rick | 1266 | rc=0 | 见 git log |
| ch33 | Kaylee | 1506 | rc=0 | 见 git log |
| ch34 | Rick | 1007 | rc=0 | 见 git log |
| ch35 | Kaylee | 1783 | rc=0 | 见 git log |
| ch36 | Kaylee | 820 | rc=0 | 见 git log |
| ch37 | Rick | 1470 | rc=0 | 见 git log |
| ch38 | Ansel | 422 | rc=0 | 见 git log |
| ch39 | Rick | 1166 | rc=0 | 见 git log |
| ch40 | Kaylee | 2133 | rc=0 | 见 git log |
| ch41 | Rick | 2664 | rc=0 | 见 git log |
| ch42 | Kaylee | 1060 | rc=0 | 见 git log |
| ch43 | Kaylee | 4200 | rc=0 | 见 git log |
| ch44 | Rick | 911 | rc=0 | 见 git log |
| ch45 | Ansel | 408 | rc=0 | 见 git log |
| ch46 | Rick | 1187 | rc=0 | 见 git log |
| ch47 | Kaylee | 1317 | rc=0 | 见 git log |
| ch48 | Ansel | 874 | rc=0 | 见 git log |
| ch49 | Rick | 1696 | rc=0 | 见 git log |
| ch50 | Rick | 1203 | rc=0 | 见 git log |
| ch51 | Kaylee | 1531 | rc=0 | 见 git log |
| ch52 | Kaylee | 1676 | rc=0 | 见 git log |
| ch53 | Kaylee | 749 | rc=0 | 见 git log |

## 完工记录（2026-11-06，主会话零子代理）

- **正文**：ch00–ch53 共 54 章全部 rc=0；`bash scripts/gate.sh` **EXIT=0（0 阻断）**
- **总览三篇**：`00_概述.md`（10 引语）/ `00_金句精选.md`（25 条块引用）/ `00_情感节点.md`（10 节点 17 引语）
  - `overview.py quotes` 39/39 ✅（金句短句 7 条按工具 <20 字母口径跳过，已另用 Counter+子串严格核 25/25）
  - `overview.py labels` 59/59 逐字 ✅ · `full` 0 拼接 / 0 查无 / 0 错配
- **T1 自检**：抽 12/54 章（ch00/05/10/15/20/25/30/35/40/45/50/53，首末必含、等距），总览三篇全篇人判，
  `assertion_scan.py` 539 行全量扫；**阻断 0**。三件套：`review/t1-verdict.md` / `review/t1-candidates.txt` / 台账一行（审查方=自检）
- **语料侧**：verify_corpus PASS（54 件零偏移）；写作期清除 z-lib 广告行 19 行（11 章正文中混入 + 尾声 rating 行）；
  原书误植照录：ch39 章头全大写 `RICK`、ch50 首句 `Ahalf dozen` 缺空格
- **未做**：T3 全量深审（不自行启动）；push（等用户指令）
