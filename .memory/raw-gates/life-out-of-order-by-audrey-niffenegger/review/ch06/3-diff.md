# ch06 Rosehill — 对账（R3）

素读：`1-suread.json`（8 条，全部锚点经脚本核对命中，见下「锚点自检」）
机器层：`2-machine.json`，rc=0，verdict=ok，4 块 / 1395 words / 空引号 0 / 查无 0 / 子项缺 0 / 关键词缺 0 / 形态偏离 0
精读：`ch06 rosehill.md`（91 行，4 个引语块）

## 锚点自检

`python3 /tmp/verify_suread.py ch06` → 8/8 `OK`，行号逐条命中原文件（其中第 5 条初稿误写 97 行，命中 98 行，已改）。

## 一、漏（素读有 / md 无）

| # | 素读条目 | 原文（text/ch06_rosehill.txt） | md 对应 | 判 |
|---|---|---|---|---|
| L1 | 第 3 条：Lucinda 提议「回家只会被抓去做事，去 Rosehill」 | 48: “If we go back to my house they’ll just put us to work,” Lucinda points out, correctly. “Let’s go to Rosehill.” | 全篇未提这个提议与理由；导航只说「难得的一次出门」（:12），未说目的地是她临时选的 | 提示（非关键事件，未损因果） |
| L2 | 第 7 条：Lucinda 让 Alba 重讲父母的话、「We love her very much」、歌名《You're All I Need to Get By》、唱一段后忍哭 | 127–131: “Tell me again what they said?” / “‘We love her very much.’”　154–155: “It turned out to be ‘You’re All I Need to Get By.’”　155: “I realize that she’s trying not to cry.” | 四个块均未覆盖；仅导航之外的一句总结提到「只有一首歌的旋律」（:91）。墓园段落在 md 里只剩墓碑与死因（原句 3） | 提示（墓园中段整段无块；但导航 :11 提到「讲起…那次时间旅行」，情节线未断） |
| L3 | 第 8 条：Lucinda 提「Maybe we should plant a little tree over them?」与「你说过将来这片墓园是森林」 | 155: “Maybe we should plant a little tree over them?”　164: “You told me once that in the future this cemetery is a forest.” | 未进块，仅 :91 引了半句种树的话（放在「一句话总结」里） | 提示（伏笔性质，非本章转折） |

> 结论：无一构成「关键事件/转折未进任何一块或导航」。第 7 条是本章情绪重心，但导航 :11–:12 已交代墓园、父母、时间旅行三条线，故记提示不判阻断。

## 二、编（md 有 / 原文无）

| # | md 断言 | 原文 | 判 |
|---|---|---|---|
| F1 | :91「两个人拎着化掉的甜筒穿过英式哥特式大门」；:13 同义（「拎着化掉的甜筒走进去」） | 原文只写**边走边吃**：53: “licking our rapidly melting ice cream”；且 Lucinda 在**进门前**已吃完——88: “Lucinda takes the last bite of her ice cream cone, wipes her fingers fastidiously on a napkin and tucks it into her purse.”；93 行才进大门 | 提示（画面细节外推，非情节/关系/数字；改法：删「拎着…走进去」或改为「边走边吃」） |
| F2 | :12「到墓碑前落到最低（父母、外婆、两个舅舅，一年之内全没了）」 | 122: “but a year later there was a fire”——火在父母死后**一年**；五人之死跨约一年，非「一年之内」一气发生 | 提示（时序压缩，量级不差；非硬数字） |

## 三、错（两边都有 / 不一致）

| # | md 断言 | 原文逐字 | 判 |
|---|---|---|---|
| E1 | :91「墓碑上，Jasmine 与 Malcolm 后面跟着**同一组日期**」 | 111: `3-8-1976—2-10-2014`（Jasmine，108 行名）　117: `11-2-1976—2-10-2014`（Malcolm，114 行名）——**生年日期不同**（3-8 vs 11-2），仅卒日同为 2-10-2014 | **阻断**（数字不一致；改法：「两人卒于同一天 2-10-2014」） |

## 四、R4 逐块对应（人判）

| 块 | 引语 | 中文是否在讲这句 | 三问 | 判 |
|---|---|---|---|---|
| 原句 1 | 25 行 “She’s always been tall… still a child, unfinished, a girl.” | 是：身高/改裙/2044 的她/relieved | 主语＝Lucinda（试穿）＋Alba（看与想）；受事＝裙子、2044 年的 Lucinda；归属：2044 是 **Alba 记忆里的未来**，md 写「她想到的却是 2044 年的那个 Lucinda」方向正确 | 通过 |
| 原句 2 | 53–54 行 甜筒＋“Court is just a place where I don’t have much say in my own life” | 是：口味/大道/怕上法庭 | 主语＝两人（买、走）；受事＝甜筒；引语主语＝Lucinda，md 未误挂给 Alba | 通过 |
| 原句 3 | 122 行 抢劫→火灾→外婆与两个舅舅 | 是：死因链与人名归属（外婆＝Jasmine 的母亲） | 主语＝Lucinda 父母／外婆／舅舅；受事＝Lucinda（被留下）；“Jasmine’s mother” 的同位关系 md 译对 | 通过 |
| 原句 4 | 174 行 “We are absorbed into our big, cobbled-together family… Don’t worry, Alba. It’s all good.” | 是：客厅人声、柠檬水、皱眉后安慰 | 主语＝一家人（absorbed）；受事＝Alba 与 Lucinda；安慰的**发出者＝Lucinda**，接受者＝Alba，未颠倒 | 通过 |

> 密度检查：4 块均非字面复述；原句 4 的中文把 `cobbled-together` 解到「火／寄养／收养攒出来」，属本章内可回溯的解读，未越到全书主旨。

## 五、已核实为正确（防下一轮误修）

1. **抬头 `Alba is 42`（2023 年）**：`text/ch06_rosehill.txt:18` “Thursday, September 7, 2023 (Alba is 42, Lucinda is 16)”——原书原文如此，非译文错；**md 全篇未据此刻算 Alba 年龄**（grep `42 岁` 零命中），无需改。
2. **「Celia 在正文里没有一句台词」**（md :14）：`grep -nE 'Celia'` 得 23/30/67/71/75/174 六处，全为叙述或他人转述；174 行 “Celia arrives a few minutes after we do.” 只有动作。断言成立。
3. **5'10"**：md 写「身高 5 英尺 10 英寸」，原文 :25 “she’s suddenly 5'10" and a little more”——换算正确（原文的 “a little more” 未译，不影响）。
4. **350 英亩**：原文 :98 “Rosehill is huge, 350 acres”，md :91 照抄，未夸大。
5. **13 条词汇例句**：逐条回 `text/ch06` 命中本行（transformative:25、fastidiously:88、cobbled-together:174、bewildered:122、imposing:93、sporadic:97、humidity:93、sleepover:122、swapping:174、memories:135、foster kid:75、grocery store:154、daughter:122），无跨章搬句。
