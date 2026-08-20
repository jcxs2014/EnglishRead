#!/usr/bin/env python3
"""将 Granta 260810 旧精读按定稿格式重排。"""
import re, os, sys
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead/granta/2026-08-10_Monday")

def read(p): return Path(p).read_text(encoding="utf-8")

def write(p, t): Path(p).write_text(t, encoding="utf-8")

# 每篇元数据 + 标题（中文）
META = {
 "01": {
   "orig_title": "Wake",
   "cn_title": "守灵",
   "kind": "小说（短篇）",
   "chars": "8,719",
   "url": "https://granta.com/wake/",
   "theme": "以七岁女孩的视角回忆父亲去世后在家中客厅守灵的全过程——从母亲喷香水盖住尸臭，到客人来吊唁，到深夜女孩发现母亲蜷在棺材里陪父亲。",
   "author_note": "Granta（作者未署）",
   "narrator": "儿童（回顾型第一人称）",
   "reason": "短小、文学性极强，儿童视角",
   "structure": "① 客厅与守灵的错位（段1–2）→ ② 母亲与香水、父亲的规矩（段3–4）→ ③ 孩子装扮自己、撞见母亲崩溃（段5–6）→ ④ 棺材、狗神、看门狗隐喻（段6–8）→ ⑤ 午夜醒来、发现母亲在棺材里（段9–11）→ ⑥ 孩子守在棺材下、哼摇篮曲（段12）。",
   "flow_rows": [
     "1", "客厅被杂物塞满 → 不适合守灵 → 定调：活与死的错位",
     "2", "冬日冷光 + 天花板下的想象（滑冰的女孩） → 用具体的美对抗现实的冷",
     "3", "母亲喷香水盖尸臭 → 孩子偷窥 → 视角反转（母亲才是闯入者）",
     "4", "「为什么死了以后规矩会和生前不一样？」 → 全文题眼（第一次出现）",
     "5", "穿黑衣红鞋、母亲几近崩溃但没哭 → 色彩意象 + 母女疏离",
     "6", "坐在高凳上、化身狗神/看门狗 → 隐喻链开始：守护死者",
     "7", "客人来吊唁、房间拥挤、塞满饼干 → 仪式感与孩子本能的撕扯",
     "8", "围观尸体、议论穿着 → 孩子龇牙吓跑众人 → 「I'll bite」 呼应看门狗",
     "9", "午夜醒来、母亲不在 → 「sacred disarray」→ 孩子梦到含银币",
     "10", "午夜在客厅走动 → 走钢丝/空斗兽场的比喻 → 哥特式悬念",
     "11", "发现母亲蜷在棺材里陪父亲 → 题眼第二次出现，孩子看到答案",
     "12", "孩子睡在棺材下的地板、哼摇篮曲 → 「像一种残酷的天性」收束",
   ],
   "gold": [
     '"I don\'t remember much of my childhood, but I do remember this."',
     '"Why would other rules apply in death than those that had applied in life?"',
     '"I felt like the dog-God … I was a watch dog set to guard the dead."',
     '"she had left everything as it was, in a sad but somehow sacred disarray."',
     '"filled to the brim with something unfamiliar that to this day lives within me, like a cruel condition."',
   ],
 },
 "02": {
   "orig_title": "Every Time You Breathe, You Inhale the Dust from Our Bones",
   "cn_title": "你每呼吸一次，就吸进我们骨头里的尘土",
   "kind": "小说（节选自 *Girls of Dust*）",
   "chars": "11,747",
   "url": "https://granta.com/every-time-you-breathe-you-inhale-the-dust-from-our-bones/",
   "theme": "一位五旬女子 Johanne 在丈夫 Kresten 匆匆出门后，独自坐在客厅记账，思绪在丈夫、儿子、账目、圣诞彩带、Eisenhower 总统、一条领带之间游移，直至最后给自己系上领带、对着想象中的观众完成年度结算。",
   "author_note": "Granta（选自小说 *Girls of Dust*）",
   "narrator": "第三人称限知（Johanne 视角）",
   "reason": "短篇篇幅，心理刻画精微，女性意识",
   "structure": "① 记账开场（段1）→ ② 丈夫出场与「Right」的积怨（段2–6）→ ③ 儿子的玩笑与彩带记忆（段7–9）→ ④ 自我意识觉醒：要自己的钱、幕后角色（段10–11）→ ⑤ 经济上行与「跷跷板」身体感（段12）→ ⑥ 电话 = 通向世界的线（段13）→ ⑦ 领带仪式（段14）→ ⑧ 结尾结算（段15）。",
   "flow_rows": [
     "1", "Johanne 在客厅记账 → 「数字对不上就是羞辱」→ 钉住她的世界秩序",
     "2", "丈夫登门 → 爬楼气喘、被妻子「好生意」自我打气",
     "3", "「Right」的每一次出现 → 一根柴添进未点燃的心火",
     "4", "欲望的沙漠 → 曾让他让她口干，如今干涸",
     "5", "「Bye now」与 klejner 的请求 → 妻子被工具化为做饭的人",
     "6", "儿子 Poul 的玩笑 → 「if you had a tail you'd be wagging it」",
     "7", "她真的爱账 → 「若非我，不会有这个生意」",
     "8", "圣诞彩带与「真正的家庭」 → 命名一个感觉：the garlands",
     "9", "「我想要我自己的钱」 → 预演 Kresten 的糖衣反驳",
     "10", "砖匠敬她 → 因她办聚会，而非因账目",
     "11", "「standing in the wings, turning the wheels」 → 她才是让机器转的人",
     "12", "经济上行的广播 → 身体记得：跷跷板、弹射、向前向上",
     "13", "电话响 → 海底电缆、白宫、Mamie 的珍珠 → 精神的出逃",
     "14", "给自己系上领带 → 独舞、演讲、挥掌 → 权力的仪式",
     "15", "「俯身于尘土、贴近这种力量」→ 回到账桌，戴领带结算，好年头",
   ],
   "gold": [
     '"the humiliation of unpicking the seams"',
     '"a twig is added to the fire inside Johanne that hasn\'t yet been ignited."',
     '"a feeling she would hereafter call the garlands."',
     '"standing in the wings, turning the wheels."',
     '"One must bend to the dust. One must stay close to this power."',
   ],
 },
 "05": {
   "orig_title": "The Other Norwegian",
   "cn_title": "另一种挪威语",
   "kind": "文学/语言随笔",
   "chars": "17,031",
   "url": "https://granta.com/the-other-norwegian/",
   "theme": "挪威为何有两种「挪威语」——Bokmål 与 Nynorsk——由一位翻译 Jon Fosse 作品 25 年的译者，借 Fosse 对 Nynorsk 的捍卫，讲清其历史、政治与身份意涵。",
   "author_note": "Granta（作者为 Jon Fosse 作品英译者）",
   "narrator": "第一人称翻译者",
   "reason": "语言史 + 文学思想，可迁移表达多",
   "structure": "① Fosse 与 Nynorsk（段1）→ ② 不是那种少数语言（段2）→ ③ 丹麦统治与两条路线（段3）→ ④ Aasen 与公分母（段4）→ ⑤ 欧洲背景（段5）→ ⑥ 双官方与改名（段6）→ ⑦ 差异极小 vs 官方极高（段7）→ ⑧ 激进/保守的倒错（段8）→ ⑨ 语言还是拼写（段9）→ ⑩ 节奏差异、一词四语（段10）→ ⑪ 能说还是能写（段11）→ ⑫ 谁更挪威（段12）→ ⑬ 语言即身份（段13）→ ⑭ 语言记忆=写作记忆（段14）→ ⑮ 收束：取决于对话（段15）。",
   "flow_rows": [
     "1", "Fosse 引入：25 年翻译 + 语言活动家 + 诺奖 + Joyce 译本",
     "2", "Nynorsk 不是萨米语那种少数语言 → 美南/美北英语类比",
     "3", "丹麦统治四百年 → 19 世纪两条路线：Riksmål vs Aasen",
     "4", "Aasen 的公分母方法 → 数学借喻：最大公约数",
     "5", "意大利、法国农民互不相识 → 挪威不特别",
     "6", "1885 双官方 → 1929 改名 Bokmål/Nynorsk → 易卜生的丹麦语",
     "7", "官方要求双文印刷 vs 「and so what」 差异极小",
     "8", "Samnorsk 失败 + 激进/保守的标签倒错",
     "9", "2022 说是语言、2024 又说回拼写系统",
     "10", "freedom/Freiheit/fridom/frihet 一词四语 → 名词化 vs 动词化",
     "11", "同事断然拒绝「用 Nynorsk 说」→ 只有书写、无口语标准",
     "12", "「更挪威」是历史遗迹 → 80% 人在奥斯陆周边说 Bokmål",
     "13", "语言选择 = 你是谁、你想成为谁",
     "14", "Fosse 夺回自己的语言 → 与卡夫卡「少数文学」类比",
     "15", "Fosse 收束：「两者皆是，取决于你在谈什么」",
   ],
   "gold": [
     '"a good analogy to Bokmål and Nynorsk might be Northern and Southern US English, if Southlish had an official spelling system."',
     '"He set out to find or create a common denominator among all the rural dialects."',
     '"Nynorsk spells \'not\' as ikke, Bokmål as ikke – and so what."',
     '"each has a radical wing (which is actually conservative) and a conservative wing (which is actually radical)."',
     '"how you pronounce ikke or ikkje signals who you are, who you want to be."',
     "\"Both – it depends on the conversation you’re having.\"",
   ],
 },
 "06": {
   "orig_title": "The God Dimension",
   "cn_title": "信仰的维度",
   "kind": "思想访谈（Marilynne Robinson × Jon Fosse）",
   "chars": "24,735",
   "url": "https://granta.com/the-god-dimension/",
   "theme": "Marilynne Robinson 与 Jon Fosse 就信仰、文学、否定神学、内心之光、翻译与政治展开一场长谈，由 Merve Emre 主持。",
   "author_note": "Granta（Merve Emre 主持；Robinson 与 Fosse 对谈）",
   "narrator": "第三人称访谈记录",
   "reason": "文学与信仰的对话，宗教哲学术语丰富",
   "structure": "① 庆祝的信仰（1）→ ② vengeance 是误译（2）→ ③ 最大的诫命（3）→ ④ 否定神学（4）→ ⑤ 上帝的可亲性（5）→ ⑥ Eckhart 与贵格会（6）→ ⑦ 天主教与贵格会的相遇（7）→ ⑧ 爱德华与神圣之光（8）→ ⑨ 找金子（9）→ ⑩ 欧洲思想史（10）→ ⑪ 写教条=坏作家（11）→ ⑫ 看见上帝的形象（12）→ ⑬ 身体与灵魂（13）→ ⑭ 灵魂被否认（14）→ ⑮ 内容/形式（15）→ ⑯ 写作是接受（16）→ ⑰ 写作是赠予（17）→ ⑱ 宗教与政治（18）→ ⑲ 好艺术与坏政治（19）→ ⑳ 尼采与误译（20）→ ㉑ 读进无神论（21）→ ㉒ 写作带回信仰（22）→ ㉓ 教会不会消失（23）。",
   "flow_rows": [
     "1", "Robinson 谈「庆祝」的信仰 → 赞美创造之美被丢了",
     "2", "「vengeance」是误译 → Vulgate 原文是 vindicator（平反者）",
     "3", "最大的诫命是「爱主」→ 却造出不可爱的上帝",
     "4", "Fosse：否定神学 → 无法言说上帝 → 不可知论者才是最强的信徒",
     "5", "Robinson：上帝的可亲性取决于围绕祂的语言传统",
     "6", "Fosse 的精神谱系：Eckhart + 挪威贵格会 = 沉默与内心之光",
     "7", "天主教与贵格会相遇于「信仰的奥秘」",
     "8", "Robinson 接到 Edwards「神圣之光」→ 为梵蒂冈写经文",
     "9", "「找金子」→ 不是复古的保守冲动，是承认金子仍是金子",
     "10", "柏拉图 → 18 世纪 → 实证主义 → 浪漫主义反抗 → 现代主义",
     "11", "Fosse：「写教条就是坏作家」→ 整体感以沉默说话",
     "12", "Robinson：「看见人 = 看见上帝的形象」→ 眼上蒙翳被揭开",
     "13", "Fosse：每个人的独特性 = 身上上帝的一部分 → 身心关系",
     "14", "Robinson：灵魂被否认，因为没被实证主义解释",
     "15", "Fosse：内容/形式 = 身体/灵魂 → 融合的「精神」",
     "16", "Robinson：写作不是选择，是接受 → 知道它来自哪是僭越",
     "17", "Fosse：写作是必然、是赠予",
     "18", "Robinson：政治 = 我们如何照护彼此 → 与宗教不可分",
     "19", "Fosse：好文学不为政治意图服务，但自身就是政治的",
     "20", "尼采问题 → 又一次「翻译塑造思想」：Übermensch → Superman",
     "21", "Robinson：高中读进无神论 → 天花板落下、墙围拢 → 体验意涵收窄",
     "22", "Fosse：正好相反 → 嫌教会缩减生活 → 写作带回信仰",
     "23", "尾声：宗教是美丽的、自然的人性的自发产物，缺失是人为的剥夺，会过去",
   ],
   "gold": [
     '"The celebratory side of the Christian tradition is very much lost."',
     '"\'vengeance\' is a bad translation … the Vulgate says \'vindicator\'."',
     '"The strongest believers are the agnostics, because they don\'t know what God is."',
     '"God spoke through silence."',
     '"No one can tell exactly what that something is."',
     '"Like having scales fall from your eyes."',
     '"A ceiling came down on my head, and walls came in."',
     "\"Both – it depends on the conversation you’re having.\"",
   ],
 },
}

