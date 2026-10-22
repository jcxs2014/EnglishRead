# ch43 4-verdict

- 文件：`ch43 this is not your home.md`
- 结论：**1 阻断 / 4 提示**

## 阻断

### 阻断 1｜原句1 读者视角提示（第 32 行）：把"没缠绷带的手"说成受伤的那只手
- 位置：`ch43 this is not your home.md:32`「注意"unbandaged hand"。她身上还带着上一章伤的那只手，这只手现在握着斧头。」
- 原文证据：`text/ch43_chapter_43.txt:8`「I wheezed and splayed out my arms, the axe still clutched in my unbandaged hand. Miraculously, I hadn’t gouged myself with it.」——`unbandaged` 是"**没有**缠绷带"的那只，也就是**没受伤**的那只。受伤的手在第 40 章由 Callie 包扎：`text/ch40_chapter_40.txt:146`「Callie-Ann gently applied a sterile patch to my now clean hand and wrapped a bandage around it.」、`:347`「She pointed to my bandaged hand.」；第 41 章同一个用法：`text/ch41_chapter_41.txt:17`「the dirt on my unbandaged hand」（用没伤的那只洗脸，`:29`）。
- 为什么是阻断：md 把"没伤的手"写成"伤的那只手"，是**受伤归属反转**（哪只手伤、哪只手握斧全反了），且顺手把伤口年代说成"上一章"（实为 ch40）。这类"身体部位/施事归属"错误正是本章要防的。
- 建议改后中文：「注意"unbandaged hand"——**没**缠绷带的那只，也就是没伤的那只；伤手是第 40 章 Callie 包扎的另一只，此刻空着。两只手分工正好说明：她是用还能用的那只握着斧头。」

## 提示

1. **导航·一句话概括（第 12 行）｜两次扑击被压成一次（提示）**
   证据：`text/ch43_chapter_43.txt:50`「The figure burst into life, arms raised high and wide, impossibly long, bending in all the wrong places. It charged toward me.」→ 她挥斧打中、尖啸、它消失（`:53-62`）→ 屋里静下、她看见空屋（`:68`）→ 然后 `:83`「An explosion of wood to my right. The front door burst open. The figure rushed me from the outside.」md 只写"然后从门口扑进来"，把第一次从客厅里的冲锋与她的第一次命中省掉了。建议改为：「它先冲了一次，她挥斧打中、只换来一声尖啸；等屋里静下来，前门又爆开，那东西从外面再冲进来。」

2. **导航·情感弧线（第 14 行）｜"第一次带着怒火打回去"与前面章节冲突（提示）**
   证据：她此前已经动过斧——`text/ch29_chapter_29.txt:11`「…or smacking an axe into someone’s face? I’d google it later.」、`text/ch40_chapter_40.txt:182`「“I put an axe in her head.”」、`text/ch38_chapter_38.txt:89` 也说她让邻居额上留了疤。建议限定为："这一章是她第一次在**知道对手是什么**之后，仍然带着怒火打回去"。

3. **全章｜漏掉"你把她惹成猎人了"这句（提示）**
   证据：`text/ch43_chapter_43.txt:11`「Well, you definitely have her on the hunt now.」这是她滚下楼梯后的第一反应，也是本章"决斗"性质的定调（她现在是猎物）；md 内 `hunt` 查无（rc=1）。建议在导航或原句1 分析后补一句。

4. **词汇表高级档（第 93 行）｜`mantras` 释义"曼陀罗"错（提示）**
   证据：`text/ch43_chapter_43.txt:35`「…and repeat your mantras…」；`mantra` 是"曼怛罗/真言、反复念的咒语"，**曼陀罗（mandala）**是另一回事（坛城/图样），且与"反复念"不搭。建议释义改为「曼怛罗，反复念的咒语/真言」，原句2 中文里的"曼陀罗"同改。

## R4 三问

1. **谁做的**：① 说"这不是你的家"、亮起光点眼、两次扑上来的是**同一个瘦长黑影**（`:17,26,35,44,50,83`）；② 挥斧的是 Tamsin（`:53,89`），第一次命中换来一声尖啸（`:56-59`），第二次连砍到"挥空、失衡"（`:92`）；③ 前门是那东西从外面撞开的（`:83`「The front door burst open. The figure rushed me from the outside.」），不是她开的；④ 章末地上的脸是 **Rowan 的**，但**谁把它打成这样、它是不是 Rowan 本人，本章一个字都没交代**（`:101` 只给脸、光、黑液）。
2. **什么关系 / 谁欠谁**：这一章没有"复制体-本体"的判定，也没有债务关系；它的关系轴是**占有权之争**——它反复说"这不是你的家/房子"（`:17/44`），她手里的凭据（纸、钱、族谱、法）被逐项作废（`:35`）；她与 Rowan 的关系在本章被推到最危险处：如果地上那张脸是真的，她刚刚亲手砍了他；如果是假的，那她砍的是"顶着 Rowan 脸的东西"——原文**刻意不给答案**，md 也没给，正确。
3. **数字与死因**：① 无年龄、无金额、无日期；② 数量只有"一级一级楼梯"（未计数）与"两次冲锋"；③ **本章无确认死亡**——只有"被打烂的脸"（`battered face`）与"黑色液体"（`black liquid`），没有 `dead`、没有 `blood`（原文用 `black`，`coppery` 只写气味）；把黑液直接说成"血"、或说"她杀了他"，都属无据；④ 她的伤：肋侧尖痛（`:14`）、髋部（`:62`）、小腿淤青未断（`:8`），均非致命。

## 已核实为正确（下一轮不要改坏）

① 原句 1–6 逐字，均可在本章相邻自然段内对上；② "papers and coins"指第 1 章那叠购房文件**有据**：`text/ch01_chapter_1.txt:17`「I dug out my copy of the paperwork from the glove box. … So, I signed without reading it properly.」——跨章指认正确；③ "眼睛按位置认出来、不是按样子"（`:38`）是原文的判断，md 未写反；④ 空屋清单（没有沙发/扶手椅/餐桌，只有一张羊皮毯，`:68`）与 md 一致，未添家具；⑤ 结尾"不结案"的处理正确：md 明说"既不说我杀了人，也不说那是假的"（第 80 行），与原文一致；⑥ `black` 而非 `red` 被点出（第 80 行），这是本章最关键的留白，下一轮不要改成"血"。
