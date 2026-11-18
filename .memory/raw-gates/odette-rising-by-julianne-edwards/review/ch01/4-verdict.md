# 4-verdict · ch01 the funeral from the window（T3 深审 2026-11-18）

R1：子代理盲读 8/8（区间验证 0 失败）。R2：chapter.sh --json rc=0。R3：漏 0 / 编 2 / 错 0（见 3-diff.md）。

## 逐块判定（10 块）

| 块 | 断言 | 证据（text/ch01_chapter_1.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 原句1 house/bier | 中文理解「灰、方正、退坐」＝引语 | 区间 87:318 附近逐字 | 对应 | ✅ |
| 原句2 silhouette | 「煤气灯在身后亮」＝引语 | "framed in silhouette by the gas lamps" | 对应 | ✅ |
| 原句3 ten years | 「十年没出过家门」 | "she had not left the house for ten years."（4602:4643） | 对应 | ✅ |
| 原句4 gossip | 谣言清单逐项＝引语；说话人＝Dendron 与 Cook 的转述 | "had heard Madame Dendron and Cook gleefully repeating the gossip" | 对应 | ✅ |
| 原句5 gossamer | 动机剥层＝引语 | "It was a need to feel... of gossamer." | 对应 | ✅ |
| 原句6 buildings | 面包房凸窗/金字招牌＝引语 | "bow windows and a sign in gold leaf" | 对应 | ✅ |
| 原句7 wonder | 因果链（先退/再被推）＝引语 | "retreating at first from her father's indifference, and then the world's scorn" | 对应 | ✅ |
| 原句8 scowler/factory man | 施事：看的人＝粗脸男人（he looked directly at her）；被看＝她——与原文一致 | "he looked directly at her and paused" | 对应（修复后） | 阻断→已修（儿子偷看系墓园场，跨场景归属） |
| 原句9 collapse | 施事：跪倒＝她；赶来＝邻居——一致 | "At the second tree she collapsed... The pale neighbor rushed to her." | 对应（修复后） | 阻断→已修（「第一次被陌生人伸手」无据且与 driver 触碰矛盾） |
| 原句10 sky/empty space | 「快的人＝静止的人」＝引语内对撞 | "He had been such a fast man; must he lie still now forever?" | 对应 | ✅ |

## 修复（3 处，均已跑 chapter.sh rc=0）

1. 原句8 分析补括注：随行男孩不在引语内、偷看发生在墓园一场。
2. 原句8 读者视角提示删「儿子还在旁边偷看她」。
3. 原句9 读者视角提示「十年来第一次被陌生人伸手」→「跪倒后第一个赶来的外人」。

## 已核实为正确

- 「十年来第一次离家」的限制：ch01 内她此前仅到过庭院门槛（front door），driver 触碰发生于同日出门过程——原句9 修复后不再含「第一次」断言。
- 原句4 「他太太死得及时」：原文 "How fortunate that his wife had died young and had not lived to see this."——同情流向父亲而非母亲，转述无误。
- 原句3 「十年」为原文逐字（ten years），非修辞。
- 导航「邻居（瘦高、黑发、约三十）」：text "a tall man of about thirty, with a slender face and black hair"。

已核实为正确（本节按 R5.5 固定格式收尾）：以上各条后续不得以「读着不对」为由改动，除非给出反证。
