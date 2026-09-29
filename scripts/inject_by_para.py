#!/usr/bin/env python3
"""按「定位前缀」从 text/ 逐字取引语，注入 md 的 «QN» 占位符（零手打）。

用法:
  python3 scripts/inject_by_para.py <md> <ch.txt> 'Q1=@The army has launched' ...
  python3 scripts/inject_by_para.py <md> <ch.txt> 'Q1=@Viv ignored*' ...   # * = 取整段

两种取法:
  Q1=@prefix      取「以 prefix 开头的那一句」（在所有段落里唯一定位）
  Q1=@prefix*     取「含 prefix 的那一整段」

为什么改成前缀定位而不是段落号:
  段落号要先把全文空行切分后数行（读正文时不方便），前缀只要抄短的一小段，
  而**引语本身仍是脚本从原文逐字取的**——引语字形不可能与原文不同
  （em dash / 弯引号 / 软连字符都由原文带出，见记忆 #1972）。

硬保证（任一不满足 ⇒ 退出码 2 且**不写文件**）:
  - 前缀必须唯一定位（0 处或多处都报错）——防「我以为在 A 段其实在 B 段」；
  - 取出的串 flat 归一化后必须在本章 text/ 内；
  - md 里出现未被 spec 覆盖的 «QN» ⇒ 报错不写；
  - 引语里每个非 ASCII 字符必须在原文出现（抓手打走形）。
"""
import re
import sys
from pathlib import Path


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def sents(par: str):
    """按句边界切段。

    ⚠️ 2026-09-29 修正：原实现 `(?<=[.?!])\\s+` 把 `Mr. Vandermeer` 切成两段
    ⇒ `+N` 连取少取片段（ch08 第 ⑧ 块因此被截成 2/3 段）。
    修法：句号后若紧跟的是**称谓/缩写**，不视为句边界。
    """
    ABBR = (r"Mr|Mrs|Ms|Dr|Prof|St|Mt|Rev|Hon|Sen|Rep|Gov|Gen|Col|Capt|Lt|Sgt|"
            r"Mme|Mlle|Sr|Jr|Fr|vs|etc|Nos|Fig|Vol|Op|pp|ca|cf|ed|al")
    text = par.strip()
    out, start = [], 0
    for m in re.finditer(r"[.?!]\s+", text):
        # 判据是**句点之前**那个词：Mr. / Mrs. / etc. / p.m. 收尾 ⇒ 不是句边界。
        # （先看句点之后是错的：`Mr. Vandermeer` 后面是 "Vandermeer"，匹配不上。）
        if re.search(rf"(?:^|\W)(?:{ABBR})\.$", text[:m.start() + 1], re.I):
            continue
        # 3 p.m. / U.S. / e.g. 这类「单字母.」缩写同理
        if re.search(r"(?:^|\W)[A-Za-z](?:\.[A-Za-z])?\.$", text[:m.start() + 1]):
            continue
            continue
        piece = text[start:m.start() + 1].strip()
        if piece:
            out.append(piece)
        start = m.end()
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    return out


md_path, txt_path = Path(sys.argv[1]), Path(sys.argv[2])
specs = sys.argv[3:]
if not specs:
    print(__doc__)
    sys.exit(2)

raw = txt_path.read_text(encoding="utf-8")
paras = [p for p in raw.split("\n\n") if p.strip()]
sent_list = [(pi, i, s) for pi, p in enumerate(paras) for i, s in enumerate(sents(p))]

pairs = []
for spec in specs:
    if "=" not in spec:
        print(f"❌ spec 须为 'Q1=@前缀'（或 'Q1=@前缀*'）: {spec}")
        sys.exit(2)
    tag, loc = spec.split("=", 1)
    tag, loc = tag.strip(), loc.strip()
    if not loc.startswith("@"):
        print(f"❌ {tag}: 前缀须以 @ 开头: {loc}")
        sys.exit(2)
    whole = loc.endswith("*")
    body = loc[1:].rstrip("*").strip()
    span = 0
    m = re.match(r"^(.*?)\+(\d+)$", body)
    if m:
        body, span = m.group(1).strip(), int(m.group(2))
    pref = body
    fp = flat(pref)
    if not fp:
        print(f"❌ {tag}: 前缀为空")
        sys.exit(2)

    if whole:
        hits = [(pi, p) for pi, p in enumerate(paras) if fp in flat(p)]
        if len(hits) != 1:
            print(f"❌ {tag}: 前缀 {pref!r} 在 {len(hits)} 段命中（须唯一）")
            sys.exit(2)
        quote = hits[0][1].strip()
    else:
        hits = [(pi, i, s) for pi, i, s in sent_list if flat(s).startswith(fp)]
        if len(hits) != 1:
            print(f"❌ {tag}: 前缀 {pref!r} 在 {len(hits)} 句命中（须唯一）")
            sys.exit(2)
        pi, i0, _ = hits[0]
        n_more = span
        if n_more:
            same = [s for pi2, i2, s in sent_list if pi2 == pi and i2 > i0]
            if len(same) < n_more:
                print(f"❌ {tag}: 段 {pi} 在该句之后只有 {len(same)} 句，取 +{n_more} 越界")
                sys.exit(2)
            quote = " ".join([hits[0][2]] + same[:n_more])
        else:
            quote = hits[0][2]

    if flat(quote) not in flat(raw):
        print(f"❌ {tag}: 取出的串 flat 查无: {quote[:60]!r}")
        sys.exit(2)
    for chx in quote:
        if ord(chx) > 127 and chx not in raw:
            print(f"❌ {tag}: 字符 {chx!r} (U+{ord(chx):04X}) 本章原文未出现（手打走形？）")
            sys.exit(2)
    pairs.append((tag, quote))

md = md_path.read_text(encoding="utf-8")
for tag, quote in pairs:
    if f"«{tag}»" not in md:
        print(f"❌ md 里没有占位符 «{tag}»")
        sys.exit(2)
    md = md.replace(f"«{tag}»", quote)

left = sorted(set(re.findall(r"«Q\d+»", md)))
if left:
    print(f"❌ 仍有占位符未替换: {left}")
    sys.exit(2)

md_path.write_text(md, encoding="utf-8")
print(f"✅ {md_path.name}: {len(pairs)} 条引语按前缀逐字注入本章 text/（零手打）")
for tag, q in pairs:
    print(f"   {tag}: {q[:76]}{'…' if len(q) > 76 else ''}")
