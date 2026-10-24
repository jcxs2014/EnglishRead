# ch09 No Place Like Home — 对账（R3）

素读：`1-suread.json`（8 条，锚点脚本核对 8/8 命中）
机器层：`2-machine.json`，rc=0，verdict=ok，6 块 / 1818 words / segments 8 / 查无 0 / 空引号 0 / 子项缺 0 / 关键词缺 0 / 形态偏离 0；`block_target [3,6]`、`issues` 全空
精读：`ch09 no place like home.md`（109 行，6 个引语块）

## 一、漏（素读有 / md 无）

| # | 素读条目 | 原文（text/ch09_no_place_like_home.txt） | md 对应 | 判 |
|---|---|---|---|---|
| L1 | 第 2 条：Zach 关于「为何不告家人」的整段独白（婚礼前几周），核心三句——「我不是羞于示人，恰恰相反，是我把这事搞砸了」、「我时不时让他们知道我还活着，再多说只会助长他们」、妹妹们在 **Tulsa**、父母连他**改了姓**都不知道 | 42: “I mean, I’m not ashamed of you. Quite the opposite. I’ve screwed this up.”　34: “I let them know I’m alive every now and then. Anything more than that would just encourage them.”　43: “I wish they could come, though. I just can’t figure out how we’d get them up here from Tulsa safely… my parents don’t even know I changed my name.” | 无块（6 块里没有这段）；导航 :14 只压缩成 5 条理由（先见谁／疫情／父亲站另一边／母亲难过／妹妹要保密）。`grep -nF "ashamed"`／`"Tulsa"`／`"changed my name"` → 各零命中，退出码 1 | 提示：非情节缺失（理由在导航里），但**「不是羞于你」这一层是本章对 Zach 的定性**，且是他篇幅最长的一段话，一笔未落；建议并入导航一句 |
| L2 | 第 4 条：婚礼当天全员戴口罩（疫情又起）；到场名单（Caralora 的伴 **Miriam**、David 与 Nancy **Kendrick** 带儿子 Colin、互助组织的朋友）；缺席者 Nadia、Nick、Kimy、祖父 | 62: “We are all wearing masks because the pandemic is surging again.”　62–63: “…Caralora and her date, Miriam; Celia and Lucinda… David and Nancy Kendrick, with their son, Colin.”　63: “How I miss Nadia today, and Nick, too. I wish Kimy and my grandfather could be here.” | 全缺。`grep -nF "口罩"`／`"Miriam"`／`"Kendrick"`／`"Nadia"` → 各零命中，退出码 1；导航 :11 只写「朋友」 | 提示：名单属长名单，可只列两三组；但「全员戴口罩」是 2025 年设定的外部标记（与 opening 的「the conflict」同级），一个词都没有，疫情这层背景在整章失重 |
| L3 | 第 7 条：Zach 撞见她站在一道**梯形阳光**里、闭眼张臂、一手小提琴一手琴弓，「她第一次像是属于这所房子」；婚礼上她**几乎一直握着他的手，像拿他当压舱物** | 103: “I saw Alba standing in a trapezoidal band of sunlight, her eyes closed, arms outstretched, her violin in one hand, bow in the other… For the first time, Alba seemed to belong in the house”　108: “Alba held my hand almost continuously, as though she were using me as ballast.” | 全缺。`grep -nF "阳光"`／`"小提琴"`／`"压舱"` → 各零命中，退出码 1；导航 :14 只写到「他注意到 Alba 一直看后门」 | 提示：「属于这所房子」是本章「home」主题唯一由 Zach 视角给出的实证，无块亦无导航；「ballast」也是全章最好的一个比喻 |

## 二、编（md 有 / 原文无）

| # | md 断言 | 原文 | 判 |
|---|---|---|---|
| — | 未发现凭空出现的情节、关系、数字 | — | 无 |

## 三、错（两边都有 / 不一致）

