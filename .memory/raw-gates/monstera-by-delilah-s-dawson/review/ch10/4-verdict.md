# ch10 the smell of the sea —— R4 逐块追问 + R5 定档

## R4：固定追问（主语是谁／受事是谁／归属方向）
| 原句 | 主语 | 受事 | 归属方向 by/to/from/of | 判定 |
|---|---|---|---|---|
| 1 | Lucy | 她的门／她的书／她自己 | `of sleeping without a door`／`on the floor` | 通过 |
| 2 | Lucy | 她自己 | `in the darkness`／`for herself` | 通过 |
| 3 | Saskia | 那些平装本／Lucy | `over some of the newer books`／`into the main room` | 通过 |
| 4 | Saskia | 充电器（被砸） | `into Lucy’s bedroom`／`with Lucy’s new marble bust` | 通过 |
| 5 | Saskia | 小方块 | `until the black plastic shatters`／`I’m guessing Roger did` | 通过 |
| 6 | Saskia（对 Lucy 说） | Roger／前门 | `for your front door`／`without your consent` | 通过 |
| 7 | Saskia | Roger／任何人 | `in this apartment`／`while you’re asleep` | 通过 |
| 8 | 那些设备（Roger 持有） | 视频 | `through a phone app`／`every time the camera was triggered` | 通过 |
| 9 | Lucy | 她的心意／邀请 | `into her eyes`／`with which Saskia is familiar` | 通过 |

## R5：定档（阻断／提示／假红／跳过）
| # | 观察 | 档位 | 说明 |
|---|---|---|---|
| 1 | 引语逐字 9/9、词表 14/14 | — | `chapter.sh` rc=0；块序 0 缺陷；关键词 `not just a charger` 已按原文逐字（原稿写 `this isn’t just a charger` 时曾触发 ⑱，已在生产中修） |
| 2 | R1 第 4/6/8 条未落点 | **提示 1（已修）** | 补原句 6、原句 8 ＋ 导航补「违法」一层 |
| 3 | 单句成段的短段（`It makes her feel so off-kilter.`／`This line of thinking makes her nauseated.` 等） | 假红（非缺陷） | 1 句、10–12 词，无法单块、不可跨段拼接；内容由导航、一句话总结与词表（`off-kilter`／`nauseated`）承载 |
| 4 | 「闹上法庭，租金与水电全没」（反转一） | 已核实为正确 | `:124` `If we went to court, all that would go away.` |
| 5 | 「Saskia 先替 Roger 排除嫌疑，再补一句 Roger 或别的什么人」 | 已核实为正确 | `:214`／`:220`（顺序如实：排除在前） |
| 6 | 「读者比 Lucy 多知道那根从睫毛里拔出来的绿藤」 | 已核实为正确 | `text/ch07_chapter_7.txt` 种子线、ch09 指甲缝四粒 |
| 7 | 「晨间前门从里面锁着」 | 已核实为正确 | `:8` 一带（她确认落锁的习惯）与 `:247` 的收尾 |
| 8 | 云石半身像来自 Goodwill 且 Saskia 刚夸过 | 已核实为正确 | `text/ch08_chapter_8.txt` 胸像；`:106` 前一段的夸赞 |

## 计数
- 阻断 **0** ／ 提示 **1（已修，含 3 条漏项）** ／ 假红 **1 类（非缺陷）** ／ 跳过 **0**
- 逐字：引语 9/9、词表 14/14｜对应：0｜形态：块数 9（⑱ 上限 3–8，提示型）｜断言：0 条落空

## 已核实为正确
1. 手指的海味、塌下的书、开着的门、十年没有门——`:4`。
2. 两根手指与 `claiming the forbidden`——`:25`。
3. 书架上的手指与秘密笑容——`:88`。
4. `That son of a bitch.` 与半身像砸充电器——`:106`。
5. 砸碎后的 `Babe, this isn’t just a charger. It’s a camera.`——`:112`。
6. 违法与惹麻烦——`:118`；租金/水电/停车/法庭——`:124`。
7. 门挡建议与 `He’s a creep, but I don’t think he would do that.`——`:214`。
8. 云端与三十秒视频——`:232`。
9. `Roger, or anyone.`——`:220`；眼睛、好奇心与邀请——`:250`。

结论：**补 2 块＋导航一句（提示），无阻断**；修后 `chapter.sh` rc=0、`structure.py order` 29 md / 172 块 · 0 缺陷。
