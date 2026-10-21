# 第 4 章 R3–R4 差异单（人工审查）

- **审查对象**：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md`（156 行，8 个引语块，modified 2026-10-21）
- **唯一真值**：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch04_chapter_4.txt`（373 行 / 24436 字符）
- **机器层**：`review/ch04/2-machine.json`（已存在，未改动）——`verdict: ok`；8 块 `ok=true`；`counts`：blocks 8 / quote_long 0 / segments 8 / segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0；`issues` 四组全空。
- **流程**：先整章素读原文并落 `review/ch04/1-suread.json`（R1），再开成品 md 对照（R3–R4）；本轮只出指令，**未改动任何 md 文件，git 未执行任何操作**。
- **行号约定**：`text/ch04_chapter_4.txt:NNN`＝原文行号；`ch04 chapter 4.md:NNN`＝成品 md 行号。字符区间为原文 UTF-8 解码后的 `[start,end)`，由 python3 读原文计算。
- **本轮口径**：本单只报**当前版本**仍存在的问题。父代理已代修的一处（md:13「控制型长姐」→「控制型妹妹」）记为**已修复**，不重复报错（详见「四、交叉说明」第 5 条）。
- **取证口径**：全部取证用显式路径 `/usr/bin/grep`（`text/` 被 `.gitignore` 排除，`git grep` 永远查无）；查单词用 `-w`，交替匹配用 `-E`。每条「零命中」类断言在文末附原命令、输出与退出码。

---

## 一、漏（L）

### L1【提示】Diana 在车厢里确实做过一次确认（戴上眼镜又看了一遍），md 写成「没做任何确认」

- **原文侧**（`text/ch04_chapter_4.txt:216`，字符区间 [18320,19856)）：`Once she found her glasses and put them on, she looked at him again, in case she’d been mistaken. But no, it wasn’t a trick of the eye. It was a knife.`——她戴上眼镜后**又看了一遍**，只是为了排除自己看错；紧接着才是 `Diana stood up. Without thinking twice, she pushed through…`
- **md 侧**：`ch04 chapter 4.md:12`「最高点是车厢里那个**没做任何确认就起身喊人下车的自己**」；md:111「注意这一次她**没有先去确认**。整章她都在向别人求证，这一刻她直接动手了」；md:156「这是她**不再反复确认就行动**的代价」。
- **影响**：原文里她做过两层确认——先眯眼看（`:213`「She squinted, and it seemed that what the young man juggled was a knife.」），再戴眼镜复看（`:216`）——「no, it wasn’t a trick of the eye」是她**排除误认**之后才站起来的。md 写成「没做任何确认」，把「确认过但不再向他人求证」压成了「未经确认」，与 md:11 自己写的「认定有人在玩刀」（认定＝已作判断）也自相矛盾。三处口径同源，一处修即可。
- **修法**：把 md:12 改成「车厢里那个**自己确认过、却不再向别人求证就起身喊人下车**的自己」；md:111 改成「注意这一次她**不再向别人求证**。整章她都在向别人求证（给学校打电话、跟丈夫确认），这一刻她只信自己的眼睛，直接动手了」；md:156 改成「这是她**不再向别人求证就行动**的代价」。（三处不必全改，改 md:111 + md:156 两处即可覆盖。）
- **取证**：`/usr/bin/grep -n "in case she" text/ch04_chapter_4.txt` → 命中 `:216`，退出码 0。

### L2【提示】Alba「挟持母亲、吓住其余人」这一章最重的指控，md 全文没有

- **原文侧**（`text/ch04_chapter_4.txt:195`，字符区间 [9563,12184)）：`He could see very clearly Alba was holding Carmen hostage and intimidating the rest of them.`
- **md 侧**：`ch04 chapter 4.md` 全文检索 `挟持` / `要挟` / `hostage` 命中数均为 **0**。md:13 只写「Alba 的要求从不商量，Carlos 看得一清二楚却插不上话」；md:85 只写「两个说法互相咬合」。
- **影响**：这是原文里对 Alba 最重的一句定性，也是 md:13「控制型妹妹的套路在本章兑现」唯一可依托的原文凭据。md 把 Carlos 的核心判断抽象成了「要求从不商量」，「母亲被当作人质、其余家人被吓住」这层反而消失了；读者也拿不到 Carlos 与 Diana 在同一场对话里「一个看见挟持、一个不敢说不」的结构性张力。
- **修法**：在 md:85（块 6「为什么这样写」）或 md:87（块 6「读者视角提示」）补一句，例如「Carlos 看得再清楚也只敢在心里说『Alba 是在拿母亲当人质、吓住其余的人』——他唯一能做的，是把这条指控换个说法递给 Diana，而 Diana 立刻替妹妹辩护」。
- **取证**：`/usr/bin/grep -n "holding Carmen hostage" text/ch04_chapter_4.txt` → 命中 `:195`，退出码 0；`/usr/bin/grep -c "挟持\|要挟" "ch04 chapter 4.md"` → 输出 `0`，退出码 1。

