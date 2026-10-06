# 《Immortal》(Sue Lynn Tan) 五步审查报告 · 2026-10-06

- 书目录：`notes/books/novels/immortal-by-sue-lynn-tan/`（47 章精读 ＋ 总览三篇）
- lane：**完整 lane**（`library/Immortal (Sue Lynn Tan) (Z-Library).epub` 在位，判定权威可用）
- 发起与执行：用户发起「独立进行五步审查」并指定同会话执行 ⇒ a–e 五步全部完整跑，**不以同会话局限为由减步骤**；a 步门禁**全部重跑、零采信**此前自报数字；b/c/d/e 均换用**与写作期不同的检查路径**（第二实现检查器 ＋ 现写扫描）
- 缺陷合计：**阻断型 45**（d 步 33 ／ e 步总览层 12）· **提示型 51**（只记不改）· **假红型 7**（工具侧，不改 md）

## 一、a 步：第 3 条门禁全量重跑

原始逐行输出见 `.memory/raw-gates/immortal-by-sue-lynn-tan/review_a_2026-10-06.txt`。

| 门禁 | 结果 | 档位 |
|---|---|---|
| verify_quotes（epub） | 400/400 可核实（100%），完全干净 48/48 | 阻断型 0 |
| sweep_full（整串 flat） | 本章命中 376／跨章 0／拼接 0／查无 0 | 阻断型 0 |
| check_chapter_quotes | 47 章逐章归属全对（每章 8 块） | 阻断型 0 |
| check_vocab | 词条 1406 行，FAIL 0 | 阻断型 0 |
| check_entities | 未知实体 0 | 阻断型 0 |
| corruption_scan | FAIL 0（U+FFFD／双句号） | 阻断型 0 |
| verify_overview_quotes | 58/58（情感节点 33、金句 25） | 阻断型 0 |
| check_overview_full | A 命中 87／查无 0；B 86 对＋1 歧义；C 2；E H1 错配 0 | 提示型 3 |
| check_vocab 超纲词 | 基础档 ≥9 字符启发式若干 | 提示型 |
| check_analysis_indep | 835 片段全命中，1 条整串查无（`ch01:10 Grandfather Zhao Likang`＝并列专名枚举，人判非冒充） | 提示型 1 |

⚠️ **a 步必须写清的一条**：`check_overview_full` B 段只验「逐字命中章 == 标注章」，对说话人、人物、关系、结局**零覆盖** ⇒ **标签对 ≠ 内容对**；本书 e 步的 12 处全是这一类，六道门禁全绿也查不出来。

## 二、b 步：逐章归属

cliffhanger 边界重点复查 ch43→ch44（藤蔓扔进液体在 ch43、Dalian 之死与拱门塌在 ch44）、ch23→ch24（Wuxin 到宫门外）、ch14→ch15（典礼与夺莲）。47 章逐章严格校验全对，**跨章搬句 0**。

## 三、c 步：结构扫描（第二实现）

`check_struct_indep.py`／`check_xref_indep.py`／`check_analysis_indep.py`（均与写作期自检不同实现：QRE `^> \*\*原句 (\d+):\*\* (.+)$`、SUB 四子项齐检、RANGE (3,8)、引语后配对＋≤3 字符证据窗）。整改后复跑输出见 `review_cd_2026-10-06.txt`：结构缺陷 0／提示 0；xref 英文证据报警 0；分析层片段全命中。

**工具侧发现（假红型，不在本书修复范围）**：
1. `check_analysis_indep.py` 只 `glob('ch*.md')` ⇒ **总览三篇的 inline 英文全库无门禁覆盖**。本书曾有一条凭空英文句写进 `00_概述.md` 而六道门禁全绿。补救＝现写一遍按 `00_*.md` 扫的扫描（本轮 177 片段，flat 查无 0）——**不要把 `check_analysis_indep` 的绿当成总览层的绿**。
2. `check_xref_indep.py` 收「只有 ch*.md」的目录时只报 2 处引用（那两个是 `来源:` 标签）；本书 192 处跨章引用**全部活在 `00_*.md`** ⇒ 跑它必须把总览三篇放进作用域，否则等于没跑。
3. 复核「原文有没有 X」时**一律展平匹配**（本书全弯撇号＋硬换行）；直引号 grep 造出过两次假「查无」。
4. **金句条目间的互指锚点无门禁**（「与 ⑰ ch24 相邻」这类）：本轮 ⑯ 指向一段并不存在的对应关系、① 指向 ㉑ 而墙句实为 ⑲——六道门禁全绿。⇒ **写完总览要按条目号逐条重读一遍互指关系**，这是独立于引语核对的第二遍。

如实标注：本节 1–4 是本轮**还能逐条复述**的工具类发现；c/d 步当时登记的假红型共 **7 条**，其余 3 条属当轮工具口径细节，未在此凭印象重写（不复述比补写更安全，需要时按 `git show 9ada60edb` 与项目记忆 `immortal-reading.md`「工具侧发现」节回查）。

## 四、d 步：语义二审（全部引语↔分析逐对核对）

5 批只读子代理 ＋ 主会话复核，覆盖 376 个引语块；指令附本库真实失败案例（100G ch86 ⑧「引语讲遮盖、分析讲没有叔叔」）与防幻觉条款（报警前须确认引语行与中文理解行同文件相邻）。

