# ch06 R5 判定表 · T3 2026-11-04

断言 | 证据 | 结论 | 档位
---|---|---|---
13 块引语逐字 | 2-machine.json + fragments_indep 0 MISS | 成立 | —
「Paula 38 岁」「Donald 30 岁」「Beacon 62 岁」「Marc 三年」| 行13 "Paula, thirty-eight"／行43 "Donald, thirty"／行94 "sixty-two-year-old internist"／行163 "three years out of law school" | md 一致 | —
「药盒 20 秒/天＝2 小时/年」「邮件 16 小时/年」| 行73 "twenty seconds saved a day, the equivalent of two hours a year"／"sixteen hours a year" | md 一致 | —
「Suno 2000 万用户」| 行268 "more than 20 million users" | md 一致 | —
「溴」无涉本章（在 ch09）| — | md 未错置 | —
「iPatient 术语归 Verghese」| 行115 "what the physician Abraham Verghese called the “iPatient,”" | md 词表释义标注 Verghese ✓ | —
T1 曾修「analyst→初级分析员」两处 | chapter.sh 复跑 EXIT=0 | 已修复闭环 | —

已核实为正确：
- 原句4 用行79 段（"As time goes on, says Sonnenberg..."）而非含脚注的行76 "AI begins as your partner and ends as your leader.7"——partner/leader 句以中文理解转述且逐字片段出现在 md 分析层（行76 原文在场），合规。
- 原句9 访谈摘要块 "The man, all the while insisting that his major concern about generative AI was privacy..."——行211 逐字；「隐私 vs 初潮」的错位归位正确（此案在 ch06 非 ch04——T1 前的初稿曾无误置，本次 R1 复核确认）。
- 原句13 "It can't paint our Guernica."——行289 逐字；「AI 无肉身故无抵抗新语汇」为作者论断的转述，方向一致。
