# 4-correspondence.md · ch36 逐块对应（人判）

> 判据：只看「这段中文是不是在讲这句引语」。
> · 讲引语之外的上下文 → **引语选短**
> · 讲全书主旨 / 作者生平 → **不对应**
> · 只复述字面、没有「为什么这样写」 → **密度不足**
> 固定追问：① 每个动词的主语是谁 ② 受事/宾语是谁 ③ 「谁的 / 谁欠谁 / 谁问的」回原文按 `by`/`to`/`from`/`of` 定向。
> 区间＝`text/ch36_36.txt` 的**绝对字符偏移** [起,止)（本审查员自算）。
> 口径提示：`2-machine.json` 里的 `pos` 是**归一化后**语料的偏移（`scripts/lib/text.py::norm` 把换行折成空格、去引号），与本文绝对偏移不同源，二者不可直接相减（B1 机器 20 / 本文 36；B10 机器 12721 / 本文 13124）——**这是口径差异，不是内容差异，不构成假红**。

| 块 | 引语原文区间 | 中文在讲这句引语吗 | 三问（主语 / 受事 / 归属） | 判定 |
|---|---|---|---|---|
| B1 | [36, 171]｜`text/ch36:20` 「Callie knocked on … get set up.」 | **是**。中文理解复述的就是「提前半小时到场布置」，为什么这样写给的是「用一个『提前』的细节立住做事方式」——引语之外没有另起话题（未延伸到出租车/「Laura」那条支线，见 3-diff L2）。 | ①主语＝凯莉（敲门的人）②受事＝梅尔与欧拉莉亚家的门 ③「另一方」＝梅尔/欧拉莉亚，无归属反转 | **对应成立**（密度够：有「为什么」） |
| B2 | [1066, 1245]｜`text/ch36:23` 「Mel thought Callie’s make-up helped … Mel was furious.」 | **部分**：主体在讲这句引语（装备检阅＝逐项清点妆容/发型/裙子；「梅尔生气了」），但「为什么这样写」点名的「**她本不该这么好看**」那句落在引语**之前**（`text/ch36:23`），即讲到了引语之外的上下文。 | ①主语＝梅尔（做评价的人）②受事＝凯莉（被看的人）③「谁的」＝make-up/hairdresser/dress **都属凯莉**（原文 `she’d got a good hairdresser who’d given her a blow out`）——md 中文理解写成「她还认识一个…发型师」把雇用关系走样为「认识」（3-diff X6） | **引语选短**（应把引语前扩一句覆盖「shouldn’t have been this attractive」；分析本身不要删） |
| B3 | [1553, 1754]｜`text/ch36:29` 「She admired Callie’s work ethic … marched in with.」 | **是**。中文理解＝「欣赏敬业与那一大堆道具 / 觉得自己拿到了对等价钱 / 不欣赏那份自信」；为什么这样写＝「借梅尔把『欣赏作品』和『喜欢这个人』拆成两件事」。 | ①主语＝梅尔 ②受事＝凯莉的 work ethic 与 props ③「自己拿到了对等价钱」＝梅尔是花钱的一方（原文 `Mel felt she was getting her money’s worth`）——md 归属正确 | **对应成立** |
| B4 | [5879, 6110]｜`text/ch36:122` 「You don’t like other women … a hog in lipstick.」 | **是**（讲的正是这句攻击）。但「为什么这样写」里的**「让第三方…盖了一枚勋章」**在归属上不成立：欧拉莉亚是这场会面的**主人之一**（`text/ch36:83` 她走进客厅、`:110` 她向梅尔发难），不是第三方；且此处被「盖章」的是凯莉的**衣着**，与本章「作品＝概念与手册」的框架冲突（3-diff X3）。 | ①主语＝**欧拉莉亚**（`text/ch36:110`「Eulalia hissed」）②受事＝梅尔（「you look like a hog in lipstick」中的 you＝梅尔）③「谁的」＝被攻击者＝梅尔；被夸奖者＝凯莉。md 的中文理解归属正确（「欧拉莉亚说梅尔不喜欢别的女人」） | **对应成立**，但**归属措辞有误**（只记不改级：把「第三方」改掉即可） |
| B5 | [6505, 6712]｜`text/ch36:134` 「Eulalia stared at the ground … pocket of her jeans.」 | **是**，而且是全章对应最好的一块：中文理解＝「盯着凯莉包放过的地方，捡起一样东西，那不是垃圾，是宝贝，塞进牛仔裤口袋」；为什么这样写＝**跨段给出「这件东西是什么」并解释「为什么这样写」**（把身体痕迹写成别人眼中的珍宝），不是字面复述。 | ①主语＝欧拉莉亚 ②受事＝地上那件物事（= `text/ch36:44` 从包里滚出的棉花球）③「谁的」＝口袋是欧拉莉亚自己的 | **对应成立**（密度足；跨段识别有原文支撑，见 3-diff「已核实为正确」第 1 条） |
| B6 | [7288, 7534]｜`text/ch36:143` 「She’d then bound them herself Japanese-style … two years prior.」 | **是**。中文理解＝自己日式线订、黑丝绒带、旧裙余料提花缎封面；为什么这样写＝把工序写成「礼物的制作」并给出「作品的分量」——有 why。 | ①主语＝凯莉（`She’d then bound them`）②受事＝那几本册子 ③「谁的」＝**两年前她自己那条裙子的余料**（`a skirt she’d made two years prior`）——md 说「两年前做裙子剩下的」归属正确 | **对应成立**（仅「暖橙与巧克力色」被压成「橙棕色调」，措辞级） |
| B7 | [10242, 10375]｜`text/ch36:194` 「Of course she’d gone through the samples first … hidden the others.」 | **是**。中文理解＝梅尔预先筛过、只留她要欧拉莉亚挑的、其余藏起来；为什么这样写＝「选择权早已被做过手脚」的冷意。 | ①主语＝**梅尔**（`she’d gone through the samples`）②受事＝样品（samples）③「谁的」＝「她想让欧拉莉亚挑的」＝梅尔的主意；被蒙在鼓里的是欧拉莉亚与凯莉 | **对应成立**；但「凯莉对此一无所知」比原文强（原文只写她「confused」、察觉 Mel 的 smug，3-diff X4） |
| B8 | [11642, 11759]｜`text/ch36:221` 「Callie stood in front of the boards … The glamour.」 | **是**。中文理解＝四个名词一一对上；为什么这样写＝「把讲解压成四个名词」「从手工变成体系」——有 why。 | ①主语＝凯莉 ②受事＝展板（boards）③「谁的」＝概念是**她的**（`explaining the concept`） | **对应成立**；但读者提示里「**与香水的名字对照着读**」指向一个全书不存在的名字（3-diff X5） |
| B9 | [12869, 12992]｜`text/ch36:234` 「I’ve got to say, that was bloody fascinating … the usual shit I see.」 | **部分**：主体在讲这句引语（正面评价落在手册这一实物上、为什么这样写讲「认可会扩散出去」），但中文理解把引语**之后**的句子也说了出来——「紧接着她还说要把这一本带回办公室传看」（原文 `text/ch36:234` 紧接下一句：`I’m going to take this one back with me to pass around the office`），即分析覆盖的原文比引语长。 | ①主语＝**Venetia**（那位女士，非 Adam）②受事＝手册（the booklet you made）③「谁的」＝手册是**凯莉做的**（`the booklet you made`）——md 归属正确 | **引语选短**（把「take this one back… pass around the office」并入引语，或把该句从中文理解里撤出） |
| B10 | [13124, 13225]｜`text/ch36:234` 「I wasn’t sure how that was going to go … the other not enough.」 | **是**。中文理解＝「原本也不确定会怎么样 / 那两位啊：一个存在感太强，另一个又不够」；为什么这样写＝「两句极短的评价构成一组对称的诊断」＋「局外人在作品谈完之后才下判语」，并回扣本章「作品被审视 / 人被审视」两条账——有 why，且**没有**把「too present / not enough」分配给具体人（与原文一致，属正确处理，不许改）。 | ①主语＝Venetia ②受事＝「那两位」＝梅尔与欧拉莉亚（`those two`，原文未指名，md 也未指名）③「谁的」＝评价的受事是两个人，评价者是局外人 | **对应成立**（密度足、归属正） |

