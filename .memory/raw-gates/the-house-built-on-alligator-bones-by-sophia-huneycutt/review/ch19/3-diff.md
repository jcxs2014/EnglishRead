# ch19 R3 三张单子（漏／编／错）

- 章文件：`ch19 live alligator in skinning room.md`
- 语料：`text/ch19_chapter_eighteen.txt`（216 行 / 1,797 词；块内引用一律写 `:行号`）
- R1 素读：`review/ch19/1-suread.json`（160 条事实 / **MISS 0**）
- R2 机器层：`review/ch19/2-machine.json`（chapter.sh rc=0；块数 6、引语块 6／片段 7／查无 0；H1 ✅；导航 5 项 ✅）
- ⚠️ 机器层假绿提示：本章 md 内**反引号 span 0 个**、**ASCII 撇号 0 处**，所以 ch18 的两类形态缺陷（C-18-13 撇号字形、T-18-13 ASCII 引号）在本章**不适用**，勿照抄整改。
- ⚠️ 口径缺口（工具层，非本章缺陷）：`scripts/bookform.py` 的 `QUOTE_RE` 只匹配 `> **原句 N:**` 行 ⇒ **导航五句与「一句话总结」里内嵌的英文不在逐字 lane 内**。本轮用 `/tmp/in19b.py` 补查：md 内非块内英文串 63 条，除 `Chapter Eighteen`（H1 用词）与 `Tropes`（导航标签）外**全部命中本章 text**，逐字与字形均正确。

## 一、阻断（11 条）

### C-19-1 【断言·因果凭空】「救下我」把叙述者没写的因果写成事实
- md:10（导航·一句话概括）「压住鳄鱼下颌救下我的，是 Gazzie」
- md:12（导航·Tropes）「千钧一发的搭救也不是情人完成的」
- md:74（块 6·为什么这样写）「搭救的姿态不是温柔而是蛮力」
- md:76（块 6·读者视角提示）「也没有被救后的安心描写」
- md:112（一句话总结）「而徒手按住鳄鱼下颌救下我的，正是……Gazzie」
- 原文逐字：
  - `:210` "As I turned to run, the room turned with me. I sensed the alligator moving—lunging, maybe—but I was already falling forward, out the door I’d left cracked open. I stumbled about six steps down the hallway before my foot caught on something, throwing me to the floor."
  - `:213` "My vision grayed. I thought I heard shouting but couldn’t be sure."
  - `:216` "At some point, I opened the eye not pressed into the concrete floor. On the skinning room’s threshold, Gazzie lay on top of the alligator, holding its jaws closed with her bare hands, her mouth open in a scream."
- 判据：原文只给「她趴着／鳄鱼被按颌／Gazzie 在尖叫」三个观察项；鳄鱼是否已扑出、按颌是否阻断了对 Dart 的攻击、Gazzie 何时进入房间，一个字未写（"lunging, maybe" 本身就是她的不确定）。md 把「搭救成功」写成事件。
- 改法：五处「救下我／搭救／被救后」改为观察级表述（例：md:112 → 「而压住鳄鱼下颌的，正是那个连早安都不肯当面回给我的 Gazzie」）；是否构成「救」列进不许裁决。

### C-19-2 【断言·全称被同章反证】「先看后怕，本章从头到尾没有断过」
- md:76（块 6·读者视角提示）「这条『先看后怕』的习惯，本章从头到尾没有断过」
- 原文逐字：`:201` "It hissed again, the sound loud and hollow and terrible." ／ `:204` "I froze. How did you scare off an alligator? …" ／ `:210` "As I turned to run, the room turned with me."
- 判据：末场恰恰是先给怕（terrible → I froze → 转身要跑）再给细看；「先看后怕」只在块 6 的醒来一瞬成立。全称断言被本章内三处反证。
- 改法：限定为「醒来那一瞬仍是先看后动」，删「本章从头到尾没有断过」。

