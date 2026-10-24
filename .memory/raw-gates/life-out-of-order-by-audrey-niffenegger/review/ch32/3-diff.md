# ch32 richard — 对账单（R3）

- 原文：`text/ch32_richard.txt`（367 行，五段：2012-12-06 Alba 11 → Alba 35 → Alba 11 → Clare → 1982-12-03 Henry）
- 精读：`ch32 richard.md`（131 行）
- 机器层：`2-machine.json`，rc=0，verdict=ok，块数 8，段数 8，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，words 2941

## 〇、亲属链核对（本章要点，逐条回原文）

| 关系 | 原文证据 | md 写法 | 判 |
|---|---|---|---|
| Richard ＝ Henry 之父 ＝ Alba 的祖父 | `:23` “I’m staying over at Grandpa’s apartment… I am lying in my dad’s bed in his old room.”；`:367` “I think about my father, climbing that tree” | 「祖父公寓」「我爸爸的旧房间」「商量亨利那间屋」 | 一致 |
| Annette ＝ Richard 的亡妻 ＝ Henry 之母 ＝ Alba 的祖母 | `:52` “He could never bear to give away any of my grandmother’s clothing.”；`:79` ““Darling. Annette.” He’s mistaken me for my grandmother.”；`:268` “Annette is buried in Graceland Cemetery under a double-wide granite stone with Richard’s name already carved next to hers.” | 「穿祖母的旧衣」「他把她认成 Annette」「兑现『被错认成亡妻』」 | 一致（祖母＝亡妻同一人，未拆成两人） |
| Clare ＝ Richard 的儿媳 | `:23` “Mama has gone to Michigan…”；`:264` “Richard and I had an affectionate but formal relationship.” | 只作为「克莱尔」出现，未给称谓 | 未写错，也未明写 |
| Kimy ＝ 房东兼老友，**非亲属** | `:128` “Kimy lives downstairs; she is Grandpa’s landlady.”；`:218` “I’m eighteen years older than Richard” | 「房东金米」「Kimy … landlady」 | 一致（未写成继祖母／亲戚） |
| Alba 与 Henry | `:23` “my dad’s bed”；`:283` “Not as bad as Daddy.” | 「爸爸」「亨利带小阿尔芭」 | 一致 |

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | 克莱尔当时在密歇根看自己的父亲（Alba 的「另一个祖父」）——这是 Alba 独自在祖父家过夜、以及天亮「赶回」的前因 | `text/ch32_richard.txt:23` “Mama has gone to Michigan to see my other grandpa.” | 导航只写「天亮后克莱尔与金米吃松饼」（`ch32 richard.md:11`）；块 6 只写「她坐在理查德的桌前」，未交代她从哪来 | 提示（因果前置条件缺失，但不影响事件链成立） |
| L2 | Kimy 比 Richard 大十八岁、原以为自己会先走；Richard 在这栋房子里住了五十年 | `:218` “I’m eighteen years older than Richard, no way he would go first.”；`:242` “He was here fifty years.” | 导航、块、总结均未收 | 提示（本章唯一的黑色幽默，未进块属取舍） |
| L3 | 1982 段的情感支点：Alba 问「你相信天堂吗」，Henry 正犹豫要不要承认自己觉得死后什么都没有，她就消失了 | `:362` ““Do you believe in Heaven?” Alba asks me.”；`:367` “But I’m spared having to answer…” | 一句话总结写「听她说祖父死了；她在他眼前消失」（`:131`），问答未收 | 提示（消失前最后一问，属关键一拍但已在总结中保留「消失」） |
| L4 | Henry 那句自嘲式交代：「在我的现在，你才三岁」 | `:313` “In my present, you’re only three.” | 块 7 未收 | 跳过（时间坐标细节） |

## 二、编（md 有、原文无）

无。逐块核过「中文理解」「为什么这样写」「读者视角提示」：所增细节均有原文落点——「整柜衣裙、外套、衬衫」对应 `:52`；“Two enormous blueberry muffins” 对应 `:153`；“His face looks lopsided” 对应 `:110`。

## 三、错（两边都有但不一致）

| # | 断言位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | `ch32 richard.md:14` 人物弧线、`:21` 块 1 中文理解（两处「弹起」）、`:131` 一句话总结 | 「祖父从**弹琴**的人变成被摆正的人」/「他**弹**起《Goodnight, Ladies》」「他又**弹**起别的」/「**弹**《Goodnight, Ladies》催她睡」 | 同夜同一段音乐：`:42` “Music; a violin; Brahms; my grandfather is playing.”；`:57` “holding his violin and bow at his sides”；`:110` “His violin is next to him, with the bow beside it.”。`/usr/bin/grep -nE "piano\|violin\|bow" text/ch32_richard.txt` 五条命中全是 violin/bow，**全文无 piano**（exit=0） | 提示（乐器写错：应为「拉／奏」提琴。本章提琴是核心道具——他死时琴就搁在身边——4 处「弹」宜统一改「拉」） |
| E2 | `ch32 richard.md:61` 块 5 中文理解 | 「祖父**端坐**在沙发上，头歪成一个不自然的角度」 | `:110` “Grandpa is sitting on the sofa. His head is at a weird angle…” | 提示（「端坐」是端正挺直地坐，与「头歪成不自然角度、手摊在膝上掌心朝上」相抵；原文只是 sitting） |
| E3 | `ch32 richard.md:57` 块 4 读者视角提示 | 「……读者读得出不对，**她还没说出那个词**。「uselessly」是这屋里头第一个明确的坏消息，**虽然她还没说出那个词**。」 | 原文该段只发生一次「尚未说破」这件事（`:70-75`，直到 `:75` 才说 “You’re having a stroke”） | 提示（同一段内同一句意重复两次，属编辑残留；建议删后一处） |
| E4 | `ch32 richard.md:11` 一句话概括 | 「孩子醒来发现他歪在沙发上，**叫来房东与急救**」 | `:115-128` 她先给妈妈打五次电话，妈妈让她下楼找 Kimy，Kimy 用她的电话打 911 | 跳过（压缩转述，未颠倒主体；总结 `:131` 已写「打电话叫回妈妈、叫来房东金米」） |
| E5 | `ch32 richard.md:14` 人物弧线 | 「祖父从弹琴的人变成**被摆正的人**」 | `:87` “I help him to lean back, prop him with cushions” | 已核实（「被垫起」的转写，非误读） |

## 四、归属方向复核（R4 三问）

- 块 4「他把她的手攥得很紧」⇄ `:70` “he clasps my hand tightly” —— 施事是祖父、受事是 35 岁的 Alba，未写反。
- 块 4「他另一只手摊在膝上」⇄ `:70` “His left hand lies uselessly in his lap” —— 方向正确（废掉的是左手；能攥人的是右手）。
- 块 8「他想到父亲——那个爬上树的人」⇄ `:367` “I think about my father, climbing that tree” —— 爬树者是**父亲**（Richard），五岁的爬窗者是 Henry 本人（`:313`），md 未把两人对调。
- 一句话总结「他把她认成 Annette」⇄ `:79` “He’s mistaken me for my grandmother” —— 施事祖父、受事 35 岁的 Alba，被认成的是祖母 Annette，方向正确。
- 块 6「她坐在理查德的桌前，金米煮了咖啡」⇄ `:153` “I sit at Richard’s table, and Kimy makes coffee” —— 煮咖啡的是 Kimy，落座的是 Clare，未对调。
