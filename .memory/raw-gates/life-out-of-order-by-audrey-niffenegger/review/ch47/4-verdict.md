# ch47 the air becomes music — 判定表（R5）

- 原文：`text/ch47_the_air_becomes_music.txt`（402 行）
- 精读：`ch47 the air becomes music.md`（152 行）
- 机器层：`2-machine.json` rc=0（verdict=ok，10 块，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5）
- 结论：**无阻断**；漏 8（提示）· 编 0 · 错 4（提示）· 跳过 2

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 10 块引语逐字、均属本章 | `2-machine.json` segments=10, segment_miss=0；回捞 `:23` `:96` `:129` `:182` `:198` `:221` `:258` `:279` `:387` `:393` 全命中 | 引语层干净 | 假红 |
| 2 | 块数 10 偏离本书常见区间 3–9 | `2-machine.json` form.block_hint；block_target [7,11] 仍达标 | 未超硬上限，只报不判红 | 假红 |
| 3 | 亲属称谓 | `grep -c "舅舅\|叔父"` → 0；全篇「叔叔斯蒂芬」；原文 `:23` “my Uncle Stephen” | 统一「叔叔」 | 已核实为正确 |
| 4 | 年龄与日期 | `:18` “Friday, November 1, 2041 (Oliver is 13)”；md:11「二〇四一年十一月，十三岁的青」 | 正确 | 已核实为正确 |
| 5 | **题眼句「人生就是一场长长的试奏」全无** | `:216` “the first lesson is that life is one big long audition.”；`grep -c "试奏"`→0、`grep -c "试音"`→0、`grep -c "audition"`→0（rc=1） | **漏**：全章立意句；它把「假事要真做」封了顶 | 提示 |
| 6 | 「他们演奏什么」「机器人」→「你要学的正是没有机器人的弹法」全无 | `:173` ““Robots.””；`:177` ““You are going to learn to play without robots, Oliver.””；`grep -c "机器人"`→0（rc=1，整篇无此三字） | **漏**：本章核心对照（用机器听音乐 → 学不用机器的琴） | 提示 |
| 7 | **「这个院子就是我昨晚来的那个院子——我当时在未来」全无** | `:226` “I realize that this is the garden I was in last night—I was here, in the future!”；`grep -c "昨晚"`→0 | **漏**：把 ch46 那夜的穿越与「老师家」缝在一起的关键接榫，md 一句未提 | 提示（最没把握是否该升阻断） |
| 8 | 耳塞式生物机器人（心跳同步、只彼此相连、不接「间隙」）无块交代 | `:231` “she opens her hand and shows me two earpieces.”；`:237` “It has synchronized to your own heartbeat.”；`:247` “they are only connected to each other, not to the Interstices.”；仅 `md:15` 叙事手法有「耳塞」一词 | **漏（机制层）**：后半章两人能顺畅对话全靠它，md 里是凭空听懂的 | 提示 |
| 9 | 「我过敏」＋「这是最好的说法」＋眨眼（教他说谎）全无 | `:262` ““I have allergies,” she says. “By the way, that’s a good explanation to give anyone…” She winks at me.”；`grep -c "过敏"`→0 | **漏**：给他一个可复用的掩护说法，后文要用 | 提示 |
| 10 | 母亲从叔叔手机发来的留言全无 | `:50` “There is a message from my mother: We are so happy that you have arrived safely! Work well, lovely boy, we are thinking of you.”；`grep -c "留言"`→0、`grep -c "平安"`→0 | **漏**：父母在本章唯一的「在场」 | 提示 |
| 11 | 「Crouch End——地势高」全无 | `:82` ““It’s high ground.””；`grep -c "高地"`→0 | **漏**：与 ch46「淹水的旅馆」构成水性/高地对照 | 提示 |
| 12 | 「叔叔从没见过这位老师」全无 | `:45` “I’ve never met her. But she is highly praised by everyone I consulted.” | **漏**：他把自己没验过的人交出去，是本章前提 | 提示 |
| 13 | 时间旅行者不能有永久植入（丢植入可能脑出血） | `:252-253` “As a time traveler, I can’t have any kind of permanent implant… losing it might cause a brain hemorrhage.”；`md:128` 词汇例句已收原句 | 词汇层已覆盖，块内无 | 跳过 |
| 14 | 脱鞋/条纹袜、房间、Canary Wharf、crumpet、猫名 Gwen、中音 C | `:101` `:115` `:66` `:49` `:348-352` `:327-338` | 未收 | 跳过 |
| 15 | `md:15`「成年的奥利弗回述十三岁那一天」 | 全篇现在时：`:23` “the second day I am in England my Uncle Stephen says”；`:28` “I say”；`:129` “I look at her, panicked.” 无成年叙述层 | **错（提示）**：「回述」把即时现在时改成追忆，且本章没有成年叙述者 | 提示 |
| 16 | `md:11`/`md:152`「老师拆开琴盖」 | `:177` “She raises the top of the piano and props it open.”——掀开并支起，不是拆开 | **错（提示）** | 提示 |
| 17 | `md:13`「还当面承认自己在撒谎」 | `:262` “She winks at me. **Is she trying to tell me that she is lying?**”——她只眨眼，由孩子猜 | **错（提示）**：把孩子的猜测写成她的承认 | 提示 |
| 18 | 真名汉字「青」 | 原文只有拉丁转写：`:23` “apply yourself, Qing”；`:130` “speak, Qing”；ch46 `:184` “Yang Qing” | **口径问题（提示）**：「青」是译名选择（亦可能是「清」）；ch46 `4-verdict.md` 已写「勿臆造汉字」，两章须统一 | 提示 |
| 19 | 「反制了叔叔留下的录音方块」 | `:271` “It’s a transmit/record cube. My cube is reforming it.”；`:284` “the cubes are both white and still.” | 概括成立 | 假红 |
| 20 | 块 7 的「和他爸妈身上的一样」属谁 | `:258` “just like my mom and dad’s. They both had theirs removed when they went underground.” | 比较对象＝他父母，不是她父母；md `:81` 正确 | 已核实为正确 |
| 21 | 块 8「有人告诉过他」的施事未点名 | `:279` “He was told not to bring such a thing here” | 原文未说是谁交代；md `:91`「被人交代过」保留了空位，正确 | 已核实为正确 |
| 22 | 词汇 14 条例句逐字 | 例：`:125` “But to make music, we have to be disorderly.”；`:127` “The voice I hear is almost simultaneous with her speaking”；`:136` “jiggling his knee and reading his phone” | 全命中，无改写 | 已核实为正确 |

