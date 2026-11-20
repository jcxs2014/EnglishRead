# ch09 R3 对账（素读 8 条 ↔ md）

R1 来源：review/ch09/1-suread.json（子代理盲读 text/ch09_9.txt，8 条，自检 8/8 PASS）。

| # | 素读事实 | md 覆盖 | 判 |
|---|---|---|---|
| 1 | 差点被围（狼群不再怕她）、窗中逃生 | 导航"救场成功与战局恶化同时发生"；块8 结尾自评链 | 提示 |
| 2 | 八岁宴会 Francois 银斧救命；英雄=站起来 | 原句1 逐字 | 对 |
| 3 | 破窗引注意 + 击毙威胁 Madame Denue 的 Devereaux | 原句2 逐字（引注意）；Devereaux 之名在导航"连毙 Devereaux、Jareau 两狼" | 对（导航点名+块3 名字链） |
| 4 | Jareau 前爪下部中箭、嘴朝下倒地、单银尖伤 | 原句3 三段逐字 | 对 |
| 5 | "meant to rule by my side" + friends since childhood + 整夜受苦威胁 | 块3 提示含 friendship；统治意图未入块 | 提示→修（词序校正，见 4-verdict）；统治线由 ch12 块2 全量承接 |
| 6 | 数箭识破最后一支 + 取"纪念品"撤退 | 原句4/原句5 逐字 | 对 |
| 7 | Madame Denue 称射六七匹；她更正只射三匹 | 未入块（块6 收饮酒否认） | 提示（计数 3 = ch08 Tumier + ch09 两狼，与 md 各章叙述无冲突） |
| 8 | 结尾自评：十六岁/十箭/无弱点 | 原句8 逐字；十箭在块4 分析 | 对 |

漏：0（转折层全在：英雄定义/破窗/双杀/数箭/纪念品/醉酒否认/装填疏漏/单边透明）
编：0
错：1 —— **块3 提示引语词序**："childhood friends" 不是原文词序（text 为 "friends since childhood"）⇒ 提示层英文须逐字。已校正，chapter.sh rc=0。档位：**提示→当场修**（取证：`/usr/bin/grep -o "friends since childhood" text/ch09_9.txt` exit 0 命中）。
