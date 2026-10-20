#!/usr/bin/env python3
"""模板 → 成品：把 md 模板里的 {{...}} 占位符替换为 text/ 原文的**逐字**片段。
占位符语法: {{TAG|起始锚|结束锚|K}}
  起始锚：
    普通   → 起点 = 该锚所在**句**的开头
    ^ 前缀 → 同上，但**跳过句首的引号**（`“` `"` `‘` `'`）——用于中途发言节选
    ~ 前缀 → 起点 = 该锚在原文中的位置（精确到字）
  结束锚：
    普通   → 终点 = 该锚所在**句**的末尾（默认去掉尾部引号与空白）
    ~ 前缀 → 终点 = 该锚在原文中的结束位置（精确到字）
  第四段 K → 保留末尾的原文引号（完整发言用）
用法: python3 fill.py <ch> <模板路径> <成品路径>
"""
import re, glob, sys, os

BOOK = os.environ.get("ER_BOOK", "notes/books/novels/the-dues-don-ts-of-magic-by-delemhach")
ch = int(sys.argv[1])
tpl_path, out_path = sys.argv[2], sys.argv[3]
src = open(glob.glob(f"{BOOK}/text/ch{ch:02d}_*.txt")[0], encoding="utf-8").read()
md = open(tpl_path, encoding="utf-8").read()

# ---- 预检：一次性报出全部查无的锚点 ----
_bad = []
for _m in re.finditer(r'\{\{([^}]+)\}\}', md):
    _ps = _m.group(1).split("|")
    if len(_ps) > 2 and _ps[-1].strip().upper() == "K":
        _ps = _ps[:-1]
    for _a in _ps[1:3]:
        if not _a:
            continue
        _k = _a[1:] if _a[0] in "~^" else _a
        if _k not in src:
            _bad.append((_ps[0], _k))
if _bad:
    print("❌ 锚点查无：")
    for _t, _k in _bad:
        print(f"   [{_t}] {_k!r}")
    raise SystemExit(1)

units, pos = [], 0
for m in re.finditer(r'[.!?][”"’\']*(?=\s|$)|\n[ \t]*\n', src):
    end = m.end()
    if end > pos and src[pos:end].strip():
        units.append((pos, end))
    pos = end
if src[pos:].strip():
    units.append((pos, len(src)))

def unit_of(anchor):
    for i, (a, b) in enumerate(units):
        if anchor in src[a:b]:
            return i
    raise SystemExit(f"❌ 锚查无: {anchor!r}")

filled = []
def rep(m):
    parts = m.group(1).split("|")
    tag = parts[0]
    keep = len(parts) > 2 and parts[-1].strip().upper() == "K"
    if keep:
        parts = parts[:-1]
    a = parts[1]
    b = parts[2] if len(parts) > 2 else ""
    a_tilde, a_caret = a.startswith("~"), a.startswith("^")
    ka = a[1:] if (a_tilde or a_caret) else a
    kb = b[1:] if b.startswith("~") else b
    if a_tilde:
        i = src.find(ka)
        if i < 0:
            raise SystemExit(f"❌ 锚查无: {ka!r} ({tag})")
        start = i
    else:
        start = units[unit_of(ka)][0]
    if not b:
        end = units[unit_of(ka)][1]
        trim = True
    elif b.startswith("~"):
        i = src.find(kb)
        if i < 0:
            raise SystemExit(f"❌ 锚查无: {kb!r} ({tag})")
        end = i + len(kb)
        trim = False
    else:
        end = units[unit_of(kb)][1]
        trim = True
    frag = src[start:end]
    if trim and not keep:
        frag = re.sub(r'[\s”"]+$', '', frag)
    frag = frag.lstrip()
    if a_caret:
        while frag[:1] in ('“', '"', '‘', "'"):
            frag = frag[1:]
    filled.append((tag, frag))
    return frag

out = re.sub(r'\{\{([^}]+)\}\}', rep, md)
open(out_path, "w", encoding="utf-8").write(out)
print(f"✅ 回填 {len(filled)} 处 → {out_path}")
for t, f in filled:
    print(f"  [{t}] {f[:110]}")
