# ch40 subtle bodies — 对账单（R3）

- 原文：`text/ch40_subtle_bodies.txt`（645 行）
- 精读：`ch40 subtle bodies.md`（142 行）
- 机器层：`2-machine.json`，rc=0，verdict=ok，块数 9，段数 9 全 ok，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，template 0，hole 0，words 4610，H1 `40. Subtle Bodies`，导航 5 条，block_target [8,14]

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | **另一座博物馆属于贝克的前夫 Jasper**——那个博物馆将来会进到现实世界、变成 the Interstices，这正是「绝不能装 bioware」的理由 | `:566-567` “But there is another version of the Museum out there—it belongs to Beck’s ex-husband, Jasper. And that Museum will eventually find its way into our world, as the Interstices. And that’s why you mustn’t get bioware.” | 零命中：`/usr/bin/grep -nE "Jasper|贾斯珀" "ch40 subtle bodies.md"` → 无输出（**rc=1**）；`grep -nE "前夫"` → 无输出（**rc=1**）。块 8 只保留「另一个座博物馆留下入口」式的抽象提法（`:95`「也替另一座博物馆留下入口」），一句话总结（`:142`）写「另一座博物馆终将以『间隙』之名进入这个世界」——**主语的归属被抹平了** | 提示（强）（警告在、禁令在、甚至「间隙」这个名字在，唯独**是谁的博物馆**丢了；这条恰恰是下一章贝克声部要处理的旧账。建议补「属于贝克的前夫贾斯珀」一句，改动成本极低） |
| L2 | Marshall Field's 的整段童年记忆：母亲每年八月带 Alicia 与 Clare 来买衣服（难看绿格天主教校服）、十二月来买圣诞礼物；兄弟 Mark 从不肯来、嫌长途与试衣、坐在女装试衣间外生闷气；所以这总是「女孩们的一天」；午餐永远是鸡肉派＋蔬菜沙拉＋冰淇淋，「这里只有价钱会变」 | `:28` “I remember when this was Marshall Field’s, and my mother brought Alicia and me here every August for clothes”；`:28` “So it was always a girls’ day out, a rare treat.”；`:29` “We always ate lunch here in the Walnut Room, and it was always the same lunch: chicken potpie with a green salad and ice cream for dessert… only the prices ever change here.” | 零命中：`grep -nE "Marshall"`、`grep -nE "鸡肉派|potpie"` 均无输出（**rc=1**）；导航情感弧线（`:12`）只留「旧百货公司的记忆」五个字 | 提示（这一章唯一的「母亲」记忆就在这一段，且是全书少见的 Clare 与生母同框；抹成一句「旧记忆」，餐厅场景就只剩布景） |
| L3 | Isadora 借的形是 **Ida B——贝克死去多年的黑猫**，且被放大到「德国牧羊犬那么大」；贝克与 Isadora 常为「博物馆里的东西该多大」争执，今天 Isadora 显然觉得越大越好 | `:284` “Everyone is looking at Isadora in the form of Ida B, Beck’s long-deceased black cat, who saunters across the carpet… She’s German shepherd–sized. Beck looks displeased; she and Isadora often have disagreements about what size things should be in the Museum, and Isadora has obviously decided that bigger is better today.” | 零命中：`grep -nE "Ida"`、`grep -nE "德国牧羊犬"` 均无输出（**rc=1**）。块 6 读者视角（`:77`）只写「体型大小也由自己拿主意」 | 提示（「博物馆里的第一件复活的失物是一头死猫」是这座博物馆的伦理原点，也是贝克「我不断失去我在乎的东西」那句话的实物；缺它，Isadora 的猫形就只是一个设计选择） |
| L4 | 绿门后那间卧室的**具体陈设**：没铺的单人床半盖着彩色枕头与毛绒玩具、行李箱里炸出来的衣服、一把摇椅、床头灯下的电子杂物、哈密瓜橙的墙、白色荷叶边窗帘后面关着的百叶窗、透进来的金色午后阳光 | `:386` “an unmade single bed half covered in brightly colored pillows and stuffed toys; a riot of clothing bursting from a suitcase on the floor; a rocking chair; electronic clutter under a lamp on the nightstand; cantaloupe-orange walls; frilly white curtains covering closed blinds that are back-lit with golden afternoon sun.” | 零命中（`grep -nE "哈密瓜|摇椅|行李箱|荷叶边"` → 无输出，**rc=1**）；块 7 读者视角（`:87`）只写「屏幕刚放过那间儿童卧室几秒钟」 | 提示（这一间房之所以让人哭，全靠这些物件被逐一报出——它证明记录是真的、是「她的房间」，不是一个泛泛的童年意象） |
| L5 | 伊莎多拉对卢辛达的承诺：「你的房间永远为你留着。别人都不能来看它。**只有你有这把钥匙。**」以及「谢谢。我已经准备好走了。」 | `:493` ““Your room will always be here for you. No one else can visit it. You have the only key.””；`:497` “Lucinda opens her hand. The key is still there. “Thank you. I’m ready to go now.”” | 半命中：总结（`:142`）提到「又用一把铜钥匙打开一间被录下的旧卧室」，但**「只有你有这把钥匙」这条排他承诺**零命中（`grep -nE "只有.*钥匙"` 命中的是 `:142`「只有微细身的伊莎多拉……一把铜钥匙」，不是这句） | 提示（这句是让「借出相貌」这件事变得可以接受的关键条件：房间是**她的**，别人进不去。少了排他性，整桩交易看起来只是被录下来示众） |
| L6 | 老 Alba 预言的**具体条款**：Celia 会要求设大学信托，**四年、全额、学校由 Lucinda 自己选**；「Smith，不过她现在当然还不知道」 | `:236` “Celia will ask for you to set up a college fund for Lucinda, to be held in a trust. Four years, full ride, college of Lucinda’s choice.”；`:245` ““Smith, but of course she won’t know that yet.”” | 零命中：`grep -nE "Smith|史密斯"`、`grep -nE "四年|全额"` 均无输出（**rc=1**）；导航（`:11`）只写「要求付酬并设大学基金」 | 提示（「Smith」是本章唯一一处具体的未来兑现，也是老 Alba「我知道结局」的实证；删掉后她的话只剩劝告，没有预言的分量） |
| L7 | 博物馆里收了什么：**纳粹掠夺的画**、**藏在瑞士自由港里的艺术**、**希腊雕塑**（在这里是完整的，现实里是碎片） | `:347` “Celia’s gaze swivels from wall to wall, taking in Nazi-looted paintings, art that is hidden in Swiss free ports, Greek sculptures (whole here, but in fragments in the real world).” | 零命中：`grep -nE "纳粹"`、`grep -nE "瑞士"` 均无输出（**rc=1**）；块 6 读者视角只写「带她们看那些对人有过意义的东西」（`:142`） | 提示（「失物」在这里第一次有了政治与历史的重量——被盗的画、被藏起来的艺术、只剩碎片的雕塑；抽掉清单，「博物馆」就退回成一个温柔的比喻） |
| L8 | 卢辛达的适应史：起初沉默、继而「过度有礼」（怕被送回去），**「你根本没法跟她开玩笑」**；介绍了 **Darcy**（Celia 最近一个「超龄退出系统」的寄养女儿）之后才安定下来；「最近她在试探我一点点，我觉得我们能成」 | `:80` “At first she was mostly silent, and then she was ultrapolite, like she was scared I was going to send her back… You couldn’t joke with her at all. But I introduced her to Darcy—” (Celia’s most recent foster daughter, who has aged out of the system) “—and I think Darcy calmed her down.” | 零命中：`grep -nE "Darcy|达西"` 无输出（**rc=1**）；`ultrapolite` 只出现在词汇表例句（`:115`），不在任何一块的中文里 | 提示（「怕被送回去」是理解这个孩子为什么如此克制、又为什么在一间卧室前崩溃的钥匙；Darcy 则是 Celia 这条支线唯一的人物接续） |
| L9 | 餐厅布景（梅西的巨树占住喷泉位置、摇摆版《Jingle Bells》三重奏、脚边塞着购物袋的中年女士）；「像跟 Beyoncé 一起上街」；Isadora 的口音「有点像 Tilda Swinton」；博物馆场景是 **Isabella Stewart Gardner Museum 的庭院**；抬头里的 **Alba is 14 and 60**；Alba 一年长六英寸；结尾「Everyone needs a backup disk」那组屏幕对话 | `:23` “Macy’s has erected an immense sparkling tree in place of the fountain”；`:72` “it’s like walking down the street with Beyoncé”；`:284` “a slightly haughty accent that reminds me of Tilda Swinton”；`:305` “the courtyard of the Isabella Stewart Gardner Museum”；`:180` “(Alba is 14 and 60, Clare is 44, Beck is 39)”；`:93` “she grew six inches in one year”；`:456` “Isadora: Everyone needs a backup disk.” | 均零命中（`grep -nE "Beyoncé|Tilda|Gardner|六英寸|十四岁|六十"` 全部 rc=1）；`backup disk` 只在词汇表（`:137`） | 跳过（布景与彩蛋，不承载事件；但 `Alba is 14 and 60` 这个「同时是十四岁和六十岁」的写法是本书时间观的一个漂亮标本，若日后再修，可考虑补进抬头引述） |
| L10 | 贝克解释「为什么造它」的原话：**「我开始这个项目时，我的生活正在崩解，我不断失去我在乎的人、东西和地方」**；以及「有些人会在手机里存一堆照片，或者留一件衣服」 | `:512` ““Sometimes you need something more,” Beck says. “When I started this project, my life was falling apart, I kept losing the people and things and places that I cared about. Some people might keep a bunch of photos on their phone, or a piece of clothing, you know what I mean?”” | 零命中（`grep -nE "崩解|失去"` → 无输出，**rc=1**）；原句 3 读者视角（`:47`）只处理「礼物」与商业动机 | 提示（这是贝克这条线的自白，也是全章唯一解释「博物馆为什么存在」的话；缺它，博物馆的动机只剩克莱尔的「孤独的机器人」一句代述） |
| L11 | 送客之后：克莱尔问卢辛达想跟谁通信，老 Alba 答「**这是我和她之间的事**」；确认不是骗人（「我把信送到她想去的地方，也带回了回信」）；「我确保卢辛达得到了我们能给的一切」；说完她显得**低落、沉重** | `:617` “I ask Older Alba who Lucinda wanted to communicate with. “That’s between me and her,” Alba says.”；`:627` “I got the messages where Lucinda wanted them to go, and brought back messages in return… I made sure Lucinda had everything we could give her.” Alba seems low-spirited, heavy.” | 半命中：块 9 读者视角（`:107`）提到「替人给去世的亲友捎话」是成交原因；「这是我和她之间的事」与「低落、沉重」零命中（`grep -nE "之间的事|低落"` → rc=1） | 提示（她拒绝说出那个名字，加上「沉重」两个字，是结尾那句「Before everything」之前的情绪台阶；少了它，最后一个块像是突然暗下来） |

