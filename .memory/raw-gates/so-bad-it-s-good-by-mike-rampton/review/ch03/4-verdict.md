# ch03 How to Tell a Terrible Joke Brilliantly 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，9 块；`verify_fragments_indep` 0 MISS；字符数 3,204 与概览一致。

## 逐块对应（9 块）

| 块 | 落位 | 中文是否讲这句引语 | 关键词 | 施事 | 档位 |
|---|---|---|---|---|---|
| 1 | :15 | 是：文本 vs 表演 | telling / art ✅ | 说话人＝作者 ✅ | 通过 |
| 2 | :22 前三句 | 是：现象—后果—定性为偷窃 | botch / mangled / theft ✅ | 讲砸者＝被抱怨的讲者 ✅ | 通过 |
| 3 | :22 后半 | 是：不要第一次就对着人群试讲 | crowd / no good ✅ | 主语＝你（读者）✅ | 通过 |
| 4 | :30 | 是：荒唐前提要当真，熊不走进酒吧 | inherently / suspend / disbelief ✅ | 搁置怀疑者＝讲者与听者双方 ✅ | 通过 |
| 5 | :38 前半 | 是：别像被枪逼着赶 | rattle through / digested ✅ | 跟不上的是听众 ✅ | 通过 |
| 6 | :38 后半 | 是：铺垫越厚回报越大，落空也越大 | buildup / payoff ✅ | 作者自述“unique to jokes” ✅ | 通过 |
| 7 | :46 | 是：脏话有效但要省着用 | sparely / emphasis ✅ | 使用者＝讲者 ✅ | 通过 |
| 8 | :54 | 是：加嗓音、音效、长名字 | pointlessly / entirety ✅ | 执行者＝讲者 ✅ | 通过 |
| 9 | :62 | 是：讲砸本身可以最好笑 | failing / joyous ✅ | 笑场的是孩子 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 正文六节、每节一段 | text 六个 H2 节标题（:19/:27/:35/:43/:51/:59） | 正确 | 通过 |
| 「鲸鱼/鲨鱼」类比喻确为 Jaws | :46 “You barely see the shark through most of Jaws.” | 正确 | 通过 |
| 「highlighter」句是“不能整本书都用高亮笔” | :46 | 正确 | 通过 |
| 章末“joyous”句是全章最后一段 | :62 为文件末段 | 正确 | 通过 |

## 已核实为正确

- 原句 6 的「the bigger the buildup, the more satisfying the total lack of payoff」：`:38` 原文 “But also, uniquely to jokes, the bigger the buildup, the more satisfying the total lack of payoff.” —— md 引语与释义都保留了“落空也满足”这一层，未简化成“铺垫越长越好”。
- 原句 4 的“bears don't walk into bars”不是 md 编造：`:30` 原文。
- 「六节互相拉扯」的评述（可质疑处 1）：`:30` 要求“当真”、`:54` 要求“加料拖长”，两者确有张力，评述有原文依据，非臆断。

## 结论

阻断 0 / 提示 0 / 假红 0。本章无需改动；`chapter.sh` rc=0（复跑确认）。
