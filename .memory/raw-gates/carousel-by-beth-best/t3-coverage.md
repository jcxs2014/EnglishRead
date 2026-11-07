# Carousel by Beth Best — T3 审查覆盖

日期：2026-11-07（本地）
范围：`notes/books/novels/carousel-by-beth-best/` ch01–ch50 + 3 overview files（机器层已绿：`gate.sh` / `2-machine.json` / `2-verify-fragments.txt`）

## 人判覆盖（50/50 章，逐章点名）

| 章 | 目录 | R1 素读 | R2 机器/碎片 | R3 对账 | R4 判定 |
|---|---|:---:|:---:|:---:|:---:|
| ch01 | ch01 the card of the visitor | ✓ | ✓ | ✓ | ✓ |
| ch02 | ch02 the downed hive | ✓ | ✓ | ✓ | ✓ |
| ch03 | ch03 the man from the sky | ✓ | ✓ | ✓ | ✓ |
| ch04 | ch04 the assembly will provide | ✓ | ✓ | ✓ | ✓ |
| ch05 | ch05 the emperor's captain | ✓ | ✓ | ✓ | ✓ |
| ch06 | ch06 the flight of the hawker | ✓ | ✓ | ✓ | ✓ |
| ch07 | ch07 the lonely heir | ✓ | ✓ | ✓ | ✓ |
| ch08 | ch08 the dragoness | ✓ | ✓ | ✓ | ✓ |
| ch09 | ch09 the osimidite canisters | ✓ | ✓ | ✓ | ✓ |
| ch10 | ch10 the captain's dinner | ✓ | ✓ | ✓ | ✓ |
| ch11 | ch11 the chalkboard | ✓ | ✓ | ✓ | ✓ |
| ch12 | ch12 the clandestine mission | ✓ | ✓ | ✓ | ✓ |
| ch13 | ch13 the swan test | ✓ | ✓ | ✓ | ✓ |
| ch14 | ch14 the sky provision sacrifice | ✓ | ✓ | ✓ | ✓ |
| ch15 | ch15 the communal baths | ✓ | ✓ | ✓ | ✓ |
| ch16 | ch16 the consequences of actions | ✓ | ✓ | ✓ | ✓ |
| ch17 | ch17 the morale boosters | ✓ | ✓ | ✓ | ✓ |
| ch18 | ch18 the unstolen radio | ✓ | ✓ | ✓ | ✓ |
| ch19 | ch19 the happy feeling | ✓ | ✓ | ✓ | ✓ |
| ch20 | ch20 the silver knife | ✓ | ✓ | ✓ | ✓ |
| ch21 | ch21 the court martial | ✓ | ✓ | ✓ | ✓ |
| ch22 | ch22 the cost of a lie | ✓ | ✓ | ✓ | ✓ |
| ch23 | ch23 the happy feeling | ✓ | ✓ | ✓ | ✓ |
| ch24 | ch24 the blood magic | ✓ | ✓ | ✓ | ✓ |
| ch25 | ch25 the last line of defence | ✓ | ✓ | ✓ | ✓ |
| ch26 | ch26 the meeting of the magics | ✓ | ✓ | ✓ | ✓ |
| ch27 | ch27 the two crane flies | ✓ | ✓ | ✓ | ✓ |
| ch28 | ch28 the prisoner in the brig | ✓ | ✓ | ✓ | ✓ |
| ch29 | ch29 the implosion of magic | ✓ | ✓ | ✓ | ✓ |
| ch30 | ch30 the end of an alliance | ✓ | ✓ | ✓ | ✓ |
| ch31 | ch31 the holes in memories | ✓ | ✓ | ✓ | ✓ |
| ch32 | ch32 the iron remains | ✓ | ✓ | ✓ | ✓ |
| ch33 | ch33 the tethered bird | ✓ | ✓ | ✓ | ✓ |
| ch34 | ch34 the ultimate betrayal | ✓ | ✓ | ✓ | ✓ |
| ch35 | ch35 the first fortune | ✓ | ✓ | ✓ | ✓ |
| ch36 | ch36 the card of the choice | ✓ | ✓ | ✓ | ✓ |
| ch37 | ch37 the final battle | ✓ | ✓ | ✓ | ✓ |
| ch38 | ch38 the unwanted truce | ✓ | ✓ | ✓ | ✓ |
| ch39 | ch39 the oxygen mask | ✓ | ✓ | ✓ | ✓ |
| ch40 | ch40 the deep breaths | ✓ | ✓ | ✓ | ✓ |
| ch41 | ch41 the counterbalance | ✓ | ✓ | ✓ | ✓ |
| ch42 | ch42 the last night | ✓ | ✓ | ✓ | ✓ |
| ch43 | ch43 the magic of the unmagical | ✓ | ✓ | ✓ | ✓ |
| ch44 | ch44 the unsolicited proposal | ✓ | ✓ | ✓ | ✓ |
| ch45 | ch45 the osimidite chamber | ✓ | ✓ | ✓ | ✓ |
| ch46 | ch46 the metal ladder | ✓ | ✓ | ✓ | ✓ |
| ch47 | ch47 the things we want | ✓ | ✓ | ✓ | ✓ |
| ch48 | ch48 the erasure of pain | ✓ | ✓ | ✓ | ✓ |
| ch49 | ch49 the new world | ✓ | ✓ | ✓ | ✓ |
| ch50 | ch50 the epilogue | ✓ | ✓ | ✓ | ✓ |

## 未审
- 无。**未审 0/50**。

## 方法与证据
- R1：逐章读取 `text/chNN_*.txt`，抽取 5–8 条可验证事实（动作/关系/数字/日期）并用原文片段定位证据 span/字符范围，写入 `review/<ch>/1-suread.json`。
- R2：全书机器产物 `review/2-machine.json` + `review/2-verify-fragments.txt`（已生成）；本轮未重跑改写类操作。
- R3：逐章对照 `text/` 与精读 md 的关键事实，重点检查施事三问（谁做/对谁/因何）、跨章断言风险、数字/专名/归属，写入 `review/<ch>/3-diff.md`。
- R4：逐章给出 R4/R5 判定结论，写入 `review/<ch>/4-verdict.md`；当前批次机器层通过，未发现需立即改文的阻断项；对高风险处（记忆抹除、Cosmer 视角 epilogue、Ephraine 死亡归因的“人物指责”vs事实）按原文口径记录。

## 备注
- 本覆盖完成“每章 R1→R4 产物与人判结论落盘”。若后续需更细的逐块 1:1 复核，可在现有 `review/<ch>/` 基础上加深 R3 行级证据，但本轮未留下未审章节。
