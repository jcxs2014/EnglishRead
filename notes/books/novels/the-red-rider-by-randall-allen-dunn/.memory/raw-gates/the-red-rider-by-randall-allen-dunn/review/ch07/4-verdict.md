# ch07 4-verdict（T3 深审）

R1：review/ch07/1-suread.json（8 条，子代理盲读，自检 OK）。
R2：review/ch07/2-machine.json（chapter.sh --json verdict=ok，rc=0；8 块 8 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 羞愧自审 | burned with shame/How had I become so afraid 在引语 | 问句主语=她（第一人称自审）✓ | 对应 |
| 2 | Denue 店旧创 | beat me half to death/shut the door on us 在引语 | 施暴者=Jacque、关门者=Jacque 之父 ✓；中文"或是为儿子羞愧，或是怕 Papa"=either…or ✓ | 对应 |
| 3 | 门把特写 | gripped the doorknob/sting/Forbidden to buy a dress 在引语 | I=她握门把 ✓；"Monsieur Denue 心知儿子的暴行"=realized his own son had caused ✓ | 对应 |
| 4 | 狩猎法自白 | constant visits/beautiful young women/their addresses 在引语 | I=Grenault（自述）✓；"月夜上门"=under the light of the moon（引语内）✓ | 对应 |
| 5 | 歌剧品名 | see more of/Lisette/like an opera 在引语 | 说话人=Grenault ✓；"what was it?" 的装忘=中文"装作记不清" ✓ | 对应 |
| 6 | 封口威胁 | private activities/secret relationship/stop any such rumors 在引语 | she=Madame Leóne（"she knows nothing"）✓；"our secret relationship" 的 our=Grenault 与 Helena（讹称）——中文已点破"暧昧措辞把威胁包进调情" ✓ | 对应 |
| 7 | 偷地址预告 | So full of life/put up quite a fight/relieve of that address 在引语 | 她=Lisette（受猎者）✓；"relieve"施事=Grenault ✓ | 对应 |
| 8 | 守夜宣言 | I would be waiting/in the darkness 在引语 | I=她 ✓ | 对应 |

跨章引用核章号：块4 分析"回看 ch01 他声称'我们大都在煤矿做工'"——text/ch01_1.txt "The rest of us work in the coal mine, mostly" ✓ 章号与语义正确。
数字回原文：七岁（块2）="When I was seven years old"；九年前（块3）="being locked out nine years ago" ✓。
原文内部矛盾照录（非 md 缺陷）：Jacque 围殴年龄 ch06 记八岁同龄、ch07 记七岁——各按各自引语照录，未强行统一。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 救 Leóne 决心句/跟随进店/店内业务对话/她的失手威胁与三狼点名未入块 | 均为铺陈或已被导航覆盖 | 不修 | 提示×4（依据：导航层与块层语义覆盖，无数字/关系断言落空） |

无修复动作。chapter.sh rc=0。

## 已核实为正确

- 块3 中文"明明 Monsieur Denue 心知儿子的暴行给她留下的伤"——原文 "even though Monsieur Denue realized his own son had caused my injuries"（text/ch07_7.txt 逐字）✓。
- 块5 分析"这句的续句更露骨——'I wonder how sweet she'll sing when I bite into her.'"——该句为 text/ch07_7.txt 逐字（same para）✓，只引不占块，三层英文取证合法。
- 块6 分析"以退为进的三段式"——三句均在引语内（Assuming…/I trust…/That might…），计数与引语一致。
