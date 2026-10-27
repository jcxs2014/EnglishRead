# ch10 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，10 块 10 引语，issues 全空。
R4 人判：10/10 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块6「这正好成全了表姐的计划」方向反转 | text/ch10:47「…would close back over him, **foiling** Christiana's cousin's plan to leave the guilty party there, identified and caught」 | foiling＝挫败；应为「这正好会挫败表姐的计划」 | **阻断** |
| 块1 读者视角「ch09 里 Nate 赢下的那颗八号球」 | text/ch09:110「an eight ball **painted in** after」（门面彩绘）；素读#1「miscue 擦中 8 号、白球撞进 9 号」 | ch09 无「赢下八号球」；彩绘标志与 Christiana 的掌心球非同物 | **阻断** |
| 块7「被骨头划伤」归因 | text/ch10:191「It was from handling those splintered bones.」 | 有据 | 已核实为正确 |
| 素读#3/#4 女厕与磁铁细节未入块 | 素读 anchor 命中 True ×2；导航 11 已提磁铁 | 非关键转折 | 提示（不修） |

取证命令记录：
- `/usr/bin/grep -n "eight ball\|eight-ball\|9 ball\|nine ball" text/ch09_8_a_bullshit_day_to_die.txt` → 行110（仅门面彩绘）；退出码 0
- `/usr/bin/grep -n "middle finger\|deep cut" text/ch10_9_the_secret_maps_of_america.txt` → 行191；退出码 0（完整行含「handling those splintered bones」）

## 已核实为正确

- 块6 主干事实（手机触地与钟砸同一刻、Nate 仰倒进拖拉机挖出的坑、大地吞没）与素读#6 完全一致——错的只是「成全/挫败」一个词的方向。
- 块10 Seine 辩解五要素（It was him or us／none of us had desecrated／save all of us／Chris／the only way）逐字对应，称呼「Chris」与 ch20「Chrissy」构成原文自身的称谓家族。
- 块3「beavers have two pairs of lips」译「河狸有两对嘴唇」——比喻归属 Christiana 内心独白，非 md 添乱。

**结论：阻断 2（方向反转 ×1、跨章指认 ×1）、提示 1（不修）。**
