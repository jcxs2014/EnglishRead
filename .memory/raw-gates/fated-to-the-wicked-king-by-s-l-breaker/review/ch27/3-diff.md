# ch27 对账（R3）

R1：`1-suread.json`（10 条：8 正文＋关系＋数字）。R2：`2-machine.json`（13 块 / 13 片段 / 查无 0）。
边界：正文止于第 531 行（`I'm sure they are going to live happily ever—you know.`）；第 539 行起为作者的话/Patreon/下册预告，**未引、未析**。

## 漏
| # | 素读事实 | md | 判定 |
|---|---|---|---|
| 1 | 记忆洪流回灌、她认出自己是 Eleanor Carter | ✅ 原句1＋原句2 | — |
| 2 | 她趁他睡着取走 F-capacitor、换衣下楼 | ✅ 导航（装上最后一枚 F-capacitor） | — |
| 3 | **他从背后抱住她：“No cage will hold you… Not even the prison of my heart.”** | ❌ md 0 次（`/usr/bin/grep -c "牢笼"` → 0，exit 1） | **阻断（已修）**：导航补入（`text/ch27:148` 逐字） |
| 4 | General 闯入、拉开关、掏出原世界的手枪 | ✅ 原句5＋原句6 语境 | — |
| 5 | 她扑枪被甩倒、**Rabb 从背后锁喉**、她按下按钮冻住 General | ✅ 原句7 | — |
| 6 | 午夜潮汐、机器停不下、她装上 F-capacitor 并设过载 | ✅ 原句9 | — |
| 7 | **告别：“My love… you would have made a fine queen.”** | ❌ md 0 次 | **阻断（已修）**：导航补入，并标注 would have made 的虚拟语气 |
| 8 | 她穿过光球、钟楼上部爆炸、钟面裂开坠落 | ✅ 原句11＋原句12 | — |
| 9 | 国王捡起齿轮护身符、扎进漩涡追她 | ✅ 原句12 | — |
| 10 | 【数字】42,000 比 1 的存活概率 | ✅ 导航（forty-two-thousand-to-one） | — |

## 编 / 错
| # | md | 原文 | 判定 |
|---|---|---|---|
| 1 | 「My love… you would have made a fine queen」 | `text/ch27:409` 逐字 | 成立（**虚拟语气**，md 标注） |
| 2 | 「No cage will hold you…」 | `text/ch27:148` 逐字 | 成立 |
| 3 | 原句9「I'm setting it to overload after I go」 | `text/ch27:379` 区间 | 成立 |
| 4 | 原句10「I can't be selfish again」 | `text/ch27:391` 逐字 | 成立 |
| 5 | 导航「写 happily ever—you know」 | `text/ch27:531` | 成立（作者故意截断） |
