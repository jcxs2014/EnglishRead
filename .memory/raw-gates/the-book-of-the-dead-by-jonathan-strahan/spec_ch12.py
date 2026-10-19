# -*- coding: utf-8 -*-
"""ch12《A Shovel, a Rope, and a Bottle of Whiskey》（Samantha Mills）中文化规格。

原文依据：text/ch12_a_shovel_a_rope_and_a_bottle_of_whiskey_.txt
（已核实：作者署名 Samantha Mills、1882/1883 年费城、
Arthur Sullivan（叙述者，二十三岁，孤儿，掘尸人，无神论）、
Joseph（信神、怕来世）、Charlie Davis（送货人／威士忌掮客）、
一晚二十五美元、铲子（直挖墓头）、绳子（拖尸）、威士忌（壮胆）、
「他们不过是东西」，Arthur 的唯物论；Joseph 的「不是留下什么才可怕，是来世」、
Filippo Rossi（科学家，研究身体与灵魂之间的系绳）、
「我是个科学家，我在研究身体与灵魂之间的系绳」、
Joseph 主动躺上实验台（自己找了个坏疽的陌生人做试验，后来是自己）、
Arthur 看到「Joseph 尸体周围有一道光……胸骨下方有个锚点……一张脸的轮廓」、
Arthur 杀死 Rossi 埋在后院、
结尾降神会：「死后有生命吗？」「毫无疑问。」「那有没有苦难？」
并补齐原文的「（keep）」占位：真词汇表三档 + 真一句话总结。）
"""

VOCAB12 = [
    "### ⭐⭐⭐ 高级",
    "",
    "| 词/短语 | 释义 | 原文例句 |",
    "|---|---|---|",
    "| resurrection men | 掘尸人、盗尸者（为解剖学供给尸体的行当） | Here's what a pair of enterprising young resurrection men needed to rob graves in 1882: a shovel, a rope, and a bottle of whiskey. |",
    "| betrothals | 婚约 | He'd grown up surrounded by a community in mourning, parents without children, children without parents, betrothals broken by the grave. |",
    "| bullheaded | 固执的、一意孤行的 | Joseph wanted to go home, but Arthur was bullheaded, intent on getting paid. |",
    "| enraptured | 狂喜的、忘我的 | They got a single message that day—It was good of you to take the boy—and they were enraptured. |",
    "| repercussions | 报应、后果 | He didn't believe in devils or ghosts or eternal repercussions. |",
    "| practitioners | 从业者（此处指灵媒） | Kate Fox moved on to the next stop in her tour, but the Sullivans found more practitioners. |",
    "",
    "### ⭐⭐ 进阶",
    "",
    "| 词/短语 | 释义 | 原文例句 |",
    "|---|---|---|",
    "| scandalized | 骇然、为之震惊 | Joseph was scandalized, but he didn't storm off. |",
    "| pocketbooks | 钱袋 | Somebody in the family had deep pocketbooks. |",
    "| downgrading | 降格、回到更差的境况 | But the money was too good and the thought of downgrading back to the mill and their mold-infested room in the back was too rotten. |",
    "| simultaneously | 同时地 | He watched as Kate spoke one message aloud while simultaneously scrawling another on paper. |",
    "| accomplished | 完成、达成 | With a bit of practice, the whole operation could be accomplished in less than half an hour—a relief for an anxious lookout. |",
    "| predictable | 可预料的、不出所料 | The result was predictable. |",
    "",
    "### ⭐ 基础",
    "",
    "| 词/短语 | 释义 | 原文例句 |",
    "|---|---|---|",
    "| shovel | 铲子 | The shovel was for digging straight down at the head of the grave. |",
    "| rope | 绳子 | The rope was for hauling the corpse out, looped snug around the neck or under the armpits. |",
    "| whiskey | 威士忌 | The whiskey was for steadying his nerves. |",
    "| coffin | 棺材 | Hours of drudgery to find already-emptied coffins, or worse: putrid corpses too far gone for the anatomist's lab. |",
    "| anatomist | 解剖学家 | Hours of drudgery to find already-emptied coffins, or worse: putrid corpses too far gone for the anatomist's lab. |",
    "| séance | 降神会（灵媒与亡者沟通的集会） | He was eight years old when his grandparents dragged him to his first séance. |",
]