**阻断型 33 处，全部整改**（commit `9ada60edb`，23 个文件、39 行级 edit／39 删，引语层逐字未动）。**缺陷簇第一名是「章内时序／相邻断言写反」**——引语逐字全对、门禁全绿，错的只是「谁先谁后」「是 A 说的还是 B 说的」。

整改后仍登记为**提示型**的：51 条（措辞正当／启发式误报），**只记不改**。

### d 步逐条（改前 → 改后，超 300 字符截断；完整 diff 见 `git show 9ada60edb`）

**ch02 chapter 2.md**
- 改前：**为什么这样写：** 遗言被抽成单独一行，不带任何「他说」的框架，因此它不像回忆，更像直接贴在读者眼前的一条叮嘱。省略号的位置也讲究：前半句是要求，后半句是把要求往回收的温柔——他真正放不下的不是她报不报仇，是她苦不苦。紧接着一行 And now he’d found a way. 不加任何解释，把「好好活着」与「他替她换来这条命」并置成一句反话。
- 改后：**为什么这样写：** 遗言被抽成单独一行，不带任何「他说」的框架，因此它不像回忆，更像直接贴在读者眼前的一条叮嘱。省略号的位置也讲究：前半句是要求，后半句是把要求往回收的温柔——他真正放不下的不是她报不报仇，是她苦不苦。再往前是 And now he’d found a way. 一行，不加任何解释；它隔着她的一个闭眼动作落在这句遗言之前，两句并置成一句反话——「好好活着」这条叮嘱，正是他替她换来的那条命。

**ch03 chapter 3.md**
- 改前：- **一句话概括**：Liyen 面对烧了她家园、又刚救了她一命的 God of War：她当着他报出 Lady of Tianxia 的身份，看他杀尽剩下的 Winged Devils，听他说祖父并非他直接所杀、死于「心疾与恐惧」，接下必须向 Queen Caihong 效忠的规矩，换来一个月的期限与一把退不掉的 immortal 剑。
- 改后：- **一句话概括**：Liyen 面对烧了她家园、又刚救了她一命的 God of War：他当着她报出 Lady of Tianxia 的身份，看他逐一对付剩下的 Winged Devils——最后一只在他问出话之前自己用爪割了颈，听他说祖父并非他直接所杀、死于「心疾与恐惧」，接下必须向 Queen Caihong 效忠的规矩，换来一个月的期限与一把退不掉的 immortal 剑。

**ch03 chapter 3.md**
- 改前：**为什么这样写：** 这是本章他先向她问出的唯一一句：不问她是谁，问谁伤了她。轻声与杀意被一个 yet 钉在同一句里——比咆哮更有压迫感。后半句是无主语的悬置片段，句子停在她的听觉上：menace 是她先接住的，不是他说完才轮到别人听见的。
- 改后：**为什么这样写：** 这不是他本章的第一问：他先前已经问过 Who are you?，还复问过她的头衔；到这里问出的不再是身份，而是伤害。轻声与杀意被一个 yet 钉在同一句里——比咆哮更有压迫感。后半句是无主语的悬置片段，句子停在她的听觉上：menace 是她先接住的，不是他说完才轮到别人听见的。

**ch05 chapter 5.md**
- 改前：- **线索进展**：① 她身体的变化：只有她自己知道胸口每日涌起的那股新暖、每晨醒来都是足的，对外却照旧装作没复原；那一缕由死水留下的白发她今天没藏，别人只看得一眼便躲开；② 祖父的治国课落地成一条具体政令——开仓放粮；③ 她把朝局交给两个互为政敌的臣子与 Chengyin，算的是「让他们互相牵制」；④ 神界有条硬规矩：凡人一生只能进一次，超了时辰人就没了，这条规矩靠一根串金珠的红线系在她腕上；⑤ The Shield of Rivers and Mountains 就在这边，或许正在这位神的家中——这是她留下来的真正理由。
- 改后：- **线索进展**：① 她身体的变化：只有她自己知道胸口每日涌起的那股新暖、每晨醒来都是足的，对外却照旧装作没复原；那一缕由死水留下的白发她今天没藏，别人只看得一眼便躲开；② 祖父的治国课落地成一条具体政令——开仓放粮；③ 她把朝局交给三位臣子（Guo、Dao、Hu，其中 Guo 与 Dao 互为政敌）与 Chengyin，算的是「让他们互相牵制」；④ 神界有条硬规矩：凡人一生只能进一次，超了时辰人就没了，这条规矩靠一根串金珠的红线系在她腕上；⑤ The Shield of Rivers and Mountains 就在这边，或许正在这位神的家中——这是她留下来的真正理由。

**ch05 chapter 5.md**
- 改前：> **原句 1:** "A few courtiers exchanged impatient glances—their disdain for me evident in such looks, their shallow bows and increasingly brazen demands for lands and titles, anything they might grasp while the soil was still loose over my grandfather’s grave."
- 改后：> **原句 1:** "The escort to the Immortal Realm was late, a discourtesy that was hardly surprising. A few courtiers exchanged impatient glances—their disdain for me evident in such looks, their shallow bows and increasingly brazen demands for lands and titles, anything they might grasp while the soil ……

