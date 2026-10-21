# ch24 逐块对应（人判 · R4）

规则：只看每块的中文分析，回答一个问题——**这段中文是不是在讲这句引语？**
- 讲的是引语之外的上下文 → 引语选短了
- 讲的是全书主旨／作者生平 → 不对应
- 只复述字面、没有「为什么这样写」 → 密度不足
另附固定三问：① 每个动词的主语是谁 ② 宾语/受事是谁 ③「谁的／谁欠谁／谁问的」回原文看 `by`/`to`/`from`/`of`。

> 顺序：R1 素读落盘（`1-suread.json`）→ 才开 md。机器层 `2-machine.json` 只提供逐字/形态/密度，不参与本步判断。

| 块 | 引语（原文位置） | 这段中文在讲什么 | 对应？ | 密度 | 三问（主语/受事/归属） | 结论 |
|---|---|---|---|---|---|---|
| 块1 | `:20` "For the third time … He rang for a fourth time." | 中文理解逐句复述「第三次按铃／窗没擦／栏杆像矛／按了第四遍」；为什么这样写把它读成「开场把一次登门拖成僵持、栏杆让房子带敌意」；读者视角提示讲「被挡的次数与理由在变」 | **对应**（讲的就是这句引语本身） | 有「为什么」：把动作序列读成叙事策略，非字面复述 ✓ | ① 主语＝Caius（按铃、被栏杆挡住）② 受事＝窗户/栏杆/门铃 ③ 无归属反转 | **对应**；但读者视角提示引了引语之后的「I am important」与案情对话作前瞻（合法），不构成「引语选短」 |
| 块2 | `:41` "‘Oh, a DI.’ He swung the door open … ‘I suppose you may enter.’" | 中文理解逐句对上（开门/双手举起/I am important/读有品位文学/请进）；为什么这样写拆「一句话里挤着三件事：被需要的自我、文学品味、对来客的分类」——正是引语那三件事 | **对应** | 有「为什么」：拆解引语内部结构 ✓ | ① 主语＝Benedict（开门、举手、说话）② 受事＝门/Caius ③ 「I am important」的主语是他自己，不是 Caius ✓ | **对应** |
| 块3 | `:77` "‘I’m not going to lie, I’d had a few … white like death herself … they fled … the gin hadn’t agreed with me.’" | 中文理解逐句对上（没打算撒谎/几杯/正是你现在坐的那把/白得像死亡本人的脸/说不清长相/自己吓了一跳/对方跑了/杜松子酒不对劲）；为什么这样写抓「usual few 与 normal few 重复」与「惊悚笔触紧跟不可靠叙述」 | **对应** | 有「为什么」：解释重复措辞的酗酒者心理 + 恐怖与不可证并存 ✓ | ① 主语＝Benedict（说话、睡、惊跳）② 受事＝那把椅子/那张脸/杜松子酒 ③ 「The very one you're sat in now」= 对 Caius 说的第二人称 ✓ | **对应**（唯一瑕疵见 3-diff X4「不合身」误译） |
| 块4 | `:83` "‘Well here’s the thing … my back door was wide open … it was flapping about and so was the door to my basement. I never go down there.’" | 中文理解逐句对上；为什么这样写由此展开「没人翻动任何东西、书堆/抽屉原样、被打开的是地下室那扇门、后门是他历来不上锁的那扇」；读者视角提示落到「门开着却什么都没丢 → 只盯着地下室的目标访问」 | **对应**（分析对象＝这句引语所陈述的反常本身） | 有「为什么」：用「我总忘锁后门」的自辩反过来消解那扇敞开的门 ✓ | ① 主语＝Benedict ② 受事＝后门/地下室门 ③ 「Not conclusive」是他给自己下的判断 ✓ | **对应**；但分析引用的「书堆还堆着／抽屉原封未动」是本章别处场景（→ 3-diff L1/L2/C1/X2），不判「引语选短」 |
| 块5 | `:104` "‘What’s that?’ … It looked to him like a pentagram. Maybe Matt was right and the goths of Camden were really involved …" | 中文理解逐句对上；为什么这样写读「符号藏在漆层底下→比现有装修更老→Caius 立刻接上 Matt 的猜测」；读者视角提示给出「另一套来历（降神会）」 | **对应** | 有「为什么」：漆层埋藏这一点被用来说明「更老」 ✓ | ① 主语＝Caius（问、看出、联想）② 受事＝墙上的痕迹 ③ "Maybe **Matt** was right"＝归属明确指向 Matt，未安到 Benedict 头上 ✓ | **对应** |
| 块6 | `:143` "‘Only thirty years’ worth of manuscripts. Only a career. They didn’t steal that from me. Martin fucking Amis did.’ He gestured towards the door. ‘Thank you for taking me seriously.’" | 中文理解逐句对上（三十年的手稿/一段生涯/他们没能从我这里拿走/是 Martin Amis 拿走的/朝门一比/谢谢认真对待）；为什么这样写读「什么也没被偷」这句由 Benedict 自己说出→丢的其实是名声与位置→入室没有损失也就没有动机 | **对应** | 有「为什么」：把「没被偷」与「被 Martin Amis 毁掉生涯」并置 ✓ | ① 主语＝Benedict（拥有、被偷者）② 受事＝手稿/生涯 ③ "**They** didn't steal" vs "**Martin fucking Amis** did" 的施事方向被正确分开 ✓ | **对应** |
| 块7 | `:183` "A bunch of chequered fritillaria had been left at the base. He only knew they were fritillaria because **Callie** had pointed them out …" | 中文理解逐句对上（碑座下一束棋盘格纹贝母/因 Callie 在摄政公园周日上午散步时指给他看过）；为什么这样写讲收尾镜头由地下室移到露天广场、纪念碑的疙瘩造型与献辞、由一束花把读者拉回日常 | **对应** | 有「为什么」：把道具（花）当作把怪谈接回日常的收束件 ✓ | ① 主语＝Caius（认出、读牌）② 受事＝那束花 ③ "because **Callie** had pointed them out"＝归属明确是 Callie 告诉他的 ✓ | **对应**（读者视角提示里的 Alice 身份断言见 3-diff C4，跨章可证） |

---

## 逐块小结

- **对应**：7/7 块对应。**引语选短**：0。**不对应（讲主旨/生平）**：0。**密度不足**：0（7 块「为什么这样写」均给出写法层面的理由，机器 `cjk_low:0`）。
- **施事/归属反转**：逐块三问全部核对，**0 条反转**。块5「Matt 的猜测」、块6「They vs Martin Amis」、块7「Callie 指认」三处归属方向均与原文一致。
- 唯一受块内问题牵连的是块4（引用了引语之外的场景细节）与块7（跨章身份断言），二者均已在 `3-diff.md` 记为提示级。
