---
状态: 未读
modified: "2026-10-31"
source_text: ch04
---

# 04. Chapter 3 Waves and Winters of AI（AI 的浪潮与寒冬：规则系统为何失败，狂热为何反复）

## 概览

- **出处**：*Raising AI: How Artificial Intelligence Is Shaping Us and How We Shape It*（Bloomsbury Libraries Unlimited，2026）Chapter 3
- **作者**：Chirag Shah（华盛顿大学西雅图分校信息与计算机科学教授，InfoSeeking Lab 创办人，RAISE 中心联合创办人）
- **体裁**：非虚构论述（个人回忆＋技术史＋周期分析）
- **章节定位**：正文第三章，约 62,000 字符。任务是回答上一章留下的问题：真实 AI 的历史到底怎么走？作者先用自己的 UNL 惨败引出「规则系统不可行」的结论，再用五个时代（1940s–2020s）证明 AI 一直在「狂热—寒冬」的周期里前进，最后借股市类比回答「下一个寒冬会不会来」
- **字符数**：约 62,000 字符
- **一句话主旨**：规则系统永远无法捕捉自然语言——这是作者在 UNL 项目里用几年青春换来的教训；AI 的历史由此展开，五次浪潮、两次寒冬，每一波都在破灭后以更强形态回归；所以当下的生成式 AI 狂潮终会回调，但别信炒作、理性参与，才能穿越周期。

全章从 2002 年作者冲出 IIT Bombay 实验室写起：他本科时因私建 ad hoc 网络被 HOD 罚了 500 卢比，却在 CKB 老师的帮助下进了 IIT，从此深陷联合国资助的 UNL 通用语言项目。项目让「Ram eats rice」成了实验室的玩笑，也让他得出结论——自然语言不可能被一组规则捕获。接着他展开五段式历史：Era-1 信息论与感知机的狂热、第一次寒冬；Era-2 专家系统与日本 FGCS、第二次寒冬；Era-3 机器学习与 LSTM 的蓄力；Era-4 深度学习与强化学习的爆发；Era-5 生成式 AI 的当下。最后用「AI Winter Is Coming」收束：回调不可避免，但理性者可以像研究股票一样研究 AI。

### 结构列表

1. **2002 年的怀疑**：作者与 PB Sir 争吵、冲出实验室，第一次对 AI 产生动摇。
2. **本科的迷恋**：科幻喂养的少年幻想，被一门只讲符号逻辑的课程和严苛的 HOD 双重压制。
3. **500 卢比的教训**：私建 ad hoc 网络被拆，HOD 罚款相当于一个月房租，作者打工偿还。
4. **UNL 项目**：联合国资助的通用中间语言，理论上源自图灵机，实践里只让「Ram eats rice」通过。
5. **规则系统的死刑**：自然语言变化无穷，一组固定规则永远无法捕捉——这是全章的立论。
6. **Era-1（1940s–1960s）**：Shannon 的 bit、Bush 的 Memex、图灵的十四行诗、感知机的狂热与第一次 AI 寒冬。
7. **Era-2（1970s–1980s）**：专家系统、DENDRAL、日本第五代计算机 FGCS，与第二次 AI 寒冬。
8. **Era-3（1990s–2000s）**：机器学习从数据推断规则、LSTM、Deep Blue 与 Stanley 的复苏。
9. **Era-4（2010s）**：深度学习＋强化学习，AlphaGo 击败李世石，RL 给谷歌数据中心省电 40%。
10. **Era-5（2020s 至今）**：生成式 AI，DALL-E 画鳄梨扶手椅、ChatGPT 走进日常。
11. **Winter Is Coming**：股市类比——回调必然发生，但不等于末日；理性参与才是出路。

## 论证结构

- **核心论点**：AI 的历史不是线性进步，而是「狂热—寒冬」的反复周期；而每一次寒冬的根源，都是把一种方法论过度承诺为万能解（规则系统、专家系统都是如此）。作者用 UNL 的个人失败证明「规则系统无法捕捉自然语言」，用五段历史说明周期确实存在，再用股市类比论证当前生成式 AI 的狂热终将迎来回调——回调不可怕，可怕的是盲目跟风者会在低点出局。

