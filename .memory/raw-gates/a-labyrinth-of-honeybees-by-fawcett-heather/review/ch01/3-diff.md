# ch01 The Royal Inquisitor — R3 对账（素读 ↔ md）

素读件：`review/ch01/1-suread.json`（8 条，锚点经 `/tmp/t3_validate.py` 复核，异常 0）
被查件：`notes/books/short-story-anthologies/a-labyrinth-of-honeybees-by-fawcett-heather/ch01 the royal inquisitor.md`
原文：`text/ch01_the_royal_inquisitor.txt`（下称 ch01:NN = 段落号）

## 一、编（md 有、原文无）

### 编-1（阻断候选）md:10 导航「两名税吏**溺死**蓝河」
- md 侧：「调查两名税吏溺死蓝河一案」（`ch01 the royal inquisitor.md:10`）
- 原文侧：ch01:40 `“Their bodies were found in the Blue River.”`；ch01:41 `The Blue River flows from the Errant Falls, which are located behind the Goddess’s gardens.`；ch01:42 `“I didn’t see them leave,” I said. “If they fell, I had no part in it. Nor did anyone here.”`
- 取证（零命中须附命令）：
  ```
  $ /usr/bin/grep -rn -iE "drown" text/ch01_the_royal_inquisitor.txt text/ch02_the_errant_falls.txt text/ch03_the_campfire.txt text/ch04_the_balcony.txt text/ch06_farewell.txt
  （无输出，rc=1）
  $ /usr/bin/grep -rn -iE "drown" text/ | head
  text/ch05_the_attack_at_the_falls.txt:203: … the Goddess, drowning Her gardens in shadow …   ← 仅比喻用法，与税吏死因无关
  ```
- 判定：原文只说**尸体在蓝河被发现**，且叙述者自己用的是条件句「If they **fell**」；ch02 的版本是「the tax collectors had wandered off the edge inadvertently」。md 把死因写成「溺死」，是原文没有的机制。

## 二、漏（素读有、md 无）

### 漏-1（提示）开篇：鬼魂**先于**审问官到达，叙述者喝止它们并称此地为圣地
- 素读侧（1-suread.json 第 1 条，ch01:0 段区间 135–199）：`“No farther, please,” I told them. “This is consecrated ground.”`
- 原文侧 ch01:1 `The royal inquisitor’s ghosts arrived before he did.`；ch01:2 同上引语；ch01:3 `I tried to shoo the nearest ghost back down the path, but how does one shoo a ghost?`
- md 侧：`## 精读` 4 块均未取此段；`## 本章导航`（:10）只写「带着一大群鬼魂……来到女神的花园」，未写「先到」与「喝止／圣地」。
- 说明：非失实，属覆盖取舍（本章 1409 词，契约给 3–4 块）。但「鬼魂先到」是全篇第一个信息点，建议导航补半句。

### 漏-2（提示）女鬼没有下山，而是走进了环绕神庙的圣迷宫
- 素读侧（1-suread.json 第 2 条，区间 1254–1389）：`But when I saw her next, she had not gone down the mountain, as I had meant, but into the holy maze that enclosed the Goddess’s temple.`
- md 侧：全书 6 章 md 均未出现「迷宫里的女鬼」这一线（ch01 md 内 `迷宫` 零出现）。
- 交叉证据（该线在 ch04 兑现）：`text/ch04_the_balcony.txt:37` `In the first few years after I killed her, she had followed me incessantly, even sleeping next to me in the tent` ＋ `text/ch04_the_balcony.txt:55` `I adjusted my scarf in a fruitless attempt to ward off her cold.`（老女祭司＝被她杀死、会随访的鬼）
- 说明：属伏笔线未记，非事实错。建议在 ch01 导航/总结留一句「一只女鬼进了圣迷宫」。

## 三、错（主语／因果／数字／时序）

### 错-1（提示）md:37 时序倒置：「前一段刚写他身后跟着一大群鬼」
- md 侧：`ch01 the royal inquisitor.md:37`「前一段刚写他身后跟着一大群鬼，这一段却把死者的脸搬到活人脸上」
- 原文侧：原句 2 = ch01:12（幻象）；「一大群鬼」的句子在 ch01:14 `Not to mention his ghosts, so many ghosts! I had never seen such a horde attached to one person.`——**在原句之后**。原句之前只有 ch01:1「鬼魂比审问官先到」。
- 判定：内容判断成立（幻象里的脸＝被他杀的人，ch02:29 `those he had killed` 佐证），仅段落先后说反 → 提示。

### 错-2（提示）md:10 导航「并答应带他去看现场」超前于本章
- md 侧：`ch01 the royal inquisitor.md:10`「并答应带他去看现场」
- 原文侧：ch01:44–46 他要求的是「find a murderer, not a priestess」→ `“I would be happy to help,” I said.`；「带路」发生在 ch02:1 `I led him to the Errant Falls first.`
- 判定：跨章预叙，本章内无「带路」事实 → 提示（若保留，宜写「答应配合调查」）。

## 四、数字与专名核对（本章）

| 项 | md 写 | 原文 | 结论 |
|---|---|---|---|
| 人脸数 | 十二张（:33） | ch01:12 `The faces of a dozen people`（下文 `Two dozen faces. A hundred.`） | ✅ T1 已修，成立 |
| 随行士兵 | 未写 | ch01:19 `one of the three soldiers who accompanied him` | ✅ 无冲突 |
| 天马数 | 未写 | ch01:7 `four of them` | ✅ 无冲突 |
| 案件数 | 两名税吏 | ch01:19 `the deaths of two of his tax collectors` | ✅ |

## 五、已核实为正确（看似可疑、回原文成立）

- md:10「自称 "the groundskeeper"」→ ch01:25 `“The groundskeeper,” I said.` ✅
- md:13 叙事手法引「This was both true and untrue」→ ch01:34 `This was both true and untrue, depending on the circumstances.` ✅（逐字、说话人为叙述者本人）
- md:12 人物弧线「被鬼魂弄得手足无措的守园人」→ ch01:5 `I sounded like an inexperienced tavern maid trying to reason with a drunk. I have never been a particularly authoritative person, despite my position.` ✅
- md:101 总结「审问官带着他杀过的人」→ ch01:12 幻象（`Two dozen faces. A hundred.`）＋ ch02:29 `those he had killed` 明文佐证 ✅
- md:51 块 3「审问官刚问『那你是……』」→ ch01:23 `Then you are . . . ?`（说话人＝审问官）✅
- md:55「It’s embroidered 是现在时，I cursed 是过去时」→ ch01:24 原句 ✅
