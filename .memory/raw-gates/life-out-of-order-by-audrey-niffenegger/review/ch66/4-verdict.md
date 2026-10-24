# ch66 判定表（Voltairine）

- 覆盖：深审人判全块（4/4）+ 四件套齐全；素读 8 条（`1-suread.json`）
- 机器层：`bash scripts/chapter.sh "…/ch66 voltairine.md" --json` → **rc=0**，块数 4，引语段 4/4 命中，查无 0，空引号 0，子项缺 0，关键词异常 0，中文密度低 0，nav 5（5 项齐），H1 `66. Voltairine` 形态正确，块数 4 vs 本书中位 6 / 区间 3–10（在范围内）
- 报数：**逐字 0 · 对应 0 · 形态 0 · 断言 1（另提示 3）**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 抬头日期与年龄：「2044 年 6 月 25 日，Alba 41 岁」 | text/ch66:18 `Saturday, June 25, 2044 (Alba is 41)` | md 只写「2044年6月」，未写 41 岁；与全书出生年推算不冲突（2044−41=2003） | 提示 |
| 一句话概括「已婚一年、十个月大的女儿沃泰琳」 | text/ch66:35 `“This is Voltairine,” Caralora says. “She’s ten months old.”`；text/ch66:63 `“We got married a year ago,” Lucinda-Isadora interjects.` | 数字与说话人都对（结婚一年出自 Lucinda-Isadora 之口，md 未错记为旁白） | 已核实为正确 |
| 「阿尔芭问这是怎么回事，卡萝拉只得意地说，有个同卵双胞胎兄弟会很方便」 | text/ch66:35 `“But—how?”`；text/ch66:39 `Caralora looks smug. “It can be convenient to have an identical twin brother.”` | 问答配对、说话人、`smug`→「得意」均对；md 未把这位兄弟指名为扎克（原文也未给名） | 已核实为正确 |
| 人物弧线把「喂奶」写给卡萝拉 | text/ch66:43 `I hand Voltairine over to Lucinda-Isadora. They arrange a small white flannel blanket across their shoulder, unhook their bra and put the baby to their breast to nurse.`；对照 text/ch66:35 卡萝拉只做过 `takes the baby from Lucinda-Isadora and lowers it carefully into my arms` | **施事错位**：哺乳者是卢辛达-伊莎多拉，md 第 14 行写成 `卡萝拉…抱着孩子、递出孩子、喂奶、唱歌`；同段下一句自己又写 `卢辛达-伊莎多拉…解开衣襟喂奶`，前后互斥 | **阻断** |
| 块 1「船屋树荫里看天鹅船／公园里没有一群人属于她」 | text/ch66:23-24 `I’m resting in the shade at the Boathouse in Humboldt Park, watching the swan pedal boats glide around and around the lagoon. The park is crowded with picnicking families, volleyball players, dog walkers, even a birthday party with an elaborate puppet show.` | 中文逐项对应（船屋／树荫／天鹅脚踏船／野餐家庭／排球／遛狗／木偶戏）；「不在任何一群里」是基于同句的合理推断，非编 | 对应 |
| 块 2「Ouch 之后紧接 entranced」 | text/ch66:35 `“Ouch,” I say, entranced.` | 与原文顺序一致；婴儿体征（soft black curls / light brown skin / gold-flecked hazel eyes / two tiny teeth）逐项无增删 | 对应 |
| 块 3「I put my hand on her shoulder, and she covers it with hers」的主语 | text/ch66:71 `She’s sitting on the blanket near my feet. I put my hand on her shoulder, and she covers it with hers.` | md 写「阿尔芭把手放在卡萝拉肩上，卡萝拉用自己的手覆住它」——`I`=阿尔芭、`she`=卡萝拉，方向正确 | 已核实为正确 |
| 块 4 手指按唇与「值得等」的归属 | text/ch66:101-102 `when he asks why I’m so exuberant I just smile and put a finger to my lips. “You’ll find out soon,” I say, kissing him. “It’ll be worth the wait, you’ll see.”` | `him`=扎克，说「值得等」的是阿尔芭；md 未把「值得等」误挂到扎克或卡萝拉 | 已核实为正确 |
| 导航「卡萝拉承认自己一直知道在等什么」 | text/ch66:80 `“Not exactly,” Caralora says. “I knew enough. When they came to me, I understood.”` | 原文先否认「确切知道」再退到「知道得够多」，md 未收这层限定，措辞比原文更绝对 | 提示 |
| 「Gomez 与父亲未能见到孩子」未进块 | text/ch66:92 `“I wish Gomez could have known her. And my dad, too,” I say.` | 本章唯一写到两名死者的地方，md 仅以词汇例句收了紧邻的回应句 | 提示 |
| 卢辛达-伊莎多拉的称谓 | text/ch66:30 `kiss Lucinda-Isadora on their flushed cheek`；text/ch66:43 `unhook their bra`；同段 `the baby hears her mother’s voice` | 原文 they/their 与 her 并存，md 统一作「她」；属称谓口径，须与全书统一，非本章可判错 | 提示 |
| 零命中类断言 | 本章无 | — | — |

