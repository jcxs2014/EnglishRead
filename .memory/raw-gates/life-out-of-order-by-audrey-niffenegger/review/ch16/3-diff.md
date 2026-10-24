# ch16 The Empty Bottle · R3 对账

- 素读：`1-suread.json`（10 条 + 转折点补条，写定于打开 md 之前；**全章 Zach 第一人称**，声部标记 `Zach:`）
- 机器层：`2-machine.json`，rc=0，8 块 / 8 引语 / segment_miss=0 / 查无 0 / 空引号 0 / 字数 1911
- md：`ch16 the empty bottle.md`（131 行）

## 一、漏（素读有、md 无）

### L1（提示）Oliver 的三处「时代错位」全部不在 md 里

```
text/ch16_the_empty_bottle.txt:129  “I thought they were meant to be confined to garages until they were ready to perform in public?”
text/ch16_the_empty_bottle.txt:137  Oliver darts his eyes at the cars. “Was there a football match?” he asks.
text/ch16_the_empty_bottle.txt:142  “No, the Puerto Rican Day parade is this weekend. You don’t live in Chicago?”
```

md 侧：导航 5 项、正文 8 块、一句话总结均未出现「车库」「波多黎各」「足球」任一条。
取证：`/usr/bin/grep -cE "车库|garage" "ch16 the empty bottle.md"` → `0`，**rc=1**；`/usr/bin/grep -cE "波多黎各|Puerto" …` → `0`，**rc=1**；`/usr/bin/grep -cE "足球" …` → `0`，**rc=1**。

判定：这三处正是「读者比 Zach 多知道一层」的全部证据——把 garage band 按字面理解、把游行旗帜当成足球赛，都是他不属于 2034 年的破口。全丢之后，本章只剩「神秘客」的模糊感（Tropes 那条仍写着「住伦敦、妻子住这里」，靠台词撑）。属暗线而非转折 ⇒ **提示**（强烈建议至少折一句进原句 6 的读者视角）。

### L2（提示）物证细节全缺：祖父的 Ronson 打火机、亮黄 Weejuns 无袜

```
text/ch16_the_empty_bottle.txt:133  I notice that he’s wearing bright yellow Weejuns without socks.
text/ch16_the_empty_bottle.txt:162  I have an old Ronson lighter that used to belong to my grandfather. When I hand it to him he looks surprised to see it, but he knows how to use it.
```

md 侧：无。取证：`/usr/bin/grep -cE "Weejun|乐福鞋" "ch16 the empty bottle.md"` → `0`，**rc=1**；`/usr/bin/grep -cE "Ronson|打火机" …` → `0`，**rc=1**。

判定：打火机那一下「他见到它显得意外，却会用」是本章唯一一处让读者心里一动的物证（Oliver 在后来的时间里见过它），漏掉不影响主线 ⇒ **提示**。

## 二、编（md 有、原文无）

未发现实体级添加。核过的可查项：

| md 写法 | 原文 | 结论 |
|---|---|---|
| 「2034 年 6 月 9 日（Zach 33、Oliver 27）」 | `text/ch16:18` `Friday, June 9, 2034 (Zach is 33, Oliver is 27)` | 对 |
| 「灰西装、白衬衫、浅蓝领带」 | `:38` `a gray suit, white shirt and a light blue tie` | 对 |
| 「IPA」 | `:34` `She pulls an IPA for me` | 对 |
| 「替 Gomez 做社交媒体」 | `:29` `doing social media for Gomez` | 对 |
| 「刚满二十一岁的人」 | `:29` `mostly the barely twenty-ones in the clubs` | 对 |
| 「九点半」 | `:29` `It’s only nine thirty.` | 对 |
| 「二零一六年…David Bowie」 | `:245` `“Twenty sixteen,” she says. “Consoling Isadora about David Bowie dying.”` | 对 |
| 「他可能是间谍或外交官」 | `:184` `He could be a spy, or a diplomat` | 对 |

## 三、错（两边都有但不一致）

### E1（提示）md 第 15 行：观察顺序写成「先衣着、再口音、再国籍」

```
md:15  Zach 的观察顺序是先衣着、再口音、再国籍、最后才问名字——身份被一件件拆开摆出
text/ch16:38  He’s immaculately dressed… he’s wearing a gray suit, white shirt and a light blue tie.
text/ch16:43  Then I realize that he’s Chinese and he hasn’t said a word yet; maybe he doesn’t speak English?
text/ch16:50  “Oh, please don’t! That’s quite unnecessary,” he says with a very elegant English accent.
```