### C-19-3 【对应·否定式断言反了】「本章没有给倒下的成因判语」
- md:36（块 2·读者视角提示）「本章没有给倒下的成因判语，留给读者的是一具先出问题的身体」
- 原文逐字：`:15` "…When it did, the wall clock read three in the afternoon. **No wonder I felt faint.**" ／ `:207` "Another worry hit me: I’d eaten lunch, but I hadn’t had water, and I was hot. Very hot."
- 判据：同段末句就是她自己下的判语（"No wonder"），`:207` 又是她自己归因。且与 md:10「脱水与酷热让身体先倒下」自相矛盾——同一份 md 里两处对同一事实判成相反。
- 改法：md:36 该句改为「成因由叙述者自己给出（`:15` "No wonder I felt faint." 与 `:207` 的缺水自察），读者拿不到的是第三方诊断」。

### C-19-4 【对应·章内时序写反】缺水念头与见鳄的先后颠倒
- md:36（块 2·读者视角提示）「她自己**先**冒出『我吃过午饭，可我没喝水，而且我很热』这个念头，**再**站到鳄鱼面前」
- 原文逐字：`:198` 见活鳄 → `:204` "I froze." → `:207` "Another worry hit me: I’d eaten lunch…" → `:210` "As I turned to run…"
- 判据：念头在站到鳄鱼面前**之后**才出现（`:198` 先于 `:207`），md 写的方向正相反；这一顺序正是本章「身体先背叛」的落点。
- 改法：改为「她是在鳄鱼面前僵住之后，才冒出缺水与酷热的念头——恐惧先占了身体，归因晚了一步」。

### C-19-5 【对应·块引语截短，漏掉承重句】块 2 引语止于 "…three in the afternoon."
- md:28（块 2 引语）末句为 "When it did, the wall clock read three in the afternoon."
- 原文逐字：`:15` 同段紧接一句 "No wonder I felt faint."
- 判据：截短本身不违规（块引语 ≤100 词），但被截掉的这一句是 C-19-3 误判的直接来源，且是本章身体线的第一个判语。补齐后引语仍合规（原段 3 句 + 1 短句）。
- 改法：引语末补 `No wonder I felt faint.`；同步 **中文理解** 增「难怪我觉得发晕」；**关键词** 增 `No wonder`。

### C-19-6 【断言·极性读反】把原文否定式的自我台阶读成肯定式
- md:56（块 4·读者视角提示）「留意她随后给出的台阶——把漏洞归到『**他也喝过第二杯下午咖啡了吧**』一类的日常理由（同段后文）」
- 原文逐字：`:159` "Would he really have forgotten? **I supposed he hadn’t had that second cup of afternoon coffee yet.** He wasn’t a perfect employee, after all."
- 判据：原文是 hadn’t had（还没喝 ⇒ 所以真的忘了，这才是台阶）；md 写成「他喝过了」，把台阶的机制反了。属本书已知缺陷簇「评价极性反转／无据时刻」。
- 改法：引号内改为「他也还没喝到那第二杯下午咖啡吧」。

### C-19-7 【断言·全称被同块反证】「『我』只出现在被撞的肩上」
- md:44（块 3·为什么这样写）「三个句子的主语全是 He，而『我』只出现在被撞的肩上，压迫感由语法承担」
- 原文逐字：`:27` "He walked disrespectfully close in hallways, bumping my shoulder **when we passed**." ／ "Every time **our eyes** met, he smirked, like he knew something that gave **him** the upper hand."
- 判据：第一句含 `we passed`、第三句含 `our eyes met`；「我」以复数第一人称与所有格出现在三句中的两句里，不是只出现在肩上。
- 改法：改为「三句小句主语全是 He，『我』只作 `we`／`our` 出现、从不做主语，压迫感由语法承担」。

