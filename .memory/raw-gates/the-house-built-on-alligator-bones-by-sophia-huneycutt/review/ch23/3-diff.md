# ch23 对账（R1–R4）

text = `text/ch23_chapter_twenty_two.txt`（172 行，1,928 词）｜md = `ch23 hidden room and ruined sketchbook.md`｜块数 6（建议 4–6 ✅）｜素读事实 156 条／MISS 0｜机器层 rc=0（引语块 6／片段 6／查无 0）

## 阻断

- **[C-23-1] 伪造引语＋语义相反**｜md:13「她起初决定不带走笔记本（**'我了解舅舅为什么要藏着'**）」
  这句带引号的"原文"在全书 text/ 查无，且原意相反。:27 实际是：`My instinct was to retreat with them to my room, but I decided against it. Why hide the fact that I was learning about my uncle, especially when Gazzie had already opened up about him?`
  ——她反问的是**自己**为什么要藏着（既然 Gazzie 已主动讲过 Leon），并据此决定**不**偷偷带回房间；md 把它写成"她理解舅舅当年为什么藏"。主语与对象同时移位。
  ⇒ 改法（去掉引号、按原文重述）：「她本想把这些本子带回自己房间，却决定不这么做——既然 Gazzie 已经主动讲过 Leon，她不明白自己有什么理由要藏着。」
- **[C-23-2] 亲属关系反转（两处，同一根错）**｜md:13「Mama（Caroline）借**儿子**的转述出场」＋ md:64「这是 Leon 抄写**妈妈的话**——日记里他一路称呼 Mom，这里改用名字 Caroline，语域一沉，说明这句是被当作家训供起来的」
  原文证据：Caroline 是 Leon 的**姐姐**——`ch20:351` `He was two—she was four—when we took him to feed the gators`、`ch20:363` `When Leon was seventeen… Caroline told him she needed him to help here`、`ch20:378` `after another tuition argument, Caroline and I made him go to the farm`；Leon 日记里的 **Mom＝Gazzie**（:46 `Mom too busy to visit`、:60 `Clearly, he's never met Mom`，与 ch20 断学费同人）。
  ⇒ md:64 的"语域一沉"整套推论（Mom→名字＝升格为家训）建立在把姐姐读成妈妈之上，须整段重写；md:13「儿子」改「弟弟」。
- **[C-23-3] 越界裁决「有人」＋与自身矛盾（三处）**｜md:10「那本速写本**被人**挪进浴室水槽」／md:74「证据够确认'**有人**'，不够确认是谁」／md:112「如今仍**有人**不许人看，而她已被列进需要被阻止的名单」
  :168 的 `No. Someone had taken the sketchbook…` 是**她在场外的推理**，而同一章把闹鬼道具全留在原句里：:144 `Greer House's familiar hum`、`the scent of sour jasmine`、`the tail end of a black shape slip into the bathroom`、随后 `Then came the sound of the faucet turning on`；:168 自己也只给 `somehow snuck out, **maybe** through the bathroom window`。
  ⚠️ 同一份 md 的 md:12 已写对：「嗡鸣、酸茉莉气味、黑色形状这些闹鬼道具，**被叙述者按成**人类作案现场」⇒ 三处须统一到"她判定"，并把 md:74 的"证据够确认有人"改为"证据够让她否掉'失足落水'"。
- **[C-23-4] 漏·承重单元（1983 年本的四条展示体短记全部未登记）**｜:40 `Get a load of this idiot.`／:43 `Jeannette said no to a date, but we're meeting up for ice cream tomorrow. What does that mean?`／:46 `Brought Aunt V flowers at the hospital. Mom too busy to visit. Shocker.`
  导航五句、6 块、词表 15 行——全 md 无一处提到这三条短记。它们不只是"青少年腔"的样品：:46 同时交出两条承重事实（**Aunt V 住过院**、**Mom 忙得不去探望**＋孩子的 `Shocker`），而 Mom＝Gazzie 这一条正是 C-23-2 的原文纠错依据。md:14 只登记了「日记引文以独立短段插进第一人称叙述」这个形式，没有登记任何一条内容。
  ⇒ 在「人物弧线」或加一块中至少处理 :46，并标明它是 1983 本而非 1985 本。
