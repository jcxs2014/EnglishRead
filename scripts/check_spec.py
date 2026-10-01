#!/usr/bin/env python3
"""check_spec.py — mkchapter.py 的 spec JSON 预检器（并可自动补一处低级失误）。

为什么需要（2026-10-01 The Death of Us 实测连踩三次）
------------------------------------------------------
我自己手写喂给 `mkchapter.py` 的 spec JSON **反复漏掉 `nav` 数组的闭合方括号**，
而 `mkchapter.py` 直接 `json.loads` 后抛 JSONDecodeError —— **不生成文件、也不产出
任何可读报错**，看上去像工具坏了（ch08/ch10/ch11 三次，每次多花两轮）。

本脚本做四件事，任一不满足即退出码 2：
  1. `json.loads` 成功；失败且文件以 `"\n}` 结尾（典型的漏 `]`）⇒ 自动补 `  ]`；
  2. 必备字段齐全：book / ch / h1 / nav / summary / quotes / blocks；
  3. nav 恰好 5 项、quotes 与 blocks 条数相等且 ≥3；
  4. **同段引语检查**（2026-10-01 ch44 实测缺陷新增）：多个 `@前缀` 落在本章
     `text/` 的**同一个自然段**内 ⇒ `inject_by_para` 会取出重叠的引语，导致
     `check_chapter_quotes` 报「md 块 N / 工具抽到 M」+ `audit_structure` 结构缺陷。
     门禁能抓到，但那时 md 已生成、spec 已写过，白费一轮；这里前置拦。
  5. **跨说话轮次检查**（2026-10-01 ch45/ch51/ch53 连续五次实测新增）：前缀里在
     **非末尾**出现 `,” ` / `.” ` / `?” ` ⇒ 前缀闭合了引号又继续，即把「X，」她说。
     「Y。」两句连成一条引语，违反 AGENTS 禁令 5。注入器会拒收，但那时
     quotes/blocks/中文理解都已写完；而这个失误的成因是我写中文理解时习惯把一段
     对话当成流畅字符串，所以必须在写之前拦。正确写法见下方 `prefix_hint`。

用法:
  python3 scripts/check_spec.py <spec.json> [...]
  python3 scripts/check_spec.py --patch <patch.py> <spec.json> [...]
      --patch 传入的 .py 文件在**已解析对象 d 上** exec（可一次性补 quotes/blocks/
      summary 等长字段，避免再手写一遍 JSON 字符串）
"""
import json
import re
import sys
from pathlib import Path

REQUIRED = {"book", "ch", "h1", "nav", "summary", "quotes", "blocks"}

# quotes 串里每个 `Qn=@前缀[*]` 的前缀与是否整段
_QRE = re.compile(r"Q\d+\s*=\s*@(.+?)(\*?)(?=\s*(?:;|$))")


def find_text(book: str, ch: str) -> Path | None:
    """按 ch 号定位该章的 text/ 提取件（取唯一命中者）。"""
    d = Path(book) / "text"
    if not d.is_dir():
        return None
    pat = f"ch{int(ch):02d}_*.txt"
    hits = sorted(d.glob(pat))
    return hits[0] if hits else None


def same_paragraph_problems(book: str, ch: str, quotes: str) -> list[str]:
    """若两个以上引语前缀**落在**同一自然段内 ⇒ 报阻断。

    注意判定必须用「段内包含」而非「段首匹配」：ch44 实测三个前缀都在同一段的
    中间位置（段首是别的句子），只查 startswith 会漏放（回归已验证）。
    前缀过短（<20 字符）易在多段重复出现，故不参与判定。
    """
    txt = find_text(book, ch)
    if txt is None:
        return []
    paras = [" ".join(x.split()) for x in
             txt.read_text(encoding="utf-8").split("\n\n") if x.strip()]
    where: dict[int, list[str]] = {}
    seq = re.finditer(r"(Q\d+)\s*=\s*@(.+?)(\*?)(?=\s*(?:;|$))", quotes)
    for m in seq:
        label, prefix = m.group(1), " ".join(m.group(2).split())
        if len(prefix) < 20:
            continue
        hits = [i for i, para in enumerate(paras) if prefix in para]
        if len(hits) > 1:
            return [f"前缀 {label} 在本章 {len(hits)} 段均命中（前缀过短或歧义）："
                    f"{prefix[:30]}…"]
        if hits:
            where.setdefault(hits[0], []).append(label)
    return [f"同一自然段多引语（段 {i}）：{'、'.join(v)}——须合并为一条或换段"
            for i, v in sorted(where.items()) if len(v) > 1]


def cross_turn_problems(quotes: str) -> list[str]:
    """前缀在非末尾出现闭合引号 ⇒ 跨说话轮次（禁令 5）的**可判定子集**。

    注意这只覆盖「把引号和 said 一起写进前缀」的情况；更常见的手写失误是
    **直接把 said 标签省掉再把两句台词连写**（ch45/ch51/ch53 连续五次），
    那种前缀里根本没有闭合引号，规则查不出来——它由下面的 `prefix_match_problems`
    兜住（这种前缀不是任何一段的逐字子串）。两条规则互补，都留在 check 里。
    """
    bad = []
    for m in re.finditer(r"(Q\d+)\s*=\s*@(.+?)(\*?)(?=\s*(?:;|$))", quotes):
        label, pre = m.group(1), m.group(2)
        for cl in (',” ', '.” ', '?” ', '!” '):
            i = pre.find(cl)
            while i != -1:
                if i + len(cl) < len(pre.rstrip()):
                    bad.append(f"{label} 跨说话轮次（第 {i + 1} 字出现 {cl.strip()!r}）"
                               f"——应改用 prefix_hint 的写法")
                    break
                i = pre.find(cl, i + 1)
    return bad


