# ch08 对账（R3）

R1：`1-suread.json`（8 条）。R2：`2-machine.json`（8 块 / 9 片段 / 查无 0）。

## 漏
| # | 素读事实 | md | 判定 |
|---|---|---|---|
| 1 | 数不清多少夜没睡、夜里踱步 | ✅ 导航＋原句1 | — |
| 2 | Chez 凭空出现在寝殿 | ✅ 原句2 | — |
| 3 | 女巫传言（决定市民生死）＋她否认 | ✅ 原句3＋原句4 | — |
| 4 | 她自述：残余力量、感应意图、判断忠诚、护无辜 | ✅ 原句5 | — |
| 5 | Chez 提出带她逃走；她只答「Yes. No. Maybe.」 | ✅ 原句7 | — |
| 6 | 结尾国王不看她就下令带下一批囚犯 | ✅ 原句8 | — |
| 7 | 【关系】「Knowing Chez and the Duchess were on my side」 | ❌ md 0 次（`/usr/bin/grep -c Duchess` → 0，exit 1） | **提示（不修）**：`text/ch08:218` 的安心感是情绪补白，非情节转折 |
| 8 | 【数字】For several months（她数月来说服自己与他无关） | ❌ md 未用 | 提示（不修）：与 ch07 的 `eight whole months` 并存，二者不冲突（前者=她的自我说服期，后者=距上次亲近） |

## 编 / 错
| # | md | 原文 | 判定 |
|---|---|---|---|
| 1 | 导航「城堡内室样样由魔法备好」 | `text/ch08:19` "tea had been magically set up… washing implements had been prepared" | 成立 |
| 2 | 原句3「新得一位女巫，由她决定生死」 | `text/ch08:100` "having acquired a new sorceress. She who decides which citizens live or die." | 成立（**sorceress**，md 写「女巫」可，勿写成 witch） |
| 3 | 原句7「他追问『你不想走？』」 | `text/ch08:136` "Do you not want to leave?" | 成立 |
| 4 | 一句话总结「Yes. No. Maybe.」 | `text/ch08:142` 独立成段 | 成立 |
