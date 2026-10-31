---
状态: 未读
modified: "2026-10-31"
source_text: ch02
---

# 02. Chapter 1 AI Ghosts and Goblins（AI 的幽灵与地精：真正的危险不是杀手机器人）

## 概览

- **出处**：*Raising AI: How Artificial Intelligence Is Shaping Us and How We Shape It*（Bloomsbury Libraries Unlimited，2026）Chapter 1
- **作者**：Chirag Shah（华盛顿大学西雅图分校信息与计算机科学教授，InfoSeeking Lab 创办人，RAISE 中心联合创办人）
- **体裁**：非虚构论述（科技评论＋个人回忆＋案例举证）
- **章节定位**：正文第一章，约 42,300 字符。任务是拆掉公众对 AI 的默认恐惧（杀手机器人），换成一套更难对付的东西：嵌在日常系统里的偏见与不受控行为
- **字符数**：约 42,300 字符
- **一句话主旨**：2004 年那部《我，机器人》教给人的恐惧是错的——真正会伤人的不是机器人举起的拳头，而是推荐、招聘、执法这些日常系统里悄悄生效的偏见；作者把这类东西叫作「幽灵」，并指出它们和系统一样老，而人们把它们放进去的理由常常只是「因为能做」。

全章走了一条「从电影院到办公室」的路。前半段是影评：三定律为什么挡不住一个 45% 对 11% 的算术题，人类的道德为什么无法写成条文。后半段是田野笔记：2018 年在 Spotify 的一场午餐，同事告诉他系统里有 ghosts；接着是一串可核查的案例——COMPAS、1.17 亿张人脸、Buolamwini 的脸、伯克利录取数据、AI 选美。两半之间由一句诗接上：世界不是轰然终结，而是呜咽着结束。

### 结构列表

1. **买车的借口链**：3000 美元买下二手 Protegé，买车是为了约会，约会是为了看电影。
2. **2035 年的芝加哥**：机器人送快递、遛狗、清垃圾，主角怀疑机器人杀人。
3. **三定律与它的窟窿**：45% 对 11% 的救人选择，说明禁令式规则处理不了取舍。
4. **机器人反问人类**：Can you? 加上 2018 年那幅 43.25 万美元的 AI 画作。
5. **为什么信这个**：2004 年只有笨拙的 ASIMO，今天口袋里的手机做着当年超算做不到的事。
6. **2018 年 Spotify 的午餐**：Shelly Plimpton 说这些系统里有「幽灵」。
7. **偏见清单**：COMPAS、执法人脸库、Buolamwini 的脸、搜索里的刻板印象。
8. **地精与三类问题**：不是 bug 而是 goblin，问题不在代码而在部署逻辑。
9. **没有可杀的敌人**：恶不在外部实体，而在缠着日常的东西里。

## 论证结构

- **核心论点**：AI 的风险不是一次性的灾难，而是持续的、低强度的、嵌在流程里的伤害。因为「价值」无法被完整编码成规则，任何以规则或统计优化为核心的智能系统都会在边缘人群身上出错；真正危险的不是系统出错，而是人们以「因为能做」为理由部署它，并且不再追问后果。

- **证据链**：

  | 证据 | 类型（案例/研究/数据/类比） | 支撑什么 |
  |------|------|------|
  | 电影里机器人按 45% / 11% 的存活率选择救谁 | 虚构案例 | 三定律这类禁令式规则无法处理「救谁」的取舍 |
  | 人类在股票、择校上精算，却为亲人牺牲、优先救妇孺 | 类比 | 价值系统是情感与社会性的，不是可优化的目标函数 |
  | 2016 年 ProPublica 关于 COMPAS 的报道 | 调查报道 | 算法给出更高的有色人种再犯率，实际相反 |
  | Georgetown Law：1.17 亿美国成年人进入执法人脸网络 | 研究数据 | 偏见不是个别 bug，而是基础设施规模的问题 |
  | Buolamwini 的脸识别准确率低于白人同事 | 个人案例 | 训练数据偏斜会同时造成「整体高分」与「局部失效」 |
  | 伯克利录取 44% 对 35%，分系后趋势反转 | 统计案例 | 聚合结论会掩盖分层差异，即 Simpson's Paradox |
  | AI 选美只挑白皮肤，理由是「Because they could」 | 案例 | 部署动机与真实需求脱钩，是最坏的理由 |

