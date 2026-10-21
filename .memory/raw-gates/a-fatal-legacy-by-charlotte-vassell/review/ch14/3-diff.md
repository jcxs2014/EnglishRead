# 3-diff.md · ch14《A Fatal Legacy》审查对账（漏 / 编 / 错）

- 原文（唯一权威源）：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch14_14.txt`（3,550 字符 / 113 行）
- md（审查当时名）：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch14 the red lion is closing down.md`
- md（**现名，2026-10-21 14:26 依 C1 改名**）：`…/ch14 the special unit is closed down.md`（软链接同步）
- 行号＝原文 `text/ch14_14.txt` 的行号；引语逐字抄。
- 语料完整性核验：`library/*.epub` 的 `OPS/s025-Chapter-014.xhtml` 与 `text/ch14_14.txt` 逐行比对（去页码后）**完全一致**，语料无缺段、无并章。

---

## 一、漏（原文有，md 无）

### L1 ·「凯厄斯会不会辞职」这条线全章未进 md —— 档：提示（严格判据可升阻断）
- 原文（`text/ch14_14.txt:59–63`）：
  > `‘Do you still think he’s going to quit?’` / `‘Yeah.’ Matt watched Caius from across the pub. ‘His family will make him or maybe even Callie.’`
- md 侧：5 个引语块、导航 5 项、一句话总结全文检索无「quit / 辞职 / 不干」任何一处。
- 说明：这是本章唯一一条**新开的剧情问句**（且与全书人物设定相扣：`text/xx_characters.txt:20`「he is surprised he's still there」），读者读完精读会漏掉「凯厄斯可能不干了」这条线，以及马特给出的答案（家人会留住他，也许 Callie 也会）。
- 建议：在「线索结构」或「人物弧线」里补一句即可，不必新开引语块（本章 5 块已达本书下限，见形态组）。

### L2 · 凯厄斯对 Hampton 的最新态度「I have. I left him on read.」未进 md —— 档：提示
- 原文（`text/ch14_14.txt:83`）：`‘I have. I left him on read.’`（艾米问「Heard from him?」之后）
- md 侧：导航只在「线索结构」里列了「Hampton 退出内阁引发的领导权之争」，未提凯厄斯本人对 Hampton 的态度（已读不回）。
- 说明：属可接受的取舍（本章 5 块），但「已读不回」是全书 Hampton 线的最新状态，值得一句。

---

## 二、编（md 有，原文无）

### C1 ·【阻断】文件名 keyplot「the red lion is closing down」——凭空的情节：Red Lion 酒吧全章（全书）没有要关闭
- md 侧：文件名 `ch14 the red lion is closing down.md`（= 站点 URL slug 与章名）。同名软链接亦存在：`ch14 the red lion is closing down -> ch14 the red lion is closing down.md`。
- 原文侧（逐字）：全章 113 行里**没有任何一句**说酒吧要关闭；被关闭的是**专案组（special unit）**：
  > `text/ch14_14.txt:38`：`‘Nope.’ They’d been summoned to the Chief Superintendent’s office a little over three weeks ago and had been informed of its closure.`
  > `text/ch14_14.txt:53`：`He hadn’t mentioned the unit closing beyond uttering ‘Well, that’s that’ in the lift afterwards.`
- 取证（按 R5-补「零命中」三件套：显式路径 + 贴命令输出 + 退出码）：
  ```
  $ cd notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text
  $ /usr/bin/grep -n "Red Lion" *.txt
  ch14_14.txt:17:The Red Lion Public House          （退出码 0；全书仅此 1 处＝章节小标题）
  $ /usr/bin/grep -n -i "closing" *.txt
  ch12_12.txt:26 / ch13_13.txt:256 / ch14_14.txt:53 / ch30_30.txt:62   （退出码 0）
  $ /usr/bin/grep -n -i "closed" *.txt
  ch12 / ch14:41 / ch16 / ch22 / ch23 / ch31 / ch32 / ch33 / ch37 / ch47   （退出码 0）
  ```
  「Red Lion」全书只作为**小标题**出现一次；`closed/closing` 的全部命中里，与本章相关的两处（:41、:53）都指**专案组**。