### C-19-8 【断言·框架复用】「一章的被动接招里少见地主动推理」（ch18 同类已被推翻）
- md:54（块 4·为什么这样写）「这是她在一章的被动接招里少见地主动推理」
- 原文逐字（本章她的主动发问／主动判断）：`:42` "Without thinking, I asked, 'Are you close?'" ／ `:78` "'Have you talked to Gazzie about it?' I asked." ／ `:129` "'Why?'" ／ `:135` "'Can we do it tomorrow?'" ／ `:147` "'She needs us this minute?'" ／ `:153` "'Joe’s not even around.'" ／ `:174` "And put rat poison in it? Not today." ／ `:204` 四连问（How did you scare off an alligator? …）
- 判据：本章她是持续的追问者；「被动接招」是 ch18 审查已推翻的框架（C-18-8），在本章反证更多。
- 改法：删「被动接招」，改为「本章少见的连续推理段——她一次把消息的传递路线逐条盘完」。

### C-19-9 【断言·跨章「第一次」不实】「与 Mama 的矛盾第一次成句说出」
- md:13（导航·人物弧线）「与 Mama 的矛盾第一次成句说出（她『拒绝用我看自己的方式看我』）」
- 原文逐字：本章 `:93` "No, in that we argued constantly, and she refused to see me the way I saw myself. How could I be close with a woman who thought I was a monster?"
- 反证（更早成句）：`ch13:222` "Mama’s voice ghosted in my ear. You’d better tame that devil in you." ／ `ch13:225` "…didn’t want to be **the twisted person she believed I was**—a raging creature drawn to darkness." ／ `ch02:94` "After the incident with Michelle, when Mama had pulled me from middle school, I’d accepted her explanations…"
- 判据：「她认为我是扭曲的人」在 ch13 已成句；本章的推进是**第一次当着别人把这段说出来**，不是第一次成句。
- 改法：改为「与 Mama 的矛盾第一次在对话里被说出口（此前 ch13 已把『她认为我是扭曲的人』写成独白）」。

### C-19-10 【漏·本章的留白声明全 md 未登记】`:102` "I couldn’t get into the night she died."
- 取证：`/usr/bin/grep -c -i "night she died" "ch19 live alligator in skinning room.md"` → 0；同查 `lupus`／`kidney` → 0。
- 原文逐字：`:102` "I had to take care of her. She had lupus, so she needed a lot of help. Then she had a kidney transplant that didn’t go well, so." **I couldn’t get into the night she died.**
- 判据：这一句是叙述者**自己声明不讲**——正是全书「Mama 死法一律不裁决」在本章的落点。md 反而把 Mama 线写成「矛盾第一次成句说出」（C-19-9），把「说出的只是病因、说出的一半是回避」这一层抹平。
- 改法：块层或某块「读者视角提示」登记此句并注明「当夜如何死亡，叙述者明写不讲」；不许裁决条目同步补该出处。

### C-19-11 【形态·导航感官顺序写反】「按听觉（嘶声）、触觉（闷热）、视觉（灯亮）依次展开」
- md:14（导航·叙事手法）末句
- 原文逐字：`:186` "Pushing open the door, I found the air **humid and hot**, like I’d stepped outside. A persistent **drip echoed** in the cavernous space." → `:189` "A **hiss** sounded somewhere in front of me." → `:195` "The **lights blinked on** immediately, illuminating the room."
- 判据：实际次序是触觉在前、听觉（滴水）次之、嘶声第三、灯亮最后；md 把「嘶声」提到「闷热」之前。
- 改法：改为「按触觉（闷热）、听觉（滴水→嘶声）、视觉（灯亮）依次展开」。

## 二、提示（14 条）

