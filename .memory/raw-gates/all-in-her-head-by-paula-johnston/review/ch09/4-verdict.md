# ch09 T3 判定

覆盖：R1 text-only 8 事实、R2 JSON rc=0、R3 三账、R4 原句 1–5 全块逐对人判。

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 「不忍心她和醉汉调戏她的深夜夜班」 | text/ch09_8_blair.txt:82 “he wouldn’t feel comfortable with me being wolf-whistled at by drunken men”；md:49 | 被动关系丢失，受事方向错 | 阻断 |
| 「十六年的打工史」 | text:79 “from the week I turned sixteen”；md:97 | 十六岁起打工 ≠ 十六年工龄 | 提示 |
| 五块引语逐字与说话人 | 2-machine.json；text:19,55,79,82,100 | 正确 | 已核实 |

四组数：逐字 5/5；对应 5/5；形态 5 导航/4 子项/5 块；断言 1 阻断、1 提示。已按指令就地修复；chapter.sh rc=0，整书 gate EXIT=0。

## 已核实为正确
- 错名 Becky/Bianca/Becca、destined for greater things、两份甜点、脑内微波炉幻想均在本章或紧邻章；「It was his idea」确在 Blair 线开篇（ch03）。
