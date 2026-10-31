# R3 对账 · ch13（R1 素读 8 条 vs md 10 块→修复后 11 块）

## 漏（素读有、md 无）

| R1 # | 事实 | 判定 | 处置 |
|---|---|---|---|
| R1#6 | 妈妈听到 Waboose 之名僵住捂眼、「No. No way.」、支开孩子——家族隐藏历史的关键信号 | **阻断（漏）** | **已同步修复**：插入新块 原句8（30 词，逐字命中 text:211 段），后续块顺延为 9–11；chapter.sh rc=0，commit 1504fff47 |
| R1#2 后半 | Drew 在法官面前称熊「约 300 磅、显然自杀式」 | 提示（不修） | 撞熊事件本体由块3 覆盖；300 磅是 Drew 的抗辩措辞（text:151 段），块5 分析已写「Drew 被制住」的语境 |
| R1#3 后半 | Thunder Lake 村人口 842 | 提示（不修） | 「遇见耶稣」笑话由块4 覆盖；人口数是调侃的注脚（text:85 段） |

**其余 R1#1/4/5/7/8 全部有块覆盖**（GPS/目的地→块1/2+导航、法官判决→块5/6、GPS 指 Waboose→块7、留下孩子→块8、五词课→块9、结尾→块10/11）。

## 编（md 有、原文无）

- 导航「Henry Small Oak / crane clan」← text:133 段 ✓
- 块1「THUNDER LAKE, TEN MILES」← 逐字 ✓
- 块3「Makwa. Makwa. Makwa. Makwa.」← 逐字（四次重复）✓
- 块7「ornery cuss / talk the bark off a tree」← text:193 段 ✓
- 块10（修复前为9）「五个新的奥吉布瓦词」← "learning five new Ojibwe words a day" ✓

**编 0 条。**

## 错（两边都有但不一致）

- 施事：块3 "Then we hit it, or it hits us"——双向撞击保留 ✓；"Drew swears the steering was taken over"——发誓者=Drew、被接管=方向盘 ✓。
- 施事：块4 "'Ah, Makwa.' The man gestures with his chin"——说话人=当地男人 ✓；"That old one rises from the dead every time just like Jesus"——复活者=那头熊（"That old one"）✓。
- 施事：块6 "because Makwa has chosen you"——施动=Makwa、受事=你们全家 ✓；"Neeb will give you a pass"——发放者=Neeb ✓。
- 施事：块8（修复前7）"'I'll keep the girl and the book-boy with me'"——说话人=Waboose、留下对象=Gil 与 Tony ✓；"places his fist over his heart"——按心口者=Waboose ✓。
- R1#6 妈妈反应与修复后块8 一致（freeze/cover eyes/Pollyanna deflates）✓。

**错 0 条。**
