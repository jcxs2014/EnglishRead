# 4-correspondence.md · ch26 逐块对应（人判）

> 方法：只看每块的「中文理解 / 为什么这样写 / 读者视角提示」四段中文，回答一个问题：**这段中文是不是在讲这句引语？**
> 判据：讲引语之外的上下文 ⇒ 引语选短；讲全书主旨/作者生平 ⇒ 不对应；只复述字面、没有「为什么这样写」 ⇒ 密度不足。
> 引语逐字侧已由 R2 机器层确认（5/5 ok），故此处只判「中文↔引语」的对应关系与密度。

## 块 1（`> **原句 1:**` = `‘These are fat rascals,’ Matt said, opening the box of scones he’d quickly purchased on his way out of Harrogate.`）
**对应：是（密度足）。** 中文分析紧扣引语内部的三个着力点——「on his way out」（交代来处）、「quickly purchased」（匆忙味）、司康饼的胖头傻相与「胖小鬼」的玩笑；并说明「为什么这样写」：把命案隔在食物之后。读者视角提示讲的也是这一句本身（「本章只用这一句交代」这一判断经核属实：本章正文再无一句交代 Harrogate 之行的内容）。无「引语选短」也无「只复述字面」。

## 块 2（`‘So she’s what, some sort of black widow?’` + 前置叙述 `Matt looked up at the new whiteboard that had appeared for Scott Brown’s murder.`）
**对应：是（密度足）。** 四个子项都在讲引语本身：白板→新案子→把「黑寡妇」当假设而非结论（引语是疑问句，md 也点出「疑问句的用法…这只是抛出的假设」），与后文蔡斯否定连杀假设相扣。唯一越出引语的一句是「白板是这间警局处理命案的固定动作」（记为 C4，提示），不影响本块对应判定。

## 块 3（`‘No,’ Caius said, although he hesitated. ‘Digby’s murder was thoroughly planned… Scott could easily identify them.’`）
**对应：是（密度足）。** 中文分析讲的正是引语里那段推理——两桩命案两种逻辑、动机私人却晦涩、事后灭口、犹豫紧跟「不」；「读者视角提示」也落在引语末句的「指认」动作上。施事核对：动词主语为 Caius（`Caius said`），受事为 Scott（`Scott was killed`）、对象为凶手（`identify them`）——与原文一致。唯一偏差：把 `Once we’d found him` 的触发条件译成「影像一旦找到」（原文 him = 斯科特本人），记为 W2（提示）。

## 块 4（`‘I doubt it,’ Matt said, staring at the board. ‘It was transactional. He was taking the letters to get in her good books.’`）
**对应：是（密度足，但「中文理解」有否定域反转）。** 施事核对无误：主语 Matt（`Matt said`），受事为 Scott（「替对方拿那些信」＝`He was taking the letters`），受益方为「她／对方」（`get in her good books`，方向正确）；「为什么这样写」「读者视角提示」也都在讲这句引语，且给出了「transactional」降级的理由与「盯着白板＝边想边说」的写法观察。
**问题不在对应而在准确度**：「中文理解」把 `I doubt it` 译成「**我怀疑他知道**」，中文常规读法是「我怀疑（他）知道」＝ *I suspect he knows*，与原文 *I doubt it*（*I doubt that he knew he was an accomplice*）极性相反；同一块的「为什么这样写」又写「拿信**不是**因为知情或忠诚」＝ Scott 不知道，自相矛盾。⇒ 判**对应成立**，但该块译文另记 **W1（阻断）**。

## 块 5（`‘Also known as her knickers.’ Caius’s desk phone rang… ‘It’s going to be a long night.’`）
**对应：是（密度足）。** 中文分析紧扣引语本身的结构变化：电话响 → 玩笑收束成一串具体指令 → 三条线索分给三人 → 「会是个漫长的夜晚」写时间压力；「读者视角提示」讲的也是这三路各自的落点（入职表/母亲联系方式、The Purple Toad 的约会线、电子设备）。施事核对：`Matt, get the staff from The Purple Toad in` → Matt 去叫人；`Amy, please chase up where his electronics have got to` → Amy 去查电子设备；`I’ll deal with that` → Caius 自己处理母亲联系方式——三路归属与原文完全一致。唯一弱点：开头那句荤笑话的说话人原文未标注，md 块级写「有人」是稳妥的（导航里归给 Amy 见 C2，提示）。

---

## 小结

- 逐块对应：**5/5 成立**（无「引语选短」块，无「讲全书主旨/作者生平」块，无「只复述字面、无为什么这样写」的低密度块）。
- 密度（机器层）：块 1–5 的「中文理解」CJK 占比 0.59–0.83、「为什么这样写」0.69–0.89、「读者视角提示」0.73–0.89，「关键词」子项 CJK 计数 0（该子项按设计放英文词条，`keyword_bad 0`）——无「中文过薄」块。
- 逐块对应层面发现的实质问题只有一处、且属**译文准确度**而非对应关系：**块 4 的否定域反转（W1，阻断）**。
- 其余与引语无关或越出引语的问题集中在导航与总结层（C1 分部名、C2 荤笑话说话人、C3 联系方式位置、C4 白板通则、W3 总结压缩），见 `3-diff.md` 与 `4-verdict.md`。