**ch10 chapter 10.md**
- 改前：- **一句话概括**：她一早就在盘算怎么把 Lord Zhangwei 那点"保护"从心里拔出去，结果一顿早饭被他拆成一场关于恐惧的谈话；她先是被他一句 "Fear keeps you safe" 撬开一条缝，接着抢先用极难听的话把他的好意砸回去，两人各自身上的面具裂了一次，随后在宫门前他又把话拉回来，只嘱咐她别出头。
- 改后：- **一句话概括**：她一早就在盘算怎么把 Lord Zhangwei 那点"保护"从心里拔出去，结果一顿早饭被他拆成一场关于恐惧的谈话；他一句 be afraid 反倒撬开她一条缝（one that pried a little of me apart），她当场承认 I am afraid，接着抢先用极难听的话把他的好意砸回去，两人各自身上的面具裂了一次，随后在宫门前他又把话拉回来，只嘱咐她别出头。

**ch10 chapter 10.md**
- 改前：**读者视角提示：** 这一句刚说完，她就把害怕承认了出来；本章后面她所有的狠话，都是在这个已经被听见的位置上说的。
- 改后：**读者视角提示：** 她先前已经把害怕承认了出来（那句 I am afraid 就在本句之前），这一句是他对那份承认的回应；本章后面她所有的狠话，都是在这个已经被听见的位置上说的。

**ch10 chapter 10.md**
- 改前：**为什么这样写：** 这一段口气近乎技术说明，句式短、条目清楚，和前面那些绕着的对白形成强烈反差。channeled 这个词把刑罚讲成一件需要人把力量引进来差使的东西——受刑者被排在施刑者的手上。After that would be 那种依次报上来的口气随后就有回声（"It whets the appetite."），刑罚在本章因此有了两副面孔：一种身体上的重，一种宫廷生活里的日常。
- 改后：**为什么这样写：** 这一段口气近乎技术说明，句式短、条目清楚，和前面那些绕着的对白形成强烈反差。channeled 这个词把刑罚讲成一件需要人把力量引进来差使的东西——受刑者被排在施刑者的手上。这种按轻重排下来的口气落在一场已有前文的对话里——更早他把刑罚直接排进日程（Such events are typically held before the afternoon meal. It whets the appetite.），此处再依次报一遍名目，刑罚在本章因此有了两副面孔：一种身体上的重，一种宫廷生活里的日常。

**ch12 chapter 12.md**
- 改前：**读者视角提示：** 这句是接在他的两句自嘲之后说的（You are one of the few who ask such things / Most think I feel no pain.）。她把「他也是会痛的」这件事说出口，而这正是她后面那句 weakness 的源头。
- 改后：**读者视角提示：** 这句是接在他的两句自嘲之后说的（You are one of the few who ask such things / Most think I feel no pain.）。她把「他也是会痛的」这件事说出口；而她在本章更早些时候给自己下的那道判词（for such weakness led to ruin）正是被这一句推翻的对象——先有禁令，后有这句「一样真」。

**ch12 chapter 12.md**
- 改前：**为什么这样写：** 段落以一个词的独句 Impossible. 开场，先给判决再补论证——她拒绝把那件事当成可讨论的对象。a brief interlude 借戏剧术语，a blink 借身体动作，两个尺度都在写「短」，且短的是他的时间而不是她的。最后一句是「拿王国去换心」这种交易句式，被保住的王国排在被让出的心之前；这个动词结构回收了她本章一直在做的事：用血、用陪伴、用结盟去换东西，而在这一笔上她拒付。
- 改后：**为什么这样写：** 段落以一个词的独句 Impossible. 开场，先给判决再补论证——她拒绝把那件事当成可讨论的对象。a brief interlude 借戏剧术语，a blink 借身体动作，两个尺度都在写「短」，且短的是他的时间而不是她的。最后一句是「拿王国去换心」这种交易句式，被保住的王国排在被让出的心之前；这个动词结构回收的是她一路在做的事——上一章她拿血相换，本章她给的是陪伴与结盟，而在这一笔上她拒付。

**ch15 chapter 15.md**
- 改前：- **一句话概括**：God of War（Lord Zhangwei）以「真实感情」为燃料的法术来夺她体内的 Divine Pearl Lotus；法术在她确认「不爱」的那一刻停摆，她反手以发簪破局、夺下他的剑，趁 Winged Devils 攻破宫殿之际乘 qilin 逃离。
- 改后：- **一句话概括**：God of War（Lord Zhangwei）以「真实感情」为燃料的法术来夺她体内的 Divine Pearl Lotus；法术先在半空停住，她把这一停认成自己不爱的证据，随后反手以发簪破局、夺下他的剑，趁 Winged Devils 攻破宫殿之际乘 qilin 逃离。

**ch15 chapter 15.md**
- 改前：- **线索进展**：① 抽取停在半空——the glittering trail of the lotus stilled in the air like time itself had frozen；② 只认主人的剑落在她手里而她没死；③ 她 regret 地丢下 the Shield of Rivers and Mountains（原文：left on the table），空手离殿；④ qilin 由追逐者变救者（The qilin who’d chased the God of War and me），心意始终未被言明；⑤ Winged Devils 破宫（the Winged De……
- 改后：- **线索进展**：① 抽取停在半空——the glittering trail of the lotus stilled in the air like time itself had frozen；② 只认主人的剑落在她手里而她没死；③ the Shield of Rivers and Mountains 始终 left on the table——她从未拿到它，只在离殿时回头看了一眼，regret 全在这一眼里；④ qilin 由追逐者变救者（The qilin who’d chased the God of War and me），心意始终未被言明；⑤ Winged Devils 破……

