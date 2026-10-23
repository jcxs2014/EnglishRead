# ch21 R3 三张单子（漏／编／错）

- 章文件：`ch21 shredded skins steak knives and arson.md`
- 语料：`text/ch21_chapter_twenty.txt`（378 行 / 3,397 词；块内引用写 `:行号`）
- R1 素读：`review/ch21/1-suread.json`（**292 条事实 / MISS 0**）
- R2 机器层：`review/ch21/2-machine.json`（chapter.sh rc=0；块数 11、引语块 11／片段 12／查无 0；H1 ✅「21. Chapter Twenty」；导航 5 项 ✅）
- 含 `…` 的块 5（:141 拼接）已由 `scripts/verify_fragments_indep.py` 独立取证：**全书 313 条／443 片段／MISS 0／拼接未标省略号 0**。
- 形态层本章**零缺陷**：词表 15 行逐字全中、ASCII 撇号 0、反引号 span 0、块外内嵌英文 174 串全部命中（除 H1 用词 `Chapter Twenty` 与标签 `Tropes`）。⇒ **ch18/ch19 的撇号与引号整改类不适用**。

## 一、阻断（8 条）

### C-21-1 【对应·张冠李戴】「她转向**最不爱搭话**的 Nova」
- md:10（导航·一句话概括）
- 原文逐字：`:72` "Besides me, Gazzie, Harrison, and Joe, five other people worked at the farm full-time. Javier and Will primarily worked outside. Seth and Benny-G managed the meat. I'd run into them around the farm, **they all seemed reluctant to chitchat with the owner's granddaughter. But the person least attached to the business might be willing to share information. Nova.**"
- 判据：「不愿闲聊」是**那五位全职员工**的画像；Nova 的入选理由是「最不依附这份生意」（least attached to the business）。md 把两个定位合并成「最不爱搭话」，正好抹掉 Dart 这一步的推理内核——她找的是**利益上最不必保密的人**，不是话最多或话最少的人。
- 改法：md:10 → 「她转向**与这份生意最不相干**的 Nova（其余五名全职员工都不愿和老板的孙女搭话），拿到两条线索……」

### C-21-2 【断言·施事错置，且与同文件另一处自相矛盾】总结写「Gazzie **亲口承认自己烧过**对面一座棚」
- md:162（一句话总结）；md:10「Gazzie 亲口承认扩张时曾**派联系人**放火烧了对面一座小棚」同族
- 原文逐字：`:231` "**A contact of mine** set one of his smaller sheds on fire. Just to let him know I was serious about taking over. Nothing that would harm the business's value."
- 反证（同一份 md 内）：md:84 块 7 分析已经写对——「动手的是 "a contact of mine"，**不是她**」；`:219` 她用的是第一人称复数 "we had to give the other owners a little encouragement"。
- 判据：原文给的施事是"一个联系人"，她的自认停在「we… 给了一点鼓励」「让他知道我是认真的」。"自己烧过"与"派联系人放火"都比原文多走一步（后者原文无 "I told him to"）。同一份 md 一处判对、两处判错。
- 改法：md:162 → 「而当 Gazzie 亲口承认为了接手**曾让对面付出过一座着火的棚**」；md:10 → 「Gazzie 亲口承认扩张时**她的一个联系人**放火烧了对面一座小棚，并命令她『不许接触任何一方』」。

### C-21-3 【对应·章内时序写反】把纵火承认排在尸骸场景之后
- md:11（导航·情感弧线位置）：「……直到她撞开卡死的后门、闻到腐臭、看见铺在草地上的尸骸，情绪变成生理性的窒息……**Gazzie 承认纵火那一段**把恐惧换了对象」
- 原文逐字：`:207` "Bringing up the former-owners idea to Gazzie didn't go as well. I found her in the slaughtering room…" → `:231` 纵火承认 → `:240` "Do not contact either of them" → `:243` 回储藏室 → `:246`–`:258` 二十盒档案全霉 → `:264` 逃进加工楼 → `:267` 撞开后门 → `:270` 腐臭 → `:273` 尸骸
- 判据：纵火承认在**霉与尸骸之前**（约早 40 个自然段），md 却把它写成窒息之后的转折。这条弧线的因果也被排错：md:11 说「她怕的不再是破坏者，而是自己正在讨好的这个人」，实际此后仍接着写她对霉与尸骸的生理恐惧（`:261` "mold spores…clogging my lungs"、`:285` "my thoughts spun out of control"），两种恐惧是**并存**而非替换。
- 改法：把该句移到「皮被绞碎、刀插成阵」与「霉吞掉二十盒档案」之间，并将「换了对象」改为「叠上一层」。