- **证据链**：

  | 证据 | 类型（案例/研究/数据/类比） | 支撑什么 |
  |------|------|------|
  | UNL 项目多年只让「Ram eats rice」类简单句通过，变体即崩 | 个人经历 | 规则系统无法处理自然语言的无穷变化 |
  | 1966 年 ALPAC 报告：机器翻译更贵、更不准、更慢 | 官方报告 | 第一次 AI 寒冬的触发条件 |
  | 1969 年 Minsky/Papert 证明感知机无法解决某些问题 | 学术研究 | 早期神经网络热潮的理论上限 |
  | 1997 年 Deep Blue 胜 Kasparov、2005 年 Stanley 穿越 131 英里沙漠、2016 年 AlphaGo 击败李世石 | 里程碑事件 | 每次寒冬之后 AI 都更强地复苏 |
  | 2021 年 DALL-E、2022 年 Stable Diffusion 与 ChatGPT | 技术产品 | 生成式 AI 构成第五波浪潮 |
  | 美国股市 1962–2010 年五次崩盘与 2009 年起十年牛市 | 类比 | 任何长期繁荣都包含必然的回调 |

- **论证脉络**：2002 年个人挫败（UNL）→ 归纳出「规则系统不可行」→ 追问历史以理解当下 → 五段式时代史（Era-1 到 Era-5）→ 用股市周期类比 AI 周期 → 结论：下一个 AI 寒冬会来，但理性参与者可以从中获益。

- **可质疑处**：
  1. 「自然语言无法用规则捕捉」是作者 2002 年基于 UNL 项目得出的结论，但当代大语言模型本质上仍是在海量文本上做统计模式匹配——它是否真的绕开了「规则」的局限，还是把规则换成了更大规模的参数，仍是开放问题。
  2. 用股市类比 AI 周期可能过度简化：股市的均值回归有百年数据支撑，而 AI 只有几次样本，且技术演进未必服从同样的心理周期。
  3. 「每次寒冬后 AI 都更强复苏」带有幸存者偏差：历史上被放弃的路线（如 UNL 本身）并未复苏，作者只选取了最终成功的几条线索来叙事。

## 选择性精读

> **原句 1:** "The year was 2002 and for the first time, I was having my doubts about this whole AI thing."

**中文理解**：时间是 2002 年，作者第一次对「AI 这整件事」产生了怀疑。这是全章个人叙事的起点。

**关键词**：`doubts`、`the first time`、`AI thing`

**为什么这样写**：作者不按时间顺序从童年讲起，而是先抛出结果——怀疑。用一句简短的自述把读者拉进关键时刻，再倒叙解释怀疑从何而来，制造悬念。

**句子结构**：and 连接两个并列分句；前一个 The year was 2002 是背景，后一个 for the first time, I was having my doubts about this whole AI thing 用过去进行时强调「正在怀疑」的状态。

**表达方式**：口语化的 this whole AI thing 带着自嘲与亲近感，与学术写作形成反差；把宏大的 AI 话题说成「这整件事」，暗示作者已从信徒变成怀疑者。

> **原句 2:** "So he fined me Rs. 500. Back then, this much money could pay one month’s rent."

**中文理解**：于是 HOD 罚了他 500 卢比；在当时，这笔钱够付一个月房租。作者只能靠打工还清罚款。

**关键词**：`fined`、`Rs. 500`、`month’s rent`

**为什么这样写**：用「罚款等于一个月房租」的具体换算，让读者立刻感到处罚的沉重；一个穷学生的处境跃然纸上，也强化了「追求 AI 的热情」与「体制压制」之间的张力。

**句子结构**：第一句 So he fined me Rs. 500 是简洁的结果句；第二句 Back then 是时间状语，this much money 作主语，could pay 是谓语，one month’s rent 作宾语。

**表达方式**：数字加生活经验的换算比任何形容词都有冲击力；两句都用短句，节奏平静克制，委屈都藏在句号后面。

> **原句 3:** "That sentence “Ram eats rice” was so prevalent in our demos that it became the subject of jokes around UNL’s failures."

**中文理解**：「Ram eats rice」这句话在演示里出现得太过频繁，以至于它成了大家拿 UNL 的失败开玩笑的梗。

**关键词**：`prevalent`、`demos`、`jokes`

**为什么这样写**：用一个具体的梗（可怜的 Ram 只会吃米饭）把项目多年停滞的荒诞感具象化；实验室里的自嘲，比任何数据都更能说明「规则路线走不通」。

**句子结构**：主干 That sentence was so prevalent... that it became...，so...that... 构成结果状语从句；around UNL’s failures 作 jokes 的后置定语。

**表达方式**：学术词 prevalent 与日常词 jokes 并置，一本正经地说出实验室的黑色幽默；用笑声反衬挫败，比直接抱怨更有力。

