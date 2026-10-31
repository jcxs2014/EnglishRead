# R3 对账 · ch02（R1 素读 8 条 vs md 10 块→修复后 11 块）

## 漏（素读有、md 无）

| R1 # | 事实 | 判定 | 处置 |
|---|---|---|---|
| R1#6 | Uncle Jon 被 Mishibizhii 抓辫子拖走、唱死亡之歌死去（全篇两场正面死亡之一，引发 June Bug 一家剪发守丧、"new young warriors" 的成长） | **阻断（漏）** | **已同步修复**：插入新块 原句7（"As his body repeatedly hit the hard ground…a haunting lament and farewell."，37 词，逐字命中 text:187 段），后续块顺延为 8–11；chapter.sh rc=0、gate EXIT=0，commit 6bf07b5b3 |
| R1#4 前半 | 部落挖陷阱、以氏族私藏熏鱼引诱巨兽 | 提示（不修） | md 块6 中文理解已提「跌进为巨兽挖的尖刺陷阱」，陷阱存在成立；熏鱼诱饵属过程细节（text:97 段），块数受约束下取舍合理 |

**其余 R1#1/2/3/5/7/8 全部有块覆盖**（开场故事→块1、巨兽登场→块3、Lu 之死→块4、药袋救援→块5、Mikwam 提议→块8、结尾→块10/11）。

## 编（md 有、原文无）

- 导航「Waazh Bezhig」← text:100 段 "Waazh Bezhig, the name we'd given to our first underground lair" ✓
- 导航「Mikwam…与恶赌徒 Windigo 交配」← text:241 段 "the Evil Gambler or Windigo—welcomes visitors" ✓
- 块2「十五小时的暴雨」← "fifteen-hour rains" ✓；「埃德蒙·菲茨杰拉德号」← "ships like the Edmund Fitzgerald" ✓
- 块7（新）「Waabizii 尖叫示警」← "Then Waabizii screamed" ✓
- 人物弧线「Ziib…『只有一条命』」← "we only get one fucking life" ✓（中文转述）

**编 0 条。**

## 错（两边都有但不一致）

- 施事：块4 "the animal flicked his head and a single sharp horn pierced the soft flesh of Lu's belly"——施动=巨兽/尖角、受事=Lu，md「一根尖角刺穿了 Lu 柔软的腹部」✓
- 施事：块5 "in the hand that had held the pistol was a medicine bag"——手枪变药袋的置换方向（枪→袋），md「原本握着手枪的那只手里…是一只小药袋」✓
- 施事：块7（新）"the giant had a handful of his braid and was dragging Uncle Jon"——施动=巨兽、受事=Uncle Jon，md「揪住 Uncle Jon 的辫子把他当拖拽玩具」✓
- R1#3 说 Lu 死于「尖角刺穿腹部」与 md 块4 一致 ✓
- R1#5 叙述者性别代词：素读 fact 用「他」（守夜者），md 分析层未指认性别、用「叙述者」——不冲突

**错 0 条。**