- 影响：这个 keyplot 是本次审查任务书（「众人常去的酒吧面临关闭」）的来源，属于把「关掉的单位」错记成「关掉的酒吧」。
- 建议改名（保持 `ch<NN> <keyplot>.md`、单空格、无标点的约定）：
  `ch14 the special unit is closed down.md`；并同步修 `ch14 the red lion is closing down -> ch14 the special unit is closed down.md` 软链接与 `00_情感节点.md:56` 的「节点五：据点被撤掉之后（ch13-ch14）」指向。

### C2 · 导航「表面是三个人同时松了口气」——只有艾米一个人松了口气 —— 档：提示
- md 侧（`ch14 the red lion is closing down.md:11`）：「表面是**三个人同时**松了口气，实际上他们失去的正是那个共同据点」。
- 原文侧：只有艾米表态（`text/ch14_14.txt:41`）：`‘I’m so glad it’s been closed down.’ Amy was relieved to no longer have the possibility of being compromised hanging over her.`；马特没有一句表示如释重负，反而是 `text/ch14_14.txt:50`：`‘Something will. Hampton’s down but he’s not out.’`
- 说明：把「艾米庆幸」扩写成「三人同时松气」是群体情绪的凭空扩大。md 自己的第 1 块、第 2 块其实写对了（艾米庆幸 / 马特戳破），与导航自相矛盾。建议改为「表面上艾米松了口气」。

### C3 · 把马特的推测（I think）写成既定事实（导航与总结层）—— 档：提示（文件内自相矛盾）
- md 侧：
  - `ch14 the red lion is closing down.md:11`（导航）：「**Caius 原本指望**借它查清姐姐下落的机会也就没了」；
  - `:101`（一句话总结）：「一个字的没提他失去的是**查姐姐的机会**」（把马特的判断当成凯厄斯的既成事实）。
- 原文侧（`text/ch14_14.txt:56`）：`‘He’s taken the end of the special unit harder than I thought he would. **I think** he saw it as his chance to work out what happened to his sister.’` —— 原文明确是马特的**推测**（I think），本章内凯厄斯本人从未讲过这句话，也未确认过这条因果。
- 关键对照：md 自己的第 4 块处理是**对的**（「**在马特看来**，凯厄斯一直把这个单位的存续当成查清姐姐下落的指望」）⇒ 同一文件两层口径不一致。
- 建议：导航与总结层补「马特认为」三字即可（总结层尤其要，因为它是全书读者最后看到的句子）。

---

## 三、错（两边都有但不一致）

### E1 ·【阻断·说话人／施事】第 2 块：把「什么会接替它」的提问者安给了艾米 —— 实为马特问、艾米反问
- md 侧（`ch14 the red lion is closing down.md:28`，原句 2 的**中文理解**）：
  > 「**艾米问他**「什么东西会接替它」，马特既没有安慰，也没有顺着说单位没了是好事，只丢下一句断言……」
- 原文侧（`text/ch14_14.txt:44–50`）：
  > `:44` `‘I wonder what will replace it?’ Matt said off-handedly.`
  > `:47` `‘What do you mean?’`（← 这一句才是艾米说的）
  > `:50` `‘Something will. Hampton’s down but he’s not out.’`
- 判定：这是「生产-审查对照.md §⑥ 施事/归属反转」类（提问者与答话者对调）。四道机器探针全绿（引语逐字 5/5、中文是中文、关键词成立、形态正常），只有 R4 固定三问能抓。
- 建议改法：「马特随口问『什么会接替它』，艾米反问『你什么意思？』，马特既没有安慰，也没有顺着说单位没了是好事，只丢下一句断言……」

### E2 ·【提示·说话人语体】第 3 块：「艾米说」——原文这句是艾米的心里话
- md 侧（`:35`）：「**艾米说**，她觉得自己了解凯厄斯的一切，可与此同时又觉得对他其实什么都不知道。」
- 原文侧（`text/ch14_14.txt:53`）：`Amy nodded. She watched Caius at the bar. He hadn’t mentioned the unit closing beyond uttering ‘Well, that’s that’ in the lift afterwards. ‘I feel like I know everything about Caius, and yet I somehow also feel like I know nothing about him either.’`
  —— 本句**无言语动词**，紧跟叙述句；对照前一分句用 `uttering` 明指凯厄斯在电梯里说出口的 `‘Well, that’s that’`，可知本句是艾米的**内心活动**，不是说出声的话。
