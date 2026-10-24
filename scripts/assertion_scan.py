#!/usr/bin/env python3
"""断言层六类成因预筛（T2 断言全扫的取候选步骤）。

用途：审查 T2 档，把「全书分析行里最可能藏着施事/归属/年龄/章号错误」的行先筛出来，
人只读命中行——不做素读、不逐块 R4。判据来自 2026-10-22/23 六次快审的已查缺陷反推。

六类（见 docs/rules/审查表.md §0）：
  ① 相对章号   ② 绝对断言   ③ 年龄/数字/计数
  ④ 亲属/身份  ⑤ 方向/施受/债务   ⑥ 场景/方位/时距

产出：每行 `<文件>:<行号> [类] <内容前 120 字>`；`--json` 出结构化。
退出码：0 恒（这是取候选，不是判红）。`--summary` 只打每类计数。
"""
import argparse, json, os, re, sys

# 顺序＝T2 的阅读优先级：①②③⑥ 高信噪比先读；④⑤ 噪声大，抽样读。
CLASSES = [
    ("①相对章号", r"上一章|下一章|前一章|后一章|第一章|第[0-9一二三四五六七八九十]+章"),
    ("②绝对断言", r"唯一|第一次|最后一次|从未|从来没有|总是|最先|再也没有|空前"),
    ("③年龄数字", r"[0-9]+ ?(岁|年|英里|条|个|次|天|小时|分钟)|数十|几百|上千|半数"),
    ("⑥场景方位", r"门口|屋内|窗外|车里|街对面|楼下|楼上|隔.{0,4}(条街|一栋|一堵)|当天|次日|[0-9]+ ?年后"),
    ("⑤方向施受", r"把.{1,12}(写成|说成|当作|当成了)|被.{1,12}(写成|说成)|欠|替.{1,6}(顶|背|受)"),
    ("④亲属身份", r"母亲|父亲|姐姐|妹妹|哥哥|弟弟|妻子|丈夫|继母|养父|养母|女儿|儿子|表亲"),
]
PAT = [(n, re.compile(p)) for n, p in CLASSES]
SKIP = re.compile(r"^\s*(>.*\*\*原句|#|\||```)")


def scan_book(book):
    hits = []
    for root, _, files in os.walk(book):
        if "/text" in root or "/library" in root or "/.git" in root:
            continue
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            for i, line in enumerate(open(path, encoding="utf-8", errors="ignore"), 1):
                if SKIP.match(line) or len(line.strip()) < 8:
                    continue
                for name, rx in PAT:
                    m = rx.search(line)
                    if m:
                        hits.append({"file": os.path.relpath(path, book), "line": i,
                                     "class": name, "match": m.group(0),
                                     "text": line.strip()[:120]})
                        break
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--limit-per-class", type=int, default=0, help="每类最多打几行（0=全打）")
    ap.add_argument("--classes", default="", help="只扫指定类，逗号分隔，如 ①,②,③,⑥")
    a = ap.parse_args()
    if not os.path.isdir(a.book):
        print(f"❌ 不是目录：{a.book}", file=sys.stderr); return 2
    hits = scan_book(a.book)
    if a.classes:
        want = tuple(x.strip() for x in a.classes.split(",") if x.strip())
        hits = [h for h in hits if h["class"].startswith(want)]
    if a.json:
        print(json.dumps(hits, ensure_ascii=False, indent=1)); return 0
    if a.summary:
        from collections import Counter
        c = Counter(h["class"] for h in hits)
        print(f"六类候选合计 {len(hits)} 行")
        for n, _ in CLASSES:
            print(f"  {n}\t{c.get(n,0)}")
        return 0
    from collections import OrderedDict
    per = OrderedDict()
    for h in hits:
        per.setdefault(h["class"], []).append(h)
    order = [n for n, _ in CLASSES]
    for name in order:
        rows = per.get(name, [])
        if not rows:
            continue
        rows.sort(key=lambda h: (h["file"], h["line"]))
        show = rows[: a.limit_per_class] if a.limit_per_class else rows
        print(f"\n=== {name}：{len(rows)} 行" + (f"（示前 {len(show)}）" if a.limit_per_class else "") + " ===")
        for h in show:
            print(f"{h['file']}:{h['line']} {h['text']}")
    print(f"\n合计 {len(hits)} 行候选 / {len({(h['file']) for h in hits})} 个文件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
