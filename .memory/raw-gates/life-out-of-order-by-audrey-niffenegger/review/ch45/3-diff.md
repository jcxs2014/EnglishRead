# ch45 oliver practices piano — 对账单（R3）

- 原文：`text/ch45_oliver_practices_piano.txt`（464 行；两段时间线：1975-02-24 Alba 24 / Oliver 38，Alba 叙述；2041-10-30 Oliver 13，Oliver 叙述）
- 精读：`ch45 oliver practices piano.md`（153 行）
- 机器层：`2-machine.json` rc=0，verdict=ok，10 块 / 10 段引语全逐字，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5 条，H1 `45. Oliver Practices Piano`，words 4647，block_hint：10 块偏离本书常见区间 3–9（未超硬上限，只报不判红）

## 〇、先核作业单点名的两个坑

| 检查项 | 结果 | 取证 |
|---|---|---|
| 1975 段有没有把奥利弗写成「少年」 | **没有**。`/usr/bin/grep -c "少年" "ch45 oliver practices piano.md"` → 0，rc=1 | 全文无「少年」；「十三岁」只用于他自述的**当年**（`:66` “I was thirteen”）与 2041 机场段 |
| 亲属称谓是否统一「叔叔」 | **是**。`grep -c "叔叔"` → 1（`:153`「被叔叔派来的伊莎多拉」）；`grep -c "舅舅"` → 0 | 原文 `:214` “You must call him Uncle Stephen.”、`:362` “Your Uncle Stephen sent me.” 均为父系叔父 Stephen |
| 1975 段的主角年龄 | **未写**（Alba 24 / Oliver 38 均无）；2041 段「十三岁」写对（`:11` `:14` `:153`） | `grep -c "三十八"`→0、`grep -c "二十四"`→0；年龄锚点见 L7 |

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | **父母的核心叮嘱：「别告诉他时间旅行的事」**（母亲先说「什么都别告诉他」，父亲补充明确；母亲又要求他严格管住自己「为了我，为了我们」）——这是 2041 段唯一的行动约束，也是后续章节的前提 | `:245` ““Don’t tell him anything,” my mother said with surprising force.”；`:253` ““Don’t tell him about the time traveling,” my father clarified.”；`:261` ““Just don’t—travel. Be very strict with yourself.” My mother softened her voice. “For me. For us. Try very hard, okay?”” | `grep -c "时间旅行"`→0；全篇无「别告诉」类表述；`md:15` 只把「手机」列进物件清单 | **阻断**（关键事件未进任何一块或导航，且 md 未写取舍理由） |
| L2 | 两部手机：他讨了很久的高配小米（给官方看、全息护照）+ 看不出牌子的破解旧机（无法被追踪，用来联系父母）；父亲用全息影像给他看叔叔——照片里叔叔抱着婴儿时的他，「他会叫你 Oliver」 | `:208` “my father put two phones on the table in front of me, one the fancy Xiaomi I had been begging for, the other a cheap-looking, battered one.”；`:226` ““This one is hacked—you can use it without anyone tracking it.””；`:214` ““You must call him Uncle Stephen. He doesn’t use his Chinese name now. He will call you Oliver.”” | `grep -c "手机"`→1（仅 `md:15` 物件清单里的一个词）；无「小米」「全息影像」 | 提示（改名换姓的来处被抽空，只剩 `md:13` 一句「护照上…都不真」） |
| L3 | 扫描时他调动的固定记忆：小时候常来的「林黛玉」（不是真名）、面部被酸液毁伤、声音低柔的女人，他发烧时给他煮姜茶唱歌 | `:327` “I summon the same memory I always use for scans: I think of a woman who used to visit my mother when I was little. We called her Lin Daiyu, but that was not her name. Her face had been scarred in an acid attack.”；`:328` “One afternoon when I was sick in bed with the flu, Daiyu made me ginger tea and sang to me.” | `grep -c "林黛玉"`→0 | 提示（「用同一段记忆骗过扫描」是他此后每次过关的办法，难点在此） |
| L4 | 书店礼物：Oliver Twist / Peter Pan / About a Boy / **Watership Down**（「讲兔子们必须找新家，你会喜欢」） | `:393` ““Oh, here, Oliver, this one is about rabbits who must find a new home, you’ll like this.” She hands me a book with a pretty rabbit on the cover: Watership Down.” | `grep -c "兔子"`→0、`grep -c "华特西"`→0 | 提示（「找新家」正好是这一章的主题回声，被整段略去） |
| L5 | 那句问答：「我叔叔人好吗？」→ 伊莎多拉查了「间隙」→「不。」→ 随即改口「那不是我说的，是别人说的……一切在最好的可能世界里都是最好的」 | `:447` ““Not about flying. I am nervous about arriving. I don’t remember my uncle. Is he kind?””；`:451` “Isadora consults the Interstices. “No,” she says.”；`:459` ““Oh, that isn’t what I say. Others say that. Don’t worry, Oliver. All is for the best in the best of all possible worlds.”” | 无（`md:153` 只到「接过一杯一杯粉色的酒」） | 提示（全章最重的一记伏笔：来伦敦投奔的人「不善」，而说者当场收回） |
| L6 | 「当你我都到了中年，我们有时会断断续续聊上好几天，中间大段空白；我们已经说了太多，可以彼此安静」 | `:124` “When you and I are both middle-aged we sometimes spend days talking intermittently, with long gaps between; we’ve already said so much that we can be quiet with each other.” | 无（`grep -c "中年"`→0） | 提示（这句把 Alba 与 Oliver 的关系钉在「中年伴侣」，是两人关系的硬证据） |
| L7 | 年龄锚点：1975 段 Alba 24 / Oliver 38；2041 段 Oliver 13 | `:18` “Monday, February 24, 1975 (Alba is 24, Oliver is 38)”；`:166` “Wednesday, October 30, 2041 (Oliver is 13)” | 只写了 2041 的「十三岁」；1975 的两个年龄全无 | 提示（本书年龄表最易错的一处，建议明写） |
| L8 | 上海童年的质地：父母都是诗人；父亲在长餐桌靠窗那端写作、中间书堆像山脊把桌子分成「写作侧」与「吃饭侧」；他喜欢老式电脑；最好的朋友是同楼的 Zǐ Yì，「我到现在还想他」 | `:142` “My mother and father were both poets. … In the middle of the table were piles of books, like a mountain range dividing the table”；`:156` “I had a friend in my building, Zǐ Yì, my best friend. … I still miss him.” | 引语块 5 只收了软禁与挨欺负；餐桌、书堆、Zǐ Yì 全无 | 提示（`md:61` 已覆盖软禁线，属取舍，但「最好的朋友」是孤儿感的关键） |