> **原句 4:** "It wasn’t due to lack of enough resources, set of rules, or our determination. It was because fundamentally, it is impossible to capture natural language with a set of rules, no matter how many."

**中文理解**：失败不是因为资源不足、规则不够，也不是因为决心不够；而是因为从根本上说，无论多少规则，都不可能捕捉自然语言。

**关键词**：`impossible`、`capture natural language`、`a set of rules`

**为什么这样写**：先排除三种常见归因，再给出唯一结论，把论点一层层钉死；这是全章承上启下的核心判断，后面的五段历史都是它的注脚。

**句子结构**：第一句用 It wasn’t due to... 否定三项并列（resources, rules, determination）；第二句 It was because fundamentally... 正面作答，no matter how many 是让步状语从句。

**表达方式**：两个平行句一否定一肯定，形成清晰的对照；fundamentally 一词把讨论从技术层面抬到本质层面，语气像法官宣判。

> **原句 5:** "I do not see why it (the machine) should not enter any one of the fields normally covered by the human intellect, and eventually compete on equal terms."

**中文理解**：图灵在 1949 年说，他看不出机器为什么不能进入人类智识通常覆盖的任何一个领域，并最终与人类平等竞争。

**关键词**：`human intellect`、`compete on equal terms`、`the machine`

**为什么这样写**：直接引用图灵的原话，为「AI 终将全面追赶人类」这一判断提供历史权威；括号里的 the machine 替读者指明代词 it，避免歧义。

**句子结构**：主干 I do not see why it should not enter any one of the fields；normally covered by the human intellect 是过去分词短语作定语；and eventually compete on equal terms 与 enter 并列。

**表达方式**：双重否定 should not enter any one 语气委婉而坚定，符合科学家的审慎；equal terms 一词把机器的地位与人类拉平，措辞克制却野心十足。

> **原句 6:** "machine translation was more expensive, less accurate and slower than human translation."

**中文理解**：机器翻译比人工翻译更贵、更不准、更慢——这是 ALPAC 委员会 1966 年报告给机器翻译下的结论。

**关键词**：`machine translation`、`more expensive`、`less accurate`

**为什么这样写**：引用政府官方报告的原话，说明第一次 AI 寒冬不是情绪使然，而是有权威评估背书：连最受宠的机器翻译都被判了死刑，资金自然枯竭。

**句子结构**：三个并列的比较级 more expensive, less accurate and slower 构成排比主语补语，than human translation 是比较对象；全句无从句，简洁到近乎宣判。

**表达方式**：三个比较级连用形成节奏感，一锤定音；把「贵、不准、慢」三项罪状并排，比任何形容都更有杀伤力。

> **原句 7:** "Just like we can learn to recognize objects like dogs from seeing lots of examples without an explicit definition of “dogness,” machine learning systems could infer their own rules."

**中文理解**：就像我们看大量例子就能学会认出狗、而不需要「狗性」的明确定义一样，机器学习系统也能自己推断规则。

**关键词**：`recognize objects`、`explicit definition`、`infer their own rules`

**为什么这样写**：用「认识狗」这种人人有经验的事做类比，把机器学习「从数据推断规则」的核心讲得直观易懂；这一句直接与前面的 UNL 手写规则形成对照。

**句子结构**：Just like 引导方式状语从句（we can learn to recognize...），主句是 machine learning systems could infer their own rules；without an explicit definition of “dogness” 是介词短语作条件状语。

**表达方式**：临时造词 dogness 俏皮而传神，把抽象概念具象化；just like... could 的对称结构让读者瞬间理解新旧范式的差别。

> **原句 8:** "Their methods powered “AlphaGo” in 2016, created by DeepMind (later acquired by Google), to defeat one of the world’s top players in the famously complex board game Go with intuitive strategies human experts had never tried."

**中文理解**：强化学习的方法在 2016 年成就了 AlphaGo——由 DeepMind 打造、后被谷歌收购——它用人类专家从未试过的直觉策略，击败了世界上最顶尖的围棋棋手。

**关键词**：`powered`、`AlphaGo`、`intuitive strategies`

**为什么这样写**：用 AlphaGo 这个大众熟知的事件作为强化学习威力的证据；括号补充收购信息，让不熟悉科技新闻的读者也能理解背景。

**句子结构**：主干 Their methods powered “AlphaGo” in 2016；created by DeepMind 是过去分词短语作定语，(later acquired by Google) 是插入语；to defeat... 是不定式表结果，with intuitive strategies human experts had never tried 修饰 defeat 的方式。