| # | md 断言 | 原文逐字 | 判 |
|---|---|---|---|
| E1 | :13「新家**最显眼的一件家具**是前任房主去世的**那张床**，被扔掉了」 | 131: “Alba insisted that we throw out Beatrice’s **mattress** (Zach, she died on it!)”…“we are left with all her Heywood-Wakefield furniture that her family inexplicably didn’t want” | 提示：扔掉的是**床垫**（md :11 写对了，:13 滑成「床」）；且「最显眼的一件家具」与原文相反——留下的家具几乎全是 Beatrice 的（床架也在内），只有床垫被丢 |
| E2 | :14「Alba 在这一章**几乎没有推动任何事**，她做的动作只有等」 | 29: “A few weeks before the wedding **I asked him**, ‘Do you think you’ll ever contact your family again?’”；57: “**I let my mother and Beck take me shopping**”；131: “**Alba insisted** that we throw out Beatrice’s mattress” | 提示：本章她至少三次主动发起（问家人、允母亲与 Beck 置装、坚持扔床垫），同段末尾也承认了后两件，前后略打架；属程度措辞，非事实错误 |

## 四、R4 逐块对应（人判）

| 块 | 引语 | 中文是否在讲这句 | 三问 | 判 |
|---|---|---|---|---|
| 1 | 23 行 结婚／家人不来／没告诉 | 是 | 主语＝Zach 与 I（结婚）／His family（不来）／Zach（没说）；受事＝婚礼、家人；「没告诉」升级为「家里不知道他在跟谁交往」在导航，未误把「不来」写成「被拒绝」 | 通过 |
| 2 | 68 行 万一爸爸出现／wishful thinking／unthink | 是 | 主语＝她（想）；受事＝父亲与那个念头；md「她自己先给这个念头定了性」归属正确（I know it's wishful thinking 是她自评） | 通过 |
| 3 | 82 行 戴戒指／他戴／她收抽屉／时间旅行会丢 | 是 | 主语＝Zach（戴）／I（戴、收）；受事＝戒指；「第一次时间旅行」未被译成「有一天」 | 通过 |
| 4 | 89–90 行 那天很美／希望他在／太奢求／把悲伤搁一边／活在当下 | 是（两段引语：:89 与 :90） | 主语＝她（想、问自己）；受事＝父亲（希望他在）与「当下」；md 未把「too much to expect」的主语误挂成 Zach | 通过 |
| 5 | 118 行 图吉利／门槛危险／怕恶魔进来 | 是 | 主语＝Zach（说、抱）；受事＝她／门槛；「demons getting in」方向＝进门，md「怕恶魔跟着进来」正确，未写成「把恶魔关在外面」 | 通过 |
| 6 | 148–149 行 Home, sweet home／the sweetness／we are home | 是 | 主语＝Zach（说、感到）；受事＝那份甜；md 点明「同一句俗话被第二个人重复时才成真」，未越到全书主旨 | 通过 |

> 密度：6 块均咬住句法（分号、定冠词、现在完成时、will/since、into 的方向），仅块 1 的「读者视角提示」略泛。

## 五、已核实为正确（防下一轮误修）

1. **「Clare 和 Beck」= Alba 的母亲与继父**：`:99` “it was a wedding present from **Clare and Beck**”；md :11 用「Clare 和 Beck」而未误写成「Mama 和 Beck」（正文别处称 Mama）——不矛盾，Clare 即 Mama 的名字。
2. **年龄线**：`:18` “Saturday, August 2, 2025 (**Alba is 23, Zach is 24**)”；与 ch07（22/23）、ch08（23/23）自洽（跨年＋生日差）；md 未写年龄，故未与 ch06 的 `Alba is 42` 打架。
3. **「九十六岁」**：`:99` “had died in her bed, at the age of **ninety-six**”；md :11「九十六岁」正确。
4. **戒指的归属方向**：`:82` “Zach slides a wedding band onto my finger, then I slip his ring onto his finger.”；md :41「他把婚戒套上她的手指，她把他的戒指套上他的」——两个方向都对，未互换。
5. **11 条词汇例句**：脚本逐条整串命中（`rows=11 miss=0`），含 `inconspicuous`（:85 原句）、`ordained`（:94 原句）、`split-level`（:88 原句）、`coral lipstick`（:105 原句）。
6. **「A Kiss to Build a Dream On」/「Wouldn't It Be Nice」/「Pet Sounds」**：`:73`／`:89` 原文；md :12／:51 引用无误，未串成别的曲名。
7. **门槛迷信的方向**：`:118` “for fear of **demons getting in**”；md :65「恶魔要防的方向也交代得清楚：门里」，与原文一致。
8. **「we are home」是叙述而非对白**：`:149` “After a while, we go inside, to bed, and we are home.”；md :71 处理为「收在一句陈述上」，未加引号，正确。