**ch15 chapter 15.md**
- 改前：**读者视角提示：** 这是本章的支点：法术停摆、发簪反击、剑认她为主，三件事全都挂在这一个否定式宣告上。
- 改后：**读者视角提示：** 这是本章的支点：法术停摆发生在她这一句之前，她给出的这个否定式解释才是此后两步——发簪反击、剑认她为主——的起点。

**ch15 chapter 15.md**
- 改前：以「真感情」为燃料的夺莲法术，卡死在她确认不爱的那一拍；她用发簪扳回一局，趁怪物破宫夺剑而去，乘 qilin 逃入云端——背叛清算完了，敌人的下一张帖也下了：他必来，而她等着。
- 改后：以「真感情」为燃料的夺莲法术在半空卡死，她随后把这一停认成自己不爱的证据；她用发簪扳回一局，夺下他的剑，趁怪物破宫之际乘 qilin 逃入云端——背叛清算完了，敌人的下一张帖也下了：他必来，而她等着。

**ch16 chapter 16.md**
- 改前：**为什么这样写：**她先立意志（I want to be here），再禁揣度（Don’t presume），后收职责、挂呈文——四个动作一层层把摄政提案拆干净。然后最后一句自曝方法：emulated 是「仿效」，她仿的是方才在同一座殿里压制过她的那位——权力的转移被压缩进一个动词：从伤害她的人那里借来腔调，用来守住自己的位置。
- 改后：**为什么这样写：**她先立意志（I want to be here），再禁揣度（Don’t presume），后收职责、挂呈文——四个动作一层层把摄政提案拆干净。然后最后一句自曝方法：emulated 是「仿效」，她仿的是先前那位女王对她说话时的腔调——权力的转移被压缩进一个动词：从伤害她的人那里借来腔调，用来守住自己的位置。

**ch17 chapter 17.md**
- 改前：**为什么这样写：** 三句按「禁止—理由—后果」递进，分号与 moreover 维持进谏辞令的板正节奏；viperous（毒蛇般）与 bootlickers（舔靴的奴才）两个贬义意象合成一处——蛇窝长在靴子上，是本朝最刻薄的一个画面。where nothing of worth gets done 把整段议论收在「能不能做事」上——Aunt Shou 的价值观始终是实用的，这也是她此前那句 Children shouldn’t be 一类拌嘴话底下真正的分量。
- 改后：**为什么这样写：** 三句按「禁止—理由—后果」递进，分号与 moreover 维持进谏辞令的板正节奏；viperous（毒蛇般）与 bootlickers（舔靴的奴才）两个贬义意象合成一处——蛇窝长在靴子上，是本朝最刻薄的一个画面。where nothing of worth gets done 把整段议论收在「能不能做事」上——Aunt Shou 的价值观始终是实用的，这也是方才那场拌嘴的底色——Children shouldn’t be held accountable 出自 Chengyin，Aunt Shou 当场顶回去一句 Children should respect thei……

**ch17 chapter 17.md**
- 改前：**读者视角提示：** 她刚说完，Aunt Shou 立刻把豪言翻译成手艺（We must keep the terms precise and clear），Chengyin 追问 Will giving up the lotus hurt you？——誓言迎来两道技术审问；本章给她的每一点锋芒都配一副账本。
- 改后：**读者视角提示：** 她那句誓言不是迎来而是答出两道技术审问：Chengyin 先追问 Will giving up the lotus hurt you，Aunt Shou 再把话头收进手艺（We must keep the terms precise and clear），她随后才把豪言说出口；本章给她的每一点锋芒都配一副账本。

**ch18 chapter 18.md**
- 改前：**为什么这样写：** A pause before he answered——本文特意标出他开口前的静默，停顿本身就是内容：这个问题他需要想一想才接。他不正面回答在乎与否，而是用她自己的判词回敬成三段论——你说我无心，原来你也一样。前面几个回合她刚冷笑 Why would anyone care for the God of War?，他当场把这句话说成呈堂证供。至于是不是真的无心，读者和她都听得出：两造的指控都不成立。
- 改后：**为什么这样写：** A pause before he answered——本文特意标出他开口前的静默，停顿本身就是内容：这个问题他需要想一想才接。他不正面回答在乎与否，而是用她自己的判词回敬成三段论——你说我无心，原来你也一样。他回敬的直接诱因是她紧邻的一句 Do you care?——至于那句 Why would anyone care for the God of War?，要等本块之后她才冷笑出口，他此刻还听不到。至于是不是真的无心，读者和她都听得出：两造的指控都不成立。

**ch19 chapter 19.md**
- 改前：- **场景·时间**：晚宴时分，Tianxia 的 dining hall。她带着 the God of War（她口中称 Lord Zhangwei）穿过一路侧目的宫人上殿；殿上最后只剩她与 Chengyin，末了战神起身与一名抱 lute 的乐伎合奏。
- 改后：- **场景·时间**：晚宴时分，Tianxia 的 dining hall。她带着 the God of War（她口中称 Lord Zhangwei）穿过一路侧目的宫人上殿；殿上到最后是她、Chengyin 与留在她身侧的战神三人，末了战神起身与一名抱 lute 的乐伎合奏。

