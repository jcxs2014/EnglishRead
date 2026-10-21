# 4-verdict.md · ch02《A Fatal Legacy》判定表

审查员：独立审查（只查第 2 章）｜语料：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch02_2.txt`（19,843 字符，唯一权威源）
本章 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch02 caius and matt reach the institute.md`
本目录落盘：`1-suread.json` / `2-machine.json` / `3-diff.md` / `4-correspondence.md` / `4-verdict.md`

**覆盖声明（必填）**：本次只审**第 2 章**，由任务指派。ch02 章型＝**命案现场勘查章 + 对话密集章**，S1–S5 全部人工过了一遍；**其余 53 章本次未审，不得据本报告说全书通过**。本章专属判据（勘查线／旁观线分列、结尾旁观者进入「线索结构」）已单独核对，见下表 E-16。

**R1 铁律执行情况**：先只读 `text/ch02_2.txt` → `1-suread.json` 落盘（26 条动作级事件 + 17 个人物 + 17 组数字/日期 + 两条线的观察）→ 才打开本章 md。

---

## 一、四组数

### 1. 逐字组 ｜缺陷 **0**
- 引语块 **10/10** 逐字命中原文，无 `…` 缝合（每块 1 段）、无跨话轮拼接、无一行塞多句。取证：`scripts/chapter.sh --json` 退出码 **0**、`verdict: ok`、`counts` 全 0；另以 `src.find(quote)` 独立实测，10 条全部唯一命中（字符区间见 `4-correspondence.md` 表）。
- 词汇表 **26/26** 例句逐字命中且各命中 1 次（`/usr/bin/grep -F -c`，全 rc=0；`scripts/check_vocab.py` 本章 FAIL=0、WARN 0）。
- 另：`scripts/verify_corpus.py` 未跑（本次不重取语料，用既有 `text/`）。

### 2. 对应组 ｜**8 成立 / 2 不对应**（块 5、块 9）
- 密度不足 **0**（「为什么这样写」每块 62–108 CJK 字，密度 0.83–0.94）。
- 施事/归属反转 **2**（块 5 读者视角提示、块 9 为什么这样写）——四道机器探针全绿，只有 R4 三问能抓。

### 3. 形态组 ｜**1 处偏离中位数（不构成阻断）**
| 项 | 本章 | 本书众数 / profile | 判定 |
|---|---|---|---|
| H1 写法 | `# 2. The Horatio Combe Institute, Priory Square, Camden` | 众数 `N.`（54/54 章） | 一致 |
| 导航项 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 众数 5 项，同名同序 | 一致 |
| 子项集 | 4 项：中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | 众数 4 项＝profile 子项集 | 一致 |
| 块数 | 10 | 本书中位 7，范围 5–10；profile「mystery-thriller」允许 3–10 | 落在允许区间**上界**，高于中位数 3 块 |

**偏离理由（一行）**：本章是完整的现场勘查章（到达 → 辨认尸体与死因 → 死亡时间 → 双人餐桌 → 无安防 → 办公室与失踪手机 → 抗议者 → 后巷与钥匙 → 漆死的地下室门 → 目击者），可拆的独立引语点明显多于书中中位章节，块数取到本书上限 10；**未超 profile 上限，无实质偏离**。

### 4. 断言组 ｜共核 **29** 条：**阻断 9 / 提示 12 / 已核实为正确 8**

---

