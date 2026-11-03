# 任务表 · all-the-way-home-by-alex-ritany

- 开工：2026-11-03。体裁 novels（W. W. Norton 2026 虚构长篇，双 POV Zach/Rena 交替 + Hour 倒计时结构）。
- 篇目：53 件 = ch01–ch52 + ch53 epilogue（epub 目录页三方对齐 ✓，verify_corpus PASS 53/53 FAIL 0）。
- 每章 md 命名：`chNN <keyplot>.md`（空格分隔，禁 `_` `'`）；ch53 为 `ch53 epilogue.md`。
- POV 分布（章首人名标签）：Zach=01 03 05 07 10 12 16 17 19 21 23 25 27 30 32 34 36 37 39 41 43 46 48 49 51；Rena=02 04 06 08 09 11 13 14 15 18 20 22 24 26 28 29 31 33 35 38 40 42 44 45 47 50 52；ch53 双线收束。
- Hour 章（带时刻标签）：01(10:41AM) 05(11:45AM) 09(12:50PM) 13(2:01PM) 17(3:10PM) 21(4:15PM) 25(5:26PM) 29(6:38PM) 33(7:41PM) 37(8:43PM) 41(9:54PM) 45(10:39PM) 49(6:04AM+4h)。
- 批次节奏：生成批 ~30 KB ≈ 1 章/次；每章 rc=0 立刻 pathspec 提交；每批 commit 前 gate.sh。

| 章 | 状态 | commit |
|---|---|---|
| ch01 | 试产 | 待 |
| ch02 | 完成 4d367f41e | ✓ |
| ch03–ch12 | 完成：3dd8334dc / 1f95a4745 / e88e8c358 / 4c6c07cdd / 3be1066ef / 036e001a2 / e3e57dfb3 / d1cfbd141 / 3dd8334dc / e38a58b35 / d1cfbd141（ch12）| ✓ |
| ch04 Lucy→Rena 修复 | b8079c3ed | ✓ |
| ch11 块序修复 | 80a567306 | ✓ |
| ch13–ch26 | 完成：dbe0f7327+9c7923089 / cc1e03ffb / 0199d0521 / b6a180eb9 / 13e6b80fe / d230a59b2 / c552934ae / 105d84db3 / 1b2403c73 / 237c1f38c / 2e9dc4d22 / 08d9a3626 | ✓ |
| ch27–ch52 + ch53 | 推进中 | — |
| 总览三篇 | 最后一章后写（00_概述 / 00_金句精选 / 00_情感节点） | — |
| T1 自检 | gate 全绿后（>40 章 → 抽 ≥10 章含首末） | — |
