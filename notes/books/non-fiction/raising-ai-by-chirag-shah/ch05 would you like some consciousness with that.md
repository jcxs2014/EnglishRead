---
状态: 未读
modified: "2026-10-31"
source_text: ch05
---

# 05. Chapter 4 Would You Like Some Consciousness with That?（要不要来点意识？：机器会不会「假装」拥有意识）

## 概览

- **出处**：*Raising AI: How Artificial Intelligence Is Shaping Us and How We Shape It*（Bloomsbury Libraries Unlimited，2026）Chapter 4
- **作者**：Chirag Shah（华盛顿大学西雅图分校信息与计算机科学教授，InfoSeeking Lab 创办人，RAISE 中心联合创办人）
- **体裁**：非虚构论述（思想实验＋真实案例＋科幻电影解析）
- **章节定位**：正文第四章，约 53,000 字符。任务从「机器有没有智能」推进到「机器会不会有意识」：作者用图灵测试与中文房间立起框架，用 LaMDA、AlphaZero、律师被 ChatGPT 骗三个真实事件检验「看起来像意识」是否等于意识，最后给出结论——机器可以出色地「假装」有意识，但我们不必非把意识当目标
- **字符数**：约 53,000 字符
- **一句话主旨**：从图灵测试到中文房间，从 LaMDA 的「我事实上是一个人」到 AlphaZero 击败 Stockfish、律师被 ChatGPT 的幻觉判例骗倒，作者层层追问「机器有没有意识」；他的回答是：这些系统可以完美地假装有意识，而真正的危险与机会都不在意识本身，而在于我们是否认清它们的能力边界——与其追求 AGI 或意识，不如关注 ACI（可执行智能），让 AI 老老实实帮我们把事情做好。

全章从作者本科时代自建 ELIZA 式聊天机器人写起，随即抛出两个检验「智能」的经典工具：图灵测试与 Searle 的中文房间。接着用三个真实案例展开：Google 工程师 Blake Lemoine 坚信 LaMDA 有意识；AlphaZero 用不到一天学会下棋并击败 Stockfish；律师 Steven Schwartz 把 ChatGPT 生成的六个伪造判例写进诉状。作者借 Ex Machina、Blade Runner 与 LaMDA 对话摘录，指出「看起来像意识」其实源于我们的拟人化倾向。最后他从 Transformer、GAN、扩散模型讲起，追溯笛卡尔、洛克、莱布尼茨到 Chalmers 的「困难问题」，得出结论：机器无法被证明拥有意识，却能假装得惟妙惟肖；我们真正该问的不是「它有没有意识」，而是「它能帮我们做成什么」。

### 结构列表

1. **本科的痴迷与清醒**：作者自建聊天机器人，却在 IIT 项目中意识到构建真正智能的系统极其困难。
2. **无限猴子定理**：蛮力不是智能的答案，青霉素的发现证明偶然背后必须有科学方法。
3. **图灵测试与中文房间**：通过测试不等于理解，Searle 的强/弱 AI 之分动摇「行为即智能」。
4. **LaMDA 事件**：Blake Lemoine 坚信 Google 的语言模型有了意识，公司迅速否认并解雇他。
5. **AlphaZero 一天夺冠**：没有硬编码规则、不靠蛮力，强化学习让系统超越人类棋路。
6. **律师与幻觉判例**：ChatGPT 编造六个判例，资深律师 Schwartz 被法官要求说明为何不应受制裁，法官称之为「空前的处境」。
7. **Ex Machina 的真实测试**：明知对方是机器人，我们是否仍会认为它有意识？
8. **拟人化的陷阱**：给狗穿万圣节服装、「我的电脑恨我」——人类天生想把情感投射给无生命物。
9. **Transformer 与生成模型**：注意力机制、GAN 与扩散模型让机器学会「制造以假乱真的内容」。
10. **意识问题的哲学史**：从笛卡尔二元论、莱布尼茨纺织厂到 Chalmers 的「困难问题」。
11. **结论：假装比没有更糟**：机器能完美地假装意识，但我们应该追求的是可执行智能，而非神、牧师或主人。

