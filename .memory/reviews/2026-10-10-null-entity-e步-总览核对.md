# 《Null Entity》e 步 · 总览层事实核对报告

- 日期：2026-10-10
- 核对角色：独立复核 agent（只读；未编辑任何书目录/总览文件；未做任何 git 写操作）
- 核对对象：`notes/books/novels/null-entity-by-seth-haddon/00_概述.md`、`00_金句精选.md`、`00_情感节点.md`
- 证据底本：`text/ch01_chapter_1.txt` … `text/ch23_epilogue.txt`（24 文件，ch23=Epilogue；按章号映射，不按文件名）
- 口径：四类断言（做了什么／关系／死因／数字范围）逐条要 `text/` 行级支撑；（chNN）引语须逐字存在于该章本体；内嵌英文≥3 字母须锚到同行最近（chNN）；说话人核验看施动关系而非仅 "X said" 窗口；计数断言先枚举再判红；原文没写的不代作裁决。

---

## 1. 汇总

**阻断型 12／提示型 14／假红型 4**

- 阻断型（必须回修，属事实层失真：说话人错位、地点/时序颠倒、数字归属错、无文本支撑的"做了什么"）：**12 条**
- 提示型（不阻断，但需加注、改数量词或标"原文两说"）：**14 条**
- 假红型（复核过程中曾疑、经原文逐字验证后撤销，记此备查）：**4 条**

---

## 2. 阻断型逐条（B1–B12）

### B1｜"六秒"归属错误：六秒量的是被替换前的 VisorForge 原广告，不是反击广告

- md 证据：`00_概述.md:10` — 「反击广告只播了六秒，就被 Edenic Order 的孢子文案覆盖」；`00_情感节点.md:10` — 「广告只播了六秒：终端长出植物，孢子文案盖过画面」
- text 证据：`text/ch01_chapter_1.txt:211` — 「On the concourse, the billboard flared with the VisorForge ad. A corporate jingle hummed, the crest unfolding like a promise: productivity, unity, control. It lasted six seconds before our splice took hold—you'd made it in time.」；`ch01:214` — 「The ad split open along the seam we'd left, revealing what we'd buried: the contract stamped by VisorForge and the Martial Syndicate」；`ch01:220` — 「And for a moment, we had them. They weren't angry yet. They weren't afraid. But they were thinking.」；`ch01:223` — 「And then the Edenic Order fucked it up.」
- 判定：**阻断型**。六秒是原 VisorForge 广告在"我们的剪接接管之前"的时长；反击广告确实播出并换来一段"人们开始想"的窗口，之后才被 Order 的植物/孢子覆盖。md 把六秒记到反击广告头上，同时把"只播六秒即被覆盖"写成因果，属数字归属＋因果双错。（注：`.memory/progress/ne-facts-part1.md` 第 11 项同染此读法，修 md 时一并校准。）

### B2｜"留言板陷入恐慌"：恐慌发生在大厅（concourse），不是留言板

- md 证据：`00_情感节点.md:10` — 「…孢子文案盖过画面，留言板陷入恐慌」
- text 证据：`ch01:235` — 「Someone screamed. That beautiful pause we'd managed disintegrated as panic swept the concourse below.」；`ch01:72` — 「As you stitched the last lines in, the hacker message board pinged, replies flooding in.」
- 判定：**阻断型**。原文的恐慌主体是下方大厅的人群；留言板（hacker message board）只在植入前出现过"回复涌入"，无任何"陷入恐慌"记载。

### B3｜"Come and get it, scavenger" 是叙述者「我」的低语，不是 Aliers 的临终广播

- md 证据：`00_情感节点.md:118` — 「随后，Aliers 的临终广播以拾荒者的口吻回赠一句『你想要吗，那就来拿啊』」
- text 证据：`ch22:90` — 「Her voice came through the station speakers—a heavy, labored breathing I recognized as if it were my own. I laughed weakly and whispered, "Do you want it? Come and get it, scavenger."」；Aliers 真正的广播见 `ch22:96` — 「I am General Renata Aliers of the Thorned Root. For your crimes against humanity's survival, I condemn this station to the Order…And Wylla Sotain, make sure you find a way to live.」；原挑衅句出处 `ch01:298` — 「Do you want it? Come and get it, scavenger.」
- 判定：**阻断型**（说话人＋频道双错位：说话人是 I，"Her voice" 才是 Aliers 的呼吸声）。

