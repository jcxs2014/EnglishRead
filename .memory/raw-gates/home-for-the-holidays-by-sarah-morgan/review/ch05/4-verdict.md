# 4-verdict · ch05

R2 机器层：chapter.sh --json rc=0（详见 2-machine.json）；全书 fragments 146/146 MISS 0。

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 「她冻结三秒」 | text/ch05: Only for about three seconds（Jack 原话） | 成立 | 已核实为正确 |
| 「全书第一次真正的相拥」 | 取证：/usr/bin/grep -cE 'hauled her against\|pulled her into his arms' text/ch02–04 → 0,0,0；ch05 → 1；退出码 0 | 成立 | 已核实为正确 |
| 块3 中文理解后半分析截去句 | 被引句止于 A and E.，后半句在引语外 | S2① | **阻断（已修）** |
| 块12 中文理解开头引 Lizzie 请求 | 请求在引语外（text para 494） | S2①轻度 | 提示（已修：改为「他不假思索地应下：我不走」） |
| 22%/24h 补液方案未引用 | R1 facts 5/6 vs md 15 块 | 程序细节让位关系线 | 提示（不修） |

## 已核实为正确
- 块10「你能成为一位非常重要的医生」引语同时承载传话之功（remembered all those things and done what you did＝传话任务），R1 fact 4 由它覆盖，不构成漏。