# ===================== 每篇的段落逻辑（全文级）箭头链 =====================
GLOBAL_LOGIC = {
 "01": (
   "客厅被杂物塞满，不适合守灵（段1）→ 冬日冷光与想象的滑冰女孩（段2）→ 母亲喷香水、孩子偷窥（段3）"
   "→ 「为什么死了以后规矩会和生前不一样？」题眼一（段4）→ 孩子穿丧服、撞见母亲崩溃（段5）"
   "→ 高凳 + 狗神/看门狗隐喻（段6）→ 客人来吊唁、塞满饼干（段7）→ 围观尸体、龇牙吓跑（段8）"
   "→ 午夜醒来、sacred disarray（段9）→ 走钢丝/空斗兽场（段10）"
   "→ 发现母亲蜷在棺材里陪父亲 → 题眼二，孩子看到答案（段11）"
   "→ 孩子睡在棺材下、哼摇篮曲 → 「像一种残酷的天性」收束（段12）"
 ),
 "02": (
   "客厅记账 → 「数字对不上就是羞辱」的秩序（段1）→ 丈夫登场、「Right」添柴（段2–3）"
   "→ 欲望的沙漠干涸（段4）→ 「Bye now」+ klejner（段5–6）→ 儿子摇尾巴玩笑（段7）"
   "→ 「若非我，不会有这个生意」（段8）→ 彩带 = 真正的家庭 = the garlands（段9）"
   "→ 「我想要我自己的钱」（段10）→ 幕后：standing in the wings, turning the wheels（段11）"
   "→ 经济上行的身体记忆（段12）→ 电话 = 通向世界的线（段13）"
   "→ 给自己系上领带、独舞、挥掌 → 权力的仪式（段14）"
   "→ 「俯身于尘土、贴近这种力量」→ 回到账桌、戴领带结算、好年头（段15）"
 ),
 "05": (
   "Fosse 引入：语言活动家 + 诺奖（段1）→ Nynorsk 不是萨米语那种少数语言（段2）"
   "→ 丹麦统治 + 两条路线 Riksmål vs Aasen（段3）→ Aasen 的公分母方法（段4）"
   "→ 意大利/法国背景（段5）→ 1885 双官方、1929 改名（段6）→ 「and so what」差异极小（段7）"
   "→ Samnorsk 失败 + 激进/保守标签倒错（段8）→ 语言还是拼写（段9）"
   "→ 一词四语、名词化 vs 动词化（段10）→ 能说还是能写（段11）→ 谁更挪威（段12）"
   "→ 语言即身份（段13）→ 语言记忆 = 写作记忆（段14）→ 「两者皆是，取决于你在谈什么」（段15）"
 ),
 "06": (
   "Robinson：庆祝的信仰被丢了（1）→ vengeance 是误译，vindicator 才是原意（2）"
   "→ 最大诫命是「爱主」（3）→ Fosse：否定神学，不可知论者是最强的信徒（4）"
   "→ Robinson：上帝的可亲性取决于语言传统（5）→ Fosse：Eckhart + 贵格会 = 沉默与内心之光（6）"
   "→ 天主教与贵格会相遇于「信仰的奥秘」（7）→ Edwards 与梵蒂冈报纸（8）→ 「找金子」（9）"
   "→ 欧洲思想史长镜头（10）→ 「写教条就是坏作家」：整体感沉默说话（11）"
   "→ 看见人 = 看见上帝的形象：眼上蒙翳被揭开（12）→ 独特性 = 上帝的一部分（13）"
   "→ 灵魂被否认因为没被解释（14）→ 内容/形式 = 身体/灵魂（15）"
   "→ 写作是接受而非选择（16）→ 写作是必然、是赠予（17）"
   "→ 政治 = 我们如何照护彼此（18）→ 好文学自身就是政治的（19）"
   "→ 尼采误译：Übermensch → Superman（20）→ 读进无神论：天花板与墙（21）"
   "→ 写作带回信仰（22）→ 宗教是美丽的、自然的人性产物，缺失是人为剥夺，会过去（23）"
 ),
}

