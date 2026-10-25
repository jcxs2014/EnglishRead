#!/usr/bin/env python3
"""t3_suread_fix.py — R1 素读清单的**集中取证与格式化**（fail-closed）

子代理只写 `1-suread.raw.json`（锚点原文，无偏移）；本脚本负责：
  1. 回 `text/` 逐条核 anchor：**必须逐字存在且全文只出现一次**；
  2. 实测 start / end 字符偏移；
  3. 核通过才写 `1-suread.json`（带偏移的正式件）；核不过**不写**，
     逐条报告「哪一条不合格、命中几次、首次出现在哪」。

用法：
    python3 .memory/tools/t3_suread_fix.py "<书目录>" [ch01 ch02 …]

退出码：0 = 全部核过；1 = 有不合格条目（正式件未写）。
"""
import json
import os
import re
import sys


def text_path(book_dir, chno):
    tdir = os.path.join(book_dir, "text")
    digits = f"{int(chno):02d}"
    for f in sorted(os.listdir(tdir)):
        if re.match(rf"^ch{digits}([_. ].*)?\.txt$", f):
            return os.path.join(tdir, f)
    return None


def main():
    book_dir = sys.argv[1]
    review = os.path.join(".memory", "raw-gates",
                           os.path.basename(book_dir.rstrip("/")), "review")
    want = set(sys.argv[2:])
    dirs = sorted(d for d in os.listdir(review)
                  if re.match(r"^ch\d\d$", d) and (not want or d in want))
    ok = bad = 0
    for ch in dirs:
        raw_p = os.path.join(review, ch, "1-suread.raw.json")
        if not os.path.exists(raw_p):
            continue
        try:
            data = json.load(open(raw_p, encoding="utf-8"))
        except Exception as e:
            print(f"❌ {ch}: raw 解析失败 {e}")
            bad += 1
            continue
        tp = text_path(book_dir, ch[2:])
        if not tp:
            print(f"❌ {ch}: text/ 里找不到提取件")
            bad += 1
            continue
        text = open(tp, encoding="utf-8").read()
        facts, problems = [], []
        for i, f in enumerate(data.get("facts", []), 1):
            a = (f.get("anchor") or "").strip()
            if not a:
                problems.append(f"  fact {i}: anchor 为空")
                continue
            n = text.count(a)
            if n == 0:
                problems.append(f"  fact {i}: anchor 在原文查无（{a[:50]!r}）")
                continue
            if n > 1:
                first = text.find(a)
                problems.append(f"  fact {i}: anchor 出现 {n} 次（不唯一，首次在 {first}）")
                continue
            st = text.find(a)
            facts.append({"anchor": a, "start": st, "end": st + len(a),
                          "fact": f.get("fact", "").strip()})
        if len(facts) < 5:
            problems.append(f"  facts 仅 {len(facts)} 条（<5，不合格）")
        if problems:
            print(f"❌ {ch}: {len(problems)} 项不合格 → 正式件未写")
            for p in problems:
                print(p)
            bad += 1
            continue
        out = {"chapter": data.get("chapter", ch),
               "facts": facts,
               "turning_point": data.get("turning_point", "").strip()}
        with open(os.path.join(review, ch, "1-suread.json"), "w", encoding="utf-8") as fp:
            json.dump(out, fp, ensure_ascii=False, indent=2)
        print(f"✅ {ch}: {len(facts)} 条事实全部核过（锚点唯一、逐字命中）")
        ok += 1
    print("=" * 50)
    print(f"核过 {ok} 章 ｜ 不合格 {bad} 章")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
