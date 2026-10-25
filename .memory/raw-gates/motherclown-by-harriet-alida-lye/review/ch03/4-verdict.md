# ch03 · T3 判定表

- 章：Chapter Two（md：`ch03 chapter two the colour blue.md`；原文 `text/ch03_chapter_two.txt`，7,744 词）
- R1 素读：`1-suread.json`（独立子代理，只读 `text/`；8 条，锚点 8/8 唯一）
- R2 机器层：`2-machine.json`（verdict=ok，15 块 / 15 片段，查无 0）
- R3 对账：`3-diff.md`（漏 5 提示 / 编 1 阻断（F1）/ 错 0）
- 覆盖：**全章 15 块逐块 R4 + R5**

## R4 逐块对应

| 块 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|
| 1 | whore's bath · flights · sink | ✓ | ✓ 讲「母亲的声音先住进房间」与用水换算台阶 | ✓ 她给自己擦洗（母亲只是命名） | 通过 |
| 2 | costume · backdrop · gender | ✓ | ✓ 讲「黑是减法」的校规美学 | ✓ 学校要求**她们**，非她自选 | 通过 |
| 3 | dad · breaks · unbearable | ✓ | ✓ 讲「想告诉他」这个动作本身 | ✓ **她**想告诉**爸爸** | 通过 |
| 4 | standards · dropping · leave | ✓ | ✓ 讲「否定、否定、再命名」的判决句式 | ✓ 她自审：反对的是**被留下** | 通过 |
| 5 | half-wall · recliner · frame | ✓ | ✓ 讲「退出取景框」的摄影术语 | ✓ **Seb** 退出（不是 Catherine 退出） | 通过 |
| 6 | punch · seed · night | ✓ | ✓ 讲未来时态的迟到与 seed | ✓ 她后来重放这场架 | 通过 |
| 7 | alien · ladybugs · perfect | ✓ | ✓ 讲 alien 冒犯母爱常规与指甲细节 | ✓ **她**造了这东西 | 通过 |
| 8 | minutes · millions · break | ✓ | ✓ 讲 and 串起的排比与 break | ✓ 她想自己会**弄坏她** | 通过 |
| 9 | fog · echo · original | ✓ | ✓ 讲三个 misses 与回声失去原声 | ✓ 她缺的是女儿（不是女儿缺她） | 通过 |
| 10 | urgency · question · late | ✓ | ✓ 讲问句套问句、痛变成燃料 | ✓ 她自问「如果还不太晚」 | 通过 |
| 11 | ring · miss · bigger | ✓ | ✓ 讲断线反而保证决定不被驳回、转婚戒 | ✓ **她**说「我要来巴黎」、她转戒指 | 通过（F1 已修） |
| 12 | mirror · mother · gone | ✓ | ✓ 讲镜子里的母亲＝甩不掉的东西 | ✓ **她**看见母亲（幻觉归属正确） | 通过 |
| 13 | blue · crossing · guard | ✓ | ✓ 讲坏英语即教学法、being vs pretending | ✓ **Tomas** 教、她们被要求成为蓝 | 通过 |
| 14 | easily · continuation · tether | ✓ | ✓ 讲「悲伤成了最熟练的素材」 | ✓ **她**哭、Max 的手按在**她**背上 | 通过 |
| 15 | head · face · body | ✓ | ✓ 讲从念头出发的路径错误 | ✓ **Tomas** 判**她**「在你脑子里」 | 通过 |

形态：H1 `# 03. Chapter Two` ✓｜导航 5 项 ✓｜子项齐全 ✓｜块数 15（建议 14–15，硬限内）。

## R5 判定表

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| F1 | 「她十九岁没能去成的地方」 | ch03 全文无 `nineteen`（grep 0 命中）；ch16/ch21 的十九岁指怀孕与被轻视 | 信息提前且改写 | **阻断** → 改为「在欧洲——那是她一辈子没去过的地方」 |
| L1–L5 | 见 `3-diff.md` | — | 未收细节 | 提示（不修） |

## 四组报数

- 逐字：15/15 块全可核实（查无 0）
- 对应：R4 15/15 通过，施事/受事 0 反转（第 5 块 Seb 退出画框、第 12 块「她看见母亲」方向正确）
- 形态：H1 ✓ 导航 5 项 ✓ 子项齐全 ✓ 块数 15 合规
- 断言：1 条阻断（已修）+ 5 条提示

## 已核实为正确（防误修）

| 写法 | 原文 | 说明 |
|---|---|---|
| 「这个问题让她恐惧」 | `text/ch03_chapter_two.txt:269` `The question wasn’t rhetorical—it terrified her.` | 成立，勿删 |
| 「We be blue, not a blue thing」 | 原句 13 | 成立；Tomas 的坏英语（we be）是原文特征 |
| 「父亲退到画框外」 | 原句 5 `this was definitely him stepping out of the frame` | 成立，施事是 Seb |
| 「一名四十岁女人的回声」 | 原句 9 `Catherine feels like an echo` | 成立；不是「女儿是她的回声」 |
