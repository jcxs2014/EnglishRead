# ch39 making music — 对账单（R3）

- 原文：`text/ch39_making_music.txt`（435 行）
- 精读：`ch39 making music.md`（130 行）
- 机器层：`2-machine.json`，rc=0，verdict=ok，块数 8，段数 8 全 ok，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，words 2761，H1 `39. Making Music`，导航 5 条，block_target [5,9]

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | **她已知的未来清单**：明年的总统选举结果、所有疯狂的仇恨犯罪、**大流行病**、**内战**、气候变化——「可我不能告诉妈妈。我不想知道这些。知道未来帮不上忙。」 | `:123` “I agree, but I already know more than I want to: next year’s presidential election results, all the crazy hate crimes, the pandemic, the civil war, climate change . . . but I can’t tell Mama. I don’t want to know these things. Knowing the future doesn’t help.” | 零命中：`/usr/bin/grep -nE "选举|疫情|大流行|内战|气候|仇恨" "ch39 making music.md"` → 无输出（rc=1）。md 只有导航「已知未发生的事」与教堂枪击一处实例 | 提示（「知道未来没有用」是本章的题眼，md 保住了判断、抽掉了证据；这五样也是二〇一五年的时代底噪，建议至少留「选举结果／大流行病／内战」三样） |
| L2 | **贝克雇侦探的真正目的**：不想跟 Jasper 联系，「只想知道他是否安全，以及是不是他动了她的服务器」；以及由此引出的因果回路玩笑（「能不能直接问未来的我」「没人去查，未来的你怎么会知道」） | `:64` ““She doesn’t want to get in touch with him,” Mama says. “She just wants to know he’s safe and find out if he’s the one who messed with her servers.””；`:73` ““How would your future self know, unless somebody investigates?””；`:77` ““I dunno. Causal loops are weird.”” | 零命中（`grep -nE "服务器"` → 无输出）；md 导航（`:11`）只写「雇侦探去查失踪的贾斯珀」 | 提示（「服务器」是这条线的**物证方向**，后文若回指 Jasper 与贝克的旧账会断线；因果回路的对话则是本书时间观的一次明确交代） |
| L3 | **亨利缺席的那张桌子**：Henry 在世时桌上也许只有盐胡椒瓶或报纸，但除了吃饭没人坐；Alba 上学后每晚上坐在桌边讲幼儿园的事、Henry 做饭，吃的时候把她的美术作业与提琴功课**推到空着的第四副餐具**那边；Beck 搬进来以后桌上开始堆满东西 | `:174` “When Henry was alive, there might have been salt and pepper shakers or a newspaper on it, but we didn’t spend time sitting around between meals.”；`:174-175` “We’d eat with her art projects and violin homework pushed over to the empty, fourth place at the table”；`:180` “After Beck moved in, we started to leave more things on the table” | 零命中（`grep -nE "第四|餐具"` → 无输出）；md 读者视角（`:67`）只交代「刚把报纸送到工作室、抱着一捆亚麻碎布回到餐厅」 | 提示（这是全书对「亨利不在了」最克制的一处正面书写，「空着的第四副餐具」比任何追忆都重；建议补一句） |
| L4 | 母亲关于音乐为何有用的**全部理由**：音乐给人快乐、快乐对人极好、艺术能重塑大脑、音乐能改变情绪、能疗愈；「你父亲总说音乐帮他留在当下，我想它对你也一样，**它让你专注，你专注时就不会那么频繁地穿越**」；以及末句「如果你不想做音乐，你就不必做。它是你的」 | `:137` “Music gives people joy, and joy is very good for a person… Art can reshape your brain… Your dad always said that music helped him stay in the present, and I think it does that for you, too; it helps you concentrate, and when you concentrate you don’t time travel so much.”；`:156` “But if you don’t want to make music, you don’t have to. It’s yours” | 总结（`:130`）只留「母亲说快乐本身就有用」；「专注→少穿越」这条机制与「它是你的」零命中 | 提示（「专注就不穿越」是全章把音乐与时间病接上的那根线，缺它，母亲的劝导就只是一段育儿鸡汤） |
| L5 | 三人关于「怎么得到点子」的实操清单与玩笑：洗车、吸尘、洗澡；「凡是有水的都好，我卡住的时候家里从来没这么干净过」；克莱尔昨天洗厨房地板时想到新雕塑的点子；阿尔芭反问「你是不是就为了让我多干家务」；贝克「这背后有真科学，你该去谷歌一下」 | `:324-325` “Or, you can do some boring thing, like washing the car, or vacuuming.”；`:334` “Anything involving water is good. The house is never so clean as when I’m stuck for an idea.”；`:347-351` ““Are you just saying this to get me to do more chores?”… “There’s real science behind this. You should google it.”” | 零命中（`grep -nE "吸尘|洗车|谷歌|家务"` → 无输出）；md 只留「贝克说艺术家得闲荡」 | 提示（「闲荡」抽象地收了，但这一串具体办法＋那记家务玩笑是本章最像过日子的一段；可留一处） |
| L6 | 电话往事的下半：克莱尔想起**那些拼命想怀孩子的年头**，Alba 就在电话那头呼吸、然后轻轻挂掉；Henry 每次遇到就说「Kids」 | `:409` “I think of those years when we were trying so hard to have a baby and Alba was there on the other end of the telephone line, breathing and then hanging up gently. Kids, Henry used to say whenever it happened.” | 零命中（`grep -nE "求子|怀孩子|Kids"` → 无输出）；md 读者视角（`:87`）只到「她只是想听听他们的声音……变成了温柔的事」 | 提示（这一句把「打错的电话」从可爱的怪癖变成「她一直在，只是还没出生」，也与前文求子的旧痛接上；建议补） |
| L7 | 开头那幅漫画：戴尖条纹派对帽、垂头丧气的自己，像鸟雕塑一样飞着的母亲，看书的父亲，以及「不想让贝克觉得被落下」而画的贝克＋膝上的 Isadora | `:28` “I draw a little cartoon Alba wearing a pointy striped party hat, looking depressed. I draw my mother flying around like one of her bird sculptures and my dad reading a book. I don’t want Beck to feel left out, so I draw her with Isadora curled up on her lap.” | 零命中 | 跳过（速写式过场；但它同时交代了 Isadora 属于贝克、以及她把四个人都画进去的心事，删掉后「不想让贝克被落下」这层善意就没了） |
| L8 | 读纸质报纸的仪式（Beck 与 Alba 都嫌「死掉的树」；他爱油墨蹭手；报纸在工作室里也是美术材料）；以及「这听着像约会」那一笑 | `:189` “Neither Beck nor Alba have any interest in The New York Times in physical form. Dead trees, they both say.”；`:419` ““That sounds like dating,” I say. Beck and I exchange smiles.” | 零命中 | 跳过（生活质感与一句玩笑，不承载事件） |

