# ch47 the air becomes music — 对账单（R3）

- 原文：`text/ch47_the_air_becomes_music.txt`（402 行；2041-11-01，Oliver 13，第一人称**现在时**叙述）
- 精读：`ch47 the air becomes music.md`（152 行）
- 机器层：`2-machine.json` rc=0，verdict=ok，10 块 / 10 段引语全逐字，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5 条，H1 `47. The Air Becomes Music`，words 3650，block_hint：10 块偏离本书常见区间 3–9（未超硬上限，只报不判红）

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | **本章题眼「人生就是一场长长的试奏」全无** | `:216` “After he is gone Mrs. Baxter says, “Well, young Oliver, the first lesson is that life is one big long audition.” She laughs, and though I don’t understand the joke I laugh, too.” | `grep -c "试奏"`→0、`grep -c "试音"`→0、`grep -c "audition"`→0；十条导航全无 | 提示（题眼句整体缺席，而它正是「假事真做」的注脚） |
| L2 | 「他们演奏什么」「机器人」→「你要学的正是没有机器人的弹法」 | `:173` ““Robots.””；`:177` ““You are going to learn to play without robots, Oliver. Come here, look.”” | `/usr/bin/grep -c "机器人"` → 0，rc=1（整篇 md 无「机器人」三字） | 提示（「用机器人听音乐、学不用机器人的琴」是本章的核心对照，块 4 只留了后半段物理讲解） |
| L3 | **他认出这个院子就是昨晚（穿越时）来的那个院子：「我那时在未来！」** | `:226` “As I follow her, I realize that this is the garden I was in last night—I was here, in the future!” | `grep -c "昨晚"`→0；导航无一句提及「院子＝未来」 | 提示（把 ch46 那夜的穿越与「老师家」缝在一起，是本章最深的一处接榫；md 未收） |
| L4 | 耳塞式生物机器人：心跳同步、只彼此相连、不接「间隙」，从此两人能直接对话 | `:231` “In the kitchen she opens her hand and shows me two earpieces.”；`:237` ““It has synchronized to your own heartbeat,” Mrs. Baxter says.”；`:247` “These are biorobots. … they are only connected to each other, not to the Interstices.” | 仅 `md:15` 叙事手法出现「耳塞」一词；无任何块交代机制 | 提示（后半章所有对话都建立在耳塞上，md 里凭空能听懂） |
| L5 | 「我过敏」＋「这是别人问你为什么没植入时最好的说法」＋眨眼（她在教他说谎） | `:262` ““I have allergies,” she says. “By the way, that’s a good explanation to give anyone if they want to know why you don’t have it.” She winks at me. Is she trying to tell me that she is lying?” | `grep -c "过敏"`→0 | 提示（她给的是一个可复用的掩护说法，后文要用） |
| L6 | 母亲从叔叔手机上发来的留言：「你平安到了我们太高兴了！好好用功，好孩子，我们想着你。」 | `:50` “There is a message from my mother: We are so happy that you have arrived safely! Work well, lovely boy, we are thinking of you.” | `grep -c "留言"`→0、`grep -c "平安"`→0 | 提示（父母在全书此章唯一「在场」的方式） |
| L7 | 「Crouch End——地势高」 | `:82` ““It’s high ground.”” | `grep -c "高地"`→0 | 提示（与 ch46「淹水的旅馆」正好构成水性/高地的对照） |
| L8 | 叔叔从没见过这位老师，只凭「我问过的每个人都极口称赞她」 | `:45` ““I’ve never met her. But she is highly praised by everyone I consulted.”” | 无 | 提示（他把自己没验过的人交出去，是这一章的前提） |
| L9 | 时间旅行者不能有永久植入（一穿越就丢；丢 Interstitial 可能脑出血） | `:252-253` “As a time traveler, I can’t have any kind of permanent implant; I would lose it the first time I traveled, and the Interstitial implant is so invasive that losing it might cause a brain hemorrhage.” | 仅作词汇例句出现在 `md:128`（hemorrhage 条），块内无 | 跳过（词汇层已收原句） |
| L10 | 玄关脱鞋/绿条纹袜、房间、Canary Wharf、crumpet 与 Marmite、猫名 Gwen、中音 C 与 C/Cat | `:101` `:115` `:66` `:49` `:348-352` `:327-338` | 无 | 跳过（细节与教学游戏，非关键事件） |

## 二、编（md 有、原文无）

无。逐条回查：`md:11`「反制了叔叔留下的录音方块」有 `:271` “It’s a transmit/record cube… My cube is reforming it.”；`md:12`「落点不在音乐，而在一包纸巾」有 `:393`；`md:13`「她抽烟、家具老旧、书摊得到处都是」有 `:310`（cigarette）、`:155`（armchair 窝）、`:119`（书）；`md:14`「她不问他的来历，只把耳朵借给他」有 `:159`–`:177`。