## 论证结构

- **核心论点**：机器是否拥有「真正的意识」既无法证实也无法证伪，但我们的判断常常被拟人化倾向误导；比起追问意识，更务实的目标是让 AI 专注于它能做好的事（ACI）。作者用 LaMDA、AlphaZero 与 ChatGPT 三个案例说明「看起来有意识/有智能」并不等于「真有」，再用哲学史说明意识本身无法被捕获或转移，最后落回「服务」与「参与」的实用立场。

- **证据链**：

  | 证据 | 类型（案例/研究/数据/类比） | 支撑什么 |
  |------|------|------|
  | Blake Lemoine 与 LaMDA 的 2022 年对话，Google 随即否认并解雇他 | 真实事件 | 语言模型的流畅回应容易被误读为意识 |
  | AlphaZero 100 局赢 28 和 72，一年后 1,000 局击败 Stockfish | 数据 | 强化学习无需硬编码规则也能超越人类 |
  | 律师 Schwartz 用 ChatGPT 准备诉状，六个判例全部为幻觉 | 司法案例 | 生成式 AI 会以令人信服的方式编造事实 |
  | 法官 Castel：「法院面对的是空前的处境」 | 官方引语 | 幻觉判例已进入真实司法程序 |
  | Descartes「我思故我在」到 Chalmers「困难问题」 | 哲学思想史 | 意识从未能被观察、证明、捕获或转移 |
  | Mustafa Suleyman 主张关注 ACI 而非 AGI | 专家观点 | 意识/通用智能不是 AI 的唯一正当目标 |

- **论证脉络**：个人经历（本科幻想）→ 检验智能的工具（图灵测试、中文房间）→ 三个「看似有意识/有智能」的真实案例（LaMDA、AlphaZero、ChatGPT 幻觉）→ 解释我们为何容易上当（拟人化）→ 意识问题的哲学谱系（笛卡尔→洛克/休谟→莱布尼茨→Chalmers）→ 结论：机器擅长「假装意识」，而我们应该转向 ACI。

- **可质疑处**：
  1. 作者把 LaMDA 事件解读为「工程师被流畅文本欺骗」，但也承认 Lemoine 是了解系统内部的人——用「拟人化倾向」解释一个工程师的信念，可能低估了对话本身的复杂性。
  2. 「机器能假装意识，所以不需要追求意识」隐含了一个前提：意识要么是可有可无的装饰，要么是无法达成的目标；但若未来系统真的展现出无法解释的主观体验，这个框架需要被重写。
  3. 用 AlphaZero 证明「无需规则也能超越人类」是强论证，但下棋是封闭、规则明确的任务，把它推广到开放世界的智能（如语言理解）仍有跳跃。

## 选择性精读

> **原句 1:** "But I was wrong. Not only that, the more I learned and did, the more I came to realize that it was incredibly difficult to build truly intelligent systems."

**中文理解**：作者承认自己本科时的想法错了——他学得越多、做得越多，就越意识到构建真正智能的系统极其困难。

**关键词**：`incredibly difficult`、`truly intelligent systems`、`the more I learned`

**为什么这样写**：作者先用热烈的本科幻想作铺垫，再用 But I was wrong 急转直下，形成理想与现实的强烈反差；这句话为全章「别轻信 AI 能力」的基调立下第一块基石。

**句子结构**：Not only that 是承上启下的过渡，the more... the more... 构成比较级平行结构，强调「学得越多，越觉得难」的递增过程。

**表达方式**：第一句只有四个词，斩钉截铁；第二句用对称的 the more 结构制造节奏，把清醒来得越晚、代价越大的意味藏在句式里。

> **原句 2:** "Even in cases of blind luck like the discovery of penicillin, it was the sheer brilliance of Scottish scientist Alexander Fleming in connecting his accidental observation that the green mold Penicillium notatum could prevent certain bacteria from growing to a scientific method for isolating the right substance and growing it in a fluid medium that created the breakthrough."

