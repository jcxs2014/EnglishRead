#!/usr/bin/env python3
"""列出精读 md 里的 U+FFFD（以及双句号）损坏位置。

用途：写入长 md 时偶发多字节截断，corruption_scan 只报行号，
本脚本直接给出上下文与码位，便于定点替换。

用法：
    python3 scripts/fffd_check.py <书目录>
"""
import io
import os
import sys
import glob

BAD = chr(0xFFFD)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = sys.argv[1]
    total = 0
    for path in sorted(glob.glob(os.path.join(root, "*.md"))):
        s = io.open(path, encoding="utf-8").read()
        for i, ch in enumerate(s):
            if ch != BAD:
                continue
            ln = s.count("\n", 0, i) + 1
            line = s.split("\n")[ln - 1]
            col = i - (s.rfind("\n", 0, i) + 1)
            print(f"{os.path.basename(path)}:{ln}:{col}  …{s[max(0,i-40):i]}"
                  f"[{ch}]"
                  f"{s[i+1:i+40]}…")
            print(f"    码位上下文: {[hex(ord(c)) for c in line[max(0,col-6):col+6]]}")
            total += 1
    print(f"--- U+FFFD 合计 {total} 处 ---")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