**表达方式**：长句层层嵌套但逻辑清晰；intuitive strategies 与 human experts had never tried 并置，突出 AI 已经走出人类经验之外的震撼。

> **原句 9:** "Want an armchair shaped like an avocado in a rococo palace? DALL-E could illustrate complex scenes like this in remarkable fidelity."

**中文理解**：想要一把放在洛可可宫殿里的鳄梨形扶手椅？DALL-E 能以惊人的保真度画出这样复杂的场景。

**关键词**：`armchair`、`avocado`、`remarkable fidelity`

**为什么这样写**：用一个荒诞而具体的例子展示生成式 AI 的能力边界，让读者直观感受第五波浪潮与以往的不同——AI 不再只是分析，而是创造。

**句子结构**：第一句是省略主语 You 的疑问句；第二句 DALL-E could illustrate complex scenes like this in remarkable fidelity 是简单的主谓宾结构。

**表达方式**：疑问句直接对读者发问，像现场演示的口语；avocado 与 rococo palace 的混搭制造喜剧效果，让「生成式 AI」这个抽象概念变得可触摸。

> **原句 10:** "Don’t buy into the hype. Instead, focus on the strengths and risks with this technology, much like what you would do researching while buying a stock. Learn, participate, and prosper."

**中文理解**：别轻信炒作。相反，要像买股票前做研究那样，去关注这项技术的优势与风险。去学习、去参与，然后获益。

**关键词**：`hype`、`strengths and risks`、`prosper`

**为什么这样写**：作者把 AI 比作投资，给出全章的行动建议；三个短祈使句收尾，把「历史会重演」的冷静判断转成对读者的号召，避免全书停在悲观里。

**句子结构**：三个句子都是祈使句；第二句 much like what you would do researching while buying a stock 用方式类比，第三句用三个并列动词构成首尾呼应。

**表达方式**：短促有力的祈使句像格言一样铿锵；从 buy into the hype 到 prosper，完成「警示—建议—希望」的情绪弧线。

## 词汇分级

### ⭐⭐⭐ 高级

| 词汇 | 释义 | 例句 |
|------|------|------|
| infatuation | 迷恋、痴迷（常指短暂的强烈喜爱） | My love was really a form of infatuation with AI that was based on superficial qualities and projections that I had gathered from reading and watching sci-fi stories. |
| palpable | 可感知的、明显的 | His passion and love for UNL was palpable to everyone around him and in the NLP community at large. |
| prevalent | 普遍的、流行的 | That sentence “Ram eats rice” was so prevalent in our demos that it became the subject of jokes around UNL’s failures. |
| galvanized | 激励、推动（使人行动起来） | In 2002, the first DARPA Grand Challenge galvanized autonomous vehicle research through a competition won by none other than a student team from Stanford in 2005. |

### ⭐⭐ 进阶

| 词汇 | 释义 | 例句 |
|------|------|------|
| interlingua | 中间语言（翻译中承载通用意义的媒介） | Such a language is called interlingua because a message from a natural language such as English would be converted to the intermediated form of UNL, later to be deconverted into some other natural language such as Spanish. |
| bootstrap | 白手起家；引导、自举（不靠外力启动） | They built a deep learning system called World Models that first trained on gameplay images, then used that virtual experience to bootstrap RL agents. |
| democratization | 民主化、大众化（让更多人能用上） | DALL-E pioneered this generative leap, but wider democratization soon followed. |
| fidelity | 保真度、精确程度 | DALL-E could illustrate complex scenes like this in remarkable fidelity. |

### ⭐ 常用

| 词汇 | 释义 | 例句 |
|------|------|------|
| supportive | 支持的、鼓励的 | One of my teachers—CKB—who was always very supportive of my explorations with AI encouraged me to use the lab equipment in school to set this up. |
| rent | 房租 | Back then, this much money could pay one month’s rent. |
| breakthrough | 突破、重大进展 | I couldn’t reconcile how our approach was going to lead to a breakthrough. |
| hype | 炒作、天花乱坠的宣传 | Don’t buy into the hype. |
| prosper | 兴旺、获益、成功 | Learn, participate, and prosper. |

## 一句话总结

AI 的历史是狂热与寒冬的交替：作者在 UNL 项目里用几年时间验证了「规则系统捕捉不了自然语言」，而此后每一次浪潮——从感知机、专家系统到深度学习、生成式 AI——都在破灭后以更强形态回归；面对当下这波生成式 AI，别信炒作，像研究股票一样研究它的优势与风险，理性参与，才能穿越周期。