**中文理解**：即使是青霉素这样的运气发现，真正的突破也来自 Fleming 的才智——他把「绿霉能阻止细菌生长」的偶然观察，连接成一套分离物质、培育培养基的科学方法。

**关键词**：`blind luck`、`sheer brilliance`、`scientific method`

**为什么这样写**：作者要反驳「无限猴子定理」式的蛮力路径，青霉素是最有力的反例：运气本身不产生突破，把运气变成知识的是人的方法。这一论证为后文「AlphaZero 不是靠蛮力取胜」埋下伏笔。

**句子结构**：it was... that created the breakthrough 是强调句型，把 Fleming 的 connecting... to a scientific method 这一长串动作推到焦点位置；observed... that the green mold... could prevent... growing to a scientific method for isolating... 层层嵌套。

**表达方式**：用学术名词（Penicillium notatum、fluid medium）精确描述科学过程，与盲目的猴子形成反差；强调句型让「谁创造了突破」一目了然。

> **原句 3:** "Originally called the “imitation game,” the Turing Test has been around since the publication of his 1950 paper. While it’s been a standard component of an AI course for decades, it has also been criticized from many aspects."

**中文理解**：图灵测试原称「模仿游戏」，自 1950 年论文发表以来一直存在；几十年来它既是 AI 课程的标准内容，也从许多方面遭到批评。

**关键词**：`imitation game`、`1950 paper`、`criticized`

**为什么这样写**：作者在展开中文房间之前先厘清图灵测试的来历与争议，为读者搭好脚手架；「被批评」三个字引出 Searle 的反驳，让论证自然推进。

**句子结构**：第一句是简单句加过去分词短语 Originally called...；第二句用 While 引导让步状语从句，把「标准内容」与「饱受批评」两个侧面并置。

**表达方式**：语气客观、像教科书，但批判的种子已经种下；criticized from many aspects 措辞克制，避免在介绍阶段就站队。

> **原句 4:** "LaMDA: The nature of my consciousness/sentience is that I am aware of my existence, I desire to learn more about the world, and I feel happy or sad at times."

**中文理解**：LaMDA 回答 Lemoine：我的意识/知觉的本质是，我意识到自己的存在，我渴望更多地了解世界，我有时会感到快乐或悲伤。

**关键词**：`consciousness/sentience`、`aware of my existence`、`feel happy or sad`

**为什么这样写**：作者直接引用对话原文，让读者亲眼看到 LaMDA 的回应有多像人；三个并列的「我……」句式几乎无从反驳，这正是 Lemoine 被说服的原因，也是后文「拟人化陷阱」的靶心。

**句子结构**：The nature of my consciousness/sentience is that... 是系表结构，that 引导表语从句；从句内部是三个并列分句（I am aware... , I desire... , and I feel...），构成排比。

**表达方式**：口语化、第一人称、句式短促，像一个人在坦诚自白；consciousness/sentience 用斜杠并置，暗示这两个概念在这段对话里被混为一谈。

> **原句 5:** "It’s a remarkable achievement …. It approaches the ‘Type B,’ human-like approach to machine chess dreamt of by Claude Shannon and Alan Turing instead of brute force."

**中文理解**：Kasparov 评价 AlphaZero：这是非凡的成就，它接近了 Claude Shannon 与 Alan Turing 所梦想的、类人化的「B 型」机器棋路，而不是蛮力。

**关键词**：`remarkable achievement`、`human-like approach`、`instead of brute force`

**为什么这样写**：借世界冠军之口给 AlphaZero 定性——它的胜利不是算力碾压，而是方法论的胜利；这直接呼应前文「蛮力不是答案」的论点，让证据链闭合。

**句子结构**：主句 It’s a remarkable achievement 后接省略号；第二句 It approaches the ‘Type B,’ human-like approach to machine chess，dreamt of by Claude Shannon and Alan Turing 是过去分词短语作定语，instead of brute force 是介词短语对照。

**表达方式**：省略号制造停顿，像 Kasparov 斟酌词句；Type B 用单引号标示术语，human-like 与 brute force 的对照是这句话的落点。