## 二、编（md 有、原文无）

| # | md 写法 | 原文 | 判 |
|---|---|---|---|
| — | 未发现凭空出现的情节、关系或数字。人名（贾斯珀／菲利普·马洛／Terryl／伊莎多拉）、年份（1994／2001）、调性（D 调两个升号）、纸张（三张）均与原文一致 | — | — |

## 三、错（两边都有但不一致）

| # | 位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | 块 2 读者视角（`:37`） | 「贝克说要去找侦探，还自比侦探小说里**让马洛跑腿**的女人」 | `:47` ““I’m going to be that dame giving Philip Marlowe the runaround.”” | 提示（give someone the runaround＝把人耍得团团转／敷衍推诿，md 词汇表 `runaround` 释义本身写的就是「推诿、拖延」；但这里译成「让马洛跑腿」——跑腿是 run errands，方向与词义都偏了。建议改「把马洛耍得团团转的那个蛇蝎美人」） |

## 四、归属方向复核（R4 三问）

- 谁雇侦探：`:47` ““I’m off to hire a detective,” **Beck** says.” —— 是**贝克**，不是克莱尔；md 导航（`:11`）、人物弧线（`:14`）、总结（`:130`）三处都写「贝克雇侦探」，正确。
- 谁失踪：`:55` “She wants to know what happened to **Jasper**. He seems to have vanished off the earth.” —— 失踪者是 **Jasper（贾斯珀）**，本章原文只称其名；据 `text/ch34_lost_love_last_laugh.txt:47` “Our actual divorce is not as painful as the struggle for the Museum. Jasper imagines that he’s entitled to half of my patents…” 与 `:66` “When was the last time you actually saw Jasper?” —— 他是**贝克的前夫**（离婚、赡养费、专利纠纷），**不是**她的父亲、也不是克莱尔的旧识。md 只写「失踪的贾斯珀」，未错挂关系，安全；但若日后补写这条线，务必写「贝克的前夫」。
- 谁说「艺术不是你欠任何人的」：`:156` “**Mama** laughs… “Alba. Art isn’t something you owe to anyone…”” —— 说话人是**克莱尔**；md 总结把「父亲和外公想给她音乐」挂回母亲转述，正确。
- 谁说「艺术家得闲荡」：`:324` ““Artists have to noodle, that’s how we get ideas,” **Beck** says.” —— 是**贝克**；md 人物弧线（`:14`）「贝克以……『艺术得闲荡』推进另外两条线」、总结（`:130`）「贝克说艺术家得闲荡」均正确。**克莱尔说的是「去，找到你的小提琴，闲荡」（`:435`）**，是命令句，不是理论句——两者勿合并成一个人说的。
- 谁在电话那头：`:405` ““Yeah, I just wanted to hear your voices,” **she** says, unabashed.” —— 是**阿尔芭**（小时候的她）打过去听父母的声音；md 读者视角（`:87`）「阿尔芭承认她只是想听听他们的声音」方向正确，未错挂成克莱尔。
- 谁不能打：`:390` ““I can’t call here before Mama and Daddy bought this house in 1994. And I don’t call before 2001, when I was born.”” —— 限制的主语是**阿尔芭**（她自己不能打），不是父母不接；md 块 7 中文理解（`:81`）写「不能往……之前打」，主语保留，正确。
- 谁在做纸浆：`:435` “I collect all the bits of linen into a bag… I head to my studio to beat the linen into paper pulp.” —— 是**克莱尔**；贝克下楼训练 Isadora。md 块 8 中文理解（`:91`）分工正确。
- 视角归属：六月六日是**阿尔芭**第一人称（`:23` “Alba: I wake up in my own bed”），六月七日是**克莱尔**（`:174` “Clare: These days our lives are conducted around the dining room table”）。md 叙事手法（`:15`）「两日两视角」正确，块 5 读者视角（`:67`）注明「这一段由克莱尔叙述」也对。

## 五、可核验断言（供 R5 抄）

```
$ /usr/bin/grep -nE "选举|疫情|大流行|内战|气候|仇恨" "ch39 making music.md"
（无输出）
rc=1

$ /usr/bin/grep -nE "服务器|第四|餐具|死掉的树|吸尘|洗车|谷歌|家务|求子|Kids" "ch39 making music.md"
（无输出）
rc=1

$ /usr/bin/grep -nE "next year’s presidential election|the pandemic, the civil war|messed with her servers|empty, fourth place|Dead trees|Anything involving water|trying so hard to have a baby|giving Philip Marlowe the runaround" text/ch39_making_music.txt
47:“I’m going to be that dame giving Philip Marlowe the runaround.”
64:“She just wants to know he’s safe and find out if he’s the one who messed with her servers.”
123:I agree, but I already know more than I want to: next year’s presidential election results, all the crazy hate crimes, the pandemic, the civil war, climate change . . .
174:We’d eat with her art projects and violin homework pushed over to the empty, fourth place at the table
189:Neither Beck nor Alba have any interest in The New York Times in physical form. Dead trees, they both say.
334:“Anything involving water is good,” Beck agrees.
409:I think of those years when we were trying so hard to have a baby…
rc=0
```
