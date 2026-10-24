# ch04 The Balcony — R3 对账（素读 ↔ md）

素读件：`review/ch04/1-suread.json`（8 条，锚点 `/tmp/t3_validate.py` 复核异常 0）
被查件：`notes/books/short-story-anthologies/a-labyrinth-of-honeybees-by-fawcett-heather/ch04 the balcony.md`
原文：`text/ch04_the_balcony.txt`（ch04:NN = 段落号）

## 一、编（md 有、原文无）

无。全部事实断言可回原文。一处**推断被写成事实**，列于「错」。

## 二、漏（素读有、md 无）

| 编号 | 素读事实 | 原文 | md 侧 | 档位 |
|---|---|---|---|---|
| 漏-1 | 他下令：明天带他们去神庙 | ch04:12 `“Tomorrow you will escort us to the temple,” he said.` | 未记（正章的转折令） | 提示 |
| 漏-2 | 神为何需要人：「诸神皆浅薄，他们不朽、固定于时间、永不改变，所以他们需要我们」 | ch04:27 `“All the gods are shallow. They’re immortal, fixed in time. Unchanging. It’s why they need us.”` | 未记 | 提示 |
| 漏-3 | 她追问第三名士兵的下落，他拒绝回答 | ch04:9 `I asked him what had happened to the third soldier that night ... He wouldn’t tell me.` | 未记（正是"两人死"数目何以含糊的原因） | 提示 |
| 漏-4 | 飞马掀翻骑手时踩塌了祭司的帐篷 | ch04:5 `They charged back into the meadow, trampling the priest’s tent as they went.` | 未记 | 提示（低） |

## 三、错（主语／因果／数字／时序／措辞）

### 错-1（提示·低）md:10「他拿出从玫瑰丛上扯下的公主围巾」
- md 侧：`ch04 the balcony.md:10`（导航）
- 原文侧：ch04:11 `This one was torn from where he must have pulled it off a rosebush` —— `must have` 是**她的推断**，不是确证。
- 判定：情态被抹平（md 自己的块 2 中文理解保留了"想必是他拉下来的"） → 提示（低）。

## 四、数字与专名核对

| 项 | md | 原文 | 结论 |
|---|---|---|---|
| 死亡人数 | 两个人先后死去 | ch04:8 `There were only three of them now—the royal inquisitor and two servants`（原四骑）＋ ch04:15–16 虫蜇致死 ＋ ch04:20 `whatever had killed two of his men` | ✅ |
| 逃走者 | 最后一个仆人带着飞马逃走 | ch04:16 `the inquisitor’s remaining servant ... he and his pegasus were gone` | ✅ |
| 围巾纹样 | 绣国王纹章、纯金线缝边 | ch04:11 `bore the symbol of the king, stitched along the hem with threads of pure gold` | ✅ |
| 赌局 | 几天能进神庙 | ch04:28–31 她说"再一个月"，老女祭司说 `“Three days.”` | ✅ |
| 谁杀了老女祭司 | 她（叙述者） | ch04:19 `In the first few years after I killed her` | ✅ |

## 五、已核实为正确（看似可疑、回原文成立）

- md:10「云只在她独自一人时散开」→ ch04:3 `the clouds rolled in and hid the maze below ... The clouds blew away once I was alone.` ✅
- md:10「骑马闯迷宫被飞马掀翻」→ ch04:5 `they went into a frenzy, rearing until they threw their riders` ✅
- md:10「两个人先后死在迷宫里」→ ch04:8（人数只剩三）＋ ch04:15–16（虫蜇致死）＋ ch04:20（`killed two of his men`）✅
- md:12「审问官开始把她当作凶手」→ ch04:13 `no doubt he was now`（认定她以血腥仪式杀了继承人）✅
- md:12「她的秘密第一次交底：她杀过那位老女祭司」→ ch04:19 ✅
- md:13「石上的闲聊与迷宫里男人的挣扎交替」→ ch04:19–33（石上）与 ch04:20（他张弓穿行）✅
- md:23「神是有偏好的，而偏好可以被观察、被下注」→ ch04:25 `The Goddess likes beauty` ＋ ch04:29 `Are we placing bets?` ✅
- 块 3「鬼的规矩（被杀者跟着凶手）前面已经立好」→ ch02:16 `ghosts follow their murderers` ✅
- 词表 10 条例句全部逐字出自本章（chapter.sh 机器层复核一致）✅