### L3【提示】Carlos 是独生子、几乎不与父母来往——他只能待在外围的根因，md 全文没有

- **原文侧**（`text/ch04_chapter_4.txt:195`，字符区间 [9563,12184)）：`Carlos, who was an only child and barely had any contact with his parents, often stayed on the edge of family turmoil. He found it overwhelming and only engaged when it was directly and seriously affecting him. As was the case currently. This family dynamic was his weak spot…`
- **md 侧**：`ch04 chapter 4.md` 全文检索 `独生子` / `独生` 命中数均为 **0**。md:13 只说「Carlos 看得一清二楚却插不上话」。
- **影响**：md:13「插不上话」缺解释——读者不知道他为何只能站在边缘。这条同时决定了一个身份事实：**Alba 是他的妻妹（`sister-in-law`）与岳母（`mother-in-law`），不是他的血亲**（原文同段另有 `So—though it wasn’t like him at all—he sometimes criticized his sister-in-law.`）。少了这条，md:14「Carlos 劝她对 Alba 说不出不」的分量就偏轻。
- **修法**：在 md:13（现写「Carlos 看得一清二楚却插不上话」处）或 md:85 补一句，例如「Carlos 是独生子、几乎不跟父母来往，习惯待在这场家庭动荡的边缘，只在直接影响到自己时才介入——Alba 在他这里是妻妹，不是血亲」。
- **取证**：`/usr/bin/grep -n "only child" text/ch04_chapter_4.txt` → 命中 `:195`，退出码 0；`/usr/bin/grep -c "独生子\|独生" "ch04 chapter 4.md"` → 输出 `0`，退出码 1。

### L4【提示】拿刀者的可辨特征（冬天穿短袖、双臂有新旧伤口、找自己的倒影）全部缺失

- **原文侧**（`text/ch04_chapter_4.txt:216`，字符区间 [18320,19856)）：`The young man was searching for his reflection. He was wearing short sleeves, though it was winter, and his arms were full of wounds, some of them open. The tattoos partially concealed them, but there they were, fresh.`；同行还有 `His skin was sunburned, his eyes were too far apart, and he could have been anywhere between twenty and fifty years old.`
- **md 侧**：`ch04 chapter 4.md` 全文检索 `短袖` / `伤口` / `纹身` / `倒影` 命中数均为 **0**。md:11 只写「认定有人在玩刀」；md:109 只做动作分析。
- **影响**：md 的摘句选了块 8（`:216` 段的中段），但把该段最有信息量的部分——一个在冬天穿短袖、双臂伤口敞开、还在找倒影的人——整段略过了。读者只拿到「有刀」，拿不到「这个人不对劲」；「找倒影」这一动作还与 Diana 自己反复确认的行为形成对照，是本章与主题直接咬合的一处细节（`:216` 该段里另有 `His skin was sunburned, his eyes were too far apart, and he could have been anywhere between twenty and fifty years old.`，md 亦未取用）。
- **修法**：在 md:107（块 8「关键词」）或 md:109（块 8「为什么这样写」）补一句，例如「原文里那人正在**找自己的倒影**，穿着短袖、双臂有敞开的伤口——他也在确认什么，只是方式跟 Diana 正好相反」。（若改 md:107 关键词行，须与机器层 `keyword_bad` 口径一致，建议加在 md:109 分析行。）
- **取证**：`/usr/bin/grep -n "short sleeves" text/ch04_chapter_4.txt` → 命中 `:216`，退出码 0；`/usr/bin/grep -n "twenty and fifty" text/ch04_chapter_4.txt` → 命中 `:216`，退出码 0。