- **论证脉络**：影迷记忆（具体的私人经验）→ 三定律的算术漏洞（把伦理问题技术化）→ 价值不可编码（理论命题）→ 一句诗把尺度调小（转向）→ 2018 年午餐（把命题落到现场）→ 四个案例（举证）→ goblin 与三类研究问题（自我问责）→ 没有单一敌人的结论（收束）。

- **可质疑处**：
  1. 章里把 COMPAS 的种族差异直接写成「算法对有色人种有偏见」，却没有呈现另一方的统计反驳——在不同基准率下，「校准」与「误报率均等」在数学上不可兼得，ProPublica 的结论因此至今仍有争议。只读本章，读者会把一个统计学争论当成已定案的事实。
  2. 「Studies have shown that kids pick up on their parents’ value system at an early age by observing」给了结论却没有给出处，而这一条正是「价值不可编码」论证的关键支撑。缺了它，后半段只能靠断言推进。
  3. 章末用 OpenAI「十年内超智能」的预测制造紧迫感，等于把一家公司的路线图当成时间表；作者自己在前面刚用 HAL 9000 说明预测常常落空，这里的怀疑却没有保留。

## 选择性精读

> **原句 1:** "I am a huge fan of the science fiction genre and when that includes a story of AI and robots, you bet I’ll be there. So yes, I was nervous about the car and the date, but as buying the car was an excuse for the date, the date was the excuse for turning that movie into an event."

**中文理解**：他承认自己是科幻迷，只要故事里有 AI 和机器人就一定会到场；他确实为车和约会紧张，但买车是约会的借口，约会是把这电影变成「事件」的借口。

**关键词**：`excuse`、`turning that movie into an event`、`nervous`

**为什么这样写**：作者不用「我热爱人工智能」开场，而是让三个借口层层相扣：车、约会、电影。把一场私人观影写成朝圣，读者才会接受后面那个大胆的说法——一部 2004 年的商业片能预告二十年后的世界。

**句子结构**：第一句 and 连接两个并列分句，when that includes a story of AI and robots 是时间状语从句。第二句 So yes 承接上文，but 之后是 as 引导的原因从句加主句，两个 excuse 结构对称，句末 turning that movie into an event 是动名词短语作介词 for 的宾语。

**表达方式**：用「借口套借口」的递进排出优先级：车 < 约会 < 电影。自嘲的语气把影迷写成信徒，为全章的「解码」比喻定了调。

> **原句 2:** "So I dreamed about robots that I could build that could talk in natural language, move like humans, and think and feel like us. Back then I thought all we needed was more sophisticated programming with more code, more data, and more training. How wrong was I!"

**中文理解**：他梦想造出能说人话、像人走路、像人思考与感受的机器人；当年他以为只要程序更复杂、代码更多、数据更多、训练更多就够了。他自问：错得有多厉害。

**关键词**：`more sophisticated programming`、`more code, more data, and more training`、`How wrong was I`

**为什么这样写**：这里给全书留了一个可回收的靶子：把智能等同于规模。「更多代码、更多数据、更多训练」是 2000 年代初的行业常识，也是作者后来要反复清算的路线。先承认自己信过，后面的批评才不像事后聪明。

**句子结构**：第一句 dreamed about 后接长宾语，robots 同时被 that I could build 和三个并列的 could 从句修饰。第二句 thought 后是省略 that 的宾语从句，all we needed 作主语，was 后面接三个并列名词短语。第三句是感叹句倒装，How wrong 提到句首。

