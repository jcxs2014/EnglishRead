# ch06 a store bought cake —— R4 逐块追问 + R5 定档

## R4：固定追问（主语是谁／受事是谁／归属方向）
| 原句 | 主语 | 受事 | 归属方向 by/to/from/of | 判定 |
|---|---|---|---|---|
| 1 | Lucy | 她自己（那笔订单） | `at the top of what increasingly feels like Rapunzel’s tower` | 通过 |
| 2 | Lucy | 松饼／她自己的手 | `on Saskia’s door` | 通过 |
| 3 | Saskia | 她自己的肌肉／时间 | `this afternoon` | 通过 |
| 4 | Lucy | 她自己（那个问题） | `about the evils of man` | 通过 |
| 5 | Lucy | 她自己（身世） | `growing up` | 通过 |
| 6 | Lucy（被关的那个） | 她自己 | `out of the house after middle school` | 通过 |
| 7 | 祖父 | Lucy 的家门 | `on all the doors` | 通过 |
| 8 | Saskia／Lucy | Lucy／Saskia | `since her mom left`／`around Saskia’s waist` | 通过 |
| 9 | Saskia | 气球与超市蛋糕 | `with a handful of balloons and a store-bought birthday cake` | 通过 |

## R5：定档（阻断／提示／假红／跳过）
| # | 观察 | 档位 | 说明 |
|---|---|---|---|
| 1 | 引语逐字 9/9、词表 22/22 | — | R2 与 `check_vocab` 均过；修后 `chapter.sh` rc=0 |
| 2 | 形态：H1 06. Chapter 6 / 导航 5 项 / 块数 9 | — | 落 ⑱ 3–8 上限（9 为全书块数最多的一章，格式提示型 ⚠️） |
| 3 | 原句 6 引语从句子中间起头 | **提示 1（已修）** | 已恢复 `I… wasn’t allowed…` 原句；原著自带 `…` 不影响块序判定 |
| 4 | 叙事手法第三层声音「楼上的脚步」 | **提示 2（已修）** | 原文无据，改为 `:52` 四点整的敲门声 |
| 5 | 「不像只在需要被救时才敲门的人」 | 已核实为正确 | `text/ch06_chapter_6.txt:7` |
| 6 | 「Was that weird?」「you don’t have to wait for anything」「Yes, ma’am」 | 已核实为正确 | `:118`／`:178`／`:202` |
| 7 | 生日在十月与「store-bought cake」 | 已核实为正确 | `:166`／`:175` |

## 计数
- 阻断 **0** ／ 提示 **2（均已修）** ／ 假红 **0** ／ 跳过 **0**
- 逐字：引语 9/9、词表 22/22｜对应：0｜形态：合规｜断言：0 条落空

## 已核实为正确
1. 未再见 + 不肯只在求救时敲门——`text/ch06_chapter_6.txt:7`。
2. `In two steps, Saskia is across the room`——`:112`（与 `tentatively returns the hug` 同段）。
3. 「第二个边桌也没留给 Lucy 单独装」——`:148` `although Saskia could easily leave the second one for Lucy to do alone`。
4. 「Was that weird?」——`:118`；「I’m weird, you’re weird, the world is weird」——`:124`。
5. 十月生日 + 商店蛋糕——`:166` `There’s just something about store-bought cake.`／`:175` `It’s in October`。
6. `“Yes, ma’am,” she murmurs as Saskia charges down the spiral staircase.`——`:202`。
7. 章末大哭——`:229` `She bursts into tears.`

结论：**本章 2 条提示当场修正**，修后 `chapter.sh` rc=0、`structure.py order` 29 md / 166 块 · 0 缺陷。