### L5【提示】Diana 手臂的伤是车门夹的，md 只写「卡在车门中间」，没交代伤

- **原文侧**（`text/ch04_chapter_4.txt:222`，字符区间 [19921,20071)）：`"There was a guy with a knife on the train," she answered, still out of breath, touching her right arm. One of the doors had pinched her, and it hurt.`；`:240`（区间 [20775,21072)）`Her arm was completely red, but it was impossible to tell whether it was from the door or from taking off her coat.`
- **md 侧**：`ch04 chapter 4.md` 全文检索 `门夹` / `夹伤` / `手臂` 命中数均为 **0**；md:11、md:156 只写「自己却卡在车门中间」。
- **影响**：原文里她除了「疑似持刀」之外，还**实实在在受了伤**——车门夹的右臂，整条通红；而且原文明确说红肿的原因分不清（车门夹的，还是脱外套蹭的）。md 把这一层整个删掉，只剩「卡在车门」的动作结果，读者不知道这一趟她还带着伤；「原因不可分辨」这一笔更是被抹掉了。
- **修法**：在 md:11 或 md:156 补半句，例如「自己却卡在车门中间，右臂被车门夹出一道红肿——原文没说清那红是夹的还是蹭的」；或在 md:109 之后另起一句交代。
- **取证**：`/usr/bin/grep -n "pinched her" text/ch04_chapter_4.txt` → 命中 `:222`，退出码 0；`/usr/bin/grep -n "completely red" text/ch04_chapter_4.txt` → 命中 `:240`，退出码 0。

### L6【提示】生日饭的时点差一天（今天是生日、明天才是平安夜），md 只写「生日饭」没写日期关系

- **原文侧**（`text/ch04_chapter_4.txt:54`，字符区间 [5851,5935)）：`"Because tomorrow is Christmas Eve, and celebrating two things at once is bad luck."`；`:36`（区间 [5166,5382)）`"We’re meeting up for Alba’s birthday…"`；`:72`（区间 [6209,6314)）`"No, no, we have to go for lunch. I tried to tell her we’d just come for the cake, but there was no way."`
- **md 侧**：`ch04 chapter 4.md` 全文检索 `平安夜` 命中数为 **0**；md:11 只写「吃妹妹 Alba 的生日饭」。
- **影响**：本章的核心喜剧机制是**两场庆典撞在同一天不吉利**，而这一句只有在「明天才是平安夜」的前提下才成立；连带的还有「不能只买蛋糕、必须去吃午饭」这一条。md 把时点抹掉后，这段争执只剩「她坚持要去」的情绪，没有理由。跨章看：**ch05 就是这场生日聚会本身**（`ch05:315`「You're going to be at urgent care for no reason, two days before Christmas」；`ch05:567`「It's past four o'clock and we still haven't eaten lunch.」），md 不写清日期，读者无法把 ch04 的「今天要去」与 ch05 的「聚会当天」对上。
- **修法**：把 md:11 的「吃妹妹 Alba 的生日饭」改成「吃妹妹 Alba 的生日饭——偏偏明天就是平安夜，她认定两件喜事撞一天不吉利，非去吃午饭不可（蛋糕都不行）」；或在 md:63（块 4「读者视角提示」）补一句时点说明。
- **取证**：`/usr/bin/grep -n "Christmas Eve" text/ch04_chapter_4.txt` → 命中 `:54`，退出码 0；`/usr/bin/grep -n "go for lunch" text/ch04_chapter_4.txt` → 命中 `:72`，退出码 0；`/usr/bin/grep -c "平安夜" "ch04 chapter 4.md"` → 输出 `0`，退出码 1。

### L7【提示】临时礼物是自己买给自己、还没穿过的红毛衣——md 只留了「自拍」一件糗事

