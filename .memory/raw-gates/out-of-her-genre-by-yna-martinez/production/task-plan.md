# 任务表 · out-of-her-genre-by-yna-martinez

- 书：Out of Her Genre — Yna Martinez（自出版，© 2026），言情长篇（rom-com：言情作家 Yna × 特技替身演员 Kai）
- 语料：`text/` 32 件，零偏移（ch01–ch30 = Chapter 1–30；ch31 = Epilogue；ch32 = Special Chapter）
- 三方对齐 PASS：目录页 toc.xhtml 32 篇正文 = 实测 32 件；版权页无篇目列表（自出版）；另 2 推广页（ch33 广告页已删 / c035 Easter Eggs 本就跳过）非正文
- verify_corpus：PASS（FAIL 0 / WARN 0）——单 POV 连载，shared 豁免 14 个复现角色 + ch31=Okanagan 独占锚点
- ⚠️ epub 印刷形态：正文前有大量空行 + 章标题重复两次（drop-cap 形态？写引语时以 text/ 为准）
- 体裁 profile：novels（导航 5 项 / 4 子项 / 新书前 3 章块数 2–15）
- 章词数：863–3,822（中位约 2,000）；块数配额按创建卡 §3 篇幅档（约 1,000 词 2 块、1,000–1,600 词 3–4 块、1,600–2,400 词 4–6 块、2,400–4,500 词 6–12 块）
- 生成批节奏：约 1 章/次；每章 suread → 写 → chapter.sh → pathspec commit → 每批 gate
- 完工定义：总览三篇 + T1 自检三件套（t1-verdict.md / t1-candidates.txt / 台账一行）

## 章清单（keyplot 写完本章后回填）

| ch | 语料 | 词数 | 内容 | commit |
|---|---|---|---|---|
| 01 | ch01_chapter_1 | 1329 | The Art of Tactical Survival | 9465816b7 |
| 02 | ch02_chapter_2 | 1616 | The Empire of Controlled Silence | f097dbf71 |
| 03 | ch03_chapter_3 | 3546 | The Physics of Unintended Collisions | 48033502c |
| 04 | ch04_chapter_4 | 2113 | Out of Her Element | 3228ffed5 |
| 05 | ch05_chapter_5 | 1812 | Terms and Conditions | 8f1a986fc |
| 06 | ch06_chapter_6 | 2176 | The Quiet After the Storm | f0c85fc81 |
| 07 | ch07_chapter_7 | 1743 | Executive Provisions | 422007a27 |
| 08 | ch08_chapter_8 | 3722 | Forced Proximity | 568cf669d |
| 09 | ch09_chapter_9 | 2797 | Off the Clock | d109f76b4 |
| 10 | ch10_chapter_10 | 2255 | The Lower Loop | 043af1e18 |
| 11 | ch11_chapter_11 | 3215 | The Sunday Verdict | 52ae5a06c |
| 12 | ch12_chapter_12 | 1515 | Out of His League | 7723b82eb |
| 13 | ch13_chapter_13 | 2422 | The Emerald Wrap | 5cf4a7048 |
| 14 | ch14_chapter_14 | 3584 | The Midnight Dispatch | 043e7a453 |
| 15 | ch15_chapter_15 | 2324 | The Dark Prince Protocol | 043e7a453 |
| 16 | ch16_chapter_16 | 2581 | The Co-Conspirators | 6f92123c1 |
| 17 | ch17_chapter_17 | 2375 | The Dark Prince Debrief | 47c0adf78 |
| 18 | ch18_chapter_18 | 3819 | Unscripted Vulnerability | a46ac0483 |
| 19 | ch19_chapter_19 | 2388 | The Weight of the Shield | b3b7aad98 |
| 20 | ch20_chapter_20 | 1094 | Ghosts in the Skyline | a2fb96639 |
| 21 | ch21_chapter_21 | 1837 | The Tactical Buffer | 8b38bc027 |
| 22 | ch22_chapter_22 | 2564 | Thermal Irregularities | 7e6c742be |
| 23 | ch23_chapter_23 | 2060 | The Steep Time | |
| 24 | ch24_chapter_24 | 2001 | The Approaching Storm | |
| 25 | ch25_chapter_25 | 2038 | The Canopy of Glass | |
| 26 | ch26_chapter_26 | 1739 | The Unscripted Title | |
| 27 | ch27_chapter_27 | 2031 | The Floral Handover | |
| 28 | ch28_chapter_28 | 1565 | Pure Fiction | |
| 29 | ch29_chapter_29 | 1307 | The Edge of the River | |
| 30 | ch30_chapter_30 | 1211 | Round Tables and Red Bean Buns | |
| 31 | ch31_epilogue | 1003 | Epilogue · Sandcastles and Sovereign Rulers | |
| 32 | ch32_special_chapter | 863 | Special Chapter · Sovereign of Fiction | |
