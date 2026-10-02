#!/usr/bin/env python3
"""把每章 spec 的「书内章号」字段改成**实测的**切点来源。

为什么要机械化
--------------
本书没有章节标记，「书内章号」只能说明切点是怎么来的。若人手写，
ch01（起点是全书正文起点）会被误写成「出版方装饰花饰切出」——
本库已多次出现「工具猜的号既不是书内号也不是阅读序」（Parable 先例）。

判据来自 extract_chapterless.slice_body 的分级返回值，不是重新推导一遍。
"""
import glob
import json
import sys

sys.path.insert(0, "scripts/attic")
from extract_chapterless import pick_body, read_epub, slice_body  # noqa: E402

LBL = {
    "start": "全书正文起点",
    "ORN": "出版方装饰花饰分隔符（章界信号）",
    "DASH": "出版方破折号分隔符（场景界信号）；此处为该场景段超过 25,000 字符后的补切",
}
BOOK = "notes/books/novels/astarion-by-t-kingfisher"


def main():
    z, base, spine = read_epub(glob.glob(f"{BOOK}/library/*.epub")[0])
    _href, raw = pick_body(z, base, spine)
    segs = slice_body(raw, 25000)
    for i, (_a, _b, kind) in enumerate(segs, 1):
        p = ("scripts/attic/astarion_ch01.json" if i == 1
             else "scripts/attic/spec/astarion/ch%02d.json" % i)
        try:
            d = json.load(open(p, encoding="utf-8"))
        except FileNotFoundError:
            continue
        txt = ("无。本书 epub 正文无任何章节标记（spine 13 件中正文仅 1 件，"
               "h1/h2/h3 计 0 个，全文「Chapter」出现 0 次，NCX 目录只把整本正文"
               "列为一条）。本节由 scripts/attic/extract_chapterless.py 按出版方"
               "自有的两级分隔符切出：起点是%s；全书 29 段 = 正文起点 1 + 装饰花饰"
               "（章界）20 + 破折号补切 8。" % LBL[kind])
        for row in d["nav"]:
            if row[0] == "书内章号":
                row[1] = txt
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("ch%02d %s" % (i, kind))


if __name__ == "__main__":
    main()
