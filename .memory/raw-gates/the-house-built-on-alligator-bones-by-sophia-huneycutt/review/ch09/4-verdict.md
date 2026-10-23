# ch09 深审判定表（R5）

章：`ch09 woman in the bathwater.md`（书内 Chapter Eight，H1 `# 09. Chapter Eight` ✓）
语料：`text/ch09_chapter_eight.txt`（132 行／6,447 B）
流程：R1 素读（45 条事实／0 MISS）→ R2 机器层（verdict `ok`）→ R3/R4 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 3／分片 3／MISS 0；无 `…` 拼接块；词表 17 行例句展平逐字 **0 MISS**；直撇号 0 站 | 🟢 全绿 |
| 对应 | 3 块 anchor 全在素读表内；缺项：:120 后半（机制句）、:132（末拍）、:45 第二句、:27、:30 末句、:9 夜声 | 🟠 阻断 3（C-09-6／C-09-7／T-09-5 归漏）＋提示 4 |
| 形态 | nav 5 项 ✓／子项四项 ✓／blocks 3 ∈ [2,3] ✓／words 1108／struct_bad 0 | 🟢 全绿 |
| 断言 | 认知对冲／跨章首次／情绪时序／单次事实常态化／已出场写成未出场 | 🔴 阻断 4（C-09-1／C-09-2／C-09-3／C-09-5）＋提示 3 |

**本章合计：阻断 7 ／ 提示 7 ／ 假红-不报 6**

## 缺陷形态归因

- **短篇章＝导航层集中出错**（同 ch07 的 5/7）：1108 词、3 块，承重判读全挤在 md:10–md:14 五句里，本章 7 条阻断有 5 条落在 md:10／md:11／md:14；块层（3 块）反而几乎全对——只有 block3 的读者视角提示带出一条跨章错（C-09-5）。⇒ 规则建议复述：**章越短，人判越要往导航五句挪，块层抽验可以放宽。**
- **`probably`／`I think`／`like` 这类对冲词被中文层钉死**（C-09-1）：与 ch08「想象中的红顶谷仓被复数化」、ch07「门外裁决」同族——叙述者的不确定被写成已然。
- **单次事实 → 人物属性**（C-09-4）：`I was already awake` ＋ 此刻一把刀 ⇒ 「睡眠浅且随身有刀」。本类在导航层的「本章给出的 X：…」句式里最易发生，该句式本身就是「归纳成人物属性」的授权，需逐条回查是否只发生一次。
- **跨章「第一次／唯一一次」**（C-09-2）：必须先枚举前章同型动作再落笔；本章取证方式＝`grep -inE "redeem|distract|impression|flatter" text/ch0[1-8]*.txt`（0 命中）＋通读 ch06 的 Gazzie 台词行（34 处，找到 :228 反例）。**关键词 0 命中不等于无实例**，仍需读。
- **「本章未给 X」型否定断言**（C-09-5）：字面在本章成立，但它附带的一句「后面它真出场时」把范围扩到全书，就跨出了本章凭据。⇒ 规则建议：**否定式断言的适用域必须与它同句里的时间副词一致**（「本章没给」可以，「后面才出场」需全书取证）。

## 已核实为正确（下轮勿改坏）

