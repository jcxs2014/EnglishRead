---
状态: 未读
modified: "2026-10-31"
source_text: ch01
---

# 01. Prologue（序言：考场上的一个问题）

## 概览

- **出处**：*Raising AI: How Artificial Intelligence Is Shaping Us and How We Shape It*（Bloomsbury Libraries Unlimited，2026）Prologue
- **作者**：Chirag Shah（华盛顿大学西雅图分校信息与计算机科学教授，InfoSeeking Lab 创办人，RAISE 中心联合创办人；研究透明、公平、可问责的智能系统）
- **体裁**：非虚构论述（科技评论＋个人回忆），全书序章
- **章节定位**：正文七章之前的短序（约 7,100 字符），任务是给出全书的问题起点：机器能做到的事越来越像「学习」，而我们连人类自己怎样学习都答不上来
- **字符数**：约 7,100 字符
- **一句话主旨**：一次本科口试把作者问住了——「你觉得人类也是这样学习的吗？」——考官的「没人知道」既救了他，也成了他此后二十多年反复回到的那个问题。

序言是一段被压缩得很紧的回忆。场景只有一间考场、一张考官桌、一个紧张到出汗的本科生；冲突也只有一句追问。作者先用身体感受把读者按进那个下午，再退后一步，把这个私人时刻接到一条七十年的技术谱系上：1943 年的 McCulloch–Pitts 神经元、1957 年 Rosenblatt 的 Perceptron 演示、报纸头条里的「机器会学习」。个人的窘迫因此不再是青春轶事，而成了「这个领域最核心的问题至今没有答案」的现场证据。

### 结构列表

1. **考场与心跳**：教室显得比平时小，脚步声在寂静里回响，焦虑拉满。
2. **项目本身很朴素**：前馈网络、多层感知机、反向传播，做模式分类。
3. **稀缺条件**：课上不教神经网络，学院没有网络，只有小镇图书馆的旧书。
4. **室友的质疑**：为什么不做个正常的规则系统；他也认为作者超出了自己的能力。
5. **七十年的谱系**：McCulloch 与 Pitts 的神经元构想在先，Rosenblatt 的 Perceptron 演示在后。
6. **考官的追问**：神经网络是否就是人类学习的方式。
7. **语言的第二重门槛**：二十岁前十八年不说英语，技术词汇之外无法展开。
8. **「没关系，没人知道」**：他通过了考试，也第一次遇到一个没有标准答案的问题。
9. **五年与地球另一端**：作者预告自己会回到这些问题，世界不再是非黑即白。

## 论证结构

- **核心论点**：AI 最重要的那个问题——人类如何学习、什么使我们有智能——从 1943 年到今天都没有答案；作者用自己考场上的失语证明，这个空白不是知识不足，而是领域本身的边界。因此讨论 AI 不能停在「能不能做到」，必须先承认我们对「智能」本身所知有限。

- **证据链**：

  | 证据 | 类型（案例/研究/数据/类比） | 支撑什么 |
  |------|------|------|
  | 本科 AI 课期末口试，用自学的神经网络项目应考 | 个人案例 | 技术演示与真正理解之间存在落差 |
  | 1943 年 McCulloch–Pitts 神经元模型 | 历史 | 「向生物大脑取经」的构想早于现代 AI，今天仍在教 |
  | 1957 年 Rosenblatt 的 Perceptron 演示与《纽约时报》标题 | 历史＋媒体 | 单层感知机的一次演示就足以让公众相信机器会学习 |
  | 课上不教、学院无网、只能读小镇图书馆旧书 | 个人处境 | 稀缺条件迫使自学者面对原理，而不是调用现成工具 |
  | 考官的回答「That's ok, nobody does!」 | 对话 | 领域内的权威同样承认这个问题没有答案 |
  | 二十岁前十八年不说英语 | 个人数据 | 技术能力之外还有语言门槛，非母语者要多付一层代价 |

- **论证脉络**：考场场景（具体、低风险）→ 项目细节（把技术门槛降下来）→ 七十年的神经元谱系（把个人经验接进历史）→ 考场上的那句追问（转折）→ 「没人知道」（承认空白）→ 五年后回到问题（预告全书）→ 世界不再非黑即白（收束）。