SPECS = {
    "ch12 a shovel a rope and a bottle of whiskey.md": {
        "nav": {
            "一句话概括": "1882 年费城的黑色历史故事。两个掘尸人 Arthur 与 Joseph 靠替医学院和科学家"
                          "偷运尸体过活；科学家 Filippo Rossi 在研究「身体与灵魂之间的系绳」，"
                          "Joseph 被这套说法迷住，主动躺上实验台，最终死在自己参与设计的手术里。"
                          "Arthur 目睹那道光之后杀了 Rossi 泄愤并埋尸，却在多年后坐到灵媒对面。"
                          "通灵者回答「死后有生命吗」时用了「毫无疑问」；"
                          "Arthur 选择了相信，然后问出第二个问题：有没有苦难？故事就停在这里。",
            "时间": "1882—1883 年（费城）；结尾的降神会已隔了多年。",
            "地点": "费城——棉纺厂与后巷、廉价酒馆、杰斐逊医学院、Rossi 的大宅与实验室、"
                    "乱葬岗、灵媒家那间整洁得不敢坐家具的客厅。",
            "人物": "Arthur Sullivan（叙述者，孤儿，掘尸人，不信神；二十三岁）；"
                    "Joseph（同伴，信神，怕来世，最终自愿成为实验体）；"
                    "Filippo Rossi（科学家，研究灵魂的系绳，把死亡做成可操作的实验）；"
                    "Charlie Davis（送货人，实际是威士忌掮客，把活计介绍给他们）；"
                    "灵媒（一女子，为 Arthur 通灵 Joseph）；"
                    "Arthur 的祖父母（招魂主义者，从小带他参加降神会；祖母 Mary 是 Mumler 幽灵照的经手人之一）。",
            "叙事手法": "第三人称限制视角贴着 Arthur，后半段插入降神会的框架；"
                        "以 1880 年代费城的掘尸业与招魂术为史料底色；"
                        "开篇与结尾用同一份清单（铲子、绳子、威士忌）首尾扣合，"
                        "把同一套工具从「挖别人的坟」翻成「埋自己杀的人」；"
                        "结尾停在第二个问题之前，不给答案。",
            "与后文的钩子": "Strahan 在导言里提到 Samantha Mills 写的是"
                          "「一群掘尸人和一位想把灵魂锚住的科学家」——本篇正是那一篇；"
                          "它的锋利处在于把「死亡是否受苦」这个问题留给了读者，"
                          "而不是替死者说话。",
        },
        "summary": "Samantha Mills 的「一铲、一绳、一瓶威士忌」是选集里最像历史小说的恐怖故事。"
                   "1882 年的费城，孤儿 Arthur Sullivan 和信神的 Joseph 做起掘尸人，"
                   "一晚二十五美元，从坟里挖尸体送到医学院与解剖实验室；"
                   "他们需要三样东西：挖的铲子、拖的绳、壮胆的威士忌。"
                   "科学家 Filippo Rossi 说自己在研究身体与灵魂之间的系绳，Joseph 听得入迷，"
                   "从替 Rossi 找试验材料，到把方法用在活人身上，最后把自己交了出去——"
                   "他死时，Arthur 看见尸体周围有一道光，集中在胸口的切口，"
                   "有卷须状的东西钩在胸骨下方，隐约带着一张脸的轮廓。"
                   "Arthur 杀了 Rossi 泄愤，把人埋进后院，"
                   "却在多年后坐到灵媒对面，问出他一辈子最想问的那句：死后有生命吗？"
                   "回答是「毫无疑问」。他选择了相信，然后问了第二个问题：有没有苦难？"
                   "故事在这里停下。",
        "vocab": VOCAB12,
        "blocks": {
            "1": {
                "zh": "「1882 年，一对有进取心的年轻掘尸人需要什么才能挖坟？"
                      "一把铲子、一根绳子、一瓶威士忌。」"
                      "这是全篇的清单式开场，也是后来会被原样用回来的那三件东西。",
                "why": "作者把盗尸写成创业项目："
                       "「有进取心」（enterprising）用得极妙，它在英语里既是褒义也是商业词，"
                       "落在两个掘尸人身上就成了反讽。"
                       "而三件工具被一一解释用途（铲子直挖墓头、绳子拖尸、威士忌壮胆），"
                       "把全篇写成了一份操作手册——"
                       "这套流程在结尾会被原封不动地再用一次，"
                       "只不过从「挖别人的坟」变成「埋自己杀的人」。",
                "tip": "掘尸人（resurrection men）是十九世纪为医学解剖学盗尸的行当；"
                       "结尾那份清单的年份是 1883，工具一件没变。",
            },
            "2": {
                "zh": "「不过是些东西罢了，」Arthur 一遍遍对他说。「人一走，什么也留不下。」"
                      "这是他的唯物论，也是他安慰 Joseph 的话：尸体是东西，不是人。",
                "why": "作者用一句反复的安慰写出一个人的世界观：死亡是彻底的抹除，什么都不剩。"
                       "而正是这套说法让 Arthur 干得了掘尸这行——"
                       "把尸体称作「东西」，就等于取消了死者的尊严。"
                       "全篇的道德张力就架在这句话上："
                       "Joseph 怕的是「来世」（那不是留下什么才可怕，是来世才可怕），"
                       "Arthur 什么都不信；"
                       "而作者最后让他亲眼看到那道光，让这套世界观在他身上失效。",
                "tip": "这是全篇的道德轴心：把死者称为「东西」，正是盗尸得以成立的前提。",
            },
            "3": {
                "zh": "「你什么也不信，」Joseph 指责他。「你从来就不信。」",
                "why": "作者让被指责的一方用「从来」二字把话说死——"
                       "Arthur 的不信不是一时的怀疑，是一整套身份。"
                       "这句指控同时也是 Joseph 的立场：在他看来，"
                       "不信等于精神上的空缺，等于迟早会被什么东西填上——"
                       "而他后来的确自愿躺上了 Rossi 的实验台。"
                       "两个朋友的分歧因此不是神学之争，"
                       "而是一句更朴素的话：一个人愿不愿意把命交出去。",
                "tip": "Rossi 自称「我是个科学家，我在研究身体与灵魂之间的系绳」——"
                       "这正是 Joseph 最想听见的说法。",
            },
            "4": {
                "zh": "「Joseph 死的时候，尸体周围有一道光。那光聚在胸口的切口上，"
                      "有卷须似的东西钩在那里，像是在拼命抓住什么——"
                      "胸骨下方的一个锚点，正如 Joseph 所说的那样；"
                      "那是一道货真价实、无可否认的光，隐约带着一张脸的轮廓。」",
                "why": "作者把「灵魂的证据」写成一个物理观察：聚光、卷须、锚点、脸的轮廓——"
                       "全是解剖学的词汇，却指向一样解剖学解释不了的东西。"
                       "「无可否认」（undeniable）是关键：Arthur 是个唯物论者，"
                       "而他偏偏在这件事上无法否认。"
                       "于是全篇的悲剧结构成形：他杀了唯一能证明灵魂存在、"
                       "也可能因此治好死亡的人；"
                       "「如果那是真的，也许全都是真的」——这句话把科学、灵魂与罪责连成一条线。",
                "tip": "Joseph 早已说过灵魂有一个「锚点」；"
                       "Rossi 研究的正是把灵魂锚住的技术——他不是受害者，他是自愿的。",
            },
            "5": {
                "zh": "「死后有生命吗？」「毫无疑问。」"
                      "灵媒这样回答；而 Arthur 选择了相信。",
                "why": "作者把全篇最重要的答案交给一个身份可疑的人："
                       "她可能真的在通灵，也可能只是 Arthur 需要的谎言。"
                       "而「毫无疑问」（undoubtedly）这个绝对语气，"
                       "正好对上 Arthur 一辈子的绝对怀疑——"
                       "两个人用同一种确定说话，方向相反。"
                       "作者随后点破：「他选择了相信」——"
                       "信仰在这里不是被说服的结果，而是悲伤里的一个决定。",
                "tip": "灵媒要他把手放在桌上、闭眼、想着你的朋友；"
                       "而她第一句叫出的是「Hello, Arthur」。",
            },
            "6": {
                "zh": "「他问：『有没有苦难？』」"
                      "Arthur 终于问出了第二个问题，故事就停在这里。",
                "why": "作者在最需要答案的地方收手。"
                       "第一个问题（有没有生命）已经得到肯定的回答，"
                       "第二个问题（有没有苦难）却没有；"
                       "而这个问题对 Arthur 恰恰是最要命的——"
                       "如果 Joseph 在那边受苦，那么他杀死的是一个正在受苦的人。"
                       "两个答案各有各的毒：没有苦难，可以赦免他；有苦难，他就永远欠着。"
                       "作者让读者自己站到问句这一边，故事因此没有结论，却比结论更重。",
                "tip": "灵媒的回答停顿过一次——"
                       "她先说「Hello, Arthur」，再让他在桌对面坐下；"
                       "而「毫无疑问」之后，她并不急着接第二个问题。",
            },
        },
    },
}