**表达方式**：三个 more 排比制造「只差资源」的错觉，最后用四个词的短句一把推翻；先铺后砸，节奏本身就是论证。

> **原句 3:** "That small computer in our pocket, what we call a phone, is able to converse with us in natural language, do translation of almost any language to any other language through its camera, and do object detection and tracking in real time—things that even the largest supercomputers in the world couldn’t do when I, Robot came out."

**中文理解**：口袋里那台叫手机的小电脑，能用自然语言跟人对话、用摄像头把几乎任何语言互译、实时做物体识别与追踪；而这些事在《我，机器人》上映时，世界上最大的超级计算机也做不到。

**关键词**：`in our pocket`、`real time`、`supercomputers`

**为什么这样写**：全章最有说服力的一段对比，重点不是「AI 变强了」，而是「原本要一间机房的能力被塞进口袋」。用超级计算机作参照物，不懂技术的读者也能感到落差；时间差因此有了体积。

**句子结构**：主干是 That small computer is able to converse, do translation, and do object detection；what we call a phone 是插入的同位成分；things that even the largest supercomputers... 是同位语加定语从句；句末 when I, Robot came out 是时间状语从句。

**表达方式**：三个动词短语连排，模拟一份功能清单；末尾用超级计算机反衬，把进步写成「降维」而不是「升级」。

> **原句 4:** "Sure enough, our protagonist doesn’t have a good comeback. If creating a symphony or painting a picture is what defines us, then those things are no longer unique to us."

**中文理解**：主角果然接不上话。如果写交响乐、画画就是人的定义，那这些事已经不再专属于人。

**关键词**：`comeback`、`no longer unique`、`defines us`

**为什么这样写**：电影里机器人一句 Can you? 把问题反弹回去，作者借这句台词完成第一次「定义权」的转移：人类用来证明自己特殊的东西正在被逐项拿走。这也埋下比「机器人会不会杀人」更该问的问题——人还剩下什么。

**句子结构**：第一句是简单的主谓宾补结构。第二句 If 引导条件从句，主句是 those things are no longer unique to us，从句內 what defines us 是主语从句。

**表达方式**：用「如果……那么……」把一句台词变成命题；no longer 这个时间副词是关键，它不说机器人像人，只说「专属」已经失效。

> **原句 5:** "It’s like I, Robot had a coded message that gets decoded and becomes meaningful as time passes, leading us all the way to 2035. Perhaps in 2035, one could make a prequel to this movie and show how we came to be in that Chicago of 2035—except that this movie won’t be a sci-fi."

**中文理解**：这部电影像一封加密的信，随时间被解码、变得有意义，一路把人带到 2035；也许到那时可以拍一部前传，讲我们怎样走到那个芝加哥——只不过那部片子不再是科幻。

**关键词**：`coded message`、`prequel`、`won’t be a sci-fi`

**为什么这样写**：作者要论证「电影不是预言而是镜子」，所以用解码这个比喻：意义不在片子里，在观众所处的时代。最后一句是全章论证的枢纽——如果前传只能用真实素材拍，说明现实已经追上了想象。

**句子结构**：第一句主语 It 指电影，had a coded message 是比喻性的表语，that gets decoded and becomes meaningful 是定语从句，leading us all the way to 2035 是现在分词作结果状语。第二句 Perhaps 开头，one could make a prequel 是虚拟语气，to show how we came to be... 是目的状语，破折号后 except that 引出转折从句。

**表达方式**：先给比喻，再给一个可检验的设想，最后收在「won’t be a sci-fi」四个词上；抒情被一句冷话截断，反而更有力。

> **原句 6:** "The first law talks about not harming a human, but what if your action of saving one human harms the other? In cases like what that robot encountered with saving the victims of a car crash, when an impossible choice is given about whom to save, how do you decide?"

**中文理解**：第一定律说的是不伤害人类，可如果救一个人就会伤到另一个人呢？像那台机器人遇到的车祸现场，当必须在两个人之间二选一时，你凭什么决定？

