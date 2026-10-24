# ch27 对账（漏 / 编 / 错）

原文：`text/ch27_speculations_upon_the_nature_of_love.txt`（180 行，**三个日期的短记拼成**：`Sunday, April 18, 2010 (Beck is 34, Clare is 38)` / `Saturday, April 24, 2010` / `Sunday, May 30, 2010`，末尾再接一小段「a few days later」无独立日期）。
精读：`ch27 speculations upon the nature of love.md`（90 行，4 块＝原句 1 `:28`、原句 2 `:33`、原句 3 `:65`、原句 4 `:145`）。

---

## 一、漏（md 无）

| 编号 | 素读条目 | 原文（逐字） | md 侧核查 | 档 |
|---|---|---|---|---|
| L1 | **Isadora 场景整段缺失**：4 月 18 日 Beck 晚到工作室，Isadora 先说破「You were with Clare.」；「Clare is a wild thing.」／「She's in the wild thing club, sweetie.」／「Wild thing, you make everything groovy,」——Beck 当场哭，「as though we're going to live happily ever after, after all.」这是第一则短记的情绪落点 | `:37`「This morning, when I arrived at my studio later than usual, Isadora asked me where I'd been, and before I could answer, she said, “You were with Clare.”」；`:44`「Isadora said, “Clare is a wild thing.”」；`:48`「I told her, “She's in the wild thing club, sweetie.”」；`:52`「Isadora replied, “Wild thing, you make everything groovy,” and then I started to cry, as though we're going to live happily ever after, after all.」 | `/usr/bin/grep -c -F "Isadora" "ch27 …md"` → **1**（唯一一处是 `:75` 词汇例句 `false dilemmas`）；`grep -c -F "groovy"` → **0**；导航 `:11-15` 五项、总结 `:90` 全段均无 Isadora、无「哭」 | **阻断** |
| L2 | 「You're perfect.」被 Beck 顶回：「Don't burden me with that. Sooner or later I'll disappoint you and what then?」→「Don't worry. Let's just be, here.」 | `:75`「I say, “You're perfect.”」；`:79`「Beck replies, “Don't burden me with that. Sooner or later I'll disappoint you and what then?” I start apologizing and Beck shushes me. “Don't worry. Let's just be, here.”」 | `grep -c -F "perfect"` → **0**；`"burden"` → **0** | 提示 |
| L3 | 4 月 24 日那句卡住的话：「Here and now,」+「I want to say I love you but it catches in my throat.」 | `:84`「“Here and now,” I say. I want to say I love you but it catches in my throat.」 | 块内无；总结 `:90`「她想说「我爱你」，话卡在喉咙里」已转述 | 提示 |
| L4 | 5 月 30 日的开场问题与两句核心台词：「I don't want you running into him at breakfast.」／「I've been waiting for Henry since I was a child. It's hard to stop.」／「Do you want to stop?」／「You're here now. I'd like to live in the present, with you.」——**全章分量最重的一组，md 里只活在词汇例句中** | `:111`「“It's weirder than that. I don't want you running into him at breakfast.”」；`:162`「She says, “I've been waiting for Henry since I was a child. It's hard to stop.”」；`:167`「“I bet it is. Do you want to stop?”」；`:171`「“You're here now. I'd like to live in the present, with you.”」 | `grep -c -F "waiting for Henry"` → **0**；`"breakfast"` → 1（`:85` 词汇例句）；`"present"` → 1（`:86` 词汇例句）；总结 `:90` 有转述 | 提示 |
| L5 | 黑人／女人的玩笑（这一段的情调，也是 Clare 说 Henry 会「意外」的原因） | `:115`「“Ugh. Okay, I take your point. But wouldn't he have mentioned that? 'Um, sweetie, are you shacking up with some brown lady after I'm gone?'”」；`:120`「“Henry wouldn't have been minded about the brown, it's the lady part that would have surprised him.”」；`:124`「“My lady parts aren't all that surprising.”」 | 块内无；`shacking up` 只在 `:76` 词汇例句 | 提示 |
| L6 | 日期头里的两个年龄与年份 | `:18`「Sunday, April 18, 2010 (Beck is 34, Clare is 38)」 | 导航/总结写「四月十八日」「四月二十四日」「五月三十日」，无年份、无 34／38 | 提示 |
| L7 | Alba 的住处处境（八岁、住外公或 Mrs. Kim）——Beck 为什么要问「couldn't I come over?」的前提 | `:97`「she's only eight, no reason to be too in-her-face about sleeping over. … So Alba stays with her grandfather or Mrs. Kim, and Clare comes to my apartment.」 | `grep -c -F "八岁"` → **0**；`"Kimy"` → 0；`"grandfather"` → 0 | 提示 |
| L8 | O'Hare 表亲午饭（关系「太顺」的证据之一） | `:33`「we meet my cousins for lunch near O'Hare one day when they have a layover, and she gets along with them immediately—we are joking around together before the drinks arrive.」 | `grep -c -F "O'Hare"` → **0**；`"午餐"` → 0 | 提示 |

