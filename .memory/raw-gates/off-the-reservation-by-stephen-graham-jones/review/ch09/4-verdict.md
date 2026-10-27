# ch09 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，15 块 15 引语，issues 全空。
R4 人判：15/15 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块14「某种第四个存在」解读超出原文自解 | text/ch09:1320–1322：「four is the sacred number」→「four Blackfeet coming home」→「he understood: the boy, the bones.」 | 原文自解仅「the boy, the bones」；md 的四件套清单与「第四个存在」为开放推测（以省略号标记） | 提示（不修） |
| 素读#2/#5 两个进场细节未入块 | 素读 anchor 命中 True ×2 | 非关键转折；#2 的「四个月前颅骨骨折」与 ch02:41 口径一致 | 提示（不修） |
| 块10「older cousin＝表姐」与 ch04「niece's only son」 | 两章各自原文 | 原文内部称谓差异，md 各自忠实 | 已核实为正确（不修） |
| 块4/14/15 引语头部 `""` | 与 ch08 同源的 11 行格式缺陷 | 已在 ch08 verdict 建档，修复指令统一列 | 阻断（归并至格式项） |

取证命令记录：
- `/usr/bin/grep -n "four Blackfeet" text/ch09_8_a_bullshit_day_to_die.txt` → 行1320；退出码 0（上下文 1310–1326 已读）
- 素读 anchor 偏移验证 True ×8

## 已核实为正确

- 块15 施事与时序：「Nurse Seine **already** bringing that little granite clock」——砸钟与 Benjamin 的话**同时**进行，md「Seine 护士已经举起……重重砸向」保留了 already 的同时性。
- 块12「Doby or White Jackson or KellyKel」三人并列的不确定性被中文「Doby 或 White Jackson 或 KellyKel」忠实保留（Nate 视角不知道是谁）。
- 块1「BROKEN」三连与「Christian was driving again」——开车的确是 Christian（素读#6 拖拉机前的行车段），归属无误。

**结论：本章新增阻断 0（引语头部 `""` 归并入全书格式项）；提示 3（不修）。**
