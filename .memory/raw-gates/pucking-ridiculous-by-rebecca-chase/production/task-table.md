# 任务表 · pucking-ridiculous-by-rebecca-chase

> Rebecca Chase《Pucking Ridiculous》Cloud Family Series Book 2 · 言情长篇（novels profile：导航 5 项 / 子项 4 项）
> 语料：69 件（ch00 foreword + ch01–ch67 + ch68 epilogue）· verify_corpus PASS（FAIL 0 / WARN 0，--expect 69 --shared Flora,Max）
> 不收：ch70–74（There's More / Start Your Engines 第3本预览 / Playlist / Books By / Coming Soon）
> 双 POV：Flora(37)/Max(31)；敏感章口径：谨慎选句、克制分析（露骨段不取引语）
> 素读 facts 文件：本目录 chNN-facts.txt（格式=锚点 || 事实）

## 批次（生成批 ≈1 章/次；每章 rc=0 即 commit 回填）

| 章 | 文件名 | 状态 | commit |
|---|---|---|---|
| ch01 | ch01 flora caught and must lead the class.md | ✅ | ff44c6540 |
| ch00 | ch00 foreword.md | ✅ | ea7085bca |
| ch02 | ch02 max wants his son back.md | ✅ | 94930d7a4 |
| ch03 | ch03 max and bailey walk in.md | ✅ | 055bdaf7a |
| ch04 | ch04 max drives back to apologise.md | ✅ | 85f82780c |
| ch05 | ch05 car park men in the dark.md | ✅ | 583f3438f |
| ch06 | ch06 three apologies and a freckle.md | ✅ | def62959e |
| ch07 | ch07 the phone call leak.md | ✅ | 91b8e4f5c |
| ch08 | ch08 nine digits only.md | ✅ | 96df8b926 |
| ch09 | ch09 the number on her arm.md | ✅（1 修复 c5284089d） | 846ef3669 |
| ch10 | ch10 baklava and maximus x.md | ✅ | c54ebeb2b |
| ch11 | ch11 just check that hes okay.md | ✅ | 9c2b0c88d |
| ch12 | ch12 bailey sets the rules.md | ✅ | ffcecc555 |
| ch13 | ch13 the nanny proposal.md | ✅ | a50a69e35 |
| ch14 | ch14 hell will freeze over.md | ✅ | e86ea1f1b |
| ch15 | ch15 reason ten and the pantry.md | ✅ | f859d2fe1 |
| ch16 | ch16 the pantry confession.md | ✅（1 修复 f20c223d5） | f20c223d5 |
| ch17 | ch17 she asks to move in.md | ✅ | f862aa622 |
| ch68 | （epilogue） | 待 | — |
| 总览三篇 | 00_概述 / 00_金句精选 / 00_情感节点 | 待（最后） | — |
| T1 自检 | 69 章 >40 ⇒ 抽 1/5 且 ≥10 章（首末章必含）；三件套 t1-verdict / t1-candidates / 台账 | 待 | — |

## 已定口径
- H1：`# NN. Chapter N`（书内既有形态 Chapter One…Chapter Sixty-Seven / Epilogue）
- 块数：ch01=9 块（2,115 词）；满 3 章后按本书众数自校准
- 词汇：vocab_candidates.py 候选减法，敏感词（lube/clit 等露骨例句）一律不取
- 取证：/usr/bin/grep 显式路径（text/ 被 gitignore，git grep 恒假零）
- 多段引语：` … ` 缝合，各段独立逐字、段间不跳非空段（ch01 已验证 gate 通过）
- git：pathspec 提交（本目录全部未跟踪，勿 git add -A）
