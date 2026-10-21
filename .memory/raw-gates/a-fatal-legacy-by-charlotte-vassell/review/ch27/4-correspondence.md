# 4-correspondence.md · R4 逐块对应（人判）

判据（`docs/rules/审查表.md` R4）：不看子项标题，只回答「**这段中文是不是在讲这句引语**？」
- 讲的是引语之外的上下文 → 引语选短
- 讲的是全书主旨／作者生平 → 不对应
- 只复述字面、没有「为什么这样写」 → 密度不足
另加固定三问：① 每个动词的主语是谁 ② 受事/宾语是谁 ③ 「谁的／谁欠谁／谁问的」的归属方向（回原文看 `by`/`to`/`from`/`of`）。

逐块结论表（每块一行）：

| 块 | 引语原文区间 | 这段中文是不是在讲这句引语？ | 主语/受事核对（回原文） | 判定 |
|---|---|---|---|---|
| 原句 1 | char 276–611（line 26） | **是**。中文理解逐项对上：代号客户、动物园会员卡、猴子叫声、孩子会走路。 | 主语＝Callie（她在走路时回话）；受事＝「动物园会员卡」是盘算对象，「不能公开点名的那位」是 dinner 对象——与原文 `I’m out tonight having dinner with she-who-must-not-be-publicly-named` 一致 | 对应；**引语选短**（首句「Caius 打电话来预告自己要晚归」在引语前一句，char 106–134） |
| 原句 2 | char 2530–2796（line 62） | **是**。中文理解覆盖「听不下去→太私人→三种方式唱自我了断→album destructive→先破碎再重造」。 | 主语＝Callie（她的判断）；受事＝Eulalia 的音乐/专辑——与原文一致（`Now that she’d met Eulalia she couldn’t bear…`） | 对应；**但漏引同一自然段前半**（`It was about Julian of Norwich`，char 2282–2313）；另「自我了断」＝`trying to kill herself` 译重了 |
| 原句 3 | char 3629–3955（line 68） | **是**。中文理解逐项对上：三家餐厅、寿司问题、Botticelli、珍珠、蚌。 | 主语＝Eulalia（她在发问）；受事＝Callie（`Are you a sushi person?`、`You look like…`）——方向与原文一致（`Callie` 是被描述方，不是提问方） | 对应；计数「三次提问」与原文 8 个问号不符（见 3-diff X1） |
| 原句 4 | char 4628–4875（line 77） | **是**。中文理解覆盖「好多第一次约会／猜谁放鸽子／把对方拖进关于旁人的猜测／共谋式亲密」。 | 主语＝Callie（`My favourite game… This was an old trick of hers`）；受事＝对方（the other person）——方向一致 | 对应。「把话题挪到窗边那对食客」是引语外的下一轮（Eulalia 说 `That couple in the window.`），属延伸，不构成对应失败 |
| 原句 5 | char 6458–6711（line 119） | **是**。中文理解覆盖「想点一壶酒／被挡下／一杯 Valpolicella／Callie 点 Limonata」。 | **主语/受事核对要点**：原文里**想点酒的是 Eulalia**（`Eulalia tried to order a carafe of wine`）、**挡酒的是 Callie**（`but Callie said her dermatologist had told her to stop drinking`）；Callie 自己 `daintily refrained and ordered a Limonata`。md 中文理解写「Eulalia 本想点一壶葡萄酒，Callie 却说皮肤科医生为了她的皮肤让她别再喝」——**归属方向与原文一致** | 对应；但「半真半假的健康理由」是 md 自加的动机断言（原文未说，见 3-diff C4） |
| 原句 6 | char 7909–8012（line 137） | **是**。中文理解覆盖「Callie 请求先听专辑／Eulalia 无辜撅嘴／Mel 不会希望这样」。 | 提问的是 **Callie**（`‘Would it be possible to hear the album? It might help me with my process.’`，char 7496，在引语**之外**）；拒绝的话是 **Eulalia** 的；否决者是 **Mel**（转述）——md 写「Callie 问…Eulalia 说…Mel 不会希望」方向正确 | 对应；「Mel 第一次在餐桌上被点名」✓（全章 Mel 首次出现即此行，char 7977 之前 0 次）；**「决定了酒」是归属反转**（见 3-diff C1）；引语选短（Callie 的问句在引语外） |
| 原句 7 | char 8015–8153（line 140） | **是**。中文理解覆盖「说没关系／给小水壶各倒一杯／低声说不想让你惹麻烦」。 | 主语＝Callie（`Callie poured them each a glass of water`）；受事＝**them ＝两个人**（Callie 与 Eulalia），与原文 `them each` 一致；**没有第三人** | 对应；「倒了两杯不是三杯」✓（`Table for two`，char 4516）；**但「桌上剩下的液体只有水」与原文不符**（还有 Valpolicella 与 Limonata） |
| 原句 8 | char 9358–9502（line 161） | **是**。中文理解覆盖「Mel 改口／台上戴、拍照采访露脸」。 | 主语＝**Mel**（`Mel is now saying…`）＋ **Eulalia**（转述者，`the label’s plan is for me to perform`）；**不是 Callie**——md 中文理解写「Eulalia 说 Mel 现在改口了」方向正确 | 对应；「那份写清楚的方案在晚餐前被改了」✓（line 158 `Mel’s very clear brief had left them out`）；**「她接下来说的那句『我本来以为』后面的沉默」与原文不符**（原文是出声反问 + `Callie was confused`） |
| 原句 9 | char 11506–11809（line 200） | **是**。中文理解覆盖「Callie 点头／礼貌／快吃完了／Eulalia 揽肩亲脸颊／竖中指」。 | 主语＝Eulalia（`put her arm around Callie’s shoulder and kissed her on the cheek`、`flipped him the bird`）；受事＝Callie（被揽被亲）与**邻桌男人**（被竖中指）——md 写「伸手揽住 Callie 的肩、亲了亲她的脸颊，然后转过身，冲那个男人比了个中指」方向**正确** | 对应；**引语选短**（首句「侍者送来两杯 limoncello」在引语前一句，char 11369–11412）；「作者在本章里点破」应为 Callie 的推测（line 218） |
| 原句 10 | char 16679–17032（line 320） | **是**。中文理解覆盖「也许吧／掩饰敷衍的礼貌笑容／坐进后座报地址／Eulalia 挥手／给 Caius 发短信说有点怪」。 | 主语＝Callie（`she texted Caius from the back of the cab that Eulalia was kind of weird`）；受事＝Caius（短信对象）——方向正确 | 对应；密度足够（「用『有点怪』这种最省力的说法打包一整晚」是「为什么这样写」而非复述）；提及 £60 现金在引语外，但属对照而非主体 |

**逐块小结**

- 10 块**没有一块**出现「讲的是全书主旨／作者生平」的不对应情形：每块的中文都落在本块引语上。
- 10 块**全部**有「为什么这样写」，且都给出装置级理由（不只复述字面），**密度不足 0 块**。机器层佐证：10 块「中文理解」CJK 占比 0.54–0.82、「为什么这样写」0.69–0.90，无一块低于门禁。
- 施事／归属三问的结果：主语错配 **1 处**（导航「玻璃」句说话人＝Eulalia 却写成 Callie）；受事方向错 **0 处**（原句 5「谁在给谁斟酒」写对了：想点酒＝Eulalia、挡酒＝Callie、倒水＝Callie 倒两杯）；「谁问的」错配 **0 处**（原句 6、8 的提问/否决归属正确）；但**决定权归属**错 1 处（原句 6 与导航把「酒」的开关归给 Mel）。
- 引语选短（分析覆盖的原文比引语长）：**3 块**（原句 1、6、9）——均只多出紧邻的上一句，且都在正文另处被覆盖，判提示。
- 引语选长／跨话轮拼接／省略号缝合：**0 处**（10 段引语机器逐字 10/10 命中，每块只有一段、无 `…` 拼接）。