**ch23 chapter 23.md**
- 改前：**为什么这样写：** shutter 本是窗板、闸板一类的东西，用作动词就是「啪地拉下」；作者选这个机械感的词，让「他收起表情」变成一个听得见声音的动作。`Of course` 是让步的说法，字面上同意、语气里全是不情愿；而他不提任何名字，只用 `your betrothed` 这个身份称呼——距离就是这么划出来的。她上一句刚说要通知 `Chengyin, Aunt Shou, the ministers`，他这一句接的是「你的婚约者」，两处是不是同一个人，本章没有写死。下一句她立刻接上 `His tone rankled`，并把他拉回公事：`“He’s also my First Advi……
- 改后：**为什么这样写：** shutter 本是窗板、闸板一类的东西，用作动词就是「啪地拉下」；作者选这个机械感的词，让「他收起表情」变成一个听得见声音的动作。`Of course` 是让步的说法，字面上同意、语气里全是不情愿；而他不提任何名字，只用 `your betrothed` 这个身份称呼——距离就是这么划出来的。本章已经把这两处钉成同一个人：她上一句点名的 `Chengyin`，就是他这一句口中的「你的婚约者」。下一句她立刻接上 `His tone rankled`，并把他拉回公事：`“He’s also my First Advisor,” I reminded him.` 两人用一个……

**ch24 chapter 24.md**
- 改前：- **一句话概括**：敌人为她体内的莲花而来；她为了不让族人死亡而把自己送上对方的条件，又在最后一刻把力量从自己身体里抽给那个护着她的人。
- 改后：- **一句话概括**：敌人为她体内的莲花而来；他们要她投降随行才肯放过族人，她假意周旋、迈步在即，被一道拦在中间的火焰打断——条件她始终没有接受；而在最后一刻，她把力量从自己身体里抽给那个护着她的人。

**ch24 chapter 24.md**
- 改前：**为什么这样写：** 这一句的情绪是双向的：前半是保护他，后半是心疼他「认领」了一个位置。`claiming a position he did not want` 的措辞极其克制——作者不写他表白、不写他牺牲，只写他当众把自己登记成一个身份。破折号前后的两个动作（我想藏他／他在自我暴露）互相抵消，于是她的无助被写成了两难。此前他只是一句 `Chengyin straightened. “Her betrothed.”`——三个字，没有一句解释，这一段的分析全部由叙述者承担。
- 改后：**为什么这样写：** 这一句的情绪是双向的：前半是保护他，后半是心疼他「认领」了一个位置。`claiming a position he did not want` 的措辞极其克制——作者不写他表白、不写他牺牲，只写他当众把自己登记成一个身份。破折号前后的两个动作（我想藏他／他在自我暴露）互相抵消，于是她的无助被写成了两难。此前他只是站直身子留下两个字——`Her betrothed.`，没有一句解释，这一段的分析全部由叙述者承担。

**ch25 chapter 25.md**
- 改前：**读者视角提示：** 说话人是 Captain Li，不是她。叙述者随后为这句辩驳记了功（Pride surged through me at her words），并补了一句 it was no easy thing to correct the God of War——本章把「君」写成被臣下提醒的那个人。
- 改后：**读者视角提示：** 说话人是 Captain Li，不是她。叙述者随后为这句辩驳记了功（Pride surged through me at her words），并补了一句 it was no easy thing to correct the God of War——被臣下纠正的那位是 the God of War 本人，本章的「君」是她，这句记的是 Captain Li 的胆量。

**ch27 chapter 27.md**
- 改前：- **一句话概括**：一位神扮成孩子试探她——她在自身未保时仍伸手去救、仍不肯对一个孩子撒谎，于是被按「你以为那是真的时，你怎么做了」称量了一次，并拿到一份护身的祝福。
- 改后：- **一句话概括**：水中的孩子与林中的白兽事后被点明是一场 illusion——the Ancient Grandmaster 布下的试探；她在自身未保时仍伸手去救、仍不肯对一个孩子撒谎，于是被按「你以为那是真的时，你怎么做了」称量了一次，并拿到一份护身的祝福。

**ch29 chapter 29.md**
- 改前：**为什么这样写：** 与本章早些时候穿墙那一段对照：那时他们出来时身上不剩一粒灰，此刻他的力量却成了信号。beacon 一个词把「他在护她」与「他在暴露她」焊死在同一件事上——他越强，她越危险。those hunting us 用的是 us：追兵是冲着她来的，这一点他到此刻仍说成「我们」。对白全是无连接词的短句，和段落层的长句不同步，读者因此听出他在硬撑。
- 改后：**为什么这样写：** 与本章早些时候穿墙那一段对照：那时他们出来时身上不剩一粒灰，此刻他的力量却成了信号。beacon 一个词把「他在护她」与「他在暴露她」焊死在同一件事上——他越强，她越危险。those hunting us 这个 us 出自她的叙述，不是他的台词——他嘴里全是 you must go、they’ll come soon；追兵明明只冲她而来，落到她笔下一切仍旧是「我们」。对白全是无连接词的短句，和段落层的长句不同步，读者因此听出他在硬撑。

**ch30 chapter 30.md**
- 改前：- **线索进展**：① lotus 因她自愿让出而转移到 Zhangwei 身上，她此后体内空了一处，也变得可以被追上；② 他得力量后气息变强，两人之间多出一条新的联结；③ 最强的 the Wuxin 能偷别人的形，本章末尾制住她的正是这样一个；④ 她手里那把剑被认出是 the God of War 的 companion blade，连她自己也不知道为什么在他手上；⑤ Zhangwei 提过她的士兵就在附近，她也想到要去警告他们；本章结束时，这条路她还没走到。
- 改后：- **线索进展**：① lotus 因她自愿让出而转移到 Zhangwei 身上，她此后体内空了一处，也变得可以被追上；② 他得力量后气息变强，两人之间多出一条新的联结；③ 最强的 the Wuxin 能偷别人的形，本章末尾制住她的正是这样一个；④ 她手里那把剑被认出是 the God of War 的 companion blade，对方追问她从何得来，而她心里问的是他为何把剑交到自己手上；⑤ Zhangwei 提过她的士兵就在附近，她也想到要去警告他们；本章结束时，这条路她还没走到。

**ch31 chapter 31.md**
- 改前：> **原句 1:** "Anger was good; it helped me forget my fear and misery, the very thing these creatures thrived on."
- 改后：> **原句 1:** "My hands balled into fists. Anger was good; it helped me forget my fear and misery, the very thing these creatures thrived on. When I lunged at him, he shoved me aside with brutal force, his hand ice-cold. I fell against the wall, fighting the tears that threatened."

**ch31 chapter 31.md**
- 改前：**中文理解：** 冒名的对方推进囚室，她扑上去被一把甩开，撞在墙上强忍眼泪。下一句她立刻换了姿态：愤怒是好事，因为它盖掉了恐惧和痛苦——而这些东西正是这类生物赖以生存的食物。
- 改后：**中文理解：** 她攥紧拳头给自己定调：愤怒是好事，因为它盖掉了恐惧和痛苦——而这些东西正是这类生物赖以生存的食物。随后她扑上去，被一把甩开，他的手冷得像冰；她撞在墙上，强忍住快要涌上来的眼泪。

**ch31 chapter 31.md**
- 改前：**关键词：** anger · fear · misery · thrived
- 改后：**关键词：** balled into fists · anger · fear · misery · thrived · shoved me aside · fighting the tears

**ch31 chapter 31.md**
- 改前：**读者视角提示：** 读者先看到她的手在抖，再看到她在挑情绪用，于是期待她后面靠这份冷静周旋，而不是硬碰硬。
- 改后：**读者视角提示：** 读者先看到她攥紧的拳头，再看到她在挑情绪用，于是期待她后面靠这份冷静周旋，而不是硬碰硬。

**ch31 chapter 31.md**
- 改前：**中文理解：** 对方说 Chengyin 早就学会了藏自己的记忆，而他连脸上那道疤都注意到了。她紧跟着认下 Zhangwei had been right 这句判断——是自己只看想看的，才漏掉了那些迹象。
- 改后：**中文理解：** 前一句对方刚说 Chengyin 早就学会了藏自己的记忆，还自认漏看了那道疤（I was remiss to overlook the scar）——是他漏看，不是他看出。她紧跟着认下 Zhangwei had been right 这句判断：是自己只看想看的，才漏掉了那些迹象。

**ch35 chapter 35.md**
- 改前：- **场景·时间**：temple 里的池塘边——她一个人对着水面上的两个倒影；后半段从码头乘一小船回宫殿，同船的是 Aunt Shou。全章是一次连续行程：先看完两场镜中所见，再听完一船对白。她脚下这座 temple 在本章始终只写作 temple——没有一个字交代它落在哪一界，也没有说它是不是对白里提到的那座 Temple of the Crimson Moon（Aunt Shou 那句是「Not in the Temple of the Crimson Moon」，说的是另一件事）。
- 改后：- **场景·时间**：temple 里的池塘边——她一个人对着水面上的两个倒影；后半段从码头乘一小船回宫殿，同船的是 Aunt Shou。全章是一次连续行程：先看完两场镜中所见，再听完一船对白。她脚下这座 temple 在本章始终只写作 temple——没有一个字交代它落在哪一界；不过 Aunt Shou 回她「There was no taint in the pond」那句时说「Not in the Temple of the Crimson Moon」，等于当面替这座 temple 报了名，只是行文仍不点名。

**ch35 chapter 35.md**
- 改前：> **原句 8:** "I was Queen Caihong’s daughter, the only one who had a chance of lifting the enchantment crafted with her magic—the one that ran in my veins."
- 改后：> **原句 8:** "But it wasn’t my mortal heritage they wanted. I was Queen Caihong’s daughter, the only one who had a chance of lifting the enchantment crafted with her magic—the one that ran in my veins. And they would never let me go, not until I’d done what they wanted."

**ch41 chapter 41.md**
- 改前：- **叙事手法**：第一人称限知，信息几乎全部藏在"压低声音的对白"里——muttered through clenched teeth 这类耳语承担推进；她嘴上应答、心里评估 Lin 的忠诚，说出的话与盘算之间始终错开一拍；章末以一句独立成段的自我剖白收束，不作解释。
- 改后：- **叙事手法**：第一人称限知，信息几乎全部藏在"压低声音的对白"里——muttered through clenched teeth 这类耳语承担推进；她嘴上应答、心里评估 Lin 的忠诚，说出的话与盘算之间始终错开一拍；章中有一句独立成段的自我剖白，不作解释，其后才接上 Dalian 的宣告与章末那场风暴。

**ch42 chapter 42.md**
- 改前：- **线索进展**：① Lord Dalian 求娶之意，据他说是起于其母（Aunt Shou）昔日对她的推崇；② Aunt Shou 的女儿、Dalian 的妹妹（本章只以"his sister""my daughter"称之、未提其名）死于 Queen Caihong 麾下兵士的突袭，Dalian 从那日起 learned to hate；③ gateway 非靠她不能开启——她若跳水入 Wangchuan，Dalian 便开不了它，这是她本章自陈的筹码；④ 她向 Aunt Shou 讨一句护 Chengyin 周全的承诺，Aunt Shou 却回探她是否真会开 gateway——两人各……
- 改后：- **线索进展**：① Lord Dalian 求娶之意，据他说是起于其母（Aunt Shou）昔日对她的推崇；② Aunt Shou 的女儿、Dalian 的妹妹（本章只以"his sister""my daughter"称之、未提其名）死于 Queen Caihong 麾下兵士的突袭，Dalian 从那日起 learned to hate；③ gateway 非靠她不能开启——她若跳水入 Wangchuan，Dalian 便开不了它，这是她本章自陈的筹码；④ 她向 Aunt Shou 讨一句护 Chengyin 周全的承诺，Aunt Shou 却回探她是否真会开 gateway——她这一……

**ch42 chapter 42.md**
- 改前：一条河的两岸此刻都站满了要她撒谎的人——她对 Lord Dalian 虚与委蛇、对 Aunt Shou 层层试探，一边不肯以身殉国、一边又逼自己活下去争那一点转机；到头来连那位口称关心她的旧长辈，也只剩用一句假承诺与她彼此停战。
- 改后：一条河的两岸此刻都站满了要她撒谎的人——她对 Lord Dalian 虚与委蛇、对 Aunt Shou 层层试探，一边不肯以身殉国、一边又逼自己活下去争那一点转机；到头来连那位口称关心她的旧长辈，也只是点点头与她彼此停战——她这一边的假承诺由自己点破，对方那一边的猜测原文始终没有替她落实。

**ch43 chapter 43.md**
- 改前：**读者视角提示：** 这个念头之所以成立，靠的是前一段刚立好的规矩：gateway 不吃魔法，那就给它一样属于它自己的东西。读者手里已经握着答案，只是比她早不了几秒。
- 改后：**读者视角提示：** 这个念头之所以成立，靠的是紧随其后的那一段当场把规矩试出来：水不挪、灯不灭——gateway 不吃魔法，那就给它一样属于它自己的东西。读者与她几乎是同时拿到这条前提的，谁也没比谁早几步。

**ch45 chapter 45.md**
- 改前：**为什么这样写：** How heavy my heart was 是没有谓语的感叹残句，插在台词与判断之间，像一个没说完的呼吸。We had won, yet lost so much 用 yet 把胜利与损失压进同一格；助动词 had 只写了一次，lost 共用它，于是整场战争的赢与亏被收进同一时态，本章此后所有关于「回去」的商量都在这半句的阴影里进行。
- 改后：**为什么这样写：** How heavy my heart was 是 how 引导的感叹句，主语 my heart 与系动词 was 俱在，只因 heavy 被 how 提前，读起来才像半口气；它插在台词与判断之间，像一个没说完的呼吸。We had won, yet lost so much 用 yet 把胜利与损失压进同一格；助动词 had 只写了一次，lost 共用它，于是整场战争的赢与亏被收进同一时态，本章此后所有关于「回去」的商量都在这半句的阴影里进行。

**ch46 chapter 46.md**
- 改前：- **线索进展**：① 她记起了 Golden Desert 与母亲，但本章两处自问这场相见是否真实（or was it because this wasn’t real?、Is this a dream?），母亲的回答只把判断交回她心里；② 母亲承认当初随她下去是自私的决定，且多年找不到人；③ 「本可以让 Wuxin 被毁灭而不折一名 immortal」的抉择被摊开，回答是 I am proud of you；④ 父亲只出现在母亲的假设句里（if I had your father back）与她的追问里（not avenging Father），本章未写其结局细节；⑤ 回家的条件是重新与……
- 改后：- **线索进展**：① 她记起了 Golden Desert 与母亲，但本章两处自问这场相见是否真实（or was it because this wasn’t real?、Is this a dream?），母亲的回答只把判断交回她心里；② 母亲把当年那一层动机称作自私的决定（It was a selfish decision），并说多年找不到她、以为她已失于彼界——本章没有写母亲随她下去，反倒写明她当时不在身边；③ 「本可以让 Wuxin 被毁灭而不折一名 immortal」的抉择被摊开，回答是 I am proud of you；④ 父亲只出现在母亲的假设句里（if I had you……

## 五、e 步：总览层事实核对（本会话执行；委派的只读代理触 150 轮上限失败、无可采信产出）

**阻断型 12 处，全部行级 edit**（总览三篇 12 ＋ ch43 同步 4 处措辞；引语层未动）。这一层是六道门禁**结构上查不到**的：a 步已写明 `check_overview_full` B 段只管「命中章 == 标注章」，对事件、时序、说话人、人物关系零覆盖。

### 00_概述.md（9 处）
1. 「Liyen 误饮了 Netherworld 的 Wangchuan 河水…祖父以欺神之罪当场被问斩，火随后从她的家烧起」→ 按 text/ 重排：ch01 由占卜者点出要解的是 Wangchuan 之水；问罪队伍压进门来、她的家已在火中；祖父跪在殿前把罪认到自己身上，却在 Queen Caihong 面前心脏病发、当场死掉；ch02 她自己把「神杀了他」推翻一半（他们并没有杀他）。
2. 同段补：那只把手伸向莲花之外、给水的那一位是谁，到 ch33 才由 Aunt Shou 摊开——ch01 原文不含此信息，不得前置。
3. 「四名 immortal 士兵……死在 Zhangwei 织起的网里成四具焦尸」→ 网接住的是遗骸：四人坠到眼前时已是焦尸，没有一个被救回；Lieutenant Yang 在内；判定这禁术出自 Wuxin 的是 Zhangwei。
4. 「她与 Zhangwei 都不肯忘，她便以 ruler of the Netherworld 的身份替两人求得」→ 两个「她」指代不同的人，显名为 Liyen／Aunt Shou，并补「向船夫求得」。
5. 「醒来之后她独自坐朝」→ ch47 开场是她夜里独自坐在书案边，等一个回天上一个多月没有消息的人；翌日临朝才有那次当众求娶。
6. 主题二「祖父教给她的不是诚实，是一条分类」→ 拆开陈述：ch01 病榻边的原话落点是「你选择说出的那些谎，会定义你的品性」，而 `lies of necessity / of malice` 那条分类是 ch07 她自己立的行为准则。
7. Aunt Shou 弧「作者不给她任何一次辩解：投毒、劝嫁、丧子、掌权」→ ch33 她自己把话说得很多（承认投毒、把「放出 Winged Devils 追她」辩回去、摊开自己是 Dalian 与 Damei 的母亲），而接领袖之位的理由在 ch45；叙述层不替读者判定这些理由真伪；「劝嫁」原文无支撑，删。
8. 「船夫的价目表要求她把两世的记忆分开付账」→ 价目表写的是一整套记忆；最后是她自己不肯付、而身边那些人各饮一口替她把这笔账分摊开。
9. 「用 gateway 自己的法术炸开缺口，与 Aunt Shou 合力把 Chengyin 从裂口送走」→ 藤蔓触发的是拱门自己的法术吞掉最靠近拱门的那一排士兵（她要的那一瞬空档，`I needed to create a diversion`）；Chengyin 由 Aunt Shou 召起的风托着、从 gateway 上那道窄缝被送走，她自己的力量与对方的合在一处结成屏障。

### 00_金句精选.md（1 处）
10. ② 的上下文「祖父因偷莲被斩」→ 认罪后在女王面前心脏病发当场死去、她的家正在烧。

### 00_情感节点.md（2 处）
11. 节点九「是他们两人共同算过的一步」→ 指代含混（可误读成 Zhangwei＋Queen Caihong 两人）；明写是她与 Zhangwei 在她还是 immortal 时共同定下的方案。同处把「我真希望你从一开始就把真相告诉我」按原文时序放回他那段解释**之前**（原文：她先说这句，他才解释不能提前透露）。
12. 节点十「借 gateway 自己的法术炸开缺口」→ 同第 9 条。

### ch43 chapter 43.md（同步 4 处，非新增缺陷）
一句话概括「炸开一个空档」→「触发 gateway 自己的法术吞掉……换来一瞬空档」；线索 ①「可用的破口」→「可用的机关」；线索 ⑥ 补「Aunt Shou 召起一阵风」、「裂口」→「拱门上那道窄缝」；一句话总结「用一根藤蔓炸开缺口」→「换来一瞬空档」。

### 复核为「不是缺陷」的两条（如实登记，避免下轮改坏）
- 「投毒」确实归 Aunt Shou（这话是 Liyen 在 ch36 说的，逐字：`She did it to force my grandfather’s hand into giving me the lotus.`；投毒的正面摊牌在 ch33）——审查中途我曾把它列为凭空，撤回。
- shield「被她留在了桌上」成立（ch15 原文 `left on the table`），与 d 步 ch15 的整改不冲突。

### 全域／序数断言的处理
「全书唯一／每一次／只此一处／最完整」这类断言一律改成可核的具体陈述（本轮 8 处＋概述若干），因为它们无法被任何门禁证伪。

## 六、复验（整改后重跑，与 a 步基线一致）

corruption_scan FAIL 0 ｜ verify_quotes 400/400 ｜ sweep_full 376／跨章 0／查无 0 ｜ check_vocab 1406 行 FAIL 0 ｜ check_entities 未知实体 0 ｜ verify_overview_quotes 58/58 ｜ check_overview_full A 87、B 86 对＋1 歧义、C 2、E 0 ｜ check_xref_indep **192 处引用／0 报警**（cd 步为 187，+5 全部来自 e 步改写时补进的章号标注，报警数 0 未变）｜ check_analysis_indep 835 片段全命中 ｜ check_chapter_quotes 43 章 100% ｜ 总览层第二实现 177 片段 flat 查无 0（cd 步那次 222 条，差在切分口径不在内容，两次结论一致）。

原始逐行输出：`.memory/raw-gates/immortal-by-sue-lynn-tan/review_{a,cd,e}_2026-10-06.txt`

## 七、局限如实标注

- 语义终判（d/e 两步的人判）由**同一会话**做出，写作上下文无法对冲；子代理只读、不带写作记忆，其报警我已逐条按三档分类复核，其中 2 条我自己的报警被证伪并撤回（见 e 步末）。
- 提示型 51 条**只记不改**：包括 check_overview_full 的 3 条章节标注歧义（骰子句 ch01/ch04 双现，正文已写明出处）、check_vocab 基础档 ≥9 字符启发式若干、章内中文理解人称「她/我」混用（完工条目登记 106 处，属风格层非事实层）。
- 本书另有既存风险：叙述者名 `Liyen` 在 27 个章的 `text/` 里一次都没出现——凡 md 里出现她的名字而该章无支撑即为凭空指名，本轮已按此逐章复查，未发现新增。