- **原文侧**（`text/ch04_chapter_4.txt:300`，字符区间 [23189,23285)）：`"Oh, it’s a sweater I bought for myself, but I haven’t worn it yet. I’ll get another one later."`；`:303`：`"The red one?"`；`:321`（区间 [23534,23598)）：`"Well, that and the selfie you sent her from the dressing room."`
- **md 侧**：`ch04 chapter 4.md` 全文检索 `毛衣` 命中数为 **0**；`礼物` 仅命中 **1** 次（md:63「后面那件临时拿出来的礼物也是同一回事」）；`自拍` 命中 1 次（md:14）。md:63、md:14 都只点了「礼物」「自拍」。
- **影响**：md:63 特意写了「后面那件临时拿出来的礼物也是同一回事」，却没交代那件礼物是什么——读者拿不到「买给自己还没穿过的红毛衣」这个笑点，也读不出它与「试衣间自拍」并列时的杀伤力（两件糗事叠在一起，Carlos 才拿自拍开玩笑）。
- **修法**：把 md:63 改成「后面那件临时拿出来的礼物也是同一回事——买给自己、还没穿过的红毛衣，她还得另外买一件」；并在 md:14 的 Carlos 句后补一句「拿她那张试衣间自拍开玩笑时，他其实还知道另一件糗事：那份礼物是买给自己的」。
- **取证**：`/usr/bin/grep -n "it’s a sweater I bought for myself" text/ch04_chapter_4.txt` → 命中 `:300`，退出码 0；`/usr/bin/grep -n "the selfie you sent her from the dressing room" text/ch04_chapter_4.txt` → 命中 `:321`，退出码 0；`/usr/bin/grep -c "毛衣" "ch04 chapter 4.md"` → 输出 `0`，退出码 1。

### L8【提示】Carmen 对 Diana 的疲惫「几乎没有反应、然后换话题」，md 把它写成 trope

- **原文侧**（`text/ch04_chapter_4.txt:21`，字符区间 [3284,4786)）：`When she tried to explain this to her mother, it made her feel crazy—Carmen would barely react, as if she couldn’t hear her, then change the subject.`
- **md 侧**：`ch04 chapter 4.md:13`：「母亲的话没人当真这一套也部分兑现——Carlos 追问的是她的视力，不是她的判断。」
- **影响**：md:13 把这条写成了「母亲的话没人当真」，但原文里被无视的**是 Diana 的话**（`she tried to explain this to her mother`），不是母亲的话；母亲的反应是「几乎没反应、像没听见、然后换个话题」。方向被调了个个儿。同一行后半句「Carlos 追问的是她的视力，不是她的判断」反倒是对的，说明这两件事被并置但没对齐。
- **修法**：把 md:13 后半句改成「Diana 说累的时候母亲几乎没反应、像没听见、然后换个话题——这一套也部分兑现；Carlos 追问的则是她的视力，不是她的判断」。
- **取证**：`/usr/bin/grep -o "When she tried to explain this to her mother.\{0,120\}" text/ch04_chapter_4.txt` → 命中 `:21`，退出码 0。

### L9【提示】Alba 的生日聚会「他们都不能只买蛋糕」——md 未提

- **原文侧**（`text/ch04_chapter_4.txt:72`，字符区间 [6209,6314)）：`"No, no, we have to go for lunch. I tried to tell her we’d just come for the cake, but there was no way."`
- **md 侧**：`ch04 chapter 4.md` 全文检索 `蛋糕` / `午饭` 命中数均为 **0**。
- **影响**：这是 Diana 「没法拒绝」的具体形态——她试过只买蛋糕，被驳回。md 只说「Alba 的要求从不商量」，读者看不到要求具体长什么样。
- **修法**：并入 L6 的改写句（同一处补「不能只买蛋糕、必须去吃午饭」），不必单独加行。
- **取证**：`/usr/bin/grep -n "go for lunch" text/ch04_chapter_4.txt` → 命中 `:72`，退出码 0。

---

## 二、编（C）

**无。** md 本章所有事实性断言均已回原文取证，未发现凭空造出的情节、人物、数字或引语。逐条核过的断言如下：

