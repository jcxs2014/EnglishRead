#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""五步审查 d 步整改：按缺陷清单做行级替换。
纪律：
- 每条 old 必须在该文件中恰好出现 1 次（replaceAll 项除外），否则中止（防误改）。
- 写盘用 tempfile + os.replace（记忆 #2042：io.open(p,"w") 失败会截成 0 字节）。
- 写后断言行数不变。
用法：python3 review-fix.py --dry   # 只打印将要改的行
      python3 review-fix.py         # 实际写入
"""
import os, sys, tempfile

B = "notes/books/mystery-thriller/this-is-the-night-they-come-for-you-by-robert-goddard"
DRY = "--dry" in sys.argv

# (文件, 旧串, 新串, 是否 replaceAll)
EDITS = [
("ch01 one.md", "而推动它的不是任何人的劝说，是他自己承认他好奇。",
                "而推动它的不是任何人的劝说——是他自己承认他还在找一个目的，一种意义。", False),
("ch01 one.md", "在楼梯的半层上承认他答应的理由不是责任、不是报复、也不是赎罪，而是好奇。",
                "在楼梯的半层上承认他要的不是赞誉、不是赎罪，也不是刺激，而是一个目的、一种意义。", False),
("ch01 one.md", "从局长的办公室望出去，景色不错，墙上却有一块白色的长方形——那是",
                "他陷在那张出了名难坐的沙发上，视线却正好落在局长办公桌后面的墙上：那里有一块白色的长方形——那是", False),
("ch02 two.md", "Harriet 在一九八八年的巴黎失踪", "Harriet 一九六五年六月在巴黎的失踪", False),
("ch04 four.md", "一九六四年他在伦敦 Foyle 书店遇见 Harriet Gray，两年后跟她去巴黎",
                 "一九六四年十一月他在伦敦 Foyle 书店遇见 Harriet Gray，几个月后跟她去巴黎", False),
("ch04 four.md", "他穿着花哨的条纹西装、戴着软呢帽在片场扮一个法国人——纠正刻板印象的人此刻正在扮演刻板印象。",
                 "他穿着花哨的条纹西装、戴着软呢帽站在片场当临时演员——纠正刻板印象的人此刻正穿着一身刻板印象。", False),
("ch06 six.md", "Nigel Dalby 这个名字第一次被说出——他写了自述",
                "Nigel Dalby 这个名字在本章被点名——他写了自述", False),
("ch07 seven.md", "Nazim 这个名字第一次出现，Zarbi 把他与自己并称",
                  "Nazim 这个名字在这里被 Zarbi 与他并称时说出口", False),
("ch09 nine.md", "读者到那里才明白她看的不只是一段旧胶片。（`twenty-three-year-old`）",
                 "读者到那里才明白她看的不只是一段旧胶片（上一句的 `twenty-three-year-old`）。", False),
("ch12 twelve.md", "读到这里应当回头看一眼上一章那个院子：作者已经把她家里多住了一个人这件事写进过场景，只是当时没人注意。",
                   "读到这里应当回头看一眼上一章那座院子：Abderrahmane 家当时看上去只是又一个老太太的日常，而本章结尾那句「没想到她还收留了一个房客」说明它一直是这条线上的一环。", False),
("ch13 thirteen.md", "这一句也解释了全书标题的另一半含义（他，是一对夫妻深夜来找的人）：活下来的确有代价。",
                     "这一句写的是活下来的代价：他逃过了追捕，却没逃过自己参与过的那件事——代价不是被找到，而是从此知道它会找到他。", False),
("ch13 thirteen.md", "政权并不是与他们外在的东西", "政权并不在他们身外", True),
("ch14 fourteen.md", "① Dalby 死于 1993 年「疑似伊斯兰主义袭击」",
                     "① Dalby 在 1993 年那次谈话后不久死于一场「疑似伊斯兰主义袭击」（实为 1994 年 2 月）", False),
("ch14 fourteen.md", "第一次带进 2021 年的时间线", "第一次带进 2020 年的时间线", False),
("ch16 sixteen.md", "章末，Wendy 用倒车的一撞让箱子「自己」打开",
                    "章末，Wendy 挂前进挡撞过去，让那些箱子「自己」塌开", False),
("ch16 sixteen.md", "他是在本书 2021 年的时间线里唯一同时认识", "他是在本书 2020 年的时间线里唯一同时认识", False),
("ch16 sixteen.md", "那是一台老式的 Olivetti 手提打字机。", "那是一台老式的 Olivetti 手动打字机。", False),
("ch16 sixteen.md", "`old manual Olivetti typewriter`（老式的 Olivetti 手提打字机）",
                    "`old manual Olivetti typewriter`（老式的 Olivetti 手动打字机）", False),
("ch17 seventeen.md", "Wendy 决定不再替哥哥兜底", "Wendy 决定不再替弟弟兜底", False),
("ch17 seventeen.md", "这一次，Wendy 要对自己的哥哥把规矩立下来。", "这一次，Wendy 要对自己的弟弟把规矩立下来。", False),
("ch17 seventeen.md", "`to her brother`（对自己的哥哥）", "`to her brother`（对自己的弟弟）", False),
("ch18 eighteen.md", "Zarbi 现在大概在馬赛", "Zarbi 现在大概在马赛", False),
("ch18 eighteen.md", "把它与 Q1 的处世哲学连起来读", "把它与前面原句 1 的处世哲学连起来读", False),
("ch19 nineteen.md", "他靠 Boukhatem 打通关系，租下那间公寓的旧住户，最终在厨房橱柜底板的夹层里找到自述的原稿与复写件",
                     "他花了很长时间、付给那间公寓里那位孤僻的住户一大笔钱，才换得进屋搜查，最终在厨房橱柜底板的夹层里找到自述的原稿与复写件", False),
("ch19 nineteen.md", "这一章是妹妹审哥哥", "这一章是姐姐审弟弟", False),
("ch19 nineteen.md", "这段也补上了上一章 Suzette 的推断", "这段也补上了第 17 章 Suzette 的推断", False),
("ch19 nineteen.md", "记住这五个词：「量水的人称金子」。它与 ch15 里 Bahlouli 说出的「Laloul 就是那个量水人」是同一件事的两半",
                     "记住这句话：「量水的人称金子」。它与 Bahlouli 说出的「Laloul 就是那个量水人」（第 14 章；第 16 章由 Taleb 复述）是同一件事的两半", False),
("ch19 nineteen.md", "Wendy 用一组对仗结束与哥哥的辩论", "Wendy 用一组对仗结束与弟弟的辩论", False),
("ch19 nineteen.md", "妹妹用了二十句话把哥哥的三十年问成了一个洞", "姐姐用了二十句话把弟弟的三十年问成了一个洞", False),
("ch20 twenty.md", "Gray——失去证物、住处与妹妹的信任", "Gray——失去证物、住处与姐姐的信任", False),
("ch20 twenty.md", "与 Q1 那句「不引起争议才是最重要的」合读", "与前面原句 1 那句「不引起争议才是最重要的」合读", False),
("ch21 twenty one.md", "而她的手机早在 Gray 的怀疑名单上", "而 Gray 此前警告过她，手机可能已被 Laloul 窃听", False),
("ch23 twenty three.md", "德高乐", "戴高乐", True),
("ch25 twenty five.md", "`It was ten million euros`（原先是八位数的一半——一千万欧元）",
                        "`It was ten million euros`（原先是一千万欧元）", False),
("ch25 twenty five.md", "Kermadec 的回应不是解释而是威胁式的命令（下一段「你们俩都给我闭嘴」）——力量对比在这两个回合中已经交代清楚。",
                        "Kermadec 对这句反驳不加解释，只给了一道让他闭嘴的眼色（`a silencing glare`），随后把话接过去——力量对比在这两个回合中已经交代清楚。", False),
("ch29 twenty nine.md", "两人最后一次见面在十余年前（见前章回忆）",
                        "两人最后一次见面在二十多年前（1993 年那次问话）", False),
("ch30 thirty.md", "第 27 章的「不交原件」", "第 26 章的「不交原件」", False),
("ch30 thirty.md", "与他在第 20 章第一次出现时的客气是同一套语言", "与他在第 22 章第一次出现时的客气是同一套语言", False),
("ch30 thirty.md", "最后一句「这是你的选择」（`It’s your choice.`）与第 26 章 Ménard 说过的同一句对调——本书的权力关系在此彻底反转。",
                    "最后一句「这是你的选择」（`It’s your choice.`）把 Ménard 惯用的语言还给了她——本书的权力关系在此彻底反转。", False),
("ch31 epilogue.md", "「水计量官」这个从第 5 章起就悬着的职位", "「水计量官」这个从第 14 章起就悬着的职位", False),
]

def apply_file(path, edits):
    lines = open(path, encoding="utf-8").read().splitlines(True)
    orig_n = len(lines)
    assert orig_n > 50, "疑似已被截断，中止: " + path
    plan = []
    for old, new, allf in edits:
        hit = 0
        for i, l in enumerate(lines):
            if old in l:
                hit += l.count(old)
                plan.append((i + 1, old[:40], new[:40]))
        if hit == 0:
            sys.exit("!! 未匹配: %s | %s" % (os.path.basename(path), old[:50]))
        if hit > 1 and not allf:
            sys.exit("!! 匹配 %d 次（非 replaceAll）: %s | %s" % (hit, os.path.basename(path), old[:50]))
    if DRY:
        print(":: %s（%d 条）" % (os.path.basename(path), len(plan)))
        for n, a, b in plan:
            print("   行%d: %s ⇒ %s" % (n, a, b))
        return
    for old, new, allf in edits:
        lines = [l.replace(old, new) if allf else (l.replace(old, new, 1) if old in l else l) for l in lines]
    out = "".join(lines)
    assert out.count("\n") == orig_n, "行数变了: " + path
    d = os.path.dirname(os.path.abspath(path))
    fd, tmp = tempfile.mkstemp(dir=d)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(out)
    os.replace(tmp, path)
    print("✅ %s：%d 处已改（行数 %d 不变）" % (os.path.basename(path), len(plan), orig_n))

by_file = {}
for fn, old, new, allf in EDITS:
    by_file.setdefault(fn, []).append((old, new, allf))
for fn, eds in by_file.items():
    apply_file(os.path.join(B, fn), eds)
print("--- %s ---" % ("DRY-RUN（未写盘）" if DRY else "已写入"))