| # | 位置 | 问题 | 证据（原文逐字） |
|---|---|---|---|
| T-19-1 | md:13 | 「父亲**病逝**」把两句合成死因；原文只说生病与去世，未并句 | `:51` "It’s been a while since he died… Fished every Sunday until he got sick. He didn’t have health insurance…" |
| T-19-2 | md:11 | 「前半段是**全书**里少有的平稳上升带」——全书级评价无跨章依据 | 建议限定为「本章前半段」 |
| T-19-3 | md:11 | 「惊骇覆盖了一切安抚」——末段无任何情绪词，安抚与惊骇都由评论者补 | `:213` "My vision grayed."／`:216` 全句只有观察 |
| T-19-4 | md:12、md:112 | 「不肯当面跟我说一句话」「连早安都不肯当面回给我」的证据在 **ch18**（`:1`/`:5`/`:13`），本章 Gazzie 全程不在场 | `:9` "…inside Greer House, which was empty, besides Gazzie"；`:159` 只写她绕道传话 |
| T-19-5 | md:14 | 「Joe 的威胁**全部**经叙述者的观察拼贴传递（撞肩、切橙、冷笑）」漏第四笔；本章 Joe 的另一条存在感经 Harrison 转述 | `:27` "His presence usually cast a slimy film over Greer Fine Alligators, but I hadn’t felt that creeping sensation all day."／`:150` "Word came from Joe."／`:156` "He left me a note…" |
| T-19-6 | md:54 | 「两个问句追的不是『丢了什么』」——本章疑心对象是被召回文件，「丢了什么」无所指（疑为 ch18 盗皮线残留） | `:126` "Gazzie wants you and me to go over the progress you’ve made on the files." |
| T-19-7 | md:64 | 「这正是她检查死鳄鱼时惯用的那双眼」——本章无死鳄计量；长度标准出自 Harrison 之口 | `ch18` "…we raise them until they’re six or so feet before we, you know." |
| T-19-8 | md:34、md:46 | 「读者反而会去数她遮住了什么」替读者预定反应；本书其余章多用「留意／注意」 | 形态统一建议 |
| T-19-9 | md:28–36 | C-19-5 补引语后，中文理解与关键词需同步，否则触发 `关键词不成立` | 门禁项 |
| T-19-10 | 全 md | `:75` 的雇主道德判断未登记（她对 Gazzie 态度线的关键转折） | `:75` "I was shocked Gazzie could hold her head high among her employees. I wasn’t sure I’d be able to look them in the eye now." |
| T-19-11 | md:11 | 「私人的防御在咖啡桌边松了一次口子」只取一半——原文下一句立刻把这份松口子重解释成攻势，反转漏登记 | `:105` "His voice gentled… 'Sounds like a sacrifice.'"／`:108` "Was he trying to act like my friend now? This was another tactic. Another attempt to disarm me. Weaken me." |
| T-19-12 | md:11 | 「**农活**带来掌控感」——本章的掌控感来自剥皮（加工环节），措辞与 `:12` 不完全对应 | `:12` "Skinning itself fell into a rhythm." |
| T-19-13 | 块层 | 块数 6＝本章建议上限；午餐对话 `:39`–`:117`（约 80 行，全章最长、最揭示人物的场景）**零块覆盖**，md 只在导航里概括 | 硬限 2–15，可加至 7–8 块（候选 `:102`、`:180`） |
| T-19-14 | 全 md | 中文语境引号用弯双引号，与全书 39/49 章的「」形态不一致——延续 ch18 的书级定档问题，**不在单章整改** | 见 `review/ch18/3-diff.md` T-18-13 |

## 三、假红（14 条，写进护栏，勿改）