## 三、错（两边都有但不一致）

| # | 断言位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | `md:15` 叙事手法 | 「这一章是第一人称限知，**成年的奥利弗回述**十三岁那一天」 | 全篇**现在时**：`:23` “The second day I am in England my Uncle Stephen says”；`:28` “I say, “But I’ve never even touched a piano.””；`:129` “I look at her, panicked.” 无任何成年叙述者标记（对比 ch46 结尾才有「年长的自己」出场） | **错（提示）**：「回述」把现在时的即时感改成了追忆；本章并没有成年叙述层 |
| E2 | `md:11` 与 `md:152` | 「老师**拆开琴盖**讲声音怎么来」 | `:177` “She raises the top of the piano and props it open.”——是**掀开并支起**琴盖，不是拆开 | **错（提示）**：「拆开」会让读者以为把琴拆散了 |
| E3 | `md:13` Tropes | 「她抽烟、家具老旧、书摊得到处都是，**还当面承认自己在撒谎**」 | `:262` “She winks at me. **Is she trying to tell me that she is lying?**”——是她眨眼、由孩子**猜**她可能在撒谎；她没有一句承认 | **错（提示）**：把「孩子的猜测」写成「她当面承认」 |
| E4 | `md:11`/`md:21`/`md:152` | 真名作「青」 | 原文只有拉丁转写：`:23` “you must apply yourself, Qing”；`:130` “Go ahead and speak, Qing”；`:184`（ch46）“Yang Qing” | **口径问题（提示）**：汉字「青」是译名选择（亦可能是「清」）；ch46 的 `4-verdict.md` 已注明「勿臆造汉字」，两章需统一——要么都写「青」，要么都只写 Qing |
| E5 | `md:11`「反制了叔叔留下的录音方块」 | — | `:271` “My cube is reforming it.” + `:284` “the cubes are both white and still” | 假红（「反制」是对 reforming 的合理概括） |
| E6 | `md:13`「兑现音乐即救赎：声音比语言更早抵达他」 | — | `:393` 他哭、`:401`「是，老师，我准备好了」 | 假红（分析层判断，有文本支撑） |

## 四、归属方向复核（R4 三问）

- 块 1 “my Uncle Stephen says” ⇄ `:23`：说话人＝**叔叔**；受话人＝Oliver（称他 Qing）；md `:21`「叔叔斯蒂芬就说该干活了…还点名叫他青」——正确。
- 块 2 “The white lady who answers the door” ⇄ `:96`：被描述者＝**老师**；md `:31` 写外形，未把「white」误译成衣物颜色（原文该词在此更可能是「白人女性」，md 不译反而安全）。
- 块 3 “He taps it twice… it turns blue” ⇄ `:129-130`：施事＝**叔叔**（敲方块）；「Go ahead and speak, Qing」是叔叔用普通话说的；md `:41`「他用普通话叫青开口」——正确，未写成方块自己点名。
- 块 4 “The key pushes the hammer…” ⇄ `:182`：说话人＝**老师**；「Put your hand on your heart」的受事＝Oliver；md `:51`「她说自己在推动空气」——正确。
- 块 5 “She plays with her back straight” ⇄ `:198`：弹琴者＝**老师**；叔叔此时皱眉、正要抗议（`:198` “he opens his mouth to protest”），md `:59` 未提，属省略非倒置。
- 块 6 “She opens a cabinet and brings out another cube” ⇄ `:221`：施事＝**老师**；受事＝她自己的方块；md `:71`「老师从柜子里又拿出一个方块」——正确。
- 块 7 “She has the tattoo… just like my mom and dad’s” ⇄ `:258`：纹身在**老师**颅底；比较对象＝**他父母**（父母转入地下时取掉）；md `:81`「和他爸妈身上的一样」——方向正确（不是「和她父母一样」）。
- 块 8 “He was told not to bring such a thing here” ⇄ `:279`：被交代者＝**叔叔**；交代者原文未点名（「有人告诉过他」）；md `:91`「对方被人交代过不许把这种东西带来」——保留了不确定性，正确。
- 块 9 “I crash and I tickle” ⇄ `:387-388`：施事＝**他**（乱砸）；老师「绕着他的声音」＝受事侧；md `:101` 未把两者主语对调。
- 块 10 “her hand placing a small packet of tissues on the keys” ⇄ `:393`：施事＝**老师的手**（人未入画）；md `:111`「他看见她的手把一小包纸巾放在琴键上」——正确。