- **可质疑处**：
  1. 用一次本科口试的紧张来承载一个认识论判断，是把个人经验抬升为论证。作为序言的引子它有效，但读者不宜把「我当时答不上来」当成「这个问题无人能答」的证据。
  2. 「我们真的不知道人类如何学习」这句话在序言里没有划定范围。认知科学与神经科学已有大量局部模型，作者要表达的是「没有统一答案」，字面上却更绝对。
  3. 序言把 1957 年的演示写成世界第一次看见这类构造的力量，却没有提到此后对感知机表达力的质疑。只读序言会得到一条持续上升的技术线，而这条线在正文第三章会被打断。

## 选择性精读

> **原句 1:** "The exam room felt smaller than usual as I walked toward the examiner’s desk, my footsteps echoing in the silence. I could tell my heartbeats were up and the level of anxiety hitting high. It was the final exam for my undergraduate AI class and while we were not taught neural networks in that class at the time, I had decided to do my final project using neural networks."

**中文理解**：他走向考官桌子时觉得教室比平时更小，脚步声在寂静里回响；他能感觉到心跳加快、焦虑升到高点——这是本科 AI 课的最后一次考试。那门课当时并不教神经网络，期末项目却是他决定用神经网络来做的。

**关键词**：`exam room`、`heartbeats`、`anxiety`、`footsteps echoing`

**为什么这样写**：全书要用一个具体场景立住问题，作者选的是最低风险的一种失败——不是战争、不是失业，而是一场考试。风险越小，读者越容易代入，后面那句「没人知道」的松动才显得意外。

**句子结构**：第一句主句是 The exam room felt smaller than usual，as I walked toward the examiner's desk 是时间状语从句，my footsteps echoing in the silence 是独立主格结构，补足听觉细节。第二句 I could tell 后面接省略 that 的宾语从句，从句内 my heartbeats were up 与 the level of anxiety hitting high 并列。

**表达方式**：不写「我很紧张」，只写教室变小、脚步声回响、心跳变快——用感官的失真写出紧张，让读者自己完成判断。

> **原句 2:** "Nothing fancy—a simple feed forward network with multiple layers of Perceptrons running backpropagation algorithm to do a pattern classification task. But back then when we were not taught such things in the class and I had no access to the internet at my college in India, this was a daunting task."

**中文理解**：项目并不花哨：一个简单的前馈网络，多层感知机跑反向传播，做模式分类。可当时课上不教这些，他在印度的学院也没有网络，这件事因此很难。

**关键词**：`feed forward network`、`backpropagation`、`daunting`

**为什么这样写**：先自贬技术含量，再把难度挪到条件上——不是他聪明，而是环境不允许偷懒。这一步为后文「自学者只能面对原理」埋下前提。

**句子结构**：第一句以 Nothing fancy 起头，破折号后是一个名词短语作补充说明，with multiple layers of Perceptrons 修饰 network，running backpropagation algorithm 是现在分词短语修饰 Perceptrons。第二句 But 转折，back then 与 when 从句叠用给出时间与条件，主句 this was a daunting task 落在最后。

**表达方式**：用「Nothing fancy」压低期待，再用 but 把读者拉到另一侧：同样的东西在没有网络、没有课程的条件下要难得多。

> **原句 3:** "One of the early ideas that took inspiration from the biological brain came from Sturgis McCulloch and Walter Pitts. They proposed that we could build an artificial construct, a neuron, that could do simple cognitive tasks."

**中文理解**：最早从生物大脑取来的想法之一出自 McCulloch 与 Pitts：他们提出可以造一个人造物——神经元——来完成简单的认知任务。

**关键词**：`biological brain`、`artificial construct`、`cognitive tasks`

**为什么这样写**：他把自己的考场项目挂到一条七十年的链条上。个人的笨拙因此不是孤例，而是这一领域从一开始就在做的事：用人造结构模仿认知。

**句子结构**：第一句主语 One of the early ideas 被 that took inspiration from the biological brain 这个定语从句切开，谓语 came from 直到句末才出现。第二句 They proposed that 引导宾语从句，a neuron 是 artificial construct 的同位语，后面的 that could do simple cognitive tasks 修饰 construct。

**表达方式**：同位语 a neuron 把抽象概念一步落地；cognitive tasks 这个词组替「智能」留了余地——做任务，而不必先定义智能。

> **原句 4:** "But it wasn’t until Frank Rosenblatt did his famous demonstration of a new kind of neuron, what he called Perceptron, in 1957, that the world saw the real power of what such artificial constructs could do."

