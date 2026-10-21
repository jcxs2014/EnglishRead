# 4-verdict.md · 第 27 章《A Fatal Legacy》判定表

审：独立审查员（只负责 ch27）· 日期 2026-10-21
原文：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch27_27.txt`（17,033 字符）
md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch27 callie has dinner with eulalia.md`
落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch27/`（1-suread.json / 2-machine.json / 3-diff.md / 4-correspondence.md / 4-verdict.md）
**本次未改动书目录任何 md，未执行 git add / commit。**

---

## 一、四组数（只报这四组）

| 组 | 分母 | 通过 | 缺陷 |
|---|---|---|---|
| **逐字** | 40 条（10 条引语 + 30 条词汇例句） | **40/40** | 引语：机器 10/10 `ok`；人工用原文子串直查复核 10/10 `FOUND`（起止区间见 4-correspondence.md），无省略号拼接、无跨话轮拼接。词汇例句：30/30 逐字命中原文，每条恰好命中 1 次。**0 错** |
| **对应** | 10 块 + 导航/总结 2 层 | 对应 **10/10**；密度不足 **0**；不对应（讲主旨/生平）**0** | 施事/说话人错 **1**（导航「玻璃」句）；归属反转 **1**（酒的决定权，见 A1/A2）；引语选短 **3**（原句 1、6、9）；覆盖缺失 **2**（L1 Julian 主线、L2 Callie 预期被晾着） |
| **形态** | 4 项（H1 / 导航项 / 子项集 / 块数） | **4/4 合规** | **0 偏离**（详见下） |
| **断言** | 17 条事实性断言被逐条裁定（明细编号 A1–A9、P1–P8；另有覆盖类 L1–L5 单列、已核实正确项 10 条见第四节） | 与原文一致或仅措辞可改 **8**（P1–P8） | **与原文不符 9 处（A1–A9，去重后 7 条独立错误：A1+A2 同一错误两处、A5+A6 同一错误两处）** |

**阻断型条数：9 条独立错误，分布在 11 处** —— 断言组 7 条（A1+A2／A3／A4／A5+A6／A7／A8／A9）＋ 覆盖组 2 条（L1、L2）；**提示 10 条**（P1–P8 断言组 ＋ L3–L5 覆盖组）；**假红 0**；**跳过 0**。

> 分布：实质型（影响读者对文本的理解）5 条 = A1/A2（酒的决定权）、A3（说话人）、A4（Mel 在场）、L1（Julian 主线）、L2（甲方预期）；措辞/数字型（一处措辞或一个数字即可修）4 条 = A5/A6（编造断言）、A7（桌上只剩水）、A8（沉默）、A9（8 个问号）。

---

## 二、判定表（断言 | 证据（章:区间） | 结论 | 档位）

### 形态组

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| M1 | H1 = `27. St John’s Wood` | md:7；`2-machine.json.form.h1` = `27. St John’s Wood`，`h1_shape_ok: true`；全库 54 章 H1 均为 `N.` 式（`bookform.py`：H1 写法 `{'N.': 54}`） | 合规 | 通过 |
| M2 | 导航项 5 项、项名为众数 | md:9–15（一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法）；`2-machine.json.form.nav_count: 5`、`nav_missing: []`；`bookform.py`：导航项众数 5 项 | 合规 | 通过 |
| M3 | 子项集 = 4 项 | md 各块（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）；`form.subitems_modal` 与 `profile_subitems` 同为这 4 项 | 合规 | 通过 |
| M4 | 块数 10 | `form.blocks: 10`；本书块数中位 **7.0**、范围 **5–10**；profile `mystery-thriller` 允许 3–10；全书 54 章块数分布 5×5 / 6×19 / 7×10 / 8×5 / 9×8 / **10×7** | 10 落在本书范围上限、且全库有 7 章同为 10 块，**不构成偏离** | 通过（无偏离，故无需写理由行） |

### 断言组 · 阻断型（9 处 / 7 条独立错误）

| # | 断言（md 侧） | 证据（`text/ch27_27.txt`） | 结论 | 档位 |
|---|---|---|---|---|
| **A1** | 导航「人物弧线」：`Mel 全程不出场，却决定了这顿饭能喝什么、能听什么、能长什么样。` | char 6458–6711（line 119）：`Eulalia tried to order a carafe of wine but Callie said her dermatologist had told her to stop drinking for the sake of her complexion, so Eulalia had had to settle for a solo glass of Valpolicella while Callie daintily refrained and ordered a Limonata.` —— **挡酒的是 Callie**；Mel 在此段 0 出现 | **与原文不符**：Mel 未决定酒；「能喝什么」的决定权在 Callie。md 自相矛盾（同一篇导航「一句话概括」写的是「专辑、头套和面包**三种**开关」，无酒）；全书 `00_情感节点.md:82` 的正确版本已在案：`桌上只有两个人，第三个人从未露面，却握着专辑、头套和面包三种开关` | **阻断** |
| **A2** | 原句 6「读者视角提示」：`把 Mel 记下来：本章她一次都没出现，却决定了酒、专辑、头套和面包。` | 同 A1；Mel 在全章的 8 次出现（行 137,143,158,161,164,176,179,227）全部是对话或转述，**无一处是 Mel 的动作** | 同 A1（**同一错误第二处**）。修法：删「酒」字，与本篇导航「三种开关」及 `00_情感节点.md:82` 对齐 | **阻断** |
| **A3** | 导航「叙事手法」：`…而她对男人的那句评价（里面是玻璃做的一样脆），和她自己刚刚起步的那段关系形成反讽。`（「她」全链指 Callie） | char 6173–6394（line 110–116）：`‘No, Mr Polo. They’re easy to break. All bravado but their insides are fragile. Like they’re made of glass.’` / `‘I don’t doubt that you’ve broken a few hearts in your time.’ Callie picked up the menu.` / `‘A few skulls too.’` | **说话人错配**：`made of glass` 是 **Eulalia** 对 Callie 说的（针对「Mr Polo」这类男人）；Callie 的相邻台词只有 `I don’t doubt that you’ve broken a few hearts…`。末句「和她自己刚刚起步的那段关系形成反讽」也随说话人一起失据 | **阻断** |
| **A4** | 一句话总结：`那位从未露面的 Mel 在旁边握着专辑、头套和面包的开关` | char 4516–4540 / 4543–4588（line 71,74）：`‘Table for two, please.’` / `A waiter seated them to the side near the bar.`；`/usr/bin/grep -n "Mel" text/ch27_27.txt` → 8 行命中，退出码 0，全部是对话 | **与原文不符**：Mel 全程不在场；同一句前半「从未露面」与后半「在旁边」自相矛盾。读者可能读成「Mel 在餐桌旁」 | **阻断** |
| **A5** | 原句 2「为什么这样写」：`…还临时编了一套皮肤病学的理由把酒挡掉。` | char 6458–6711（line 119）只写 Callie **说了**这句话：`Callie said her dermatologist had told her to stop drinking…`，**无「编造」**；取证见下方「零命中取证」 | **与原文不符**：原文未判定这条理由真假，md 断言成「编」。`00_情感节点.md:82` 的写法是 `卡莉用一句"皮肤科医生的嘱咐"挡下那壶酒`（不判定真假） | **阻断** |
| **A6** | 原句 5「为什么这样写」：`Callie 用一个半真半假的健康理由替她挡掉` | 同 A5；`/usr/bin/grep -rn "dermatolog" text/` → **仅 1 处命中**（`text/ch27_27.txt:119`，即 Callie 说这句本身），退出码 0 | 同 A5（**同一错误第二处**）。原文未出现「半真半假」的依据 | **阻断** |
| **A7** | 原句 7「为什么这样写」：`酒被挡掉之后，桌上剩下的液体只有 Callie 亲手倒的水` | char 6458–6711（line 119）桌上仍有 `a solo glass of Valpolicella`（Eulalia）与 `a Limonata`（Callie）；char 11369–11412（line 197）后又有 `two limoncellos` | **与原文不符**：挡掉的只是整壶 carafe，桌上仍有酒与饮料。md 自相矛盾：原句 5 写「桌上只剩一杯酒」 | **阻断**（措辞级，一处可改） |
| **A8** | 原句 8「为什么这样写」：`作者用她接下来说的那句「我本来以为」后面的沉默，表明她的工作正被另一个人的意志推着走。` | char 9210–9330（line 158）：`‘I thought that was the plan?’ Callie was confused. Eulalia had said as much on their first meeting and Mel’s very clear brief had left them out.` | **与原文不符**：是**出声的反问** + 叙述层 `Callie was confused`，全段无「沉默」 | **阻断**（措辞级，一处可改） |
| **A9** | 原句 3「为什么这样写」：`一句话里塞进三种餐厅、三次提问和两个比喻` | char 3629–3955（line 68）该句实含 **8 个问号**（`How are you?` `Do you fancy Italian?` `maybe?` `better?` `What do you think?` `Are you a sushi person?` `aren’t you?` `Did you pop out of a clam fully formed?`） | **数字与原文不符**：「三种餐厅」✓（Italian / Korean barbecue / sushi），「三次提问」✗（8 个问号）。「两个比喻」可辩（Botticelli painting、pearly） | **阻断**（数字级；改「三次提问」为「一串提问」即可） |

### 断言组 · 提示型（措辞正当 / 记录不改）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| P1 | 导航「视角」：`她数着对方说话的停顿` | char 3323–16698 全段无此描写；Callie 对 Mel 的猜测在 char 7013–7070（`Callie assumed that Eulalia didn’t like her new producer.`） | 原文无此细节，「猜 Mel 的意图」成立、「数停顿」属添加 | 提示 |
| P2 | 原句 2 中文理解：`唱着自我了断` | char 2530–2796（line 62）：`She sang about trying to kill herself metaphorically, physically and emotionally.` | 「trying to」＝试图；「自我了断」读作已完成，译重了 | 提示 |
| P3 | 原句 9「读者视角提示」：`作者在本章里点破` | char 13132–13200（line 218）：`She didn’t think Eulalia’s behaviour was really about the limoncello…` | 主体是 Callie 的推测（`She didn’t think`），非叙述者断语 | 提示 |
| P4 | 原句 1 中文理解首句 `Caius 打电话来预告自己要晚归` | 引语起于 char 276，该句在 char 106–134（引语**前一句**） | 引语选短（S2 ①），主体内容仍在引语内 | 提示 |
| P5 | 原句 9 中文理解首句 `侍者送来两杯 limoncello…` | char 11369–11412，在引语（起 char 11506）**前一句** | 同 P4 | 提示 |
| P6 | 原句 6 中文理解首句 `Callie 问能不能先听一听那张专辑` | char 7496–7600（line 134）：`‘Would it be possible to hear the album? It might help me with my process.’` 在引语外 | 同 P4 | 提示 |
| P7 | 原句 2 引语截掉了同段前半（`It was about Julian of Norwich…`，char 2282–2313） | md 引语起于 char 2530 | 引语选短，与 L1 同源 | 提示 |
| P8 | 原句 5「为什么这样写」`Callie 用一个半真半假的健康理由替她挡掉` 中「替她挡掉」的方向 | char 6458–6711：`Eulalia tried to order a carafe… but Callie said…` | 归属方向（想点酒＝Eulalia、挡酒＝Callie）**写对了**，与本章专属判据一致 | 提示（此处正确，护栏） |

### 断言组 · 覆盖缺失（漏）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| L1 | md 覆盖了本章的中世纪—修女主线 | md 侧 `/usr/bin/grep -c`：`Julian`→0、`Norwich`→0、`Marie de France`→0、`修女`→0、`nun`→0（退出码 1＝无命中）；原文侧：char 1415–1790（情绪板/Marie de France/十三岁想当修女）、char 2282–2313（Julian 播客）、char 15808–16016（`‘Julian! I love Julian! Did you know that there was a mystic nun who was burnt at the stake not too far from here?’`）三处；跨章：`text/ch12_12.txt:134`（Eulalia 自称 Julian 的粉丝）、`text/ch36_36.txt:221`（提案板点名 `Marie de France … Julian of Norwich`） | **关键线索缺失**（ch12→ch27→ch36 的同一条线在 ch27 被整段剪掉），md 未写取舍理由 | **阻断** |
| L2 | md 覆盖了 Callie 对甲方关系的预期（她以为会被晾着） | 原文 char 3248–3569（line 62）：`She’d expected to be kept waiting, to be told that she was the lowly freelancer whose time wasn’t important. Callie wasn’t one for such power play and it seemed Eulalia wasn’t either.`；md 侧 `grep -c "kept waiting"` → 0 | 缺失；md 导航「人物弧线」（`从以为这是一次普通的甲方饭局，到看出自己正处在一个三人权力结构里`）的前提句没进正文 | **阻断** |
| L3 | md 覆盖了「Callie 脑中闪过 Eulalia 会走到迎面来的车前」 | 原文 char 12828–12904（line 209）：`…she was gripped by a vision of Eulalia stepping in front of an oncoming car.`；md 侧 `grep -c "oncoming"` → 0 | 漏一笔强烈意象（md 只收了同段的 £60 现金） | 提示 |
| L4 | md 收了孕吐线索 | 原文 char 2530 段内 `…when the nausea allowed.`、char 16120–16144（line 296）`the nausea was returning.` | md 仅在导航写「可能怀孕」，正文未收 | 提示 |
| L5 | md 引用了「两人桌」的决定性证据 | 原文 char 4516–4540：`‘Table for two, please.’`；md 侧 `grep -c "Table for two"` → 0 | 结论（两人、Mel 不在场）已在原句 7 提示中以「倒了两杯，不是三杯」出现，但**缺原文锚点**；本章专属判据要求的正是这句 | 提示 |

---

## 三、零命中取证（R5-补：凡「查无」必须贴命令、输出、退出码）

```
/usr/bin/grep -rn "dermatolog" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/
→ text/ch27_27.txt:119（唯一命中，就是 Callie 说这句本身）
退出码 0
```
⇒ 全书 54 章无任何旁证支持 A5/A6 的「编造／半真半假」。

```
/usr/bin/grep -n "Mel" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch27_27.txt
→ 行 137,143,158,161,164,176,179,227（8 行命中，全部是对话或转述）
退出码 0
```
⇒ Mel 在本章**零动作描写**，A1/A2/A4 的「Mel 决定酒 / Mel 在旁边」不成立。

```
/usr/bin/grep -c "Julian" "notes/…/ch27 callie has dinner with eulalia.md"   → 0（退出码 1）
/usr/bin/grep -c "Norwich" 同上                                            → 0
/usr/bin/grep -c "Marie de France" 同上                                     → 0
/usr/bin/grep -c "修女" 同上                                                 → 0
/usr/bin/grep -c "Table for two" 同上                                       → 0
/usr/bin/grep -c "kept waiting" 同上                                        → 0
/usr/bin/grep -c "oncoming" 同上                                            → 0
```

```
/usr/bin/grep -rn "Julian" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ | wc -l
→ 5（ch12:134、ch27:62、ch27:284、ch27:287、ch36:221）
```

---

## 四、已核实为正确（防误修；后续任何人不得以「读着不对」为由改动，除非给出反证）

1. **原句 7 读者视角提示「注意她倒了两杯，不是三杯——Mel 在这顿饭里连一只杯子都没有」** —— 正确。原文 char 8028–8068：`Callie poured them each a glass of water from the tiny jug on the table.`（them＝Callie＋Eulalia）；char 4516–4540：`‘Table for two, please.’`。
2. **原句 5「桌上只剩一杯酒」** —— 正确。char 6458–6711：`so Eulalia had had to settle for a solo glass of Valpolicella`（被取消的是 carafe，不是这一杯）。
3. **原句 5 的归属方向「Eulalia 想点酒、Callie 挡下、Callie 点 Limonata」** —— 与原文一致，是本章专属判据（谁在给谁斟酒）的正确答案。
4. **导航「线索结构」中 Mel 的三项开关「否决放专辑、改了头套方案、不许吃面包」** —— 三处逐字对得上：char 7977–8010（`I don’t think Mel would like that.`）、char 9358–9437（`Mel is now saying that the label’s plan…`）、char 10426–10454（`Mel says I can’t eat bread.`）。问题只在把「酒」也算成第四项。
5. **导航「可能怀孕的帽匠 Callie」** —— 正确。帽匠：`text/xx_characters.txt:26` `CALLIE … is a milliner by trade.`；怀孕：本章 char 500 附近 `when the baby is a toddler`、`we’ll be pretty good parents`。
6. **导航「分部 A WEDNESDAY IN MAY」** —— 正确。本章 char 4590–4625（line 74）：`It was pretty busy for a Wednesday.`；本书 ch21、ch26 同属「WEDNESDAY IN MAY」分部，ch28、ch30 属「THURSDAY IN MAY」，一致。
7. **原句 9「Callie 点了点头——这本是有礼貌的做法」** —— 正确。char 11506–11552：`Callie nodded; that was the polite thing to do, after all.`
8. **原句 10「Eulalia 在路边朝她挥手」「把地址报给司机」「从后座给 Caius 发短信说有点怪」** —— 正确。char 16679–17032 逐字：`She opened the door of the cab, and got into the back as she gave the driver her address. Eulalia waved at her from the pavement as she texted Caius from the back of the cab that Eulalia was kind of weird.`
9. **原句 10「Callie 用『有点怪』这种最省力的说法，把一整晚没法归类的感受打包发回给 Caius」** —— 与原文一致，不是复述字面（有「为什么」），密度达标。
10. **词汇表 30 条例句** —— 全部逐字命中原文，每条恰好 1 次（脚本复核）；词档分层未发现注水（bread / waiter / bill / cab / pavement 在 ⭐ 基础，detachedness / speculative / conspirative intimacy 在 ⭐⭐⭐ 合理）。

---

## 五、覆盖声明

- **本次审查范围：仅第 27 章**（独立审查员指派），R1→R5 全跑（素读 → 机器层 → 三张单子 → 逐块对应 → 判定表）。
- 机器层：`bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch27 callie has dinner with eulalia" --json` → **退出码 0**，`verdict: ok`，引语 10/10 `ok`，`struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0`；形态 4 项全部合规。原始输出见同目录 `2-machine.json`。
- **全书其余 53 章：只有机器层，未做人判** —— 不得记作「通过」。
- 本次未审 `00_概述.md` / `00_金句精选.md` / `00_情感节点.md` 的全部断言（仅在需要反证时引用了 `00_情感节点.md:82` 作为**正确版本**的对照）。
- 机器全绿但人判出 9 处阻断：全部落在「覆盖 / 施事归属 / 说话人 / 人物动机断言 / 数字计数」五类，**四道机器探针结构上查不了**（引语逐字、中文是中文、关键词成立、形态正常——这 9 条一条都没被触发）。与 `docs/rules/审查表.md` §0.5「不许用机器全绿推出缺陷都在摘要层」一致。

