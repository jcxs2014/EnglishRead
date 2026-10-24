# ch02 The Errant Falls — R5 判定表

路径：R1（子代理，仅读 text/ch02）→ `/tmp/t3_validate.py` 锚点复核 → R2 `chapter.sh --json` → R3（`3-diff.md`）→ R4 → 本表。
md：`notes/books/short-story-anthologies/a-labyrinth-of-honeybees-by-fawcett-heather/ch02 the errant falls.md`

## 一、四组报数

| 组 | 数 | 结果 |
|---|---|---|
| 逐字 | 引语块 8 / 分段 8 / 查无 0 | ✅ 含 `. . .` 分段独立取证 |
| 对应 | 导航 4 项 + 总结 1 项 + 8 块 ×5 子项 = 45 项 | 43 项成立，2 项措辞不准（错-1、错-2） |
| 形态 | H1 `02. The Errant Falls` ✅ / 导航 4 项 ✅ / 块数 8（契约本章区间 5–8）✅ / 引语 >100 词 0 ✅ | ✅（⑪ lane 曾提示 8 块偏离本书众数 3，属长篇正常） |
| 断言 | R3 三单：编 0、漏 3、错 2 | 阻断 0 / 提示 5 |

R2（`review/ch02/2-machine.json`，rc=0）：`verdict: ok`，`quotes 8 / blocks 8`，`segment_miss 0`，`struct_bad 0`，`empty_quote 0`，`keyword_bad 0`，`cjk_low 0`，`template 0`，`hole 0`，`words 2699`。

## 二、R4 逐块核对

| 块 | 引语出处 | ①主语 | ②受事 | ③谁的/谁欠谁 | 结论 |
|---|---|---|---|---|---|
| 原句 1 | ch02:2 | The maze is not ... but composed of ... | 迷宫自身 | paths **we** maintain（守园人的路） | ✅ |
| 原句 2 | ch02:11 | You（泛指）couldn't see；the Falls created mist | 观者（她与他） | 失足说辞是**她**曾打算提的 | ✅ |
| 原句 3 | ch02:14 | **his people**（征服者）abandon names；peasants keep theirs | 「我」没问他的名字 | 名字属于审问官 | ✅ |
| 原句 4 | ch02:16 | ghosts follow **their murderers**；跟着「我」的鬼只有一个 | 「我」＝凶手之一（自我指认） | 那个鬼是「我」的 | ✅ |
| 原句 5 | ch02:34 | He laughed；**I** forgot who he was；**he** asked | 双方互为主体 | 问句属审问官 | ✅ |
| 原句 6 | ch02:53 | **I** said nothing；his eyes bore into me | 「我」被审视 | 「围巾」是她的（my scarf） | ✅ |
| 原句 7 | ch02:61 | **I** have no mixed feelings；I worshipped home | 「我」自己 | home＝这些园子溪流 | ✅ |
| 原句 8 | ch02:71 | **He** had before him ...（她在揣度他的目光） | 她与森林神祭司 | 帝国分开「这样的人」 | ✅（md:121 的「视角换成审问官」措辞不准 → 错-1） |

无施事反转、无说话人错配；引语与中文逐块对得上。

## 三、判定

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| md 全篇未记 Harper（真守园人、不能说话） | ch02:35、ch02:41 | 覆盖取舍（ch03 承接） | 提示 |
| md 全篇未记「尸体折断＋口袋苹果花」 | ch02:18 | 关键物证未记 | 提示 |
| md 全篇未记 Threefold God / 八十三位神 | ch02:44 | 世界设定未记（ch06 兑现） | 提示 |
| md:121「视角的主人在这里换成了审问官」 | ch02:71 第一人称，她在想象其目光 | 叙述学误述 | 提示 |
| md:79「接下来就是继承人的失踪」 | ch02:34→:50，其间尚有三段落 | 衔接说快了 | 提示 |

**本章阻断 0 条。**

## 四、已核实为正确

| 断言 | 证据 | 结论 |
|---|---|---|
| 「我崇拜家甚于崇拜女神」（md:103） | ch02:61 `I have always worshipped home more than I worship the Goddess` | ✅ |
| 她**未选**当祭司、境遇所迫（md:107） | ch02:61 `I didn’t choose to become Her priestess ... circumstances essentially forced the job upon me` | ✅ |
| 「交出名字是虔诚」（md:51） | ch02:14 | ✅ |
| 迷雾「像船帆」与「急着离开的水」同一意象（md:41） | ch02:11 `like sails` ＋ ch02:23 `eager to leave the Goddess’s lands behind` | ✅ |
| 审问官「可以被打断」（md:83） | ch02:6 `his mask of politeness slipping a little`；ch02:28 `an unexpectedly warm sound` | ✅ |
| 森林神祭司「站到征服者一边」（md:12） | ch02:68 `I required a guide ... He led me to the trailhead`；ch02:66 她指责其违约 | ✅ |
| 苹果花/折断等物证未写入 md 不等于写错 | —— | ✅ 无误述 |

## 五、同会话自检已知盲区

- 与 ch01 同一会话产出，非异会话独立复核。
- 8 块为本书最长章之一，语义二审仅由我逐块比对；「哪些段落未被选入」的判断属编辑取舍，本表只报不判红。
