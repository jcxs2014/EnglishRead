# ch14 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，12 块 12 引语，issues 全空。
R4 人判：12/12 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 素读#7「1898 Rosebud 录音／Pratt 烧毁档案」未入任何块 | 素读 anchor 命中 True | 硬年份史实缺席，Benjamin 动机链的第一环缺失 | 提示（建议补记，本轮不改稿） |
| 素读#1/#2/#5/#6 细节未入块 | 素读 anchor 命中 True ×4 | 场景细节级 | 提示（不修） |
| 块6 施事：砸晕者=Benjamin、凶器=Christian 的后视镜 | 引语「wrenched off the first thing his hand could clamp on…popped her…on the left temple」；素读#4 | 一致；「power-off button」为叙述者比喻，md 未误作事实 | 已核实为正确 |
| 块4「He already called me once」 | 素读#3（Mooch 挥小翻盖手机） | 一致 | 已核实为正确 |

取证命令记录：
- 素读 anchor 偏移验证 True ×8（ch14 子代理自证，覆盖 1898/Carlisle 十一名男孩等数字锚点）
- `/usr/bin/grep -n "wrenched off" text/ch14_13_road_king.txt` → 命中（块6 引语）；退出码 0

## 已核实为正确

- 块6「power-off button」的翻译「关机键」保留叙述者的机械比喻，未被误写成 Mooch 真的关掉了什么。
- 块8「old-style pull tab」译「旧式拉环」+「when he was sixteen」——啤酒罐的年代细节（Benjamin 十六岁时代）与素读#6 一致；「八罐中的第一罐」为素读#6 增补细节，md 未提（见漏项）。
- 块12「shirtless, one side of his face crusted with dried blood, his mouth open like he was a child, crying」——与素读#8 逐要素对应（光膀子/半脸血痂/张嘴如孩子哭）。

**结论：阻断 0、提示 2（1 不修、1 建议补记 1898/Pratt 史实）。本章干净。**