## 二、编（md 有、原文无）

无。逐条回查：`md:13`「护照上除了瞳色与身高都不真」有 `:232` “everything except my eye color and height quite untrue”；`md:14`「把父母留在栏杆那边」有 `:281` “They hug me and duck under the rope.”；`md:15`「两条线都用具体物件承重」有 `:176`（衣物）`:208`（手机）`:274`（证件）`:301`（扫描）`:393`（书）；`md:13`「来接他的人笑着，他却先想跑」有 `:347` “my first instinct is to run”。

## 三、错（两边都有但不一致）

无对照级错。两处需记账：

| # | 断言位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | `md:11` | 「一九七五年二月，阿尔芭记下奥利弗一天练琴十几小时的样子，问出一段她不知道的来历：他十三岁被父母用别人的试音录像送进皇家学院」 | 事实链正确（`:66` “we sent someone else’s audition video. I had never touched a piano. I was thirteen”），但 1975 段那句「他十三岁」是**回述**，容易被读成 1975 年他十三岁 | 假红（句子主语是「他…被送进」，指 2041 的当年；未与 1975 的 38 岁混，见 〇 节取证） |
| E2 | `md:15` | 「二〇四一年换成奥利弗自述，中间隔着几十年与一次跨时旅行」 | 1975 到 2041 是 66 年；Oliver 生于 2028 年 8 月（`ch44:121`），1975 年他尚未出生，故 1975 段本身就是回溯 | 假红（「跨时旅行」指这段关系的性质，措辞笼统但不错） |

## 四、归属方向复核（R4 三问）

- 块 2 “we sent someone else’s audition video” ⇄ `:66`：施事是**父母/家里**（母亲托关系），受事是皇家学院；md `:31`「送去的是别人的试音录像」——未写成「他自己送的」，方向正确。
- 块 3 “I spoke no English, so we used translation robots” ⇄ `:75`：we＝**Oliver 与 Baxter 太太**；md `:41`「他不会英语，和老师靠翻译机器人说话」——正确。
- 块 5 “boys at school would bully me because my parents were dissidents” ⇄ `:147`：施事是**同学**，原因是父母身份，受事是他；md `:61` 未倒因为果。
- 块 6 “I was born in a particularly beautiful place and time, to parents who were kind” ⇄ `:157`：说话人＝**Oliver**，评价对象＝自己的出生地与父母；md `:71`「自己出生在一个格外美的地方」——正确。
- 块 7 “She packed every piece of clothing I owned” ⇄ `:176`：施事＝**母亲**；「父母不指望我回来」的判断者＝**Oliver 自己**（`:176` “I understood for the first time”）；md `:81`「他才明白：父母并不指望他回来」——判断归属正确，未写成母亲说出口。
- 块 9 “Someone says, ‘Oliver!’ and grabs my arm” ⇄ `:347`：抓人者是**伊莎多拉**（`:352` 自报姓名）；md `:101`「有人在身后喊…一把抓住他的手臂」→ `md:153`「被叔叔派来的伊莎多拉领走」——方向正确。
- 「叔叔」指向：`:214` “You must call him Uncle Stephen.”——叔叔是**父系**的 Stephen，也是**雇伊莎多拉的人**（`:362` “Your Uncle Stephen sent me”）；md `:153`「被叔叔派来的伊莎多拉」——正确。