1. md:11「戴上手镜／近视眼镜」——成立。`text/ch04:213`「She squinted, and it seemed that what the young man juggled was a knife.」＋`:216`「Once she found her glasses and put them on…」；`:234`「"I put my glasses on."」（Diana 自己向 Carlos 复述）；`:231`「"How is that possible? Are you sure it wasn’t something else? … You know how your vision is."」
2. md:11「站起来挤过人墙喊全家马上下车」——成立。`:216`「Diana stood up. Without thinking twice, she pushed through the wall of bodies… She yelled that they had to get off the train, now.」
3. md:11「自己却卡在车门中间」——成立。`:216`「Diana, behind them, was trapped inside, stuck halfway in the car until two other passengers managed to pry the metal doors apart.」
4. md:12「把检查的循环从家里的门锁推到拥挤的车厢」——成立。`:9`「She recognized the sound of the dead bolt, the second lock, and the third one…」；`:96`「I was about to call the school and have them check that she was there, but I restrained myself」。
5. md:12「最低点是她在女儿学校门口那种明明记得却仍然不信的自我折磨」——成立。`:96`「I watched them both go in, I remember both moments. The images in my head are clear as could be. And still, I swear… Brisa hadn’t made it inside.」
6. md:14「Carlos 劝她对 Alba 说不出不」——成立。`:189`「"You're already tired. I don't understand why you never tell her no."」；`:186`「"I don't have the energy to argue with her. I get so tired."」（说话人＝Diana）
7. md:14「到发现争不赢而认命上车」——成立。`:195`「He knew it was better not to insist. And he also knew that, insist as he might, he would end up on the blue line headed toward Sant Ildefons.」
8. md:14「末了还能拿她那张试衣间自拍开玩笑」——成立。`:321`「"Well, that and the selfie you sent her from the dressing room."」
9. md:14「Brisa 与 Tomás 的天真落在抢圣诞节手工作品和追问匕首是什么上」——成立。`:276`「The girl had torn the Christmas craft out of her brother’s folder.」；`:279`「"Stop, Tomás, you're going to hurt your sister, and me as well."」；`:354`「"What's a dagger?" asked Brisa.」
10. md:15「第三人称限知在 Diana 与 Carlos 之间整段切换（谈 Alba 的那一段落到伴侣一侧）」——成立。`:195`「Carlos went out to the dining room. He knew it was better not to insist.…」
11. md:15「车厢段落用穿了几层、拎了几袋的清单式排布制造窒息感」——成立。`:204`「She was carrying her bag, the kids’ backpacks, their sketchbooks with their crafts in them, their end-of-semester projects.」；`:204`（穿几层）thermal shirts / `:231`「How much clothing do you have on? You must be sweating to death.」
12. md:15「结尾把刀的高危收进一家人的插科打诨和一句站名纠正里」——成立。`:363`「"People going around with knives in Cornellà. Maybe your mom is right—maybe you do think you're above this neighborhood."」；`:372`「"Anyway, this isn't the Cornellà stop. It's L'Hospitalet."」
13. md:21「每次搬家都会去家具店比价，再去打听专业搬家的报价」——成立。块 1 引文即 `:6` 原文，词表例句（md:120、md:132）逐字命中。
14. md:27「书架是她给自己定的第一条标准线」——成立（原文 `:6`「Diana had dreamed for years of buying expensive shelving, real wood, solid and custom-made.」紧接同段「Diana's apartment was obsessively organized.」）。
15. md:99「她顺口说出的那句「这对她意义重大」」——**成立**，但说话人是 **Diana**，见 W2。
16. md:156「她又被妹妹的生日饭拖出门」——成立。`:36`「She invited me yesterday and I tried to get out of it, but she called me this morning all pissed off…」；Alba 是妹妹（跨章 `ch02:129`「Only her older sister, Diana」）。

---

## 三、错（W）

### W1【阻断】md:27「对女儿演出的过高要求」——要求是 Diana 对自己提的，不是对女儿提的