## 已核实为正确（防下一轮误修）

1. **「叔叔」不是「舅舅」**：`:23` “my Uncle Stephen”。**勿改。**
2. **2041 年 11 月 1 日、他 13 岁**：`:18`。**勿与他 26 岁（2055）或 38 岁（ch45 的 1975）混。**
3. **老师全名 Madeline Baxter，与 ch45 里「那个教他六个月的人」是同一人**：`:96` “This is Mrs. Madeline Baxter, my teacher.”；ch45 `:74` “Madeline Baxter was her name.”。**勿当成两个人。**
4. **本章没有成年叙述者，是十三岁当场的第一人称现在时**：`:23` “…my Uncle Stephen says”；`:28` “I say”。**勿照 `md:15` 的「回述」去改写时态。**
5. **是真名「Qing」先出现、英文名「Oliver」后被叫**：`:23`（叔叔叫他 Qing）→ `:125`（老师叫 Oliver）→ `:129` 他「panic」。顺序勿倒。
6. **她掀开的是琴盖顶部并支起，不是拆琴**：`:177` “She raises the top of the piano and props it open.”。
7. **她弹的是莫扎特《妈妈请听我说主题十二变奏》，叔叔误认成《小星星》**：`:203` ““Was that ‘Twinkle, Twinkle, Little Star’?”；`:207` “That was a piece called Twelve Variations on ‘Ah, vous dirai-je, Maman’ by Mozart.”。**两首都对，勿删叔叔的误认**（误认本身是笑点，也说明他不懂音乐）。
8. **她没有口头承认撒谎，只眨眼**：`:262` “She winks at me. Is she trying to tell me that she is lying?”。**勿写成「她承认自己过敏是假的」。**
9. **录音方块是叔叔留下的、被她的方块「改写」（reforming）**：`:271`；`:284` 两只方块最后都是白色静止。**勿写成「她砸碎了方块」。**
10. **红叉纹身是「取掉植入」的标记，不是新纹的图案**：`:258` “there is a red X tattooed over it, just like my mom and dad’s. They both had theirs removed when they went underground.”。**勿写成「她纹了一个叉」。**
11. **递纸巾时她没进房间**：`:393` “I see through my tears her hand placing a small packet of tissues on the keys”。**勿写成「她走过来安慰他」。**
12. **结尾他只答「是，老师，我准备好了」**：`:402` ““Yes, Teacher, I’m ready.””——没有拥抱、没有表白。**勿加戏。**