### C-21-4 【断言·全称被同章反证】「Joe **全程只有**否认与『我现在能不能干活』」
- md:13（导航·人物弧线）
- 原文逐字：`:33` "'What can I do for you?' he asked in an **exaggerated customer-service voice**." ／ `:39` "'No time for those,' he said, yanking another knife out of the ground." ／ `:45` "**Lost count at two hundred fifty.**" ／ `:51` "**Too long.**" ／ `:63` "He stood and strode to the other side of the pond, ending our conversation."
- 判据：他给了两条计数/时长的实质回答、一条讥讽式开场、一条动作性逐客。md 的"全程只有"抹掉了 Joe 在本章最有人味的三笔。
- 改法：→ 「Joe 给她的只有否认、两句带刺的应付（夸张的客服腔、『没那个时间』）和一句『现在我能干活了吗』」。

### C-21-5 【断言·被同段首句反证】「破坏就贴着前一句里那点好转发生，**中间没有过渡**」
- md:44（块 3·为什么这样写）
- 原文逐字：`:12` "**Before I could look into that particular incident more, the situation at the farm regressed.** Minutes after lunch on Thursday, Harrison reported that someone had shredded the skins…"
- 判据：段落首句就是显式过渡（先收上一件事、再宣告局势倒退）；日子也从 `:9` "The next day" 推进到 "Thursday"。md 想论证的"紧密"恰恰是靠这句过渡句完成的。
- 改法：→ 「章先用一句『还没来得及追查上一件，局势就倒退了』把两件损毁焊在一起，再把时间钉在『午餐后几分钟』——好转与毁坏之间只隔一个句子」。

### C-21-6 【对应·地点混为一栋】「破坏正落在生意的两端中间——**加工的一端**和繁殖的一端」
- md:100（块 9·为什么这样写）
- 原文逐字：`:273` "Animal carcasses spread across the grass between **the main building** and the breeding pond." ／ `:264` "With my new set of keys, I slipped into **the processing building**."（尸骸场景是她从加工楼后门出来才撞见的，`:267`）
- 判据：本章同时存在 main building（`:273`）与 processing building（`:264`）两栋；把 "main building" 读成"加工的一端"是把两栋并成一栋，且抹掉了「她正是为了躲开加工楼里的人才走到户外」这条动线（`:261` "I couldn't spend another second inside"）。
- 改法：→ 「地点精确到**主楼与繁殖池之间**——一边是账目与门面，一边是繁殖；而她是从加工楼的后门撞出来才撞上这一幕的」。

### C-21-7 【断言·全称被首个时间点反证】「**每个**时间点交一件新损毁物」
- md:14（导航·叙事手法）
- 原文逐字：`:9` "The next day, I returned to work." 段内**无新损毁**，交的是钥匙、休息时可自由走动、午餐露面，以及盘问结果（`:9` "at least my interrogation confirmed one thing"）。
- 判据：四个时间点里第一个交付的是"关系好转＋一条结论"，损毁物从 `:12` 才开始出现；而这个"先给好转再给损毁"的错位正是本章的手法。
- 改法：→ 「首个时间点交的是好感与一条结论，**此后**每个时间点交一件新损毁物」。

### C-21-8 【对应·地点名混用】「周五下午的**档案室**」
- md:14（导航·叙事手法）
- 原文逐字：`:147` "Realizing I wouldn't make more headway, I headed back to **the filing room**." ／ `:243` "Instead, I stomped back to **the storage room**." ／ `:246` "In the doorway, I surveyed the work ahead… **Twenty boxes** loomed before me."
- 判据：本章把 filing room 与 storage room 写成两个去处（她先说回文件房，随后实际回到堆箱子的储藏室）；霉变整段发生在 **storage room** 门口。md:10/md:11 用「档案盒／二十盒档案」是对的，只有 md:14 把房间写错。
- 改法：md:14 → 「周五午后的**储藏室**」。

## 二、提示（12 条）

