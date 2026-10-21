# ch06 人工审查 · R5 判定表

书：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/`
本轮：R0–R5 人工审查（唯一真值＝`text/ch06_chapter_6.txt`）｜只出指令不改稿
配套：`review/ch06/1-suread.json`（R1）· `review/ch06/2-machine.json`（R2，退出码 0）· `review/ch06/3-diff.md`（R3 三张单子＋R4 逐块对应）

**档位口径**：阻断＝与原文不符或缺失（且有逐字证据）；提示＝措辞正当但与原文有出入；假红＝初判报警被原文证伪；跳过＝本轮未核。

---

## 1. 判定表（15 行）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | `ch06 chapter 6.md:11`「打给母亲那通」＝Diana 打给母亲 | `text/ch06_chapter_6.txt:90`「Diana’s iPhone lit up on the kitchen table.」（手机亮屏＝**来电**）；`:108`「Who was it? Your mom or your sister?」；`:111`「My mom.」；对照第二通 `:171`「She was getting a call.」`:174`「It’s me,” Alba said.」 | 两通电话**都是打进来的**：第一通母亲→Diana，第二通 Alba→Diana。md 用「打给母亲那通／妹妹打来那通」并列，把第一通方向写反（§⑥ 施事反转） | **阻断** |
| A2 | `md:11`「说她是在替**姐姐**开脱」＝被开脱者是 Diana 的姐姐 | `text/ch06_chapter_6.txt:162`「Are you going to start making excuses for your **sister** now?」；`:168`「When you say things like that, you’re rationalizing it.」（说话人 Carlos）；关系方向 `text/ch05_chapter_5.txt:549`「She, on the other hand—who was **six years older than Alba**—did sometimes express her bewilderment. She called her sister selfish」；本书口径 `00_概述.md:74`「**妹妹**，两个孩子的母亲。」、`00_概述.md:68`「**妻子的姐姐**」 | 被开脱的是 **Alba＝妹妹**（比 Diana 小六岁）。md 写「姐姐」＝关系方向反 | **阻断** |
| A3 | `md:14`「走到当面说她「在替**姐姐**开脱」」 | 同 A2（`text/ch06_chapter_6.txt:162`、`:168`；`text/ch05_chapter_5.txt:549`；`00_概述.md:74`） | 同 A2 的第 2 处 | **阻断** |
| A4 | `md:13`「他们知道这是她跟母亲或**姐姐**说话时的调子」 | `text/ch06_chapter_6.txt:93`「All of them knew that this was the tone Diana used when she was talking with her mother or **her sister**.」 | 「her sister」＝Alba＝妹妹。md 写「姐姐」＝关系方向反 | **阻断** |
| B1 | `md:14`「插着的**充电器**」 | `text/ch06_chapter_6.txt:51`「Diana, that’s not going to happen. **You never leave anything charging.** You even unplug the microwave. And you check everything a thousand times before bed.」；全章 `charger` 零命中（§3 命令 4） | 原文只说泛指「anything charging」，未点名充电器；语义等价但属具体化 | 提示 |
| B2 | `md:15`「一个**不肯回应那五个小时**」 | `text/ch06_chapter_6.txt:120`「At urgent care? At nine p.m.? They’ve been at urgent care with all three kids for five hours?」→ `:123`「**Yeah, they just got out.**」 | 她字面上**答了**；md 想说的应是「不肯接 Carlos 对延误与丈夫失职的指责」（`:132`–`:144`） | 提示 |
| B3 | `md:12`「孩子**一律**套上**反光外套**」 | `text/ch06_chapter_6.txt:9`「On the few occasions when they had **no excuse**, Diana would dress Brisa and Tomás in **reflective hoodies**」 | hoodie＝连帽衫非外套；「一律」与「仅在没有推不掉的理由时」不符 | 提示 |
| B4 | `md:13`「从母亲讲起的那桩**旧事**传到姐妹俩手上」 | `text/ch06_chapter_6.txt:219`「She said the mediums came up to you **yesterday** at Finestrelles?」；`text/ch05_chapter_5.txt:336`「some old women went up to her **yesterday** at Finestrelles」 | 灵媒一事发生在**昨天**，非旧事（其余结构：母亲讲起→传到姐妹俩 ✓） | 提示 |
| B5 | `md:11` 同句内「**母亲**白天怕孩子在公园、在学校出事」＋「打给**母亲**那通」 | `text/ch06_chapter_6.txt:6`（Diana＝孩子的母亲）、`:111`「My mom.」（Diana 的母亲＝Carmen） | 一句之内「母亲」兼指两人，一词二义，易把两通电话的对象混为同一人 | 提示 |
| B6 | `md:129`「**这个家里**有两个人急着把惊吓收尾」 | `text/ch06_chapter_6.txt:171`–`:180`（Alba 与孩子在急诊/回家路上，不在这个家里） | 「这个家里」指代不准（Alba 不是该家成员）；建议「这两个人」 | 提示 |
| B7 | `md:73`「作者还顺手让这通电话差点烤焦了自家那份披萨：**丈夫的一声抱怨**，把急诊室里的五个小时和厨房里的晚饭接在了同一处」 | `text/ch06_chapter_6.txt:99`「**“Well, this almost burned thanks to you,” she said**, crouching to check on the pizza.」（说披萨快烤焦的是 **Diana**）；丈夫的抱怨＝`:120`/`:132`/`:144` | 后半句为真（Carlos 在厨房抱怨五个小时，把急诊与晚饭并置）；但冒号使读者把「烤焦」的因由挂到「丈夫的一声抱怨」上，而那句抱怨出自 Diana | 提示 |
| C1 | `md:13`「这是她跟母亲或姐姐说话时的**调子**」——tone 属于打电话的对端 | `text/ch06_chapter_6.txt:93`「All of them knew that this was the tone **Diana used** when she was talking with her mother or her sister.」 | **报警被证伪**：tone 是 **Diana 本人**的调子，md 归属正确（本行只错在 A4 的「姐姐」，已单列） | 假红 |
| D1 | 词汇表 21 条的**释义与 ⭐ 星级**是否合理 | 本轮只核了 21 条例句的逐字（全部命中 1 次），未逐条复核释义/档位 | 未核 | 跳过 |
| D2 | frontmatter（`:2` 状态: 未读／`:3` modified／`:4` source_text）字段合规性 | `chapter.sh` 未纳入该项 | 未核 | 跳过 |
| D3 | `md:129`「两套说法都把她**真正害怕**的那部分挡在了外面」的文本依据 | 文本无对应句（属读者解读）；`text/ch06_chapter_6.txt:147`/`:180` 两段只呈现两套说法本身 | 未核（解读层，不作阻断依据） | 跳过 |

**判定表计数：15 行 ＝ 阻断 4（A1–A4）· 提示 7（B1–B7）· 假红 1（C1）· 跳过 3（D1–D3）。**

---

## 2. 四组报数（只报这四组）

| 组 | 口径 | 结果 |
|---|---|---|
| **逐字** | md 内英文引语与词表例句是否与原文逐字一致 | 27 项（6 条引语 ＋ 21 条例句）→ 命中 **27**，不符 **0**；6 条引语在 `text/ch06_chapter_6.txt` 各命中 1 次（无 `…` 缝合、无跨话轮拼接、无一行塞多句） |
| **对应** | 每个引语块的中文分析是否在讲这句引语（R4 人判） | 6 块 → 对应 **6/6**；固定三问 18 问全查：主语 6/6 对、受事 6/6 对、归属方向 5/6 对（块 5 后文 Carlos 的 `your sister` → 妹妹，md 写「姐姐」＝A2/A3） |
| **形态** | H1／导航项／子项集／块数 vs 本书众数；中文密度 | 4 项全过、**0 偏离**：H1「06. Chapter 6」`h1_shape_ok=true`；导航项 5（`nav_count_ok=true`）；子项集 [中文理解, 关键词, 为什么这样写, 读者视角提示] 与 `profile_subitems` 一致；块数 6 落在 `block_range [5,8]`、`block_median 7.0` 内（`profile: novels`，`baseline: book`）；中文密度 0.81–0.93 全部达标（`cjk_low 0`；「关键词」项 cjk_ratio 0.0 属设计如此，不计） |
| **断言** | 本判定表的断言条数与分档 | **15 行** ＝ 阻断 4 / 提示 7 / 假红 1 / 跳过 3 |

---

## 3. 取证命令（「查无」类断言三件套：命令＋输出＋退出码）

工作目录 `/Users/jcxs2014/Documents/Works/EnglishRead`；`MD`＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch06 chapter 6.md`；`TX`＝同目录 `text/ch06_chapter_6.txt`；**一律用 `/usr/bin/grep` + 显式路径**（`text/` 被 `.gitignore:132 notes*/books/**/text/` 排除，`git grep` 与尊重 ignore 的 rg 在此永远查无，不可区分「真查无」）。