| # | 表面疑点 | 判定 | 证据 |
|---|---|---|---|
| F-19-1 | 「祖母」称谓 | 正确 | `ch02:144` "Gazzie Greer was my grandmoth…" |
| F-19-2 | 「『Dart』这个称呼第一次从他嘴里喊出来」 | **跨章核实成立** | `text/ch13·14·16·17·18` 中 `Dart` 0 次；`ch15:42/:48` 两处均 Aunt Virginia；`ch12:12/:51` 的 Dart 出自 Gazzie；本章 `:120` 为 Harrison 首次 |
| F-19-3 | 「一周里」 | 正确 | `:9` "Over the next week"／`:12` "Halfway through the week" |
| F-19-4 | 「Joe 的纸条」 | 正确 | `:156` "He left me a note thirty or so minutes ago." |
| F-19-5 | 「独自摸黑回剥皮间拿水壶」 | 正确 | `:165` "I’ll just grab my water bottle."／`:168` Harrison 提出代取被拒／`:174` "I’m quite capable, thanks."／`:183` "The room was dark." |
| F-19-6 | 「七八英尺的活鳄鱼」 | 正确 | `:198` "A live alligator, seven or eight feet long…" |
| F-19-7 | 「Gazzie 的伤情、后续处置，这段一个字都不给」 | 正确 | `:216` 即本章末行 |
| F-19-8 | 「两个 why 之间略开的那句…最良性解释」 | 正确 | `:159` "Maybe she’d just run into Joe at the opportune moment." |
| F-19-9 | 「他追出来喊我 Dart」 | 正确 | `:117` "…I heard Harrison calling my name."／`:120` "…he repeated… as he jogged toward me." |
| F-19-10 | 词表 15 行 | 逐字全部命中本章，词头全部在场 | `/tmp/v19.py`：rows 15 / flagged 0 |
| F-19-11 | 撇号层 | 本章 md 内 ASCII 撇号 **0 处**、反引号 span 0 个 | `/tmp/ap19.py` |
| F-19-12 | 导航与总结的内嵌英文（门禁不覆盖区） | 63 串中除 `Chapter Eighteen`（H1）、`Tropes`（标签）外全部命中本章 text | `/tmp/in19b.py` |
| F-19-13 | 「温室和院子不像主楼，那里没有异象异响」 | 正确 | `:9` "I’d discovered that the conservatory and yard were free from odd sights and sounds, unlike the original building" |
| F-19-14 | 「与 Harrison 借一杯咖啡交换了医保、他父亲与 Mama 的话题」 | 正确 | `:36`／`:49`／`:91` |

## 四、不许裁决（12 条）

1. Harrison 父亲的死因（`:51` 只给 got sick / died / 无医保，不得并句）。
2. Mama 死亡当夜（`:102` 叙述者明写不讲）。
3. 活鳄鱼如何进剥皮间、谁放的、是否 farm 的鳄鱼。
4. 鳄鱼是否已扑出、Gazzie 按颌是否阻断攻击（＝C-19-1 的「救」）。
5. Gazzie 的伤情与后续处置。
6. Dart 是否被咬到／身体受损。
7. Joe 全天缺席的原因与纸条动机（`:27` 的 slimy film 一整天未出现，原文未解释）。
8. Harrison 是否故意延迟传达（她的四条 why 都自带台阶，`:159`）。
9. Gazzie 为何绕道 Joe→Harrison 传话（`:159` 叙述者自己也在猜）。
10. Aunt Virginia 的 mysterious errands 内容（`:9`）。
11. Uncle Leon 的 lockbox／sketchbooks（`:9` 只写「稍后再开」）。
12. Greer House 的异象是否超自然（`:9` 全部由叙述者自行合理化）。

## 五、跨章取证（登记表候选）

| 实体／母题 | 本章 | 其它章 |
|---|---|---|
| `Dart`（Harrison 首次喊出） | `:120` | ch12 由 Gazzie 引入；ch13–ch18 Harrison 侧 0 次；ch27/ch32/ch35 起高频 |
| 早安备拒（Gazzie 不答） | 本章仅绕道传话 `:159` | 实体证据在 ch18:1/:5/:13 |
| `dryer sheets` 气味链 | 本章 0 次 | ch13:48→ch17:33→ch18:309 |
| 无医保／`Greer Fine Alligators doesn’t offer health insurance` | `:66`／`:75` | 全书首次成句 |
| `POTS` | `:75` | 前章已建立（病历线） |
| 剥皮＝最爱任务／`the key to impressing her` | `:9` | ch18 引入 |
| 屋顶漏水 / `The leak had sprung again` | `:186` | ch18:171/:174（three buckets 升级前） |
| `Ironheart`／曾曾祖母 Ida | 本章 0 次 | ch04、ch10 |