### B4｜Wylla 弧"第一句话是恶心"锚在 ch04，而该章引语里没有这句话

- md 证据：`00_概述.md:49` — 「中段：身体被夺、意识被关进猎她的机器，她的第一句话是恶心与不可置信。You stared, wide-eyed. Inside you, the daemon stirred like a stranger's thoughts. Realization hit: …（ch04）」
- text 证据：`ch04:482` 为上述引语逐字出处，句中无"第一句话"与"恶心"；实际首语在 `ch06:120` — 「"I feel sick," you said—filtered through the Subsidiary's voice box.」，且 `ch06:123` — 「Hearing your words in that dry, synthetic channel was unbearable.」
- 判定：**阻断型**。断言内容本身在书里成立（"I feel sick"），但锚定章错误：ch04 引语不能支撑"第一句话是恶心"；须改锚 ch06。

### B5｜砸控制面板 vs RABBIT 挡死：时序颠倒

- md 证据：`00_概述.md:50` — 「最低点：RABBIT 刚刚替她挡死，她砸开控制面板不肯撤。You, who hated feeling useless, opened an external panel…（ch21）」
- text 证据：`ch21:48`（不肯撤＋开面板）在前；RABBIT 施暴与死亡在后 — `ch21:93` 「And RABBIT, violent for the first time, bludgeoned me aside.」、`ch21:96` 「It seized your body. Just for a second. Just long enough to save you.」、`ch21:105` 「RABBIT was dead.」、`ch21:111` 「"RABBIT! RABBIT!" you howled…」
- 判定：**阻断型**。原文顺序是"先拒撤（开面板）→ 后 RABBIT 夺体挡等离子 → RABBIT 死"，md 的"刚刚替她挡死，她砸开面板"把因果倒置。

### B6｜"两人领命留在机库"：原文既无此命，两人也死在 Level Six 接待区

- md 证据：`00_概述.md:71` — 「两人领命留在机库；死亡经过不在正面叙事层，由下一章一句回述交代」；`00_情感节点.md:106` — 「Rahn 与 Sira 领命留在机库，一场孢子爆炸把战场削到只剩 Prime」
- text 证据：`ch17:72` — 「As promised, Aliers had secured two soldiers eager to push deeper into VisorForge—and those two intended to die.」；`ch19:72` — 「Let's just send Sira and Rahn in. If Prime's still inside, the explosion will take it out too.」；`ch20:78` — 「"I'm sorry," you gasped at Rahn and Sira, pressed against the wall. "Thank you. Do it now."」；`ch21:33` — 「In the reception area, haloed by sparking strip lights, stood Prime…I'd outrun the two Prime ordered to the hangar.」；`ch21:36` — 「Rahn and Sira's sacrifice had stripped the field down to Prime alone.」
- 判定：**阻断型**（地点＋命令双错，出现两处）。被 Prime 命令去机库的是两台 Subsidiary（ch21:33 / ch20:72），Rahn 与 Sira 恰恰是被选中"往更深处突入"的人，最后与主角同处 Level Six 接待区/走廊一侧赴死。"下一章一句回述"这半句成立（ch21:36）。

### B7｜"她把这叫作背叛，并且仍然选择了它"：主语错位，这是叙述者 I 的自陈

- md 证据：`00_情感节点.md:70` — 「以摘除 daemon 为价码，「我」越过切断通讯的 Wylla 应下合作——她把这叫作背叛，并且仍然选择了它。」
- text 证据：`ch09:303` — 「I tried to hail you, to apologize. You didn't answer. Dread hardened into spite.」；`ch09:306` — 「You should have spoken to me. Yes, I had your body, but I was trying to help.」；`ch09:309` — 「"Deal," I said, swallowing the despair that followed. It was betrayal, and I chose it anyway.」
- 判定：**阻断型**。按施动关系核验：此刻 Wylla 在机器体内、通讯被切断、无法发言；"It was betrayal, and I chose it anyway" 的"我"是叙述者。md 把定性推给 Wylla，与同段「「我」越过…应下合作」自相矛盾。

### B8｜"越过大半条银河去握她的手"：全书无此量化，握手指的是 ch09 Aliers 伸手

