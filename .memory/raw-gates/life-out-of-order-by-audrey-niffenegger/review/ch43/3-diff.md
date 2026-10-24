# ch43 the last evening of the old normal — 对账单（R3）

- 原文：`text/ch43_the_last_evening_of_the_old_normal.txt`（346 行）
- 精读：`ch43 the last evening of the old normal.md`（132 行）
- 机器层：`2-machine.json`，rc=0，verdict=ok，8 块 / 8 段引语全逐字（segment_miss 0），empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5 条，H1 `43. The Last Evening of the Old Normal`，words 2658

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | 死者有了名字：李文亮；而「年长的自己提过他、却没给名字」正是 Alba 传话方式的样本 | `:95` ““Li Wenliang,” Alba says. “I never knew his name.””；`:104` “My older self mentioned him a while ago. She didn't say his name, though.” | `ch43 …md:11` 只写「死者的名字」；`grep -c "李文亮"` → 0 | 提示（正文点名，导航泛指；建议补名字） |
| L2 | 下周的纽约之行与克莱尔在 Drawing Center 2 月 17 日开幕的画展；Beck 说「你不想我们去，我们就不去」 | `:117` “We're going to New York for Clare's show next week.”；`:121` ““New York?” Alba says, aghast.”；`:127` “My show at the Drawing Center opens on the 17th.”；`:128` “if you don't want us to go, we won't go.” | md 全篇零命中：`grep -c "纽约"`→0、`grep -c "画展"`→0 | 提示（本章唯一被预言直接撞上的具体计划；`/usr/bin/grep -ln "Drawing Center" text/*.txt` 仅命中本章，属一次性布景，故不判阻断） |
| L3 | 人物关系背景：Nick 是 Carl 的双胞胎，两人都是密歇根大学大一；Nick 是 Nadia 的男友，Nadia 与 Alba 同在西北大学 | `:86` “Nick is Carl's twin. They're both freshmen at the University of Michigan. He is Nadia's boyfriend, and since Nadia is at Northwestern with Alba…” | `grep -c "尼克"`→0、`grep -c "密歇根"`→0 | 提示（关系网背景，未影响本章因果） |
| L4 | 两个大人的无声结论：「他是同性恋，我们早知道」 | `:161` “We exchange confirmative looks: He's gay, we knew it.” | `grep -c "同性恋"`→0 | 提示（对 Carl 分手理由的解释性伏笔，且是本章唯一的黑色幽默落点） |
| L5 | 贝克自己的旧伤：高中恋人赴斯坦福前一天把她甩了 | `:171` “she had a high school sweetheart who dumped her the day before he left for Stanford” | md 未收 | 跳过（细节性回照，非情节） |
| L6 | 卧室里那段关于伊莎多拉的对话：贝克想「她要在没有母亲的情况下长大」，克莱尔说「我更担心阿尔芭」 | `:307` “I felt bad for Isadora, that she would have to grow up without a mother.”；`:312` “what would happen to Isadora?”；`:325` “I can't bear to think of her down there, waiting.”；`:329` “I'm more worried about Alba” | `ch43 …md:11` 只写「怕得握着手商量不死，克莱尔最后开口祈祷」；`grep -c "伊莎多拉"`→0 | 提示（伊莎多拉线的收束被整段跳过；这一问在全书里是重要伏笔，建议至少一句） |
| L7 | 行动决定：「明天列清单，今晚太难过」 | `:249` ““Tomorrow,” Alba says. “We'll make a list and start on it tomorrow. Tonight I'm too sad.”” | `grep -c "清单"`→0 | 提示（承接下一章的钩子，导航未留） |
| L8 | 年龄锚点：Alba 18、Clare 48、Beck 43 | `:18` “Friday, February 7, 2020 (Alba is 18, Clare is 48, Beck is 43)” | md 只写日期（`:132`），无年龄 | 跳过（同 ch30 口径） |

## 二、编（md 有、原文无）

无。「只当是电影」有原文（`:230` “it sounds more like a zombie movie than real life”）；「商量不死」有原文（`:290-303` “What if one of us dies?” / “Let's not.” / “Deal?” / “Deal.”）；「母亲如释重负」有原文（`:47` “To my relief she's wearing the same clothes she left our house in”）。

## 三、错（两边都有但不一致）

| # | 断言位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | `ch43 …md:11` 一句话概括 | 「两个大人**只当是电影**，**直到**她说出戴口罩、抢厕纸与死者的名字」 | 原文次序是：李文亮的名字（`:95`）→ 疫情与两年（`:112`）→ 纽约（`:117-121`）→ 口罩／厕纸／关店（`:211`）→ **之后**贝克才说 “it sounds more like a zombie movie than real life”（`:230`）→ Floyd 与升桥（`:234`） | 提示（错：时序被压缩成「电影→口罩→名字」，与原文相反；导航概括句，非情节错挂） |
| E2 | `:132` 一句话总结 | 「年长的自己让**她转告母亲**，一场全球大流行病要来」 | `:112` 阿尔芭是对着**克莱尔与贝克两个人**说的：“she wants **you** to go out and buy tons of groceries”；`:117` 贝克当场回 “Two years! We're going to New York…” | 提示（错：受话人写窄了，把在场的贝克排除；块 4 的中文理解 `md:51` 写「要母亲与贝克」是对的，前后不一致） |
| E3 | `:13` Tropes | 「两个大人**先笑、再问、最后沉默**」 | `:117` 贝克先 nervous laugh；`:196` “We all fall silent” 出现在**卡尔分手**之后（不是疫情段末），紧接着 `:244` 克莱尔又问 “So what do we have to do?” | 跳过（顺序被压平，但「笑—问—沉默」作为反应序列在原文都能找到锚点，不作事实断言判） |

## 四、归属方向复核（R4 三问）

- 块 4 “she wants **you** to go out and buy tons of groceries…” ⇄ `:112`：施事是「年长的阿尔芭」（she wants），受事是**克莱尔与贝克**（you），不是阿尔芭自己去买；md `:51`「要母亲与贝克去囤」——方向正确。**但 `:132` 的「让她转告母亲」把受话人缩成母亲一人**（见 E2）。
- 块 5 “Carl broke up with me today” ⇄ `:134`：主动方是**卡尔**，受事是阿尔芭；md `:61`「卡尔今天和她分手」——方向正确，未写成「她与卡尔分手」。
- 块 6 “We have to stay home so we don't catch it, or infect anyone” ⇄ `:211`：主语「我们」＝全家；md `:71` 未写成「你们」。
- 块 7 “A Black man named George Floyd will be murdered by police” ⇄ `:234`：施事是**警察**，受事是 Floyd；md `:81`「会被警察杀害」——方向正确。
- 块 8 “I had wanted to be free… but now I pray” ⇄ `:342`：祈祷者是**克莱尔**（本章第一人称），不是贝克；md `:91`「结尾克莱尔说」——正确。
- 「贝克问要是我们中有一个死了怎么办」⇄ `:290` “What if one of us dies?”（贝克说的）；「两人说好不死」⇄ `:295-303` “Let's not.” / “Deal?” / “Deal.”——md `:132` 归属正确。
- 「克莱尔最后开口祈祷」⇄ `:342` “I find myself praying (though I don't know to whom, or what)”——正确；注意祈祷发生在**床上、睡前**，不是梦后。
