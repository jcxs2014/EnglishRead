# 4-correspondence.md · ch43 逐块对应（R4）

> R4 只回答一个问题：**这段中文是不是在讲这句引语？**（不看子项标题，不引入引语之外的解释）

| 块 | 引语（原文区间 `text/ch43_43.txt`） | R4 三问结论 | 依据 |
|---|---|---|---|
| 1 | Matt 给论坛定性：「把真实当代人物塞进中世纪故事乱搞」（L23） | 对应 | 中文理解讲的正是「把现实里活着的人塞进中世纪的故事，跟任何人、任何东西乱搞」；「为什么这样写」的「先讲游戏规则，后面的泄密才有支点」也对得上「游戏规则」这一说法本身 ✓ |
| 2 | Matt：「In my one… Isolde talks about being allergic to strawberries… one of your facts from Digby’s letters, right?」（L35） | 对应 | 「草莓过敏出自迪吉书信」＝引语内 `Her allergy was one of your facts from Digby’s letters` ✓；「写故事的人手里握着案卷级的私人资料」＝把设定与来源并置的分析，引语内无越界内容 ✓ |
| 3 | Matt 刷新页面，新故事不是 Isolde 账号，「一个喜欢她所有作品、总在评论的人」（L41） | 对应 | 中文理解逐项对上：`Another story just dropped` / `It’s not from Isolde’s handle though` / `someone who likes all of hers and is always commenting` ✓；「换了署名，就多了一个可能的作者」是引语的分析 ✓ |
| 4 | Matt 出声朗读：「让我来搭台子……一个侍从，尚未受封，正在学搭救落难少女的本事」（L68） | 对应 | 「还没受封的侍从，正在学着如何搭救落难少女」＝ `A squire, not yet a knight, is learning his trade in rescuing fair damsels` ✓；「作者还特意让他念出声」＝引语内 `Matt began reading the story aloud` ✓ |
| 5 | Amy 肩后那段韵文 ＋ 她指出 Clemmie O'Hara（L83） | 对应 | 中文理解的三句韵文翻译逐句对上（`Neath a laurel` / `her dark knight an ignoble lover` / `He loved all over town`），「跟上司有染后死在灌木丛下」＝ `found dead under a bush after having an affair with her boss` ✓；「为什么这样写」的「艳妇、暗黑骑士、情爱遍及全镇各自对应哪一桩旧案」三个意象全在引语内 ✓ |
| 6 | Matt 一边下滑一边断言：作者把自己写进情欲三角（L104） | 对应 | 中文理解「作者把自己写进了一个情欲盎然的三方关系里」＝引语逐字对应 ✓；「写的人不再站在故事外面，他就在局中」是引语内判断的延伸，未越出引语 ✓ |

**6/6 块成立**（改后）。

- 「引语选短」（讲的是引语之外的上下文）：**0**
- 「不对应」（讲全书主旨/作者生平）：**0**
- 「密度不足」（只复述字面、无「为什么这样写」）：**0**
- 形式提示：块 2 的引语 44 词、块 5 的引语 64 词，均 ≤100 词阈值 ✓（`chapter.sh`：「引语长度：全部 ≤100 词」）

**归属复核**（逐块回原文对说话人）：

| 块 | 引语出处 | 说话人 | md 归属 | 结论 |
|---|---|---|---|---|
| 1 | `…,’ Matt said.` | Matt | Matt | ✓ |
| 2 | `‘In my one…`（接 Matt 的上一轮发问之后） | Matt | Matt | ✓ |
| 3 | `Matt refreshed the group page.` | Matt | Matt | ✓ |
| 4 | `‘Amy, listen to this.’ Matt began reading the story aloud.` | Matt | Matt | ✓ |
| 5 | `Amy stood over his shoulder.` … `She looked at Matt.` | **Amy**（韵文朗读者原文未标，见 3-diff 三·1） | Amy | ✓（朗读者为推断项，提示级） |
| 6 | `Matt continued scrolling.` | Matt | Matt | ✓ |

**归属错误 0。**（本章 md 唯一的主语错误不在块内，而在导航与总结两层——办案人被安到 Amy/Matt 自己身上，见 3-diff B1。）
