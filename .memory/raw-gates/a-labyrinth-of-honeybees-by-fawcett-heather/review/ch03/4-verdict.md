# ch03 The Campfire — R5 判定表

路径：R1（子代理，仅读 text/ch03）→ `/tmp/t3_validate.py` 锚点复核 → R2 `chapter.sh --json` → R3（`3-diff.md`）→ R4 → 本表。
md：`notes/books/short-story-anthologies/a-labyrinth-of-honeybees-by-fawcett-heather/ch03 the campfire.md`

## 一、四组报数

| 组 | 数 | 结果 |
|---|---|---|
| 逐字 | 引语块 6 / 分段 6 / 查无 0 | ✅ |
| 对应 | 导航 4 + 总结 1 + 6 块 ×5 = 35 项 | 32 项成立，3 项技法/措辞不准（错-1～错-3） |
| 形态 | H1 `03. The Campfire` ✅ / 导航 4 项 ✅ / 块数 6（契约 1,600–2,400 词给 4–6）✅ / 引语 >100 词 0 ✅ | ✅；chapter.sh 曾 ⚠️「块数 6 偏离其启发式 3–5」，属契约与启发式不一致，保留 6 |
| 断言 | R3 三单：编 0、漏 4、错 3 | 阻断 0 / 提示 7 |

R2（`review/ch03/2-machine.json`，rc=0）：`verdict: ok`，`quotes 6 / blocks 6`，`segment_miss 0`，`struct_bad 0`，`empty_quote 0`，`keyword_bad 0`，`cjk_low 0`，`template 0`，`hole 0`，`words 1694`。

## 二、R4 逐块核对

| 块 | 引语出处 | ①主语 | ②受事 | ③谁的/谁欠谁 | 结论 |
|---|---|---|---|---|---|
| 原句 1 | ch03:4 | **Harper** 曾与国王作战→被俘→被割舌 | 受事＝Harper 本人 | 割舌的是国王的士兵；叙述者在评价 | ✅ |
| 原句 2 | ch03:10 | **审问官**打出荆棘、决定回头 | 他的来路被换掉 | 迷宫（女神）在引他 | ✅ |
| 原句 3 | ch03:28 | **审问官**自述：街头孤儿、神庙收留 | 他自己 | 家＝那些神庙（his） | ✅ |
| 原句 4 | ch03:31 | **她**先让步再否定 kind | 众神（受评者） | 那些鬼属于审问官 | ✅ |
| 原句 5 | ch03:47 | **她**承认不虔诚、并怨神 | 她自己 | 怨的对象＝女神（Her） | ✅ |
| 原句 6 | ch03:51 | **她**放罐子、说药性 | 受事＝审问官（未接） | 蜂蜜来自她的花园 | ✅ |

无施事反转；块 3「他用的词是 street rat——一个把自己说得比实际更低的词」与原文自述人称一致。

## 三、判定

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| md:13「三个人各讲一次'家'」 | ch03:28 仅审问官交代；哈珀无台词（ch03:4）；祭司谈神意（ch03:36） | 技法描述不成立 | 提示 |
| md:128「一个说家是这片园子」 | 该说法在 ch02:61，ch03 内未复述 | 跨章归因 | 提示 |
| md:41「white roses 与 hand trees 都是编出来的景观」 | ch03:10；白玫瑰为现实花卉 | 措辞易误读 | 提示（低） |
| 漏：炖苹果、走中间路、拔匕首、案子主线（ch03:2/5/8-9/16-17） | 同上 | 覆盖取舍，未失实 | 提示 |

**本章阻断 0 条。**

## 四、已核实为正确

| 断言 | 证据 | 结论 |
|---|---|---|
| 哈珀十年前与新国王作战、被俘割舌以取乐（md:17） | ch03:4 `He’d fought against the new king a decade ago ... cut out his tongue for no reason other than sport` | ✅ |
| 「比起对他们别人做的，这还算仁慈」（md:19） | ch03:4 `which was a kindness compared to what they had done to others` | ✅ |
| 审问官原是街头孤儿（md:45） | ch03:28 `I was a street rat` | ✅ |
| 「住过五六座神庙」→ md 未写数字，无冲突 | ch03:28 `a half dozen temples` | ✅ |
| 她「只在被要求时才虔诚」（md:73） | ch03:47 `I was devout only when it was required of me` | ✅ |
| 药＝蜂蜜兑猫尾草乳汁、止痛+促愈（md:89） | ch03:51 `honey mixed with catrush milk. It will dull the pain and help the skin knit.` | ✅ |
| 「钻进帐篷、不看他怎么用」（md:128） | ch03:52 `I ducked back into the tent and yanked the flap shut` | ✅ |
| 「蜂蜜是女神的符号」（md:93） | ch03:6 迷宫蜂群＋书名 honeybees；原文无"符号"字样，属诠释 | ✅ 可推断 |

## 五、同会话自检已知盲区

- 非异会话独立复核；「哪些段落未选」的判断属编辑取舍，本表只报不判红。
- 块数为 6 而 chapter.sh 启发式给 3–5，两者冲突已记录；按 `bookform --contract` 的 4–6 保留。
