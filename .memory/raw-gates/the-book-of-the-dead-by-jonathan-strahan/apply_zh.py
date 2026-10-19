#!/usr/bin/env python3
"""把「我手写的中文规格」精确落盘到章文件里。

**设计原则（对应 AGENTS 第 8 条 + 记忆 #1965 / #2042）**
------------------------------------------------
1. **内容由规格给出，脚本不生成任何文字**——本脚本只做「整行精确替换」。
2. **行级作用域**：不跨块、不跨行做正则 sub（AGENTS 第 9 条 g）。
3. **引语行不可动**：改前改后逐字节比对 `> **原句 N:**` 行集合，不一致即中止。
4. **原子写**：同目录 mkstemp → 写全量 → os.replace（记忆 #2042：`open(p,"w")` 会截断文件）。
5. **幂等**：目标行已等于新内容时跳过，重跑不会二次损坏。

用法：
    python3 apply_zh.py "<书目录>" "<spec.py>"
"""
import glob
import os
import re
import sys
import tempfile

BOOK = sys.argv[1]
SPEC = sys.argv[2]

ns = {}
with open(SPEC, encoding="utf-8") as f:
    _src = f.read()
# ⚠️ 规格文件自身体检：中文里混入 U+FFFD 会随内容落进 md
_bad = [i for i, c in enumerate(_src) if c == "�" or ord(c) == 0]
if _bad:
    for i in _bad[:5]:
        print(f"❌ 规格文件含损坏字符（位置 {i}）：{_src[max(0,i-25):i+25]!r}")
    sys.exit(f"{SPEC}: 规格含 U+FFFD/NUL，中止")
exec(compile(_src, SPEC, "exec"), ns)
SPECS = ns["SPECS"]


def find_section(lines, anchor):
    """返回 (起, 止) 行号区间：anchor 标题行之后到下一个同级标题行之前。"""
    start = None
    for i, ln in enumerate(lines):
        if re.match(r"^#{2,4}[ \t]*" + re.escape(anchor) + r"[ \t]*$", ln):
            start = i
            break
    if start is None:
        return None
    for j in range(start + 1, len(lines)):
        if re.match(r"^#{2,4}[ \t]+", lines[j]) or re.match(r"^\*\*[^*]+\*\*[ \t]*$", lines[j]):
            return (start + 1, j)
    return (start + 1, len(lines))


def quote_lines(lines):
    return [ln for ln in lines if ln.startswith("> ")]


