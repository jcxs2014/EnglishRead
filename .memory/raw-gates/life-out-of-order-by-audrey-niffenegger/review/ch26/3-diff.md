# ch26 对账（漏 / 编 / 错）

原文：`text/ch26_celia_says.txt`；精读：`ch26 celia says.md`（89 行，4 块）。

判定口径：R3 三张单。**漏**＝素读有、md 无，且属关键事件/转折；**编**＝md 有、原文无；**错**＝两边都有但不一致。md 已在「本章导航·一句话概括」与「一句话总结」两处做了压缩取舍的，按「有覆盖」计，最多到提示级。

---

## 一、漏（md 无）

| 编号 | 素读条目 | 原文（逐字） | md 侧核查 | 档 |
|---|---|---|---|---|
| L1 | Celia 直接表白「I love you. Why don't you love me?」与 Clare 的回答「I do love you. But not the way you want to be loved.」——这是本章的摊牌顶点，**没有任何一块引它** | `:93`「She tries again. “Clare? I love you. Why don’t you love me?”」；`:97`「“I do love you. But not the way you want to be loved.”」 | `grep -c -F "I love you" ch26 celia says.md` → 0；`"not the way you want"` → 0。但「一句话总结」`:89` 写「为什么你爱的是 Beck，不是我」「Clare 只能承认自己爱她，却不是她要的那种爱」，语义已覆盖 | 提示（覆盖在总结，块内无） |
| L2 | Henry 的**遗言**被 Celia 提起、又被 Clare 一句打断：`"his last words were—"` / `"Enough, Celia."`——本章唯一的悬念钩子 | `:181`「“But Henry would never have left you. I mean, his last words were—”」；`:185`「“Enough, Celia.”」 | `grep -c -F "last words"` → 0；导航 `:12` 只写「话擦到 Henry 的遗言时绷紧」，总结 `:89` 写「提到 Henry 时两人都停住」——**事件在、遗言这个钩子没写出是什么** | 提示 |
| L3 | Clare 给 Beck 的定性只有一个词：「She's restful.」，Celia 立刻拿 Henry 反驳「Henry sure wasn't restful」 | `:111`「“She’s restful.”」；`:115`「“You don’t really go for restful! Henry sure wasn’t restful. Really, Clare, what?”」 | `grep -c -F "restful"` → 0，全 md 无此词 | 提示（Beck 的性格定义整段缺失） |
| L4 | Celia 的情史：她爱过 Ingrid，而 Ingrid 爱的是 Henry、后来自杀——这是「她为什么等了这么久」的唯一解释，且原文就长在 md 原句 3 的同一段里 | `:102`「Celia has had bad luck with love. Celia loved Ingrid, who loved Henry and then killed herself.」 | md 原句 3 从「I love Henry」起引，正好切掉这句；md 全文 `grep -c -F "Ingrid"` → 0 | 提示（引语起点截短所致，非整段取舍） |
| L5 | 邻桌白人老妇皱眉、Celia 甜声回敬「Ain't they got any lesbians where you're from?」——本章唯一的公开场合张力，也是「握手」真正发生的位置 | `:193`「I slide my hand across the table and Celia takes it. An elderly white woman two tables over frowns at us. Celia smiles at her and says sweetly, “Ain’t they got any lesbians where you’re from?”」 | `grep -c -F "Ain’t they got"` → 0；`"frowns"` → 0 | 提示 |
| L6 | 香槟的祝词是「To the next Jane Addams」，把 Celia 的社工身份接到芝加哥传统上 | `:29`「“To the next Jane Addams,” I say as we touch glasses.」 | `grep -c -F "Jane Addams"` → 0；md 只说「庆她拿到社工执照」 | 提示 |
| L7 | Celia 只在上周 Charisse 生日会见过 Beck 一次，却对 Clare 的近况知道得比她讲过的多 | `:38`「Celia seems to know more than I’ve told her about my recent encounters with Beck, even though Celia’s only met Beck once, at Charisse’s birthday party last week.」 | `grep -c -F "Charisse"` → 0 | 提示 |
| L8 | 收束句「If it can't be me, then Beck seems all right.」 | `:213`「“Seriously for a minute, Clare,” Celia says, her hand on my bare arm. “If it can’t be me, then Beck seems all right.”」 | `grep -c -F "If it can’t be me"` → 0；总结 `:89`「临别 Celia 说 Beck 看着还行」已覆盖 | 提示 |

> L1 未判阻断的理由：作业单要求「关键事件/转折未进**任何一块或导航**」。此处虽未进块，但进了「一句话总结」的概括，读者不会不知道摊牌发生过；按「md 已写明取舍（压缩到总结）」处理。

## 二、编（md 有、原文无）

无。逐条核过 md 的每一处事实性断言，均能在原文找到出处：

- 「满桌辣酱」→ `:23`「There are so many kinds of hot sauce on the table there’s hardly room for place mats.」
- 「吵闹的餐厅」→ `:23`「we have to shout-talk at each other to be heard」
- 「人散后的安静」→ `:38`「The place becomes quieter as the lunch crowd leaves.」
- 「种族、身高、性向一一试过」→ `:123` / `:139` / `:143`（身高那句 `Maybe if I were taller?` 确为 Celia 自嘲）
- 「黄铜大理石大堂」→ `:208`「the cool brass and marble lobby」

## 三、错（两边都有、不一致）

| 编号 | 断言 | 原文（逐字） | 错在哪 | 档 |
|---|---|---|---|---|
| E1 | 导航 `:11`「临别两人握手、拥抱，各自走开」 | 握手在 `:193`「I slide my hand across the table and Celia takes it.」（吃馅饼 `:208` **之前**，是中段）；临别只有拥抱 `:221`「Celia reaches up to hug me」 | 把中段的「握手」并到「临别」，时序错位 | 提示 |
| E2 | 原句 2 引语以「“There's all kinds of love」开头 | `:75`「Celia regards me over her half-glasses. “Clare. There’s all kinds of love: eros, philia, agape, ludus…」 | 引语丢掉呼语「Clare.」，却仍以引号开头，读起来像完整发言 | 提示 |

## 四、块序核对

原句 1（`:23`）→ 原句 2（`:75`）→ 原句 3（`:102`）→ 原句 4（`:221`），单调递增，**无倒置**。
