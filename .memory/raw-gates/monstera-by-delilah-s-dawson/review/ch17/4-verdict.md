# ch17 someone gets hurt —— R4 逐块追问 + R5 定档

## R4：固定追问（主语是谁／受事是谁／归属方向）
| 原句 | 主语 | 受事 | 归属方向 by/to/from/of | 判定 |
|---|---|---|---|---|
| 1 | Saskia（喊停、按门）／Lucy（看） | 烤箱门／Lucy | `on the oven`／`following her` | 通过 |
| 2 | 长期受压制的人（泛指＝Lucy） | 她的恐惧／那些窗 | `under near constant anxiety and oppression`／`painted shut` | 通过 |
| 3 | 祖父 | Lucy（被看的对象） | `under her grandfather’s scrutiny`／`a sinning sheep that required a firm shepherd` | 通过 |
| 4 | Lucy（发问人） | Saskia／那只口罩 | `out of her mouth`／`why you wore the mask` | 通过 |
| 5 | Saskia | Lucy／她自己的责任 | `I don’t want to hurt you`／`nuzzles her, cheek to cheek` | 通过 |
| 6 | Saskia | Lucy 的手臂／距离 | `squeezes Lucy’s arms`／`steps away`／`around me` | 通过 |
| 7 | Saskia | Lucy 的背／伤口 | `It’s all red`／`Someone gets hurt` | 通过 |
| 8 | Roger（他看的）／Lucy（定性） | Lucy 脖子以下／Roger 的目光 | `below the neck`／`look elsewhere` | 通过 |
| 9 | Roger／Lucy | 摄像头插座／新的充电器 | `illegally recording a young woman in her home`／`I want my tenants to have what they need` | 通过 |

## R5：定档（阻断／提示／假红／跳过）
| # | 观察 | 档位 | 说明 |
|---|---|---|---|
| 1 | 引语逐字 9/9、词表 18/18 | — | `chapter.sh` rc=0；块序 0 缺陷 |
| 2 | R1 第 3 条（女朋友／口罩／`Nope`）在 md 里零命中 | **提示 1（已修）** | 补原句 4 |
| 3 | `See? Someone gets hurt.` 与前面「我不想伤你」的对照 | 已核实为正确 | 原句 6 与 7 同章对读，导航「Tropes 反转」已写明 |
| 4 | 门是 Saskia 没关的 | 已核实为正确 | `:236` 一带；导航与一句话总结均承载 |
| 5 | Roger 的黄色牙齿与 `doll` 称呼 | 已核实为正确 | `:161`／`:172`；导航「人物弧线」已写他暴露的是房子的气味与新烤箱 |
| 6 | 玉米面包与铁锅、黑烟里的黑炭饼 | 已核实为正确 | `:4`／`:181`；词表 `alarm blares` 与导航均承载 |
| 7 | 全章无凭空英文引语 | 已核实为正确 | 导航反引号片段均可在 `text/` 命中（脚本 ⑯ 归章正确 0 ／ 伪造 0） |
| 8 | 假红：无 | — | 本章无不可成块的一行成段句 |
| 9 | 块数 9（⑱ 配额 3–8 上浮 1） | **提示（非阻断，已记）** | `structure.py` 报「引语块数与配额相差过大」提示型；理由：新增块承载全章唯一的口罩之问，属关键转折，按先例不删不并 |

## 计数
- 阻断 **0** ／ 提示 **2（1 待改已改；1 为块数上浮，记录不改）** ／ 假红 **0** ／ 跳过 **0**
- 逐字：引语 9/9、词表 18/18｜对应：0｜形态：块数 9（⑱ 3–8 上浮 1，提示型）｜断言：0 条落空

## 已核实为正确
1. `Oh, no. The cornbread!` 与踉跄回跑——`:4`。
2. `Leave the door closed` 与 OFF 键——`:13`。
3. `under her grandfather’s scrutiny…a sinning shepherd`——`:40`。
4. 口罩之问与 `Nope`——`:64`／`:67`（本次补块）。
5. `There is absolutely nothing wrong with you. I just don’t want to hurt you.`——`:94`。
6. `People get hurt around me…I’m the problem`——`:100`。
7. `Oh, you poor thing. It’s all red.` 与 `See? Someone gets hurt.`——`:124` 一带。
8. Roger 站在卧室门口与 `below the neck`——`:161`／`:175`。
9. 插座、`illegally recording` 与加租十美元——`:205`／`:211`。

结论：**补 1 块（1 条提示可修项）＋1 条块数上浮提示，无阻断**；修后 `chapter.sh` rc=0、`structure.py order` 29 md / 180 块 · 0 缺陷、`gate.sh` RC=0。
