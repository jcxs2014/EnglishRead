# ch31 4-verdict

- 文件：`ch31 from the start.md`（160 行）
- 结论：**3 阻断 / 5 提示**

## 阻断

### B1 一句话总结编出本章不存在的物象：“一杯没喝的酒”
- 位置：`ch31 from the start.md:160`（一句话总结）
- 现状：「她……用**一杯没喝的酒**、一辆没上的车和一条泥路，把自己重新关了起来。」
- 问题：本章 Tamsin 全程没有点过、端过、放下过任何饮品；她在这章只吃（ch30 的 bridies）、听、走。原文里 wine / beer 全部出现在 **Rowan 自述的往事**里，与她无关。取证：
  - `/usr/bin/grep -n -i -E "my (pint|drink|glass)|took a (sip|drink)|untouched|half-finished" text/ch31_chapter_31.txt` → **无输出，`echo $?` = 1**
  - `/usr/bin/grep -n -i -E "drink|wine|beer|glass of" text/ch31_chapter_31.txt` → 仅 `71 / 77 / 89 / 104 / 110`，`rc=0`；逐行核对，`71`「couples and wine glasses」、`77`「I threw the bottle at the wall. Red wine and glass everywhere.」、`89`「I’d been drinking」、`104 / 110`「beer bottle」「glassed a guy」——**全是 Rowan 的过去**。
- 建议改后：「她……用一辆没上的车、一句“I like walking”和一条泥路，把自己重新关了起来。」（若想保留三样，第三样可用“那把被她拉到身边的铲子”，`text/ch31_chapter_31.txt:20`。）

### B2 全章第二半的关键转折整段缺失：她为什么翻脸被写成“只是受不了怜悯”
- 位置：`ch31 from the start.md:12`（导航·一句话概括）、`:18`（人物弧线）
- 现状：导航写到「讲完他转头对她说“我希望那时候有人跟我谈谈”；她听懂那是怜悯，于是翻脸、辩解、落荒而走」就收束；精读 7 组原句从「It was pity」（`:143`）直接跳到「I like walking」（`:272`），**`:173–:263` 无任何落点**。
- 问题：原文第二半的引擎是 Rowan 挑明动机——他之所以讲这一整段，是因为**她自己在酒吧跟他讲过旧公司的事**；而她根本不记得（以为又是自己醉后失态），于是从“被怜悯”升级为“被揭底”，否认、指控他 gaslighting，最后逃走。缺这一层，md 把她的反应降格为“讨厌被可怜”，因果被改写；下一章开头「Oh God, he knows. He knows what happened at the office!」也失去来处。原文证据：
  - `text/ch31_chapter_31.txt:173`「“After what you told me in the pub, I thought you could do with hearing from someone who’s been there—”」
  - `:176`「My whole body went cold. I knew I’d done something that night.」
  - `:185`「“About what happened at your old workplace.”」
  - `:209`「This was gaslighting! Or something like it.」
- 建议改后：导航补一句——「讲完他才挑明：**是她自己在酒吧跟他讲过旧公司的事**，他才想用自己的经历接住她；她根本不记得自己说过什么，只当他在揭她的底、在 gaslight 她，于是翻脸、否认、落荒而走。」

### B3 词汇表 4 处行破损（`|` 行被对白/重复行截断）
- 位置：`ch31 from the start.md:100-103`（bristling）、`:115-118`（stifled）、`:136-145`（mud）、`:146-155`（wind）
- 现状：每处都是“表格行 → 空行 → 游离例句行（或对白行） → 再一行以 ` |` 收尾”，表格被切成碎片：
  - `:100` 的 bristling 行后，`:103` 又重复一遍「“That must have felt good,” I said, envy bristling my skin. |」
  - `:115` 的 stifled 行后，`:118` 重复「I stifled a laugh at the image. |」
  - `:136` 的 mud 行后接 `“It’s a long walk.”`／`“I like walking.”`／叙述句，最后 `:145` 才以「…mud road. |」收尾
  - `:146` 的 wind 行后接 `“I’m sorry.”`／`“Good.”`，`:155` 以「The wind whipped around us. |」收尾