def apply_one(fname, spec):
    path = os.path.join(BOOK, fname)
    with open(path, encoding="utf-8") as f:
        orig = f.read()
    lines = orig.split("\n")
    n_before = len(lines)
    q_before = quote_lines(lines)

    # ---- 1) 导航层：逐条替换 `- **键**：值` ----
    nav = spec.get("nav")
    if nav:
        rng = find_section(lines, "本章导航")
        if rng is None:
            sys.exit(f"{fname}: 找不到「## 本章导航」节")
        done = set()
        for i in range(rng[0], rng[1]):
            m = re.match(r"^(\s*[-*]\s*\*\*([^*]+)\*\*\s*[：:]\s*)(.*)$", lines[i])
            if not m:
                continue
            key = m.group(2).strip()
            if key in nav and key not in done:
                lines[i] = m.group(1) + nav[key]
                done.add(key)
        missing = set(nav) - done
        if missing:
            sys.exit(f"{fname}: 导航层未匹配到条目 {sorted(missing)}")

    # ---- 3) 词汇表整节替换 / 一句话总结整节替换 ----
    if "vocab" in spec:
        rng = find_section(lines, "本章词汇")
        if rng is None:
            sys.exit(f"{fname}: 找不到「## 本章词汇」节")
        body = ["", ""] + list(spec["vocab"]) + [""]
        lines[rng[0]:rng[1]] = body
    if "summary" in spec:
        rng = find_section(lines, "一句话总结")
        if rng is None:
            sys.exit(f"{fname}: 找不到「## 一句话总结」节")
        body = ["", ""] + list(spec["summary"]) + [""]
        lines[rng[0]:rng[1]] = body

    # ---- 4) 引语块内的四个字段 ----
    blocks = spec.get("blocks") or {}
    if blocks:
        # 定位每个 `> **原句 N:**` 行的下标
        idxs = [i for i, ln in enumerate(lines) if re.match(r"^> \*\*原句 \d+:\*\*", ln)]
        bounds = []
        for k, i in enumerate(idxs):
            end = idxs[k + 1] if k + 1 < len(idxs) else len(lines)
            bounds.append((i, end))
        seen = set()
        for (b0, b1) in bounds:
            m = re.match(r"^> \*\*原句 (\d+):\*\*", lines[b0])
            num = m.group(1)
            if num not in blocks:
                continue
            seen.add(num)
            fields = blocks[num]
            # 规格键名 → md 里的标签（两种写法都接受）
            alias = {"zh": "中文理解", "why": "为什么这样写", "tip": "读者视角提示",
                     "kw": "关键词", "struct": "句子结构"}
            fields = {alias.get(k, k): v for k, v in fields.items()}
            # ⚠️ 引语替换：只允许在**该章 text/ 里逐字存在**时进行（防伪造）
            if "quote" in fields:
                newq = fields.pop("quote")
                corpus = ""
                cnum = re.match(r"ch(\d+)", fname).group(1)
                for tp in sorted(glob.glob(os.path.join(BOOK, "text", "ch*.txt"))):
                    if os.path.basename(tp).startswith("ch" + cnum + "_"):
                        corpus += open(tp, encoding="utf-8").read()
                flat = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
                inner = newq.strip().strip('"').strip("“”")
                if not corpus or flat(inner) not in flat(corpus):
                    sys.exit(f"{fname} 原句 {num}: 新引语在 text/ 里查无，中止")
                lines[b0] = f'> **原句 {num}:** "{inner}"'
            for i in range(b0 + 1, b1):
                lm = re.match(r"^(\s*[-*]\s*\*\*([^*]+)\*\*\s*[：:]\s*)(.*)$", lines[i])
                if not lm:
                    continue
                key = lm.group(2).strip()
                if key in fields:
                    lines[i] = lm.group(1) + fields[key]
        miss = set(blocks) - seen
        if miss:
            sys.exit(f"{fname}: 未匹配到引语块 {sorted(miss)}")

    out = "\n".join(lines)
    # ---- 4) 安全断言 ----
    q_after = quote_lines(out.split("\n"))
    if q_before != q_after:
        # 只有规格显式声明了引语替换时才允许变动，且变动处必须逐字见于 text/
        changed = [i for i, (a, b) in enumerate(zip(q_before, q_after)) if a != b]
        declared = set()
        for fname2, sp in SPECS.items():
            for num, fields in (sp.get("blocks") or {}).items():
                if isinstance(fields, dict) and "quote" in fields:
                    declared.add((fname2, num))
        if len(changed) != len(declared):
            sys.exit(f"{fname}: 引语行被改动但未在规格中声明，中止")
        for c in changed:
            if not q_after[c].startswith("> **原句 "):
                sys.exit(f"{fname}: 引语行格式异常，中止")
    if len(lines) < n_before - 3:
        sys.exit(f"{fname}: 行数异常减少，中止")
    if "\x00" in out or "�" in out:
        sys.exit(f"{fname}: 输出含 NUL / U+FFFD，中止")
    if out == orig:
        print(f"· {fname}: 无变化")
        return False

    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(out)
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    print(f"✓ {fname}: 已更新（{n_before} → {len(lines)} 行）")
    return True


changed = 0
for fname, spec in SPECS.items():
    if apply_one(fname, spec):
        changed += 1
print(f"—— 共更新 {changed} 个文件 ——")
