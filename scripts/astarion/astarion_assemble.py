#!/usr/bin/env python3
"""把 spec + tiers 两份 JSON 装订成一章 md。

分工：引语与词表**都不手打**——
  引语 ← astarion_build.py 按首尾锚点从 text/ 逐字切片（取不到即 exit 2）
  词表 ← build_vocab_table.py 从 tiers.json 建表（词头不在本章即 exit 2）
本脚本只负责把两份产物按本书骨架拼起来，并把文件名定成 `chNN <slug>.md`。

⚠️ 幂等：spec 里若已有 vocab_file 则忽略命令行传入的，避免重跑时错位。
"""
import json
import os
import subprocess
import sys

BOOK = "notes/books/novels/astarion-by-t-kingfisher"
SPEC_DIR = "scripts/attic/spec/astarion"
CH01 = "scripts/attic/astarion_ch01.json"


def main():
    chapters = sys.argv[1:-1]
    out_name = sys.argv[-1]          # 末位是输出文件名模板里用的 slug dict 文件
    names = json.load(open(out_name, encoding="utf-8"))
    tmp = "/private/var/folders/zp/wpjjl43x5q71v8g4pp42tl_80000gn/T/opencode"
    os.makedirs(tmp, exist_ok=True)
    for n in chapters:
        spec = CH01 if n == "01" else f"{SPEC_DIR}/ch{n}.json"
        tiers = f"{SPEC_DIR}/ch{n}.tiers.json"
        if not os.path.exists(spec):
            sys.exit("缺 spec: %s" % spec)
        if not os.path.exists(tiers):
            sys.exit("缺 tiers: %s" % tiers)
        vfile = f"{tmp}/astarion_vocab_{n}.md"
        r = subprocess.run(
            ["python3", "scripts/build_vocab_table.py", BOOK, "--ch", n,
             "--tiers", tiers],
            capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("ch%s 词表构建失败：\n%s" % (n, r.stderr))
        open(vfile, "w", encoding="utf-8").write(r.stdout)
        d = json.load(open(spec, encoding="utf-8"))
        d["vocab_file"] = vfile
        spec2 = f"{tmp}/astarion_ch{n}.json"
        json.dump(d, open(spec2, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        out = os.path.join(BOOK, "ch%s %s.md" % (n, names[n]))
        r = subprocess.run(
            ["python3", "scripts/attic/astarion_build.py", BOOK, spec2, out],
            capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("ch%s 引语构建失败：\n%s" % (n, r.stderr))
        print(r.stdout.strip())


if __name__ == "__main__":
    main()
