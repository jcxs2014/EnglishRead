# ch09（书内 Chapter Eight）深审 R3/R4 三张单子

素读基线：`review/ch09/1-suread.json`（45 条事实／0 MISS，只读 `text/ch09_chapter_eight.txt`，写完才开 md）
机器层：`review/ch09/2-machine.json` → verdict `ok`（blocks 3 ∈ target [2,3]；segments 3／MISS 0；words 1108）
直撇号探针：`/tmp/apos.txt` 未列 ch09 ⇒ 0 站
词表：17 行例句展平逐字比对 **0 MISS**（脚本见本卷「已核实为正确」）
本章为短篇章（1108 词／3 块），承重信息全在导航五句 ⇒ 人判重点按 ch07 的做法移到 md:10–md:14。

## 🟥 阻断（7）

### C-09-1 认知对冲被抹平＋评价凭空：「本是 Aunt Virginia 的好意」
- md:10：**「篮里的浴球和茉莉香本是 Aunt Virginia 的好意」**
- 原文逐字：`text/ch09_chapter_eight.txt:24` — `Aunt Virginia’s doing, probably.`
- 判定：原文给的是**推测**（probably），md 写成已然（「本是」）；「好意」是原文没有的评价词——原文只说那是 Virginia 放的，紧接着 :27 房子起电嗡、:30 香气转酸，这一段的功能是**铺垫善意与变质之间的落差**，把「probably」钉死等于替读者提前结账。改法：「篮里的浴球与茉莉香，她**猜**是 Aunt Virginia 放的」。

### C-09-2 跨章「第一次」断言有反例
- md:11：**「本章是 Dart 第一次不靠正面追问、而靠操纵印象取得与 Gazzie 的相处时间」**；末节 **一句话总结**同调重复一次：**「而 Dart 第一次不再正面追问」**
- 反例逐字：`text/ch06_chapter_five.txt:228` — `After a glance at Gazzie to make sure she was listening, I added, “But I would love to learn.”`；紧接 :240 `Gazzie spoke without looking up… “Have you ever even seen an alligator?”`、:279 `The full fury of Gazzie’s attention returned to me.`
- 取证：`/usr/bin/grep -inE "redeem|distract(her|ing her)|make a good impression|flatter" text/ch0[1-8]*.txt` → 无命中（rc=1），但 ch06:228 已是一次**为了被 Gazzie 听见而调整自己说法**的动作，且确实换来 Gazzie 的注意力——「第一次」不成立。
- 改法：把「第一次」限定到本章真正新出的那张牌——「本章她第一次把手里唯一那条提示当工具用出去」（对照 md:13 已有「把 Virginia 的 tip 当工具用出去」，删掉「第一次…取得相处时间」的跨书首创判定即可）。

### C-09-3 章内情绪时序写反：「尖叫之后立刻叠上羞耻」
- md:11：**「尖叫之后立刻叠上羞耻（怕被看作白痴）与二次紧张（对着刀解释）」**
- 原文逐字：`text/ch09_chapter_eight.txt:63` — `“I don’t know.” Irritation shot through me. How dare she yell at me when I was terrified like this.` → `:69` — `My cheeks heated, and I bowed my head… my grandmother considered me more of an idiot than she had before.`
- 判定：第一拍是**被吼的怒火**（:63），羞耻在其后（:69）；「立刻叠上羞耻」把两拍合并并把顺序倒过来。本库缺陷簇第一名即章内时序，此处正是典型。改法：「尖叫之后先是挨吼的恼（:63），随后才叠上羞耻（怕被看作白痴）与二次紧张（对着刀解释）」。

### C-09-4 一次性事实被常态化：「睡眠浅且随身有刀」
- md:13：**「本章给出的 Gazzie：睡眠浅且随身有刀」**
- 原文逐字：`text/ch09_chapter_eight.txt:96` — `“Lucky for you,” she said, making her way out of the bathroom, “I was already awake.”`；`:54` — `Gazzie stood in the bedroom doorway, wearing a chartreuse collared PJ set. An object glinted in her hand—a knife.`
- 判定：原文只给**这一次**她已醒着（一句自述），以及**这一次**手里有刀；刀从哪来、平日是否带刀、她的睡眠习惯，本章均无。「睡眠浅」「随身」把单次场景升级成人物属性，属归属／常态断言。改法：「本章给出的 Gazzie：这时已醒着、进门时手里拿着一把刀（本章未写刀从何来）」。

