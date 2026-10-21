# 4-correspondence · ch20 逐块对应（人判，不可机械化）

判据（R4）：**这段中文是不是在讲这句引语？**
- 讲的是引语之外的上下文 → 引语选短（退回创建卡 §2 ①）
- 讲的是全书主旨／作者生平 → 不对应
- 只复述字面、没有「为什么这样写」 → 密度不足
固定三问（施事／归属）：① 每个动词的主语是谁 ② 受事是谁 ③ 「谁的／谁欠谁／谁问的」回原文看 `by`/`to`/`from`/`of`。

| 块 | 引语（原文逐字，区间） | 中文讲的是不是这句引语 | 施事三问核对（主语／受事／归属） | 密度 | 对应结论 |
|---|---|---|---|---|---|
| 原句 1 | `‘The old adage is that you wait for the twelve-week scan because most miscarriages happen earlier than that.’`（L26，`[274,383)`） | 是：讲「用一条老规矩把「什么时候告诉别人」这问题往后推」；引语前一句是 Caius 的 `‘When can we tell people?’`（L23），中文把它作为触发语境写出——这是引语的**直接前件**，不算越界 | ① 主语=Callie（这条老说法是她说的）✓ 与原文一致；② 受事=「等满十二周再公布」这件事 ✓；③ 「告诉别人」的发起人是 Caius（L23），md 写「凯厄斯钻进被窝后问」✓ 方向未反 | 有「为什么这样写」：把犹豫包进不容置疑的理由，且把它升级成全章的句法母题（不是字面复述） | **对应成立**（密度足） |
| 原句 2 | `‘Bits and pieces from portraits,’ Callie said, sitting up. ‘I think that a sort of Renaissance-era portrait of Eulalia could be really interesting.’`（L56，`[1137,1285)`） | **半对应**：前两句（捡速写本、问在画什么）讲的是引语**之前**的 L53 setup → 引语选短（提示）；后半（用创作计划代替请求、谁先提）确在讲引语本身 | ① 主语=Callie（`Callie said, sitting up`）✓；② 受事=Eulalia 的肖像 ✓；③ 「抬上桌」=她在本章第一个提到 Eulalia ✓（`grep -c "Eulalia"` → 1） | 有「为什么这样写」：交付物包装法；但**理由层前提被换掉**——原文无人提出「去见她」，md 却把它写成「要不要去见她」被包装（见 3-diff 编-3，阻断） | **对应成立但带编造前提**（引语选短 1 处 + 前提错误 1 处） |
| 原句 3 | `‘You should speak to Georgie.’`（L59，`[1288,1318)`） | 是：讲「不表态、只转介」这一手法；引语外扩到全章模式也仍围绕这句的语气 | ① 主语=Caius ✓（L59 紧接 L56 Callie 的话，属 Caius 回话）；② 受事=Callie（对 Callie 说的建议）✓；③ 方向：Callie→Caius 提画像，Caius→Callie 给转介 ✓ 未反 | 有「为什么这样写」：否定式转介、问题性质被换掉 ✓ | **对应成立**（但同段末尾「每一个念头都走这条路径」是本章级过宽断言，见 3-diff 错-1，阻断） |
| 原句 4 | `‘Yes, I thought the same, but I doubt there’s time for a full-blown portrait. I love the idea of sketches. Not Vitruvian man exactly, but something along those lines.’`（L62，`[1321,1488)`） | 是：讲「她自己也把野心降一档」与「用 Vitruvian man 抬高速写的谱系」 | ① 主语=Callie ✓（`Yes, I thought the same` 回 L59 的建议）；② 受事=完整肖像→速写 ✓；③ 「想到一块儿去了」的「也」指 Caius 的转介建议 ✓ 归属正确 | 有「为什么这样写」：务实理由与学术谱系对冲，退让看起来像品味 ✓ | **对应成立**（密度足，无归属反转） |
| 原句 5 | `‘Tabs wants to go for coffee.’ Callie reread the message twice. She didn’t know what to do. She didn’t want to be rude, Tabs was a nice girl, but she also didn’t think it was wise to get sucked into that circle. ‘I’m not sure.’`（L140，`[3711,3938)`） | 是：讲犹豫如何被写成「动作＋两条相反理由」，并把「我不确定」定性为「未结案」而非拒绝 | ① 主语=Callie（reread / 不知道该怎么办 / 给两条理由）✓；② 受事=Tabitha 的邀约 ✓；③ 「谁问的」=Tabitha（L135 消息）✓；④ 唯一小瑕：「三个字」与「我不确定」四字不符（3-diff 错-2，提示） | 有「为什么这样写」：信息没变是人乱了；两条理由并排、不给真怕的东西 ✓ | **对应成立**（密度足） |
| 原句 6 | `‘There you go,’ Caius said, whisking the eggs together and adding them to the pan. It might not be the worst thing if Callie heard the odd account of Arthur Hampton’s goings-on. ‘Meet up with her.’`（L149，`[4136,4333)`） | 是：讲「谁替谁做了决定」与「替她做决定时真正追求什么」——正对本章专属判据的最后一环 | ① 主语=Caius（`Caius said` / 搅蛋下锅）✓；② 受事=Callie（`Meet up with her` 指令指向她）✓；③ 归属方向：`Arthur Hampton’s goings-on` = Callie 可能听到的对象；动机归 Caius（叙述插入其内心）✓ 未反；④ 「上一句」= L146 的 `‘Mercenary, I know.’` ✓ 相邻关系正确 | 有「为什么这样写」：家常话替另一桩心事定下一步；「你看吧」把她的自嘲当证据 ✓ | **对应成立**（密度足） |

**逐块小结：6/6 块的中文都在讲各自引语**（原句 2 属「对应成立但含编造前提 + 引语略短」，原句 3 属「对应成立但段尾含本章级过宽断言」）。
**密度：6/6 达标**——每块都有「为什么这样写」的机制层解释，没有只复述字面的块。
**引语选短：1 处**（原句 2 的中文首句讲了引语外的 setup 句 L53）。
**施事/归属反转：0 处**（3 问逐块核对，主语、受事、归属方向与原文一致；唯一方向性疑问「去见她」在导航 L8 中经核为指 Tabitha，正确）。
