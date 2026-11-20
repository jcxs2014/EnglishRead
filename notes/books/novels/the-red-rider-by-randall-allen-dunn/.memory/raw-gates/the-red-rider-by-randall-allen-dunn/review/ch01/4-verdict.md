# ch01 4-verdict（T3 深审 · 边审边改）

R1：review/ch01/1-suread.json（8 条，子代理盲读，自检 ALL_OK）。
R2：review/ch01/2-machine.json（chapter.sh --json verdict=ok，rc=0；修复后复跑 rc=0，10 块 10 片段逐字全 ok）。

## R4 逐块对应（人判，修复后 10 块）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 握弩开场 | crossbow/wolves/This had become my life 在引语 | I=她握弩 ✓ | 对应 |
| 2 | 骑马入场 | cobblestone/wafting/revelry/loitering 在引语 | "两个闲晃的男人她都认得"=I recognized them both（她认得他们）✓ 方向无反 | 对应 |
| 3 | 身份与让路 | imposing/mere/parted/the Red Sea/weak smiles 在引语 | They recognized me=他们认得她 ✓；让路施事=守门人 ✓ | 对应 |
| 4 | 店主递情报 | cronies/wolf attacks/one of them 在引语 | "he said"=Touraine（text 邻域 Gerard Touraine）✓；"他"=大个子受指者 ✓ | 对应 |
| 5 | 反派疤貌 | clump/dead leaves/jagged/skull 在引语 | He stared=Grenault（上下文唯一在场者）✓ | 对应 |
| 6 | 血色威胁 | the color of blood/sort out/bloody mess 在引语 | I like=Grenault（对 her cloak）✓；受事=her ✓ | 对应 |
| 7 | 银箭威慑 | recoiled/tipped with silver/within seconds 在引语 | They knew=同伙们 ✓；"even a trace of silver would kill them" 受事=狼群 ✓ | 对应 |
| 8（新） | Lisette 标价 | lifted his chin/important to you/taste even sweeter 在引语 | He lifted his chin=Grenault ✓；she=Lisette（受问者非在场者）✓；"her taste even sweeter" 的 her=Lisette——中文"那会让她的味道尝起来更甜"方向一致 ✓ | 对应 |
| 9 | 新秩序宣战 | take orders/a new order/dealing with 在引语 | I don't take orders=Grenault ✓；"You're dealing with me now" 的 you=她 ✓ | 对应 |
| 10 | 预判收尾 | held his gaze/march out/tear me to shreds 在引语 | They would follow me=狼群追她 ✓；"撕碎"受事=她 ✓ | 对应 |

跨章引用核章号：新块8 提示"第 3 章揭示的伏笔（Lisette 是 Pierre 的继母）"——ch03 text "Madame Lisette Leóne. The woman Grenault said he was targeting." ✓；原句9 提示 Prime/delivery 两句均在 text/ch01_1.txt 逐字。
数字回原文：two months ago（原句2）✓、sixteen-year-old（原句3）✓、within seconds（原句7）✓。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| Lisette 情感转折（taste even sweeter）未入精读 | text/ch01_1.txt:"He lifted his chin, looking amused. “Is she important to you, Mademoiselle? That would make her taste even sweeter.”" | 按原文顺序插入新原句8，后续块重编号 | 提示→当场修（首章 S1 加权） |
| Prime 自报与 "dead or barely alive" 威胁未入 | text/ch01_1.txt:"“I am Luc Grenault. Soon to become the new Prime.”" / "once I deliver you to them, dead or barely alive." | 补入原句9 提示（逐字） | 提示→当场修 |
| "The Red Rider" 称号句未入块 | ch05/ch07/ch10 的 Red Rider 逐字链条不断 | 不修 | 提示（依据：身份确认句， epithet 在后续章精读均逐字在场） |
| "I didn't have much time." 未入块 | 原句10 分析"生死账"已含其义 | 不修 | 提示（悬置句独立成段，语义已覆盖） |

## 修复动作（边审边改）

1. 插入原句8（Lisette 标价块），原 8/9 顺延为 9/10；2. 原句9 提示补 Prime 自报与交人威胁（逐字）。修后 chapter.sh rc=0（10 块/逐字 10/10），gate.sh 退出码 0，pathspec 提交。

## 已核实为正确

- 原句3 中文"挤出一脸勉强的笑"="weak smiles"（text 逐字）——弱笑=恐惧而非敬意，是解读且锚在原文词组上。
- 原句4 中文"店主全程低头擦杯子"——原文 "Touraine kept staring down at the mug he was cleaning as he said"（text/ch01_1.txt 逐字）支撑，非编造。
- 原句7 "对两种形态通杀"——原文 "in human or wolf form—within seconds" 逐字支撑。
- 新块8 插入位置在原句7（银箭）与原句9（新秩序）之间，与原文出现顺序一致（text 308–311 行邻域先于 320–323），块序合规（structure.py order 口径）。