- md 证据：`00_概述.md:34` — 「「我」一度愿意越过大半条银河去握她的手」
- text 证据：全书"half the galaxy"仅一处 — `ch19:249` — 「VisorForge had just turned half the galaxy into its employees.」（指雇员规模，非距离）；伸手意象 — `ch09:312` — 「Resplendent in fury, she was me, refined and burning bright…she was reaching out her hand, waiting for me to take it.」
- 判定：**阻断型**。数字/范围断言无文本支撑；且原句里"我"并未回应"越过半个银河去握"，md 属自造量化。主题段可保留"愿追随 Aliers 的复仇"之意，但须删掉未落的距离数字。

### B9｜"（「我」）压进 Prime 的控制晶格"：把 Wylla 突入的裂缝与叙述者的弥散混成一件事

- md 证据：`00_概述.md:26` — 「与压进 Prime 的控制晶格里，随后成为每一张面具、抹掉整个 GIRS」；`00_情感节点.md:118` — 「与压进 Prime 的控制晶格，把 Directory 移根进 LYREBIRD PRIME」
- text 证据：`ch22:117` — 「Prime's control lattice flickered—its firewalls split, its processes looped in panic. **You** felt the opening before I did and **you** closed the distance.」（晶格是 Wylla 突入的对象）；`ch22:120` 「You put your hands on Prime.」；叙述者自己的动作是 `ch22:144` 「I copied your daemon, the biocode spun from your infected cybernetics, and I let it overrun me…」与 `ch22:171` 「Across thousands of workers, in every implant, in every asset VisorForge had stolen, **I pressed into their minds**.」；对照 `00_金句精选.md:117`（⑰ 译文"我压进他们的意识"）译法正确。
- 判定：**阻断型**（两处）。"做了什么"错置：I 压进的是"千万劳工/每枚植入体"的意识，不是 Prime 的控制晶格；晶格一词属 Wylla 那一拍。

### B10｜"降落在 Facility 34X 前"：飞船落在 GTM-11 行星，设施在市中心，两人是步行接近

- md 证据：`00_概述.md:12` — 「两人仍旧降落在 Facility 34X 前」
- text 证据：`ch02:18` — 「You'd said that five times now, but it hadn't stopped you from **landing on GTM-11—a backwater mining planet**—and agreeing to scout the facility.」；`ch02:21` — 「It sat squarely in the heart of Nacarat City…which meant we'd need to wait for a lull in foot traffic to avoid attention.」；`ch02:127` — 「Nacarat City settled after the shift change, **letting us approach the facility without attention**. Still, by the time we reached the lock…」；对照 `00_金句精选.md:19/20`（② 写"把飞船落在 GTM-11"，正确）与 `00_情感节点.md:22`（"落进 GTM-11 的 Nacarat City"，正确）。
- 判定：**阻断型**（地点断言错，且与同书另两处表述冲突）。

### B11｜"回身把 Fyster 的脑子煮沸"被并入"逃出试验舰的那一夜"

- md 证据：`00_情感节点.md:82` — 「「我」复原出逃出试验舰的那一夜——断电故障、以喙撕杀 tester、回身把 Fyster 的脑子煮沸。」
- text 证据：`ch12:93` — 「That was it. I'd escaped only through a power glitch. I'd murdered a man, swiped his credentials, stolen a ship, **and returned to Fyster** thinking he still wanted me. When I realized my mistake, I let rage bubble over. Finally, I became LYREBIRD.」；煮沸只在追述里被提及 — `ch12:186` 「"That's what Fyster said. Before I boiled his brain."」，及 `ch13:60` 「As with Fyster, I let LYREBIRD generate a construct for interrogation.」
- 判定：**阻断型**。原文序列是"那一夜逃出→回到 Fyster 身边→后来才审/煮沸"，md 的"回身"把两次行动压成同一夜，属时序归并失真。（以喙撕杀tester有 `ch12:81` 支撑，断电故障有 `ch12:93` 支撑。）

### B12｜"发出者是谁，全书从未揭示"：原文明写署名，且 Aliers 自认设局