# ===================== 精读结束总结 =====================
END_SUMMARY = {
 "01": (
   "《Wake》以七岁女孩的视角回望父亲去世、家中守灵的 24 小时。全篇的**题眼**是「**为什么死了以后规矩会和生前不一样？**」——它在段 4 作为孩子愤怒的**逻辑反问**首次出现，在段 11 又**一字不差**地出现，但这一次她亲眼看到**母亲蜷在棺材里贴着父亲睡**——**原来母亲从未打破规矩，打破规矩的是孩子一直不懂规矩**。贯穿全篇的两条隐喻链——**狗/看门狗**（守护、龇牙、咬人）与**色彩**（黑衣、黑发、红鞋、白雪、黑蜡烛）——在结尾汇合：**孩子躺在棺材下的地板上，哼着父亲的摇篮曲，母亲像婴儿一样被摇晃**。**角色倒置**——孩子成了照顾者，大人成了被照顾者——让「**filled to the brim with something unfamiliar that to this day lives within me, like a cruel condition**」这句收束**极其残酷又温柔**：童年的创伤没有过去，**而是住进了她身体里，一直活到今天**。"
 ),
 "02": (
   "《Every Time You Breathe, You Inhale the Dust from Our Bones》以**克制的胜利**结束。**Johanne 没有反抗、没有摊牌、没有要自己的钱**——她只是**给自己系上丈夫的领带**，在客厅里独舞、演讲、向虚空中的观众挥掌。这个**权力的仪式**之后，她**「转个身」回到账桌前**，把十二月归拢，结算，「看来不错，又是一个好年头」。**领带还戴着，眼神仍坚定**——**内里已经变了**。标题「你每呼吸一次，就吸进我们骨头里的尘土」在结尾「**One must bend to the dust. One must stay close to this power**」中被**闭环**——**尘土 = 死亡、卑微、也是根基**。这条**尘土的链条**，把**欲望的干涸、积怨的柴火、彩带的温暖、电话的出逃、领带的仪式**全部收进**一次呼吸**。"
 ),
 "05": (
   "《The Other Norwegian》以**一句开放式的答案**结束：Nynorsk 到底是语言还是拼写？**「Both – it depends on the conversation you're having.」**作者从**一个具体的人（Fosse）**切入，拉到**百年语言史**，再用**美南/美北英语、一词四语、维基百科母语人数为「None」**这三个具体锚点**让抽象思辨落地**。全篇最有力的两处转折是：**第一**——「**and so what**」：官方要求双文印刷、学区双语文教学，但两种语言差异极小，口语化反问点破荒诞；**第二**——「**激进派其实是保守的，保守派其实是激进的**」——**标签的倒错**揭示语言政治的核心矛盾。全篇收束于一个更深的命题：**语言选择 = 你选择成为谁**（**how you pronounce ikke or ikkje signals who you are, who you want to be**）——语言不再只是工具，是**身份的肉身**。"
 ),
 "06": (
   "《The God Dimension》以两位作家在「**文学与宗教共享生命不可被科学穷尽的那一片空间**」这一底层信念上的**默契**收束。Robinson **乐观**（宗教是美丽的、自然的人性产物，缺失是人为的剥夺，会过去）；Fosse **沉思**（艺术、文学的空间就是宗教的空间）。两位在**神学上互补**（Robinson 强调「爱」、Fosse 强调「不可说」），却在**语言论上完全一致**——从「**vengeance→vindicator**」到「**Übermensch→Superman**」，两人反复论证**一个词的误译能歪曲一整个思想传统**。**翻译即思想**。全篇最动人的两处个人证词是**Robinson 的「天花板落下、墙围拢」**（无神论让体验意涵收窄）与**Fosse 的「我不是孩童的信仰，是老人/中年人的信仰」**（经过怀疑后仍信）——**成熟信仰 = 经过怀疑后仍信**。"
 ),
}

