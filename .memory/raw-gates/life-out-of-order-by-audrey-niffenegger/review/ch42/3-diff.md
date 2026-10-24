# ch42 embodiment — 对账单（R3，复核版）

- 原文：`text/ch42_embodiment.txt`（396 行）；精读：`ch42 embodiment.md`（131 行，**mtime 2026-10-25 01:06:34**）
- 素读：`1-suread.json`（11 条，396 行全文读完）；机器层：`2-machine.json` rc=0，verdict=ok，8 块 / 8 段引语全逐字（segment_miss 0 / empty_quote 0 / struct_bad 0 / keyword_bad 0 / cjk_low 0）、nav 5 条、H1 `42. Embodiment`、words 2908
- ⚠️ **版本注记（关键）**：上一版 `3-diff.md`（00:56）把 E1「一月十四日叙述者是阿尔芭」与 E2「母亲下楼讲和」判为**阻断**；当前 md 在这两处**已经改对** —— `:15` 现写「一月十二日由阿尔芭记，一月十四日与五月五日由贝克讲」，`:12` 现写「贝克承认自己苛刻，下楼去……」。本轮据当前文件重判，E1/E2 **降为「已修复」，不计阻断**（证据见 §四.1、§四.2）。

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | 换养老院的**因由**：原来那家失火 | `:23` "they have to move Beck's parents into a different nursing home because the one they were living in caught fire" | `:11` 只写「去底特律」；`:131` 写「处理养老院的事」；`/usr/bin/grep -c "失火"` → 0 | 提示（因果压缩，不误读） |
| L2 | 次日晨 Carl 问「我要不长这样你还爱吗」＋「You never know.」 | `:124` "Would you still love me if I didn't look like this?"；`:132` "'You never know.'" | 全篇无此场景（`grep -c "剃\|刮胡子"` → 0）；1 月 12 日段在 md 只剩 `:15` 一句概述 | 提示（对 Carl 身份最重的暗示；本章转折不在此，未按阻断计，建议导航补一句） |
| L3 | 短信里 Alba 否掉「请 Nick 和 Nadia」 | `:42` "should we invite nick and nadia?"；`:45` "nope, just us" | 未收；`grep -c "尼克\|纳迪亚"` → 0 | 提示 |
| L4 | 不敢一个人做饭，怕自己消失烧房子 | `:53` "I don't like to cook by myself in case I vanish and burn down the house" | 未收（块 1 止于 "So I invite Carl over"） | 提示（本书时间消失设定的轻笔） |
| L5 | 停战成立的**办法**：年长 Alba 把未来告诉她；Beck 事后才确证「她见过他」 | `:299` "She's telling Isadora her future."；`:307` "she's old enough to know all the outcomes, so she will tell if it supports whatever happens"；`:344` "She's seen him. They didn't meet each other. He doesn't know about her." | `:11`／`:131` 只有「谈成停战」；`grep -c "未来"` → 0 | 提示（转折已在导航，缺的是机制） |
| L6 | 年龄锚：Alba 17 / Carl 17 | `:18` "(Alba is 17)"；`:225` "He is seventeen, the same age as Alba." | 无年龄；`grep -c "十七"` → 0 | 跳过（同 ch30 口径） |

「零命中」取证：

```
/usr/bin/grep -cE '未来' "notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch42 embodiment.md"        → 0；退出码 1
/usr/bin/grep -cE '失火' "notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch42 embodiment.md"        → 0；退出码 1
/usr/bin/grep -cE '尼克|纳迪亚' "notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch42 embodiment.md"  → 0；退出码 1
```

## 二、编（md 有、原文无）

| # | md 说法 | 核查 | 档 |
|---|---|---|---|
| F1 | `:13`「被造出的孩子**索要身体**与爱」 | 原文她要的是「一个真人」与「到外面去」：`:246` "I need the actual person. Boyfriends are human?"、`:256` "I could be out there, with the boyfriend, who is human?"——没有一句要「身体」 | 提示（措辞外推，宜改「一个真人」） |

其余：8 块中文与 nav 5 条均无凭空人名／数字。「弗兰肯斯坦」=`:316` "Dr. Frankenstein. Don't be mean to your monster."；「准备好就拔插头」=`:290` "I'm ready to unplug her."；「树下」=`:396` "sitting under the tree"；「听见楼上的克莱尔在动」=`:396` "I can hear Clare stirring upstairs"。

## 三、错（两边都有、不一致）

| # | md 说法 | 原文 | 档 |
|---|---|---|---|
| E3 | `:13`「先被说不像人，再被说不像成年人」 | `:173` 是 Isadora **自问** "I don't look sufficiently human to be romantic?"；`:177` Beck 第一次否定的是**年龄**："You don't look old enough to inspire thoughts of romance… You look like a child. It's a category error."；`:181` 自行加龄后才说「Barbie-doll version of Lucinda」 | 提示（顺序倒置＋把自问写成「被说」；分析层表述） |
| E4 | `:12`「工作间里的亲密被屏幕另一头看见」 | `:110` 只写绿灯亮＋Alba 自问 "What has Isadora seen?"；`:344` "She's seen him" 指看见 Carl 本人 | 提示（把不确定写成确定，改「可能被看见」即可） |
| E5 | `:11`／`:131`「卡尔误入地下室的工作室」 | `:79` "I just want to see, I won't touch anything."＋"Carl has strong urbex tendencies. He loves being where he isn't supposed to be."；门是 Alba 与 Lucinda 忘锁（`:66` "Lucinda and I must have forgotten to close up"） | 提示（「误入」把主动探看写成误闯；**方向没错**：不是阿尔芭带他下去的） |

## 四、已核实为正确（防下一轮误修）

1. **叙述者归属（原 E1 已修复）**：`:15`「一月十二日由阿尔芭记，一月十四日与五月五日由贝克讲」＝ 原文 `:23` 段首 "Alba:"、`:146` "Beck: Clare and I get home later than we'd planned"。
2. **下楼赔不是的是贝克（原 E2 已修复）**：`:396` "I suddenly feel ashamed of myself for being so harsh with Isadora. I can hear Clare stirring upstairs, but instead of waiting for her I go downstairs to make amends to my lonely monster-daughter."；Clare 本章只「在楼上走动」，未发一言。**不得改回「母亲下楼」。**
3. **绿灯＝Isadora 醒着**：`:93` "The little green light that indicates Isadora's awake is not lit, to my relief."——md `:47` 成立。
4. **停战由年长 Alba 谈成**：`:294` "I hear her say, 'Isadora! Shut the fuck up for a minute! Listen!'"、`:370` "Detente. Isadora will behave herself."——md `:11` 正确。
5. **「嘴上不知道、心里明白不会做」**：`:260` "I don't know how to make that happen." ＋ 同段 "I don't add that I wouldn't do it, even if I knew how."——md `:131` 成立，勿删。
6. **镜像房间四处细节**：`:152` "…sitting on the sofa, wearing a black dress with skinny straps, high heels and dark red lipstick, holding a wineglass that's half full of pale yellow liquid."——md `:51`「半杯」「暗红」未写错。
7. **「她要的是真的」是年长 Alba 的判断**：`:326` "She wants the real thing. Her emotions are real… she doesn't want a synthetic love. Would you?"——md 未挂到贝克名下。
8. **年长 Alba 的年龄外貌**：`:277` "The extra Alba is in her late fifties or early sixties."、`:278` "Her hair is waist-length and completely white"——md `:81` 一致。
9. **「怪物女儿」**：`:396` "my lonely monster-daughter"、`:317` "Don't be mean to your monster."——md `:91` 有据。
