#!/usr/bin/env python3
"""严格引语比对（保留标点）——sweep_full 的补充实现，用于抓「标点/词形被替换」型伪造。

与 sweep_full 的差别：sweep_full 的 flat 比对会抹掉标点，因此
「句末 . 写成 :」「that's 写成 thats」「— 写成 -」这类改动**它查不出来**。
本脚本只抹掉引语首尾的成对引号，**保留句中标点**。

用法：python3 strict_quote_check.py <书目录>
退出码：0 = 全部命中；2 = 有未命中
"""
import re
import sys
import unicodedata
from pathlib import Path


def norm(s: str) -> str:
    """归一化：NFC + 弯引号转直 + 破折号统一 + 压缩空白，但**不删标点**。"""
    s = unicodedata.normalize("NFC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("—", "-"), ("–", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def strip_outer_quotes(s: str) -> str:
    """去掉引语块最外层的成对引号（md 保留了，text 里靠说话人标签带出）。"""
    s = norm(s)
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return s[1:-1]
    return s


def key(s: str) -> str:
    """比对键：保留 . , ; : ! ? - 与单双引号，丢弃其余标点与空白。"""
    s = strip_outer_quotes(s)
    return re.sub(r"[^a-z0-9.,;:!?\"'-]", "", s.lower())


def main() -> int:
    book = Path(sys.argv[1])
    md_files = sorted(
        p for p in book.glob("ch*.md") if not p.name.startswith("00_")
    )
    total = 0
    misses = []
    for md in md_files:
        text_files = sorted((book / "text").glob(f"{md.stem[:4]}*.txt"))
        if not text_files:
            misses.append((md.name, "?", "找不到对应 text/ 提取件"))
            continue
        tt = key(text_files[0].read_text(encoding="utf-8"))
        body = md.read_text(encoding="utf-8")
        for q in re.findall(r"^> \*\*原句 \d+:\*\* (.+)$", body, re.M):
            total += 1
            qk = key(q)
            if qk in tt:
                continue
            # 二分找最长命中前缀，定位首个偏离字符
            lo, hi = 0, len(qk)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if qk[:mid] in tt:
                    lo = mid
                else:
                    hi = mid - 1
            misses.append((md.name, q, f"前缀 {lo}/{len(qk)}｜偏离处 {qk[lo:lo + 45]!r}"))

    for name, q, why in misses:
        print(f"❌ {name}  {why}")
        print(f"   引语: {q[:140]}")

    print(f"=== 严格比对（保留标点）: {total - len(misses)}/{total} 命中 ===")
    if misses:
        print("⚠️ 有未命中——逐条人工判：是真实伪造，还是省略式截断/说话人标签差异")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
