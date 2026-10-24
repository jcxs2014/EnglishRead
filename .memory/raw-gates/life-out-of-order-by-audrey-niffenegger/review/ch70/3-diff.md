# ch70 R3 对账（素读 8 条 vs md）

- 原文：`text/ch70_ever_after.txt`（188 行 / 1285 词），单段第一人称，署名 `Zach:` 只在 :23 出现一次
- 精读：`ch70 ever after.md`（4 块 / 92 行）
- 素读：`1-suread.json`（8 条，附字符区间）；机器：`2-machine.json`（rc=0，4 块，4 段全命中 39/31/44/67 词，pos 244/1860/3964/6240，nav 5，子项 4，H1 `70. Ever After`）

## 漏（素读有、md 无）

1. **「我没给你写结局」——全章最重要的那个决定不在块里、也不在导航里** —— 档：**阻断**（修在导航，不加第 5 块：本块数配额 `block_target` 上界＝4）
   - text/ch70:120 `“Can it be finished?” Alba asks me. “How do you know how it ends? Or did you invent endings for us?”`；text/ch70:125 `“Oliver told me his ending a few days ago, and mine is obvious. I didn’t write one for you.”`；text/ch70:134 `“If I don’t give you an ending, maybe you’ll live forever?”`；text/ch70:138 `“No. I don’t want to keep going without you.”`
   - md 侧：`结局` 全篇只 1 次（第 27 行，且只是「他自己把『我的结局』说成显而易见」，指扎克自己的结局）；`永远活` 0 次、`没有你` 0 次（`/usr/bin/grep -c` 均返回 `0`，退出码 **1**）。
   - 影响：章题 *Ever After* 的双关正落在这里——他写完了所有人的结局，唯独不写她的，因为「不写，也许她就能永远活着」；而她说「不，我不想没有你继续活」。这一问一答被跳过，第 14 行的人物弧线就只能收在「最后把书推给阿尔芭」，导航第 11 行的「说这是一封情书」也失去动机。修法：在**第 11 行**或**第 14 行**补一句「他唯独没给她写结局——「不写，也许你就能永远活着」；她说不愿没有他继续活」，**不要**为此新增第 5 块。

2. **Isadora 也帮过忙** —— 档：**提示**
   - text/ch70:111 末 `Even Isadora helped, though she kept offering to write the book for me. (I could do it in less than a minute! I don’t know why you want to struggle so much.)`
   - md 侧：`伊莎多拉`／`Isadora` 各 0 命中。这是全章唯一让 Isadora（ch69 里 Jasper 提到的那个「你的 Isadora」）出场的一句，也是 AI 与手写者对照的落点：她能一分钟写完，而他用四十多年。

3. **奥利弗道歉的具体内容** —— 档：**提示**
   - text/ch70:42 `“If I could do that over, I’d skip the part where I get covered in beer. And the part where I lie to you for years about Alba. I’m so sorry.”`；text/ch70:47 `“I don’t know if it had to happen that way, but it did. All is forgiven.”`
   - md 侧：第 14 行只写「奥利弗只出现一小段，道了歉，也被原谅」。被啤酒浇透是第一章那场派对的回照，多年隐瞒阿尔芭身世是全书主线；两句内容全丢，道歉就只剩一个动作（`啤酒`／`隐瞒` 各 0 命中）。

4. **失魂博物馆在断电的地下室里沉睡** —— 档：**提示**
   - text/ch70:53 `This house used to hum with conversation, music, Beck’s servers in the basement; now our only music is what Alba plays, and the servers are silent because the generator is broken. Perhaps the Museum of Lost Souls is still in there, a sleeping wonderland awaiting the kiss of electricity.`
   - md 侧：`失魂` 0 命中。这句是 ch69 那个虚拟来世的余响——它还在，只是没电。md 保留了「水毁」「烧掉的黄房子」（第 13 行），却把这一层收掉了。

5. **年龄与日期未落地** —— 档：**提示**（与 ch68/ch69 同一口径）
   - text/ch70:18 `Tuesday, June 23, 2082 (Zach is 81, Alba is 80, Oliver is 60)`
   - md 侧：只写「二〇八二年六月」（第 11 行），无 23 日、无 81/80/60。

## 编（md 有、原文无）

- **「书名里的 us」**（第 45 行：`书名里的 us 把所有名字收进同一个范围`）——原文从未给出书名，text/ch70:111 只说 `a book of us`（一本关于「我们」的书）。档：**提示**（属编类，但是修辞性指称、无事实后果；改「书里的 us」即可）。
- 其余无凭空新事：洗衣、晾床单、接龙、喂饭、苹果酱、雪夜舞会、两百一十二本笔记、唯一一份稿子、Alba 是唯一读者，均有原文对应。

## 错（两边都有但不一致）

- **无。** 主语、受事、归属方向、数字、时序逐项核过，未发现不一致：
  - 「奥利弗被拉回他自己的时间」是 Alba 上楼后三人握手时发生的（text:47），md 第 11/14 行顺序对；
  - 「他希望自己也能在那里」是扎克对奥利弗说（text:28），不是奥利弗对扎克说；
  - 「两百一十二本笔记」「四十多年」「两人搬进阿尔芭童年的家（原属她父母、后属 Clare 与 Beck）」均与 text:53/111 一致；
  - 「接龙用的牌是从 Beck 书桌里找到的」——md 第 12 行写「打牌」，未错标来源（原文 text:63 `a pack of cards Alba found in Beck’s desk`）。

## 其他（留档）

- 第 12 行「这一章没有一句哭喊」成立：原文最激动处是 text:102 `She panics. “But you’re not that sick, yet—”`，无哭。
- 第 13 行「两百多本笔记只有一份，读者只有一个」与 text:183 `It’s the only copy, but Alba is my only reader.` 逐字一致——这是本章最见功力的一处概括。