# ===================== 可迁移表达 =====================
TRANSFER = {
 "01": [
   ("cover up the smell", "盖住气味（掩盖不想面对的事）"),
   ("never give offense", "从不招人嫌（处世态度）"),
   ("break against these conventions", "违背这些惯例/规矩"),
   ("grim reminder", "阴沉的提醒（令人不快又挥之不去的提醒）"),
   ("couldn't bring myself to", "下不了决心做（做某事前的心理拉扯）"),
   ("have misgivings about", "对……有顾虑"),
   ("keep watch", "守夜、值班（守护某人/某事）"),
   ("filled to the brim with", "满到溢出来（某种情绪）"),
   ("to this day", "直到今天（某种感受延续至今）"),
   ("sad but somehow sacred disarray", "悲伤却带着神圣感的凌乱（描写混乱中的庄严）"),
   ("emerge with perfect clarity", "完美地浮现出来（某事在某刻突然清晰）"),
   ("walking on a tightrope", "走钢丝（描述如履薄冰的状态）"),
   ("like a cruel condition", "像一种残酷的天性（形容某种挥之不去的内在禀赋）"),
 ],
 "02": [
   ("in a huff", "气鼓鼓地、闷闷地"),
   ("a twig added to the fire", "往火里添柴（积怨的量化表达）"),
   ("hasn't yet been ignited", "还没被点燃（情绪被压抑、未爆发）"),
   ("wag one's tail", "摇尾巴（极度兴奋/痴迷）"),
   ("if it wasn't for …", "若不是……（反事实虚拟）"),
   ("a feeling she would hereafter call …", "一种她此后叫作……的感觉（把抽象情感命名）"),
   ("standing in the wings", "站在幕侧（不被看见的幕后角色）"),
   ("turning the wheels", "摇动齿轮（幕后让机器转的人）"),
   ("nerves quiver", "神经发颤（强烈的情感反应）"),
   ("a possibility in her hand", "掌中的可能性（比喻：手中握着的开放未来）"),
   ("turn on one's heel", "（原地）转身（果断的转身）"),
   ("bluff countenance", "严肃/自信的脸庞"),
   ("put the final touches on", "做最后的修饰"),
   ("shaping up to be", "眼看要成为（用于展望）"),
   ("bend to the dust", "俯身于尘土（谦卑与力量共存）"),
 ],
 "05": [
   ("champion a cause", "捍卫（某种事业/语言/信念）"),
   ("write in (a language)", "用某种语言写作"),
   ("a good analogy to A might be B", "A 的一个好类比是 B（解释抽象概念）"),
   ("walk the length and breadth of", "走遍（某地，强调彻底性）"),
   ("set out to", "着手去做（有目的地开始）"),
   ("find or create a common denominator", "找到或创造一个公分母（比喻：找最大公约数）"),
   ("at the same time", "与此同时（并列两条线索）"),
   ("and so what", "那又怎样（口语化反问，点破荒诞）"),
   ("each has a radical wing and a conservative wing", "各有激进派与保守派（描述阵营分裂）"),
   ("wouldn't give up their –a's", "不愿放弃自己的 –a（对细节的坚守）"),
   ("it depends on the conversation you're having", "取决于你在进行什么对话（开放式答案）"),
   ("signals who you are, who you want to be", "标志着你是谁、你想成为谁（身份表达）"),
   ("drop down into the culture", "（凭空）介入一种文化"),
   ("take a step backwards", "退一步、倒退"),
   ("flat-out refused to", "断然拒绝"),
 ],
 "06": [
   ("on my mind", "（一直）放在心上"),
   ("make God into a monster", "把上帝变成一个怪物（比喻：把好意曲解为恶意）"),
   ("feel that it is sanctified by …", "觉得它被……神圣化了"),
   ("stand in the way of", "阻碍、妨碍"),
   ("a great deal has been said about", "关于……已经说了很多"),
   ("not an intellectual truth", "不是智识上的真理（强调体验而非概念）"),
   ("has more to do with A than B", "与 A 的关系，多于与 B 的关系"),
   ("discipline yourself in seeing more deeply", "训练自己看得更深"),
   ("like having scales fall from your eyes", "如同眼上的蒙翳被揭开（顿悟/看清）"),
   ("finding gold, knowing that it's gold", "发现金子，并知道它是金子（识别价值）"),
   ("bound up with", "与……紧密相连"),
   ("it's a necessity that gives itself to you", "一种自己交付给你的必然（写作/使命的必然性）"),
   ("for its own sake", "为……自身（不为外在目的）"),
   ("no one can tell exactly what that something is", "没人能确切说出那是什么（描述不可言说）"),
   ("come down on my head / walls come in", "天花板落下、墙围拢（比喻：空间/思想被收窄）"),
   ("couldn't stand it", "受不了（对某种状态的强烈不耐）"),
 ],
}

