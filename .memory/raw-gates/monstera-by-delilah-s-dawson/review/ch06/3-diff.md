# ch06 a store bought cake —— R3 差异单

对照物：`review/ch06/1-suread.json`（R1 独立素读，8 条）＋ `review/ch06/2-machine.json`（R2）。

## 单子一：漏（素读有、md 未体现）
- 无关键事件/转折缺失：箱子搬不上楼、拿松饼换一次接触、四点搬电视、坦白身世、锁、拥抱、气球+超市蛋糕——八条全部已入块或已入导航。
- `She smells like vanilla and clean laundry and girl`（`:112`）、`I've said weird like ten times`（`:124`）属细节。非漏。

## 单子二：编（md 有、素读无）
- **1 条（已修）**：叙事手法原写「声音分三层：窗外是铁片的 clank，耳边是心跳的 thunderstorm，**楼上是下楼的脚步**」——全章没有「下楼的脚步」这类声音描写（`steps` 只出现在 `In two steps` 与 `little steps`，均为动作/比喻）。已改为可核实的第三层：四点整的敲门声（`:52`）。

## 单子三：错（md 与素读不一致）
- **1 条（已修）**：原句 6 的引语从 `wasn’t` 起句，把主语 `I…` 丢在引号外，成为全书唯一一处「引语从句子中间起头」的块（用正则扫 29 章仅此一例）。已恢复成原文整句起头 `I… wasn’t allowed out of the house after middle school.`——`…` 是原著自带的停顿，实测 `structure.py order` 与 `chapter.sh` 因此全绿（真正会让块序「不可判定」的是**跨句缝合**的 `…`，不是原文自带的这一个）。
