# ch05 R3 对账（素读 8 条 ↔ md）

R1 来源：review/ch05/1-suread.json（子代理盲读 text/ch05_5.txt，8 条，自检 PASS）。

| # | 素读事实 | md 覆盖 | 判 |
|---|---|---|---|
| 1 | 打猎出发（Papa 战时十字弓传给她，Papa 持 musket） | 块1 军令三条；装备细节未入 | 提示（背景铺陈） |
| 2 | 拖鞋陷泥 Papa 拒帮 "We're not here to find slippers" | 未入块 | 提示（兔子课的铺垫，同训导者同场景） |
| 3 | 射兔迟疑、三连催令 | 原句2 逐字 | 对 |
| 4 | 荆棘伤脚、"Mama's not here. Dress it yourself"、撕裙四圈自裹 | 原句3 逐字（Glancing up…four times）；"Then bleed." 在分析逐字引用 | 对 |
| 5 | 小鹿 Now 令下击颈倒地、"Well done, Helena" | 原句4 逐字（wonder and pity 段）——扣扳机句与 Well done 未入 | 提示（心理课链条已收：pity→shoved aside→meat 均以逐字英文入分析） |
| 6 | 一小时后到家，Papa 报喜，Mama 追问，她答 "I stopped the bleeding" | 未入块（T3 修复：补入原句3 提示） | 提示→当场修 |
| 7 | 现在线：箍桶铺屋顶伏击 | 原句5 扼喉段；"No hesitation." 在提示逐字引用 | 对 |
| 8 | 跃墙扼喉、夺弩、提三狼之死、宣判慢慢杀、因楼下喊话松手 | 原句5/6/7/8 四块逐字 | 对 |

漏：0（转折层全在：军令/犹豫课/止血课/首杀心理课/扼喉/宣判/脱身/颤栗收尾）
编：0
错：1 —— **原句7 分析把 "It was meat." 错指"第 3 章"**；取证 `/usr/bin/grep -rn "It was meat" text/` → 仅 `text/ch05_5.txt:344` 命中、ch03 计数 0（exit 1）⇒ 属本章狩猎课闪回。已改"本章狩猎课闪回里那句"。档位：**阻断（跨章章号，7a 类）→ 当场修**。
