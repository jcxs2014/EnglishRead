#!/usr/bin/env python3
"""审查用：核对「独立成段，N 个词」这类**可机械判定**的词数断言。

判据（只查有唯一真值的形态）：
  ① 行内声明「独立成段 / 单独成段」＋「N 个词」→ 取该块引语，数 flat 后的词数
  ② 行内形如 「只有 N 个词」紧跟一个反引号英文串 → 数那个串
其余形态（「三个词」泛指、指示语内子短语）**不判**，避免假红。
"""
import glob
import os
import re
import sys
import unicodedata

CN = {"一":1,"二":2,"两":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10,
      "半":None}


def cn2int(s):
    if s.isdigit():
        return int(s)
    if "十" in s:
        a, b = s.split("十")
        return (CN.get(a, 1) if a else 1) * 10 + (CN.get(b, 0) if b else 0)
    return CN.get(s)


def words(s: str) -> int:
    """连写算 1 词；don't 算 1 词；well-known 算 2 词（audit_numbers 同口径）。"""
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"[’‘]", "'", s)
    toks = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", s)
    return len(toks)


def main() -> int:
    book = sys.argv[1]
    bad = []
    for md in sorted(glob.glob(os.path.join(book, "ch*.md"))):
        name = os.path.basename(md)
        body = open(md, encoding="utf-8").read()
        blocks = re.split(r"^> \*\*原句 \d+:\*\* ", body, flags=re.M)[1:]
        for p in blocks:
            lines = p.split("\n")
            quote = lines[0].strip().strip('"“”')
            for line in lines[1:]:
                if not line.startswith("- **"):
                    continue
                # 形态①：独立成段/单独成段 …… N 个词
                m = re.search(r"独立成段|单独成段", line)
                if m:
                    n = re.search(r"([一二两三四五六七八九十]|\d+)\s*个?词", line)
                    if n:
                        want = cn2int(n.group(1))
                        got = words(quote)
                        if want and got != want:
                            bad.append((name, quote[:50], want, got, "独立成段"))
                # 形态②：只有 N 个词 + **紧邻**反引号英文短语
                # ⚠️ 2026-10-01 两次修正（都记在这里，因为它们互相打脸）：
                # ① 初版对形态②一律数「反引号内的短语」——若断言写的是
                #    「全章最后一句只有八个词」而反引号里只是被讨论的那个词
                #    （ch28 `So` 写 8 实 1 / ch31 `When I was a child` 写 2 实 5），
                #    就是假红。
                # ② 改成「一律数整条引语」后假红更多（ch02 We represent the
                #    children 写 2 实 4、ch53 写 1 实 11…），因为中文里
                #    「N 个词」常指引语内**被拎出来谈的那个短语**。
                # ⇒ 现行判据：反引号短语与断言**同子句且紧邻**才数它，
                #    否则**不判**（宁可漏，不制造假红）。
                m2 = re.search(
                    r"只有\s*([一二两三四五六七八九十]|\d+)\s*个?词[^。]{0,12}`([^`]+)`",
                    line,
                )
                if m2:
                    want = cn2int(m2.group(1))
                    got = words(m2.group(2))
                    if want and got != want:
                        bad.append((name, m2.group(2)[:50], want, got, "只有N个词+紧邻短语"))
    print(f"=== 可机械判定的词数断言：不符 {len(bad)} 条 ===")
    for n, q, w, g, kind in bad:
        print(f"❌ {n} [{kind}] 「{q}」 写 {w} 实 {g}")
    return 2 if bad else 0


if __name__ == "__main__":
    sys.exit(main())