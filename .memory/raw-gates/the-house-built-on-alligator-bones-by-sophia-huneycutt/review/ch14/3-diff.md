# ch14（书内 Chapter Thirteen）深审 R3/R4 三张单子

素读基线：`review/ch14/1-suread.json`（69 条事实／**0 MISS**，只读 `text/ch14_chapter_thirteen.txt`，写完才开 md）
机器层：`review/ch14/2-machine.json` → verdict `ok`（blocks 4 ∈ target [2,4]；segments 5／MISS 0；words 1168；struct_bad 0）
拼接引语独立取证：`python3 scripts/verify_fragments_indep.py "<书目录>"` → **引语条数 313｜受检片段 443｜MISS 0**（原句2 的 `…` 两段同落 :42 一段内，逐片段命中）
直撇号：`python3` 逐行扫描 → ch14 md **0 站**（md:56 的 `It’s not like…` 是弯形 ✓）
词表：13 行例句展平逐字 **0 MISS**

## 🟥 阻断（6）

### C-14-1 单位误写：「五指远」（且与同文件两处自相矛盾）
- md:14：**「人对峙用可量的距离写（五指远、三人行）」**
- 原文逐字：`text/ch14_chapter_thirteen.txt:105` — `“What I need,” she said to me, stepping closer, her pointer finger five inches from my nose,…`
- 反证（同文件已写对的两处）：md:50「食指停在离我鼻子**五英寸**的地方」；md:54 `"five inches from my nose" 用可量距离写威胁`
- 判定：`five inches` 被写成「五指远」——单位（inch→指）与身体部位（食指示指→五根手指）双错；「三人行」对 :114 `the line of three people` ✓ 无误。这正是既有规则「**同卷两处口径不一致＝自查报警信号**」的样本：导航与块层各写一套，块层是对的。
- 改法：md:14 → 「（食指离鼻尖五英寸、三人行）」。⚠️ 整改时**不得反向把 md:50／md:54 改成「五指」**。

### C-14-2 承重信息缺失：她对自己用词的当场拆台（sty）
- 原文逐字：`:42` — `Did you call a breeding pool a habitat, or something more sterile, like a sty?`
- md 现状：原句 2 的引语块用 `…` 跳过了这句；中文理解、为什么这样写、导航、词表（13 行）**一处未收**。
- 取证：`/usr/bin/grep -nE 'Ironheart|sty|辫子|braid|多少起' "ch14 caught in the grow out barn.md"` → **无输出，退出码 1**
- 判定：这句是本章「经营者眼光」这条自我形象的**刹车片**：md:34 盛赞她「看动物的眼睛已经在用管理者词汇」，而原文紧接着就让她自己怀疑那个词（habitat 还是 sty？）。少了它，md 把她的同情写成单向的成熟，实际原文写的是同情＋自嘲＋用词洁癖三样叠在一起。**且 md:34 的结论正建立在这句被删掉的词（habitat）上。**
- 改法：md:34 末补「而话音刚落她就自查用词——breeding pool 该叫 habitat，还是更无菌的说法如 sty（:42）；同情还没站稳，她已经开始管自己的名词」。

### C-14-3 语法术语误称＋内部自相矛盾：分裂句被叫成「命令的宾语前置」
- md:54：**「命令的宾语前置——"What I need" 起头就把答案钉死，中间塞进步伐和手指的距离，句法上不给其他选项留插槽」**
- 原文逐字：`:105` — `“What I need,” she said to me, …, “is for you to digitize those files. If you can manage it.”`
- 判定：这是 **what 引导的分裂句（伪分裂句）**，信息焦点被**推迟**到 `is` 之后（`is for you to digitize those files`）；「宾语前置」不成立（`what` 是从句内 need 的先行成分，主句层面并无命令宾语被前移），「起头就把答案钉死」更与句法相反，并与同句后半「中间塞进距离／不给其他选项留插槽」自相矛盾——正因为答案被推到 `is` 之后，中间才塞得进那根手指。属既有缺陷簇「分析层语法术语误称／时态误称」（ch13 C-13-4 同型，连续两章）。
- 改法：「分裂句 `What I need … is for you to …` 把真正的命令推到系动词之后，中间只容得下她上前一步和那根食指——句法本身就是『你要的只有这一件』；尾句 `If you can manage it.` 再把条件挂在整件事之后」。

