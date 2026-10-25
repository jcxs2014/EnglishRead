#!/usr/bin/env python3
"""⑦ 复述层断言候选扫描（T1 六类预筛的补充）

为什么需要：引语层由 19 lane 覆盖，而「概述 / 导航 / 人物弧线 / 一句话总结」里的中文转述
没有引语可锚 ⇒ 任何引语门禁都看不见。life-out-of-order 实证：T3 修完 45 条后，
T1 复核 15 章仍查出 5 条阻断，全部在这一层（唯一/数量、说话人、主客方向）。

本工具只**取候选**，恒 exit 0，不判红（同 assertion_scan）。
三类：
  R1 全称/量词断言：唯一、仅、全部、从未、第一次、最后一个…
  R2 说话归属：他说/她问/告诉/喊道 + 引号（同一句出现两个以上人名时更要看）
  R3 指代范围：所有人、全书、每一章、从头到尾（易与「本章」混淆）

用法：
  python3 scripts/restate_scan.py <书目录> [--class R1|R2|R3] [--summary] [--limit N]
"""
import re, sys, pathlib

CLASSES = {
    "R1": ("全书级唯一断言", re.compile(
        r"唯一的|唯一|唯一一处|只此一次|仅此一次|全书只有|全文只有|全书都没|全文都没|"
        r"从未出现过|从没出现过|一次也没|一章都没|再也没有出现过")),
    "R2": ("说话归属", re.compile(
        r"(?:他|她|克莱尔|贝克|奥利弗|阿尔芭|伊莎多拉|扎克)[^，。；]{0,8}"
        r"(?:说|问|告诉|喊|答|道|打断|补充|低声|低声说)[^。；]{0,10}[「“]")),
    "R3": ("指代范围", re.compile(
        r"所有人|全家人|每个人都|从头到尾|每一章|全书都|整本书|贯穿全书")),
}
SENT = re.compile(r"[^。；！？]+[。；！？]?")
NAMES = ("克莱尔","贝克","奥利弗","阿尔芭","伊莎多拉","扎克","露辛达","妈妈","母亲","父亲","哥哥","妹妹")
FIELD = re.compile(r"^(?:>\s*)*(?:[-*+]\s+)?\*\*([^*]{1,20})\*\*\s*[：:]\s*(.*)$")


def field_lines(path):
    """只取「字段行」（- **一句话概括**：… / > **中文理解**：…），跳过引语行与原句行。"""
    for i, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        if "**原句" in line:
            continue
        m = FIELD.match(line.strip())
        if m:
            yield i, m.group(1), m.group(2)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 0
    book = pathlib.Path(argv[1])
    want = None
    summary = "--summary" in argv
    limit = None
    if "--class" in argv:
        want = argv[argv.index("--class") + 1]
    if "--limit" in argv:
        limit = int(argv[argv.index("--limit") + 1])

    files = sorted(list(book.glob("00_*.md")) + list(book.glob("ch*.md")))
    hits = {k: [] for k in CLASSES}
    for f in files:
        for ln, label, body in field_lines(f):
            for sent in SENT.findall(body):
                s = sent.strip()
                if len(s) < 6:
                    continue
                people = sum(1 for n in NAMES if n in s)
                for k, (_, rx) in CLASSES.items():
                    if k == "R2" and people < 2:
                        continue
                    if want and k != want:
                        continue
                    if rx.search(s):
                        hits[k].append((f.name, ln, label, s))
                        break

    for k in ("R1", "R2", "R3"):
        rows = hits[k]
        name, _ = CLASSES[k]
        if summary:
            if rows:
                print(f"{k} {name}：{len(rows)} 条，涉及 {len({r[0] for r in rows})} 个文件")
            continue
        if not rows:
            continue
        print(f"\n=== {k} {name}（{len(rows)} 条）===")
        for f, ln, label, s in rows[:limit] if limit else rows:
            print(f"{f}:{ln} [{label}] {s[:110]}")

    if summary:
        total = sum(len(v) for v in hits.values())
        print(f"合计候选 {total} 条（本工具只取候选，需人判；恒 exit 0）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
