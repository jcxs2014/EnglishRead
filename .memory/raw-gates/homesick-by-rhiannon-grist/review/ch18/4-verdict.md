# ch18 4-verdict

- 文件：`ch18 the begonias and the unknocked door.md`
- 结论：**阻断 1 / 提示 4**

## 阻断

### B1 开篇“秋海棠＝她没事的证据”整段缺失，分析却虚指“那句”，形成悬空引用

- 位置：原句1 · 为什么这样写（行30「才有后面那句"这总该算她没事的证据吧"」）；全章导航（行12）与标题（`The Begonias…`）也无所指
- 原文证据：`text/ch18_chapter_18.txt:5`
  - 「A planter full of tumbling begonias had been added to my neighbour’s window sill. Surely that was enough evidence she was fine.」
  - 紧接 `text:8`：「Unless she put it up yesterday after I left for the pub.」——证据当场被自己推翻，这是本章第一拍（自我安慰→立刻自拆）。
  - 取证：`/usr/bin/grep -n 'begonias' text/ch18_chapter_18.txt` → 只有 `5:` 一处；`/usr/bin/grep -n 'begonias\|秋海棠' "ch18 the begonias and the unknocked door.md"` → 只有 `75:`（词汇表例句）。`/usr/bin/grep -n '那句' …md` → `30:`（正文找不到被指代的那句）。
- 影响：读者读完精读仍不知道“秋海棠”为何是章名、也不知道她凭什么认为邻居没事；行30 的“那句”在 md 内不存在，属**分析指向空处**，开篇因果链（证据→自拆→才去敲门）因此断开。
- 建议改为（在原句1 分析里补一句，并把虚指换成实指）：「她先给自己找了个证据：邻居窗台多了盆垂枝秋海棠，'这总该说明她没事'——随即又被自己推翻：'除非是她昨天我去酒馆之后才摆上去的。'一个连站都站不舒服的人，最容易抓住任何能让自己好过的解释。」

## 提示

1. **原句3 跨自然段拼接**（行44）：`My neighbour was just out for breakfast…` 在 `text:119`，`I would go into the village…` 在 `text:122`，中间隔着 `text:120-121` 空行。建议加「……」或拆两句引（ch17 原句4 同型，属系统性问题，建议统一处理）。
2. **“我这种人”非原文**（行18）：原文的自我指控是 `text:38`「Even though you knew what that felt like.」与 `text:44`「Hypocrite.」，没有“我这种人”。建议改为「也第一次在心里骂自己 Hypocrite——'你明明知道被撇下是什么滋味'」。
3. **`early-summer-late-spring` 译偏**（行26「初夏未满、暮春已过的潮气」）：“未满/已过”把季节说成两头都不在；原意是暮春与初夏之交。建议改为「暮春将尽、初夏未至的那种潮气」（或「晚春初夏之交的湿冷」）。
4. **“一具还没被证实的尸体”措辞过头**（行14）：原文始终是假设句（`text:83`「Or she could be lying…」／`text:119`「…than lying dead in her basement.」），没有任何尸体出场。建议改为「一个还没被证实的死亡画面」。

## R4 三问

1. **谁做的**：本章不确认任何事。md 标题与导航守住“不行动”（行12「这是她给自己的第四种不行动」），**与原文一致**；唯一措辞风险是行14 的“尸体”，按提示4 改即可，不阻断。
2. **关系/谁欠谁**：md 行18 把“昨晚没邀邻居”与“此刻的愧疚”接上，方向正确（她自觉欠、自觉 hypocrite，`text:29-44`）；**未出现倒置**。
3. **数字与死因**：`text:17` 上午十一点 ✓（md 行12）；`text:80` 一小时 ✓（行97“一个小时空窗”）；`text:50/83/95` “with an axe wound in her face” 恰 3 次 ✓（md 行20 记“三次”，经 `/usr/bin/grep -c` 核实为 3）。**死因未定**：斧伤是她的想象，md 未写死，正确。

## 已核实为正确（下一轮不要改坏）

- 原句1 逐字（`text:5`），且未把 `I was minging. Bogging.` 混进引语——裁剪干净。
- 原句2 逐字（`text:77`），`nothing to wait for` 译“再没有什么可等”准确。
- “with an axe wound in her face 出现三次”这个计数是真的，别当成夸大改掉。
- 词汇表 `minging` 标注“苏格兰/北英口语”与本书 Carlinsrest 设定相符；`occluded` / `restorative` / `rummaging` 例句均可在 `text/` 命中。
- 导航“把敲门、破门、报警三条路一条条想完”对应 `text:23-26`（break down the door / smash in a window / could try knocking first）与 `text:86`（call the police）。
- H1 形态 `# 18. Chapter Eighteen` 与 ch17 一致。
