# ch04 对账（R3）

R1：`1-suread.json`（8 条）。R2：`2-machine.json`（6 块 / 7 片段 / 查无 0 / 最长 46 词）。

## 漏
| # | 素读事实 | md | 判定 |
|---|---|---|---|
| 1 | 骑黑烟云、兜帽斗篷、浅金发的男子落在阳台 | ✅ 原句1 | — |
| 2 | 惊醒，确认又是关于他的梦 | ✅ 导航「天亮才发现整场是梦」 | — |
| 3 | 被昨夜扔在地上的靴子绊了一下；另一只已当作丢失 | ✅ 原句5（"one boot"）＋导航 | — |
| 4 | 黑色马车浮在阁楼门外、男仆开门 | ✅ 导航＋词汇表 black stagecoach | — |
| 5 | 无形声音宣布国王召见、已查出靴子主人 | ✅ 导航「召令」；`:216` 原句 | — |
| 6 | 披实验袍、抓仅剩的靴子、男仆手中现出铁镣铐 | ✅ 原句5＋原句6 | — |
| 7 | 【关系】**祖母绿发簪是他当年给的「最后一件礼物」，她曾以为是爱情的信物** | ❌ md 0 次（`/usr/bin/grep -c "发簪\|发夹"` → 0，exit 1） | **阻断（已修）**：补入导航情感弧线。证据 `text/ch04:153` "He had given me this last gift that same night as well. I'd once thought it was a token of his love." |
| 8 | 【数字】阁楼离地约 five hundred feet | ⚠️ 未用 | 提示（不修）：环境尺寸，非剧情量 |

## 编 / 错
| # | md | 原文 | 判定 |
|---|---|---|---|
| 1 | 导航「她退到玻璃墙边也无路可退」 | `text/ch04:99` "the cool glass wall met my spine and I had nowhere left to retreat" | 成立 |
| 2 | 原句3「世界缩成两人之间那点空隙」 | `text/ch04:43` "the world narrowed to the space between us" | 成立 |
| 3 | 原句6「满腹怀疑地下巴都掉了」 | `text/ch04:243` "My jaw dropped in full skepticism." | 成立 |
| 4 | 原句4「无论他变成了什么、无论他们曾经是什么」 | `text/ch04:234` 对应 | 成立 |
