# ch56 4-verdict

- 文件：`ch56 blood bath.md`
- 结论：**2 阻断 / 3 提示**

## 阻断

### 1. “第 1 章第一封信是账单”——ch1 没有信、没有账单

- 位置：块3「读者视角提示」“对照**第 1 章**她收到的第一封信是**账单**”。
- 原文证据：`text/ch01_chapter_1.txt` 全章无 letter/bill/invoice/post/mail（`/usr/bin/grep -n "bill\|letter\|invoice" text/ch01_chapter_1.txt` 无输出；`post|mail|envelope` 亦无）。ch1 里她拿到的是购房文件与钥匙（`:17` “I dug out my copy of the paperwork”）。
- 建议改为：「这是全书第一次有人给她留便条——对照第 1 章她手里只有一叠没细看的购房文件」。

### 2. “第 8 章五金店里他当众羞辱她”——ch8 是 Rowan 的店，Fergus 的店戏在 ch33

- 位置：块6「读者视角提示」“对照**第 8 章五金店**里他当众羞辱她的那段，同一个词（prick）在这里被他自己捡起来了”。
- 原文证据：ch8 五金店是 Rowan 初登场、态度友善（`text/ch08_chapter_8.txt:31` “a man straightened up from behind a counter”、`:44` 她预期“tourist-tired local”的 sneer 并未出现）；ch8 无 Fergus（`/usr/bin/grep -n "Fergus" text/ch08_chapter_8.txt` 无输出）。Fergus 在五金店封箱（工业钉枪）、讲 Fairy Mirror 故事在 ch33：`text/ch33_chapter_33.txt:8` 「Fergus looked up at the ring of the electronic doorbell… industrial stapler the size of his head」；且 `:118` 明写店里没有别人，谈不上“当众”。
- 建议改为：「对照第 33 章五金店里他用工业钉枪封箱、拿‘Fairy Mirror’吓她的那段——同一个词（prick）在这里被他自己捡起来了」。

## 提示

1. 块2 “folks 是本地人的说法/第一次使用这里的口音”：folks 偏美式，不是苏格兰本地用语，“第一次”亦无据；建议只保留“她开始用更随口的说法”。
2. 块1 “全书唯一一次用现在时开场/格言体”：ch1 开篇同样是现在时格言式（`text/ch01_chapter_1.txt:5`），建议改为“少见的现在时开场”。
3. 块3 引语把 “Next to it was a note:” 与便条正文并为一句，原文便条另起一段。

## R4 三问

1. **谁做的**：**Fergus** 来探病、送仙人掌、道歉、往她手机里塞提醒（`text/ch56_chapter_56.txt:35-65`、`:224`）；**Rowan** 开车带 Fergus 来查看、冲进 1b、在地下室找到她并让急救队去找“邻居”（`:89`、`:110`、`:134`）；医院救治、验血（`:134`）。Tamsin 对针眼撒谎说是地板钉（`:158`）。
2. **什么关系 / 谁欠谁**：Fergus 与 Rowan 同住、关系亲密（`text/ch57_chapter_57.txt:146` “Rowan and Fergus’ place”），是她的邻居；Fergus 欠她一个道歉——他因 Rowan 总“捡流浪者”而把气撒在她身上（`:203`），本章当面道了（`:212`），她接受（`:200` “I don’t mind.”）。邻居（1a 那半）不欠她：房塌了，她反而可能拿到赔偿（Aunt Sheila 是前律师，`:254`）。
3. **数字与死因**：住院**第三天** Fergus 来访（`:26`）；塌的是 **1a**，**1b** 几乎无损（`:104`）；针眼一排、红线不见（`:146`）；无年龄、金额（赔偿未定）；**无死亡**——她被从地下室救出，血全是她自己的（`:140`）。

## 已核实为正确（下一轮不要改坏）

① 塌的是 **1a**（邻居那半），她的 **1b** 没塌（`:104`），未写反；② “Blood Bath” 来历正确：血全是她的，医院验血排除她杀人（`:134`、`:140`）；③ 针眼与“红线不见”对应 ch55 的缝合（`:146`），未被写成“伤口感染”；④ Fergus 的道歉理由正确：不是“因为她是城里人”，而是他把对 Rowan 的气撒在她身上（`:203`、`:212`）；⑤ 仙人掌、黄丝带、卡片 “A prickly bastard from a prickly bastard, F x” 逐字无误（`:59-62`）；⑥ 结尾 “DRINK WATER.” 提醒与“她喝了”顺序正确（`:269-272`）；⑦ 章号 56、第一人称 Tamsin 正确。
