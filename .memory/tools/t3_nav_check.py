#!/usr/bin/env python3
"""t3_nav_check.py — 「本章导航」+「一句话总结」层的**专名/数字锚定**核验（35 章全量）

层结构：
- `## 本章导航`：一句话概括 / 情感弧线位置 / Tropes 兑现/反转 / 人物弧线 / 叙事手法
- `## 一句话总结`

核两条：
1. **专名锚定**：导航层与总结层里出现的**人名/地名/机构名**（大写词组、去掉句首大写），
   是否在**全书** `text/` 出现过。查无 ⇒ 凭空生词候选。
2. **数字锚定**：层里的数字（含中文数字）是否在**本章** `text/` 出现。查无 ⇒ 数字无出处候选。

口径（重要）：
- 只取**中文层**（不含引号内的英文引文）——引文内的词已由引文逐字核验覆盖。
- 专名判定：连续 2 个以上首字母大写的词（如 "Crescent City"），或已知名词表。
- 数字判定：阿拉伯数字 + 常见中文数字量词（百/千/万）。
- 排除常见词表（Agency/CEO 等若全书有则通过）。

退出码：0 = 无候选；1 = 有候选。
"""
import os
import re
import sys

CJK = re.compile(r"[一-鿿]")
PROPER2 = re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b")
NUM = re.compile(r"\b(\d{1,4})\b")
CN_NUM = re.compile(r"([一二三四五六七八九十百千万两]+)(个|张|次|条|场|件|句|轮|点|只|本|束|人|根|小时|分钟|秒|周|年|天|页|美元|英里|英尺|里|块|磅|级|倍)")
# 泛指量词白名单：这些中文数字在原文里必然以英文单词出现（数词 + 泛指量词），
# 拿中文去查原文＝必然查无 ⇒ 假红，不参与数字锚定。
GENERIC = {("一", "个"), ("一", "张"), ("一", "次"), ("一", "条"), ("一", "场"), ("一", "件"),
           ("一", "句"), ("一", "轮"), ("一", "点"), ("一", "只"), ("一", "本"), ("一", "束"),
           ("一", "人"), ("两", "人"), ("两", "张"), ("两", "个"), ("两", "条"), ("两", "次"),
           ("三", "个"), ("三", "场"), ("三", "次"), ("三", "句"), ("四", "个"),
           ("四", "人"), ("四", "条"), ("四", "张")}
CN_DIGIT = {"一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7,
             "八": 8, "九": 9}
UNITS = {"十": 10, "百": 100, "千": 1000}


def cn_to_int(s):
    """把中文数字串转成 int（支持到千位级；不支持则返回 None）"""
    if not s:
        return None
    total, section, number = 0, 0, 0
    for ch in s:
        if ch in CN_DIGIT:
            number = CN_DIGIT[ch]
        elif ch in UNITS:
            section += (number or 1) * UNITS[ch]
            number = 0
        elif ch == "万":
            total += (section + number) * 10000
            section = number = 0
        else:
            return None
    return total + section + number


_ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
         "eighty", "ninety"]


def to_english(n):
    """整数 → 英文数词（用于「中文数字 ↔ 英文原文」的锚定）"""
    if n is None or n < 0 or n > 9999:
        return set()
    out = set()
    if n < 20:
        out.add(_ONES[n])
    elif n < 100:
        t, r = divmod(n, 10)
        out.add(_TENS[t])
        if r:
            out.add(f"{_TENS[t]}-{_ONES[r]}")
    elif n < 1000:
        h, r = divmod(n, 100)
        base = f"{_ONES[h]} hundred"
        out.add(base)
        if r:
            e = sorted(to_english(r))[0]
            out.add(f"{base} and {e}")
            out.add(f"{base} {e}")
    else:
        th, r = divmod(n, 1000)
        base = f"{_ONES[th]} thousand"
        out.add(base)
        if r:
            e = sorted(to_english(r))[0]
            out.add(f"{base} {e}")
    return {x for x in out if x}
STOP = {
    "The", "This", "That", "There", "These", "Those", "And", "But", "For", "She",
    "He", "They", "We", "You", "It", "Its", "His", "Her", "Their", "Our", "My",
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    "Meanwhile", "Instead", "However", "Then", "When", "While", "Because", "Before",
    "After", "Until", "Though", "Despite", "Since", "Once", "Every", "Each",
    "Chapter", "Part", "Prologue", "Epilogue", "The End",
}


def sections(md):
    out = {}
    for key, start, end in (("nav", "## 本章导航", "## 精读"),
                            ("sum", "## 一句话总结", None)):
        i = md.find(start)
        if i < 0:
            continue
        j = md.find(end, i) if end else len(md)
        out[key] = md[i:j if j > i else len(md)]
    return out


def main():
    book_dir = sys.argv[1]
    tdir = os.path.join(book_dir, "text")
    alltext = ""
    chapter_text = {}
    for f in sorted(os.listdir(tdir)):
        if f.startswith("ch") and f.endswith(".txt"):
            t = open(os.path.join(tdir, f), encoding="utf-8").read()
            alltext += "\n" + t
            chapter_text[f[:4]] = t
    alltext = alltext.lower()

    md_files = sorted(f for f in os.listdir(book_dir) if f.startswith("ch") and f.endswith(".md"))
    bad_names, bad_nums = [], []
    n_name = n_num = 0
    for mf in md_files:
        ch = mf[:4]
        md = open(os.path.join(book_dir, mf), encoding="utf-8").read()
        ct = chapter_text.get(ch, "").lower()
        for key, seg in sections(md).items():
            for ln_no, line in enumerate(seg.splitlines(), 1):
                if not CJK.search(line):
                    continue          # 只核中文层
                # 去引号内英文
                clean = re.sub(r"“[^”]*”|\"[^\"]*\"", " ", line)
                for m in PROPER2.finditer(clean):
                    name = m.group(1)
                    if name.split()[0] in STOP:
                        continue
                    n_name += 1
                    if name.lower() not in alltext:
                        bad_names.append((ch, key, name, line.strip()[:90]))
                for m in NUM.finditer(clean):
                    n_num += 1
                    if m.group(1) not in ct:
                        bad_nums.append((ch, key, m.group(1), line.strip()[:90]))
                for m in CN_NUM.finditer(clean):
                    n_num += 1
                    num, unit = m.group(1), m.group(2)
                    if (num, unit) in GENERIC:
                        n_num -= 1
                        continue
                    iv = cn_to_int(num)
                    cands = {str(iv)} if iv is not None else set()
                    cands |= {num}
                    if iv is not None:
                        cands |= to_english(iv)
                    if not any(c in ct for c in cands if c):
                        bad_nums.append((ch, key, m.group(0), line.strip()[:90]))
    print("── 专名（全书查无）──")
    for ch, k, n, l in bad_names:
        print(f"❌ {ch} [{k}] 专名「{n}」 ｜ {l}")
    print("── 数字（本章查无）──")
    for ch, k, n, l in bad_nums:
        print(f"❌ {ch} [{k}] 数字「{n}」 ｜ {l}")
    print("=" * 56)
    print(f"专名锚定 {n_name} ｜ 全书查无 {len(bad_names)} ｜ 数字锚定 {n_num} ｜ 本章查无 {len(bad_nums)}")
    return 1 if (bad_names or bad_nums) else 0


if __name__ == "__main__":
    sys.exit(main())