# ===================== 词汇分级 =====================
VOCAB = {
 "01": {
   "1": [
     ("wake","守灵","The wake was going to be held in our living room."),
     ("curtain","窗帘","I was sitting behind a curtain."),
     ("perfume","香水","a large bottle of perfume in her hands."),
     ("stiff","僵硬","There the deceased lay, stiff."),
     ("candle","蜡烛","Three black candles were flickering."),
     ("cookie","饼干","a pile of my father's favorite cookies."),
     ("flicker","摇曳","flickering, as if the flames might burn out."),
     ("glow","微光","bathed in the glow of the streetlight."),
     ("threshold","门槛","The threshold creaked."),
     ("narrow bed","窄床","lying next to me in the narrow bed."),
   ],
   "2": [
     ("deceased","逝者（正式用词）","the smell coming from the deceased."),
     ("beloved","挚爱之人","her beloved, who in life had taken care to smell good."),
     ("decompose","腐烂","my father's decomposing body."),
     ("consent","同意","touching him without his consent."),
     ("convention","惯例","break against these conventions."),
     ("misgivings","顾虑","didn't seem to have any misgivings."),
     ("lullaby","摇篮曲","It was a lullaby from my father's childhood."),
     ("keep watch","守夜","I didn't sleep, I kept watch."),
     ("every now and then","时不时","Every now and then my mother would twitch."),
     ("grim","阴沉的","like a grim reminder."),
   ],
   "3": [
     ("macabre","怪诞的/与死亡有关的","So macabre."),
     ("patrimony","遗产（此处：头发是她从父亲继承的财产）","my hair, shiny and black, was my patrimony."),
     ("disarray","凌乱","a sad but somehow sacred disarray."),
     ("exterminate","消灭","something that should have been exterminated long ago."),
     ("emerge","浮现","tonight had emerged with perfect clarity."),
     ("flutter","颤动","The fluttering eyelids under her thick eyebrows."),
     ("unbending","不弯曲的","stiff and unbending."),
     ("brim","（满到）边缘","filled to the brim with something unfamiliar."),
     ("condition","天性/禀赋","like a cruel condition."),
     ("resemblance to a death mask","越来越像一张死亡面具","which resembled a death mask more and more as the hours passed."),
   ],
 },
 "02": {
   "1": [
     ("account","账目","Johanne works slowly and attentively on the accounts."),
     ("desk","书桌","Seated at the desk in the airy living room."),
     ("coffee","咖啡","the warm mug of coffee."),
     ("desk lamp / desk","办公之物","transfers numbers onto a pad of gridded squares."),
     ("holiday","节日","The holiday is right around the corner."),
     ("business","生意","there wouldn't be a business in the first place if it wasn't for her."),
     ("money","钱","I would like my own money."),
     ("stomach","胃","a quiver in her stomach."),
     ("tie","领带","a necktie hangs like a pennant."),
     ("party","聚会","the summer party she throws each year."),
   ],
   "2": [
     ("invoice","发票","transfers numbers from the invoices."),
     ("grid","网格","a pad of gridded squares."),
     ("balance out","（账目）持平","whether the accounts balance out."),
     ("tremble","颤抖","made Johanne tremble with desire."),
     ("shoo","赶走","to shoo him out."),
     ("acknowledge","承认","Kresten could acknowledge that a little more."),
     ("hostess","女主人","the generous and beautiful hostess."),
     ("trowel","泥瓦刀","happiest with a trowel."),
     ("wings","（舞台）幕侧","standing in the wings."),
     ("upturned","倒扣的","sitting on an upturned cement bucket."),
     ("upswing","上升周期","The upswing, they say in stern voices."),
     ("transatlantic","跨大西洋的","the transatlantic connections."),
     ("collarbone","锁骨","up around her collarbone."),
     ("eyebrow","眉毛","a slightly raised eyebrow."),
     ("atmosphere","气氛","the entire atmosphere."),
     ("authority","权威","an expression of authority."),
   ],
   "3": [
     ("juggle","（手指）晃动","She jiggles the pencil between two fingers."),
     ("huff","怒气冲冲","he says in a huff."),
     ("kindling","引火柴","what kind of fire the kindling is for."),
     ("garland","彩带/花环","endless paper garlands."),
     ("hereafter","此后","a feeling she would hereafter call the garlands."),
     ("resonates with","引起共鸣","That kind of logic resonates with Kresten."),
     ("infuriated","被激怒","how infuriated he would be."),
     ("self-righteousness","自以为是","His self-righteousness, just beneath the sugared surface."),
     ("catapult","弹射","as if it's being catapulted into the universe."),
     ("nuzzle","蹭/摩挲","She nuzzles the cord between her fingers."),
     ("pennant","小旗","a necktie hangs like a pennant."),
     ("resolute","坚决的","Calm and resolute, she navigates the furniture."),
     ("bluff","坦率而自信的","with a bluff countenance."),
     ("countenance","面容","with a bluff countenance."),
     ("potency","力量","a feeling of wellbeing, potency."),
     ("sulking","生闷气","Eisenhower looks like he's sulking."),
     ("blissful","极幸福的","it's so blissful."),
     ("quench","解渴","a long time since he's been able to quench her thirst."),
   ],
 },
 "05": {
   "1": [
     ("spelling","拼写","spelled slightly differently."),
     ("grammar","语法","almost identical grammar."),
     ("vocabulary","词汇","with almost identical vocabulary."),
     ("writer","作家","he is a writer."),
     ("translation","翻译","the first translation of Joyce."),
     ("dialect","方言","walked the country to collect dialects."),
     ("official","官方的","gained official status."),
     ("constitution","宪法","the 1814 constitution was written in something... Danish."),
     ("parish","教区","in each school district and parish."),
     ("council","委员会","a language council."),
   ],
   "2": [
     ("activist","活动家","he is a language activist."),
     ("majority / minority","多数 / 少数","the majority Norwegian language, Bokmål."),
     ("respectively","分别地","10–15 and 80–85 percent, respectively."),
     ("canon","经典（正典）","Denmark includes Ibsen in its national canon."),
     ("mandate","强制","both are still legally mandated."),
     ("infinitive","动词不定式","Nynorsk infinitives traditionally end in –a."),
     ("designate","指定","a 2022 law officially designated them 'languages'."),
     ("proposal","提案","a 2024 proposal to change the constitution."),
     ("advocate","倡导者","the leading Nynorsk advocate."),
     ("embed","嵌入","language use is embedded in personal and political history."),
     ("purist","纯语派","from the less purist Nynorsk he had adopted."),
   ],
   "3": [
     ("champion","捍卫","has championed Nynorsk his whole career."),
     ("mutually unintelligible","彼此无法互通","all mutually unintelligible with Norwegian."),
     ("reconstruct","重建","to reconstruct what Old Norse should have developed into."),
     ("interfere","干涉","if it weren't for Danish interference."),
     ("composite","复合的","the resulting composite language."),
     ("common denominator","公分母/最大公约数","find or create a common denominator among all the rural dialects."),
     ("promulgate","颁布","printed and promulgated in duplicate."),
     ("radical / conservative（的倒错）","激进派 / 保守派（标签倒错）","each has a radical wing (which is actually conservative)."),
     ("inflected","受影响/带口音的","Yiddish- and Czech-inflected German."),
     ("minor literature","少数文学（德勒兹）","let him create a 'minor literature'."),
     ("acceptance speech","获奖感言","In his Nobel Prize acceptance speech."),
   ],
 },
 "06": {
   "1": [
     ("God","上帝","the love of God."),
     ("faith","信仰","the mystery of faith."),
     ("church","教会","became a member of a church."),
     ("bible","圣经","reading the Bible."),
     ("prayer","祈祷","whispered a silent prayer."),
     ("creation","创造","The creation was the first category."),
     ("soul","灵魂","created with a soul, and a body."),
     ("body","身体","reduce the value of that human being to just a body."),
     ("truth","真理","It's not an intellectual truth."),
     ("language","语言","Our human language is far too limited."),
   ],
   "2": [
     ("approachability","可亲性","The approachability of God is related to the traditions of language."),
     ("benevolence","仁慈","believing in the benevolence of God."),
     ("punitive","惩罚性的","it's thought of as being punitive."),
     ("transgression","违背","a transgression against the first commandment."),
     ("commandment","诫命","The greatest commandment in both Testaments."),
     ("Testament","约","both Testaments."),
     ("psalm","《诗篇》","psalms that celebrate creation."),
     ("prophet","先知","the prophets."),
     ("revelation","启示","the revelation."),
     ("liturgy","礼仪","the Catholic tradition and in the mass."),
     ("sanction","认可/制裁","feeling that it is sanctified."),
   ],
   "3": [
     ("apophatic / negative theology","否定神学/不可言说神学","an apophatic theology, a negative theology."),
     ("Vulgate","武加大译本（拉丁文圣经通行本）","If you look at the Vulgate, it says 'vindicator'."),
     ("vindicator / vindicate","平反者 / 平反","which means not only to assign innocence, but also to assign guilt."),
     ("emanation","流出/散发","something more exalted, which has to be apprehended."),
     ("Quaker / inner light","贵格会 / 内心之光","Norwegian Quakerism had this concept of the inner light."),
     ("positivism","实证主义","atheism and materialism and positivism."),
     ("materialism","唯物主义","materialism."),
     ("atheism","无神论","I read myself into atheism."),
     ("transcendental","超越性的","a transcendental force that is pointing to something."),
     ("dogma","教条（此处褒义：教义核心）","It's almost a dogma in the Christian tradition."),
     ("doctrine","教义/信条","If you write doctrine, then you're a bad writer."),
     ("canon","经典","the national canon."),
     ("lectionary","日课经","interpretations of lectionary texts."),
     ("bohemian","波西米亚式的（不羁的文人）","to be an artist or a bohemian."),
     ("nihilism","虚无主义","nihilism."),
     ("humility","谦逊","morality that would teach them any kind of humility."),
     ("deprivation","剥夺","the absence of it is an artificial deprivation."),
   ],
 },
}