---

## 六、最要紧的一条

**A1/A2：md 把「酒」的决定权归给了 Mel，而挡酒的是 Callie 自己。**
证据：`text/ch27_27.txt:119`（char 6458–6711）`Eulalia tried to order a carafe of wine but Callie said her dermatologist had told her to stop drinking… so Eulalia had had to settle for a solo glass of Valpolicella while Callie daintily refrained and ordered a Limonata.`；`/usr/bin/grep -n "Mel" text/ch27_27.txt` → 8 行命中全部是对话/转述，Mel 无任何动作。
为什么最要紧：① 它正是本章专属判据要核的「谁在给谁斟酒、Mel 在旁边做什么」，而答案是「Mel 不在场，斟水的是 Callie」；② 它出现在**读者最常看的两处**（导航「人物弧线」＋原句 6「读者视角提示」）；③ 它与 md 自己的导航「一句话概括」（`专辑、头套和面包三种开关`）**自相矛盾**，也与全书 `00_情感节点.md:82` 的正确表述（`桌上只有两个人，第三个人从未露面，却握着专辑、头套和面包三种开关`）相抵触——正确版本现成，改两处即可对齐。
修法：导航「人物弧线」改为「Mel 全程不出场，却决定了这顿饭能听什么、能长什么样、能吃什么」；原句 6 提示删掉「酒」字。