## 二、编（md 有、原文无）

| # | md 写法 | 原文 | 判 |
|---|---|---|---|
| — | 未发现凭空出现的情节、关系或数字。人名（Celia、Lucinda Flowers、Celia Attley、Isadora Hardwick、Ida B、Darcy）、年龄（9／14／60／44／39）、年份（2015／2060）、地址（Smith）、术语（Interstices／bioware／subtle body／avatar）均与原文一致 | — | — |

## 三、错（两边都有但不一致）

| # | 位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| — | — | 未发现主语、因果、数字、时序、归属方向上的不一致。逐条见下节 R4 | — | — |

## 四、归属方向复核（R4 三问）

- 谁提出让卢辛达当模特：`md :11`「午餐间克莱尔想到让这个女孩给贝克的人工智能伊莎多拉当形象」／原文 `:113` “An idea pokes at me… “Have you done any modeling yet?”” —— **克莱尔**，正确（不是西莉亚提议、也不是贝克先开口）。
- 谁警觉、谁称「数字劫身」：`md :11`、块 2「西莉亚」／原文 `:126` “Celia shoots me a look.”；`:148` “Celia says quietly… this is a kind of digital body-snatching” —— **西莉亚**，正确。
- 谁要付酬、谁提大学：`:148` “y’all ought to pay Lucinda handsomely”；`:167` “y’all should fund Lucinda’s way through college” —— 都是**西莉亚**（第二句是「如果成了」的条件句）；md 导航（`:11`）「要求付酬并设大学基金」挂在她名下，方向正确，条件语气略被压平成既成要求，可接受。
- 谁设信托、谁预言：`:236` ““Celia will ask for you to set up a college fund for Lucinda…”” —— 说话人是**年长的阿尔芭**，受事是**贝克**（要她去设）；md 块 5 中文理解（`:61`）用「必须设计一个激励」的无人称句，未误挂成克莱尔或西莉亚，安全，但主语可补「阿尔芭对贝克说」。
- 谁录的房间、谁帮的忙：`:401` ““Alba asked me to record that room a year ago… She helped me break in.”” —— **阿尔芭出主意并协助闯入，贝克动手录**；md 块 7 中文理解（`:81`）「阿尔芭帮她潜入，她录了大约二十分钟」——施受关系完全正确（这是本章最容易搞反的一处）。
- 谁道歉、谁装无辜：`:410` ““Don’t look at me,” says the younger one. “Sorry,” says older Alba… “But it’s what Lucinda needs.”” —— 十四岁的**小阿尔芭**推脱，六十岁的**老阿尔芭**道歉并给理由；md 读者视角（`:87`）「小阿尔芭装作无辜，成年阿尔芭轻声道歉，只说这是卢辛达需要的」——正确。
- 谁关掉系统：`:522` “Beck turns off the system, so that Isadora can’t eavesdrop on us.” —— 是**贝克**；md 块 8 读者视角（`:97`）「贝克先把系统关掉，免得伊莎多拉听见」——正确。
- 谁禁止 bioware、谁附和：`:540` 是老**阿尔芭**下禁令；`:549` ““When you understand, you’ll be very glad you don’t have it,” **Beck** says.” 是**贝克**补的解释；`:558` ““Not yet,” Alba says. “Soon.”” 又回到阿尔芭。md 读者视角（`:97`）「她说生物组件是『被技术占有』，像被邪灵附身」——把贝克的解释并入了「她」（指阿尔芭）的话里，**发言人有轻微合并**，但两人在同一段对答中各说一句、语义未错，判可接受（若修订，宜分写「贝克补一句」）。
- 谁不许说出去：`:617` ““That’s between me and her,” Alba says.” —— 拒绝透露的是**老阿尔芭**（不是克莱尔替她保密）；md 未写这一句，故无错挂。
- 谁在讲述：两节都是**克莱尔**第一人称（`:23`、`:185`）；md 叙事手法（`:15`）「两个日期分节，都由克莱尔以第一人称讲述」——正确。

