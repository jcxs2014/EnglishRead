# ch04 4-verdict（T3 深审）

R1：review/ch04/1-suread.json（8 条，子代理盲读，自检 PASS）。
R2：review/ch04/2-machine.json（chapter.sh --json verdict=ok，rc=0；5 块逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 会笑会说话的狼 | swear it was smiling/Mademoiselle/the beast clearly spoke 在引语 | it=狼 asked ✓；中文"它开口问道"主语一致 ✓ | 对应 |
| 2 | 先到外婆床上的狼 | already there/loped ahead/bloody nightgown 在引语 | it=狼 pawing at her（her=Grand'Mere）✓；"她的小腿还在狂奔"=my little legs（她）✓ | 对应 |
| 3 | 银刀爪与红痛 | chortled/silver knives/fiery red agony 在引语 | It swiped at my face——狼挥爪、她受击 ✓；中文"朝她脸上挥下"方向一致 ✓ | 对应 |
| 4 | 九岁梦醒 | nine years old/buried my scarred face/fully dressed 在引语 | his thick shirt=父亲 ✓；"他已穿戴整齐"=he was fully dressed ✓ | 对应 |
| 5 | 拥抱黑暗应征 | a tomb/embrace that darkness/cower 在引语 | "Yes, Papa"=她答 ✓ | 对应 |

跨章引用核章号：块3 分析"第 3 章那段工笔疤描"=ch03 原句3 ✓（text/ch03_3.txt triple claw marks 段）。
数字回原文：七岁="I was seven years old again."；九岁="I was nine years old."——均为 text 逐字 ✓。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 开场声音问话/摸脸颊回七岁未入引语 | 导航"声音先于狼形"已立 | 不修 | 提示（依据：转折层全收，857 词章 5 块配额下的取舍） |
| "See you soon" 道别 / "just over the ridge" 对答未入 | 对话推进细节 | 不修 | 提示（同上） |
| "You're having another nightmare" 未入 | 原句4 分析已含摇醒语境 | 不修 | 提示（同上） |

无修复动作。chapter.sh rc=0（2-machine.json 即修后状态）。

## 已核实为正确

- 块3 分析"银刀之爪与她的银箭互为镜像"——爪 "glinted like silver knives"（text/ch04_4.txt 逐字）与全书银箭设定对位，属评论性对应非事实断言。
- 块4 "父亲彻夜未眠" 的推断锚在 "It was dark but he was fully dressed."（原文逐字）——写明是解读而非事实转述。
- 导航"嵌套闪回（七岁梦境套九岁清晨）"与原文结构一致：梦境段在先、梦醒段在后。
