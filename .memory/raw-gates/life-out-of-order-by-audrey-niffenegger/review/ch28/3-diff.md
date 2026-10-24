# ch28 对账（A Muse in the Machine）

原文：`text/ch28_a_muse_in_the_machine.txt`（286 行，双声部：Alba `:23-44`，Beck `:50-286`）
md：`ch28 a muse in the machine.md`（132 行，8 块）
机器层：rc=0，8 块，block_target=[5,8]

## 一、漏（素读有、md 无）

| 编号 | 素读要点 | 原文（逐字） | md 侧取证 | 判定 |
|---|---|---|---|---|
| L1 | 座位与人位的母题：Beck 问「Henry 坐哪个位子」，答是 Kimy 坐的那个，而自己坐的是「离厨房最远、留给客人的位子」 | `:120`「Which of the seats at this table was his?」`:121`「Probably the one Kimy’s sitting in; mine is the farthest from the kitchen, the one reserved for guests.」 | `/usr/bin/grep -c -F "座位"` → 0；`"客人"` → 0；`"guest"` → 0（rc=1） | 漏（提示）：这是全章唯一把「他在这家的位置」写成实物坐标的句子，且与 L4（孩子摆座位）正好互文 |
| L2 | Alba 摆桌：Mama 熨了「我没见过的外婆」的桌布餐巾、把 Beck 安排在对面**那个空位**、Kimy 总坐 Daddy 的位子 | `:29`「Mama has ironed a tablecloth and some napkins that belonged to my grandma who I never met. …I put Beck in the seat across from me that’s empty. Kimy always sits in Daddy’s seat, across from Mama.」 | `"外婆"` → 0；`"Daddy 的位子"` → 0；`"空位"`/`"座位"` → 0。**已覆盖的部分**：导航 `:12`「熨过的桌布、祖母留下的餐巾」——餐具这一半进了导航 | 漏（提示）：缺的是「座位」这一半（谁坐哪、哪张椅子是空的），而这正是 L1 的伏笔 |
| L3 | 溜冰是「谈得顺利」的奖赏，不是既定安排：`If things go well with Beck…roller-skating` | `:29`「“If things go well with Beck,” she says, “you and Nadia and Colin might be able to go roller-skating later this afternoon.”」 | `"溜冰"` → 0；`"roller"` → 0 | 漏（提示）：孩子视角的「条件句」是本章张力起点 |
| L4 | 三种「死人也做得出来吗」之后，Beck 承认数字猫只是「在网站里晃」——不暖不软 | `:109`「“She’s not warm and soft, like my cat was. It’s nice to see her wandering around inside my website, though.”」；`:105`「“So you have a cat zombie?”」 | `"zombie"` → 0；`"website"` → 0（总结 `:132` 只写「能不能把死人也做成数字的」） | 漏（提示）：回答问题的那半句被删，只剩提问题的半句 |
| L5 | Alba 早已从「Older Alba」处听过 Beck，且清楚自己有「不能知道的事」 | `:43`「I guess I thought it would be like we already know each other because Older Alba has been telling me about Beck」；`:44`「I can’t remember what I’m not supposed to know.」 | `"Older Alba"` → 0；`"不该知道"` → 0 | 漏（提示）：孩子为何「早知道结局」的唯一文本依据，缺了它本章的「反转」就成了作者旁白 |
| L6 | 九种蓝：Alba 抱来一桶颜料管（水彩/丙烯/水粉，太贵，是 Clare 的），Beck 挑 Cerulean Blue，Alba 把管子推回去「You keep it」 | `:151`「The tubes are a mix of watercolor, acrylics and gouache; they must be Clare’s—they are too expensive for an eight-year-old. Soon there are nine different blues. “That one,” I say, handing her Cerulean Blue.」；`:165`「Cerulean Blue next to my spoon」 | `"Cerulean"` → 0；`"九种"` → 0；`"颜料"` → 0 | 漏（提示）：全章最长的一段「用孩子的语言谈画」，也是 Beck 重拾画画的转折（`:159`「The only thing I’ve painted recently is the walls of my studio」） |
| L7 | 餐桌实物：Beck 带来的白马蹄莲插瓶、Kimy 拆巧克力、三杯 pinot grigio、Alba 用葡萄酒杯喝 7-Up（冷汤 vichyssoise 的笑话） | `:70`「Clare puts the calla lilies I brought into a vase. Kimy unwraps the box of chocolates. …pours herself, Kimy and me each a glass of pinot grigio. Alba has 7-Up, with ice, in a wineglass.」；`:72`「“Let’s eat before it all gets cold,” and we laugh because the soup is vichyssoise」 | `"马蹄莲"` → 0；`"calla"` → 0；`"pinot"` → 0；`"7-Up"` → 0；`"冷汤"` → 0 | 漏（提示）：整段宴席只剩「炸丸子」一道，酒与花是「这顿饭是正式的」的信号 |

