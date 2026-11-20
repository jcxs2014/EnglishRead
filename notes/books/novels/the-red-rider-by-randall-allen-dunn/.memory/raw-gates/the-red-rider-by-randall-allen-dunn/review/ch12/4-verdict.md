# ch12 4-verdict（T3 深审）

R1：review/ch12/1-suread.json（8 条，子代理盲读，自检 8/8 PASS）。
R2：review/ch12/2-machine.json（chapter.sh --json verdict=ok，rc=0；10 块 13 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 加冕演讲 | how mine begins/strung up/piece by bloody piece 在引语 | 说话人=Grenault、受刑者=她 ✓；"your life ends / mine begins" 方向 ✓ | 对应 |
| 2 | 空屋动机 | in the mine/shared a house/Because of you 在引语 | We=Grenault 与四亡友 ✓；"Because of you" 的 you=她（她杀了四人）✓；省略号两段各为 text 相邻完整段 ✓ | 对应 |
| 3 | 毒打 | backhand/struck me again/like a rag doll 在引语 | He=Grenault 施暴、she 受击 ✓ | 对应 |
| 4 | 绝境祈祷 | failed Madame Leóne/both our lives/I've got nothing left 在引语 | I=她 ✓；"赔上两个人的命"=her+Leóne ✓ | 对应 |
| 5 | 火把发现 | silver candlesticks/had missed/The torch 在引语 | Grenault had missed——漏看者=Grenault、被漏物=银烛台 ✓ | 对应 |
| 6 | 站姿破译 | a broad grin/one paw forward, holding one paw back/to retreat 在引语 | He crept=Grenault ✓；"The same fighting stance Francois had taught me" 回指=她所学 ✓ | 对应 |
| 7 | 火攻 | shoved the torch/sizzling flesh/raced across his fur 在引语 | I=她怼火 ✓；受击者=Grenault 胸膛 ✓ | 对应 |
| 8 | 草叉封炉 | seized it/pitchfork/shoved as hard as I could 在引语 | I=她持叉 ✓；"Madame Leóne hurried to retrieve" 施事=Leóne ✓ | 对应 |
| 9 | 生存账 | would survive/had survived/the worst Lycanthru 在引语 | I=她 ✓ | 对应 |
| 10 | 格言收尾 | stopped the bleeding/I would end this 在引语 | 两段均为 text 末尾相邻完整段 ✓ | 对应 |

跨章引用核章号：
- 块1 提示"ch05 宣判、ch08 提议、此章彩排"——ch05="Then I'll kill you—slowly—in front of the entire order."；ch08=text/ch08_8.txt:194 "We're going to savor every bloodied piece of her."（grep exit 0 取证）✓。
- 块4 分析 "Father Vestille 的 'exercise your faith'"——text/ch10_10.txt "Then you need to exercise your faith" ✓。
- 块6 分析 "Francois 的站姿"——text/ch06_6.txt "one foot forward and one foot back" 同构 ✓ 章号正确。
- 块8 提示 "Run, Helena!"——text/ch11_11.txt 逐字（跨章回指，sweep 口径 ⚠️ 跨章=提示级）。
- 块10 分析 "ch05 她第一次说 'I stopped the bleeding'"——text/ch05_5.txt 有该句（跨行拼接），ch06–ch11 无此句，"第一次"成立 ✓。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 绷带/俘虏甜点/救场收尾 未入块 | 导航与块1 提示、块10 收束覆盖 | 不修 | 提示×3（依据：终章 10 块配额下转折层与格言链全收） |

无修复动作。chapter.sh rc=0。

## 已核实为正确

- 块5 分析 "'The torch.' 独立成段，全章的重心在一次抬头间换轨"——text/ch12_12.txt "The torch." 确为独立完整段。
- 块6 分析 "他连杀她都在借力"——"ramming me against it, which drove his claws a little deeper"（原句8 引语内）支撑。
- 块9 分析 "'the worst...yet faced' 里藏着一个 'yet'"——引语逐字 "the worst Lycanthru I had yet faced" ✓。
- 块10 "血止住了" 与 ch05 呼应——两句均为 text 逐字（ch05 跨行拼接、ch12 独立段），呼应关系经 R1 两侧取证成立。