## 二、断言明细（四列）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| D-1<br>≡F-1 | md `:13`「漆死而地上留着新漆屑、说明近期有人试着打开过的**后门**」 | 原文 `ch02:375` `…then he noticed **a door under the stairs**. ‘Amy, have you been down here yet?’ Caius walked over and twisted the handle. It wouldn’t budge.`；`ch02:378` `‘I didn’t try it. **Someone’s painted the door shut**,’ Amy said.`；`ch02:381` `‘It’s a town house. **The kitchen and the pantry should be down there.**’`；`ch02:297` `‘**The back door and the gate were both unlocked.**’` | 被漆死、地上有新漆屑、近期有人试图打开过的是**楼梯下的地下室门（通厨房/储藏室）**；后门与院门恰恰都没上锁。md 还与自身 `md:77`「后门与院门却都没上锁」、`md:95`「后门与院门都没上锁」**同章自相矛盾**；原文里「有人试图打开过的后门」这一情节并不存在 | **阻断** |
| D-2 | md `:105`「他还追问了一句『我们以前见过吗』，她却答不上来」 | `ch02:402` `‘**Have we met before?’ she asked** as she straightened herself up, …`；`ch02:408` `‘**No, we’ve met. I’m sure we have.**’`；`ch02:411` `‘**I don’t think so …**’`；`ch02:414` `‘I guess you really must have one of those faces.’` | 提问者是**她**（问卡伊乌斯），不是卡伊乌斯；她**并非答不上来**——她两次作答并坚持「见过」，说没印象的是卡伊乌斯。提问者与作答者双双写反；且与同章 `md:13`「撞上卡伊乌斯后**自称见过他**的亚麻色头发女子」自相矛盾 | **阻断** |
| D-3 | md `:67`「死者那侧是沙拉，对面那位只留下一个罂粟籽面包和一堆碎屑」 | `ch02:131` `‘Dinner time. … **The same salad on both plates.**’`；`ch02:134` `‘The other person filled up on bread,’ Amy said, noting that there was **a roll on Digby’s side plate and just crumbs on his guest’s**. ‘**It’s a fancy one too with poppy seeds in a swirl.**’` | 罂粟籽旋纹**面包卷在死者（Digby）那侧**，客人那侧**只剩碎屑**（客人「filled up on bread」）；两个盘子**都是同一种沙拉**。md 把面包卷与碎屑一并安到客人一侧，又把死者一侧写成只有沙拉——受事与主人对调 | **阻断** |
| D-4 | md `:97`「进出巷口没有视线死角」 | `ch02:315` `‘The alleyway leads onto the main road. There’s a playground opposite, **so no visual on the entrance**.’`（与 `ch02:303` `‘You could get in and out unnoticed.’` 一致） | 原文说巷口入口**看不见**（是视线盲区）；md 的中文按字面读是「没有死角＝看得见」，方向相反，属线索含义反转。若本意是「巷口无人看见」，措辞须改 | **阻断** |
| O-1 | md 全文无「谁发现尸体」「前门异常敞开」 | `ch02:164` `‘Willow Bell, she’s a history student at King’s College and interns on Saturdays,’ Caius said, checking his notes. ‘Came in to do her shift and found him like this. **The front door to the museum was unusually left open** and she just walked straight in. She’s on her way to the station for a cup of tea and a formal interview. I’m going to head over in a minute.’` | md `grep -c Willow`=0、`grep -c 前门`=0；发现人（Willow Bell，King's College 历史系学生、周六实习生）、前门异常敞开、正赴警局做正式笔录——勘查链第一环缺失；而 md `md:57` 读者视角提示却拿「敞开的大门」当既有事实用 | **阻断** |
| O-2 | md 无「地下室门定位 / 用黄铜钥匙试开 / 凶手也进不去」 | `ch02:381` `‘It’s a town house. **The kitchen and the pantry should be down there.**’`；`ch02:384` `…then down the basement steps. **A heavy brass key fit the lock but again he couldn’t get the door to budge.**`；`ch02:387` `‘The door’s been painted shut here too.’ … ‘**If we can’t get in then the killer couldn’t either.**’` | 本章唯一一条明写的**否定性推断**（凶手不可能走这扇门）与门的定位、试钥匙动作全部缺失；md 线索结构只把漆门当物证列出，无推断（与 D-1 同段，可一次修） | **阻断** |
| O-3 | md 无抗议者三人姓名/职业、「三个月没见到一个人」、「那个眨眼的姑娘」、请愿书 | `ch02:221` `The group introduced themselves as Kahurangi, Tākuta and Rawiri.`；`ch02:230` `‘…**I’m a nurse in a GP practice in Kingston.**’`；`ch02:236` `‘**I work in a bank in the City full-time**,’ said Rawiri.`；`ch02:239` `‘**I lecture in physics at UCL**,’ said Tākuta.`；`ch02:260` `‘What visitors? We’ve been here every Saturday morning for the last three months, **and not a soul**,’ said Tākuta.`；`ch02:263` `‘**Only that nice girl who winks at us when she goes on her break**,’ said Rawiri.`；`ch02:266` `‘**She signed our petition.**’ Tākuta handed it over to Caius.` | md `grep -c Kahurangi/Rawiri/Tākuta/winks/请愿` 全为 0。目击范围（谁在周六见过谁）与「馆中除死者外还有一名女性工作人员」是本章关键信息，未出现 | **阻断** |
| O-4 | md 无「这顿饭可能不是约会／是生意往来」的推断 | `ch02:155` `‘**It might not have been a date. A work thing, maybe? A trustee for the museum? A donor?**’`；`ch02:321` `‘**Gut says business**; it’s too creepy in here. …’` | md `grep -c business/生意/约会` 全为 0；读者最想知道的下一层（双人晚餐的性质）缺失 | **阻断** |
| O-5 | md 无抗议者的不在场证明与 mokomokai 来历 | `ch02:285` `‘**The protestors alibied each other.** They were talking strategy in the Covent Garden Wagamama … **the mokomokai were preserved as a way to honour their ancestors by showcasing their tattoos which have specific meanings attached to them. They were kept in special ceremonial spaces, but once the British arrived they started buying them as curiosities and it all gets a bit grim.**’`；`ch02:291` `‘They were pretty chill. **No real motive.**’` | md `grep -c alibi/不在场/Wagamama` 全为 0；「排除」这一侦查动作与 mokomokai 的文化来历（md 只在词汇表留了例句）缺失 | **阻断** |
| D-5 | md `:61`「一杯水里的冰早已化尽」 | `ch02:131` `…**a jug of water** in which any trace of ice had dissolved…` | jug＝壶/罐，非杯 | 提示 |
| D-6 | md `:25`「同一株木兰」、`md:115`「开篇那株…木兰」 | `ch02:20` `The magnolia trees **in the centre of the square** were blooming.`；`ch02:465` `…one of the magnolia trees **in the garden in the square**.` | 解读正当，但原文两处措辞不同，未说同一棵 | 提示 |
| D-7 | md `:87`「当天出现在馆舍门外、并且跟死者起过冲突的人」 | `ch02:257` `‘**A couple of months ago** he threatened to call the police on us because we were upsetting his visitors,’ said Kahurangi.` | 冲突在几个月前，且是**死者威胁报警**，不是他们与死者冲突 | 提示 |
| D-8 | md `:41`/`:45`/`:47`/`:51` 引用引语外内容 | 引语止于 `ch02:116` 的 `…rotting parsnips.`（`Musty. I go foraging on the weekends…` 之后）、`ch02:122` `‘Mr Combe-Watson had an open pack of tissues in one pocket and a packet of menthol cough sweets in the other,’`；`ch02:128` `‘I’ll run the requisite tests, but I don’t think there’ll be any surprises,’` | 属引语选短 + 分析超范围；但 md 以「接着那句」明示，未伪装成引语内内容 | 提示 |
| D-9 | md 引语 2 自 `Horatio Combe was one of those…` 起 | `ch02:92` `‘**It’s an anthropological nightmare,’ Caius said, leading them up the stairs.** ‘Horatio Combe was one of those Victorian adventurer types. …’` | 引语选短，丢掉卡伊乌斯的评语与上楼动作；而 md 中文却写「卡伊乌斯边带同伴上楼」；md 词汇表 `anthropological` 例句正是被丢掉的那半句 | 提示 |
| O-6 | md 无「死者手机尚未找到」 | `ch02:185` `‘Sorry to interrupt, **has the victim’s phone been found?**’`；`ch02:188` `‘**Not yet, sir**,’ the masked figure replied…` | md `grep -c 手机/phone`=0；常规问询，未构成转折 | 提示 |
| O-7 | md 无「制服警员已在广场查访目击者」 | `ch02:92` `…‘**Uniform are already canvassing the square in case anyone saw anything.**’` | md `grep -c 制服/查访`=0；与本章广场现场线直接相关 | 提示 |
| O-8 | md 无邻居 Mrs Bourne 与「这一带一向安全」 | `ch02:435` `‘…**I’ve seen all the vans parked all over the square this morning.**’`；`ch02:447` `‘**I live next door to the museum thingy.**’`；`ch02:453` `‘Mrs, bless you, **Mrs Bourne**. Did you hear that, **Halloumi**. …’`；`ch02:456` `‘**DC Noakes** here will ask you a few questions about yesterday evening.’` | md `grep -c Bourne/狗/Halloumi`=0；本章最后一场戏的另一半缺失；`DC Noakes` 这一警衔未出现 | 提示 |
| O-9 | md 无「Station first」 | `ch02:393` `‘**Station first**,’ Caius said, turning quickly towards the car…` | md `grep -c Station/警察局`=0；下一步去向未交代 | 提示 |
| O-10 | md 无保险逻辑与「两层展品 + 阁楼藏书」的规模 | `ch02:176` `‘…if there was anything with a high value here then **their insurers would’ve made them take precautions**. … **There’s two floors of exhibits and the attic contains Horatio Combe’s library.**’` | md `grep -c 保险/insurer`=0；「两层展品」未出现（仅「阁楼里的藏品账本」对应 ledger） | 提示 |
| O-11 | md 引语 2 起点偏后 | 同 D-9 | 同 D-9（漏单视角再记一次） | 提示 |
| O-12 | 开头「两分钟闲聊」整段无引语块 | `ch02:23`–`:85`（两分钟计时、meme、‘not today, Satan’、‘A consummate professional’、六位数薪水、‘thirty-five not eighty-five’、Callie 母亲脱鞋、cease and desist） | 本章聚焦命案现场，开篇属铺垫而非侦查链；但 `meme` 一节是结尾女子「recognised him from the damn memes」的伏笔，md 未把这条线接上 | 提示 |
| E-16 | 任务专属判据：勘查线／旁观线分列，结尾旁观者进入「线索结构」 | md `:13`「…**旁观线：撞上卡伊乌斯后自称见过他的亚麻色头发女子，章末从木兰树后探出身，看着他离开。**」 | **成立**——两条线分列，结尾旁观者已写入「线索结构」。（注：旁观线措辞「自称见过他」正确，反倒是块 9 的「为什么这样写」与之矛盾，见 D-2） | 提示（成立） |