### C-14-4 承重信息缺失：Ironheart 在本章唯一一次被点名（还是被她自己否定着点名）
- 原文逐字：`:66` — `Surely the alligators hadn’t moved perfectly in sync; that would be impossible. They were farm animals, not the long-lost progeny of Ironheart, lying in wait to tear at Greer flesh.`
- md 现状：Ironheart **一次未出现**（`/usr/bin/grep -nE 'Ironheart' "<ch14 md>"` → 退出码 1）；md:46 只引了 `that would be impossible`，把这句的另外一半丢了。
- 判定：Ironheart 自 ch05:135 起是贯穿全书的家系传说（本库既有记录：ch05 之后连续多章复现），本章是**叙述者第一次把「同步转头的怪事」直接接上这个传说、再用「它们是农场动物」按回去**。md:14 谈「声音先于形象」、md:46 谈「两种读法并排摆着」，却不写出这两条读法各自的名字（农场＝`farm animals`／超自然＝`the long-lost progeny of Ironheart, lying in wait to tear at Greer flesh`）——「两种读法」因此是空的。另 `Surely … that would be impossible` 是她自己的否定式自我说服，md 不能升格成「不可能」（不许裁决节已列）。
- 改法：md:46 或导航补一句「她把怪事按回原形的那句话里点名了传说本身：『它们是农场动物，不是 Ironheart 失传的后代在那儿等着撕 Greer 家的肉』（:66）——全书第一次由她亲口把两者并置又按下」。

### C-14-5「没有换来任务」与本章命令及同文件概括相抵
- md:12：**「她表演主动的全部动作（逃办公室、寻人、报藻类问题）没有换来任务，只换来 "If you can manage it." 的羞辱性确认」**
- 原文逐字：`:105` — `“What I need,” … “is for you to digitize those files. If you can manage it.”`
- 反证（同文件）：md:10「她的主动请缨最后**只换来一句命令——把文件数字化**，如果你做得到」✓
- 判定：`If you can manage it.` 是**追加在同一件任务之后的资格质疑**，任务本身确实下达了。md:12 写成「没有换来任务」等于否掉 :105 的祈使内容，并与 md:10 自己冲突。改法：「没有换来**新**任务——只把旧任务原样退回，后面再缀一句 `If you can manage it.` 的资格审查」。

### C-14-6 承重信息缺失：Harrison 没再来（三箱之后）与她「离真相更远」
- 原文逐字：`:21` — `Once on the office floor surrounded by files, I waited for Harrison to interrupt me with another cup of coffee, but by the time I’d scanned three boxes, he still hadn’t come. He’d apparently gotten all the information he needed from me. I, on the other hand, was no closer to figuring out what had happened between Gazzie and Mama.`
- md 现状：导航与 4 个块均无此段；词表 13 行里也没有（`apparently`／`no closer` 未收）。
- 判定：这是本章开场的**交换账**——ch13 那杯咖啡的刺探被她续写成预期（等他再端来），落空后她给出两句自陈：`He’d apparently gotten all the information he needed from me.`（带 apparently 的推测）与 `I, on the other hand, was no closer to figuring out what had happened between Gazzie and Mama.`。后者是全章动机的坐标（她随后「必须有进展」→ 溜出去），md:11 的弧线却直接从睡觉跳到「鼓起勇气的自荐」，跳过了这层「被榨干的一方反而没拿到任何东西」。
- 改法：md:11 或 md:13 补一句「等第二杯咖啡没等到——她认定 Harrison 要问的已问完（apparently），而自己离搞清 Gazzie 与 Mama 之间发生过什么**更远了**（:21）」，并保留 `apparently` 的对冲。

## 🟡 提示（9）