## 五、可核验断言（供 R5 抄）

```
$ cd notes/books/novels/life-out-of-order-by-audrey-niffenegger
$ /usr/bin/grep -nE "Jasper|贾斯珀" "ch40 subtle bodies.md";      → 无输出 rc=1
$ /usr/bin/grep -nE "前夫" "ch40 subtle bodies.md";                → 无输出 rc=1
$ /usr/bin/grep -nE "Ida|德国牧羊犬" "ch40 subtle bodies.md";      → 无输出 rc=1
$ /usr/bin/grep -nE "Marshall|鸡肉派|potpie" "ch40 subtle bodies.md"; → 无输出 rc=1
$ /usr/bin/grep -nE "Smith|史密斯|四年|全额" "ch40 subtle bodies.md"; → 无输出 rc=1
$ /usr/bin/grep -nE "纳粹|瑞士|Gardner|加德纳" "ch40 subtle bodies.md"; → 无输出 rc=1
$ /usr/bin/grep -nE "Darcy|达西" "ch40 subtle bodies.md";          → 无输出 rc=1
$ /usr/bin/grep -nE "Beyoncé|Tilda|六英寸|十四岁|六十" "ch40 subtle bodies.md"; → 无输出 rc=1
$ /usr/bin/grep -nE "哈密瓜|摇椅|行李箱|荷叶边|崩解|低落" "ch40 subtle bodies.md"; → 无输出 rc=1
$ /usr/bin/grep -nE "唯一|只有.*钥匙" "ch40 subtle bodies.md"
142:…又用一把铜钥匙打开一间被录下的旧卧室…   （命中的是总结句里的「只有微细身」，不是「You have the only key」）

$ /usr/bin/grep -nE "ex-husband, Jasper|Ida B, Beck’s long-deceased|German shepherd–sized|Four years, full ride|Smith, but of course|Nazi-looted|cantaloupe-orange|only key|Everyone needs a backup disk|my life was falling apart|That’s between me and her" text/ch40_subtle_bodies.txt
236:…to be held in a trust. Four years, full ride, college of Lucinda’s choice.
245:“Smith, but of course she won’t know that yet.”
284:Everyone is looking at Isadora in the form of Ida B, Beck’s long-deceased black cat… She’s German shepherd–sized.
347:…Nazi-looted paintings, art that is hidden in Swiss free ports, Greek sculptures…
386:…cantaloupe-orange walls; frilly white curtains…
456:Isadora: Everyone needs a backup disk.
493:“Your room will always be here for you. No one else can visit it. You have the only key.”
512:“When I started this project, my life was falling apart…”
566-567:…it belongs to Beck’s ex-husband, Jasper… as the Interstices…
617:“That’s between me and her,” Alba says.
rc=0
```