---

## 三、已核实为正确（防误修，固定一节）

以下写法**看着像错、回原文核对后成立**，后续任何人不得以「读着不对」为由改动，除非能给出反证。

1. **原句 3 的死因归属**：md `:41`「法医巴里给出死因：毒芹」——`ch02:107` `‘Hemlock,’ Barry said.` 说话人无误。
2. **原句 4 的时间窗与「没有意外」**：md `:51`「傍晚七点到九点之间……该做的检验都会做，但不会带来意外」——`ch02:128` `‘By the looks of him he died in the early evening. I’d say somewhere between 7 and 9 p.m.’` 与同话轮 `‘I’ll run the requisite tests, but I don’t think there’ll be any surprises’`，同为 Barry 的话。
3. **原句 6 的说话人**：md `:71`「问到有没有安保，卡伊乌斯答得很干脆」——`ch02:170` `‘Nope,’ Caius said. ‘No cameras, or alarms, nothing. Just a lock with a key.’`；md 由「保险逻辑」推出「无人觊觎」的解读有 `ch02:176` 支撑。
4. **原句 7 的陈述方向**：md `:81`「多次拒绝他们政府的请求，要把这里被不道德地保管着的人类遗骸送回 Aoteara」——`ch02:212` `‘The Horatio Combe Institute has refused multiple requests from our government to return human remains unethically kept here to Aoteara’`，施事与 `from / return … to` 方向均正确。
5. **原句 9 的外貌描写**：md `:101`「乱髻、素黑棒球帽压得很低、衣着宽松暗淡、帽檐下好奇的火花烧得很亮」——`ch02:402` `…tied up into a messy bun at the back of her head and a plain black baseball cap was pulled close over her eyes. … Her clothes were baggy and dull-coloured. But a spark, a curious flame in her eyes that peeked out from under the cap burnt bright.`（该块**只有**「为什么这样写」末句错，见 D-2）。
6. **原句 10 逐字对应**：md `:111`——`ch02:465` `…peeked out from behind one of the magnolia trees in the garden in the square. She watched him leave, hoping he’d return.`（措辞问题见 D-6）。
7. **词汇表 26 条例句**：全部逐字命中且各命中 1 次（`/usr/bin/grep -F -c -- "<例句>" …/text/ch02_2.txt`，全 rc=0）；`scripts/check_vocab.py` 本章 FAIL=0、WARN 0；档位分配（mokomokai / Aoteara / taxidermy ⭐⭐⭐；shillings / kerfuffle / traipsed ⭐⭐；kangaroo / dust / key ⭐）与词频难度相称，无注水、无生造词条。
8. **机器层**：`bash scripts/chapter.sh "<ch02 md>" --json` 退出码 **0**、`verdict: ok`；引语 10/10 逐字；`counts` 全 0（blocks 10 / segments 10 / segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0）；CJK 占比 0.83–0.94；`bookform.py` 显示 H1/导航/子项三项与本书众数完全一致。

