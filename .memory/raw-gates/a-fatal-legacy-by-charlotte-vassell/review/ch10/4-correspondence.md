# 4-correspondence.md · ch10 逐块对应（人判）

> 判据：**这段中文是不是在讲这句引语？**（R4）
> 三问：① 每个动词的主语是谁 ② 受事/宾语是谁 ③ 「谁的 / 谁欠谁 / 谁问的」回原文看 `by` / `to` / `from` / `of` 定方向。
> 六块全部通过 `scripts/chapter.sh`（退出码 0，8 个引语片段全部逐字命中）——**逐字层已由机器覆盖，本表只答「对应」这一问**。

| 块 | 引语（原文逐字） | 中文在讲这句引语吗？ | 施事 / 受事 / 归属三问 | 密度 | 结论 |
|---|---|---|---|---|---|
| 原句 1 | `Callie came home to the most delicious smell. She walked into the kitchen area to find Caius frying Korean veggie pancakes. He'd seen a video of someone doing it the other day and wanted to try it.`（`text/ch10:20`，[46,242]） | **是**。中文理解写的是「进门闻到香味 → 走进厨房区 → 看见他在煎饼 → 他看过视频想试」，逐句一一对上，没有跳出引语讲上下文，也没有拉全书主旨或作者生平。 | ① 主语：Callie（进门、走进厨房区）；② 受事：Caius 在煎的煎饼；③ 归属：「他前几天看过视频」= **Caius**（原文主语 He's），md 写「他」承接上句的 Caius ✓ | 有「为什么」：气味先行＝等她回来的信号；「凭视频上手」＝生涩。**但「不会做饭」越界**（见 3-diff F2，提示级） | **对应 ✓**（1 条提示级越界，另记） |
| 原句 2 | `‘I don’t know how to describe it.’ Callie ate another segment. ‘Like you’re lost in the back of your head. You’re not quite here, whereas last month when you helped out on that gang stabbing you were sort of chill.’`（`text/ch10:38`，[625,775]） | **是**。中文理解＝「她形容不出那表情 / 人不在这里 / 拿上月那起帮派刺伤案作比、那回他反倒松快」，全部落在引语内。「警务系统之外的人读警察的状态」是对引语内容（Callie 是局外人、他在局内）的写法性说明，不是全书主旨。 | ① 主语：Callie（描述、吃橘子瓣）；② 受事：**Caius** 的状态（「你」= Caius，原文 she 对 he 说）；③ 归属：「上个月他**参与**的那起帮派刺伤案」= `when you helped out on that gang stabbing`，md 写「参与帮派刺伤案那次」✓ 方向一致 | 有「为什么」：外人读警察＝更可信；松快 vs 不在场＝为后面认领案子埋线。**但「这不是他的本行」把落点写偏**（3-diff F3，提示级） | **对应 ✓**（1 条提示级因果倒置，另记） |
| 原句 3 | `Caius flipped a pancake over. He should've waited to make this tomorrow when his cast would be off and he wouldn't have to hold the pan with one hand. ‘It’s an odd one. I’ve had a bad run of funny cases. It’s usually drugs and gang-related like you said, or domestic violence which is a special sort of awful but this one …’`（`text/ch10:59`，[1248,1620]） | **是**。中文理解＝「翻饼 → 本该等明天石膏拆掉 → 不用单手握锅 → 这案子怪、平常是毒品/帮派/家暴、这一件……」，全部落在引语内。 | ① 主语：Caius（翻饼、心算、说案情）；② 受事：`his cast`＝**他手上**的石膏、`he wouldn't have to hold the pan with one hand`＝**他自己**单手；③ 归属：`like you said`＝**Callie 刚说的**（`text/ch10:44`「you're a professional」那段），md 写「像你说的」式承接 ✓ 方向一致 | 有「为什么」：机械动作 → 心里那句「本该明天再做」，把「明知不便仍上手」的体贴落在动作上；省略号收住半句＝全章转折 | **对应 ✓** |
| 原句 4 | `‘It looks like a man was murdered by his date.’ Caius was reluctant to go beyond that.`（`text/ch10:65`，[1674,1759]） | **是**。中文理解＝「他说这案子看起来像是一个男人被自己的约会对象杀了；叙述随即点明，他不肯再往下说」，两小句各对应引语的一小句。 | ① 主语：**Caius**（说这句的人）；② 受事：一个男人 / 他的约会对象（`by his date`＝**凶手是约会对象**，md 写「被自己的约会对象杀了」方向一致 ✓）；③ 归属：`Caius was reluctant to go beyond that`＝**他自己不肯再往下说**，md 写「他不肯再往下说」✓。**本章三处专项核对在此落地**：说话人＝Caius（非 Callie）✓ | 有「为什么」：一句话交底 + reluctant 封口＝被咽回去的省略比情绪描写更重 | **对应 ✓** |
| 原句 5 | `‘Maybe …’ Callie shrugged. She let the words in her mouth fall to the floor unspoken. That was a decision for him to make. ‘What am I doing with my life?’`（`text/ch10:74`，[1931,2050]） | **是**。中文理解＝「耸肩 → 那句『也许』没让它落地 →『那该由他来决定』→ 话锋一转问『我到底在干什么人生』」，逐小句对应。 | ① 主语：Callie（耸肩、咽回、转话题）；② 受事：`unspoken` 的是**她自己的话**（`the words in her mouth`），不是 Caius 的话；③ 归属：`That was a decision for him to make`＝**那个决定归他（Callie 的 "him" = Caius）**，md 写「那该由他来决定」✓ 方向一致 | 有「为什么」：「落到地板上」这个动作写没说出口的话，同一段里完成「照顾他的沉默」与「暴露自己的空洞」 | **对应 ✓** |
| 原句 6 | `Callie took out three full bars of Lindt milk chocolate. ‘Did you buy this in anticipation of the arrival of my period.’`（`text/ch10:110`，[3081,3201]） | **是**。中文理解＝「从他背包里翻出三整条 Lindt 牛奶巧克力，问他：你是预判着我快来月经了才买的吗」，两个动作各对应引语一小句。 | ① 主语：Callie（拿出巧克力、提问）；② 受事：`his backpack`＝**他的背包**、`three full bars`＝**三条**；③ 归属：`Did you buy this…`＝**问的是他（买的人是他）**，`anticipation`＝**她对他行为的解读**（他在预判她的生理期），md 写「你是预判着我快来月经了才买的吗」✓ 方向一致 | 有「为什么」：体贴被写成具体量（三条/整条）；`anticipation` 把家常话弄滑稽；「不是谢谢，而是『你是不是早算好了』」写出两人互相试探 | **对应 ✓**（「没拆封」越界，3-diff F4，提示级） |

## 逐块小结

- **对应组：6/6 通过**。没有一块出现「讲引语之外的上下文」（引语选短）、「讲全书主旨/作者生平」（不对应）或「只复述字面、没有为什么」（密度不足）。
- 6 块的「为什么这样写」都有实质分析（非字面复述），密度由 `chapter.sh` 量化：中文理解 32–81 CJK 字、占比 0.70–0.93；「为什么这样写」72–81 CJK 字、占比 0.77–0.89。
- 施事/归属三问全部通过（**含**本章专项的三处核对：下厨者＝Caius ✓；帽匠＝Callie 而非 Caius ✓；「像是被约会对象杀的」＝Caius 说的 ✓）。
- 越界项（不改变「对应」判定，另在 `3-diff.md` 记）：F2「不会做饭」、F3「不是他的本行」、F4「没拆封」。
