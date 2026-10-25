# ch12 movie night —— R4 逐块追问 + R5 定档

## R4：固定追问（主语是谁／受事是谁／归属方向）
| 原句 | 主语 | 受事 | 归属方向 by/to/from/of | 判定 |
|---|---|---|---|---|
| 1 | Lucy | 纸条 | `under Saskia’s door`／`like they did in middle school` | 通过 |
| 2 | Lucy／Saskia（敲门者） | 她自己的心跳 | `on her door`／`back up the spiral staircase` | 通过 |
| 3 | Saskia | 那束花（她的园子） | `from her garden`／`surrounded by monstera leaves` | 通过 |
| 4 | Lucy | 那杯冰水／Saskia 的脖颈与嘴唇 | `on a coaster`／`to drink` | 通过 |
| 5 | Saskia | 遥控器／片单的选择 | `without hesitation`／`at the corners in delight` | 通过 |
| 6 | Lucy（内心） | Saskia 的视线 | `at two girls kissing`／`at me` | 通过 |
| 7 | Lucy | 一只枕头／她自己的尖叫 | `over her face`／`when the bathroom door clicks shut` | 通过 |
| 8 | Lucy | 护手霜与气味／想象里的 Saskia | `of her hand lotion`／`in the privacy of her bedroom` | 通过 |

## R5：定档（阻断／提示／假红／跳过）
| # | 观察 | 档位 | 说明 |
|---|---|---|---|
| 1 | 引语逐字 8/8、词表 13/13 | — | `chapter.sh` rc=0；块序 0 缺陷 |
| 2 | R1 第 8 条（枕头尖叫）无落点 | **提示 1（已修）** | 补原句 7（整段原句） |
| 3 | `Stupid`／`Stupid, stupid, stupid` 等一段一个词的短段 | 假红（非缺陷） | 1–3 词，无法单块、不可跨段拼接；导航「叙事手法」已点名分析 |
| 4 | `Would things be different…` 反事实段 | 跳过（未选） | 该段可切三句（45 词），本轮未选；内容由导航「情感弧线」承载，非缺陷 |
| 5 | 「位置在第十章那个上午的一周之后」 | 已核实为正确 | `:4` `It’s been a week since Lucy last saw Saskia`；上一章＝ch11（Saskia 收拾摄像头余波） |
| 6 | 「五点踱步、五点半担心惊恐发作、六点／六点零二／六点零三」 | 已核实为正确 | `:16`／`:31`／原句 2 的三句 |
| 7 | 「没人会戴着口罩去一个想亲的人家里」 | 已核实为正确 | `:120` 一带（口罩与亲吻的自我点破） |
| 8 | 「她端水、问冰、递遥控器」 | 已核实为正确 | 原句 4 与 `:100` 一带的招待 |
| 9 | 「有女孩接吻段落的恐怖片」（原稿写「两个女孩当主角」） | 已核实为正确（已收窄） | `:196`／`:169`；推断越界处已在生产中改回原文口径 |

## 计数
- 阻断 **0** ／ 提示 **1（已修）** ／ 假红 **1 类（非缺陷）** ／ 跳过 **1（未选，非缺陷）**
- 逐字：引语 8/8、词表 13/13｜对应：0｜形态：块数 8（⑱ 3–8 内）｜断言：0 条落空

## 已核实为正确
1. 一周、偷看不算数、争一小时、纸包、门缝——`:4`。
2. 五点／五点半／六点／六点零二／六点零三的计时——`:16`／`:31`／原句 2。
3. 自家园子的花与龟背竹叶——`:52`。
4. 口罩、掀起来喝水、脖颈与嘴唇——`:43`／原句 4。
5. `Jennifer’s Body` 与不迟疑——`:118` 一带。
6. 迪士尼频道与被保护得太好——`:118`。
7. 枕头尖叫——`:208`。
8. 护手霜与想象——`:226`。

结论：**补 1 块（提示），无阻断**；修后 `chapter.sh` rc=0、`structure.py order` 29 md / 174 块 · 0 缺陷。