## 二、编（md 有、原文无）

无凭空情节。唯一可疑处是「两个月后」（导航 `:12`），但 4/24 → 5/30 实为 36 天，属**数字松散**，归到下面第三节。

## 三、错（两边都有、不一致）

| 编号 | 断言 | 原文（逐字） | 错在哪 | 档 |
|---|---|---|---|---|
| E1 | 导航 `:14`「Clare 从守丧的人变成先开口的一方：**先问「现在？」**，先笑出声，最后先发出邀请」 | 4 月 24 日那一则署名为 `Clare:`（`:65`「Clare: We have to get a little drunk beforehand…」），段内原文是 `:65`「finally **she** says, “Now?” and **I** say, “Yes,”」——「she」＝Beck、「I」＝Clare。同段「先笑出声」确是 Clare（`:70`「And **I** start laughing」），邀请也是 Clare（`:179`） | **说话人归属反了**：问「Now?」的是 Beck，答「Yes」的是 Clare。三件事并列着写，读者会以为全是 Clare 做的 | **阻断** |
| E2 | 导航 `:12`「两个月后她们把 Henry 谈开」 | 日期头 `:60`「Saturday, April 24, 2010」→ `:92`「Sunday, May 30, 2010」 | 实为 **36 天**，不是两个月（无原文可依的近似数） | 提示 |
| E3 | 原句 1 中文理解 `:21`「她急切又客气，怕自己冒犯了她，为她担心，还想照顾她」 | `:28`「Clare who is eager and polite, who is afraid she's offended **me**, who worries about **me** and wants to take care of **me**」 | 一句里两个「她」指两个人（前者 Clare、后者 Beck），读者无法分辨 | 提示 |
| E4 | 原句 3 中文理解 `:41`「**她**不再是从前那个和 Henry 做爱的人，**她**也不是原来那个自己」 | `:65`「**I am not the same me** that used to make love to Henry」 | 原文是一个主语（Clare＝同一个「我」的前后两个版本），md 拆成两个「她」，像是两个人 | 提示 |

## 四、块序核对

原句 1（`:28`）→ 原句 2（`:33`）→ 原句 3（`:65`）→ 原句 4（`:145`），单调递增，**无倒置**。

## 五、取证命令记录

```bash
cd notes/books/novels/life-out-of-order-by-audrey-niffenegger
for p in "Isadora" "groovy" "perfect" "burden" "Jasper" "Kimy" "grandfather" "waiting for Henry" "haunted" "Now?" "八岁" "外公" "午餐" "O’Hare"; do
  printf '%-18s ' "$p"; /usr/bin/grep -c -F "$p" "ch27 speculations upon the nature of love.md"; done
# Isadora 1 / groovy 0 / perfect 0 / burden 0 / Jasper 1 / Kimy 0 / grandfather 0
# waiting for Henry 0 / haunted 0 / Now? 0 / 八岁 0 / 外公 0 / 午餐 0 / O’Hare 0
```
（退出码 1，因末条无命中；`grep -c` 逐条按行计数，不受 `text/` 被 gitignore 影响——此处查的是 md，不是 text。）
