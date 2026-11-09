# 4-verdict · ch05（R4 逐块）

| 块 | 对应 | 施事三问 | 断言核查 | 档 |
|---|---|---|---|---|
| 1 | 再睡会儿=引语 | 说话人 Aelindor ✅ | — | ✅ |
| 2 | 拦救自省=引语 | Max 假设语气（would have been）✅ | Coldiron arrow 尖叫 逐字 | ✅ |
| 3 | Holt 三条不可能=引语 | 说话人 Holt ✅ | 「史上无人同帐」=not once in the entire history ✅ | ✅ |
| 4 | Coldiron 合唱=引语 | 声音来自 Veil 内 ✅ | — | ✅ |
| 5 | 递食=认领=引语 | 规则陈述=Max/递食者=Caspian（章内 "Caspian…held it out"）✅ | — | ✅ |
| 6 | 拉上桌=引语 | 说话人 Drakken ✅ | 「不是 Aelindor 拍板」=原文 It wasn't Aelindor ✅ | ✅ |
| 7 | asset 定性=引语 | 说话人 Drakken ✅ | — | ✅ |
| 8 | 机密+示范=引语 | 说话人 Drakken ✅ | White Witch/Coldiron 逐字 | ✅ |

**阻断 0 / 提示 0。**

## 已核实为正确
- 块3 说话人：三条「不可能」全部出自 Holt（原文该段引号内连续台词）——md 归属正确。
- 块5 认领礼的规则陈述者是 Max（narration），递甜甜圈者是 Caspian——md 把「规则」与「动作」分写，未混淆。

## T3 深审追加（2026-11-09）

| 断言 | 证据 | 结论 | 档 |
|---|---|---|---|
| 「全书第一反派的名字第一次与 Max 的能力绑定」 | `/usr/bin/grep -c "the White Witch’s bloodline on her" text/ch01_chap01.txt` → 1（exit=0）；ch01 已把 White Witch 血统与 Max 绑定 | 「第一次绑定」不成立（ch05 是第一次与**机密情报**挂钩） | **阻断**（已修） |

改前：「机密防的是她，全书第一反派的名字第一次与 Max 的能力绑定。」
改后：「机密防的是她，全书第一反派的名字第一次与 Max 的机密情报直接挂钩。」