| # | 位置 | 问题 | 证据 |
|---|---|---|---|
| T-21-1 | md:96 | 「时态迁移才是恐惧真正的来源」——从"做过"到"还愿意做什么"是**情态/指向**迁移（would be willing），原文时态未变（语法类别名用错，本书已知缺陷簇） | `:234` "Who else **would** she be willing to hurt…" |
| T-21-2 | md:50 | 「**成百上千**把牛排餐刀」放大原文 "hundreds"；本章的实际口径是 Joe 自报「数到 250 就放弃」＋她推算「500 把以上」 | `:24` "hundreds of steak knives"／`:45`／`:54` "Sticking five hundred or more knives…" |
| T-21-3 | md:13 | 「Harrison **第一次**给出稳定的价值判断」是跨章计数；ch18 他已给过 Joe 的性格判语（"He's a little… Old-fashioned"／"She likes competence"） | 需注明口径或改「本章第一次为他雇员说话」 |
| T-21-4 | md:66 | 「'hate' 是 Nova 的断言，**不是本章任何人的证词**」——`:165` Harrison 明说 "Gazzie pissed off both owners before taking over"，是本章内的旁证（虽不等于 hate）；md:13 自己也登记了这条承认，两处易被读成互相否定 | `:165` |
| T-21-5 | md:13 | 「Gazzie 由'缓和的上司'变成'**有前科**的所有者'」——原文只有一次自认纵火，无任何被追诉/定罪信息 | `:231`／`:234` "Arson. She'd committed arson." |
| T-21-6 | md:12 | 「也兑现'嫌疑人洗白、真凶另有其人'」——本章既没洗白 Joe（`:204` "I wasn't wholly convinced"）也没指认真凶；同句后半自己也说盘问没缩小范围 | `:204`／`:369` |
| T-21-7 | md:14 | 「**周五下午**的档案室」——`:24` "Friday morning" 之后原文不再标日，只有 `:267` "The late-afternoon sun"；同日推断可读，但应写「当日下午」 | `:24`／`:267` |
| T-21-8 | md:24 | 「在午餐时出现（**占用她的时间**）」——原文只 "made an appearance at lunch"，无占用机制 | `:9` |
| T-21-9 | md:24 | 「Harrison 的眉毛与她的笑构成第三方的见证，关系好转**因此不是她的自我感觉**」——而 "Even he could tell that my relationship with her was improving"（`:9`）本身就是她的叙述判读，见证仍出自同一双眼睛 | `:9` |
| T-21-10 | md:36 | 「往后**每一次**问话，她拿到的都是范围没有缩小的答案」——`:123`/`:141` 的 Nova 段确实新增两组嫌疑人，`:144` "Maybe Joe wasn't my only suspect"；「每一次」过满，改为「每一次都没能缩小到她手里」 | `:123`／`:141`／`:144` |
| T-21-11 | md:56 | 「本章**大量场面**都按这种『清点—沉默』的节奏写」——Nova 段（`:78`–`:141`）、Joe 段（`:33`–`:63`）、尸骸争执段（`:303`–`:366`）全是长篇对话；「清点—沉默」只适用于发现现场的那几段 | 结构核验 |
| T-21-12 | md:56 | 「警告不再是某个人的手势，而是一圈共同注视的眼睛」——原文没写刀是"某个人的手势"，`handle up` 的陈列性在 md:54 已由她推出，此处再把「手势」当成被否定的既定解释（轻微凭空） | `:24` |

## 三、假红（13 条，写进护栏，勿改）

