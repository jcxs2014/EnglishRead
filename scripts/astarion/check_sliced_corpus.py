#!/usr/bin/env python3
"""自造切点的对账（Astarion 类无章节标记 epub 专用）。

为什么不用 verify_corpus 的 --anchors
------------------------------------
本书是**单 POV 小说**，29 个文件里 Astarion 出现 29/29，人物锚点的
「本篇人物 >0 / 他篇人物 =0」双向判据对它天然失效（AGENTS 原文：
单 POV 长篇可省 --anchors）。

真正的风险是**切点是我自己造的**，不是出版方的：
  ① 丢字（某段没落进任何文件）
  ② 重复（某段落进两个文件）
  ③ 切在段落中间（首句/末句残缺）
  ④ 切点位置整体漂移（文件名与内容对不上）

本脚本逐项对账，判据全部是**闭合计数**（相等才算过），任一不等即 FAIL。
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_chapterless import (  # noqa: E402
    body_start, clean, pick_body, read_epub, slice_body,
)

MAX_CHARS = 25000


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    book = sys.argv[1] if len(sys.argv) > 1 else "."
    os.chdir(book)

    z, base, spine = read_epub(glob.glob("library/*.epub")[0])
    href, raw = pick_body(z, base, spine)
    segs = slice_body(raw, MAX_CHARS)
    files = sorted(glob.glob("text/ch*.txt"))

    fails = []
    print("=== 自造切点对账: %s ===" % os.path.basename(os.getcwd()))
    print("正文件 %s | 切出 %d 段 | text/ %d 件" % (href, len(segs), len(files)))

    # ① 件数闭合
    if len(segs) != len(files):
        fails.append("件数 切点 %d != text/ %d" % (len(segs), len(files)))
        print("  [1] 件数 切点 %d != text/ %d  FAIL" % (len(segs), len(files)))
    else:
        print("  [1] 件数 %d == %d  OK" % (len(segs), len(files)))

    # ② 逐章逐字（丢字 / 重复 / 切点漂移一次抓全）
    diff = 0
    for i, (a, b, kind) in enumerate(segs, 1):
        src = clean(raw[a:b])
        got = open(files[i - 1], encoding="utf-8").read().strip()
        if src != got:
            diff += 1
            fails.append("ch%02d 逐字不一致（切点 %s）" % (i, kind))
            print("  [2] ch%02d 逐字不一致  FAIL  切点=%s" % (i, kind))
    if not diff:
        print("  [2] 逐章逐字 %d/%d 完全一致  OK" % (len(segs), len(segs)))

    # ③ 全量对账：拼接 == 整本（字符数相等 + 文本相等，两条都过才算）
    joined = norm(" ".join(open(f, encoding="utf-8").read() for f in files))
    whole = norm(clean(raw[body_start(raw):]))
    print("  [3] 拼接 %d 字符 / 整本 %d 字符" % (len(joined), len(whole)))
    if len(joined) == len(whole):
        print("  [3] 字符数相等  OK")
    else:
        fails.append("字符数 拼接 %d != 整本 %d" % (len(joined), len(whole)))
        print("  [3] 字符数不等  FAIL")
    if joined == whole:
        print("  [3] 文本完全相等  OK（无丢字、无重复、无插入）")
    else:
        fails.append("文本不等")
        print("  [3] 文本不等  FAIL")
        for k in range(min(len(joined), len(whole))):
            if joined[k] != whole[k]:
                print("      首个差异 @%d" % k)
                print("      拼接: %r" % joined[max(0, k - 60):k + 60])
                print("      整本: %r" % whole[max(0, k - 60):k + 60])
                break

    # ④ 边界完整性：首句不得以小写/连写开头，末句须有句末标点
    bad_head = bad_tail = 0
    for f in files:
        t = open(f, encoding="utf-8").read().strip()
        first = norm(t)[:80]
        if first and not first[0].isupper() and first[0] not in "“\"":
            bad_head += 1
            print("  [4] %s 首字符非大写: %r" % (os.path.basename(f), first[:50]))
        if not t.endswith((".", "!", "?", "”", "’")):
            bad_tail += 1
            print("  [4] %s 末字符非句末标点: %r" % (os.path.basename(f), t[-50:]))
    if not (bad_head or bad_tail):
        print("  [4] 首句大写 / 末句句末标点：%d/%d OK" % (len(files), len(files)))
    else:
        fails.append("边界异常 %d 处" % (bad_head + bad_tail))

    print()
    for f in fails:
        print("FAIL  %s" % f)
    print("\n=== 切点对账: %s（FAIL %d）===" %
          ("PASS" if not fails else "FAIL", len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())