**中文理解**：直到 1957 年 Rosenblatt 演示了他称为 Perceptron 的新型神经元，世界才看到这类人造物真正的能力。

**关键词**：`Perceptron`、`demonstration`、`1957`

**为什么这样写**：时间点被写成转折点。作者需要一个「公众第一次相信机器会学习」的时刻，而 1957 年的演示正合适：它有观众、有报纸、有一个可以被记住的名字。

**句子结构**：整句是 It was not until ... that ... 的强调结构，把时间状语推到焦点位置；what he called Perceptron 是插入的同位成分，说明这种神经元的名字；句末 what such artificial constructs could do 是介词 of 的宾语从句。

**表达方式**：not until 的否定前置让「1957 年之前」显得漫长，演示因此不只是成功，而是分界线。

> **原句 5:** "Little did I know back then that even with more resources, I wouldn’t have found a good answer because we really didn’t and still don’t know how humans learn or what precisely makes us intelligent."

**中文理解**：他当年并不知道，即使资源更多也找不到好答案——因为我们当时不知道、至今也仍然不知道人类怎样学习，究竟什么使我们有智能。

**关键词**：`Little did I know`、`how humans learn`、`intelligent`

**为什么这样写**：这是序言的问题宣言。前面所有的窘迫都指向这一句：答不上来不是因为准备不足，而是因为题目本身没有答案。

**句子结构**：Little did I know 是否定词前置引起的部分倒装，后面 that 从句作宾语；从句内 even with more resources 是让步状语，because 从句里 we really didn't and still don't know 用两个时态并置，宾语是 how humans learn 与 what precisely makes us intelligent 两个从句。

**表达方式**：倒装句给出「事后才知道」的视角；didn't and still don't 把过去与现在钉在同一句里，说明这个空白没有随时间缩小。

> **原句 6:** "It will take me five more years and a place on the other side of the planet to come back to these questions. My world would never be so black-and-white."

**中文理解**：他要再过五年、到地球的另一端，才会重新回到这些问题；而他的世界再也不会那样非黑即白。

**关键词**：`five more years`、`the other side of the planet`、`black-and-white`

**为什么这样写**：序言收在一句预告上：答案不在原地，在别处、在以后。同时用 black-and-white 回指考场逻辑——要么知道要么不知道——为全书之后的灰色地带做铺垫。

**句子结构**：第一句 it 是形式主语，真正的主语是 to come back to these questions，five more years 与 a place on the other side of the planet 并列作条件。第二句用 would 表过去将来的推测，never so 是比较结构。

**表达方式**：把抽象转变写成两个可量的坐标：五年、半个地球。距离越具体，转变越可信。

## 词汇分级

### ⭐⭐⭐ 高级

| 词汇 | 释义 | 例句 |
|---|---|---|
| bitten off more than I could chew | 揽下超出自己能力的事 | Still, I knew I had bitten off more than I could chew. |
| in over my head | 陷入力所不及的境地 | He too knew that I was in over my head. |
| innuendoes | 含沙射影的话、暗讽 | Things like sarcasm or innuendoes were not something we could appreciate or respond to well. |
| ingrained | 根深蒂固的 | This was so ingrained in me that it took me a lot of time and effort to drop it when I was a new student in the United States. |

### ⭐⭐ 进阶

| 词汇 | 释义 | 例句 |
|---|---|---|
| daunting | 令人望而生畏的 | But back then when we were not taught such things in the class and I had no access to the internet at my college in India, this was a daunting task. |
| flunked | 考试不及格、挂科 | I had never flunked a class before and having this final project in my favorite subject change that in my junior year would be devastating. |
| mundane | 平淡无奇的、不起眼的 | While my structure of the neural network was a lot more sophisticated than what Rosenblatt demonstrated decades ago, the application was just as mundane. |

### ⭐ 常用

| 词汇 | 释义 | 例句 |
|---|---|---|
| stern | 严厉的、板着的 | Did I see a smile on the stern face of that examiner? |
| dawned on | （某事）突然被意识到 | It suddenly dawned on me that while I could easily impress my friends with an implementation of neural networks, I was now sitting in front of someone who knows a lot more than my friends. |

## 一句话总结

一个本科生在考场上被「人类是否也这样学习」问住，考官的回答是「没人知道」；这个没有答案的问题成了作者此后二十多年研究 AI 的起点，也是全书要接着追问的地方。