## 二、编（md 有、原文无）

**0 条。**

唯一需要说明的一处：原句 7 中文理解写「一个八岁孩子当着三个大人问『你要不要搬进来跟我妈妈结婚』」——原文 `:220` 只有「“So, are you going to move in with us and get married now?”」，「跟我妈妈」是补出的受事。这是 Alba 对 Beck 说话、且婚配对象只能是 Clare，属**合理补足**，不算编。

## 三、错（两边都有、但不一致）

| 编号 | 断言 | 原文（逐字） | md 侧 | 判定 |
|---|---|---|---|---|
| E1 | 导航写「Alba 不追问死亡，也不打听婚事」 | `:89`「“Can you do that with people? After they’re dead?”」；`:220`「“So, are you going to move in with us and get married now?”」 | 导航 `:13`「Alba 不追问死亡，也不打听婚事，她早已知道结局，不确定的只是时间」；而同篇总结 `:132` 写「饭桌上 Alba 一路追问」 | 错（提示）：**自相矛盾**，且与原文两处直接对撞。原意应是「不问『为什么』只问『什么时候』」，建议改为「Alba 不追问缘由，只打听时间」 |
| E2 | 导航写「饭桌上一句『死人也做得出来吗』问得满桌安静」 | `:76`「We eat in silence for what seems like eons.」（安静在提问**之前**，且是等菜时的沉默）；`:89` 提问后紧接的是 Clare 的「Did you have someone in mind, sweetie?」（`:91`），非沉默 | 导航 `:11` | 错（提示）：把「先有的沉默」记成「被问出来的沉默」，因果方向反了；改「饭桌上一句…问得 Clare 又惊又佩」即可 |
| E3 | 原句 4 中文写「那是她一整晚的骄傲」 | 抹甜菜是在**当天上午**做丸子时（`:23`「I got to put the carrots and beets through the food processor」），非「一整晚」 | 原句 4 中文理解 | 错（提示）：时间词无据，改「一上午」 |

## 四、逐块对应（R4）

| 块 | 引语起（原文行） | 中文是不是在讲这句？ | 主语 / 受事 / 归属 |
|---|---|---|---|
| 1 | `:23` 料理机、抹甜菜、烟雾报警 | 是。中文解释「感叹号」用得准（原文 `:23` 连用两个 `!`） | 主语 Alba ✓；受事「胡萝卜与甜菜」✓ |
| 2 | `:23` Mama 从不为别人下厨 | 是 | 主语「Mama」✓；「Kimy 更会做」✓（原文 `:23`「she’s better at it」） |
| 3 | `:50` 门开、看见女儿、变真 | 是。中文点出「不是那一晚俄式餐厅的成年女子」，与原文 `:50`「not the woman I met that night at the Russian restaurant」一致 | 主语 Beck ✓；「她」指 Beck（与全书「Beck＝她」的写法一致）✓ |
| 4 | `:50` 握手、magenta、Beet red | 是。中文把「以为流血→缩手→改口夸颜色」三层因果还原得完整 | 主语 Beck（以为/缩手/改口）✓；受事 Alba 的手 ✓ |
| 5 | `:211` 四层表情 + Isadora is child's play | 是。「狡黠/热切/羞怯/焦虑」四层与原文四个 because 一一对应 | `Clare tells me`＝Clare 告诉 Beck ✓（不是 Clare 自己想） |
| 6 | `:216` 手机记点子、Tempest 引语 | 是。中文「想通了」略过了「她在洗手间偷偷记」这层，但不影响对应 | 主语 Beck ✓；受事 Isadora 的代码 ✓ |
| 7 | `:220` 搬进来结婚 | 是（见「编」节说明） | 问者 Alba、答者 Beck ✓；「三个大人」＝Clare/Kimy/Beck ✓（原文 `:222` Kimy 带警告地叫「Alba,」） |
| 8 | `:285` 摇酒壶、Sloe gin fizzes、Welcome to the family | 是。谁举杯（Kimy）与谁补酒名（Clare）分得清 | 主语 Kimy（举杯）/Clare（补名）✓ |

**R4 结论**：8 块无一块讲引语之外的上下文，无一块只复述字面；3 块（1/4/5）密度最好。块 6 略欠（省掉了「在浴缸边偷偷记」这个动作）。

## 五、形态

H1 `28. A Muse in the Machine` ✓；导航 5 项 ✓；子项（中文理解/关键词/为什么这样写/读者视角提示）4 齐 ✓；块数 8 在 [5,8] 内 ✓；块序单调（`:19→:29→:39→:49→:59→:69→:79→:89`）✓；CJK 最低值来自机器层，未见 `cjk_low`。
