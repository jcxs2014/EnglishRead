# 4-verdict · ch08（R4 逐块，共 7 块）

| 块 | 对应 | 施事三问 | 断言核查 | 档 |
|---|---|---|---|---|
| 1 | 报告=引语 | 报告者 Enna ✅ | Marco/Frost 被烧=burns ✅ | ✅ |
| 2 | 破墙=引语 | 合力=三人（We tore through）✅ | — | ✅ |
| 3 | 应对银炎=引语 | 喝令前她转身面对；施力=Max ✅ | 「头发逆重力」=gravity-defying ✅ | ✅ |
| 4 | 「它们是我的」=引语 | 发声者=Max（she roared）✅ | 退散如狼群（snarl）✅ | ✅ |
| 5 | 目标与誓言=引语 | 「目标不是我」=Max；「绝不丢下你」=Aelindor ✅ | 「若死在这里也要让她知道」逐字 ✅ | ✅ |
| 6 | 冷铁孩子=引语 | 呼唱来自银炎 ✅ | — | ✅ |
| 7 | 收兵=引语 | 下令者=Max ✅ | 承诺原文 “I’ll come back… I promise” ✅ | ✅ |

**阻断 0 / 提示 0。**

## 已核实为正确
- 块5 誓言归属：「Even so, never without you, love.」是 Aelindor 的话（原文紧接 Aelindor decided），「I’m not their target」才是 Max——md 在中文理解里把两者分列，未混为一人，成立。

## T3 深审追加（2026-11-09）

| 断言 | 证据 | 结论 | 档 |
|---|---|---|---|
| 「Aelindor 的 love 是全书第一声公开的婚约级表态」 | `/usr/bin/grep -c "You won’t go alone, love" text/ch03_chap03.txt` → 1（exit=0）；ch03 早于 ch08 | 断言不成立 | **阻断**（已修） |
| 「把全书第一声爱的宣告放进最可能死亡的现场」 | 同上 | 同上 | **阻断**（已修） |

改前：「Aelindor 的 love 是全书第一声公开的婚约级表态。」
改后：「Aelindor 在这句里的 love 是他第一次在生死关头把称呼说出口（ch03 他已叫过她 love）。」

改前：「把全书第一声爱的宣告放进最可能死亡的现场，浪漫与遗言同一条语法。」
改后：「把一句近乎遗言的宣告放进最可能死亡的现场，浪漫与遗言共用一条语法。」