- **原文侧**：`text/ch04_chapter_4.txt:195`（字符区间 [9563,12184)）——整段里「要求/单方面决定」的主语一律是 **Alba**：`He didn't understand why neither Diana nor anyone else in the family dared to question Alba's decisions or challenge her plans, which were always made unilaterally and without consideration of their effects on others or the effort they required.`、`She complained about her sister's demands and said she was fed up.`、`He pointed out that Alba's demands weren't normal.`、`He reminded her how much money, and above all energy, they'd be saving if her sister weren't so possessive…`
- **md 侧**：`ch04 chapter 4.md:27`「书架是她给自己定的第一条标准线，后面对**女儿演出的过高要求**、对女儿是否进门的反复怀疑，都顺着这条线延伸。」
- **影响**：这是**归属方向反转**：原文里「要求」＝Alba 对这一家人的要求；md 把它挂到 Diana 对女儿 Brisa 的要求上。原文中 Diana 对女儿**只有自我要求与自责**（`:150`「"I should have known better. Fucking straightener. Why does this happen to me?"」、`:141`「"That's so embarrassing! The poor kid. And it was totally avoidable. I feel awful."」），她从未对女儿提要求；把「要求」的方向接到 Diana→Brisa，等于凭空造出一段亲子压迫关系，与本章要写的「Alba 才是那个提要求的人」正相反。同理，md:99「她对女儿是否进门的反复怀疑」是**自己不信**（不放心女儿有没有进去），不是「对女儿提要求」，此处方向亦需一并核对。
- **修法**：把 md:27 改成「书架是她给自己定的第一条标准线，往后**她自己那一套反复确认的标准**（对女儿是否进门要不要再打电话核实、对演出迟到要不要归咎到自己头上）都顺着这条线延伸——真正单方面提要求的是 Alba，不是她。」并把 md:99 的「她对女儿是否进门的反复怀疑」改为「她**对女儿是否进门**的反复怀疑」（去掉「对」字带来的「对女儿提要求」歧义）。
- **取证**：`/usr/bin/grep -nE "demand|insist|told Brisa|told Tom|told her daughter|asked Brisa" text/ch04_chapter_4.txt` → 只命中 `:195`（Alba 的 demands）与 `:354`（Brisa 问 dagger），**没有一条是 Diana 对女儿提要求**，退出码 0。

### W2【提示】md:99「她顺口说出的那句「这对她意义重大」」——说话人是 Diana，不是「她（Alba）」

- **原文侧**（`text/ch04_chapter_4.txt:192`，字符区间 [9500,9560)）：`"It means a lot to her. And it's her birthday. It's normal."`——这句在 `:186`「"I don't have the energy to argue with her. I get so tired."」（Diana 说）与 `:189`「"You're already tired. I don't understand why you never tell her no."」（Carlos 说）之后，**说话人是 Diana**，指的是 Alba（`it means a lot to her` ＝ Alba），回话对象是 Carlos。
- **md 侧**：`ch04 chapter 4.md:99`「这一章里她对女儿是否进门的反复怀疑，以及**她顺口说出的那句「这对她意义重大」**，用的都是同一套标准。」
- **影响**：md:99 这里的「她」按上下文读，指的是本章主角 Diana，而 Diana 恰恰是**评价者**、不是被评价的一方；「对女儿是否进门的反复怀疑」是 Diana 的症状，「这对她意义重大」却是 **Diana 替 Alba 找的理由**（她用这句话劝 Carlos 别再计较）。两句方向相反，被写成「同一套标准」是把症状与辩解并成了一条。另外「顺口说出的」也弱化了它——这句是她被逼到底之后的辩解。
- **修法**：把 md:99 改成「这一章里她对女儿是否进门的反复怀疑，用的是评判虚构的那套标准；而那句「这对她意义重大」则是她反过来替妹妹找的理由——同一套标准，一个用来怀疑自己，一个用来原谅别人。」
- **取证**：`/usr/bin/grep -n "It means a lot to her" text/ch04_chapter_4.txt` → 命中 `:192`，退出码 0（前后两行 `:186`/`:189` 为同一场对话）。

### W3【提示】md:13「Carlos 看得一清二楚却插不上话」——原文是「看得一清二楚」，但「插不上话」被写成了他的处境，原文里他终究说出口了

- **原文侧**（`text/ch04_chapter_4.txt:195`，字符区间 [9563,12184)）：`He could see very clearly Alba was holding Carmen hostage and intimidating the rest of them. But when he tried to convey that to Diana, it always played out the same way, and he only ended up getting frustrated.`；同段末 `Carlos became the bad guy for a bit.`
- **md 侧**：`ch04 chapter 4.md:13`「Alba 的要求从不商量，Carlos 看得一清二楚却插不上话」；md:14「Carlos 劝她对 Alba 说不出不，到发现争不赢而认命上车」。
- **影响**：「插不上话」与原文的机制不完全对应：原文里他**确实开口了**，而且这正是问题的来源——他每次开口举证，Diana 就倒戈护妹，于是 `Carlos became the bad guy for a bit`。原文的悲剧性在「说了没用、还成了坏人」，md 写成「说不上话」，把责任从机制转成了性格。
- **修法**：把 md:13 改成「Alba 的要求从不商量，Carlos 看得一清二楚、也一次次说出口，只是每说一次就被反推回来，到头来成了那个『坏人』」；md:14 可对应改成「Carlos 越劝她对 Alba 说不，她越倒戈，最后认命上车还落得一个坏人的名」。
- **取证**：同 W1 的 `:195` 逐字取证（`holding Carmen hostage` / `switched sides and defended her sister` / `Carlos became the bad guy for a bit.` 均在同一行内），退出码 0。