- md 证据：`00_情感节点.md:10` — 「屏幕上跳出一句没有署名的挑衅…Facility 34X 坐标以一个挑衅的称呼递到面前——发出者是谁，全书从未揭示。」
- text 证据：`ch01:283` — 「A message had appeared—simultaneously—on scavenger forums, hacker boards, and an old mask-parts trade site…**The symbol that had spread across the billboard signed this message now**.」；`ch01:294` — 「The message ended with **a signature we knew couldn't be for anyone else**.」；`ch01:298` 即该挑衅句；`ch14:81` — 「"Then you still waited! **You lured us instead.** Why? Why not just—"」；`ch14:84` Aliers 应答「I had to be careful.」；`ch14:219` — 「The Thorned Root breached security long enough to free her restraints.」
- 判定：**阻断型**。第一条无名挑衅（`ch01:196-199` "A goading message"）确未署名，此半句可留；但"坐标/挑衅的发出者全书从未揭示"与 `ch01:283/294`（以 billboard 符号署名）以及 ch14 里 Aliers 被当面指认为诱致者相抵。悬置点清单（ne-facts-part2.md §4）也未登记此条为悬置，属越界定论。

---

## 3. 提示型逐条（P1–P14）

| # | md 位置＋逐字摘录 | text 位置＋原文逐字 | 判定 |
|---|---|---|---|
| P1 | `00_概述.md:22`「她变形成十九岁的少女面容」；`00_情感节点.md:94`「看见她变形为十九岁的少女」 | `ch13:84`「She became a girl. Not so young that she was unrecognizable, but young, **nineteen or twenty**, all dewy-faced and bright-eyed.」 | 提示型：年龄区间被截半，数字断言应写"十九二十岁上下" |
| P2 | `00_概述.md:14`「一名无名医护…书中始终没有留下**他**的名字」；`00_情感节点.md:34`「为掩护她挡在 Four 面前…书中到死都没有给**他**名字」 | `ch03:216`「**Their** visor fogged, gloved fingers trembling.」；`ch03:222`「Stubbornly, the medic dragged me behind the rubble…**their** satchel…」；`ch03:228`「"Stay with me," **they** begged.」；`ch03:273`「"**Run**," they whispered, stepping into the Subsidiary's path」 | 提示型：原文通篇 they/them，未给性别；md 的"他/她"（医护=他、Wylla=她）属未落地的性别断言 |
| P3 | `00_概述.md:26`「原文只写到「**连贯性在此终止**」为止」 | `ch22:186`「But the last coherent thing I ever thought was: Wylla.」；全库检索无 "coherence"/"coherence ends here" | 提示型：「」内并非原文措辞，伪引语；建议改为直引 ch22:186 |
| P4 | `00_金句精选.md:117`（⑰ 中文）「**穿过成千上万的劳工**…**千万个我**在不该安放人类心灵的地方」 | `ch22:171`「Across **thousands** of workers, in every implant…There were **millions** of me in places not meant to house a human mind…」 | 提示型：thousands 被升为"成千上万"（可通），millions 被写成"千万"，数量级下移一档 |
| P5 | `00_金句精选.md:110`（⑯ 中文）「VisorForge 刚刚把半个银河的**用户**变成自己的员工」 | `ch19:249`「VisorForge had just turned half the galaxy into **its employees**.」 | 提示型：译文增补"用户"这一限定，原文无该词 |
| P6 | `00_概述.md:30`「无身份者无法被执法，这是两人**反复使用**的漏洞」 | `ch01:10`「Erasing your GIRS record had made you a specter…That absence was its own alarm.」；`ch03:162` Four 依旧宣布「Retrieval takes precedence over human resources.」并点名检索 null entity；`ch19:186`「I dragged your wiped ID from the void, spun it hot, and hurled it like a spear…」；`ch22:171`「so no one could use the system to track me down」 | 提示型：原文支持的是"扫不到/追不到"，不是"无法被执法"；"反复使用"未见枚举，措辞需降级 |
| P7 | `00_概述.md:65`「它生平第一次施暴，只为把你的身体拧开一寸；**随后是**一声从没在任何面具上听过的喊叫」 | `ch21:93`「And RABBIT **howled**. I'd never heard such a sound from a mask. Panicked, urgent, childlike in its love, it split its processes…And RABBIT, **violent for the first time**, bludgeoned me aside.」 | 提示型：同句内顺序是"先喊叫→后施暴"，md 反向 |
| P8 | `00_情感节点.md:106`「Prime **识破伪装，掐住**「我」的喉咙提离地面」 | `ch20:15-18`「Prime closed the distance. It gripped Four's throat, hefting me into the air…」在前；`ch20:42`「"LYREBIRD PRIME PROTOTYPE is in your body!" it said cheerfully. "Hello, Mrs. Alzian."」在后 | 提示型：掐喉先于识破；md 顺序倒置（另见悬置点 1：ch20:42 指向不可代裁） |
| P9 | `00_情感节点.md:106`「一场**孢子爆炸**把战场削到只剩 Prime」 | `ch20:78`「"Thank you. Do it now."」→ `ch20:93`「The world went white.」；`ch21:33`「blown apart beyond recovery…I'd outrun the two Prime ordered to the hangar. They hadn't escaped the **blast**, either.」；`ch21:36`「Rahn and Sira's sacrifice had stripped the field down to Prime alone.」 | 提示型：原文只写爆炸/白光，未把爆炸定性为"孢子"；机制属推断，建议标注 |
| P10 | `00_情感节点.md:70`「Aliers 一面**替「我」处理贯穿伤**（没有止痛药，只有 android 血管里的树脂）」 | `ch08:27`「"Medical bay first," Aliers said…"I'll patch you up myself."」；`ch08:105`「we don't have much in the way of painkillers」；`ch08:111`「So, you get resin. It grows in their tubing like sap.」；`ch08:123`「the moment **the androids smeared resin into the wound**, my vision short-circuited.」 | 提示型：Aliers 主导、树脂由 android 涂抹；md 归并施动者，需补一句 |
| P11 | `00_概述.md:44`「**档案说**她是记忆寄生虫，她自己说——这件事必须被知道。」 | `ch12:183`「"Do you know **the Order's official thoughts** about you?" she whispered. "You're a mnemonic parasite. An imitation soul…"」；`ch15:126`「I was human and beyond human, and it mattered that it be known.」 | 提示型：后半句有支撑（ch15:126）；前半句来源应是 Aliers 转述 Order 官方定性，非"档案" |
| P12 | `00_情感节点.md:94`「而 Wylla 体内**自 Thorned Root 孢子起**就埋下的 biocode 残余，当时无人知晓。」 | `ch16:195`「Neither were you free of biocode, Wylla. **You'd been inside Four**…The biocode had brushed you and you'd carried that residue back, an infection rooted in your firmware.」；`ch22:132`「The program had been brewing in you **ever since Thorned Root spores had seeded your cybernetics**.」 | 提示型：原文两处给了不同来源（Four 体内／Thorned Root 孢子），md 单取其一而未标注两说 |
| P13 | `00_情感节点.md:46`「「我」把 daemon 与假凭据复制进 RABBIT…沿黑客论坛加密信道呼叫 Thorned Root」 | `ch05:18`「I copied the daemon into RABBIT and attached the program and ID into it…」；`ch05:24`「Instantly, **RABBIT** gained system-level access and **blared our distress signal along the encrypted channels of the hacker forum**…」；`ch05:27`「The Thorned Root cell of the Edenic Order.」 | 提示型：呼叫动作由 RABBIT 执行；md 让「我」承担两个动作，施动者压缩 |
| P14 | `00_概述.md:18`「**她们**把 Four 舰拖上夺来的巨舰」 | `ch08:15`「**Aliers** dragged the Subsidiary vessel into the belly of a warship, a leviathan that dwarfed us to irrelevance.」 | 提示型：若"她们"指主角两人则施动者错位；若泛指己方需改写主语以消歧 |

