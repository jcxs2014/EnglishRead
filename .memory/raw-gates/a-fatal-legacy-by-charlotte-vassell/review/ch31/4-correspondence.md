# 4-correspondence.md · ch31 · 逐块对应（R4）

> 只回答一个问题：**这块中文是不是在讲这句引语？**
> 判据（`docs/rules/审查表.md` R4）：
> ① 讲的是引语之外的上下文 → **引语选短**；
> ② 讲的是全书主旨/作者生平 → **不对应**；
> ③ 只复述字面、没有「为什么这样写」 → **密度不足**。
> 附加固定三问（施事/归属反转）：① 每个动词的主语是谁 ② 宾语/受事是谁 ③ 「谁的/谁欠谁/谁问的」回原文按 `by`/`to`/`from`/`of` 定方向。
> 引语位置由本人用 Python 独立复核（`body in src` = True，7/7）。

**每块一行**（附三问结论）：

| 块 | 引语（原文位置） | 这段中文在讲什么 | 对应判定 | 三问（主语 / 受事 / 归属） |
|---|---|---|---|---|
| **1** | `ch31:20` pos 36「A safe and well check… Who alerted us?」 | 讲引语本身：马特下车站定、房子 identical、户型 identical、问「谁通知我们的」；「为什么这样写」落到「广场被压成复印纸」「报警链先交给读者」——**有作者手法，不是字面复述** | **对应成立** | 主语＝马特（说、抬头看）／受事＝房子、广场／归属＝「identical to all the others in the square」＝对整座广场成立 ✓ |
| **2** | `ch31:35` pos 1124「one concerned fan called it in… 8 a.m. this morning」 | 「中文理解」第一句讲的是**引语外**的 `ch31:32`「And everyone watching thought what? That it was a bit?」（以为不过是节目效果）；「为什么这样写」又把 `ch31:68` 的「No one has a visual of the alley」挪成「广场上一户户人家，没有一个人看见」 | **对应不成立 —— 引语选短**（且语义漂移） | 引语内主语＝「一位牵挂的粉丝」／受事＝电话；md 把「everyone watching」当「围观者」、把「没人看见巷子」当「居民没看见」，**两处都要回原文改归属** |
| **3** | `ch31:41` pos 1988「What is this case you're working on?… A forensic technician was swabbing…」 | 前半（ Barry 发问、问号是「第二次」、取样拍照是例行程序）**在讲引语**；但「中文理解」把 Barry 写成**法医技师**（原文是另一人），「为什么这样写」末句凭空造出**围在场边的人** | **对应不成立**（主体错配 + 末句讲的是不存在的上下文） | 主语：Barry＝发问者 ✓、技术员＝擦拭者 ✗（md 把 Barry 混进去）／受事：尸体 T 恤、周围环境 ✓／归属：**Barry ≠ forensic technician**（`ch02:101` medical examiner）→ md 反了 |
| **4** | `ch31:44` pos 2216「I wouldn't want to live on this square. I'd be worried I would be next.」 | 「中文理解」「读者视角提示」**在讲引语**（下一个就是我）；但「为什么这样写」说**他替的不是自己，是住户**、**先想到的是邻居的安危** —— 主语被换成人 | **对应不成立 —— 施事/归属反转** | 原文：主语＝**Caius**（I would be next）／受事＝他自己／归属＝「他担心的对象」＝他自己 ✗ md 写成「住户、邻居的安危」 |
| **5** | `ch31:68` pos 4142「No. …Buses were stopping and starting… Quite a few of the houses have cameras… No one has a visual of the alley.」 | 主体在讲引语（后巷、高墙、公交与骑车人、摄像头朝内、规划许可）；但「中文理解」首句「马特问……凯厄斯答『不是』」的**问句在引语外**（`ch31:65`），「为什么这样写」把「Quite a few of the houses」升级成**整个广场家家有摄像头**并推出「每个人都确信自己是安全的」 | **部分对应 —— 首句引语外（提示级）+ 事实断言过强（阻断级，见 3-diff 编 3）** | 主语＝Caius（走巷子、看摄像头）／受事＝后巷、摄像头 ✓／归属：**量词被放大**（quite a few → 家家），断言层面的错不在主语，但同样过不了原文 |
| **6** | `ch31:74` pos 4847「Digby and Scott were definitely killed by the same person… The PO Box connection cannot be a coincidence. … These two break-ins could be a coincidence…」 | **在讲引语**，而且「一松一钉」的分析**是对的**：could（松动）/ cannot（钉子）两分；「同一片区域，谋杀和针对同时发生」正对应原句「The murder happens at the same time someone else is targeting the area」 | **对应成立**（但与导航「一句话概括」「一句话总结」的「顶了回去」互相矛盾——见 3-diff 编 4） | 主语＝Caius（说）／受事＝PO Box 关联、两起入室／归属：**cannot 属 PO Box 关联，could 属两起入室**，两句主语不同、并存；md 在导航里把二者写成互相推翻 ✗ |
| **7** | `ch31:101` pos 6943「"Fake Isolde" is clever… The PO Box purchased with a random card… using Scott to avoid being seen on the CCTV at the Post Office… and yet Jimmy died because of a dodgy step.」 | 「中文理解」「为什么这样写」**在讲引语**（手法老练 vs 死于一级台阶的反差＝留给读者的题）；但「中文理解」里「那张脸」归属不明，「为什么这样写」说「作者把这一章收在一句反差上」——引语 7 **不是本章末句** | **基本对应**（一处指代方向易反＋一处位置断言错，均为提示级） | 主语＝Caius（转述）／受事＝假 Isolde、PO Box／归属：**被「避免被看见」的是冒名者一方，斯科特是被利用去露面的人** ✗ md 的「那张脸」未指明，易读反 |

---

## 汇总

- **逐块对应成立**：块 1、块 6 —— **2 块**
- **部分对应（提示级瑕疵）**：块 5、块 7 —— **2 块**
- **对应不成立**：块 2（引语选短·阻断）、块 3（角色错配 + 编造围观人群·阻断）、块 4（施事反转·阻断）—— **3 块**
- **密度不足**：0 块（7 块的「为什么这样写」都给出了作者手法，无「只复述字面」的块）
- **不对应（讲全书主旨/作者生平）**：0 块
- **对应组阻断条数＝3**（块 2、块 3、块 4）；另有 2 条提示（块 5 首句越界、块 7 指代与位置）

> 备注：块 5 的「家家有摄像头」虽是**断言层**缺陷（已计入 3-diff 编 3，阻断），因其主语/受事/归属三项在引语内均正确，故在 R4 只记「部分对应」，不重复计入对应组阻断数。
