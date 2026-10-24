# -*- coding: utf-8 -*-
import json, os, sys

BOOK = "/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/in-your-heart-a-devil-by-vanessa-santos"
OUT = "/Users/jcxs2014/Documents/Works/EnglishRead/.memory/raw-gates/in-your-heart-a-devil-by-vanessa-santos/review"

SPEC = {
    "ch19": ("text/ch19_xvii.txt", [
        ("Alexander died two years after the car crash. It was autumn",
         "亚历山大在车祸两年后的秋天病逝，此前已卧床近两周，医生查不出病因。"),
        ("I tucked pillows under his head, held cups of water to his lips",
         "伊莎贝尔在病榻前照料亚历山大：给他垫枕头、端水到唇边、后来喂稀薄的肉汤。"),
        ("‘It was not true,’ he said, before I could ask anything.",
         "亚历山大主动承认那晚的“假装相爱”不是真的，并说自己当时受伤所以反过来伤了伊莎贝尔、向她道歉。"),
        ("‘It was supposed to be me, was it not?’ I asked at last.",
         "伊莎贝尔当面推断出咒语要的“至亲牺牲”本应是她自己，并质问亚历山大是否因此娶她。"),
        ("‘I could not do it,’ he resumed, after a moment.",
         "亚历山大承认婚礼之夜下不了手，因为看见她眼里的期待与爱意，于是放过了她。"),
        ("‘He did not need a sacrifice,’ I told him.",
         "伊莎贝尔在亚历山大临终前对他说谎：尼克根本不需要献祭、随时都能来，以此作为最后的报复。"),
        ("and a crow – Alexander’s, I would swear upon it – swooped down",
         "葬礼上，一只乌鸦（伊莎贝尔确信是亚历山大的）俯冲到新坟的泥土上，低头如祈祷般久留。"),
        ("I sent flowers to Mr Stewart’s grave anyway, just in case.",
         "伊莎贝尔没能参加斯图尔特先生的葬礼，事后仍往他墓前送了花。"),
    ], "伊莎贝尔（叙述者）与临终的丈夫亚历山大；二人与恶魔尼克构成三角；斯图尔特先生（可能是非人存在的化身）在葬礼上向她转述民间传说。",
       ["two years after the car crash", "close to a fortnight", "long hours"]),

    "ch20": ("text/ch20_xviii.txt", [
        ("‘Hell is not what you think it is,’ he said.",
         "尼克向伊莎贝尔宣称地狱并非她想象的样子，并拒绝透露死后世界的秘密。"),
        ("There is nothing but the present there, no past, no future.",
         "尼克描述地狱里只有当下、没有过去与未来，把“活在当下”说成是一个不该跌入的洞。"),
        ("What if I am not me but a Catholic schoolboy, abed with a fever",
         "尼克自述怀疑自身是否真实，设想自己也许只是一个发烧卧床的天主教男学生脑中展开的地狱。"),
        ("‘It was a neat little trick you pulled there at the end,’ he told me.",
         "尼克点破伊莎贝尔临终那句谎话是“漂亮的小把戏”，语气悲伤却认命，甚至有点骄傲。"),
        ("‘You are more like me than you know,’ he said",
         "尼克对伊莎贝尔说她比自己以为的更像我，并从中感到某种诗意的公正。"),
        ("A pulse, he called it.",
         "伊莎贝尔回忆亚历山大生前唯一一次谈到尼克，把他的存在称作“脉搏”。"),
        ("There is a way, I know, of merging with the house.",
         "伊莎贝尔记起亚历山大书里一个咒语的模糊形状，决意用它与宅子合为一体。"),
        ("I am sure he will be willing to make one more deal.",
         "伊莎贝尔等待尼克再次来访，确信他愿意再做一笔交易。"),
    ], "伊莎贝尔（叙述者，已近暮年）与定期来访的恶魔尼克；亚历山大已死，仅存于回忆与梦中；宅子 S— House 本身是被她视为归宿的对象。",
       ["the fifth floor", "countless hours", "Centuries of history"]),

    "ch21": ("text/ch21_author_s_note.txt", [
        ("In sixteenth-century Aberdeenshire there lived a man called Alexander Skene.",
         "作者交代原型：十六世纪阿伯丁郡确有亚历山大·斯凯恩其人，是领主、住斯凯恩宅，民间称“斯凯恩的巫师领主”。"),
        ("Alexander escaped by cutting off his shadow with a dagger.",
         "作者转述传说第一件事：亚历山大在魔鬼的黑术学校用匕首割断自己的影子，逃脱落跑时被踩影子的留人手段。"),
        ("Alexander won, his magpie tearing the Devil’s raven apart.",
         "作者转述传说最后一件事：亚历山大赢下双方魔宠的搏斗，他的喜鹊撕碎了魔鬼的渡鸦，灵魂获释并可依基督教下葬。"),
        ("When I first came across Alexander’s story in Aberdeenshire Folk Tales",
         "作者说明自己是在《阿伯丁郡民间故事》里初遇亚历山大故事，并被其中大量冒险细节打动。"),
        ("forcing them to play and dance until their hands and feet bled",
         "作者列举自己采纳的轶事之一：亚历山大诅咒 ceilidh 上的乐手与舞者，逼他们演奏跳舞到手脚流血。"),
        ("When I first saw it, I had the same feeling of wrongness.",
         "作者亲访斯凯恩宅，第一次就感到同样的“不对劲”，此后反复造访、那种感觉才消散。"),
        ("whose name was Giles Ædie",
         "作者指出亚历山大真实的妻子名叫 Giles Ædie，史料所存极少，并感叹历史善于抹去女性。"),
        ("I did not want Skene named in the story itself",
         "作者说明为了故事本身与原传说两边都顾及，她刻意不在小说里点出斯凯恩这个地名。"),
    ], "作者凡妮莎·桑托斯本人为主语：她考据传说、实地探访斯凯恩宅、并在后记里向读者交代取材与取舍；对象是历史人物亚历山大·斯凯恩、其妻 Giles Ædie 与真实地点斯凯恩宅。",
       ["sixteenth-century", "not once, but twice", "one hundred times", "two tales"]),
}

def build(ch, rel):
    relpath, items, relations, numbers = rel
    text = open(os.path.join(BOOK, relpath), encoding="utf-8").read()
    facts = []
    for anchor, fact in items:
        assert 10 <= len(anchor) <= 80, (ch, len(anchor), anchor)
        start = text.find(anchor)
        assert start != -1, (ch, "NOT FOUND", anchor)
        cnt = text.count(anchor)
        if cnt != 1:
            print(f"WARN {ch} appears {cnt}x: {anchor}")
        facts.append({"anchor": anchor, "start": start,
                      "end": start + len(anchor), "fact": fact})
    data = {"chapter": ch, "facts": facts,
            "relations": relations, "numbers": numbers}
    d = os.path.join(OUT, ch)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "1-suread.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(ch, len(facts), "->", p)

for ch, rel in SPEC.items():
    build(ch, rel)