---

## 四、交叉说明

1. **称呼链**（本章的 `sister` / `her sister` / `his sister-in-law` / `mother-in-law` 各自指谁，必须回原文核）：
   - `:195`「She complained about **her sister's** demands」→ `her sister` ＝ **Alba**（说话人 Diana）。
   - `:195`「what **her sister** was doing was wrong」→ 同一段，＝ **Alba**。
   - `:195`「he sometimes criticized **his sister-in-law**」→ ＝ **Alba**（Carlos 视角：妻妹，非血亲）。
   - `:195`「**his mother-in-law** could divide her time between both daughters」→ ＝ **Carmen**（岳母）。
   - `:195`「Diana felt the same way, but when she sensed Carlos asking her to confront the problem once and for all, **she switched sides and defended her sister**」→ `her sister` ＝ **Alba**。
   - `:204`「**her sister’s gift**」→ ＝ **Alba** 的礼物（托特包里的礼物，`:300` 证实是买给自己的红毛衣）。
   - `:321`「the selfie you sent **her** from the dressing room」→ `her` ＝ **Alba**。
   - `:279`「you're going to hurt **your sister**」→ 说话人 Diana，＝ **Brisa**（Tomás 的姐姐）；`:276` 亦作 `his sister`（Tomás 视角）＝ Brisa。
   - `:291`「Mom is carrying around too much」→ 孩子口中的 `Mom` ＝ **Diana**（不是 Carmen；本章 Carmen 未出场）。
   - 成品 md 的称呼链现状：md:11 / md:81 / md:156 三处「妹妹」均指 Alba，**正确**；md:13「控制型妹妹」**已修复**（见第 5 条）。本单不再改动这三处。
2. **时间轴链**：本章是**平安夜前一天**（Alba 的生日）。三处互证：`:36`「We’re meeting up for Alba's birthday」、`:54`「Because tomorrow is Christmas Eve」、`:72`「we have to go for lunch」。因此 **Alba 的生日＝12 月 23 日**。跨章口径：**ch05 就是这场生日聚会本身**（`ch05:315`「You're going to be at urgent care for no reason, two days before Christmas」；`ch05:567`「It's past four o'clock and we still haven't eaten lunch.」），**ch10/ch15 是平安夜当晚**（`ch10:6`「There were five of them, not six. Alba was missing.」）。md 本章没有写出日期，见 L6。
3. **跨章事实（跨章引用必须标章号）**：
   - **Diana 是长姐、Alba 是妹妹**：`ch02:129`「Only her older sister, Diana, insisted she go to a specialist and sent her a dermatologist's number several times.」；`ch05:549`「She, on the other hand—who was six years older than Alba—did sometimes express her bewilderment.」（Diana 大 Alba 六岁）。本章原文只说 `her sister`（指 Alba），**不指明长幼**，因此方向要靠跨章定；md:13 原写「控制型长姐」方向反了（已修复），md 现写「妹妹」正确。
   - **Carlos 与 Alba 无血缘**：`ch04:195`「his sister-in-law」「his mother-in-law」；本章原文另有一处 `Carlos, who was an only child`（见 L3）。
   - **Brisa 是 Diana 的女儿**：本章 `:96`（与 friend Valeria 一起进校门）、`:276`（`Diana picked up their daughter, who was smaller`）、`:354`（Brisa 问「What's a dagger?」）三处互证；Tomás 是儿子（`:279`、`:276`「Carlos held the boy」）。跨章：Brisa 在 **ch15:30**「the day Brisa and Brigitte got bloody noses」（Brigitte 则是 Alba 的女儿）另有交代。
   - **Cornellà / L'Hospitalet**：本章 `:372` 末句「"Anyway, this isn't the Cornellà stop. It's L'Hospitalet."」；地点写法与全书一致（ch02/ch05/ch08/ch12/ch14/ch15 均作 `Cornellà`）。
   - **Alba 的年龄**：`ch02:129`「the thirty-seven-year-old whose eyes were raw and burning」（三十七岁指 Alba）；`ch05:546`「Alba had been thirteen then.」＋`ch05:549`（Diana 大六岁）⇒ 本章 Diana 约四十三岁。md 本章未写年龄，**不构成缺陷**，不补。
