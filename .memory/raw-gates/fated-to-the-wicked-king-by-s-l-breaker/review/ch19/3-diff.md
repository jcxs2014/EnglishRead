# ch19 对账（R3）

R1：`1-suread.json`（8 条）。R2：`2-machine.json`（6 块 / 8 片段 / 查无 0）。

## 漏
| # | 素读事实 | md | 判定 |
|---|---|---|---|
| 1 | 平台塌陷、肩先撞格栅、滚进钢墙；破管灌冰水 | ✅ 原句1＋原句2 | — |
| 2 | 他判断落在旧维修升降井、问她颈伤 | ⚠️ md 未写「维修井」 | 提示（不修）：`text/ch19:60` 区间 |
| 3 | 她向上呼救；Gregory 判上升索损坏、拒绝放索 | ✅ 原句3 | — |
| 4 | 【关系】Sophie 是他的最高优先；他拖走她、留下两人 | ✅ 导航＋原句3 语境 | — |
| 5 | Gregory 承诺带援手、目光越过国王以排除他 | ✅ 导航（the help was specifically not for him） | — |
| 6 | 【数字】潮汐还要数小时；他只给他们「几分钟」 | ✅ 原句4 | — |
| 7 | **两人推压力轮；水到腰际他让她爬高、她拒绝；她的手闪了一下、能透过手看见水** | ❌ md 0 次（`/usr/bin/grep -c "透明\|压力轮"` → 0，exit 1） | **阻断（已修）**：导航补入 `Then my hands flickered.` / `I saw the water through my fingers.`（`text/ch19:200–203`） |
| 8 | 水没口鼻→蓝白闪光→洪水排空→她昏过去 | ✅ 原句6 | — |

## 编 / 错
| # | md | 原文 | 判定 |
|---|---|---|---|
| 1 | 原句4「My powers are sapped」 | `text/ch19:118` 区间 | 成立 |
| 2 | 原句5「I forbid it」 | `text/ch19:236` 逐字 | 成立 |
| 3 | 原句6「the flood drained away beneath us」 | `text/ch19:270` 区间 | 成立（原文 beneath **us**，勿写 them） |
| 4 | 导航「那份援手不是给国王的」 | `text/ch19:130` 区间 | 成立 |
