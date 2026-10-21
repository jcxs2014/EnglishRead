# 3-diff.md · ch02《A Fatal Legacy》三张单子

审查员：独立审查（只查第 2 章）｜语料：`text/ch02_2.txt`（唯一权威源，19,843 字符）
本章 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch02 caius and matt reach the institute.md`
行号均为 `text/ch02_2.txt` 的行号；字符区间为原文 `[起, 止)` 字符位置。

R1 已先行完成（`1-suread.json` 落盘后才开 md），机器层见 `2-machine.json`（`chapter.sh --json`，退出码 0）。

---

## 一、漏单（素读有、md 无）

### O-1 ｜阻断 ｜发现尸体的人与「前门异常敞开」的来源
- 原文 `text/ch02_2.txt:164`（字符 7508–7871）：
  > ‘Willow Bell, she’s a history student at King’s College and interns on Saturdays,’ Caius said, checking his notes. ‘Came in to do her shift and found him like this. **The front door to the museum was unusually left open** and she just walked straight in. She’s on her way to the station for a cup of tea and a formal interview. I’m going to head over in a minute.’
- md 侧：`grep -c Willow` = **0**；`grep -c 前门` = **0**。全文无「谁发现了尸体」「前门异常敞开」的叙述。
- 判定：md 的「原句 4」读者视角提示却写着「这个时间窗和**敞开的大门**、毫无防备的馆子合在一起，划出了凶手可能的进出范围」——分析引用了一个正文从未交代来源的事实。这正是本章「命案现场勘查」链条的第一环（发现人 → 前门开着 → 凶手进出路线），缺失属关键事件未出现。

### O-2 ｜阻断 ｜「凶手也进不去」这一排除性结论 + 那扇门的真实位置（厨房/储藏室/地下室）
- 原文 `text/ch02_2.txt:381`：
  > ‘It’s a town house. **The kitchen and the pantry should be down there.**’ Caius looked at the paintwork along the door. It looked like someone had tried it and judging by the flecks of paint on the floor, recently too.
- 原文 `text/ch02_2.txt:384`：
  > Caius took the keys to the Institute out of his pocket. He went down the steps to the square and again down through the iron gate, then down the basement steps. A heavy brass key fit the lock but again he couldn’t get the door to budge.
- 原文 `text/ch02_2.txt:387`：
  > ‘The door’s been painted shut here too.’ … ‘**If we can’t get in then the killer couldn’t either.**’
- md 侧：`grep -c 地下室` = 0、`grep -c 厨房` = 0、`grep -c 楼梯下` = 0；「凶手也进不去」这一结论零出现（`线索结构` 只把漆门列为一条物证，未给推断）。
- 判定：排除性结论（凶手不可能走这扇门）与门的定位（地下室的厨房/储藏室门）双双缺失，而这是本章唯一一条被明写的**否定性推断**。属关键转折未出现。
- 附：md 同一件事在「线索结构」里被写成「后门」，构成 D-1（错）。

### O-3 ｜阻断 ｜抗议者三人的身份、职业、目击范围，以及「那个眨眼的姑娘」与请愿书
- 原文 `text/ch02_2.txt:221`：
  > The group introduced themselves as Kahurangi, Tākuta and Rawiri.
- 原文 `text/ch02_2.txt:230`：`‘Just on Saturday mornings. I take my son to his swimming class in the afternoon,’ said Kahurangi. ‘I’m busy in the week. I’m a nurse in a GP practice in Kingston.’`
- 原文 `text/ch02_2.txt:236`：`‘I work in a bank in the City full-time,’ said Rawiri.`
- 原文 `text/ch02_2.txt:239`：`‘I lecture in physics at UCL,’ said Tākuta.`
- 原文 `text/ch02_2.txt:260`：`‘What visitors? We’ve been here every Saturday morning for the last three months, and not a soul,’ said Tākuta.`
- 原文 `text/ch02_2.txt:263`：`‘Only that nice girl who winks at us when she goes on her break,’ said Rawiri.`
- 原文 `text/ch02_2.txt:266`：`‘She signed our petition.’ Tākuta handed it over to Caius.`
- md 侧：`grep -c Kahurangi` = 0、`Rawiri` = 0、`Tākuta` = 0、`winks` = 0、`请愿/petition` = 0。
- 判定：三人的姓名与职业、他们「三个月没见到一个人」、以及「馆里还有一个对我们眨眼的姑娘」——这条直接说明**除死者外馆中还有一名女性工作人员**，是目击范围与馆方人员面的关键信息——md 完全没有。关键信息未出现。

### O-4 ｜阻断 ｜晚餐是「生意」而非「约会」的推断
- 原文 `text/ch02_2.txt:155`：
  > ‘Digby didn’t live here.’ … ‘The whole house is his great-whatever-grandad’s stuff. **It might not have been a date. A work thing, maybe? A trustee for the museum? A donor?**’
- 原文 `text/ch02_2.txt:321`：
  > ‘**Gut says business**; it’s too creepy in here. Unless he’s chasing after the goths. I mean, it is Camden, after all.’
- md 侧：`grep -c business` = 0、`生意` = 0、`约会` = 0。
- 判定：md 只写了「只为两人布置的餐桌」，却没有读者最想知道的下一层——这顿饭**可能根本不是约会**。原文两处明写的推断缺失，属关键转折未出现。

### O-5 ｜阻断 ｜抗议者的不在场证明与 mokomokai 的来历说明
- 原文 `text/ch02_2.txt:285`：
  > ‘**The protestors alibied each other.** They were talking strategy in the Covent Garden Wagamama,’ Matt said, finding Caius in the hallway. … ‘Apparently, the mokomokai were preserved as a way to honour their ancestors by showcasing their tattoos which have specific meanings attached to them. They were kept in special ceremonial spaces, but once the British arrived they started buying them as curiosities and it all gets a bit grim.’
- 原文 `text/ch02_2.txt:291`：`‘They were pretty chill. **No real motive.**’`
- md 侧：`grep -c alibi` = 0、`不在场` = 0、`Wagamama` = 0。
- 判定：三名抗议者的互相佐证（「No real motive」）是本章侦查的**排除动作**，md 完全没写；md 只把他们写成「站在门外抗议的人」。属关键事件未出现。

### O-6 ｜提示 ｜死者的手机尚未找到
- 原文 `text/ch02_2.txt:185`–`:188`：
  > ‘Sorry to interrupt, **has the victim’s phone been found?**’ / ‘**Not yet, sir**,’ the masked figure replied, carting away the chicken and cheesecake.
- md 侧：`grep -c 手机` = 0、`phone` = 0。
- 判定：常规问询，未构成转折，但它是本章现场勘查的一项可查事实。

### O-7 ｜提示 ｜制服警员已在广场查访目击者
- 原文 `text/ch02_2.txt:92`（同一段内）：
  > ‘It’s an anthropological nightmare,’ Caius said, leading them up the stairs. … ‘**Uniform are already canvassing the square in case anyone saw anything.**’
- md 侧：`grep -c 制服` = 0、`查访` = 0。
- 判定：与本章「广场」现场直接相关，属本章专属判据里的广场线。

### O-8 ｜提示 ｜邻居 Mrs Bourne（抱狗、住在博物馆隔壁）与「这一带一向安全」
- 原文 `text/ch02_2.txt:435`：
  > ‘Excuse me.’ A woman carrying a small dog stood in between him and the girl as she disappeared into the ether. ‘What’s happened? **I’ve seen all the vans parked all over the square this morning.**’
- 原文 `text/ch02_2.txt:447`：`‘I live next door to the museum thingy.’`
- 原文 `text/ch02_2.txt:453`：`‘Mrs, bless you, **Mrs Bourne**. Did you hear that, **Halloumi**. …’`
- 原文 `text/ch02_2.txt:456`：`‘**DC Noakes** here will ask you a few questions about yesterday evening.’`
- md 侧：`grep -c Bourne` = 0、`狗` = 0、`Halloumi` = 0。
- 判定：md 的末场景只有「金发女子」，本章最后一场戏的另一半（现场邻居问话）未出现；另附「DC Noakes」这一称呼首次出现，md 全文用「艾米」而未给出警衔。

### O-9 ｜提示 ｜「Station first」——下一步是回警局做正式笔录
- 原文 `text/ch02_2.txt:393`：
  > ‘**Station first**,’ Caius said, turning quickly towards the car and straight into a young woman.
- md 侧：`grep -c Station` = 0、`警察局` = 0。
- 判定：原文明确说下一站是警局（见 O-1 的 Willow Bell 正在警局），md 未交代任何去向。

### O-10 ｜提示 ｜保险逻辑与「两层展品 + 阁楼藏书」的规模
- 原文 `text/ch02_2.txt:176`：
  > ‘I suppose if there was anything with a high value here then **their insurers would’ve made them take precautions**. Their security measures are non-existent,’ Caius said, receiving the guide from Amy. ‘**There’s two floors of exhibits and the attic contains Horatio Combe’s library.**’
- md 侧：`grep -c 保险` = 0、`insurer` = 0；「两层展品」未出现（`阁楼里的藏品账本` 只对应 ledger 一处）。
- 判定：md 词汇表收了 `attic` 一词且例句即此句，但正文没把这句写进勘查；提示级。

### O-11 ｜提示 ｜原句 2 的引语偏短：丢掉了卡伊乌斯的评语与上楼动作
- 原文 `text/ch02_2.txt:92` 整句：
  > ‘It’s an anthropological nightmare,’ Caius said, leading them up the stairs. ‘Horatio Combe was one of those Victorian adventurer types. Liked collecting artefacts, and taxidermy of exotic creatures. There’s a mangy-looking kangaroo at the top of the stairs.’
- md 引语从 `Horatio Combe was one of those…` 起（字符 3764），丢掉前半句；md 的「中文理解」却写「卡伊乌斯边带同伴上楼边介绍这家机构」——动作来源在被引范围之外。
- 判定：引语选短（S2 失误第 ① 类），提示级；另注 md 词汇表收录了 `anthropological`，例句正是被丢掉的那半句。

---

### O-12 ｜提示 ｜开头「两分钟闲聊」整段（字符 469–3144，约全章 13%）无任何引语块
- 原文 `:23`–`:85`：Caius 给两分钟计时；Amy 说 meme、‘not today, Satan’、gay 与 girlie 圈「collective swoon」；Matt 称 Monty Don 是 ‘A consummate professional’、希望 BBC 给他六位数薪水；Caius ‘I’m thirty-five not eighty-five’；Callie 的妈妈脱鞋要打 Max、劝她「too pretty to risk damaging」；Caius 说 Callie 父亲的律师要发 cease and desist；Matt 说 ‘It was her ex not you. He jumped in front of the camera.’
- md 侧：仅 `人物弧线`（md `:14`）以「先给同伴两分钟倒计时聊完八卦」一句带过，无引语块、无细节。
- 判定：本章聚焦命案现场，开篇闲聊属铺垫而非侦查链，故列提示级；但 `meme` 一节是后文（结尾女子「assuming she recognised him from the damn memes」）的伏笔，md 未把这条线接上。

（本文件分批写入：漏单先落盘，后续追加「二、编单」「三、错单」「四、已核实为正确」。）

---

## 二、编单（md 有、原文无）

### F-1 ｜阻断 ｜（与 D-1 同源缺陷，单计一次）凭空出现的「有人试图打开过的后门」
- md `:13`（线索结构）：
  > …漆死而地上留着新漆屑、**说明近期有人试着打开过的后门**、后巷里那辆破旧自行车…
- 原文对照：
  - `:375` `…then he noticed **a door under the stairs**. ‘Amy, have you been down here yet?’ Caius walked over and twisted the handle. It wouldn’t budge.`
  - `:378` `‘I didn’t try it. **Someone’s painted the door shut**,’ Amy said.`
  - `:381` `‘It’s a town house. **The kitchen and the pantry should be down there.**’`
  - `:297` `‘**The back door and the gate were both unlocked.**’`
- 判定：原文里「被漆死、地上有新漆屑、近期有人试图打开过」的是**楼梯下的地下室门（通厨房与储藏室）**；后门与院门恰恰**都没上锁**。md 把这组属性整组安到后门上——原文里「有人试图打开过的后门」这一情节并不存在，属凭空出现，阻断。

---

## 三、错单（两边都有，但不一致）

### D-1 ｜阻断 ｜漆死的门被写成「后门」，且与本章另外两处自相矛盾
- md 三处并列：
  - `:13`「…**说明近期有人试着打开过的后门**…」
  - `:77`「记住锁这个细节——钥匙在死者书桌抽屉里，**后门与院门却都没上锁**。」
  - `:95`「…**后门与院门都没上锁**，进出几乎没有阻力…」
- 原文：`:297` `‘The back door and the gate were both unlocked.’`；被漆死的是 `:375`/`:378`/`:381`/`:384`/`:387` 的楼梯下地下室门。
- 判定：一扇门不能既「被漆死且有人试图打开」又「没上锁」。同一章内三处自相矛盾，阻断。

### D-2 ｜阻断 ｜原句 9「为什么这样写」：问的人与答的人双双写反（施事/受事反转）
- md `:105`：
  > 这种先抑后扬的写法让读者比卡伊乌斯先一步留意她——**他还追问了一句「我们以前见过吗」，她却答不上来。**
- 原文：
  - `:402` `‘**Have we met before?’ she asked** as she straightened herself up, …`
  - `:408` `‘**No, we’ve met. I’m sure we have.**’`（是她坚持两人见过）
  - `:411` `‘**I don’t think so …**’`（是卡伊乌斯说没印象）
  - `:414` `‘I guess you really must have one of those faces.’`
- 判定：问的是**她**（对卡伊乌斯），不是卡伊乌斯；她也不是「答不上来」——她答了两次并坚持「见过」。两处归属反转，阻断。另：同章 `线索结构`（md `:13`）写的是「撞上卡伊乌斯后**自称见过他**的亚麻色头发女子」，与 md `:105` 自相矛盾。

### D-3 ｜阻断 ｜原句 5「读者视角提示」：面包卷与碎屑的主人写反
- md `:67`：
  > 注意两个人吃的不一样——**死者那侧是沙拉**，**对面那位只留下一个罂粟籽面包和一堆碎屑。**
- 原文：
  - `:131` `‘Dinner time. … **The same salad on both plates.**’`（两个盘子都是同一种沙拉）
  - `:134` `‘The other person filled up on bread,’ Amy said, noting that there was **a roll on Digby’s side plate and just crumbs on his guest’s**. ‘**It’s a fancy one too with poppy seeds in a swirl.**’`（罂粟籽旋纹面包卷在**迪吉（死者）那侧**；客人那侧**只剩碎屑**）
- 判定：md 把面包卷与碎屑一并安到客人一侧，又把死者一侧写成「只有沙拉」。原文里客人是「filled up on bread」（只剩碎屑）、死者那侧才有那个精致面包卷——**受事归属反转**，阻断。

### D-4 ｜阻断 ｜原句 8「读者视角提示」：巷口视线方向与原文相反
- md `:97`：
  > 巷子通向主路，对面是游乐场，**进出巷口没有视线死角**；这栋房子自己却一台摄像头也没有。
- 原文 `:315`：
  > ‘The alleyway leads onto the main road. There’s a playground opposite, **so no visual on the entrance**.’
  （与 `:303` `‘You could get in and out unnoticed.’` 一致：巷口**看不见**来人）
- 判定：中文「没有视线死角」按字面读＝看得见，与原文「入口处无人看得见」方向相反，属对线索含义的反转。若本意是「巷口没人看见」，措辞须改写。阻断。

### D-5 ｜提示 ｜「一杯水」与原文的「a jug of water」不符
- md `:61`：「…**一杯水**里的冰早已化尽…」
- 原文 `:131`：「…**a jug of water** in which any trace of ice had dissolved…」
- 判定：jug＝壶/罐，非杯。措辞不当，提示级。

### D-6 ｜提示 ｜「同一株木兰」是推断，原文未指同一棵
- md `:25`「**同一株**木兰在章末又被用作藏人的掩体」；md `:115`「**开篇那株**『伸手去够云』的木兰此刻成了藏人的掩体」。
- 原文开篇 `:20` `The magnolia trees **in the centre of the square** were blooming.`；结尾 `:465` `peeked out from behind one of the magnolia trees **in the garden in the square**.`
- 判定：解读正当，但「同一株」在原文中无据（centre 与 garden 两处措辞不同）。提示级。

### D-7 ｜提示 ｜原句 7「读者视角提示」：抗议者与死者的冲突不是「当天」
- md `:87`：「这三个人是**当天**出现在馆舍门外、并且**跟死者起过冲突**的人…」
- 原文 `:257`：`‘**A couple of months ago** he threatened to call the police on us because we were upsetting his visitors,’ said Kahurangi.`
- 判定：冲突发生在几个月前，且是**死者威胁要报警**（不是他们与死者冲突）。提示级。

### D-8 ｜提示 ｜原句 3 / 原句 4 的分析延伸到引语之外（引语选短）
- 引语止于 `It’s a bit like a mouse infestation or rotting parsnips.`（`:116`）；md `:41`「他周末常去野外采集…」与 `:45`「接着那句『我采过野食所以认得』」、`:47`「留意死者两个口袋里那包纸巾和薄荷糖含片」均取自引语之后（`:116` 后半、`:122`）。
- md `:51` 的「该做的检验都会做，但不会带来意外」取自 `:128` 同段 Barry 的前一句。
- 判定：属 S2「引语选短 + 分析超范围」；但 md 在「为什么这样写」里明写「接着那句」，未把引语外内容伪装成引语内内容 → 提示级。

### D-9 ｜提示 ｜原句 2 引语起点偏后（漏掉「人类学的噩梦」与上楼动作）
- md 引语自 `Horatio Combe was one of those Victorian adventurer types.`（原文 `:92` 段内第二句）起；`:92` 首句为 `‘It’s an anthropological nightmare,’ Caius said, leading them up the stairs.`
- md `:31`「卡伊乌斯边带同伴上楼边介绍这家机构」的动作与评价来源都在引语外。
- 判定：引语选短（S2 失误第 ① 类），提示级；md 词汇表 `anthropological` 的例句恰为被丢掉的那半句。

---

## 四、已核实为正确（防误修）

1. **原句 3 的「死因」归属正确**：md `:41`「法医巴里给出死因：毒芹」——原文 `:107` `‘Hemlock,’ Barry said.`，说话人无误。
2. **原句 4 的「死亡时间 7–9 p.m.」逐字正确**：md `:51`「傍晚七点到九点之间」——原文 `:128` `‘By the looks of him he died in the early evening. I’d say somewhere between 7 and 9 p.m.’`；且「不会带来意外」出自同段 `:128` `‘I’ll run the requisite tests, but I don’t think there’ll be any surprises’`（属同一话轮，未错记归属）。
3. **原句 6「没有摄像头没有报警器，只有一把配钥匙的锁」的说话人正确**：md `:71`「卡伊乌斯答得很干脆」——原文 `:170` `‘Nope,’ Caius said. ‘No cameras, or alarms, nothing. Just a lock with a key.’`；md 把它写成「收藏着猎物的屋子为何一直无人觊觎」的因果，原文 `:176` 的保险逻辑可支撑（见 O-10 属漏，不属错）。
4. **原句 7 的抗议陈述逐字对应**：md `:81`「多次拒绝他们政府的请求，要把这里被不道德地保管着的人类遗骸送回 Aoteara」——原文 `:212` `‘The Horatio Combe Institute has refused multiple requests from our government to return human remains unethically kept here to Aoteara’`，主语与方向均正确。
5. **原句 9 的外貌描写逐字对应**：md `:101`「头发在脑后挽成凌乱的髻，一顶素黑棒球帽压得很低，衣着宽松、颜色暗淡；可帽檐下那一点好奇的火花却烧得很亮」——原文 `:402` `She was flaxen-haired, although it was tied up into a messy bun at the back of her head and a plain black baseball cap was pulled close over her eyes. … Her clothes were baggy and dull-coloured. But a spark, a curious flame in her eyes that peeked out from under the cap burnt bright.`（该块**只有**「为什么这样写」的说话人部分错，见 D-2）。
6. **原句 10 逐字对应**：md `:111`「从广场花园的一棵木兰树后探出身来，看着他走远，心里盼着他会回来」——原文 `:465` `peeked out from behind one of the magnolia trees in the garden in the square. She watched him leave, hoping he’d return.`（措辞「同一株」问题另见 D-6）。
7. **词汇表 26 条例句全部逐字命中原文且各命中 1 次**（`/usr/bin/grep -F -c` 全 26 条 rc=0、hits=1；`scripts/check_vocab.py` 本章 FAIL=0）。逐条命令：
   ```
   /usr/bin/grep -F -c -- "<例句>" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch02_2.txt
   ```
8. **机器层全绿**：`bash scripts/chapter.sh "<ch02 md>" --json` 退出码 **0**、`verdict: ok`；引语 10/10 逐字命中（含省略号分段独立取证，本章 10 块各 1 段、无 `…` 缝合）；`counts` 全 0；CJK 占比 0.83–0.94。
