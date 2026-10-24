# ch26 判定表

机器层 rc=0，**4 块**（`counts.block_target=[2,3]` 只是提示值，`block_count=0` 未判红；`block_limit=[2,15]`）。人判结论：**漏 8 · 编 0 · 错 2 · 提示 10**；**无阻断**。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| Celia 的正面表白与 Clare 的回答未进任何块 | `text/ch26_celia_says.txt:93`「She tries again. “Clare? I love you. Why don’t you love me?”」；`:97`「“I do love you. But not the way you want to be loved.”」；`/usr/bin/grep -c -F "I love you" "ch26 celia says.md"` → `0`（`rc=1`） | 摊牌顶点只有「一句话总结」的转述，无逐字引语 | 提示 |
| Henry 的遗言钩子被压成「两人都停住」 | `:181`「“But Henry would never have left you. I mean, his last words were—”」；`:185`「“Enough, Celia.”」；md `grep -c -F "last words"` → `0` | 事件在（导航 `:12`、总结 `:89`），钩子（遗言是什么）未点出 | 提示 |
| 「She's restful.」整段缺失 | `:111`「“She’s restful.”」；`:115`「“You don’t really go for restful! Henry sure wasn’t restful. Really, Clare, what?”」；md `grep -c -F "restful"` → `0` | Beck 的性格定性没进 md | 提示 |
| Ingrid 的情史被引语起点切掉 | `:102`「Celia has had bad luck with love. Celia loved Ingrid, who loved Henry and then killed herself.」；md 原句 3 自「I love Henry」起引；md `grep -c -F "Ingrid"` → `0` | 引语起点截短 ⇒ 「她为什么等这么久」失去解释 | 提示 |
| 老妇皱眉与「Ain't they got any lesbians where you're from?」缺失 | `:193`「I slide my hand across the table and Celia takes it. An elderly white woman two tables over frowns at us. Celia smiles at her and says sweetly, “Ain’t they got any lesbians where you’re from?”」；md `grep -c -F "Ain’t they got"` → `0` | 公共场合张力缺失 | 提示 |
| 「To the next Jane Addams」缺失 | `:29`「“To the next Jane Addams,” I say as we touch glasses.」；md `grep -c -F "Jane Addams"` → `0` | 祝词的具体所指被抹成「庆她拿到社工执照」 | 提示 |
| 「只在上周 Charisse 生日会见过 Beck 一次」缺失 | `:38`「Celia seems to know more than I’ve told her about my recent encounters with Beck, even though Celia’s only met Beck once, at Charisse’s birthday party last week.」；md `grep -c -F "Charisse"` → `0` | 信息不对称的来源没交代 | 提示 |
| 收束句「If it can't be me, then Beck seems all right.」未引 | `:213`「“Seriously for a minute, Clare,” Celia says, her hand on my bare arm. “If it can’t be me, then Beck seems all right.”」；md `grep -c -F "If it can’t be me"` → `0`；总结 `:89` 有转述 | 末段台词只剩转述 | 提示 |
| 导航把「握手」并进「临别」 | 握手在 `:193`「I slide my hand across the table and Celia takes it.」（`We order pie` 在 `:208`，即握手在吃甜点**之前**）；临别只有拥抱 `:221`「Celia reaches up to hug me」 | 时序错位 | 提示 |
| 原句 2 引语漏掉呼语「Clare.」 | `:75`「Celia regards me over her half-glasses. “Clare. There’s all kinds of love: eros, philia, agape, ludus, all kinds…」 | 引语以引号开头却非完整发言（丢一个词） | 提示 |

**报数（四组）**

- **逐字**：4 块 / 4 段引语在 `text/ch26_celia_says.txt` 全部命中（`segment_miss=0`、`empty_quote=0`）；两处起点截短（原句 2 丢「Clare.」、原句 3 丢 Ingrid 一句）→ **逐字 2 提示，0 阻断**
- **对应**：4 块逐块过 R4，都答「这段中文在讲这句引语」（详见下节）→ **对应 0 堵塞**
- **形态**：H1 `26. Celia Says` ✓；导航 5 项 ✓；子项 4 项齐 ✓；4 块（较 `block_target` 上限 3 多 1，`block_count` 未判红）→ **形态 0 缺陷**
- **断言**：md 事实性断言全部可核（见 3-diff 第二节逐条出处），身高那句确为 Celia 自嘲（`:139`）→ **断言 0 编造**

## R4 逐块对应（人判）

| 块 | 引语 | 主语 / 宾语 / 归属核查 | 结论 |
|---|---|---|---|
| 原句 1 | `:23` Heaven on Seven 与过期珠链 | 交代地点的是 Clare（`Clare:` 标签，md 未引标签，不影响）；「她」＝Clare。受事是餐厅布景。无 by/to/from 歧义 | 对应，密度足（旧身份+残留装饰推出「喜庆是二手的」） |
| 原句 2 | `:75` eros/philia/agape/ludus | 说话人 Celia ✓；「you love her」的 her＝Beck ✓；md「逼她承认」的她＝Clare ✓。方向正确 | 对应；唯起点漏呼语 |
| 原句 3 | `:102` wayward / oughted | 全部第一人称＝Clare ✓；「她想要的方式」的她＝Celia ✓；`oughted` 解释为「把 ought 当动词」✓ | 对应；正文外的主语无混淆 |
| 原句 4 | `:221` 街上分开 / 不回头 | 看的人＝Clare，被看＝Celia ✓；`marching`（大步）与 `halting gait`（一顿一顿）并置未被写成矛盾，md 明确解成「走得不快却一次没转过来」✓ | 对应，收尾落点准确 |

## 已核实为正确（防下一轮误修）

| 看着可疑的写法 | 原文 | 核实结果 |
|---|---|---|
| 「又拿种族、身高、性向一一试过」（像是把身高硬塞给 Celia） | `:139`「“I’m just trying to figure this out. Maybe if I were taller?”」 | **正确**：紧接「Don't be mean」（Clare 说的）之后，是 Celia 自嘲身高，非 Clare。别改成 Clare 问 |
| 「Celia 损 Beck 白得不能再白」 | `:131`「“She’s the whitest possible Black person. She’s off-white. One drop.”」 | 正确；`One drop`＝「一滴血」旧法，属 Celia 的刻薄，不是叙述者立场 |
| 「黄铜大理石大堂」「异常热的四月阳光」 | `:208`「the cool brass and marble lobby where we pause before stepping out into the abnormally hot April sun」 | 正确 |
| 「满桌辣酱」 | `:23`「There are so many kinds of hot sauce on the table there’s hardly room for place mats.」 | 正确 |
| 「她争的其实是 Clare 的注意力」（导航的解读） | `:93` 的追问 + `:213` 的让位 | 属合理释义，不算编 |
| 「Clare 只能承认自己爱她，却不是她要的那种爱」 | `:97`「I do love you. But not the way you want to be loved.」 | 语义正确（转述而非引语），故 L1 只到提示 |
