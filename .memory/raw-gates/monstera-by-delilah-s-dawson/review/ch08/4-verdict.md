# ch08 a good will birthday —— R4 逐块追问 + R5 定档

## R4：固定追问（主语是谁／受事是谁／归属方向）
| 原句 | 主语 | 受事 | 归属方向 by/to/from/of | 判定 |
|---|---|---|---|---|
| 1 | Lucy | 那些旧物／她自己 | `around Goodwill`／`of a sad woman` | 通过 |
| 2 | 祖父 | Lucy 的身体与家门 | `on all the doors`／`her grandfather told her` | 通过 |
| 3 | Lucy | 她自己（欲望） | `at the sound of clanking weights`／`among the greenery` | 通过 |
| 4 | Saskia | Lucy | `to remember what a birthday feels like` | 通过 |
| 5 | Lucy | 她自己（身体） | `underneath the city`／`for being human` | 通过 |
| 6 | Lucy | Saskia（想象） | `below her`／`in her arms` | 通过 |
| 7 | Lucy | 她自己的身体 | `under the elastic of her pajama pants`／`for twenty-four years` | 通过 |
| 8 | Lucy | 她自己的白日梦 | `into her own daydreams`／`under a canopy of glowing green leaves` | 通过 |
| 9 | 房间（一切）／Lucy | 她 | `like a pinata`／`in her room` | 通过 |

## R5：定档（阻断／提示／假红／跳过）
| # | 观察 | 档位 | 说明 |
|---|---|---|---|
| 1 | 引语逐字 9/9、词表 13/13 | — | `chapter.sh` rc=0；`check_vocab` 过；块序 0 缺陷 |
| 2 | R1 第 6 条（数字油画＋找美术课）md 全无 | **提示 1（已修）** | 补原句 5（`:40` 末三句）＋导航补一句 |
| 3 | 导航「叙事手法」把沼泽比喻当引语分析却未引用 | **提示 1 同因（已修）** | 同上：沼泽与 `stamina for being human` 现已入原句 5 |
| 4 | `A tiny explosion.`／`An echo.`／`This is what she would taste like, Lucy thinks.` | 假红（非缺陷） | 各为独立单句段（2–11 词），无法单块、不可跨段拼接；内容由导航、一句话总结与词表 `echo` 承载 |
| 5 | 「不敢开台灯，只用阅读灯」 | 已核实为正确 | `:70` `She doesn’t dare turn on her lamp, but her little booklight offers adequate illumination` |
| 6 | 「她从来不信祖父那套」 | 已核实为正确 | `:10` `Not that Lucy believed him.` |
| 7 | 「一个笼子换另一个自己选的笼子」 | 已核实为正确 | `:46` `she has traded one cage for another. At least this is a cage of her choice.` |
| 8 | 气球、粉色数字 1、像猫一样 | 已核实为正确 | `:31` |
| 9 | 皮纳塔／花床单／嗅手指／羞于念出 Saskia 的名字 | 已核实为正确 | `:88`／`:94` |

## 计数
- 阻断 **0** ／ 提示 **1（已修）** ／ 假红 **3（非缺陷）** ／ 跳过 **0**
- 逐字：引语 9/9、词表 13/13｜对应：0｜形态：块数 9（⑱ 上限 3–8，提示型）｜断言：0 条落空

## 已核实为正确
1. 购物清单四项——`text/ch08_chapter_8.txt:4`。
2. 一条连衣裙+两件无袖衫+一条牛仔裤、蜕皮的蛇——`:13`。
3. 死栓、钉窗、睡衣、`Only whores did that.`、以及她不信——`:7`／`:10`。
4. 蛋糕与三只气球、`Honestly? It felt better than a real birthday.`——`:31`。
5. 钟罩下的老鼠、吃糖霜花与藤＝虔诚、`She will swallow whatever Saskia deigns to give her.`——`:37`。
6. 美术课找不到＋`She has to build up her stamina for being human.`——`:40`。
7. Saskia 也不出门、要自己编理由——`:43`；笼子——`:46`。
8. 十二英尺、肩头弧度、又硬又软——`:49`。
9. 阅读灯与不敢开台灯、酒醉女人与恶魔、`shuddering breath`——`:70`。
10. 二十四年、`swallowing`/`explore and push and press deeper`——`:76`；白日梦与绿叶穹顶——`:76`。
11. 皮纳塔、嗅手指、花床单——`:88`；`She is still too shy to think the name Saskia in such a sentence.`——`:94`。

结论：**本章补 1 块（提示）＋导航补一句，无阻断**；修后 `chapter.sh` rc=0、`structure.py order` 29 md / 169 块 · 0 缺陷。
