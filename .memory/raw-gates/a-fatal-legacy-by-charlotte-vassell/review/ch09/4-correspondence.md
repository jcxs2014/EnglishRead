# 4-correspondence.md · ch09 逐块对应（R4 人判）

判问只有一个：**这段中文是不是在讲这句引语？** 外加固定三问：① 每个动词的主语是谁 ② 宾语/受事是谁 ③ 「谁的／谁欠谁／谁问的」回原文看 `by`/`to`/`from`/`of` 定方向。
档：**对应** / **引语选短**（讲的是引语之外的上下文→退回 §2① 选引语） / **不对应**（讲全书主旨或作者生平） / **密度不足**（只复述字面、没有「为什么这样写」）。

机器层先跑：`2-machine.json`（`chapter.sh` exit 0，`verdict: ok`，7/7 引语逐字、7 块、子项 4 项、密度全过）。本表只处理机器结构上查不了的五类：漏／对应／说话人／施事归属／事实断言。

| 块 | 引语落点（text 逐字起止） | 讲的是不是这句引语？ | ① 主语 ② 受事 ③ 归属 | 密度（有无「为什么这样写」） | 结论 |
|---|---|---|---|---|---|
| **原句 1** | `text:59` [1831,1953] `Caius put his tea on his desk and then, picking up a marker pen, wrote two words on a whiteboard. ‘Money or sex,’ he said.` | 是。「中文理解」逐句复述的就是这一句：放茶→拿马克笔→写两词→说出 Money or sex | ① 主语＝凯厄斯（原文 `Caius … wrote two words … he said`）✅ ② 受事＝白板／两词 ✅ ③ 归属：两词是**凯厄斯亲笔**，md 未误给艾米 ✅ | 有：把「推理被写出来而不是想出来」「白板把猜想压成两个选项」「实物动作先于判断」讲成结构选择 | **对应** |
| **原句 2** | `text:65` [1971,2367] `‘Money.’ He drew arrows coming off the word and started writing keywords as they spoke. ‘We need to look into Digby’s personal finances…’` | 是。md 的中文理解就是这段「钱」的自陈：圈定钱→拉箭头→边说边写关键词→怀疑银行→单人公寓→骗局不成比例 | ① 主语＝他＝**凯厄斯**（原文 `He drew arrows…`，前一句 `‘Money.’` 是他对 `‘Which one?’` 的回答）✅ ② 受事＝「钱」这一支的关键词 ✅ ③ 归属：「提出者自己拆自己的假设」——拆的是凯厄斯自己刚立的「钱」，md 归属正确 ✅ | 有：「先立论再自驳」是白板推理的做法，且明说读者由此看得出哪块是虚的 | **对应** |
| **原句 3** | `text:74` [2732,2837] `‘It’s worth a bomb.’ Amy stared at the whiteboard. ‘I wonder who inherits the Institute with Digby gone?’` | 是。中文理解＝「值一大笔钱」＋「谁继承」，正是这一句的两段 | ① 主语＝**艾米**（原文 `Amy stared at the whiteboard.`）✅ ② 受事＝那栋楼／继承问题 ✅ ③ 归属：「方向的转换由另一个人给出，而不是由原提出者自己转向」——提出者是艾米，与原文一致（提白板两词的是凯厄斯，此处转向者是艾米）✅ | 有：把「案子的重心从死者移向活着且可能受益的人」讲成动机结构的转移 | **对应** |
| **原句 4** | `text:77` [2840,2913] `‘That’s a good question,’ Caius said, writing it down. ‘Sex as a motive.’` | 是。中文理解＝「问得好」＋「记在白板上」＋「把性作为动机」，正是这一句的三拍 | ① 主语＝**凯厄斯**（原文 `Caius said, writing it down`）✅ ② 受事＝「这个问题」（被写下的内容是继承问题本身，不是答案）✅ ③ 归属：`writing it down` 的宾语＝艾米刚提的继承问题，md 写作「一边把它记在白板上」✅；「谁提出、谁反驳、谁沉默」的形状描述与原文轮次一致 ✅ | 有：「被记下却不作答的沉默，与被写上去的转向并排出现在同一句里」——这是本章专属判据要求的「谁沉默」答案 | **对应** |
| **原句 5** | `text:83` [2928,3123] `‘Yes. Solitary Digby, who refuses to deal with any technology developed in the last fifty years, puts a lonely-hearts ad in a magazine. Meets a woman who appears to be tailor-made called Isolde.’` | 是。中文理解＝「是」＋孤僻反技术＋杂志征友＋量身定做的伊索尔德 | ① 主语＝他＝**凯厄斯**（原文 `‘Yes.’` 是他对艾米 `‘Isolde?’` 的回答，见 `text:80`）✅ ② 受事＝迪吉／伊索尔德 ✅ ③ 归属：「量身定做」是凯厄斯的判断 ✅ | 有：「量身定做是全段的判断核心——陌生人恰好符合你所有偏好，本身就是可疑之处」 | **对应** |
| **原句 6** | `text:116` [4166,4301] `‘Forensics are done with the letters from Isolde. No fingerprints. The envelopes weren’t licked. No trace of the person who sent them.’` | 是。中文理解＝法证查完来信：没指纹／没舔封／没痕迹，三项否定一一对应 | ① 主语＝中文用被动「法证那边把来信查完了」，未指认个人 ✅ ② 受事＝伊索尔德的来信 ✅ ③ 归属：原文这句是**艾米接完电话后转述**（`Amy’s desk phone rang… She hung up.`），md 未把结论算到法证/任何人头上，也没有误安给凯厄斯 ✅ | 有：「三句短促的否定排成一列，把『写信人』这个位置彻底清空」「写得太干净的信本身是一种不自然」 | **对应** |
| **原句 7** | `text:177` [6044,6104] `‘She’s suggesting it but letting him think it was his idea.’` | **不是——这段中文讲的是别人说这句话的那个判断，而它被安在了错的人身上**。md 的「中文理解」写 `艾米说：她是在暗示，但让迪吉以为这是他自己想出来的。`，「为什么这样写」又写 `艾米读信时抓到的是一个手法而不是一个事实` | ① 主语＝md 记为「艾米」；原文该句的说话人是**凯厄斯** ❌ ② 受事＝伊索尔德/迪吉 ✅ ③ 归属：轮次 `text:174` 艾米举证信件原文 → `text:177` 凯厄斯作推断 → `text:180` `‘Yeah. Why there and not a restaurant?’` 艾米以「Yeah」附议上一句 → `text:183` 凯厄斯 → `text:186` 艾米以「Exactly」附议凯厄斯。若 177 归艾米，则 180 的「Yeah」成了艾米附议自己 ❌ | 有（密度不是问题）：`抓到的不是一个事实而是一个手法` 是有效的「为什么这样写」 | **不对应（施事/说话人反转）** → 见 `3-diff.md` E1（阻断）。附带：`伊索尔德从不直接要求见面` 与原文不符（原文只说她不指定在 Institute 见，且明说 very keen to meet face to face）→ `3-diff.md` F5（阻断） |

## 对应组小结

- 块数 **7**；**对应 6 / 不对应 1**（原句 7）；引语选短 0；密度不足 0；讲错章 0。
- 施事三问逐块复核：主语错 **1 处**（原句 7）；受事错 0；归属方向错 0（原句 3、4 的「谁提出、谁写、谁沉默」方向与原文完全一致）。
- 引语逐字：7/7 全串命中（自建全串比对，非只看前 90 字），另有 3 条词汇例句非逐字（见 `3-diff.md` F3/F4/F6）。