1. `/usr/bin/grep -n -E "姐姐|妹妹" "$MD"` → 命中 3 行（`:11`「说她是在替姐姐开脱」；`:13`「她跟母亲或姐姐说话时的调子」；`:14`「走到当面说她「在替姐姐开脱」」＋同行「替妹妹查一下也做不到」；`:87`「妹妹一再说自己看得很清楚」）→ **退出码 0**
2. `/usr/bin/grep -n -E "打给|打来" "$MD"` → 命中 2 行（`:11`「打给母亲那通」「妹妹打来那通」；`:13`「明天一早就打给那个总是知道该怎么办的朋友」）→ **退出码 0**
3. `/usr/bin/grep -c -i -E "christmas" "$TX"` → 输出 `0` → **退出码 1**（本章正文无 Christmas 字样；「离圣诞节还有两天」来自 `text/ch05_chapter_5.txt:315`，非本章）
4. `/usr/bin/grep -n -i -E "charger" "$TX"` → 无输出 → **退出码 1**（全章无 charger／充电器；`text/ch06_chapter_6.txt:51` 只有「You never leave anything charging.」）
5. `/usr/bin/grep -n -w -E "sister" "$TX"` → 命中 4 行：`:93`、`:108`、`:144`、`:162`，四处均指 Alba → **退出码 0**
6. `/usr/bin/grep -rn -E "older than Alba" "$B/text/"` → 命中 1 处：`text/ch05_chapter_5.txt:549`「She, on the other hand—who was six years older than Alba—did sometimes express her bewilderment. She called her sister selfish…」 → **退出码 0**
7. `/usr/bin/grep -n -w -E "brother-in-law" "$TX"` → 命中 2 行：`:117`「My brother-in-law is on his way to pick them up.」`:132`「Couldn’t your brother-in-law have gone sooner…」 → **退出码 0**（Diana 所说的 brother-in-law＝Alba 的丈夫 Juan，见 `text/ch05_chapter_5.txt:147`）

