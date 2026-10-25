# ch14 the bones in the yard —— R4 逐块追问 + R5 定档

## R4：固定追问（主语是谁／受事是谁／归属方向）
| 原句 | 主语 | 受事 | 归属方向 by/to/from/of | 判定 |
|---|---|---|---|---|
| 1 | Saskia（已离开） | 毯子／电视／茶几上的字 | `draped over Lucy`／`spelled out in Cheetos` | 通过 |
| 2 | 祖父 | Lucy 能看的东西 | `anything but the Disney Channel` | 通过 |
| 3 | Lucy（假想） | 地毯、地板、土 | `into the earth`／`like a mole` | 通过 |
| 4 | Lucy | 她自己要的东西 | `with Saskia`／`under the covers` | 通过 |
| 5 | 冰（身体反应）／Lucy 的腿 | 恐惧／自行车 | `down her spine`／`keep pedaling` | 通过 |
| 6 | Dover（说话人）／尸体 | 牙科记录／十年这个数字 | `at least ten years old`／`identify it visually` | 通过 |
| 7 | Lucy | 母亲、自己、祖父的禁令 | `raise two whores`／`locked me in the house` | 通过 |
| 8 | Lucy | 旧渔具盒／手指 | `nothing but paper towels`／`around her finger` | 通过 |

## R5：定档（阻断／提示／假红／跳过）
| # | 观察 | 档位 | 说明 |
|---|---|---|---|
| 1 | 引语逐字 8/8、词表 19/19 | — | `chapter.sh` rc=0；块序 0 缺陷 |
| 2 | R1 第 2 条的迪士尼频道无落点 | **提示 1（已修）** | 补原句 2（整段原句） |
| 3 | `Just—Jennifer’s Body. That movie… changed her.` | 假红（非缺陷） | 8 词 2 句、独立成段；含原文自带 `…`；内容由原句 3 的分析与导航承载 |
| 4 | `Captivity is easier when you don’t want things because you don’t know what to want.` | 假红（非缺陷） | 16 词 1 句、独立成段；导航「叙事手法」已把三处现在时独白逐句点名 |
| 5 | `It was fear, really—` / `Fear, and the strange certainty…` 等短段 | 假红（非缺陷） | 破折号断句与一段一句，无法单块、不可跨段拼接 |
| 6 | `Except to hang paintings` 与 `Command strips` 的对招 | 已核实为正确 | `:133`（Dover 的反将）／`:136`（Lucy 顶回去）；此二句对已在生产中按原文改过 |
| 7 | 「至少十年」与章末 `the last decade` 的关系 | 已核实为正确 | `:190` 一带；生产期已把「两个十年正好合上」收窄为「与章末 last decade 对得上」 |
| 8 | 情绪清单（成功的警方结案／「可怕的已经过去」） | 已核实为正确 | `:181`／`:184`（`The scary part is over, after all.`） |
| 9 | Lucy 的「碎」与「Saskia 只能把她修好」是 Lucy 的想法 | 已核实为正确 | 章末一段（`Saskia has no choice…` 属她的内心判断，非 Saskia 的应答） |

## 计数
- 阻断 **0** ／ 提示 **1（已修）** ／ 假红 **3 类（非缺陷）** ／ 跳过 **0**
- 逐字：引语 8/8、词表 19/19｜对应：0｜形态：块数 8（⑱ 上限 8、沙盒建议 4–7）｜断言：0 条落空

## 已核实为正确
1. 奇多拼字与笑脸、毯子、关掉的电视——`:14`。
2. 祖父只准迪士尼——`:20`（本次补块）。
3. 「液体的青霉素」与曾祖母的方子——`:31`。
4. 尸体至少十年、靠牙科记录认人——`:160` 一带。
5. 249 Durant Avenue 与园林工——`:154` 一带。
6. 祖父的禁令、`raise two whores`、没有网也没有电话——`:145`。
7. Febreze、最大的刀、`the case seems pretty open and shut`——`:181`／`:184`／`:166`。
8. 旧渔具盒、纸巾、木乃伊手指与 `less violence`——`:206` 一带。

结论：**补 1 块（提示），无阻断**；修后 `chapter.sh` rc=0、`structure.py order` 29 md / 175 块 · 0 缺陷。