- 佐证：md 自己在同一句后半已经按「心里话」处理（「正是她站在酒吧这边盯着吧台那头的凯厄斯时**冒出来**的」）。
- 建议：把「艾米说」改为「艾米心里想／艾米想」。

### E3 ·【提示·计数唯一性】第 2 块读者视角提示：「这一章唯一一处对『事情已经结束』的反驳」
- md 侧（`:31`）：「它是这一章**唯一**一处对「事情已经结束」的反驳。」
- 原文侧：第 1 块的原句本身就是一处反驳——`text/ch14_14.txt:41`：`Although to her mind the threat of being dragged into a truly heinous conspiracy would never quite go away now.`（艾米明说这个威胁「永远不会完全消失」＝不承认事情已结束）。
- 建议：删「唯一」或改为「最直白的一处」。

### E4 ·【提示·计数】第 5 块为什么这样写：「邀请又被**两个**客气的说法挡了回去」
- md 侧（`:51`）：「接下来那句邀请又被两个客气的说法挡了回去，客气本身就是距离。」
- 原文侧：引语之后只有两句——
  > `text/ch14_14.txt:110`：`‘One weekend perhaps,’ Matt said, being diplomatic.`（马特唯一一次「客气」的挡回）
  > `text/ch14_14.txt:113`：`‘Yeah,’ Amy said, sipping on her dandelion and burdock.`（艾米是**应允**，不是挡回）
- 判定：挡回邀请的客气说法只有马特那一句；艾米那句「Yeah」是同意，把两个都算成「挡回去」计数错误。
- 建议：「……邀请被马特一句圆滑的『或许一个周末』挡了回去；艾米只是应了一声『嗯』——客气本身就是距离。」

### E5 ·【提示·措辞】第 5 块为什么这样写：「作者让主角亲口说出对继承生活的**不安**」
- md 侧（`:51`）：「作者让主角亲口说出对继承生活的不安，却把最重的那部分用「太习惯」三个字轻轻带过。」
- 原文侧（`text/ch14_14.txt:107`）：`‘Yeah, but he’d drive me insane,’ Caius said, before taking a sip of his pint. ‘I’m getting used to it all. I think I’m going to get too used to it. I’d invite you guys up, but I appreciate that you might not fancy it.’`
- 判定：**说话人核对通过**（＝凯厄斯，非马特、非艾米）；但原文只写「我在习惯这一切」，「不安」是解读而非文本事实，且「太习惯」三个字不成立（原文是 `too used to it`，中文作「太习惯」可以，但正文写「三个字」略不贴）。属解读层的措辞，非事实错误。
- 建议：把「对继承生活的不安」标成读者解读（「读者容易读出…的不安」），并把「三个字」改成「三个词」。

### E6 ·【提示·硬编造核对通过项】导航「凯厄斯姐姐的**失踪**」
- md 侧（`:13`）：「凯厄斯姐姐的失踪」。
- 原文侧（本章 `text/ch14_14.txt:56`）只写 `what happened to his sister`（未言失踪）；但全书设定支持「失踪」：`text/xx_characters.txt:20`「Feeling duty-bound, Caius joined the Met after the unsolved **disappearance of his sister Lydia**」。
- 判定：**不算编**，登记在「已核实为正确」。

---

## 四、机器层与语料完整性（备查）

- `bash scripts/chapter.sh "<书目录>/ch14 the red lion is closing down" --json` → **退出码 0**，verdict=ok；引语逐字 5/5 命中（我用独立脚本复核：5 条引语在 `text/ch14_14.txt` 中各命中且**仅命中 1 次**，逐字一致）；关键词 5 块全成立；子项 4 项齐全；CJK 密度最低块（块 5 中文理解 45 字 / 比例 0.88）不触发阈值；词汇表 28 条例句逐条 `count == 1`。
- 语料：epub `OPS/s025-Chapter-014.xhtml` ↔ `text/ch14_14.txt` 逐行一致（差异仅为 epub 的页码与一处硬换行）⇒ **语料无缺、无数值漂移**。
- 书中章 14 所属分部是 epub 的 `OPS/s021-Part-004.xhtml` = `MONDAY`（任务书写的「A MONDAY IN MAY」是 Part-001 的标题，与本章所属分部不符；这是**任务书口径**，非 md 缺陷——md 的 H1 用小标题，与本书 54 章一致）。