**取证命令行留档**：以上 7 条均为显式路径 `/usr/bin/grep` 交替匹配（`-E`）与单词匹配（`-w`），输出与退出码如上；「查无」只有第 3、4 两条（均为真查无，退出码 1）。

---

## 4. 阻断清单（4 条）

| 断言 | 证据区间 | 为什么阻断 |
|---|---|---|
| `md:11`「打给母亲那通」 | `text/ch06_chapter_6.txt:90`、`:108`、`:111`（并对照 `:171`、`:174`） | 电话方向是本章两通电话的骨架。原文两通都是**打进来**的：`:90` 手机亮屏＝来电，`:108` Carlos 问「Who was it? Your mom or your sister?」→`:111`「My mom.」；第二通 `:171`「She was getting a call.」`:174`「It’s me,” Alba said.」md 写成「Diana 打给母亲」＝§⑥ 施事/归属反转，读者会据此误判两人的行动线 |
| `md:11`「说她是在替姐姐开脱」 | `text/ch06_chapter_6.txt:162`「Are you going to start making excuses for your sister now?」、`:168`；关系方向 `text/ch05_chapter_5.txt:549`；`00_概述.md:74`「妹妹，两个孩子的母亲。」 | Carlos 指的是 **Alba（妹妹）**；`ch05:549` 明写 Diana 比 Alba 大六岁。本书总览自己也是「Diana＝妻子的姐姐、Alba＝妹妹」，md 与本书自身口径冲突 |
| `md:14`「走到当面说她「在替姐姐开脱」」 | 同上（`text/ch06_chapter_6.txt:162`、`:168`；`text/ch05_chapter_5.txt:549`） | 同源错误的第 2 处，且出现在「人物弧线」字段——弧线段的施事/受事方向写错，属 S3 §⑥ 家族 |
| `md:13`「他们知道这是她跟母亲或姐姐说话时的调子」 | `text/ch06_chapter_6.txt:93`「All of them knew that this was the tone Diana used when she was talking with her mother or **her sister**.」 | 同源错误的第 3 处；且此句正是外层预审疑点①所指的行，tone 归属本身经核对**正确**（见 C1 假红），错的只有「姐姐」这个方向词 |