- **[C-23-5] 逐字·撇号字形（导航层，机器不覆盖）**｜md:10 `"I'll make her let me go or die trying"`
  :119 原文是 `I’ll make her let me go or die trying.`（U+2019）。该层不在 `QUOTE_RE` 口径内 ⇒ `chapter.sh` 全绿。属全书同形态（15/49 章、51 处）逐条判形队列之一：**短语本身逐字正确，只改字形**。

## 提示

- **[P-1]**｜md:10「1985 年**最后一册**」——:53 原文是条件式 `If it was his last sketchbook, his final thoughts would be inside`；:162 `The last months of Leon's life, lost` 只算部分支持 ⇒ 建议保留假设标注（「她当作最后一册的那本」）。
- **[P-2]**｜md:20「**那具**尸体惹出的糗事」——规模不符：ch21 `Hundreds of carcasses in total. Five hundred, maybe.`、本章 :9 的 fiasco 指同一批 ⇒ 改「那堆尸骸惹出的糗事」。
- **[P-3]**｜md:11「**号角** Ida」——:70 `bright red horns crowned her head`，应为「长角的 Ida」；错字。
- **[P-4]**｜md:40「Gazzie 交代过的**纵旧事**」——漏「火」字（:67 `Gazzie's arson confession`）。
- **[P-5]**｜md:11「泡烂的速写本把恐惧换成**冷怒**」——:159–:165 只有 `With a yelp`／`“No, no, no,” I moaned`／`After I'd stopped shaking`／`the doomed task`／`my mind still spun`，全章无怒意词；建议「换成一种被正面拦住的寒意与不服」。
- **[P-6]**｜md:14「声音在'我'和 **1985 年的 Leon** 之间跳切」——前几条短记出自 1983 本（:30–:50），跳切实际跨 1983／1985。
- **[P-7]**｜md:34「暗门的'暗'**整个**交给 undetectable 一个词」——同句还有 `a hidden flush-mounted door` 的 hidden 与副词 `nearly`。
- **[P-8]**｜md:54「这一版比餐厅那些**钝**得多」——与同句自设的尺子（隐晦程度）反向：`much less subtle` 应作「直白得多／不加掩饰得多」。
- **[P-9]**｜md:76「嫌疑范围已经被这句**钉死在能进她房间的人里**」——她的名单 :147 是 `a misguided thief. Harrison. Ida Greer.`，其中 Ida Greer 不属于"能进房间的人"，而 :168 仍留 `maybe through the bathroom window`。
- **[P-10]**｜md:24「本章真正的推力被让给照片和**锁盒这两样手里的东西**」——锁盒恰是她不碰的那件（:9 `I left his lockbox alone`）；同一句末尾自己写对了（"就在手边，她不打开"）。
- **[P-11]**｜漏：:84 `I dismissed the word supernatural, instead landing on woo-woo`——她**换词**这个动作（与 ch22:111 Harrison 的 `woo-woo stuff` 同一条词链）md 只在 md:11 引了"房子老、回音大"。
- **[P-12]**｜漏：:112 `Her voice slipped into my ear: You'd better tame that devil in you, girl.`——本章唯一一次 Mama 以耳语形态回访，md 只在 md:66 用了"补全后半句"的推理，没登记"听见"这个身体事件。
- **[P-13]**｜漏：:147 `not when I'd been mistaken so many times before`——她对自己误判史的清账（决定不叫出声的理由），md 未登记。

## 假红（核对后成立——防下一轮改坏）