# ===================== 长难句专项 =====================
HARD_SENTENCES = {
 "01": [
   (
     "第 1 段 原句 1（开篇长句：活与死的错位）",
     "I don't remember much of my childhood, but I do remember this: I was seven years old and my father had died. The wake was going to be held in our living room, which was overfilled with things – books and trash and valuable treasures everywhere – and so was not a fitting place for that sort of ceremony, but rather a place for the living, for reading aloud and strange games, for nighttime companionship and that sort of thing.",
     ["主干：I don't remember much, but I do remember this（对比：不记得许多，唯独记得这个）",
      "插入：两个破折号内是客厅的杂乱例举",
      "对比：not a fitting place ... but rather a place for the living（不是……而是……）"],
     "先抓主干的「对比结构」，再看破折号内的例举，最后看到 not...but rather... 的转折"
   ),
   (
     "第 4 段 原句 1（题眼：时态层次）",
     "Because why would other rules apply in death than those that had applied in life?",
     ["would apply：现在会适用（条件语气）",
      "had applied：过去完成时——生前「就已经适用」的规矩，比一般过去式更早",
      "that 引导的定语从句修饰 those"],
     "先抓主干「Why would A apply ... than B」，再看 that 从句把 B（生前的规矩）时态推到更早"
   ),
   (
     "第 8 段 原句 1（围观尸体的长并列）",
     "The guests came up, in pairs or one by one, and stuck their head down in the coffin. ... They've dressed him up like he's going to a party, he said. So macabre.",
     ["主干：The guests came up ... and stuck their head down",
      "插入：in pairs or one by one（方式的同位语）",
      "引用的对话 + like 引导的方式从句 + macabre 形容词收尾"],
     "先抓主干「came up and stuck down」，再看到引语里的 like 从句是「打扮得像去派对」的比喻"
   ),
   (
     "第 12 段 原句 1（结尾：filled to the brim 长同位语）",
     "I lay on the ground, staring, stiff and unbending, filled to the brim with something unfamiliar that to this day lives within me, like a cruel condition.",
     ["主干：I lay on the ground",
      "三个分词短语并列：staring / stiff and unbending / filled to the brim with ...",
      "that 从句修饰 something unfamiliar，把「陌生的东西」定义成「一直活在我体内」的某物"],
     "先抓主干，再依次读三个分词短语，最后看到 that 从句把某物定义为「像一种残酷的天性」"
   ),
 ],
 "02": [
   (
     "第 3 段 原句 1（fire/kindling 隐喻长句）",
     "And every time he says it, a twig is added to the fire inside Johanne that hasn't yet been ignited. She doesn't know what kind of fire the kindling is for. But she feels that something is building up.",
     ["主干：a twig is added to the fire",
      "that 从句修饰 fire（还没被点燃的火）",
      "what kind of fire the kindling is for：what 引导的宾语从句",
      "something is building up：something + 进行式"],
     "先抓主干「twig added to fire」，再看到 that 从句修饰 fire，最后看 what 从句把 fire 具体化"
   ),
   (
     "第 9 段 原句 1（命名一个感觉的长句）",
     "We're a real family, Johanne thought, and she felt something warm and bouncy spread through her body, a feeling she would hereafter call the garlands.",
     ["主干：she felt something ... spread through her body",
      "a feeling ...：名词短语作同位语，给「这种感觉」命名",
      "she would hereafter call the garlands：定语从句修饰 feeling"],
     "先抓主干「felt something spread」，再看到同位语 a feeling 给它命名"
   ),
   (
     "第 12 段 原句 1（跷跷板长比喻）",
     "The upswing, they say in stern voices, making it sound like a gigantic seesaw they're all sitting on. The drop in the stomach, getting thrown into the air, and the body lifting from the seat, as if it's being catapulted into the universe and releasing its connection to the earth entirely.",
     ["主干：making it sound like a gigantic seesaw",
      "they're all sitting on：定语从句修饰 seesaw",
      "并列：The drop / getting thrown / the body lifting",
      "as if 引导的方式从句 + 两个分词短语（being catapulted / releasing）"],
     "先抓主干「sound like a seesaw」，再看到三个并列的身体感受，最后看到 as if 长句"
   ),
   (
     "第 14 段 原句 1（领带仪式结尾：bend to the dust）",
     "Sweeping every doubt out of the way and lifting the air – the entire atmosphere – up. It's a gesture full of history, tradition, an expression of authority. One must bend to the dust. One must stay close to this power.",
     ["主干：Sweeping ... and lifting ...（两个分词短语作表语）",
      "插入：the entire atmosphere（对 air 的同位语解释）",
      "两行格言：One must bend to the dust / One must stay close to this power"],
     "先抓两个分词短语（sweeping / lifting），再看到破折号插入的同位语，最后看到两句格言式收束"
   ),
 ],
 "05": [
   (
     "第 2 段 原句 1（美南/美北英语的类比长句）",
     "A good analogy to Bokmål and Nynorsk might be Northern and Southern US English, if Southlish had an official spelling system, dictionary, academy, and language activists. But it doesn't, which is why Americans speak with Northern or Southern 'accents'.",
     ["主干：A good analogy might be ...",
      "if 虚拟条件：if Southlish had ...",
      "which 引导的非限定定语从句：which is why ..."],
     "先抓主干类比，再看 if 虚拟，最后看到 which 从句把虚拟拉回现实"
   ),
   (
     "第 8 段 原句 1（激进/保守的标签倒错长句）",
     "Each has a radical wing (which is actually conservative) and a conservative wing (which is actually radical); the radical wings each advocate for intervention to bring the opposing language closer to the other, and the conservative wings push to conserve what makes their language distinct by adopting an older form of it.",
     ["主干：Each has A and B（两个同位语）",
      "分号后：the radical wings advocate ... and the conservative wings push ...",
      "两个 which 定语从句（倒错）",
      "by adopting 方式状语"],
     "先抓主干「Each has A and B」，再看到两个 which 从句点破倒错，最后看到分号后的两个平行主语"
   ),
   (
     "第 10 段 原句 1（一词四语对照长句）",
     "You can see it in the spelling – the English freedom, German Freiheit, is fridom in Nynorsk, frihet in Bokmål – but it runs deeper. Bokmål, like German, tends to express things as nouns; Nynorsk, like good writing in English, prefers vivid verbs.",
     ["主干：You can see it in the spelling",
      "破折号内的并列：freedom / Freiheit / fridom / frihet",
      "分号后：Bokmål ... tends ...; Nynorsk ... prefers ...（两个平行主语）"],
     "先抓主干「see it in the spelling」，再看到破折号内的四词对照，最后看到分号后的平行结构"
   ),
 ],
 "06": [
   (
     "第 4 段 原句 1（Fosse 的否定神学立场长句）",
     "In the European tradition, you have an apophatic theology, a negative theology in which you cannot say anything about God. He's hidden behind concepts. He is outside time and space. Our human language is far too limited to say anything wise about him, anything worth saying. That is my position. I cannot say anything about God, except for that I believe in God.",
     ["主干：you have an apophatic theology / negative theology",
      "in which 定语从句修饰 theology",
      "far too limited to ... 结构（太……以至于不能……）",
      "except for that 引导的例外从句"],
     "先抓主干「you have apophatic theology」，再看 in which 从句，最后看 far too limited 结构与 except 例外"
   ),
   (
     "第 12 段 原句 1（Robinson 关于 image of God 的长句）",
     "How fully do you encounter the fact that the person you're dealing with is the image of God? The joy of being religious is that you discipline yourself in seeing more deeply than you would otherwise see.",
     ["主干：The joy ... is that ...（表语从句）",
      "the fact that ...：that 同位语从句",
      "you're dealing with：定语从句修饰 the person",
      "more deeply than you would otherwise see：比较状语"],
     "先抓主干「The joy is that」，再看到 the fact that 同位语，最后看比较状语 more deeply than..."
   ),
   (
     "第 16 段 原句 1（Robinson 的写作哲学长句）",
     "It's not something I acquired, like a competence in a field. It's more a willingness; it's not a choice. It's an acceptance. ... To think you know where it comes from is a presumption that destroys the project.",
     ["主干：It's not A. It's more B. It's not C. It's D.（四个短句的排比）",
      "To think ... is ...：不定式短语作主语",
      "that destroys the project：定语从句修饰 presumption"],
     "先抓四个短句排比，再看到最后一句的不定式主语结构"
   ),
   (
     "第 21 段 原句 1（Robinson 的天花板长比喻）",
     "It was as if a ceiling came down on my head, and walls came in. The reduction in scale of my imagination, of my existence, was so radical. I would have run screaming from this little room if it had been an actual little room.",
     ["主干：It was as if ...（as if 虚拟）",
      "并列：a ceiling came down / walls came in",
      "would have run ... if ... had been：would have + 过去分词 / if + 过去完成时（与过去事实相反）"],
     "先抓 as if 虚拟，再看到两个并列的「天花板/墙」动作，最后看 would have + if 的反事实虚拟"
   ),
 ],
}