原文次序是 **衣着（:38）→ 国籍（:43）→ 口音（:50）→ 名字（:91）**；md 把国籍与口音对调了。

判定：属分析层的顺序误记，不影响任何内容理解（真正的「先说国籍、后听口音」恰恰是本章的误会来源：他先疑心对方不懂英语，才被那口英国腔打脸）⇒ **提示**（建议改为「先衣着、再国籍、再口音」）。

## 四、R4 逐块对应（8 块）

| 块 | 引语（首句） | 这段中文是不是在讲这句引语 | 三问（主语 / 受事 / 归属） |
|---|---|---|---|
| 1 | `Zach: Alba’s been time traveling more often…` | 是。三次调温、`when` 把松口气与找不到人钉在一起、`cool to my touch` 落在触感 | 主语：Alba（走）、Zach（找、摸）；受事：T 恤；归属：`Zach:` 声部标记保留，md 未误标成 Alba 说话 |
| 2 | `The house is too quiet when she’s gone…` | 是。`productive, but lonely` 的并列义、`finally`/`just` 的降调都讲了 | 主语：Zach；受事：房子、写作；归属：`just to be with other humans` 的「别的人」= 陌生人，未误读成朋友 |
| 3 | `I’ve become a homebody without meaning to…` | 是。without meaning to 的被动性、括号里 like now 的时效、递进三项都贴着引语 | 主语：Zach；受事：工作、书、Alba；归属：`all my books are there` 的 there=家里（md 第 41 行「书都在家里」正确） |
| 4 | `I turn away from the bar and I notice the guy too late…` | 是。冒号后的三连动作、too late 的「先宣判」、untasted | 主语：Zach（撞）；受事：那人、啤酒；归属：`my untasted beer` 是**他的**酒，md 第 51 行「一口没喝的啤酒全泼在了对方身上」方向正确 |
| 5 | `He’s immaculately dressed…` | 是。先欣赏后糟蹋、dive bar 与 gray suit 的反差 | 主语：他（穿）、啤酒（流）；受事：西装、脸、前襟；归属：身高归他、坐下状态解释酒为何落脸上——md 第 61 行未弄反因果 |
| 6 | `He could be a spy, or a diplomat…` | 是。三段退步（推论→观察→疑问）、embargo 不解释、Ukrainian Village 定位 | 主语：Zach（推、看、疑）；受事：Oliver；归属：`if he was traveling internationally during the embargo` 是**条件**，md 第 71 行「如果他在禁令期间还在国际上走动」保留了条件语气 |
| 7 | `Oliver says, “My wife and I both have medical issues…”` | 是。病历式措辞、第二个 but 留住「想」、even before 把「我们」推成「他一直」 | 主语：Oliver 与妻子（有病）、他（被告诉）；受事：孩子；归属：`My parents` 答的是「谁说的」= 他父母，md 第 81 行未错记成医生 |
| 8 | `Her presence suddenly seems like a gift…` | 是。happy 连用两次的急、all right 的平、suddenly 由对比激出 | 主语：她（在）、他（高兴）；受事：他的世界；归属：`as long as Alba is with me` 的条件句性质被 md 第 97 行点明（「他的世界之所以没问题，是因为条件句还成立」），方向正确 |

R4 结论：8 块全部对应；无引语选短、无讲主旨、无只复述字面。密度上 1911 字 / 8 块，落在 `block_target [3,6]` 之外偏少，缺口正好是 L1/L2 那两处场景。

## 附：一句话总结（md:131）核对

- 「Zach 想躲开一间太安静的房子」✓ `text/ch16:29`
- 「撞上了一个穿得体面、说自己是偷来这身衣服的陌生人」✓ `:38`、`:83`
- 「两人隔着很差的乐队抽烟」✓ `:95`、`:133`、`:137`
- 「他想要孩子而不能，对方也因为身体的原因不能」✓ `:203`、`:212`
- 「故事在讲述中变平」✓ `:274` `I can feel the story going flat in the telling`
- 「只要她在，我的世界就没问题」✓ `:280`
- 末句「读者刚刚陪他认识的那个男人，恰好也说过一句几乎一样的话」——指两条「想要孩子而不能」的平行，非指末句原文；md 措辞是评论不是复述，不构成编造。