### C-09-5 已出场写成未出场：「后面它真出场时」
- md:52（block 3 读者视角提示）：**「Ironheart 是谁、与 Gazzie 或 Greer 家是什么关系，本章一字未给……后面它真出场时，别拿本章这个反应替它提前定性。」**
- 反例逐字：`text/ch05_chapter_four.txt:135` — `“Ironheart, Dart. Dart, Ironheart. Personally, I wouldn’t greet visitors with a dinosaur skin, but Gazzie said it was either the gator or the portrait…”`；`:141` — `Ironheart was the first gator our family shot in the Victorian era. Kicked off the whole business.`；`text/ch06_chapter_five.txt:363` — `Aunt Virginia had implied that asking Gazzie about it might help me bond with her…`
- 判定：「本章一字未给」限定在本章，字面成立；但同一句的**「后面它真出场时」**向读者宣布 Ironheart 尚未出场——它早在 ch05（书内 Chapter Four）就以鳄鱼皮形态被 Virginia 当面介绍、并给了「家族在 Victorian era 射杀的第一条」这一定义，md:10 自己写的「浴缸黄铜脚做成鳄鱼爪」之前的门厅那张皮就是它。**「与谁的关系本章未写」是对的，「尚未出场」是错的。**改法：「Ironheart 的本章之外的信息在 ch05 已给（门厅那张皮＝家族射杀的第一条鳄鱼）；本章只给出 Gazzie 听到名字后的动作，别拿它替 Ironheart 提前定性」。

### C-09-6 承重信息缺失：Ironheart 这一计为何奏效- md:10／md:13／md:52 三处都只写「甩出／用出 Virginia 的提示」，本章**没有一句**交代这计成立的机制。
- 原文逐字：`text/ch09_chapter_eight.txt:120` — `“Go back to bed,” she ordered, dismissing me with a flick of her hand, like I was just an employee on her farm. Except she treated them with more respect than she did me. Anything alligator-related got her attention.`
- 判定：`Anything alligator-related got her attention.` 是本章的因果扣——它同时解释了 :126「停住、像在读什么信号」和 :129 的点头，也是 md:13「从『问』转成『演』」这条动作线之所以成立的唯一依据；md:10 结尾只留了「另：Aunt Virginia 有时睡在 carriage house」这条次要信息，却漏掉了它。按「漏＝整块信息单元缺失」判阻断。改法：在 md:10 的「甩出提示」前插入「（前一句刚写明：凡是鳄鱼相关的事都能引起她的注意）」，并在 md:13 补上这条机制。

### C-09-7 章末位置写错＋末拍缺失：「结尾停在『make yourself decent first』」
- md:14：**「结尾停在『make yourself decent first』，夜谈的内容本章没有给出。」**；md:10 收在 **「……随后答应，条件是先把自己收拾体面」**
- 原文逐字：本章最后一行 `text/ch09_chapter_eight.txt:132` — `Pulling down the hem of my sleep tee, I agreed.`（:129 才是 `Fine. But make yourself decent first.`）
- 判定：章**不停在** Gazzie 的条件句上，而停在 Dart 用动作（拉下睡衫下摆）把那条条件立刻执行掉、并说「我同意」——收束的主语是她。md 把结尾位置记错，同时漏掉本章最后一个信息单元：Dart 对「收拾体面」的即时候命。改法：「结尾停在 Dart 拉下睡衫下摆、答应照办（:132）；夜谈的内容本章没有给出」。

## 🟡 提示（7）

