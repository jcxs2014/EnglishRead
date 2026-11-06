# 4-verdict · ch15（R4 逐块人判 · 5 块全查）

覆盖声明：R1 子代理盲读 → 主会话 R3 对账 → 主会话逐块 R4。机器层 rc=0。

## 逐块判定

| 块 | 断言 | 证据（text/ch15_chapter_15.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 四商昨日退出/低于最低线/正午前补齐 | :38 "Four vendors withdrew yesterday…We have until noon to replace them." | 对应成立；说话人 Owen ✓ | 正确 |
| 2 | 三怪领导层/一个怪你 | :68 "Three of them told me it was leadership. One of them told me it was you." | 对应成立；说话人 Frank ✓ | 正确 |
| 3 | 十一月念出声/当成技术细节/每天在想 | :139 "I read that line out loud in a council meeting in November…every day since." | 对应成立；说话人 Owen ✓ | 正确 |
| 4 | 听不等于原谅/先听再定他的选择 | :213 "You do not have to forgive him to listen," she said. | 对应成立；说话人 Pearl ✓ | 正确 |
| 5 | 集市停办/补助随之没了/当天说坏消息按约定 | :246 "The festival is suspended…the day I got it, like we agreed." | 对应成立；留言人 Nora（voicemail）✓ | 正确 |

施事三问：块 1（通报的是 Owen、退出的是四商）、块 2（转述的是 Frank、被指的是 Nora）、块 5（留言的是她、欠账的是他）——无归属反转。
「数字」回原文：`four vendors`（:38 ✓）·`ninety percent`（:62 ✓）·`eighty-eight percent`（:83 ✓）·`forty-third`（:89/98 ✓）·`nine thousand`（:95 ✓）·`Six in favor, two abstaining`（:98 ✓）·`fifth of December`（:136 ✓）·`eighty-one`（:157 ✓）·`eleven forty-seven`（:246 ✓）。

## 已核实为正确（防误修护栏）
1. 块 2 "One of them told me it was you"——:68 原文，主语是退出的那一家，勿改成"弗兰克怪她"。
2. 块 3 "a technicality"是欧文对她的批评的回声（ch02 她原话）——勿改成诺拉自认。
3. 块 4 "she said"插语在句尾——:213 原文连续，勿判拼接。
4. 块 5 是 Nora 打给 Griffin 的留言（电话未接通）——:246 "His voicemail answered"，勿改成双向通话。