- **T-14-1**（md:11）「被**两个高尔夫车上的**男人盯到」歧义：:45 是**一辆**车上的两个男人（山羊胡驾驶＋金发壮汉），:48 才出现第二辆车（且未写车上有人）。改「一辆车上的两个男人盯着她」。
- **T-14-2**（md:13）「暴露两种自我」未含 :72 的报复幻想——原文 `I allowed myself to imagine yanking a tiny braid clean out of her head before forcing my mind blank.`，与 ch11 想砸凤梨花、ch13 想把咖啡浇在对方脚趾同族（暴力画面→自己掐掉）。建议作为第三种自我并入，或至少在该句后补「以及对 Nova 的一瞬报复幻想」。
- **T-14-3**（md:14）「鳄鱼齐转写成**慢镜头长句**」：:60 首句 `Then, each and every alligator, in unison, slowly turned to face me.` 只有 14 词、被四个逗号切碎，慢是逗号给的、不是句长给的。改「逗号层层加厚的慢镜」。
- **T-14-4**（md:30）「她**开球车**掠过 breeding pool」漏虚词，读作「开球＋车」。改「她开着球车掠过」。
- **T-14-5**（块3）未点 ch08:236 的反转：`They only hissed at Gazzie, like they knew she was responsible for their imp…`（ch08 那次嘶声**没有**跟着 Dart）；本章 :60 是它们第一次朝她嘶，:114 她还悬着「是冲我还是冲外头的 Gazzie」。补这一笔，md:14 的「不给答案」才有对面。
- **T-14-6**（md:10 之后）:84 `Nova had mentioned accidents, too. Just how many had there been lately?` 未收——它把 :81 与 ch12:105 `There’ve been accidents in the past.` 接上，是本章留给谜团的唯一追问。
- **T-14-7**（md:26）「把这三个响动与**本章别处的嗡鸣**、嘶声放在一起听」：`hum` 在 ch14 内只出现 1 次（:9，`/usr/bin/grep -nE '\bhum(ming)?\b'` → 1 命中），嗡鸣是跨章母题（ch05/06/09/10/15/16/17/20/22/23/30/31/38/39/42）。指针应改为跨章或删「嗡鸣」。与 ch13 C-13-T6（`answer` 全章仅 1 处却许诺回环）同族：**读者视角提示里的关键词须先 grep 本章命中数**。
- **T-14-8**（md:10/md:12）「被幼鳄**围住**」「少女被动物**围困**的桥段」：原文 :51 是她在栏杆旁俯看第一个围栏（`I leaned over the railing to my right`），:63 倒退着离开、:66 出门；未写被围。md:12 已正确声明「抽掉扑咬」，只需把「围住」降为「隔着栏杆被齐齐转头、逐个嘶起来」。
- **T-14-9**（md:13）:96 `I’d aimed for assertive, but my words came out as a question. At least I wasn’t being combative.` 未并入——与 :78 呛声后立刻 cringing 构成同一台「开口即自查」的机器，建议进人物弧线一句。
- **T-14-10**（md:13）:75 的后半句 `“And unless Nova’s a liar, she told you that already.”` 未收——Gazzie 的斥责以**雇员的话为前提**（同时留着「除非她撒谎」的余地），md:13 只写成「斥责乱走」。取证：`/usr/bin/grep -n '\bliar\b' "<ch14 md>"` → 无输出，退出码 1（⚠️ 用 `-w`：裸 `liar` 会命中 `familiar`，本会话即因此先误判过一次）。

## ⬜ 判为假红（7，勿改）

- **F-14-1** md:50「五英寸」与 md:54 `"five inches from my nose"` **是对的**（红在 md:14）；整改只动导航。
- **F-14-2** md:13「Nova 的作用是告状（**叙述者判断**）」——保住 :72 `She’d probably tattled on me.` 的 `probably` ✓，未被升格成事实。
- **F-14-3** md:11「第二个工作日之后睡得不错」对应 :9 `after my second day of work` ✓，与 ch13 `by my second afternoon` 时序自洽（非偏移）。
- **F-14-4** md:10 称棚里为**幼鳄**有据：:51 `each about a foot long` ＋ :114 `the juvenile alligators were still hissing` ✓；:60 `like the juveniles had with Gazzie` 指的是 ch08:177 那十间 juvenile 棚，两处不冲突。
- **F-14-5** md:40「恨意连成一片不停」对 `a wave of unceasing venom` ✓；md:44 把两个 `like` 分层（记她的脸／对 Gazzie 的旧例）不超原文。
- **F-14-6** md:56「引语之前她呛出的那句」时序正确：:78 在 :105 之前 ✓。
- **F-14-7** md:24「"becoming familiar" 比 "familiar" 更危险」保住 :9 的进行体 ✓；md:14「三个声源未明的响动」计数正确（湿布拖地 :9／疑似脚步 :12／电流嗡鸣 :9，全章均未给声源）。
- 词表 13 行例句逐字 0 MISS；`…` 拼接块受检 443 片段 0 MISS（书级），故**引语条数 313 全程不变**这条取证句在本章同样成立。

## 不许裁决（写进判定表）

见 `4-verdict.md` 末节：本章这棚与 ch08 那十间 juvenile 棚是否同一批动物；湿布声／脚步／嗡鸣的声源；同步转头是否有超自然成因；Nova 是否真去告状；事故「最近」的起数。