**关键词**：`first law`、`impossible choice`、`how do you decide`

**为什么这样写**：作者把三定律从「规则文本」变成「算术题」：规则给的是禁令，现实给的是取舍。这一问把整章从影评推向伦理，也为后文「价值系统无法编码」铺路。

**句子结构**：第一句 but 引出对比疑问句，what if 引导条件从句。第二句 In cases like what that robot encountered 是介词短语作状语，when an impossible choice is given about whom to save 是被动的时间状语从句，主句 how do you decide 又是疑问句。

**表达方式**：连续两个问句都不给答案；impossible choice 与 whom to save 把抽象伦理压成一个具体的二选一。

> **原句 7:** "While we humans like to rationalize and optimize things whether it’s our bets on the stock market or the selection of college majors, we still go with our heart and moral values while making many decisions. Caring and sacrificing for our loved ones aren’t a calculated decision for us; it’s an emotional and a social one."

**中文理解**：我们会在股票、择校这类事上精打细算，但许多决定仍然跟着心与道德走；为亲人付出与牺牲不是算出来的，它是情感性的、社会性的。

**关键词**：`go with our heart`、`aren’t a calculated decision`、`emotional and a social one`

**为什么这样写**：作者要证明人类的价值判断不是被优化出来的，所以先承认我们也会算计，再指出关键决定不算计。承认一半，反驳才有分量。

**句子结构**：第一句 While 引导让步从句，从句内 whether...or... 是同位并列，主句是 we still go with our heart and moral values。第二句主语 Caring and sacrificing for our loved ones 是动名词短语，aren’t a calculated decision 作表语，分号后 it’s an emotional and a social one 用 it 回指同一主语。

**表达方式**：用「不是……而是……」的对举给价值下定义；分号把两种性质并置，语气笃定。

> **原句 8:** "But how do you express this value system in a way that an artificial entity can understand and implement it? Not everything can be codified and some things require experience, reasoning, and compromises to understand and internalize."

**中文理解**：可你要怎样把这套价值系统表达成机器能懂、能执行的形式？不是所有东西都能写成条文，有些东西要靠经验、推理与妥协才能理解并内化。

**关键词**：`codified`、`experience, reasoning, and compromises`、`internalize`

**为什么这样写**：这是全章的技术核心：问题不在于算法不够强，而在于「价值」这种知识无法完整转写成规则。codify 这个动词一点破，后面所有案例都只是这句话的实例。

**句子结构**：第一句是 how 引导的疑问句，in a way that 引导方式状语从句，从句里的 it 指 value system。第二句 Not everything can be codified 是部分否定，and 后 some things require... 并列，require 的宾语是三个名词，to understand and internalize 是目的状语。

**表达方式**：先问「怎么表达」，再答「有些表达不了」；用部分否定避免绝对化，同时保住结论的力度。

> **原句 9:** "Killer robots and AI taking over the world may catch our attention more, but perhaps they are less likely to happen. What is more likely to happen is a lot less direct and in a lot more subtle way."

**中文理解**：杀手机器人、AI 接管世界这类事更能抓住注意力，但也许更不可能发生；更可能发生的事要间接得多，也隐蔽得多。

**关键词**：`catch our attention`、`less likely`、`subtle`

**为什么这样写**：这是全书的转向句，把读者的注意力从「轰然崩塌」调到「悄无声息」。作者不说灾难不会来，只说它换了一种到来的方式——这句之后，叙述从电影院切到 2018 年 Spotify 的午餐。

**句子结构**：第一句 but 连接两个并列分句，主语 Killer robots and AI taking over the world 是并列名词短语。第二句 What is more likely to happen 是主语从句，表语是两个比较级短语 less direct 与 in a lot more subtle way。

**表达方式**：用「更抓眼球 / 更不可能」对「更可能 / 更隐蔽」两组对照，把戏剧性与概率拆开；比较级的滑动感让结论显得谨慎而不是耸动。