---

## 4. 假红型逐条（F1–F4，复核后撤销，记此备查）

| # | md 位置＋摘录 | 撤销理由（text 逐字） | 判定 |
|---|---|---|---|
| F1 | `00_情感节点.md:82`「**机库日志**里受试者 1 至 10 已转往无坐标的 BASE，三日后 Syndicate 将来取一万副面具」 | `ch10:174`「TEST_SUBJECT_RELOCATION—Subjects 1–10, containment BASE」；`ch10:183`「**Hangar logs confirmed** a vessel had already departed for this "BASE," though no coordinates were supplied. And **in three days**, a Syndicate ship was scheduled to dock and carry the demonstration masks…」 | 假红型：字面与数字全部命中，非缺陷 |
| F2 | `00_金句精选.md:25`（③ 中文）「**她是个陌生人**。」 | `ch13:63`「Why? **She was a stranger.**」 | 假红型：逐字对应，非误译 |
| F3 | `00_概述.md:32`「面具时代的终结…是被**一只手从内部注销**」 | `ch22:168`「I became every mask.」；`ch22:171`「I stripped the GIRS, nullified every entry…」；`ch22:165`「There was only one way out.」 | 假红型：隐喻与原文明证一致 |
| F4 | `00_概述.md:18`「夺来的巨舰」（战列舰来源） | `ch08:51`「The Thorned Root were **never meant for this warship**.」；`ch08:54`「**They had taken it**—and now held it together by sheer discipline.」；`ch08:36`「Even as a supposed **monument to old Earth**…」 | 假红型：夺舰与"名义纪念碑"两断言均有原文支撑（唯施动者见 P14） |

