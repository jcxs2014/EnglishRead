#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re, sys

BASE = "/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/the-splintered-sun-by-tad-williams"
TEXT = os.path.join(BASE, "text")
OUT = os.path.join(BASE, "review")

CHAPTERS = {
    "ch13": "ch13_13_the_scryer.txt",
    "ch14": "ch14_14_among_the_crows.txt",
    "ch15": "ch15_15_up_and_down_to_crannhyr.txt",
}

DATA = {
"ch13": [
 ("维斯皮利斯（Vespillis）占卜师被卫兵引进贝丽森特夫人的起居室，卫兵因怕他的名声而急忙退出。",
  "The scryer was ushered into Lady Bellicent’s retiring room by a guard who knew enough", "event"),
 ("贝丽森特要回阿班吉特（Abaingeat）她儿子家；她妹妹的儿子就是第一领主费兰（Phelan），正有一项决定要做。",
  "My sister’s son, First Lord Phelan, has a decision to make.", "relation"),
 ("贝丽森特认定那个深肤色女孩与诺克贝格（Knockbeg）本宅失窃的重要物品有关，她带的小男孩被搜过身却一无所获。",
  "I strongly suspect the dark-skinned girl had something to do with the theft", "event"),
 ("女孩名叫薇德拉（Vedra），是南方岛屿一类的名字；贝丽森特要维斯皮利斯把她和同行的男孩找出来。",
  "The girl is named Vedra—some kind of name from the southern islands.", "relation"),
 ("维斯皮利斯的仙女镜价值远超同等重量的黄金，他花了半辈子破解它的秘密，世间同类所剩无几。",
  "It is worth greatly more than its weight in gold. I have spent half a lifetime", "number"),
 ("维斯皮利斯进入恍惚状态，身子在凳上摇晃、呼吸粗重，镜子从指间掉到地毯上；他说自己差点在“梦路”上迷失。",
  "Vespillis swayed on his stool, his breathing now loud and harsh.", "event"),
 ("他占见海中立着一块形状怪异的石头，底部被浪花染白，名为“妖精岩”（Goblin Rock），位于港口城镇克兰希尔（Crannhyr）口。",
  "It is called Goblin Rock, and it stands at the mouth of the port town of Crannhyr.", "event"),
 ("贝丽森特决定让第一领主派人去迪拉西（Dillathi）另一侧的克兰希尔追捕两个孩子，并吩咐占卜师去找费兰的管家领赏。",
  "I must tell the First Lord to send his men to Crannhyr after them.", "event"),
],
"ch14": [
 ("薇德拉发现弗拉恩（Flann）的“乌鸦帮”并不散乱：高橡营像一座村子，弗拉恩更像村长或里正，常听战略家泰农（Tynon）与梅尔娜（Mearna）的意见。",
  "Flann ruled it less like a bandit-king and more like a mayor or reeve", "event"),
 ("弗拉恩的三名首席斥候是当过水手的三兄弟：科纳尔（Conal）最年长、最严肃，瑟巴尔（Cerball）最年轻、最多话，卡登（Caden）居中。",
  "Conal was the oldest, precisely as serious, unsmiling, and cautious as she had suspected", "relation"),
 ("每年冬季乌鸦帮迁往西尔科尔（Circoille）森林边缘的深穴营，人数缩到约“两 score”（some two-score）常驻成员，需向当地人换取部分必需品。",
  "the band shrank to some two-score permanent members", "number"),
 ("竖琴手迪亚班（Diarban）像他父亲一样，曾为弗拉恩的父亲、奥尔德伍德的塔斯·罗南（Tace Ronann）做宫廷乐师。",
  "Diarban had been a court musician for Flann’s father, Tace Ronann of Alderwood", "relation"),
 ("泰斯泰恩（Tethtain）是卡舍尔里格（Cashelrigg）岛堡之主，自称末代国王图塔尔（Tuthal）家族后裔，率众在卡恩托巴（Carntobar）之战击败帝国总督、赶走纳巴奈人。",
  "Tethtain, lord of the island fortress of Cashelrigg, who claimed descent from the family line of Tuthal", "event"),
 ("泰斯泰恩把里默斯人逐出北赫尔尼斯提尔，这是自两个世纪前“诺克之战”（battle of the Knock）惨败于芬吉尔·红手（Fingil Red-Hand）以来的第一次。",
  "the disastrous battle of the Knock two centuries earlier", "number"),
 ("泰斯泰恩有合法继承人：他与纽伊斯伯爵之女克丽娅（Cria）所生的儿子埃温（Ewain）；克丽娅死于难产，婴儿被留在卡舍尔里格。",
  "his son Ewain by Cria, daughter of the Count of Newyth", "relation"),
 ("第一领主费兰没收了弗拉恩的土地，把最大部分给了亲信、克兰希尔的第一领主里正哈根（Hagan）；弗拉恩打了信使后带迪亚班、泰农等忠仆逃入西尔科尔森林。",
  "Phelan confiscated Flann’s lands and gave the largest part of them to one of his closest allies, Hagan", "event"),
],
"ch15": [
 ("在高橡营住了约一周（a sennight）后，迪亚班来叫薇德拉与梅尔娜夫人去见弗拉恩，只叫薇德拉、不带男孩。",
  "One day, after she and Daley had spent about a sennight in High Oak Camp", "number"),
 ("弗拉恩介绍泰农是他的“战争头领”，此行期间留守高橡营；秃顶大胡子伊瓦尔（Ivar）是帮里的厨子，被称作“我们的小团体的母亲”。",
  "My war chieftain, as it were. He will be in charge of High Oak Camp while we go to Crannhyr.", "relation"),
 ("弗拉恩定下次日黎明出发去克兰希尔，查明男孩从诺克贝格偷来的信究竟是什么；出行者为他、薇德拉、戴利、梅尔娜、迪亚班、伊瓦尔，全程步行，出营后不得提他的名字，因为哈根的耳目遍地。",
  "once out of camp, my name is not to be mentioned. Hagan will have his spies everywhere.", "event"),
 ("梅尔娜告诉薇德拉：弗拉恩不喜与女人同床，偏爱高大健壮的男人；伊瓦尔与他“除了一件事以外”就像老夫老妻，且弗拉恩喜新厌旧，伊瓦尔因此痛苦。",
  "In all ways but one, they are an old married couple.", "relation"),
 ("下山途中薇德拉的脚卡在横在路中的巨石与土壁之间；弗拉恩把脚蹬石、背抵土壁，发力把石头推开一线，让她抽出脚，脚踝被刮破。",
  "He put his feet against the stone and his back against the earthen wall of the track.", "event"),
 ("薇德拉脱困后望见下方克兰希尔只有“两三点灯火”（two or three lights），心里一沉，担心这地方太小难以藏身过夜。",
  "Two or three lights, anyway, and her heart sank to think of a place so small", "number"),
 ("克兰希尔沿一条主路盘绕而下，房屋高踞两侧、上层阳台几乎可隔街相握；弗拉恩带众人绕过“码头街”（Dock Row）的污秽场所，经过海神里尔（Lirr）的咸渍木庙。",
  "Across from a salt-crusted wooden temple dedicated to the sea god Lirr", "event"),
 ("众人登上山顶宅邸，无人守卫却门自开；白发黑衫的领主扎尼科（Xaniko）在火堆旁现身，说此地被他命名为“卡恩·戈巴赫”（Carn Gobach，即“破衣厅”），弗拉恩单膝下跪求助。",
  "you are welcome to Carn Gobach, as I have named it—Threadbare Hall", "event"),
],
}

report = {}
ok = True
for ch, fname in CHAPTERS.items():
    path = os.path.join(TEXT, fname)
    text = open(path, encoding="utf-8").read()
    items = []
    for fact, anchor, typ in DATA[ch]:
        c = text.count(anchor)
        start = text.find(anchor)
        end = start + len(anchor)
        wc = len(anchor.split())
        if c != 1 or start < 0 or text[start:end] != anchor or not (8 <= wc <= 20):
            ok = False
            print("FAIL", ch, c, wc, repr(anchor))
            continue
        items.append({"fact": fact, "anchor": anchor, "start": start, "end": end, "type": typ})
    report[ch] = items
    d = os.path.join(OUT, ch)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "1-suread.json"), "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    types = {}
    for it in items:
        types[it["type"]] = types.get(it["type"], 0) + 1
    print(ch, "n=", len(items), "types=", types,
          "wc=", (min(len(i["anchor"].split()) for i in items), max(len(i["anchor"].split()) for i in items)))
print("ALL_OK" if ok else "HAS_FAIL")