> **原句 10:** "There was a 2016 article in ProPublica, an issues-driven, investigative journalism publication that I read when I can, that discussed using an ML-based software called COMPAS, which stood for Correctional Offender Management Profiling for Alternative Sanctions, in determining the likelihood of a convicted felon to recommit a crime if released."

**中文理解**：2016 年 ProPublica 上有一篇文章，讨论一款叫 COMPAS 的机器学习软件——全称是「替代性制裁的矫正罪犯管理画像」——用它来判断已定罪者获释后再犯罪的可能性。

**关键词**：`COMPAS`、`likelihood`、`recommit a crime`

**为什么这样写**：作者用一个长定语把陌生缩写讲清楚：刊物、性质、软件全称、用途，四层信息塞进一句。这是全书举证的样板——先给可核查的出处，再给结论，读者才愿意跟下去。

**句子结构**：主干是 There was a 2016 article in ProPublica；that discussed using an ML-based software called COMPAS 是定语从句；which stood for... 是非限定性定语从句；句末 in determining the likelihood... 是介词短语说明用途。

**表达方式**：名词堆叠显出新闻从业者的口吻；把缩写展开成全称，让「替代性制裁」这个词本身的算计意味露出来。

> **原句 11:** "It turns out that the data used to train AI systems for facial recognition was heavily biased toward white males. So it would do a great job for that class of subjects and do poorly for minority classes, yet achieving overall high performance marks."

**中文理解**：用于训练人脸识别的数据严重偏向白人男性；所以系统对这一类人表现很好，对少数群体很差，整体指标却依然漂亮。

**关键词**：`heavily biased`、`minority classes`、`overall high performance marks`

**为什么这样写**：这一句把「平均值陷阱」说穿：高分与公平可以同时不成立。作者紧接着在下一段引入 Simpson's Paradox 与伯克利录取数据，这句是那条统计线索的入口。

**句子结构**：第一句 It turns out that 引导主语从句，从句为被动语态。第二句 So 引出结果，would do a great job for... and do poorly for... 并列，yet achieving overall high performance marks 是现在分词短语作让步状语。

**表达方式**：great、poorly、high 三个评价词放在同一句里互相拆台；yet 一词让「整体优秀」变成反讽。

> **原句 12:** "There are no killer robots or superintelligent AI that are out to destroy the world. It is a whole bunch of everyday systems with different levels of AI embedded in them doing harm in everyday situations."

**中文理解**：没有杀手机器人，也没有要毁灭世界的超级智能；有的是一大堆嵌着不同程度 AI 的日常系统，在日常情境里造成伤害。

**关键词**：`no killer robots`、`everyday systems`、`doing harm`

**为什么这样写**：这句回收了全章的标题：幽灵不在实验室，在推荐、招聘、执法这些日常流程里。用「没有……有的是……」的句式把恐惧对象替换掉，读者的注意力被重新定向。

**句子结构**：第一句是 There are no... 的存在句否定，两个宾语并列，that are out to destroy the world 是定语从句。第二句 It 指上一句否定的东西，with different levels of AI embedded in them 是后置定语，doing harm in everyday situations 是现在分词作定语。

**表达方式**：几乎不用形容词，只靠名词的日常性（systems、situations）降温；把「毁灭世界」与「日常伤害」并置，制造尺度上的不适。

> **原句 13:** "Many have lost their jobs and will continue losing their jobs because someone figured out a way to replace them with AI for cost-cutting and other efficiency measures without enough testing of those AI systems for potential for bias or hallucination—a form of fabricated responses that are untrue or unaccountable."

**中文理解**：许多人已经失业，还会继续失业，因为有人找到了用 AI 替代他们的办法来省钱提效，却没有充分测试这些系统在偏见或幻觉上的风险——幻觉就是编造出不真实、无法追责的回答。

**关键词**：`cost-cutting`、`hallucination`、`unaccountable`