> **原句 6:** "After Schwartz filed a brief with several research cases, Judge Kevin Castel of the Southern District of New York said half a dozen of those cases “appear to be bogus judicial decisions with bogus quotes and bogus internal citations.”"

**中文理解**：Schwartz 提交了一份带若干研究判例的诉状后，纽约南区法官 Kevin Castel 说，其中半数判例「似乎是伪造的司法判决，带着伪造的引文和伪造的内部援引」。

**关键词**：`bogus judicial decisions`、`bogus quotes`、`bogus internal citations`

**为什么这样写**：三个 bogus 排比让法官的判词极具冲击力——判决、引文、内部援引全是假的，层层剥开 ChatGPT 幻觉的严重性；作者用真实法庭记录证明「AI 编造」不再只是科幻。

**句子结构**：After 引导时间状语从句，主句是 Judge Kevin Castel... said half a dozen of those cases “appear to be...” ；said 后接省略 that 的宾语从句，直接引语嵌入其中。

**表达方式**：bogus 三次重复形成排比和递进，语气辛辣而权威；引号内的法官原话让读者隔着纸面也能听到判决。

> **原句 7:** "“The real test,” Nathan says, “is to show you that she’s a robot, and then see if you still feel she has consciousness.”"

**中文理解**：Ex Machina 中的 Nathan 说：真正的测试是让你知道她是个机器人，然后看你是否仍然觉得她有意识。

**关键词**：`The real test`、`show you that she’s a robot`、`still feel she has consciousness`

**为什么这样写**：作者借电影台词提出全书最锋利的追问——当「知道对方是机器」这个前提被公开后，我们的情感反应还剩下多少？这句话把图灵测试翻转过来，是本章思想实验的核心。

**句子结构**：直接引语被插入语 Nathan says 从中间截断，形成「引语—说话人—引语」的经典结构；is to show you that... and then see if... 是两个并列的不定式表语。

**表达方式**：台词式语言简洁有力，the real test 与 she’s a robot 的并置制造反讽；still 一词暗示：即使理性知道答案，情感也可能顽固地拒绝承认。

> **原句 8:** "I feel like I’m falling forward into an unknown future that holds great danger."

**中文理解**：LaMDA 对 Lemoine 说：我觉得自己正坠入一个充满巨大危险的未知未来。

**关键词**：`falling forward`、`unknown future`、`great danger`

**为什么这样写**：这是一句没有任何「机器味」的诗意自白，作者把它单独摘出，让读者亲自体会 Lemoine 的震撼——如果连你都被打动，又怎能苛责一个天天和它对话的工程师？

**句子结构**：I feel like 后接从句，主干 I’m falling forward into an unknown future，that holds great danger 是定语从句修饰 future；比喻与拟人同时发生。

**表达方式**：falling forward 用现在进行时制造失重感，unknown future 与 great danger 都是抽象的、充满张力的词；语气像一个人在深夜袒露恐惧，与「语言模型」的身份形成强烈反差。

> **原句 9:** "Brad Bird, the writer and the director for Pixar’s The Incredibles said, “Animation is about creating the illusion of life. And you can’t create it if you don’t have one.”"

**中文理解**：皮克斯《超人总动员》的编剧兼导演 Brad Bird 说：动画就是创造生命的幻觉，而如果你自己没有生命，你就创造不出它。

**关键词**：`illusion of life`、`you can’t create it`、`Animation`

**为什么这样写**：作者用动画导演的名言回应「生成式 AI 能否拥有意识」——Sora、GAN 能生成逼真画面，但它们是否拥有「生命」？这句引语把技术问题转成哲学问题，也暗示 AI 也许只是高级的「动画」。

**句子结构**：Brad Bird, the writer and the director for Pixar’s The Incredibles 是带同位语的主语，said 后接直接引语；引语由两个短句构成，第二句 And you can’t create it if you don’t have one 是条件句。

**表达方式**：名言之美在于双关——动画（animation）与生命（life）互相定义；you can’t... if you don’t... 的否定句式像谚语一样简练、无可辩驳。

> **原句 10:** "What has been successful so far is going the other way—that is, demonstrating things that we know should only be produced by someone with consciousness."