---

## 四、取证记录（R5-补：凡「零命中/查无」类断言必须自证）

```
/usr/bin/grep -c "Willow" "…/ch02 caius and matt reach the institute.md"            → 0，退出码 1
/usr/bin/grep -c "前门" "…/ch02 caius and matt reach the institute.md"               → 0，退出码 1
/usr/bin/grep -c "手机\|phone" "…/ch02 caius and matt reach the institute.md"        → 0，退出码 1
/usr/bin/grep -c "Kahurangi\|Rawiri\|Tākuta" "…/ch02 caius and matt reach the institute.md" → 0，退出码 1
/usr/bin/grep -c "alibi\|不在场\|Wagamama" "…/ch02 caius and matt reach the institute.md"   → 0，退出码 1
/usr/bin/grep -c "business\|生意\|约会" "…/ch02 caius and matt reach the institute.md"      → 0，退出码 1
/usr/bin/grep -c "Bourne\|狗\|Halloumi" "…/ch02 caius and matt reach the institute.md"     → 0，退出码 1
/usr/bin/grep -c "制服\|查访" "…/ch02 caius and matt reach the institute.md"               → 0，退出码 1
/usr/bin/grep -c "保险\|insurer" "…/ch02 caius and matt reach the institute.md"            → 0，退出码 1
/usr/bin/grep -c -- "地下室" "…/ch02 caius and matt reach the institute.md"               → 0，退出码 1
/usr/bin/grep -c -- "厨房" "…/ch02 caius and matt reach the institute.md"                 → 0，退出码 1
/usr/bin/grep -c -- "winks\|请愿" "…/ch02 caius and matt reach the institute.md"           → 0，退出码 1
/usr/bin/grep -n -E "painted the door shut|door under the stairs|back door and the gate|Have we met before" …/text/ch02_2.txt
    → 输出行号 375 / 378 / 297 / 402（依次为 “door under the stairs” 375、“Someone’s painted the door shut” 378、
      “The back door and the gate were both unlocked.” 297、“‘Have we met before?’ she asked” 402），退出码 0
/usr/bin/grep -n -E "No, we’ve met|I don’t think so" …/text/ch02_2.txt
    → 输出行号 408 / 411，退出码 0
```
（工具说明：按 R5-补，一律用 `/usr/bin/grep` + 显式文件路径，**不用 `git grep`/rg 默认 ignore 规则**——`text/` 被 `.gitignore` 排除，`git grep` 在该目录永远「查无」，其退出码 1 与「真查无」不可区分。）