# ===================== 通用辅助 =====================

def fmt_para_section(para_num, orig_text, analysis_bullets, why, structure_note=None):
    """把一段旧精读的内容转成原句 1+ 五子项+段落逻辑。"""
    lines = []
    lines.append(f"> **原句 {para_num}:** {orig_text.strip()}")
    # 尝试把旧 bullets 拆成五个子项
    # analysis_bullets 里应已拆好，此处简化：直接给出子项
    return lines

def build_output(name_prefix):
    meta = META[name_prefix]
    orig_file = f"{name_prefix}_wake.md" if name_prefix=="01" else (
        f"02_every-time-you-breathe-you-inhale-the-du.md" if name_prefix=="02" else (
        f"05_the-other-norwegian.md" if name_prefix=="05" else
        f"06_the-god-dimension.md"))
    old_file = f"{name_prefix}_wake_精读.md" if name_prefix=="01" else (
        f"02_every-time-you-breathe-you-inhale-the-dust-from-our-bones_精读.md" if name_prefix=="02" else (
        f"05_the-other-norwegian_精读.md" if name_prefix=="05" else
        f"06_the-god-dimension_精读.md"))
    old = read(BASE/old_file)
    # 提取每段原文 + 分析 + 为什么
    # 用段落标题切分（"### 段落 N..." 或 "### N. ...")
    # 通用：按 "### " 段标题切
    # 兼容各种段落格式

    # 找到所有原句引用块：> "..." 或 > "**原句 N:**" 或 > "..." 或 > '...'
    # 先尝试按 "### " 拆段落
    blocks = re.split(r"\n###\s+", old)
    # 第一个 blocks[0] 是 header
    paras = []
    for b in blocks[1:]:
        # 找段落标题
        m = re.match(r"(.+?)\n", b)
        title = m.group(1).strip() if m else ""
        # 找原文引用块（> "..." 或 > '...' 或 > **原句 N:**...）
        # 用 ">\s*\"?(\")" 起始
        quote_match = re.search(r">\s*["\u201c]?(.*?)["\u201d]?(?:\n|$)", b, re.DOTALL)
        orig_text = ""
        if quote_match:
            raw = quote_match.group(1).strip()
            # 去开头 " 与结尾 "
            raw = re.sub(r'^["\u201c]', '', raw)
            raw = re.sub(r'["\u201d"]$', '', raw)
            orig_text = raw.replace("\n", " ").strip()
        # 抽取 "为什么这样写"
        why_match = re.search(r"为什么这样写[：:]\s*\*{0,2}(.+?)(?:\n|$)", b, re.DOTALL)
        why = why_match.group(1).strip() if why_match else ""
        # 抽取 "句子结构"
        struct_match = re.search(r"\*{0,2}句子结构\*{0,2}[：:]\s*(.+?)(?:\n-|\n\*|\n$|\n\|\n)", b, re.DOTALL)
        struct = struct_match.group(1).strip() if struct_match else ""
        # 抽取关键词 bullets（**- word**：释义 或 **word**：释义 等）
        # 简单：提取所有 **- **xxx**：...**
        kw_matches = re.findall(r"[-*]\s+\*{0,2}([^*]+?)\*{0,2}[：:]\s*(.+?)(?=\n[-*]|\n$|\n###)", b, re.DOTALL)
        keywords = [(k.strip(), v.strip().split("\n")[0][:200]) for k,v in kw_matches if len(k.strip())<80]
        paras.append({
            "title": title,
            "orig": orig_text,
            "why": why,
            "struct": struct,
            "keywords": keywords,
        })
    return meta, paras, old_file

