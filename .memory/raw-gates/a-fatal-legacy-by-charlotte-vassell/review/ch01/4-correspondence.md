# 4-correspondence.md · 第 1 章逐块对应（唯一问题：这段中文是不是在讲这句引语？）

判据（`docs/rules/审查表.md` R4）：
- 讲的是引语之外的上下文 → **引语选短了**（退回创建卡 §2 ①）
- 讲的是全书主旨 / 作者生平 → **不对应**
- 只复述字面、没有「为什么这样写」 → **密度不足**

引语原文位置取 `text/ch01_1.txt` 的**原始文件**字符偏移（已独立复核，6/6 原样命中）。

| 块号 | 引语（起止字符区间） | 结论 | 一句依据 |
|---|---|---|---|
| 原句 1 | `Digby Combe-Watson is sprawled out… made merry with the ruins of Persepolis.`（**71–378**） | **对应（轻微外扩）** | 中文理解逐项复述了同一句（1849 / 纳赛尔·丁 / 曾曾曾祖父 / 亚历山大 / 波斯波利斯），「为什么这样写」给出的是本句的写法选择（先给地毯身世、后给死状）；但收尾句引述的「最后一句『僵硬的标本正在看着他』」与本块/原句 6 的译文不一致，且「这间屋子」的藏品母题取自本章后文——属**引语覆盖不足 + 内部引述不实**，不判不对应。 |
| 原句 2 | `Digby can’t feel his toes. Oh dear. It’s all happening so quickly.`（**806–872**） | **对应** | 分析贴着这三句本身展开：三个短句的下行节奏、`Oh dear` 的轻语气反差、`happening so quickly` 的时间感，并顺势立下「自下而上推进」这一线索——不是字面复述，有「为什么」。 |
| 原句 3 | `He was a man, after all, and cardinal rules like meet in a public place applied to only women.`（**1061–1155**） | **对应** | 分析抓的是这句自辩的**修辞功能**（性别给自己开后门 → 暗示邀约者即嫌疑者），不是复述字面；密度足够。惟因果方向与原文相反（原文先赴约后自辩），已在 3-diff.md X2 记为「错·提示」，**不构成不对应**。 |
| 原句 4 | `The coldness, the frozen hand of death, is moving up his body inch by mortal inch.`（**1546–1628**） | **对应** | 「一寸一寸」的速度感、`mortal` 一词的凡人肉身绑定、与原句 2 的时间感互参，三条都长在这句引语上；没有跑到全书主旨上去。 |
| 原句 5 | `He catches a cold steely eye lazily gazing back at him… the morbidity of his odious ancestor.`（**1810–1981**） | **不对应（阻断）** | 「为什么这样写」断言 `那双冷硬如钢的眼睛来自这间屋子里的收藏，与开篇铺陈的柜中标本彼此呼应`——原文里这只眼睛是**回望他的活人（凶手）**，藏品是另一组东西（`Horatio Combe’s shrine to his obsessions.` / `The shrunken heads watch from their cabinet…`）；这段中文讲的根本不是这句引语，而是 md 自己虚构的「凶手即藏品」关系。 |
| 原句 6 | `The shrunken heads watch from their cabinet as his heart stops.`（**2340–2403**） | **对应** | 主语是标本而非人这一句的写法选择被拆开讲（以「归档」收束、把谋杀现场与博物馆日常叠合），有「为什么」，且未越到作者生平或全书主旨。 |

**小结**：6 块中 5 块对应、1 块（原句 5）不对应；无「密度不足」块（6 块均含超出字面复述的「为什么这样写」层，机器测得该子项中文占比 0.81–0.92）；无「只讲全书主旨/作者生平」的块。