- **T-09-1**「不留护卫」的「护卫」概念全章无出处：md:12「屋主之一持刀而来却不留护卫」。取证：`/usr/bin/grep -inE "guard|protector|watchman|deputy|armed" text/ch09_chapter_eight.txt` → 0 命中（rc=1）。可回溯的事实只有 :54 持刀进屋、:84 检查后 `Nope. No one here.`、:96 自己走出浴室。建议改「检查后便独自离开」。
- **T-09-2**「屋主之一」本章无产权表述：本章仅给 :75（Virginia 有时睡 carriage house）与 :126（Gazzie 有 her suite）；`grep -inE "own(s|ed)? Greer House"` 全库命中 1 处且在**后文** `text/ch16_chapter_fifteen.txt:132` — `It was hard to imagine a time when Gazzie didn’t own Greer House.`。建议本章改「住在同一屋檐下的祖母」，或注明依据在后文。
- **T-09-3** eager 的触发点被前移：md:13「听到『有人』时神情转为近乎 eager」。原文 :57 说「There's someone in there」后 :60-66 她是 `What?`／`Who?`／ raised her eyebrows；eagerness 出现在 :78 — `To my surprise, Gazzie’s expression changed to something approaching eagerness.`，其直接前因是 :75 她要求「tell me exactly what you saw」之后的结巴复述（:81）。建议「听完她含混的复述后，神情转为近乎 eager」。
- **T-09-4** 漏 `text/ch09_chapter_eight.txt:45` 第二句 — `Her lips parted, like she was about to speak.`：恐怖峰少一拍，而 md:14 的「分辨率递进」链条（breath caught→只写眼睛→锁定）恰好在这一句后收口；建议补进 md:10 与 md:14。
- **T-09-5** 漏 `:27` — `Then the house’s faint electric hum began, and with it came a sense of unease. I groaned. Maybe Aunt Virginia would let me call a handyman. I couldn’t live like this for an entire month.`：取证 `/usr/bin/grep -nE "电|一个月|handyman" "ch09 woman in the bathwater.md"` → 0 命中。这条不只是氛围——:81  Dart 复述时把「the electricity was doing that buzzing thing」列为原因之一，md 里没给这条线索留位置，读者无从对接。
- **T-09-6** 漏 `:30` 末 — `I hadn’t known bath bombs went bad.`：与 T-09-1 的「香气转酸」同段，md:14 写了「茉莉香转酸」却没写她把原因归给浴球变质这个自我解释（正是它把叙述者暂时安在「讲理」一侧，随后才被 :36 推翻）。
- **T-09-7** 漏 `:9` 末 — `Outside, night birds whistled amid a chorus of crickets.`：md:10 的声音清单只留「地基呻吟与水管奔流」，本章「异响清单」少一项夜声；轻。

## ⬜ 判为假红／不报警（6）

- **F-09-1** block1「推她的人没有面孔，文本只给出方向和『边缘』这一条线」——:12 引语段内确实只给 feet／shore／a hand／edge；紧随的 :15 给出 `the person behind me` 与 `her`（性别）但没有面孔。**表述正确。**
- **F-09-2** block2「显形的介质不是镜子而是浴水」——:30 `shut off the faucet and studied the water’s surface` 在前，成立。
- **F-09-3** md:14「对视之后用第二人称把私人恐惧普世化」——:39 `…the worst dream you’ve ever had, one you think you’ve woken up from…` 确为 you 第二人称，引文与原文对应。
- **F-09-4** md:14「夜谈的内容本章没有给出」——本章止于 :129 `Fine. But make yourself decent first.`，成立（夜谈本体在 ch10）。
- **F-09-5** md:46「『the one tip』给 Virginia 的情报标上数量极限」——数量极限来自原文 :123 `the one tip`，非我方造出的跨章计数，不报。
- **F-09-6** md:10「随后露出威胁性的笑」——:45 `the woman’s mouth formed a menacing smile` 在前，`Her lips parted` 在后；md 只是没写后一句（已计入 T-09-4），顺序未写反，不另报阻断。
- **另**：快审已记的 ch05「最近／最远窗」等提示、ch06「长回来的孙女」译法不在本章范围，未重复报警。

## 逐块对应（R4）

- block1（:12）关键词 gasping／scribbled／grassy shore／black water——四条均在引语内 ✓；中文理解逐句对应 ✓；「惊醒三件套（喘气、湿透、寒战）」逐字对 `woke up gasping`／`Sweat soaked my sleep tee`／`Shivering` ✓。
- block2（:36）关键词 reflection／stranger／blurry／pulled back ✓；「先立常识…再让常识被他人占据」对应 `Where my reflection should have been was a stranger` ✓；「整体 blurry→头发勉强可辨→眼睛高清」的分辨率顺序与原文一致 ✓；读者视角提示「这一段之前她先在雾镜里看过自己」对 :24，位置正确 ✓。
- block3（:123）关键词 clicked into place／bonding／tip／Ironheart ✓；「段落却不讳言动机是挽回『像个白痴』的印象」对 :111 `I couldn’t let her leave thinking I was an airhead… to redeem myself` ✓；「停住、头偏向一边、过了一会儿才答应」对 :126／:129 ✓（`head tilted to the left` 的「左」在 md:13 也已给出）。
- 本章无对话密集块、无 cliffhanger 收尾（收在应允），md:14「结尾停在『make yourself decent first』」为全章最后一句 ✓。