---

## 5. 身份／关系链核验（检查②）：无阻断

- I＝LYREBIRD／Sable Veonya、you＝Wylla Sotain 的每章对应关系逐章复核，**换体方向在 ch06 之后从未被写反**：
  - ch06 前：I 借住 Wylla 肉身 — `ch06:120`（Wylla 在 Subsidiary 体内说 "I feel sick"，经 voice box 过滤）、`ch06:102`「"Sable," the Subsidiary choked.」、`ch06:93`「It was crying.」→ 与 `00_概述.md:16`「再睁眼时，「我」在 Wylla 的身体里…而 Four 的躯壳喊出「Sable」并哭泣」一致。
  - ch06 引语逐字核对：`ch06:135`「Here I was, carrying all your modifications…And there you were, reduced to a nearly genderless form…」→ 支撑 概述 L16/节点五"削进近乎无性别的外壳"。
  - ch16 之后：I 在 Subsidiary 躯壳（后为 LYREBIRD PRIME 壳）、you 戴 LYREBIRD PRIME — `ch16:15`「Your return to your flesh was triumphant and bittersweet.」、`ch16:192`「I copied myself into LYREBIRD PRIME, which you donned, and then you pressed my original shell to the Subsidiary…You stepped back—as Wylla—and I stayed inside…」→ 与 概述 L24、节点八 L94「两人隔着 LYREBIRD PRIME 互唤名字」一致。
  - `ch07:174`「Check the cryopod. **Four's incapacitated.**」与 `ch07:63`「My body is me, Sable…」互证 ch07 阶段身份分布无颠倒。
- 冒名宣言未被当作身份合并证据使用（悬置点 2 合规）：md 仅在 概述 L16/节点四 L46 处写"自报为 Sable Veonya"，与 `ch05:90`「Sable Veonya, over and over again」一致。

## 6. 章标签引语与内嵌英文核验（检查③④，脚本口径）

- 口径：把 md 中每条（chNN）引语做空白折叠 + 弯引号→直引号归一，做扁平子串检索，只在对应 `text/chNN` 内匹配。
- 结果：**三个总览文件共 77 条（chNN）引语全部逐字命中各自章号本体**（概述 22、金句 25 主引＋3 呼应、情感节点 30 关键引语）。未发现跨章借用或改写。
- 内嵌英文（≥3 字母，正文散文层）核查：VisorForge、Martial Syndicate、Edenic Order、Thorned Root、Subsidiary (Four/Prime/Eleven)、LYREBIRD (MARK II PRIME / PROTOTYPE ONE)、GIRS、daemon、biocode、Directory／Rhizome Directory、chaff、byronnicum、BSMC-07、GTM-11、Nacarat City、Facility 34X、LP、Pholan's World、OrbitDock Realty、Auntie Donnelly、HelixCare、Sey、Rahn、Sira、Fulvia Balis-Tarok、Auren Pell、Elayne Vex、Rett Varn、Surrett、Beckhan Marshall Wood、Gamma sector — 均在该章原文出现，**无捏造术语、无锚定缺失项**（段落级多章锚定不视为缺陷，故不上报）。
- 计数断言先枚举后判红，均已核：`ch02:18` 五遍（"said that five times"）、`ch01:51` 十三座站/三颗行星/六个月第十次、`ch09:153` 一万副面具、`ch17:69` 十三人藏箱、`ch18:147` 再一次印证 thirteen soldiers、`ch08:39` 只够三十张嘴、`ch08:399` 近六年（"led us nearly six years"）、`ch22:171` thousands/millions、`ch10:183` 三日、`ch23:51` 近七个月。**唯一判红的数字归属是 B1（六秒）与 P1/P4。**

