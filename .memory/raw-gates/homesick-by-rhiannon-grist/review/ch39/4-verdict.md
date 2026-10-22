# ch39 4-verdict

- 文件：`ch39 the painted village.md`
- 结论：**0 阻断 / 2 提示**

## 阻断

无。

本md 的引语归属、人物在场关系、地点（Bodach’s Brig → Maggie’s Café → The Curtyard → 壁炉旁的门）均与 `text/ch39_chapter_39.txt` 同向；无凭空数字、年龄、日期、死因；未把"装饰村子的人"指派给任何具体角色（原文也没说），没有编施事。

## 提示

1. **原句4 读者视角提示（第 62 行）｜漏掉"谁不在场"这条线索（提示）**
   证据：`text/ch39_chapter_39.txt:41`「The only faces I couldn’t see were Rowan’s—I imagined he was up among the trees, sat among the saplings, watching the clouds come over the glen—and the old man’s.」；全 md 无 `Rowan` 字样（`/usr/bin/grep -n "Rowan" "ch39 the painted village.md"` → 无输出、`rc=1`）。
   建议在该项后补一句：「而她唯独找不到 Rowan 与'老先生'的脸——她替 Rowan 编了个在树苗间看云的位置。」（ch41 的"浴室里的 Rowan"正是靠这条缺席铺垫）

2. **全章无落点｜"狗女"这个绰号被整章丢掉（提示）**
   证据：`text/ch39_chapter_39.txt:44`「“Look. The dog woman’s arrived,” said the boy from earlier.」+ `:50`「“Shut up.” Dave glowered in the boy’s direction.」；md 内 `dog` 查无（`/usr/bin/grep -n -i "dog" "ch39 the painted village.md"` → 无输出、`rc=1`）。
   建议在导航或原句4 的读者提示里补一句：「先前那个少年照旧叫她'狗女'（承接她在 ch34 当街学狗叫那幕），但这次没人笑，Dave 反而喝止了他——村民的敌意换成了同一种恐惧。」这不是阻断：不补也不影响本章因果，但补上能把 ch34 的羞辱与本章的"共同体恐惧"接起来。

## R4 三问

1. **谁做的**：① 把村子"装成样板村"的施事原文**没有交代**（`text/ch39_chapter_39.txt:8-20` 全是无人称的装饰描写），md 也没有指派——这一点是对的，不要在后一轮"补"成邻居或仙族；② 打吊篮的是 Maggie 本人（`:11`）；③ 在酒馆里喊"狗女"的是"先前那个少年"，喝止他的是 Dave（`:44,50`）；④ 指路并转告"她说了要留意你"的是 Viv（`:59,65`）；⑤ 门是原文新出现的（`:62`「I’d never seen a door there before」），不是她走错。
2. **什么关系 / 谁欠谁**：本章没有债务/亏欠关系，只有**权力与恐惧的再分配**：村民从"看她的笑话"（少年喊狗女）转为"集体噤声"，Dave 的喝止说明村内秩序已由恐惧接管；Viv 服从的是"她"（老妇人）的指令（`:65`），即老妇人对村子有调度权，而 Tamsin 是被"预约"的客人——不是她找上门，是对方早留了眼线。
3. **数字与死因**：① 吊篮"七个"——`:11`「one of the seven hanging baskets」；② 无年龄、无金额、无日期；③ **本章无人死亡、无尸体、无伤害事件**（她的手伤是 ch38 留下的旧伤，`:26,52` 只以"好手/伤手"出现）；md 未写任何死因，正确。

## 已核实为正确（下一轮不要改坏）

① "没有泥 / 草一样齐 / 鹅卵石干净"三短句逐字对应 `:8`，未被改写成"破败"；② 花香是"呛"而不是"好闻"（`caught in the back of my throat`，`:8`），md 第 30 行的分析方向正确；③ 水仙是"白得近乎透明的花瓣 + 金黄喇叭口"，且是**被打落在地**的那一篮（`:26`），不是她摘的；④ `Poor wee thing` 的"wee"被解释为苏格兰口语的"小"，正确；⑤ Viv 那句警告是转述（"She said…"），不是 Viv 自己的判断，md 未写成 Viv 的预言；⑥ 门的位置是"壁炉旁"（`:62`），不是"吧台后"或"地下室"。
