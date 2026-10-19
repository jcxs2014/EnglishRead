# -*- coding: utf-8 -*-
"""词汇表修复补丁：A 类虚构词头整行替换（词头+释义+例句）。

每条例句都是从该章 text/ 里切出的**单行内连续逐字片段**（已逐条 grep 取证）。
旧词头本章查无 ⇒ 换成本章真实存在的词。
"""

REPLACE = {
    "ch01 introduction.md": {
        "inevitably": ("skulls", "骷髅、颅骨",
                       "calaveras—Day of the Dead skulls. It showed sixteen highly decorated skulls, each"),
    },
    "ch08 the dead end party.md": {
        "existential": ("phantom", "幻影车（循环里重复行驶的空车）",
                        "lanes, passing all the phantom cars with no people inside. Come by"),
        "theodicy": ("potluck", "百乐餐（各人自带食物的聚会）",
                     "the last minute, a potluck of debauchery. So far I hadn’t witnessed"),
    },
    "ch10 life goes on.md": {
        "immutable": ("cantankerous", "脾气坏的、爱与人争的",
                      "point out, was a cantankerous sort of man, even by Dale standards."),
    },
    "ch14 becoming fossils.md": {
        "panicking": ("mulberry", "桑葚",
                      "an oasis of fruiting mulberry trees that—by all accounts—shouldn’t exist."),
    },
    "ch15 seven bells.md": {
        "psychopomp": ("transoceanic", "跨大西洋的",
                       "the fastest and biggest transoceanic liner ever built. Despite leading a crew"),
    },
    "ch16 the sentence.md": {
        "superposition": ("conjuring", "召唤、施法（也含「变戏法」之意）",
                          "room, but it really wasn’t about conjuring the room itself, it was more about the"),
        "parlor tricks": ("halving", "对半切分（魔术里的分割手法）",
                          "sort of like the idea of halving a second, then halving a half second, and"),
    },
    "ch17 perpetual god machines of the ancestral kind.md": {
        "reincarnation": ("divination", "占卜、卜筮",
                          "spent on client-facing practical divination, lest our skills ossify, and we lose"),
    },
    "ch19 now watch me as you hold your breath.md": {
        "complicity": ("corset", "束腰（紧身胸衣）",
                       "attached to Anna Sui-style corsets, lacy and violent. They were held upright"),
        "predator": ("Lolita", "洛丽塔（阿努托夫斯基笔下的少女符号）",
                     "wallpaper was a blue-haired Lolita. I was small and cute enough, I"),
    },
    "ch20 the invocation of the ghost the exorcism of the muse.md": {
        "possession": ("crematory", "焚化用的（火葬所用）",
                       "rice paper and a crematory ash inkstick are infinitely more portable"),
    },
    "ch22 varanasi.md": {
        "mortician": ("undertaker", "承办丧葬的人",
                      "Our family have been undertakers for generations. Seventy years of Kirkland and"),
    },
    "ch23 the leaving season.md": {
        "gout": ("kelpies", "凯尔派（神话里好叫的恶犬）",
                 "remain untended. Outside the kelpies have mostly given up barking their upset"),
        "charlatan": ("digestion", "消化",
                      "Just his digestion was a bit tricky, so a few sandwiches sat better in his stomach."),
    },
    "ch24 the grand opening.md": {
        "crematory": ("foundations", "地基",
                      "clowns who pour the foundations. Well, really, it’s the clay that goes"),
        "superintendent": ("ramrod", "验收员（专管质量检查的人）",
                           "as none of the ramrods are looking over your shoulder, doing their"),
        "insidious": ("supervisor", "监工",
                      "and on. If the supervisor doesn’t see it, though? If the incoming"),
    },
    "ch25 this is what happens when you die.md": {
        "fractal": ("lunarium", "月室（死后世界里那间核心房间）",
                    "things because of the lunarium. That is where I learned about the"),
        "verisimilitude": ("contraction", "收缩",
                           "It is the limit that triggers contraction and expansion."),
    },
    "ch26 the well of the martian queens.md": {
        "sarcophagus": ("embalming", "防腐处理（遗体防腐）",
                        "abdomen. The quality of embalming, and hence the current state of preservation,"),
    },
    "ch28 down the interstate.md": {
        "purgatory": ("interchange", "互通立交",
                      "onto a long concrete interchange that hadn’t been signposted anywhere. Without his"),
        "redemption": ("toll", "通行费",
                       "“What’s the toll?”"),
        "oblivious": ("fog", "浓雾",
                      "Brown watched the thick fog that lidded the interstate gather in a"),
    },
}