def prefix_match_problems(book: str, ch: str, quotes: str) -> list[str]:
    """每个前缀必须在本章 text/ 中**恰好命中一段**。

    这是「跨说话轮次连写」与「引语内掉词/换词」两类手打失误的总闸：
    前者把 said 标签省掉再连写、后者漏掉 `wouldn’t’ve` 里的 ’ve，
    结果都是前缀不是任何一段的逐字子串。`inject_by_para` 本身会拒收，
    但那已在写完 blocks 与中文理解之后；这里前置到 spec 阶段。
    """
    txt = find_text(book, ch)
    if txt is None:
        return []
    paras = [" ".join(x.split()) for x in
             txt.read_text(encoding="utf-8").split("\n\n") if x.strip()]
    bad = []
    for m in re.finditer(r"(Q\d+)\s*=\s*@(.+?)(\*?)(?=\s*(?:;|$))", quotes):
        label, pre = m.group(1), " ".join(m.group(2).split())
        if len(pre) < 4:
            continue
        hits = [i for i, p in enumerate(paras) if pre in p]
        if not hits:
            bad.append(f"{label} 前缀在本章 0 段命中（多半是把 said 标签省掉后连写，"
                       f"或引语内掉词/换词）：{pre[:34]}…")
        elif len(hits) > 1:
            bad.append(f"{label} 前缀在本章 {len(hits)} 段命中（前缀过短或歧义）："
                       f"{pre[:34]}…")
    return bad


def prefix_hint(book: str, ch: str, index: int) -> str | None:
    """给出该章第 index 段的**安全前缀**（对话段取首个说话轮次 + `*`）。

    这是治「跨说话轮次」的正法：锚在第一个引号内（或段首），加 `*` 取整段，
    于是整段（含 she said 与叙述）逐字连续，不需要把两句台词手工拼起来。
    """
    txt = find_text(book, ch)
    if txt is None:
        return None
    paras = [" ".join(x.split()) for x in
             txt.read_text(encoding="utf-8").split("\n\n") if x.strip()]
    if not (0 <= index < len(paras)):
        return None
    p = paras[index]
    if p.startswith("“") or p.startswith('"'):
        end = min([x for x in (p.find("” ", 1), p.find('" ', 1)) if x != -1],
                  default=-1)
        if end != -1:
            return p[1:end] + "*"
    return p[:40] + "*"


def load(path: Path) -> dict:
    s = path.read_text(encoding="utf-8")
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        stripped = s.rstrip()
        if stripped.endswith('"\n}') or stripped.endswith('"}'):
            fixed = stripped[:-1].rstrip() + "\n  ]\n}\n"
            try:
                d = json.loads(fixed)
            except json.JSONDecodeError as e2:
                print(f"❌ {path.name}: 补 ] 后仍解析失败: {e2}")
                sys.exit(2)
            path.write_text(fixed, encoding="utf-8")
            print(f"🔧 {path.name}: 已补 nav 数组闭合方括号")
            return d
        print(f"❌ {path.name}: 解析失败且不像漏 ]（需人工看）")
        sys.exit(2)


def main():
    args = sys.argv[1:]
    patch = None
    if args and args[0] == "--patch":
        patch = Path(args[1]).read_text(encoding="utf-8")   # 传的是**文件**
        args = args[2:]
    rc = 0
    for a in args:
        p = Path(a)
        d = load(p)
        if patch is not None:
            exec(patch, {"d": d, "json": json, "Path": Path})
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        keys = set(d.keys())
        nq = len([x for x in d.get("quotes", "").split(";") if x.strip()])
        nb = len([x for x in d.get("blocks", "").split(";") if x.strip()])
        problems = []
        if not REQUIRED <= keys:
            problems.append(f"缺字段 {sorted(REQUIRED - keys)}")
        if len(d.get("nav", [])) != 5:
            problems.append(f"nav {len(d.get('nav', []))} 项（须 5）")
        if nq != nb:
            problems.append(f"quotes {nq} 条 ≠ blocks {nb} 条")
        if nq < 3:
            problems.append(f"quotes 仅 {nq} 条（精简档配额 3–8）")
        problems.extend(same_paragraph_problems(
            d.get("book", ""), d.get("ch", ""), d.get("quotes", "")))
        problems.extend(cross_turn_problems(d.get("quotes", "")))
        problems.extend(prefix_match_problems(
            d.get("book", ""), d.get("ch", ""), d.get("quotes", "")))
        flag = "✅" if not problems else "❌"
        print(f"{flag} {p.name}: nav={len(d.get('nav', []))} quotes={nq} blocks={nb}"
              + ("　｜ " + "；".join(problems) if problems else ""))
        if problems:
            rc = 2
    sys.exit(rc)


if __name__ == "__main__":
    main()