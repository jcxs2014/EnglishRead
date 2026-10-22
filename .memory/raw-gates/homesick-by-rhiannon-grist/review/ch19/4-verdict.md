# ch19 4-verdict

- 文件：`ch19 two lambs one mirror.md`
- 结论：**阻断 2 / 提示 4**

## 阻断

### B1 “四个 hadn’t learned”计数错：原文只有 3 个

- 位置：原句3 · 为什么这样写（行50「四个"hadn’t learned"排比」）
- 原文证据：`text/ch19_chapter_19.txt:44`「They hadn’t learned shame. They hadn’t learned that it was better to swallow down your instincts. They hadn’t learned to worry about being rude or unfriendly or unkind.」
  - 取证：`/usr/bin/grep -o 'hadn’t learned' text/ch19_chapter_19.txt | wc -l` → `3`（退出码 0）
  - md 自己紧接的清单也只有三项（羞耻、压抑本能、怕失礼），与“四”自相矛盾。
- 建议改为：「三个"hadn’t learned"排比，把"文明"逐条剥掉：羞耻、压抑本能、怕失礼。」

### B2 人物弧线把她写成“把自己归进凶手那一类”，原文下一句正是明确否认

- 位置：人物弧线（行18「也就第一次把自己归进那一类」）
- 原文证据：`text/ch19_chapter_19.txt:20`「But that’s not what was happening to me, no. Because I was going to the village and I was going to ask after—」
  - 取证：`/usr/bin/grep -n 'that’s not what was happening to me' text/ch19_chapter_19.txt` → `20:But that’s not what was happening to me, no. ...`（退出码 0）
  - 上文 `text:14` 她确实“理解了”凶手，但理解不等于自认；`text:20` 立刻把这种可能推开，随即卡在“她叫什么名字”上。
- 影响：这一句把“共情凶手 → 立刻否认 → 被无名之问截断”的弧度压成单向的“自我归类”，人物位置反了，也削弱下一章她继续自欺的动机。
- 建议改为：「她第一次不带嘲讽地理解"杀过人的人"，可刚想到自己也可能在其中，就立刻否认——"那不是发生在我身上的事，不"；话没说完又卡住：她连邻居的名字都不知道。」

## 提示

1. **“树像卫兵／笼栏”整段意象未落**（行12-20 均无）：`text:11`「The trees in the distance stood at attention, as if they were ancient guards or bars on a cage.」——这是本章唯一的“被围/被看”空间意象，与后面羊羔的凝视同构。建议在叙事手法里补半句（不必单开块）。
2. **“篱笆边”与原文地形不符**（行12）：`text:26` 是「I stepped up to the dry stone wall」，`text:53/59` 是 hedgerow（树篱）；词汇表 `wall` 已正确译“石墙”。建议导航统一为「干砌石墙边」。
3. **“全书第一次”是无法由本章取证的全局断言**（行32）：本章只能证明“她第一次把邻居写成被爱过的人”，全书范围需跨章核对。建议删“全书”，改为「这是她第一次把邻居当成"被爱过的人"」。
4. **“买菜的普通人”属增饰**（行12）：`text:14` 的对照项是「making cups of tea, telling people about the dream you had last night, stepping in dog shit…」——泡茶、讲昨夜的梦、踩狗屎，没有“买菜”。建议改为「另一个里她只是个泡茶、跟人讲昨晚的梦、踩到狗屎的普通人」。

## R4 三问

1. **谁做的**：本章不判定，md 用“两个现实”保持未定（原句1 引用准确）——方向正确；但行18 的“归进那一类”违反了原文的否认（已列 B2）。
2. **关系/谁欠谁**：md 行32 指出她把邻居写成“被任何爱过她、她也爱过的人”记住的人（`text:14`），行18 指出“内疚的对象是个无名的人”（`text:23`）——**关系方向正确，无倒置**：她欠的是那个被她撇下、且她连名字都不知道的人。
3. **数字与死因**：① “四个 hadn’t learned”与实有 3 处不符（B1）；②“两只羊羔”有据（`text:26`「No, two lambs.」）；③ 本章**无死亡**，“snuffed out a life”是假设（`text:14`），md 未写成事实，正确。

## 已核实为正确（下一轮不要改坏）

- 原句1/2/3/4 四段引语逐字连续（`text:14` / `text:26` / `text:44` / `text:59`），无跨段拼接（本章 4 条引语都比 ch17/ch18 干净）。
- 叙事手法点名的四个重复词 unison / identical / in stereo / in perfect synchronicity **全部存在**（`text:29/35/59`），别因为 B1 的“四”字误删。
- “like the world had folded in two”译“像世界被对折了一次”准确；`text:59` 乌鸦段引语完整。
- 词汇表例句均可命中：`scraggly`(11) / `dallied`(62) / `paddock`(53) / `hedgerow`(53) / `bleating`(26) / `plastered`(14) / `crackers`(8)。
- 结尾“我磨蹭够了”（`text:62` I’d dallied long enough）与“咖啡＋培根卷”落点准确。
- H1 形态 `# 19. Chapter Nineteen` 与 ch17/ch18 一致。
