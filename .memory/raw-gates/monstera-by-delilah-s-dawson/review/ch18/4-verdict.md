# ch18 the seed in her eye —— R4 逐块追问 + R5 定档

## R4：固定追问（主语是谁／受事是谁／归属方向）
| 原句 | 主语 | 受事 | 归属方向 by/to/from/of | 判定 |
|---|---|---|---|---|
| 1 | Saskia（看的人） | Roger（被等走的人）／Lucy | `through the fenestrations of a Monstera deliciosa`／`in Lucy’s apartment` | 通过 |
| 2 | Lucy（复述）／Roger（闯入者） | Lucy 的背／那扇门 | `He let himself in`／`I thought he was you` | 通过 |
| 3 | Lucy（报账）／Saskia（从命） | 芦荟／十美元 | `to next month’s rent`／`over her shoulder` | 通过 |
| 4 | Saskia（手）／Lucy（默许） | Lucy 的背／Saskia 的手指 | `wet with aloe gel`／`the glide of Lucy’s skin` | 通过 |
| 5 | 那个做汤的人（＝Lucy）／Saskia | 汤／Saskia 的谎言 | `the innocent girl who made the mistake of liking her` | 通过 |
| 6 | Saskia（所有者） | 她公寓里的六十三株植物 | `in her apartment`／`they do not care for her` | 通过 |
| 7 | Lucy（取的人）／Saskia（被取的人） | Saskia 的眼角／那颗种子 | `the corner of Saskia’s eye`／`what Lucy has found` | 通过 |

## R5：定档（阻断／提示／假红／跳过）
| # | 观察 | 档位 | 说明 |
|---|---|---|---|
| 1 | 引语逐字 7/7、词表 13/13 | — | `chapter.sh` rc=0；块序 0 缺陷 |
| 2 | R1 第 6 条（充电器与十美元）在 md 里零命中 | **提示 1（已修）** | 补原句 3 |
| 3 | R1 第 3 条（六十三株植物与三连否定）无落点 | **提示 2（已修）** | 补原句 6 |
| 4 | 五行一行成段（`No.` / `She pulls her hand away.` / `It doesn’t matter what she wants.` / `Saskia does not have an answer.` / `She doesn’t understand it herself.`） | 假红（非缺陷） | 独立成段的单句无法成块、也不可跨段拼接；导航「叙事手法」已逐字点名 |
| 5 | Roger 翻共用的邮箱 | 已核实为正确 | `:7` 一带；导航 Tropes 明写 |
| 6 | `It’s me!` 与反锁门闩 | 已核实为正确 | `:16`；导航情感弧线用中文表述承载（避免跨章英文引语无章号） |
| 7 | Lucy 复述的四个短句 | 已核实为正确 | `:25`（原句 2 整段） |
| 8 | 章末 `pop` 与种子 | 已核实为正确 | `:85`（原句 7 整段） |
| 9 | 块数 7（⑱ 3–8 内） | — | 原 5 块承载不足，补 2 块后落区间中段 |

## 计数
- 阻断 **0** ／ 提示 **2（均已修）** ／ 假红 **1 类（非缺陷）** ／ 跳过 **0**
- 逐字：引语 7/7、词表 13/13｜对应：0｜形态：块数 7（⑱ 3–8 内）｜断言：0 条落空

## 已核实为正确
1. 开场隔龟背竹看 Roger 走远——`:4` 一带（原句 1）。
2. Roger 翻她与 Lucy 共用的邮箱——`:7`。
3. `It’s me!` 与反锁——`:16`。
4. Lucy 的四个短句复述与红痕——`:25`（原句 2）。
5. 芦荟的滑与「不肯挪开」——`:43`（原句 4）。
6. 「不该碰」与收手——`:46` 一带（导航＋读者视角提示）。
7. 汤与谎言——`:70`（原句 5）。
8. 六十三株植物——`:76`（本次补块）。
9. 眼角种子与 `pop`——`:85`（原句 7）。

结论：**补 2 块（2 条提示），无阻断**；修后 `chapter.sh` rc=0、`structure.py order` 29 md / 182 块 · 0 缺陷。
