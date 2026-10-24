# ch34 Lost Love Last Laugh —— R5 判定表

- 机器层：`bash scripts/chapter.sh "…/ch34 lost love last laugh.md" --json` → **rc=0**，verdict=ok，blocks=6，segments=6，words=2360，issues 全零（struct/empty_quote/keyword/cjk/quote_long/template/keyword_long/hole/block_count = 0/9）
- 素读：`1-suread.json`（11 条）；对账：`3-diff.md`
- 报数：**逐字 6 块全绿 / 对应 6 块全绿 / 形态 ok（H1、5 条导航、4 个子项齐全）/ 断言 漏 3 提示 · 编 0 · 错 0 阻断 + 4 提示**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 本章 Isadora 以「胸前有白星的小黑猫」现身，md 通篇未交代 | `text/ch34_lost_love_last_laugh.txt:198` “We look down and there she is, a small black cat with a white star on her chest”；md `grep -c 猫` → 1（仅 `:65`「一整套猫的动作」），`grep -n 黑猫\|白星` → 无输出（exit=1） | 关键意象缺席：机械头在工作室熔化 `:157`、她在展厅以猫形活着，这层对照全靠读者自猜 | **提示** |
| Jasper 的现状线索（深夜回信、拼写退化、克莱尔从未见过他、五年旧照、贝克一年多没回底特律）全未收 | `:61` “he always replies late at night and his spelling has deteriorated like you would not believe”；`:66` “I’ve never met him … Those photos are five years old now. Beck hasn’t been to Detroit in more than a year.”；md `grep -c 底特律` → 0 | 本章是 Jasper 唯一「只凭转述」登场的机会，删净后后半的对手显得凭空出现 | **提示** |
| 「It is partitioned. I know it, but I can’t say it.」与「Who has been giving you commands besides me?」没有任何引语块承载 | `:267` “It is partitioned. I know it, but I can’t say it.”；`:271` “Who has been giving you commands besides me?”；`:275` “I am not permitted to say.”；md `grep -c 分区` → 1（仅 `:13` 导航），`grep -c 命令` → 0 | 全书主线（消息被分区、贝克之外另有下命令者）第一次正面揭露只在导航一句话里 | **提示** |
| 导航「伊莎多拉…还会反问贝克会不会因此不信她」 | 问句出自 Beck：`:279` “How can I trust you, then, Isadora?”；伊莎多拉只答 `:283` “I love you, Beck. I always serve you, no one else.” | 归属方向反了：怀疑者是贝克，不是伊莎多拉 | **提示** |
| 导航「反转『安全屋』：家、工作室、虚拟博物馆先后被侵入」 | `:174` “we carry them to the basement just to be sure … **They are.** … “Everything’s fine here,” she says”；虚拟博物馆是被分区 `:267`，非被侵入 | 家并未被侵入（三人白跑一趟正是原文的反差） | **提示** |
| md 两处以陈述句说「服务器被酸液毁掉」 | 原文只有问句 `:164` “Did someone pour acid on those servers?”；气味是 `:157` “a weird, sweet, acrid smell, like burnt plastic”；次日 `:314` “a faint tang of acid” | 推断合理但本章内未确认，宜标「疑似」 | **提示** |
| 块 3 中文「她打了报警电话」 | `:152` “…The locks have all been rekeyed. **I call 911**, and when the police arrive…”；叙述者为克莱尔（`:18` 起第一人称） | 指代不明：最近先行词是贝克，易读成贝克报警 | **提示** |
| 块 4 中文「正在熔化」是否过度 | `:158` “Isadora’s steampunk head rests on top of the pile, broken and melting.” | 逐字对应，不是过度 | 假红 |
| 块 5 中文「把胡须抹平到第五遍」 | `:238` “After she’s smoothed her whiskers for the fifth time” | 逐字对应 | 假红 |
| md 写「十二岁的阿尔芭」「二〇一三年十二月六日」「六个人」 | `:18` “Friday, December 6, 2013 (Clare is 42, Beck is 37, Alba is 12)”；`:318` “there are six of them” | 年龄/日期/数字全对 | 假红 |
| 块 6 中文「换一个街区，她会当成毒品交易」 | `:318` “In another neighborhood I’d assume this was a drug deal and pay them no mind” | 逐字对应（含自我安慰被否掉的结构） | 假红 |
| 「蒸汽朋克」这个词是否 md 自造 | `:158` “Isadora’s steampunk head”；词汇表例句亦逐字 | 原文词，非自造 | 假红 |
| 导航「两个日期分段：十二月六日克莱尔第一人称、十二月七日切成贝克」 | `:18` Friday, December 6, 2013（Clare 叙述）；`:304` Saturday, December 7, 2013（“I wake up” 后为 Beck 视角，`:318` “I notice a small group of men”） | 分段与人称切换描述准确 | 假红 |
| 词汇表 14 条例句真实性 | `/usr/bin/grep -cE "These lawyers are wolverines\|dumped, helter-skelter\|precocious teenager\|wide with apprehension\|Our unconsumed drinks\|leaves her drink untasted\|steampunk head rests\|eyes are smarting\|sightings of white trucks\|tippling gesture\|two gin and tonics and an orange juice\|until I turn the corner\|under her eyelids\|an apple tree laden with fruit" text/ch34_lost_love_last_laugh.txt` → **14**，exit=0 | 14/14 逐字命中 | 假红 |

## 已核实为正确（防下一轮误修）

1. `:18` “Friday, December 6, 2013 (Clare is 42, Beck is 37, Alba is 12)” —— md 的「十二岁的阿尔芭」「二〇一三年十二月六日」无一处错；本章 Alba 不是 11 也不是 13。
2. `:198` “a small black cat with a white star on her chest” —— 若下一轮把 L1 补进 md，**不要**写成「伊莎多拉变成黑猫」了事：她只是换了化身，身份仍是那个以贝克声音为底、被加进 users list 的系统（对照 ch33 `:151` 的密令）。
3. `:174` “They are.” + “Everything’s fine here,” she says. “I think.” —— **家没有被侵入**。任何把「家被侵入」写成原文事实的改法都是新增错误；原文的张力恰恰在「查过了，没事，可我还是不放心」。
4. `:164` “Did someone pour acid on those servers?” —— 这是**克莱尔的问句**，不是叙述者的结论；如果改 E3，请保留问句形态，不要改成「确认是酸」。
5. `:279`/`:283` —— 「How can I trust you」是**贝克**说的，伊莎多拉的回答是低头表忠。改 E1 时别把这句话再安回伊莎多拉嘴里。
6. `:318` “there are six of them … white men with beards, sunglasses … two of them tall and thin, one heavy” —— md 的「六个人」「戴墨镜」「两个高瘦、一个胖」全部逐字，不要因为「六个太多」而改动数字。
7. `:152` “I call 911” —— 报警人是克莱尔。块 3 只改指代，不要改成「贝克报了警」以外的第三种写法（如「有人报了警」会丢掉第一人称视角）。
8. 词汇表 14 条例句经 `grep -cE` 全模式核验为 **14**（每条都命中一次），不存在拼贴改写。

## 本批最没把握的一处

块 3「她打了报警电话」——中文的「她」既可读作贝克（最近先行词），也可读作克莱尔（本章叙述者、其他块里「她」多指克莱尔）。我按 R4 的「归属方向」判为**提示**而非阻断，理由是：读成克莱尔时与原文 `I call 911` 完全一致，属**可能正确但有歧义**，不构成「两边不一致」。若上级要求严格执行「主语不一致＝阻断」，这一条可升为阻断（改法唯一：改成「我打了报警电话」）。