---

## 五、结论

- **四组数**：逐字 **0 缺陷**（10/10 引语 + 26/26 例句）｜对应 **8 成立 / 2 不对应**（块 5、块 9）｜形态 **3/4 项与众数一致，块数 10 在允许区间上界**（理由已写）｜断言 **29 条：阻断 9 / 提示 12 / 已核实为正确 8**。
- **阻断型 9 条**：D-1（≡F-1）漆门写成后门 + 同章自相矛盾｜D-2 块 9 说话人与作答者双双写反｜D-3 块 5 面包/沙拉归属写反｜D-4 块 8 巷口视线方向写反｜O-1 漏发现人 Willow Bell 与前门敞开｜O-2 漏地下室门定位与「凶手也进不去」｜O-3 漏抗议者身份/目击范围/眨眼的姑娘｜O-4 漏「可能不是约会而是生意」｜O-5 漏抗议者不在场证明与 mokomokai 来历。
- **最要紧的一条**：**D-1/F-1**——md 把「被漆死、地上有新漆屑、近期有人试图打开过」的门写成**后门**，而原文这扇门是**楼梯下通往厨房/储藏室的地下室门**；后门与院门在原文里恰恰**都没上锁**（`ch02:297`）。md 自己在 `md:77` 与 `md:95` 又两次写「后门与院门都没上锁」，同章三处自相矛盾，且「有人试图打开过的后门」在原文里并不存在。这条同时污染了「线索结构」这条读者据以复盘的线索清单，且与 O-2 的排除性结论（「If we can’t get in then the killer couldn’t either」）是同一段原文——一处修正可同时解决两条阻断。
