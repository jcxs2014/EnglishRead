# 任务表 · The Christmas We Built（Kelly Collins）· novels 言情长篇

- 语料：`text/ch01–ch25`，25 件零偏移（TOC 对齐：Chapter 1–24 + Epilogue；verify_corpus PASS 0 FAIL / 0 WARN）
- 尾部装置已剔：Sneak Peek（另一本书试读章）→ `xx_sneak_peek_the_trouble_with_tinsel.txt`；版权页 / Contents / Holly Creek 地图 / 推广页 / About the Author 均未提取
- 总词数 ~57.6k；章词数 1,116–3,120；双 POV 交替（Nora 奇数章为主 / Griffin 交替，text 章首标 POV 名）
- 形态：H1 `# NN. Chapter N`（ch25 = `# 25. Epilogue`）；导航 5 项；子项 4 项；新书块数 2–15
- 批次节奏：约 1 章/次（长篇）；每章 rc=0 立刻 commit（pathspec）；每批收口（约 5 章）跑 gate.sh 后回填 hash
- 完工定义：全书 25 件 + 总览三篇 + T1 自检三件套（t1-verdict.md / t1-candidates.txt / 台账一行）

| 章 | 词数 | 状态 | commit |
|---|---|---|---|
| ch01 | 2822 | 试产 rc=0 | 03d481cf7 |
| ch02 | 2413 | rc=0 | 3bc87fe61 |
| ch03 | 2194 | rc=0 | a3813772b |
| ch04 | 2302 | rc=0 | 9cd28c429 |
| ch05 | 2828 | rc=0 | 0704fcd84 |
| ch06 | 2520 | rc=0 | 669cbdfd9 |
| ch07 | 2396 | rc=0 | a2564deb2 |
| ch08 | 2260 | rc=0 | c1c6aa101 |
| ch09 | 2245 | rc=0 | d0286ecb8 |
| ch10 | 1775 | rc=0 | c1f384ddf |
| ch11 | 1992 | rc=0 | 3c0814750 |
| ch12 | 2543 | rc=0 | 6c6d27172 |
| ch13 | 1929 | rc=0 | 9ba9bce59 |
| ch14 | 2500 | rc=0 | d902589d9 |
| ch15 | 1860 | rc=0 | 89e9685a0 |
| ch16 | 2213 | rc=0 | 3bfd7fab7 |
| ch17 | 2921 | rc=0 | 65a62ead6 |
| ch18 | 3106 | rc=0 | 4a3ee5266 |
| ch19 | 1787 | rc=0 | 9a6b93066 |
| ch20 | 3120 | rc=0 | 2c346fc26 |
| ch21 | 1860 | rc=0 | af93919f6 |
| ch22 | 1116 | rc=0 | 6bd1bea4d |
| ch23 | 2322 | rc=0 | 0c61a484a |
| ch24 | 2881 | rc=0 | 7e5d73bb1 |
| ch25 | 1684 | rc=0 | 7bf34bb94 |

**批次收口 1（ch01–05）**：gate EXIT=0（5 章 · 阻断 0 · 提示 1=ch01 块数 12 偏建议 5–9，已记理由）。语料层剥除 9 章 Lokepub 广告行（/tmp 备份，verify_corpus 复验 PASS）。

**批次收口 2（ch06–10）**：gate 首跑 EXIT=1（ch06 词汇例句跨章错挂——hinges 例句实为 ch05 句，换成 ch06 真词 creaked）→ 复跑 EXIT=0。

**批次收口 3（ch11–15）**：gate 首跑 EXIT=1（ch15 protocol 例句漏了插语 `,” Owen said. “` → 补全字节）→ 复跑 EXIT=0。素读锚点三连坑：跨说话人插入语/尾句号 vs 原文逗号/大小写接续——facts 一律写裸子串。

**批次收口 4（ch16–20）**：gate EXIT=0（逐字 348·vocab 命中 135·拼接 0）。ch17 露骨章按惯例以对白与姿态承载、器官细节不进引语。

**批次收口 5（ch21–25）**：gate 首跑 EXIT=1×2——ch25 原句2 跨说话人插入语缝合（拆两块重编号）+ ch22 pharmacy 例句跨章错挂（实为 ch24 句，换成本章 nutcracker 句）→ 复跑 EXIT=0。全书 25/25 章 rc=0。

**事件记录**：
- 2026-11-06 开工。他实例（chosen-by-monsters）误落仓库根的 19 件提取件曾被本次通配符卷入本目录，属主实例已自行领回，本实例未动其内容；本目录现存件数已复核为 25 + xx_sneak。
- ch01 试产块数 12（建议 5–9，⚠️ 提示级）：取创建卡"2,400–4,500 词 6–12 块"区间上沿，因首章须覆盖"查档—贺礼—对峙—对视"四幕且对话密集；后续章节块数取建议区间中段。
