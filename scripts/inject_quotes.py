#!/usr/bin/env python3
"""把 md 里的 «Q1»«Q2»… 占位符替换为 text/ 里逐字取出的引语（fail-closed）。

用法:
  python3 scripts/attic/inject_quotes.py <md> <chapter_text.txt> \
      'Q1<TAB>quote text' 'Q2<TAB>quote text' ...

做什么:
  1. 对每条引语做 flat 归一化（去非字母数字、小写），在本章 text/ 里断言存在；
  2. 任何一条 MISS ⇒ 退出码 2 且**不写文件**（宁可什么都不产出，也不要落一句伪造引语）；
  3. 全部 HIT 才把 «QN» 占位符按出现顺序替换成原文（首尾空白裁掉，保留原文标点）。

为什么需要它（AGENTS 8.2 禁令 1 + 1c）:
  「复制粘贴不手打」在长批量里仍会走形；`flat` 断言是唯一的机械保证。
  本脚本是**生产工具**（替代「手打引语」这个会出错的动作），不是事后检测器。
"""
import re
import sys
from pathlib import Path

md_path = Path(sys.argv[1])
txt_path = Path(sys.argv[2])
specs = sys.argv[3:]

if len(sys.argv) < 4:
    print(__doc__)
    sys.exit(2)


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


text = txt_path.read_text(encoding="utf-8")
flat_text = flat(text)

pairs = []
for spec in specs:
    if "\t" not in spec:
        print(f"❌ 参数须为 'Q1<TAB>引语': {spec[:40]}")
        sys.exit(2)
    tag, quote = spec.split("\t", 1)
    pairs.append((tag.strip(), quote.strip()))

bad = [f"{tag}: 本章 text/ flat 查无 ⇒ {q[:60]!r}" for tag, q in pairs if flat(q) not in flat_text]
if bad:
    print("\n".join(bad))
    print(f"\n❌ {len(bad)}/{len(pairs)} 条未命中，未写入（宁缺毋造）")
    sys.exit(2)

# 排版规范化 + 非 ASCII 字符体检：
# ① 直引号统一成原文用的 ’（U+2019）——手打直引号是最高频的字形走形；
# ② 引语里每个非 ASCII 字符必须在原文出现——抓「把 … 打成 –」「— 打成 —」这类（#1972）。
fixed = []
for tag, q in pairs:
    q2 = q.replace("'", "’")
    for chx in q2:
        if ord(chx) > 127 and chx not in text:
            print(f"❌ {tag}: 字符 {chx!r} (U+{ord(chx):04X}) 本章原文未出现（可能是手打走形）")
            sys.exit(2)
    fixed.append((tag, q2))

md = md_path.read_text(encoding="utf-8")
for tag, quote in fixed:
    md = md.replace(f"«{tag}»", quote)

# ⚠️ 2026-10-06 修（EMNR ch43 实测假绿）：原判据 `re.findall(r"«Q\d+»", md)`
# 要求成对的 »，所以**占位符被写坏时（`«Q8\`` 这类右括号落成反引号）正则匹配不到，
# 残留检查静默通过、脚本仍打印「✅ 全部注入」并 exit 0**——而那一块根本没注入。
# 现在改为「文件里只要还有任何一个占位符引号就算失败」，并打印可疑行号，
# 让写坏占位符这种情况在注入这一步就被挡住，而不是留到门禁的关键词/逐字层才发现。
left = [(i + 1, ln) for i, ln in enumerate(md.split("\n")) if "«" in ln or "»" in ln]
if left:
    print(f"❌ 仍有占位符未替换（{len(left)} 行）——"
          "常见原因：占位符被写坏（如 «Q8` 缺右括号）或 tag 拼错：")
    for n, ln in left[:8]:
        print(f"   L{n}: {ln[:110]}")
    sys.exit(2)

md_path.write_text(md, encoding="utf-8")
print(f"✅ {md_path.name}: {len(pairs)} 条引语全部 flat 命中本章并已注入")