- 问题：承 `2026-10-22-复核与修复指令.md` §1-D，「`|`-行不以 `|` 结尾」为阻断类；这四处的表格在渲染时会散架，且重复例句会被当成第二个词条。
- 建议改后：每处只留一行完整表格行，删去空行与游离/重复行。mud 的例句取「He said something else, but I didn’t hear him as I marched back down the mud road.」（`text/ch31_chapter_31.txt:275`），wind 取「The wind whipped around us.」（`text/ch31_chapter_31.txt:257`，全章唯一）。

## 提示

1. `:24`｜原句 1 把**两段**并成一条引语：`text/ch31_chapter_31.txt:8` 是他的台词，`:11` 是她的内心（原文两段之间空行）。中文理解已分开，但引语框里读起来像同一段话。建议拆成两条，或中间用 `／` 标明换段。
2. `:84`｜原句 7 同型跨段：`text/ch31_chapter_31.txt:272`「“I like walking.”」＋`:275`「He said something else…」。
3. `:26`｜「至少你没被跟我一起困在卡车里」语序不顺，建议「至少你没跟我一起被困在卡车里」。
4. `:20`（并 `:16`）｜「她一边听，一边把铲子拉近」时点偏移：`text/ch31_chapter_31.txt:20`「I pulled the spade laid on the grass closer to me, gripping it for support.」发生在他**开讲之前**（她刚问完“Was it for the driving thing?”）。建议「还没开讲，她就把铲子拉到身边」。
5. 压缩掉的三处（提示级，可补）：① `:53` 十六岁把哥哥摔过肩、父母说“served him right”——这是“愤怒＝正义”的前因，导航只留“哥哥的锁头、父母的笑”；② `:77` 晚宴砸酒瓶（第二个施害实例）；③ `:122`「he hadn’t even been laughing at me」——受害者其实没笑他，这一句让“施害无端”成立，md 未落。

## R4 三问

1. **谁做的**：砸人的是 **Rowan**，不是 Tamsin——`text/ch31_chapter_31.txt:104`「I got up and picked up the beer bottle… swung it at the back of this guy’s head.」；此前童年被哥哥 headlock／坐压（`:47`）、十六岁把哥哥摔过肩（`:53`）、晚宴砸酒瓶（`:77`）也都是他。Tamsin 在本章**只有听与走**：拉铲子（`:20`）、摸口袋里的针（`:119`）、拒绝搭车（`:272`）。
2. **什么关系／谁欠谁**：Rowan 与伤者是**施害–受害**，他认罪、服刑，出狱后仍追踪伤者状况并自认「completely my fault」（`:122`）——他欠的是无法偿还的债。Rowan 对 Tamsin 不是加害者，而是**误判了亲近程度的善意干预者**：他以为她已在酒吧托付过旧公司的事（`:173`），因此“欠”她一次对等的坦白；Tamsin 欠他一次说明（她确实说过，只是不记得，`:176`），但她把这份亏欠转成“你在 gaslight 我”（`:209`）。本章**无复制体线**，1a/1b 的关系不参与。
3. **数字与死因**：三个孩子、他最小（`:47`）；十六岁（`:53`）；「a good foot」比哥哥高（`:53`）；**判四年、服刑两年**（`:122`「I was given four years, but I got out in two…」）；伤者**没死**（`:122`「He didn’t die, thank Christ.」），脑肿胀→永久记忆损伤＋情绪调节问题（同句）。本章**无人死亡**；md 导航「两年牢」与原文一致，未编数字。

## 已核实为正确（下一轮不要改坏）

- 原句 2–6 逐字命中 `text/ch31_chapter_31.txt:59 / 110 / 110 / 242 / 143`（原句 3、4 同段相接，不是拼贴）。
- 「leant into it」译“顺着它去了”准确（`:59`）。
- `:62`「缝皮针」有据：`text/ch17_chapter_17.txt:89`「A thick, curved needle.」、`:92`「It could probably be used to sew leather.」——不要改成“织针/缝衣针”。
- `:92`「下一章她还要走回来」正确：`text/ch32_chapter_32.txt:5` 她正「back down through the dark corridor of pine trees」。
- 导航「哥哥的锁头、父母的笑」对应 `:47`；「两年牢」对应 `:122` 的 got out in two。
- 叙事手法四动作均可核：攥铲子 `:20`、切空气 `:101` 一带、看疤 `:113`、屏幕上的手指 `:149`。
- 人物弧线「用否认把自己封回去」与结尾「I like walking」＋走掉（`:272`/`:275`）一致。
