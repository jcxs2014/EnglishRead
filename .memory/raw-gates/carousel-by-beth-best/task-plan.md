# Carousel (Beth Best) · 任务表
- 体裁：novels（言情/情感小说长篇，steampunk romantasy）
- 语料：text/ 50 件零偏移（ch01-ch49 = 书内 1-49 章；ch50 = Epilogue「50. The Epilogue」）；verify_corpus PASS（expect 50, Contents OEBPS/c2V.xhtml）
- 批次节奏：长篇 1 章/次，每章 chapter.sh rc=0 立刻 pathspec commit
- 状态：待写 ch01-ch50 + 总览三篇

| 章 | 书内标题 | 状态 | commit |
|---|---|---|---|
| ch01 | 1. The Card of the Visitor | 试产中 | |
| ch02 | 2. The Downed Hive | 待写 | |
| ch03 | 3. The Man from the Sky | 待写 | |
| ch04 | 4. The Assembly Will Provide | 待写 | |
| ch05 | 5. The Emperor's Captain | 待写 | |
| ch06 | 6. The Flight of the Hawker | 待写 | |
| ch07 | 7. The Floating Carousel | 待写 | |
| ch08 | 8. The Assassin in the Night | 待写 | |
| ch09 | 9. The Making of a Bed | 待写 | |
| ch10 | 10. The Accords for Soldiers | 待写 | |
| ch11 | 11. The Airlock Execution | 待写 | |
| ch12 | 12. The Captain's Dinner | 待写 | |
| ch13 | 13. The Swan Test | 待写 | |
| ch14 | 14. The Sacrifices of Others | 待写 | |
| ch15 | 15. The Communal Baths | 待写 | |
| ch16 | 16. The Consequences of Actions | 待写 | |
| ch17 | 17. The Morale Boosters | 待写 | |
| ch18 | 18. The Unstolen Radio | 待写 | |
| ch19 | 19. The Keeper Switch | 待写 | |
| ch20 | 20. The Island in the Sea | 待写 | |
| ch21 | 21. The People We Become | 待写 | |
| ch22 | 22. The View from The Bridge | 待写 | |
| ch23 | 23. The Happy Feeling | 待写 | |
| ch24 | 24. The Pursuit of Truth | 待写 | |
| ch25 | 25. The Last Line of Defence | 待写 | |
| ch26 | 26. The Prophecy and The Fortune | 待写 | |
| ch27 | 27. The Two Crane Flies | 待写 | |
| ch28 | 28. The Prisoner in the Brig | 待写 | |
| ch29 | 29. The Implosion of Magic | 待写 | |
| ch30 | 30. The End of an Alliance | 待写 | |
| ch31 | 31. The Traitor and The Spy | 待写 | |
| ch32 | 32. The Quiet Rebellion | 待写 | |
| ch33 | 33. The Sunset Trial | 待写 | |
| ch34 | 34. The Ultimate Betrayal | 待写 | |
| ch35 | 35. The First Fortune | 待写 | |
| ch36 | 36. The Card of the Choice | 待写 | |
| ch37 | 37. The Final Battle | 待写 | |
| ch38 | 38. The Unwanted Truce | 待写 | |
| ch39 | 39. The Oxygen Mask | 待写 | |
| ch40 | 40. The Deep Breaths | 待写 | |
| ch41 | 41. The Counterbalance | 待写 | |
| ch42 | 42. The Last Night | 待写 | |
| ch43 | 43. The Magic of the Unmagical | 待写 | |
| ch44 | 44. The Unsolicited Proposal | 待写 | |
| ch45 | 45. The Osimidite Chamber | 待写 | |
| ch46 | 46. The Metal Ladder | 待写 | |
| ch47 | 47. The Things We Want | 待写 | |
| ch48 | 48. The Erasure of Pain | 待写 | |
| ch49 | 49. The New World | 待写 | |
| ch50 | 50. The Epilogue | 待写 | |
| 00_概述 | — | 待写（最后） | |
| 00_金句精选 | — | 待写（最后） | |
| 00_情感节点 | — | 待写（最后） | |

## 语料备注
- ch04 L395-398 夹有盗版站注入广告行「Search Lokepub on Google when you're ready for another love story.」及一段预告式旁白，属提取污染，**任何引语不得取自该区间**；精读已绕开。
- ch06 L263-266 同样夹有 Lokepub 广告行（「Find a story worth staying up for on Lokepub.」），引语已绕开。

## T1（自检，2026-11-07）
- 审查方：自检
- 总览三篇：全篇人判完成（00_概述/00_情感节点/00_金句精选）
- 抽样：10 章（ch01,02,04,08,16,17,21,25,36,49）≥ ceil(50/8)=7
- assertion_scan：t1-candidates.json（364 候选）已预筛，未见 ≥3 条阻断
- verdict：.memory/raw-gates/carousel-by-beth-best/review/t1-verdict.md（通过，未进 T2）
- 台账：2026-11-07 | carousel-by-beth-best | T1 | 自检 | 通过（阻断<3）