- md:13「叙述者从偷翻者变成被查禁者」——:27 她主动不带走、:168–:172 被人没收机会，形状成立。
- md:14「每次响动后面都紧跟一段自我反驳」——:81 撞击 → :84 自我讲理；:144 嗡鸣／水龙头 → :147「不能再在 Gazzie 面前出丑」＋:150「也许该开安眠药」；本章再无第三处响动，全称不越界。
- md:12「嗡鸣、酸茉莉气味、黑色形状」——三者同在 :144 同一段内，顺序也对。
- md:54「餐厅里那些 Ida 全是 Leon 的手笔」——`ch16:204` `They’re hanging in the dining room`（Virginia 指 Leon 的画）＋`ch16:267` `Each subject was Ida`＋`ch20:399` 支持。
- md:10／:66「Mama 衣柜墙上那句没写完，缺的正是后半截」——:112 `It hadn’t been finished. She’d only written the first part.`＋`ch07:43` 墙上只有前半句。
- md:64「一个 1985 年的死者执笔」——:53 `the year he’d died`；md 未因此裁决死因，合规。
- md:44「'巧合'不是证据推出来的结论，是她拍板决定的结论」——:67 `but that was, I decided, probably coincidence` 逐字支持。
- md:34「压在颈后的不是灰而是 Ida 的注视」——:24 注视句确在灰尘句之前，无时序错。
- md 全篇称"叙述者"而未用 `Dart`；本章原文 0 次出现 `Dart` ⇒ 无凭空专名，也不构成"漏写名字"。
- 逐字／形态层：引语块 6 条逐字（含 :101 `The walls were made of…I frowned and leaned back in the chair. Bones.` 的断句，机器查无 0）；词表 15 行例句逐字命中；非块内嵌英文全书查无 0（仅 `Chapter Twenty-Two`／`Tropes` 模板级例外）；ASCII 撇号除 md:10 一处外无其它。

## 不许裁决

1. Leon 之死是否意外：:126 `He couldn’t have predicted his accidental death.` → :129 `Unless it wasn’t an accident.` → :132 她自己 banished it——原文悬置，md 与修复指令都不得坐实。
2. 速写本是人挪的还是"它"挪的：:144 的黑色形状与 :168 的 Someone 并存，不裁决（见 C-23-3 的修法：只标"她判定"）。
3. Virginia 1983 年因何住院——:46 只有 `Brought Aunt V flowers at the hospital`，不得补病名或时间长度。
4. Mama 是否知道她那句话的后半截——:112 只说她只写了前半，不得推定她知不知道完整版。
5. `She thinks it’s funny, but I think it’s true.` 里的 She＝Caroline 的"觉得好笑"不得扩展成她对家族史的态度定论。
6. Leon 那个夏天是"失去现实感"（:132 她的读法）还是别的——原文保留两种读法，不裁决。
7. 那间半玻璃墙的房间是否书中别处已出现过的房间——:18 `I didn’t recognize the room` 未指名，不得坐实。
8. Michelle／Leon／Mama 三种死法一律不裁决（本书级护栏，延续）。

## 跨章取证表

| 本章条目 | 取证位置 | 用途 |
|---|---|---|
| Caroline＝叙述者的妈妈 | ch02:107 `I’m Caroline Beaumont’s daughter, Dartrine` | C-23-2 |
| Caroline 与 Leon 的年齿（姐弟） | ch20:351／ch20:363／ch20:378 | C-23-2 主证 |
| Leon 日记里的 Mom＝Gazzie | ch23:46／ch23:60＋ch20:363（断学费） | C-23-2、C-23-4 |
| Gazzie 的纵火自白 | ch21（`A contact of mine set one of his smaller sheds on fire`） | :67 的所指 |
| 衣柜墙上的前半句与 Mama 原话 | ch07:43／ch07:75／ch13:222 | md:10／:66 |
| Leon 的画挂在餐厅 | ch16:204／ch16:267／ch20:399 | 假红 4 |
| 锁箱与本子的前史 | ch17:120／ch20:417 | C-23-4、md:13 |
| 尸骸规模（数百具） | ch21（`Hundreds of carcasses`）／ch22:75 | P-2 |
| woo-woo 词链起点 | ch22:111（Harrison 原话） | P-11 |

## 探针自检（本判定文件自身）

`/tmp/span23.py`：反引号 span 88 条，MISS 5——`chapter.sh`×2（脚本名）、`Chapter Twenty-Two`／`Tropes`（模板级）、ch20 那条是省略号拼接，两段各自逐字（`/usr/bin/grep -c "When Leon was seventeen"`＝1、`"Caroline told him she needed him to help here"`＝1）；`/tmp/v23.py` 词表 15 行／flag 0；`/tmp/ap23.py` ASCII 撇号 **1 处**（md:10 `I'll`，已列 C-23-5）／反引号 span 0；`/tmp/in23.py` 内嵌英文 91 串／全书查无 2（两个模板例外）；`/tmp/s23.py` 素读 156 条／MISS 0。
