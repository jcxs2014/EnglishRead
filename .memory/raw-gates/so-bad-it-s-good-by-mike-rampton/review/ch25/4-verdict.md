# ch25 Bad Jokes About Bad Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 偷窃癖 | :15 | 是：take things literally | literally ✅ | 解释＝你 ✅ | 通过 |
| 2 let minnow | :20 | 是：let me know | minnow ✅ | 说＝我 ✅ | 通过 |
| 3 tearable | :25 | 是：tearable/terrible | tearable ✅ | 有＝我 ✅ | 通过 |
| 4 失业者 | :70 | 是：don't work 双义 | don't work ✅ | 有＝我 ✅ | 通过 |
| 5 时间旅行者 | :95 | 是：过去时 | time-travelling ✅ | 讲＝我 ✅ | 通过 |
| 6 no pun in ten did | :135 | 是：no pun intended | ten puns ✅ | 投稿＝我 ✅ | 通过 |
| 7 Cornea | :130 | 是：corny | cornea ✅ | 写＝我 ✅ | 通过 |
| 8 bad joke vs dad joke | :140 | 是：a parent | a parent ✅ | 说＝答者 ✅ | 通过 |
| 9 McEnroe/Oldman | :167 | 是：Sirius Black | Sirius Black ✅ | 扮＝我 ✅ | 通过 |
| 10 反问句 | :177 | 是：无答案的问句 | rhetorical ✅ | 说＝作者 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 28 + 3 条（原写"约 30 条"） | 35 段拆分 | 改后正确 | 提示已修 |
| 404 词 | `len(text.split())`=404 | 正确 | 通过 |
| 字符数 2,270 | `len(text)` | 正确 | 通过 |
| 十则双关 | `:135` 逐字 ten puns | 正确 | 通过 |

## 已核实为正确

- 原句 7 的 `Cornea`（`:130` 段）是 corny 的谐音载体，md 未把它当解剖学解释。
- 原句 9 的 McEnroe 梗依赖 `You cannot be serious`，`:167` 原文有该语境的铺垫，md 已写明"麦肯罗名言"。
- 章末三则确无包袱（`:167`/`:172`/`:177`），与 md"全部没有包袱"一致；抬头重复两次（页眉+小节标题）已在计数里按 2 个头扣除。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。