4. **体例一致性**：本章 md 全文用英文名（`Alba` 10 次、`Diana`、`Carlos`、`Brisa`、`Tomás`），未混入中文译名，与 ch02/ch05 的写法一致；`Carmen` 一次也没出现在 md 里（本章她未出场，md 也未硬塞），**不必**改。
5. **本轮已修复（不重复报错）**：md:13 的「控制型**长姐**」→「控制型**妹妹**」。依据：`ch02:129`「Only her older sister, Diana」（Diana 是姐姐）＋`ch05:549`「who was six years older than Alba」，控制型人物是 Alba（`ch04:195`「Alba's decisions, which were always made unilaterally」）。**另核实 ch04 全文还有无第二处亲属方向错误**：结论是**没有**——md 另两处亲属表述（md:81「她抱怨妹妹的要求」、md:156「她又被妹妹的生日饭拖出门」）均指 Alba，方向正确；`ch04:195` 的 `her sister` / `her sister's demands` / `her sister-in-law` 三处全指 Alba，md 未把它们安到 Diana 身上。

---

## 五、修后复核

改完 `ch04 chapter 4.md` 后，按顺序跑下面这组命令（**只验当前 md，不要覆盖仓库里的 `2-machine.json`**；输出请落 `/tmp`）。

```bash
cd "/Users/jcxs2014/Documents/Works/EnglishRead"

# 1) L1–L9 的补充句落地（期望 exit=0 且命中 ≥1）
/usr/bin/grep -n "确认过" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"   # L1
/usr/bin/grep -n "人质" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"     # L2
/usr/bin/grep -n "独生子" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"   # L3
/usr/bin/grep -n "短袖" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"     # L4
/usr/bin/grep -n "夹" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"       # L5
/usr/bin/grep -n "平安夜" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"   # L6
/usr/bin/grep -n "毛衣" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"     # L7
/usr/bin/grep -n "换话题\|换个话题" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"  # L8
/usr/bin/grep -n "蛋糕" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"     # L9

# 2) W1–W3 的旧措辞必须消失（期望 exit=1）
/usr/bin/grep -n "对女儿演出的过高要求" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"   # W1
/usr/bin/grep -n "她顺口说出的那句" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"     # W2
/usr/bin/grep -n "插不上话" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"         # W3

# 3) 关键归属不得被改坏（期望 exit=0，命中仍在）
/usr/bin/grep -n "控制型妹妹" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"       # 已修复项，勿改回
/usr/bin/grep -n "妹妹 Alba" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"        # md:11
/usr/bin/grep -n "抱怨妹妹的要求" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md"  # md:81

# 4) 门禁（输出落 /tmp，不要覆盖仓库里的 2-machine.json）
bash scripts/chapter.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md" --json > /tmp/ch04_machine_after_fix.json 2>&1; echo "EXITCODE=$?"   # 期望退出码 0
```

补充说明：

- 补写 L1–L9 的句子时，每条都应挂在**已有的四个子项行**（中文理解 / 为什么这样写 / 读者视角提示）上，**不要新开子项、不要改块数**（块数 8，落在 3–10 内）。
- 若动 `## 本章词汇` 的例句，须重跑逐字校验：该表 24 条例句必须仍是 `text/ch04_chapter_4.txt` 的逐字子串（本轮实测 `not_verbatim=0`）。本单各条修法均不涉及词表。
- 修 W1 时注意：`ch04:195` 里 `Alba` 与 `Alba's demands` 出现多次，`her sister` 也可能指 Brisa（`:279`）——改写 md:27/md:99 时不要顺手把「妹妹」一词改成「姐姐」。
- 本单只出指令，未改动任何 md 文件；git 未执行任何操作（未 add / 未 commit / 未 push）。