---

## 5. 修复指令（最小改法，逐条可直接执行）

1. `md:11`「打给母亲那通」→「**母亲打来那通**」（与同句「妹妹打来那通」对称）。
2. `md:11`「说她是在替姐姐开脱」→「说她是在替**妹妹**开脱」。
3. `md:14`「走到当面说她「在替姐姐开脱」」→「在替**妹妹**开脱」。
4. `md:13`「她跟母亲或姐姐说话时的调子」→「她跟母亲或**妹妹**说话时的调子」。
5. （可选，提示级）`md:14`「插着的充电器」→「**一直没关的电器**」或直接引原文「you never leave anything charging」。
6. （可选，提示级）`md:15`「一个不肯回应那五个小时」→「一个**不肯接丈夫对那五个小时的抱怨**」。
7. （可选，提示级）`md:73` 拆成两句：「作者还顺手让这通电话差点烤焦了自家那份披萨（她进办公室前把烤箱托付给了丈夫）：Carlos 在厨房里对那五个小时的抱怨，又把急诊室和晚饭接在了同一处。」
8. （可选，提示级）`md:12`「孩子一律套上反光外套」→「孩子**有时**被套上**反光连帽衫**」；`md:13`「那桩旧事」→「**昨天那桩事**」；`md:129`「这个家里有两个人」→「**这两个人**」；`md:11`「母亲白天怕孩子」→「**当妈妈的她**白天怕孩子」。
9. （可选，补覆盖）增补一个引语块取 `text/ch06_chapter_6.txt:87`（Carlos 劝她吃成人剂量退黑素），可同时兑现 `md:27` 与 `md:63` 两处「那片药」的读者提示，并带出「六岁」「不到五十磅」「明天我们就和家人团聚」三个原文数字。

---

## 6. 已核实为正确

> 以下条目**初看像错**，回原文核对后成立。写入本节者，后续复核/修复**不得**以「读着不对」为由改动。

