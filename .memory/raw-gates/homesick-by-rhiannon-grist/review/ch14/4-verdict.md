# ch14 4-verdict

**结论**：本章精读整体与原文对得上（8 条素读事实 7 条有落点，"悬着的邻居""镜向房子""结尾问句"等关键落点都在），但**一句话概括把古董店里那场难堪的施事方向写反了**——原文是"她自己在店里失礼被抓包"，md 写成"Fergus 羞辱过她"。此外有 4 处细节/计数措辞无据或偏移，属提示级。

## 阻断

### B1 · L12（一句话概括）"古董店里羞辱过她的 Fergus"——施事反

- 位置：`ch14 the curtyard and the hollow hill.md:12`
- 原文证据：
  - `text/ch14_chapter_14.txt:65`「Maybe his boyfriend hadn’t shared my faux pas from the antiques shop yet.」——她担心的是**自己**的 faux pas（失礼）被转述。
  - `text/ch14_chapter_14.txt:59`「He glanced up at me coolly, did a doubletake then mouthed a swearword.」——Fergus 当场只是冷淡、低声骂了一句，没有羞辱她。
  - 事发章 `text/ch12_chapter_12.txt:134`「The sullen-faced man was at my shoulder, looking at my screen. My cheeks throbbed with embarrassment.」——难堪的来源是他**撞见她在网上比价他的货**，脸红的是她。
- 建议改为：「坐下来才发现 Rowan 的伴侣正是古董店里撞见她上网比价、臊得她脸红的 Fergus」

## 提示

1. **L12/L16 vs 素读事实 3（漏）**：招牌「The C_urtyard」缺掉的 "o" 被挂在打烊铃旁、便条写 £10 三次，且 Rowan 说的 "Curtyard" 是内部玩笑（`text/ch14_chapter_14.txt:26`、`:35`、`:29`「So that’s what Rowan had said: ‘Curtyard’.」、`:32`「An inside joke of which I was now a part.」）。md 只在词汇表例句里带出招牌与 £10，正文没写"缺 o / 内部玩笑 / 她如今也成了玩笑的一部分"。建议在"精读"里补一句，或在"一句话概括"里点出招牌梗。
2. **L16「"镜子"母题第三次出现」**：计数无据。全书至 ch14 出现 mirror 的章为 ch02(1)、ch03(2)、ch11(2)、ch12(1)、ch14(2)，本章至少是第五个带镜子的章。建议改为"镜子母题再一次出现，这次照的不是她的脸，是她的行为"。
3. **L72「"tacky"这种词在她心里出现过不止一次（古董店、花盆）」**：跨章例证无据。`grep -c -i tacky ch*.txt` 显示 ch02 那处是 "tacky to the touch"（发黏，另一义），ch18/ch24 在本章之后；ch12（古董店）与"花盆"均无此词。建议删去括号例证，或改为"她评价别人的词，最后都会回到自己身上"。
4. **L90「同一句话在第三章的梦里由老板问过」**："老板"不准。`text/ch03_chapter_3.txt:143`「The interview table filled it save for space for one chair on my side and one chair on the other.」，`:179`「“Do you think you’re a good person?” she asked.」——那是**面试官**（梦里坐在面试桌对面的人）。建议改为"由面试官问过"。

## R4 三问

**① 谁做的**
- 编故事的是 **Fergus**，且他自己拆穿（`text/ch14_chapter_14.txt:173`「“Nope.” Fergus’s face split into a grin. “I had you there, didn’t I?”」；`:179` Rowan「He’s telling you stories.」）。md 未把"编造者=Fergus"写错。
- 主动进酒馆的是**女邻居**，不是 Tamsin 邀来的；Tamsin 反而在躲（`:206`「I quickly turned away and tried not to make eye contact.」）。
- 把 Tamsin 一个人留在卡座的是 **Fergus 与 Rowan**（`:272`–`:281` 借口去拿酒）。
- 本章的"问句"没有施事，文本只给触觉（`:287`「as if right in my ear, real enough to feel cold breath on my cheek」）；md 也守住了"来源不明"。

**② 什么关系 / 谁欠谁**
- **Fergus = Rowan 的伴侣**，在古董店做事（`:71`「This is my partner, Fergus. He works at the—」、`:74`「The antiques place」）。Tamsin 与 Fergus 的紧张源于**她在他的店里失礼**（比价他的货），不是他欺负她 → 这条正对应上面 B1。
- **Tamsin 欠邻居一次**：昨天早上答应替她捎东西却放鸽子（`:224`「I remembered offering to pick her something up from the village yesterday morning.」、`:230`「I wondered if she knew I’d ditched her.」）。这是她心虚的全部来源。
- **老翁与 Tamsin**：她替他捞回两张五十镑（`:44`），但只在他背后算账（"wondered if they were now being used to get a dog drunk"），并无施恩/索报动作。
- 复制体-本体线：本章只有"镜向的房子"作铺垫（`:113`「We share a chimney, I think, but we have separate front doors.… backwards. Mirrored.」），**未出现**复制体/本体的实体对位；md 也没越界写成已发生。

**③ 数字与死因**
- £10 三次投掷：`text/ch14_chapter_14.txt:35`「a small handwritten note beneath reading: £10 for 3 tosses.」✅
- 两张五十镑：`:44`「the two fifty-pound notes I’d rescued for him earlier」✅
- 时令"五月中旬"：`:5`「The mid-May sky didn’t darken.」✅
- 死因与时间：`:164`「The whole family died of cholera the next summer.」——霍乱、次年夏 ✅（md L16 写"全家死于霍乱"对）
- 门牌 1b/1a：`:104`「Yeah. I’m in 1b. There’s… someone else in 1a.」✅

## 已核实为正确（下一轮不要改坏）

- 原句 1、2：`didn’t darken / became paler / cornflower twilight / silhouettes` 与"两个金发女孩""黄风筝"均在 `text/ch14_chapter_14.txt:5`、`:11`，逐字无误。
- 原句 3 的 `the same glass`、`a slow, careful movement`、`two fifty-pound notes`、`get a dog drunk` 全在 `:44`，且"同一只杯子先喂狗再自己喝"的顺序与原文一致。
- 原句 4「one of the ancestral homes of the Fair Folk… wasn’t from around here… leave the hill be」在 `:164` 逐字无误；"外来人"这一故事前提抓得对。
- 原句 5 的 `half wet`、`a potato sack`、`weird, tacky black trousers` 在 `:215` 逐字无误。
- 原句 6 的 `knew that hover`、`waiting to be noticed`、`the dilemma` 在 `:236` 逐字无误；"她也曾这样悬在同事旁边"确是第一人称自认。
- 原句 7 的 `right in my ear`、`cold breath on my cheek`、`the question again` 在 `:287`、`:290` 无误；"第三章梦里问过"这一跨章指认**章号正确**（只需把"老板"改成"面试官"，见提示 4）。
- L16「Fergus 说完立刻拆穿"我骗到你了"」与 `:173` 一致；L60"不是本地人"这一故事重心的解读与原文相符。