1. `:9` 全段：装头痛躲开又一顿紧张晚餐／`The break from Gazzie did my exhaustion little good`／地基呻吟与水管奔流／夜鸟与蟋蟀／太困不起床时听见 `light steps striding down the hall, a man’s soft laugh` ✓——md:10 的四项（躲避、地基水管、脚步、男人轻笑）均对应，夜声为唯一小漏（T-09-7）。
2. `:12` 梦的引语与块 1 中文理解逐句对应；`:15` `My resistance had angered the person behind me; rage radiated from her, as tangible as the mud coating my toes.` ✓——块 1「推她的人没有面孔」成立（该段只给性别 `her`，不给脸）。
3. `:21` 浴室：一英寸白八角砖、约每隔一英尺一块黑砖／玻璃淋浴房与餐盘大的花洒／外露铜管洗手盆／浴缸铜脚 `shaped suspiciously like alligator claws`／毛巾烘干架 ✓（md:10「黄铜脚『可疑地』做成鳄鱼爪」用引号标出 suspiciously，处理正确）。
4. `:24` 点柠檬蜡烛、雾镜里的自我端详 `I looked striking. Almost pretty.` ✓——块 2 读者视角提示的「这一段之前，她先在雾镜里看过自己」位置正确。
5. `:30`→`:33`→`:36`→`:39`→`:45` 的显形链条顺序与 md:14「先 breath caught→只写眼睛→与『我』锁定」一致；`:36` `Night black, they darted from side to side, like she was checking the room, making sure we were alone` ✓ md:10「左右扫视」。
6. `:42` `It was like slipping into an endless pit or stepping into the worst dream you’ve ever had, one you think you’ve woken up from but have actually fallen deeper into.` ✓ md:14「用第二人称把私人恐惧普世化」为准确的语法判定。
7. `:48` 尖叫＋冲进卧室＋`slam the door shut behind me` ✓（md:11「锁门」）；`:51` `“What?” a voice barked.`／`:54` chartreuse 领口睡衣套装＋`An object glinted in her hand—a knife.` ✓（md:10「手持一把刀、穿黄绿睡衣」）。
8. `:66` `A stranger broke in to use your bathroom?`／`:75` `She sleeps in the carriage house sometimes.` ✓ md:10「另：Aunt Virginia 有时睡在 carriage house」。
9. `:84` `Disappointment flashed across her face. “Nope. No one here.”`／`:87` `Was she disappointed she couldn’t stab an intruder?` ✓ md:12「检查后失望离开」＋ md:14「用一句猜测把异常写成黑色幽默」。
10. `:90` `Steam had billowed from the surface a moment ago, but now a chill rose from it instead.` ✓ md:14「蒸汽转寒气」。
11. `:102`＋`:108` 两条信息（一个多世纪以来客人做噩梦／`The house is drafty. Cold air gives you bad dreams.`）与 md:10「临走她抛出两条信息」的数量一致；`:96` `it wasn’t altogether unexpected` ✓ md:12「并不完全意外」。
12. `:111` `I couldn’t let her leave thinking I was an airhead. I needed a few more minutes with her to figure out how to redeem myself.` ✓ 块 3「动机是挽回『像个白痴』的印象」＋ md:11「怕被看作白痴」。
13. `:123` `the one tip`／`:126` `head tilted to the left like she was listening for something or waiting for a sign`／`:129` `Fine. But make yourself decent first.` ✓ md:10「手扶门把停住，像在读什么信号」「头偏向左边」「过了一会儿才点头答应」——md:13 的「本章只给出一个先后（先 `Go back to bed`＋挥手赶人，名字出口后才停住）」与 :120→:123→:126 的行序一致 ✓。
14. 词表 17 行例句全部为原文逐字子串（展平＋弯引号归一后比对，0 MISS）。

## 不许裁决（本章内）

- **水面显形是否为真**：:36 显形、:45 威胁性笑、:84 浴缸空无一人、:90 蒸汽转寒气——超自然是否发生，本章不给结论，且 :96 叙述者自认「我肯定是在做梦」；不得裁决其真伪，也不得裁决「Gazzie 扑空后的失望」意味着她信什么。
- **梦中推她的人是谁**：:15 只给 `the person behind me`／`her`，与 :36 水中女人、与 Mama、与 Ida 的同一性本章一律未写。
- **Gazzie 停住「像在听什么／等什么信号」**（:126）：原文是明喻，不得写成她真的听见了什么。
- **「一百多年来客人做噩梦」的成因**：:108 的「漏风／冷空气」是 Gazzie 给出的说法，本章既不支持也不反驳。
- **Ironheart 与 Gazzie／Greer 家的关系**：本章未写（前文 ch05:141 给过「家族射杀的第一条鳄鱼」这一条，不属本章凭据；不得用本章的 :126 反应替它定性，也不得把 ch10 夜谈的内容前挪进本章）。
- **Virginia 为何有时睡 carriage house**：:75 只给事实，原因本章未写。
- **夜谈内容**：本章止于答应（:132），不得预告或总结后章谈话。