1. `md:13`「电话那头近乎喊叫……他们知道这是**她**跟母亲或姐姐说话时的调子」——tone 属 **Diana 本人**：`text/ch06_chapter_6.txt:93`「All of them knew that this was the tone **Diana used** when she was talking with her mother or her sister.」（疑点①的一半，回原文成立；本行只需改「姐姐」，见 A4）
2. `md:87`「（妹妹一再说自己看得很清楚）」——说话人确为 **Alba（妹妹）**：`text/ch06_chapter_6.txt:270`「No. I didn’t. It was very clear what was happening.」（说话轮次锚点：`:249` Diana「I don’t know, **Alba**. Let me think of someone who knows about this stuff.」与 `:285`「No, **Alba**. It’s late.」锁定奇数轮＝Alba、偶数轮＝Diana）
3. `md:11`「妹妹打来那通」——方向正确：`text/ch06_chapter_6.txt:171`「Half an hour later, Tomás… **She was getting a call.**」`:174`「**It’s me,** Alba said.」
4. `md:11`「孩子在急诊待了五个小时」——数字正确：`text/ch06_chapter_6.txt:120`「They’ve been at urgent care with all three kids for **five hours**?」
5. `md:11`「（离圣诞节还有两天）」——正确，但依据在**上一章**：`text/ch05_chapter_5.txt:315`「You’re going to be at urgent care for no reason, **two days before Christmas**, when there’s hardly anyone working.」（本章正文无 Christmas 字样，见 §3 命令 3）
6. `md:11`「全章落在她答应「明天一早就打」上」——正确：`text/ch06_chapter_6.txt:285`「No, Alba. It’s late. **I promise I’ll call her first thing in the morning.**」（说话人＝Diana，被叫方＝Alba）
7. `md:14`「替妹妹查一下也做不到（她只说自己受不了去查这件事）」——正确：`text/ch06_chapter_6.txt:267`「Tomorrow I’ll call. But try to forget about it for now, OK? You probably just imagined it.」＋`:270`「No. I didn’t. It was very clear what was happening.」＋`:282`「Call Nuria now. Please.」
8. `md:12`「推不掉的生日派对照样去」——正确：`text/ch06_chapter_6.txt:9`「On the few occasions when they had **no excuse**, Diana would dress Brisa and Tomás in reflective hoodies.」
9. `md:12`「白天绕开公园」——正确：`text/ch06_chapter_6.txt:6`「Her blood went cold **in the park** because it was such an obvious simulacrum…」
10. `md:15`「本章先用**三段**叙述把恐惧写成一层层外推的推演（公园→学校→夜里的房间）」——三段对应正确：`text/ch06_chapter_6.txt:6`（公园）→`:9`（学校：「now they also took place at the school」）→`:12`（夜里的房间）
11. `md:21`「在体重不到五十磅的小小身体里」——逐字对应：`text/ch06_chapter_6.txt:6`「in creatures that weighed **less than fifty pounds**」
12. `md:45`「把光洒在她身上……直到能看清她的胸口或后背正有节奏地起伏」——`her` 指 **Brisa**：`text/ch06_chapter_6.txt:12`「approach **Brisa** like a sleepwalking explorer, and carefully cast **her** with light until she could see that **her** chest or back was inflating rhythmically.」
13. `md:73`「三件手续性事实：拍片、没问题、等单子」——对应正确：`text/ch06_chapter_6.txt:147`「the baby is fine. They did an X-ray, and there’s nothing wrong. Now they’re just waiting for the discharge papers」
14. `md:73`「她漏掉了时间，漏掉了在场的人数」——该句只提 the baby，无三人、无五小时（对照 `text/ch06_chapter_6.txt:120`「all three kids for five hours」，五小时是 Carlos 说的）⇒ 「压缩」的判断成立
15. `md:87`「那个不斜眼的灵媒」——逐字对应：`text/ch06_chapter_6.txt:276`「**The one who isn’t cross-eyed** told me that one day, I wouldn’t know how to get out of there, either.」
16. `md:87`「从该找谁求助，到「也许只是你想多了」的收尾」——对应正确：`text/ch06_chapter_6.txt:267`「You **probably just imagined it**.」（说话人＝Diana）
17. `md:12`「这一章落在全书弧线的下沉段」——与本书总览节点划分一致：`00_情感节点.md:58`「## 节点六：恐惧越过家门（ch06-ch07）」；`:64` 的关键引语正是本章原句 2
18. `md:14`「丈夫从逐条帮她数检查项」——对应正确：`text/ch06_chapter_6.txt:51`「You never leave anything charging. You even unplug the microwave. And you check everything a thousand times before bed.」（三项清单一一对应；只有「插着的充电器」的具体化问题，见 B1）
