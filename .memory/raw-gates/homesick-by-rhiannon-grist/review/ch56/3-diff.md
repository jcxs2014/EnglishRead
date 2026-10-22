# ch56 3-diff（素读事实 → md 对账）

- 文件：`ch56 blood bath.md`
- 素读：`production/ch56-facts-deep.txt`，suread 8/8 ✅

| # | 素读事实（先读 text 写下） | md 位置 | 判定 |
|---|---|---|---|
| 1 | 她在医院醒来，浑身伤；以为自己死了、这里是“灵魂医院” | 块2（原句2） | 对应 |
| 2 | 住院第三天醒来，Fergus 坐床边翻古董目录 | 导航“三天后”＋块2 后 | 对应 |
| 3 | 床头系黄丝带的小仙人掌，卡片“A prickly bastard…”；因病房禁花 | 块3（原句3） | 对应 |
| 4 | 塌的是 1a；1b 几乎没事，空得只剩羊皮地毯 | 导航＋块4（原句4） | 对应 |
| 5 | 1a 只剩瓦砾；Rowan 开车来查看、冲进 1b、在地下室找到她 | 块4 | 对应 |
| 6 | 血全是她自己的，外号“Blood Bath”；验血排除杀人 | 导航未提，块4 后 | 对应（压缩） |
| 7 | 手臂一排针眼、红线不见；她撒谎说是地板钉 | 块5（原句5） | 对应 |
| 8 | Fergus 道歉：因 Rowan 总捡流浪者而把气撒在她身上，承认看不起来自城市的人但不恨她 | 块6（原句6） | 对应（章号见阻断 2） |

## 提示与阻断定位

- **阻断 1**：块3「读者视角提示」称“对照**第 1 章**她收到的第一封信是**账单**”。ch1 全章无 letter/bill/invoice/post/mail（`/usr/bin/grep -n "bill\|letter\|invoice" text/ch01_chapter_1.txt` 无输出；`post\|mail\|envelope` 亦无），不存在“第一封信是账单”。
- **阻断 2**：块6「读者视角提示」称“对照**第 8 章五金店**里他当众羞辱她的那段”。ch8 的五金店是 **Rowan** 的店、初次见面且友善（`text/ch08_chapter_8.txt:31-44`，`/usr/bin/grep -n "Fergus" text/ch08_chapter_8.txt` 无输出）；Fergus 在五金店封箱、讲 Fairy Mirror 的戏在 **ch33**（`text/ch33_chapter_33.txt:8`、`:70` 起），且当时店里无别的顾客，不是“当众”。
- **提示 1**：块2「读者视角提示」“‘folks’……本地人的说法……第一次自然地使用这里的口音”。folks 更偏美式，不是苏格兰本地用语；“第一次”亦无据。
- **提示 2**：块1 称“全书唯一一次用现在时开场，也是唯一一次用格言体”；ch1 开篇同样是现在时格言式（`text/ch01_chapter_1.txt:5` “The symmetry should have tipped me off. Two sets of windows…”），此“唯一”不成立。
- **提示 3**：块3 引语把 “Next to it was a note:” 与便条正文压进同一句，原文便条另起一段。

判定汇总：**阻断 2 / 提示 3**