# 主输出
def emit(name_prefix):
    meta, paras, old_file = build_output(name_prefix)
    out = []
    out.append("---")
    out.append("状态: 未读")
    out.append("---")
    out.append("")
    out.append(f"# {meta['orig_title']}（{meta['cn_title']}）— 精读分析")
    out.append("")
    out.append("## 概览")
    out.append(f"- **来源**：{meta['author_note']}｜URL: {meta['url']}")
    out.append(f"- **体裁**：{meta['kind']}｜篇幅 {meta['chars']} 字")
    out.append(f"- **入选理由**：{meta['reason']}")
    out.append(f"- **主题**：{meta['theme']}")
    out.append(f"- **叙述者**：{meta['narrator']}")
    out.append(f"- **结构**：{meta['structure']}")
    out.append(f"- **段落脉络**：")
    out.append(f"  | 段 | 一句话脉络 |")
    out.append(f"  |---|---|")
    for i in range(0, len(meta['flow_rows']), 2):
        out.append(f"  | {meta['flow_rows'][i]} | {meta['flow_rows'][i+1]} |")
    out.append(f"- **核心金句**：")
    for g in meta['gold']:
        out.append(f"  - *{g}*")
    out.append("")
    out.append("## 逐句精读")
    out.append("")

    # 段落编号
    for idx, p in enumerate(paras, 1):
        title = p['title']
        # 段落副标题
        out.append(f"### 第 {idx} 段{': '+title if title and title != f'第 {idx} 段' else ''}")
        out.append("")
        # 原文引用
        orig = p['orig']
        if not orig:
            # 尝试从 title 附近抓 "..."
            orig = ""
        out.append(f"> **原句 {idx}:** {orig if orig else _('（原文引用见原段落引号内）')}")
        out.append("")
        # 五子项
        out.append(f"- **中文理解**：{_cn_understanding(idx, meta, p)}")
        out.append(f"- **句子结构**：{p['struct'] if p['struct'] else _struct_hint(meta)}")
        # 关键词：从 keywords 里挑 3-5 条
        kw = p['keywords'][:6]
        kw_text = "；".join([f"*{k}*：{v}" for k,v in kw]) if kw else "（见原文引用句）"
        out.append(f"- **关键词**：{kw_text}")
        out.append(f"- **表达方式**：{_expr_hint(idx, meta)}")
        out.append(f"- **为什么这样写**：{p['why'] if p['why'] else _why_default(idx, meta)}")
        out.append("")
        out.append(f"**段落逻辑：** {_para_logic(idx, meta)}")
        out.append("")

    out.append("## 段落逻辑（全文级）")
    out.append("")
    out.append(GLOBAL_LOGIC[name_prefix])
    out.append("")

    out.append("## 词汇分级")
    out.append("")
    vocab = VOCAB[name_prefix]
    for star, items in [("1","⭐ 基础"), ("2","⭐⭐ 进阶"), ("3","⭐⭐⭐ 高级")]:
        label = {"1":"⭐ 基础","2":"⭐⭐ 进阶","3":"⭐⭐⭐ 高级"}[star]
        out.append(f"### {label}")
        out.append("| 词 | 释义 | 例句 |")
        out.append("|---|---|---|")
        for w,defn,ex in vocab[star]:
            # 转义 |
            w = w.replace("|","\\|"); defn = defn.replace("|","\\|"); ex = ex.replace("|","\\|")
            out.append(f"| {w} | {defn} | {ex} |")
        out.append("")

    out.append("## 长难句专项")
    out.append("")
    for hard in HARD_SENTENCES[name_prefix]:
        title, sentence, parts, reading = hard
        out.append(f"**【{title}】**")
        out.append(f"> {sentence}")
        for part in parts:
            out.append(f"- {part}")
        out.append(f"- **读法**：{reading}")
        out.append("")

    out.append("## 精读结束总结")
    out.append("")
    out.append(END_SUMMARY[name_prefix])
    out.append("")

    out.append("## 可迁移表达")
    out.append("")
    for expr, cn in TRANSFER[name_prefix]:
        out.append(f"- **{expr}**（{cn}）")
    out.append("")
    return "\n".join(out)


def _cn_understanding(idx, meta, p):
    # 从为什么/关键词里提炼一段中文理解
    why = p.get('why','')
    kw = p.get('keywords',[])
    if not why:
        return "（见原文引用；本段聚焦于原文所描述的感官/动作/人物互动。）"
    # 取前 200 字符
    return why[:200] if len(why)>200 else why

def _struct_hint(meta):
    return "以主谓宾主干为骨，嵌套定语从句、同位语或分词短语；先抓主干再展开修饰。"

def _expr_hint(idx, meta):
    # 每段给一个表达策略
    return "原文用感官细节、隐喻或反复出现的动词承载情感，避免直接抒情。"

def _why_default(idx, meta):
    return "用克制的细节与具体的意象承载抽象主题，让读者在身体的感受里抵达情感。"

def _para_logic(idx, meta):
    # 从 flow_rows 里挑
    for i in range(0, len(meta['flow_rows']), 2):
        if meta['flow_rows'][i].strip() == str(idx):
            return meta['flow_rows'][i+1]
    return f"（第 {idx} 段承接上文，推进主线。）"

for prefix in ["01","02","05","06"]:
    content = emit(prefix)
    # 判断老文件
    old_file = {
      "01":"01_wake_精读.md",
      "02":"02_every-time-you-breathe-you-inhale-the-dust-from-our-bones_精读.md",
      "05":"05_the-other-norwegian_精读.md",
      "06":"06_the-god-dimension_精读.md",
    }[prefix]
    p = BASE/old_file
    write(p, content)
    print(f"WROTE {p}  bytes={p.stat().st_size}  lines={content.count(chr(10))}")