## R4 逐块对应（三问）

| 块 | 这段中文是不是在讲这句引语？ | ①动词主语 | ②受事 | ③归属方向 |
|---|---|---|---|---|
| 1 | 是（原文前两句，未越界讲全书） | Alba | 自己/公园人群 | `in the shade at the Boathouse` 归洪堡公园，md 作「洪堡公园船屋的树荫」正确 |
| 2 | 是（原文 3 句全取） | Alba / Voltairine | 婴儿的脸、阿尔芭的头发 | `grabs my hair`＝抓阿尔芭的头发，未颠倒 |
| 3 | 是（引语起于 `I put my hand on her shoulder`） | Alba / Caralora | 手 | `covers it with hers`＝卡萝拉覆阿尔芭的手，方向对 |
| 4 | 是（尾段两句） | Alba | 扎克 | `kissing him` 的 him＝扎克，md 作「亲了他一下」正确 |

## 已核实为正确（防下一轮误修）

1. **「有个同卵双胞胎兄弟会很方便」没有写成「扎克是同卵双胞胎」** —— 原文 text/ch66:39 只有 `It can be convenient to have an identical twin brother.`，未给名字；别章可证这位兄弟是 Nick（`text/ch01_the_last_party.txt:153` `she and Nick are identical twins`）。md 保留模糊是对的，**不得**据此改成「扎克的孪生兄弟」或「卡萝拉借扎克生育」。
2. **「结婚一年」出自 Lucinda-Isadora**，不是旁白、也不是卡萝拉说的 —— text/ch66:63。md 第 11 行作「她与卢辛达-伊莎多拉已婚一年」主语是卡萝拉与卢辛达二人，成立。
3. **「Ouch… entranced」** —— text/ch66:35 `“Ouch,” I say, entranced.`：原文就是「疼」与「入迷」并置，不是 md 添加的反讽。
4. **「五个祖母、三个姑姨、四个叔叔」** —— text/ch66:88 `She has five doting grandmas, three devoted aunties and four besotted uncles.`：数字与原文一一对应（md 只在词汇例句引用，未在分析里改数）。
5. **「脸上掠过一片阴云」的主语** —— text/ch66:96 `Caralora is looking up at me as she speaks, so she doesn’t see the cloud of sadness that passes over Lucinda-Isadora’s face.`：阴云在卢辛达-伊莎多拉脸上、卡萝拉没看见；md 第 14 行作「卢辛达-伊莎多拉…脸上偶尔掠过一片阴云」成立，**不要**改成「卡萝拉脸上」。
6. **「赤脚、饥饿、垃圾箱里捡来的衣服」** —— text/ch66:24 `The outfit I’m wearing was the best I could do, an extra-large Cubs T-shirt and baggy jeans, sourced from a dumpster behind a Salvation Army thrift store. I’m barefoot and hungry.`：md 三处（导航、情感弧线、一句话总结）一致，无夸大。
7. **「走两个钟头回黄房子」** —— text/ch66:24-25 `I don’t have the energy to start the long walk to the Yellow House… If I start now, I’ll get there in two hours, long before dark.`：md「走两个钟头回黄房子」逐字对应。