## 逐块小结

- **对应成立**：B1、B3、B4（措辞有归属小瑕）、B5、B6、B7（程度词偏强）、B8、B10 —— 8 块
- **引语选短**：B2（分析写到引语外的「她本不该这么好看」）、B9（中文理解写到引语外的「带回办公室传看」）—— 2 块
- **不对应（讲全书主旨/作者生平）**：0 块
- **密度不足（只复述字面、无 why）**：0 块 —— 10 块的「为什么这样写」均给出写法层面的理由（提前的细节、装备检阅、三层评价、排比勋章、珍宝化、工序化、被做手脚、压成四名词、兑现代价值、对称诊断）

## 本章专属判据的落点：「作品被审视」与「人被审视」

- **原文事实**：同一场会面里，**被评价的实物**只有两样——五本手册（Venetia：`I love the booklet you made. So much more original than the usual shit I see.`）与 Callie 本人（Mel 的逐寸打量、Eulalia 的触碰与占有式赞美、Venetia 的旧识亲昵）。
- **原文事实**：Callie 准备得越充分（提前到场、五块展板、自己装订的手工册），**梅尔越急**（`the quicker the commercial contracts got signed`）、**欧拉莉亚越被挤到边缘**（`Eulalia hovered by the window. She stared out of it.`）。md 抓到了这条对照（导航·叙事手法「把『作品被审视』与『人被审视』拆成两笔互不相干的账」）。
- **原文事实**：本章「作品」一侧还发生了**钱的转移**（Mel 付款），而 md 未写（3-diff L1）；「人」一侧，Callie 对 Eulalia 的警惕（`a bit of a ‘Laura’`）未写（3-diff L2）。**这条对照的另一半 md 抓到了，代价那一半没抓到。**
- **对方是谁（PCQV 的哪一方）**：ch36 原文写得很清楚——来的是「**The team from PCQV**」两人：Venetia（`I’m in charge of brand`）与 Adam（`from business planning`）；Callie 最初只凭西装把 Adam 猜成「business side」。md 的「那位女士」归属正确（见 4-verdict A4），但把 PCQV 整个说成「唱片公司」是错的（3-diff X1 / C1）。