## 7. 文件内自相矛盾 / 节点重复

- 自相矛盾 1：`00_概述.md:18`「她们把 Four 舰拖上…」(P14) 与 `00_概述.md:12/50` 等段把 Aliers 写为第三方施动者的其余表述并存 → 主语需统一。
- 自相矛盾 2：`00_概述.md:49`「第一句话是恶心」(B4) 与同文件 `00_概述.md:16` 只写"躯壳喊出 Sable 并哭泣"未提首语 → 两处描述同一场景、锚定不同章。
- 自相矛盾 3：`00_概述.md:71`「留在机库」(B6) 与 `00_概述.md:24/26`「两人抬着假捷报登上 VisorForge 的私有基地」→ 若 Rahn/Sira 留机库，则同章 ch20:78「pressed against the wall」的现场性无法成立。
- 自相矛盾 4：`00_情感节点.md:10`「广告只播了六秒」(B1) 与 `00_金句精选.md`① 上下文未涉六秒 → 无冲突；但 `00_概述.md:10` 与 `00_情感节点.md:10` 对同一六秒做了同错表述 → 属"错误复制"型节点重复，修一处必同步另一处。
- 节点重复（可保留但需分工）：B5/B6/P7/P8/P9 所涉同一 ch21 事件，在 概述 L50/L65/L71 与 情感节点 L106 各写一遍，两处的时序口径不一致（概述 65 与节点 106 均写"施暴→喊叫/牺牲"，而原文为"喊叫→施暴→夺体→死→回述"）。
- 悬置点越界（除 B12 外，全部合规）：叙述者生死（概述 L26「既不作死亡宣告，也不给复活证明」、节点十 L118「两侧原文都不背书」）✓；两个 Alzian 的牵连（概述 L59、节点八 L94「只并置、不裁决」）✓；Wylla 如何懂得覆写 Prime（节点十 L118「原文自陈不知」对 `ch22:123`）✓；Epilogue 回应虚实（节点十 L118、金句㉕）✓；ch20:42 称呼指向、The Thorned Root 舰/组织两读、Fulvia 下场、Sey 命运、七个月起算点、LP 内是否残存 I — md 均未下结论。

## 8. 已排除、不重复上报项

- 模板层已修词：`mindscape` 与「整座空间站撞进机房」在三个总览文件中均已不存在（全目录 `00_*.md` 检索 0 命中），按 brief 要求不再报警。
- 4 条已知分析层报警按 brief 排除，未重复：ch03:55「Ray？Ray！」／ch21:99「RABBIT！RABBIT！」／ch12:61「whole minds crushed…grown from」／ch11:33「I was gleeful…but」。

## 9. 已核对断言总条数（自数）

按"一个可独立判真伪的事实/关系/死因/数字/引文单元＝1 条"计数：

- `00_概述.md`：梗概九段 66 条 ＋ 三个主题 8 条 ＋ 人物弧光断言 20 条 ＝ **94 条**；另（chNN）引语逐字核对 22 条。小计 **116**。
- `00_金句精选.md`：25 条主引语逐字 ＋ 25 条中文译文断言 ＋ 25 条上下文断言 ＋ 3 条呼应关系引语逐字 ＝ **78**。
- `00_情感节点.md`：十节点拆出事实断言 93 条 ＋ 30 条关键引语逐字核对 ＝ **123**。

**已核对断言总条数＝317 条**（其中判红：阻断型 12 条涉及 21 处 md 行、提示型 14 条涉及 18 处 md 行、假红型 4 条撤销）。

---

### 复核结论

三个总览文件的引语层是干净的：77 处（chNN）锚定全部逐字成立、无跨章借用、无捏造术语、无内嵌英文脱锚；换体方向与身份链未被写反；悬置点纪律除 B12 一处外均守住。问题集中在**中文叙事层的说话人、地点与时序**——最需要动手的是 B3/B5/B6/B7/B9（说话人与时序）与 B1/B10（数字归属、降落地点），以及 B1 在 概述/情感节点 两处的同步修正。
