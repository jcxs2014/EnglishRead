# ch02 判定表（R4）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 原句1「唯一还能确定的，是自己是个科学家」 | text/ch02:16 | 一致 | — |
| 2 | 原句2「被发现时几乎断气＋情节记忆空白」 | text/ch02:22 | 一致 | — |
| 3 | 原句3「身份系于地点，是未验证的假设」 | text/ch02:28 | 一致 | — |
| 4 | 原句4「只为安心而修小钟＋讨黄铜发条」 | text/ch02:37 | 一致 | — |
| 5 | 原句5 施事：**她**装的预警系统、**她**是唯一工程师 | text/ch02:43 | 一致 | — |
| 6 | 原句6「Then don't」＝别去见他，非「别被人看见」 | text/ch02:160–161 | 语意合并 | **提示（已修）** |
| 7 | 原句7 心链失效、双方互不觉察 | text/ch02:211 | 一致 | — |
| 8 | 原句8「快一年」＝nearly a year | text/ch02:274 | 一致 | — |
| 9 | 导航「鞋子都替她挑」 | text/ch02:235 拒借鞋 | **与原文相反** | **阻断（已修）** |
| 10 | 导航「请柬变成礼服」 | text/ch02:106 / :176–178 两件事 | 因果虚构 | **阻断（已修）** |
| 11 | 一句话总结「蓬蓬裙」 | text/ch02:178 deep green satin | 颜色/材质缺失 | **提示（已修）** |
| 12 | 块序 8 块偏移递增 | 2-machine.json | 递增 | — |
| 13 | 「Chez/Duchess 是国王旧友」未入 md | text/ch02:223 | 背景信息缺口 | 提示（不修） |

## 已核实为正确（防误修）

1. **「连牙都替她刷了」**：`text/ch02:172` "Did you also brush my teeth for me?" — 属实，非夸张。
2. **「Jabberwocky 不会为任何人停下」**：`text/ch02:43` "you know that Jabberwocky doesn't stop for anyone"。
3. **「她与国王的联结已断，所以去不去舞会都不危险」**：`text/ch02:211` "The king would not sense you there any more than you will sense him." — 原文明确，后续不得改成「联结仍在」。
4. **章题 GRWM 未在正文解释**：`/usr/bin/grep -c "GRWM" text/ch02_two_grwm.txt` 仅命中的是章题行本身；md 写「本章正文未作解释」成立。
