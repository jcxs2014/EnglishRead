# ch01 判定表（R4）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 原句1 中文理解与引语一致（钟声停摆＝节律消失） | text/ch01:31 | 一致 | — |
| 2 | 原句1 关键词 4 项均在本块引语内 | 本块引语 | 一致 | — |
| 3 | 原句2 中文「任性而受压迫」对应 "whimsical, if oppressed" | text/ch01:103 | 一致 | — |
| 4 | 原句3 中文把两种传闻并列，无归因错误 | text/ch01:109 | 一致 | — |
| 5 | 原句3 中文夹英 "另一说simply是" | — | 中英夹杂残留 | **提示（已修）** |
| 6 | 原句4 中文「他有普通猫的分量」 | text/ch01:118 "heavier than a regular cat" | **误译（比他重）** | **阻断（已修）** |
| 7 | 原句4 施事：蹭过来的是猫、被蹭的是她 | text/ch01:118 | 一致（中文「猫用身体蹭过来」） | — |
| 8 | 原句5 中文「女王下令挖出她的心并杀了她」 | text/ch01:136 "he was ordered to extract my heart and kill me"＋":103" harvest for the queen | 施事成立（下令者女王、执行者他） | — |
| 9 | 原句5 分析引用块外句 He saved my heart | text/ch01:139（另一段） | 引语越界 | **阻断（已修）** |
| 10 | 原句6 中文「独自造了将近八个月」 | text/ch01:308 "almost eight months" / "no entire team" | 一致 | — |
| 11 | 原句7 中文「连自己从哪儿来都一点想不起来」 | text/ch01:340 | 一致 | — |
| 12 | 导航「八个月前那次换心」 | text/ch01:100 只限定决斗；换心时点无出处 | 时间断言过度精确 | **阻断（已修）** |
| 13 | 一句话总结 「她救下的那个男人如今正要挑新娘」 | text/ch01:97 选妻令 + `:136` 救人 | 成立（改后） | — |
| 14 | md 全文未出现 Cheshire / F-capacitor | `/usr/bin/grep -c "Cheshire\|F-capacitor" "ch01 the stopped clock.md"` → **0**，exit 1 | 未点专名，不构成误写 | 提示（不修） |
| 15 | 块序：7 块按原文偏移递增（641→…） | 2-machine.json quotes[].segments[].pos | 递增 | — |

## 已核实为正确（防误修）

1. **「最重的一句只有四个词」的计数本身**：`He saved my heart.` 破折号外确为 4 词（`text/ch01:139`）。本轮删的是**越界引述**，不是计数；后续不得以「四词写错」为由改回六词。
2. **原句1「Silence 与 That was more wearisome 两句独立成段」**：`text/ch01:37`、`:40` 各自成段，属实。
3. **导航「国王的选妻令」**：`text/ch01:97` 原文 "'The King does not forget unanswered invitations.' It's like saying attendance is not optional." ＋ `:88` 邀请函在桌上，成立。
4. **一句话总结的「正要挑新娘」**：`text/ch01:88` "Now he's seeking a bride like this?" 成立。
5. **「她有普通猫的分量」被改掉后**，`rarely leaned on me this way` 的「不常这样」含义未受影响——改后句仍保留「平常也极少靠人示好」。