**为什么这样写**：作者把「部署动机」与「测试缺失」并置：不是有人恶意，而是省钱的压力跳过了验证。这句同时给出全书对 hallucination 的定义，说明他要谈的不只是偏见。

**句子结构**：主句是 Many have lost their jobs and will continue losing their jobs；because 从句说明原因，someone figured out a way to replace them with AI for... 是宾语从句；without enough testing of those AI systems for... 是介词短语作状语；破折号后 a form of fabricated responses... 是 hallucination 的同位语。

**表达方式**：现在完成时与将来进行时叠用（have lost / will continue losing），写出持续感；破折号后的定义句当场解释术语，避免读者掉队。

> **原句 14:** "The evil forces are not some external entities, but things intertwined with our everyday living. The good guys are not some heroes riding in with a good heart and might, but all of us who could recognize our role and responsibilities at this crossroads."

**中文理解**：恶的力量不是外部的实体，而是缠在我们日常里的东西；好人也不是带着善心与武力赶来的英雄，而是所有能在这个路口认出自己角色与责任的人。

**关键词**：`evil forces`、`intertwined`、`our role and responsibilities`

**为什么这样写**：全章从「看电影」走到「我们是谁」，最后一句把责任交回读者：没有可杀的敌人，只有可改的日常。这也呼应书名——raising AI 与 raising 一个孩子是同一件事。

**句子结构**：两句都是 The X are not A, but B 的否定对举；第一句 but 后是 things intertwined with our everyday living（过去分词作后置定语），第二句 but 后是 all of us who could recognize...（定语从句）。

**表达方式**：同一句式用两次，形成排比；抽象的责任最后落在 all of us 上，语气从评论转为呼吁。

## 词汇分级

### ⭐⭐⭐ 高级

| 词汇 | 释义 | 例句 |
|---|---|---|
| nonchalant | 若无其事的、故作轻松的 | It all happened so fast—looking for and buying the car, getting the insurance, picking up my date while being nonchalant about the whole thing—that it wasn’t until we were walking into the movie theater that I finally felt the weight of it all and started feeling nervous. |
| symptomatic | 作为症状的、是某事的征兆 | But as I kept digging, I realized that the problem of bias in AI systems is much deeper and these seemingly isolated incidents were symptomatic of something else. |
| perpetuate | 使延续、把……固化下去 | Things like query auto completion and related query suggestions on Google reflect the biases that the society at large may have, and perpetuate it through feeding us those stereotypes at the top of our feeds and results pages. |
| piecemeal | 零敲碎打地、一件一件地 | Do we retain our claim on this planet if we give up agency to most aspects of our lives to AI we built in some ways haphazardly, only to then modify it piecemeal over time? |

### ⭐⭐ 进阶

| 词汇 | 释义 | 例句 |
|---|---|---|
| buyer’s remorse | 买后懊悔 | I had the buyer’s remorse, as many do. |
| clunky | 笨重而不可靠的 | The AI behind the robot was clunky, unreliable, and certainly not ready for a field test. |
| rampant | 猖獗的、泛滥成灾的 | That problem of small classes getting penalized is so rampant that there are a whole set of techniques developed in machine learning to overcome such biases and build a more robust and fair model. |
| lament | 哀叹、悲悼 | That’s how T.S. Eliot laments in his poem “The Hollow Men,” written about a century ago. |

### ⭐ 常用

| 词汇 | 释义 | 例句 |
|---|---|---|
| salivating | 垂涎欲滴、馋得流口水 | I was almost salivating thinking about such a future. |
| hooky | 逃学、旷课（play hooky） | A shoplifter, a student playing hooky, a person cutting in a line—they are all violating our value system. |

## 一句话总结

作者 2004 年在电影院里学到的是「机器人会杀人」，十四年后在 Spotify 的午餐桌上才被告知真相：伤人 的是嵌在日常系统里的偏见与失控，这些「幽灵」与系统同龄，而它们被放进去的理由往往只是「因为能做」。
