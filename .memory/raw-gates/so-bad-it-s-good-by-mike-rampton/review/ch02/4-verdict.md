# ch02 What Actually Is a Joke? 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，7 块；`verify_fragments_indep` 全章片段 0 MISS；字符数 3,222 与概览一致。

## 逐块对应

| 块 | 引语落位 | 中文是否讲这句引语 | 关键词在引语/本章 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 原句 1 | :15 首句 | 是：两个 story / 两个 you | stories / actually ✅ | 定义者＝作者 ✅ | 通过 |
| 原句 2 | :19 | 是：场景套路→预期被养起→翻转 | scenario / teed up / licensed establishment ✅ | 预期被谁养起＝笑话场景 ✅ | 通过 |
| 原句 3 | :22 | 是：knock-knock 的答话被重新解释 | crime-fighters / entirely ✅ | **答话人＝敲门者**，md 未把听懂的一方写反 ✅ | 阻断→已修（机制写成 Po-lice 拆字，实为 police≈please） |
| 原句 4 | :25 | 是：in my pyjamas 的修饰对象换挂 | pyjamas / elephant ✅ | 射象者＝叙述者 ✅ | 通过 |
| 原句 5 | :28 | 是：让步→通则，两类 wordplay | hinge / wordplay / homonyms ✅ | 归纳者＝作者 ✅ | 通过 |
| 原句 6 | :37 | 是：权力展示的狒狒类比 | display / equivalent / revolting ✅ | 展示者＝讲笑话的人 ✅ | 通过 |
| 原句 7 | :40 | 是：weighty→weigh 的转场双关 | weighty / weigh ✅ | 说话人＝作者 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 插图 `f006-01` alt 为 “A man walks into a bar … Clang!”，本章例子的图像版 | epub 图注；图紧跟 :15 “Take this classic:” 之后，text 无对应文字 | 正确 | 通过 |
| 本书多数笑话依赖文字游戏 | :34 | 补录后正确 | 提示→已修 |
| Groucho 句属 “one- and two-line jokes” | :25 | 正确 | 通过 |

## 已核实为正确

- 原句 2 结尾 “it was a long metal thing”：`:19` 原文，md 译作“一根长金属条”，不是“铁棍/钢管”，未加码。
- 原句 4 的解读（in my pyjamas 从修饰主语改为修饰宾语）：`:25` 后文自证 “while line two reveals the much more surreal ‘truth’”，md 与作者解读一致。
- “bark” 在本章是 wordplay 举例（`:28`），md 未把它错解成狗叫情节。

## 结论

阻断 1（机制表述错，已修）/ 提示 2（已补）/ 假红 1（插图 alt 不计入 text）。修后 `chapter.sh` rc=0。