| # | 表面疑点 | 判定 | 证据 |
|---|---|---|---|
| F-21-1 | 块 9 提示「这份清单里**没有鳄鱼**」 | **正确且是关键观察** | `:273` "Fish, mostly, but also ducks and swans and an otter or two." |
| F-21-2 | 块 11 「them 指代 culprit，本章到此处仍未给破坏者性别」 | 正确——全章 culprit 一律 they/them，无一处 he/she | `:369` |
| F-21-3 | 块 11 提示的三条"运气"证据 | 三条全部对得上：摄像头 / 用钥匙 / 全员被叫进室内 | `:300`／`:327`／`:264` |
| F-21-4 | 块 10 「三个 if 中只有 turned in sync to face me 涉及她自己」 | 句子结构核验正确 | `:282` |
| F-21-5 | 块 7 「第一句主语是 a contact of mine，后两句干脆没有主语」 | 语法核验正确（后两句是无主语的片段句） | `:231` |
| F-21-6 | 块 2 「字条两张都扔了，信息量与证据量成反比」 | 正确 | `:9` |
| F-21-7 | 块 4 「tracked our steps 让鳄鱼成了目击者」／块 9「没有鳄鱼」与 md:10「几百具被撕成两半的动物尸骸」 | 均与 `:24`/`:273`/`:279` 一致 | — |
| F-21-8 | 「有人专门冲着 Gazzie 来」的 specifically 读法 | 正确，且是本章唯一被叙述者自己盖章为「confirmed」的结论 | `:9` |
| F-21-9 | 钥匙链：块 1 提示把 `:9` 的钥匙、`:264` 进加工楼、`:327` 门锁争执连成一条 | **三处均在本章**，链条成立，勿按跨章臆断改 | `:9`／`:264`／`:327` |
| F-21-10 | 「Nova 从冷淡转为提供线索，代价是承认自己说话没人听」 | 正确 | `:105` "Sure," she said coolly → `:123` 长段分析／`:141` "no one listens" |
| F-21-11 | 「Move over, Nancy Drew」的模板自嘲 | 引语逐字正确、位置正确 | `:144` |
| F-21-12 | 「脑震荡还在愈合」 | **不是本章凭空**：`:9` 明写 my concussion，且 ch20:150 `"A concussion?"` 已建立诊断 | `ch20:150` |
| F-21-13 | 词表／撇号／内嵌英文 | 词表 15 行逐字全中；ASCII 撇号 0；块外内嵌英文 174 串全部命中 | `/tmp/v21.py` `/tmp/ap21.py` `/tmp/in21.py` |

## 四、不许裁决（12 条）

1. 破坏者是谁（单人／多人／非人）——本章只走到 `:369` 「除非有非人的东西在动手，或至少在替某人制造运气」。
2. 牛排刀是谁插的。
3. 走失鳄鱼、绞皮、插刀是否同一人（`:66`  herself 用的是 "probably"）。
4. Joe 是否说谎——他的两份不在场证明（`:21` 送货、`:306` 与 Javier 一起剥皮）都由 Harrison 转述。
5. 藻华与霉的成因（`:66` 按网络说法人为一夜造不出；`:258` "It wasn't natural" 是她的判语，不是结论）。
6. Ironheart 是否真实（`:261` 她先想到它，`:378` 末句把驱散猎物写成它的动作——全书不裁决）。
7. 纵火是否伤过人／"a contact of mine" 是谁。
8. 两位卫星农场前主人哪个更可能（`:147` Nova 明说不知道）。
9. 整盒霉变的档案里已读到／未读到的家族史内容损失多少（原文未清点）。
10. Harrison 是护短还是判断失误（`:306` 先说「不认为是这里的人」，`:312` 又主动提出外部可黑进无线摄像头）。
11. "encouragement" 除纵火外还包含什么（`:225` "Some required more than others" 原文未展开）。
12. 「她怕的到底是破坏者还是 Gazzie」——两种恐惧在本章并存（见 C-21-3），不排序。

## 五、跨章取证（登记表候选）

| 实体／母题 | 本章 | 关联章 |
|---|---|---|
| concussion（脑震荡） | `:9` 第一次在 Gazzie 口中出现为「正在愈合」 | `ch20:150` "A concussion?" 已建立诊断 ⇒ 本章是回指不是新事 |
| Joe 的橙刀 | `:27` "the knife he constantly used to **peel** oranges" | `ch19:27` "slicing oranges with a sinister, black-handled kitchen knife"（**动词 sliced→peel 有变化，同一把刀**） |
| phosphate（磷酸盐） | `:123` "the phosphate mine she's acquiring" | `ch18` Harrison 玩笑 "it's not like she has you reviewing the phosphate contracts" |
| sugarcane investments | `:123` **全书首次** | 总览层可用 |
| two satellite offices | `:135` 首次具数；`:138` 她从 Aunt Virginia 处「听过一点」 | Aunt Virginia 的 mysterious errands（`ch19:9`） |
| 纵火／fire insurance | `:225`／`:231` | 与 `:201` Harrison「他会放火烧农场」构成同一意象的两种用法 |
| Ironheart | `:261`／`:378` | `ch05:135`、`ch18` 门厅标本、`ch10` |
| 摄像头断线 | `:21`／`:300` | 与 `ch18` 结尾「挂锁＋监控摄像头」对得上 |
| 全员室内作业令 | `:264` | 使 `:315`「他们怎么知道今天所有人都在室内」成为本章争点 |
| Laura Leigh（前同事） | `:102` 用作 Nova 的对照 | `ch02`/`ch03` |