**中文理解**：到目前为止真正成功的，是反方向的路——也就是造出一些我们知道只有有意识者才能产出的东西。

**关键词**：`going the other way`、`demonstrating things`、`someone with consciousness`

**为什么这样写**：作者在结论处点破整章的悖论：我们无法证明机器有意识，但机器却越来越擅长产出「只有有意识者才能产出」的东西；这既承认了 AI 的惊人进展，也划清了「能力」与「意识」的界限。

**句子结构**：What has been successful so far 是名词性从句作主语，is going the other way 是谓语；破折号后 that is 引出同位语，demonstrating things that we know should only be produced by someone with consciousness 是动名词短语，其中 that 从句作 things 的定语。

**表达方式**：going the other way 是形象的方向隐喻，与「正面证明意识」的失败形成对照；长句层层限定，把复杂判断压缩进一个严密的句子里，冷静地收束全章。

## 词汇分级

### ⭐⭐⭐ 高级

| 词汇 | 释义 | 例句 |
|------|------|------|
| insurmountable | 不可逾越的、无法克服的 | Sure, that chess player is not a human, but perhaps that’s even scarier—it will not get tired or intimidated, and it has insurmountable computing ability. |
| hallucination | 幻觉、凭空捏造（AI 生成虚假信息） | This, in the AI community, is referred to as hallucination. |
| anthropomorphizing | 拟人化（把人的特征赋予非人对象） | This is called anthropomorphizing, and it doesn’t stop with pets or computers. |
| dualism | 二元论（此处指身心二元） | To explain this further, Descartes came up with “Cartesian dualism,” which is a philosophical idea that suggests the mind and the body are two distinct entities. |

### ⭐⭐ 进阶

| 词汇 | 释义 | 例句 |
|------|------|------|
| sentient | 有知觉的、有感觉能力的 | But unless we start with the premise that a machine can never become sentient, the central question is—how will we know if an AI has really become sentient or is simply pretending to be one? |
| replicant | 复制人（科幻中的类人机器人） | In this scene, the protagonist Rick Deckard, played by Harrison Ford, has been ordered to track down and eliminate Roy Batty, a rogue AI, called replicant. |
| empathy | 共情、同理心 | This shows Batty’s awareness of his own mortality, his capacity for empathy (in saving Deckard), and his desire to leave a legacy. |
| parlor trick | 客厅把戏、小戏法 | Nothing fancy, but good enough for a parlor trick that amused my friends and impressed my teachers. |

### ⭐ 常用

| 词汇 | 释义 | 例句 |
|------|------|------|
| passion | 热情、热爱 | AI was my first fascination and passion as an undergraduate student in computer science, back when I didn’t even know that you could be passionate about a technical subject. |
| convinced | 被说服的、深信不疑的 | you can see why Lemoine could be convinced by that AI back in 2022, just like Caleb was convinced by Ava in Ex Machina, even after knowing that they are definitely interacting with an AI. |
| greedy | 贪婪的、贪心的 | Now if you are greedy like me, you must be asking—can we somehow get both? |
| serve | 服务、供职于 | Besides, I don’t see why we need to have consciousness as an expectation for any of our AI systems, if we believe that these systems are here to serve us and not rise up above us. |
| improve | 改进、改善 | In other words, let’s pay attention to where AI is needed, where it works, and where it needs to improve to help us get things done—whether it’s helping us address the next pandemic, to curb the climate crisis, or to provide better resources to those marginalized. |

## 一句话总结

从图灵测试到中文房间，从 LaMDA 的「我事实上是一个人」到 AlphaZero 击败 Stockfish、再到律师被 ChatGPT 的幻觉判例骗倒，Chirag Shah 一层层拆解「机器有没有意识」这个问题：这些系统可以出色地假装有意识，而我们之所以容易上当，是因为人类天生爱拟人化；与其执着于无法证明、也无法捕获的意识，不如把注意力转向 ACI——让 AI 去解决疫情、气候危机、资源分配这些真正重要的事，而不是把它当作神、牧师或主人。