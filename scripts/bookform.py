#!/usr/bin/env python3
"""bookform.py — 抽「本书形态」，并做单章机器层体检。

用法：
  python3 scripts/bookform.py "<书目录>" [--json]              # 只看形态
  python3 scripts/bookform.py "<章 md>" [--json]               # 形态 + 单章体检
  python3 scripts/bookform.py "<书目录>" --chapter "<章 md>"    # 同上（显式）

「形态」= 这本书自己已经写出来的样子：H1 写法 / 导航项 / 每章块数 / 子项集。
**不是全库标准**——偏离本书众数不算错，但要在判定表里写一行理由。
（实况：2026-09 那批是「4 子项 + 无 ### 块头」，2026-10 那批是「5 子项 + ### 第N处」；
  拿一个全局模板去比，两端都会全红。）

单章体检做四件事（对应审查表 R2，全部从 text/ 重建，不读 md 的结构）：
  1. 引语逐字：每段 `原句` 按 … 拆段，逐段独立在 text/chNN*.txt 里找
     （整串比对救不了「拼接」，见 verify_fragments_indep.py 的教训）；
  2. 块结构：子项齐不齐（对照**本书**众数）、有没有空引号 ""、关键词是否成立；
  3. 中文密度：中文理解 / 为什么这样写 的 CJK 字数；
  4. 形态：H1 / 导航项数 / 块数 vs 本书众数。

退出码：0 无阻断；1 有阻断；2 无法判定（缺 md / 缺 text/）。
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

QUOTE_RE = re.compile(r"^>\s*\*\*原句\s*(\d+)\s*[：:]\*\*\s*(.+)$")
NAV_RE = re.compile(r"^\s*(?:[-*]\s+)?\*\*(.+?)\*\*\s*[：:]")
# 2026-10-20 修假绿：真书的子项常写成列表项（`- **中文理解**：…`），
# 原正则只认行首的 `**X**：` ⇒ **整本书的 4 个子项一个都没解析出来**，
# 于是「子项缺 / 中文过薄 / 空引号」三项全部在空集上判 0——**量具没量，报了绿**。
# （fabulous-bodies 实测：bookform 报「子项集 0 项」，而每块实际都有 4 个子项。）
# 现在允许可选的列表标记（`- ` / `* ` / `+ ` / `1. ` / `1) `）。
SUB_RE = re.compile(
    r"^\s*(?:(?:[-*+]|\d+[.)])\s+)?"
    r"(?:\*\*(?P<b>[^*\n]{2,12})\*\*|(?P<p>[\u4e00-\u9fff]{2,6}))\s*[：:]\s*(?P<v>.*)$"
)
H1_RE = re.compile(r"^#\s+(.*\S)\s*$")

# —— 新书基线（2026-10-20 立，用户要求「脚本固定、文档适应脚本」）——
# 问题：`book_form` 的众数取自**已有章**。新书第 1 章时众数为空 ⇒ 子项集、导航项数、
#   块数范围**全部无约束**，chapter.sh 对新书第一页等于不检查。
# 做法：已有章 < 3 时用这份**库内众数**当基线（2026-10-20 全库 3,000 章实测：
#   子项 Top5 = 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 / 句子结构；
#   导航 5 项；H1 = `# NN. 标题` 占 85%）。章数 ≥3 后自动切回本书自己的众数。
MIN_CHAPTERS_FOR_MODAL = 3
DEFAULT_SUBITEMS = ["中文理解", "关键词", "为什么这样写", "读者视角提示", "句子结构"]
DEFAULT_NAV_COUNT = 5
DEFAULT_BLOCK_RANGE = (3, 8)

# —— 体裁 profile（2026-10-20 立，用户拍板「按体裁给结构约束；短篇合集没有总览」）——
# 结构约束的**唯一定义处**是 docs/rules/genre-profiles.json；本文件只读它、不再自带一套。
# 为什么不在代码里写死：文档的体裁表与代码的默认值已经分叉过一次——体裁表写言情 4 子项，
#   而这里的 DEFAULT_SUBITEMS 是 5 项（含「句子结构」，那是非虚构/短篇的第五项），
#   于是言情新书写成 5 项、门禁只说「新书基线，放宽」，体裁表等于死条文。
PROFILE_PATH = Path(__file__).resolve().parents[1] / "docs/rules/genre-profiles.json"
_PROFILES: dict | None = None


def load_profiles() -> dict:
    global _PROFILES
    if _PROFILES is None:
        try:
            _PROFILES = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
        except Exception:
            _PROFILES = {}
    return _PROFILES


def genre_of(book: Path) -> str:
    """体裁 = 书目录的父目录名（novels / mystery-thriller / …）；不在四类下则 _default。"""
    g = book.resolve().parent.name
    return g if g in load_profiles() and not g.startswith("_") else "_default"


def profile_of(book: Path) -> dict:
    return load_profiles().get(genre_of(book), {})

def _sub_drift(prof_subs, optional, modal) -> str | None:
    """子项集偏离判定。optional 里的子项可加可不加，不算偏离。

    实测（2026-10-20，两个根）：novels 237 本里 205 本用 4 子项、32 本加「句子结构」；
    mystery 49 本里 46 / 3。把少数派写成"偏离"会让这 35 本每章都挂一条 ⚠️
    ——告警一多就没人看，等于把真偏离也淹掉。
    """
    req, opt, m = set(prof_subs or []), set(optional or []), set(modal or [])
    if not req:
        return None
    if m == req or (req <= m and (m - req) <= opt):
        return None
    return (f"子项集 {'/'.join(prof_subs)} ≠ 本书 {'/'.join(modal) or '—'}")


DIGITS = re.compile(r"\d+")
TEXTCH_RE = re.compile(r"^ch(\d+)(?![0-9])")

from lib.text import (  # noqa: E402  统一原语，见 scripts/lib/text.py
    CJK, cjk_count, cjk_ratio, norm, split_segments, strip_quotes,
)

def chapter_md_files(book: Path) -> list[Path]:
    return [p for p in sorted(book.glob("ch*.md")) if re.match(r"^ch\d+(?![0-9])", p.name)]


def text_files(book: Path) -> dict[int, list[Path]]:
    d, got = book / "text", {}
    if not d.is_dir():
        return got
    for p in sorted(d.iterdir()):
        m = TEXTCH_RE.match(p.name)
        if m and p.suffix.lower() in (".txt", ".md"):
            got.setdefault(int(m.group(1)), []).append(p)
    return got


def chapter_no(path: Path) -> int | None:
    m = re.match(r"^ch(\d+)(?![0-9])", path.name)
    return int(m.group(1)) if m else None


def parse_md(path: Path) -> dict:
    txt = path.read_text(encoding="utf-8", errors="replace")
    h1, nav, blocks = "", [], []
    in_nav = in_body = False
    cur: dict | None = None
    cur_sub: str | None = None

    for ln in txt.splitlines():
        if not h1:
            m = H1_RE.match(ln)
            if m:
                h1 = m.group(1)
                continue
        if ln.startswith("## "):
            in_nav = "导航" in ln
            in_body = "精读" in ln
            cur, cur_sub = None, None
            continue
        if in_nav:
            m = NAV_RE.match(ln)
            if m:
                nav.append(m.group(1).strip())
            continue
        if not in_body:
            continue
        if ln.startswith("### "):
            cur = {"header": ln[4:].strip(), "quote": None, "quote_no": None, "subs": {}}
            blocks.append(cur)
            cur_sub = None
            continue
        m = QUOTE_RE.match(ln)
        if m:
            if cur is None or cur["quote_no"] is not None:
                cur = {"header": "", "quote": None, "quote_no": None, "subs": {}}
                blocks.append(cur)
            cur["quote_no"] = int(m.group(1))
            cur["quote"] = strip_quotes(m.group(2))
            cur_sub = None
            continue
        if cur is None:
            continue
        if ln.strip() == "---":
            cur, cur_sub = None, None
            continue
        m = SUB_RE.match(ln)
        if m:
            label = (m.group("b") or m.group("p") or "").strip()
            cur_sub = label
            cur["subs"][label] = m.group("v").strip()
            continue
        if cur_sub and ln.strip():
            cur["subs"][cur_sub] += " " + ln.strip()

    return {"path": path, "h1": h1, "nav": nav, "blocks": blocks}


def h1_shape(h1: str) -> str:
    """形态只记「编号前缀」——标题每章不同，不参与分组。"""
    m = re.match(r"^(\d+)([.、:：]?)", h1.strip())
    return "N" + (m.group(2) or "") if m else "无编号"


def kw_problems(kw: str, quote: str, why: str, corpus: str = "") -> list[str]:
    """关键词是否成立：去掉中文注解 → 整串命中引语 → 逐实词命中（容许词形变化）
    → 退而求其次，允许是「为什么这样写」里呼应的语境延伸词（AGENTS 9b）。"""
    en = re.split(r"[（(]", kw)[0].strip().strip(".,;:!?\"'")
    if not en:
        return []
    n = norm(en).lower()
    if n in norm(quote).lower():
        return []
    if corpus and n in norm(corpus).lower():
        return []  # 语境延伸词：歌名/地名/器物名，本章原文里确有
    qw = re.findall(r"[a-z']+", norm(quote).lower())
    words = [w for w in re.findall(r"[a-z']+", norm(en).lower()) if w not in STOPWORDS]
    if not words:
        return [en]  # 整条都是虚词
    missing = []
    for w in words:
        stem = w[:max(4, len(w) - 3)]
        if not any(x.startswith(stem) for x in qw):
            missing.append(w)
    if not missing:
        return []
    if all(w in norm(why).lower() for w in missing):
        return []  # 语境延伸词，在「为什么这样写」里有呼应
    return [f"{en}（缺 {'/'.join(missing)}）"]


def _labels(b: dict) -> tuple:
    return tuple(k for k, v in b["subs"].items() if v.strip())


def book_form(book: Path) -> dict:
    files = chapter_md_files(book)
    h1s, navs, navsets, nblocks, label_sets, total = [], [], [], [], [], 0
    for p in files:
        d = parse_md(p)
        if d["h1"]:
            h1s.append(h1_shape(d["h1"]))
        navs.append(len(d["nav"]))
        navsets.append(tuple(d["nav"]))
        n = sum(1 for b in d["blocks"] if b["quote_no"] is not None)
        nblocks.append(n)
        total += n
        for b in d["blocks"]:
            if b["quote_no"] is not None:
                label_sets.append(_labels(b))
    nav_mode = Counter(navsets).most_common(1)[0][0] if navsets else ()
    label_mode = Counter(label_sets).most_common(1)[0][0] if label_sets else ()
    # 新书（<3 章）没有可信众数 ⇒ 用库内基线，否则第 1 章等于零判据
    _baseline = "book" if len(files) >= MIN_CHAPTERS_FOR_MODAL else "default"
    prof = profile_of(book)
    if _baseline == "default":
        label_mode = tuple(prof.get("subitems") or DEFAULT_SUBITEMS)
        nav_mode = ()                     # 名字不设基线，只设项数（否则会报"缺导航项"假红）
        navs = navs or [prof.get("nav", {}).get("count") or DEFAULT_NAV_COUNT]
        nblocks = nblocks or [(prof.get("blocks") or DEFAULT_BLOCK_RANGE)[0]]
    return {
        "book": str(book),
        "chapters": len(files),
        "h1_forms": dict(Counter(h1s).most_common()),
        "nav_items": list(nav_mode),
        "nav_counts": sorted(set(navs)),
        "nav_sets": {"/".join(k): v for k, v in Counter(navsets).most_common(5)},
        "blocks": total,
        "block_median": statistics.median(nblocks) if nblocks else 0,
        "block_range": ([min(nblocks), max(nblocks)] if _baseline == "book"
                         else list(prof.get("blocks") or DEFAULT_BLOCK_RANGE)) if nblocks else [0, 0],
        "blocks_per_chapter": nblocks,
        "subitems": list(label_mode),
        "subitem_sets": {"/".join(k): v for k, v in Counter(label_sets).most_common(5)},
        "text_files": sum(len(v) for v in text_files(book).values()),
        "baseline": _baseline,
        "profile": genre_of(book),
        "profile_label": prof.get("label", ""),
        "profile_subitems": list(prof.get("subitems") or DEFAULT_SUBITEMS),
        "profile_optional": list(prof.get("optional_subitems") or []),
        "profile_blocks": list(prof.get("blocks") or DEFAULT_BLOCK_RANGE),
        "profile_overview": prof.get("overview", 3),
    }


def find_corpus(book: Path, no: int) -> Path | None:
    c = text_files(book).get(no, [])
    return c[0] if c else None


def check_chapter(book: Path, md: Path, form: dict | None = None) -> dict:
    no = chapter_no(md)
    corpus = find_corpus(book, no) if no else None
    d = parse_md(md)
    form = form or book_form(book)  # 整书模式只算一次众数，否则 O(n²)
    res: dict = {"chapter": no, "md": str(md), "corpus": str(corpus) if corpus else None,
                 "verdict": "ok", "quotes": [], "blocks": [], "form": {}, "counts": {}}
    if no is None:
        res["verdict"] = "undecidable"
        res["reason"] = "文件名不是 chNN 开头，无法定位本章语料"
        return res
    if corpus is None:
        res["verdict"] = "undecidable"
        res["reason"] = f"text/ 下没有 ch{no:02d} 的语料，无法判定（不是通过）"
        return res

    corpus_n = norm(corpus.read_text(encoding="utf-8", errors="replace"))
    miss = 0
    for b in d["blocks"]:
        if b["quote_no"] is None:
            continue
        rec = {"block": b["header"] or f"原句{b['quote_no']}", "no": b["quote_no"], "segments": []}
        for seg in split_segments(b["quote"]):
            ok = norm(seg) in corpus_n
            rec["segments"].append({"text": seg[:120], "ok": ok, "pos": corpus_n.find(norm(seg))})
            miss += 0 if ok else 1
        res["quotes"].append(rec)

    struct_bad, empty_quote, kw_bad, cjk_bad = [], [], [], []
    modal = set(form["subitems"])
    for b in d["blocks"]:
        if b["quote_no"] is None:
            continue
        name = b["header"] or f"原句{b['quote_no']}"
        missing = sorted(modal - set(_labels(b)))
        if missing:
            struct_bad.append({"block": name, "missing": missing})
        if not (b["quote"] or "").strip():
            empty_quote.append(name)
        for k, v in b["subs"].items():
            if re.search(r'""|“”', v):
                empty_quote.append(f"{name}/{k}（分析里残留空引号）")
        kws = [w.strip() for w in re.split(r"[/、,，;；]", b["subs"].get("关键词", "")) if w.strip()]
        why = b["subs"].get("为什么这样写", "")
        bad_kw = []
        for k in kws:
            bad_kw.extend(kw_problems(k, b["quote"], why, corpus_n))
        if bad_kw:
            kw_bad.append({"block": name, "bad": bad_kw})
        for k, floor, ratio in (("中文理解", 6, 0.0), ("为什么这样写", 8, 0.15)):
            v = b["subs"].get(k, "")
            if not v.strip():
                continue
            if cjk_count(v) < floor or (ratio and cjk_ratio(v) < ratio):
                cjk_bad.append({"block": name, "field": k,
                                "cjk": cjk_count(v), "ratio": round(cjk_ratio(v), 2)})
        res["blocks"].append({"block": name,
                              "cjk": {k: cjk_count(v) for k, v in b["subs"].items()},
                              "cjk_ratio": {k: round(cjk_ratio(v), 2) for k, v in b["subs"].items()}})

    nav_n = len(d["nav"])
    res["form"] = {
        "h1": d["h1"],
        "h1_shape_ok": h1_shape(d["h1"]) in form["h1_forms"] if d["h1"] else False,
        "nav_count": nav_n, "nav_count_ok": nav_n in form["nav_counts"],
        "nav_counts": form["nav_counts"],
        "nav_missing": [x for x in form["nav_items"] if x not in d["nav"]],
        "subitems_modal": form["subitems"],
        "blocks": sum(1 for b in d["blocks"] if b["quote_no"] is not None),
        "block_median": form["block_median"], "block_range": form["block_range"],
        "profile": form.get("profile", ""),
        "profile_subitems": form.get("profile_subitems", []),
        "profile_optional": form.get("profile_optional", []),
        "baseline": form.get("baseline", "book"),
    }
    res["counts"] = {"blocks": len(res["quotes"]),
                     "segments": sum(len(q["segments"]) for q in res["quotes"]),
                     "segment_miss": miss, "struct_bad": len(struct_bad),
                     "empty_quote": len(empty_quote), "keyword_bad": len(kw_bad),
                     "cjk_low": len(cjk_bad)}
    res["issues"] = {"struct": struct_bad, "empty_quote": empty_quote,
                     "keyword": kw_bad, "cjk": cjk_bad}
    blocked = miss or struct_bad or empty_quote or kw_bad or cjk_bad
    res["verdict"] = "blocked" if blocked else "ok"
    return res


def print_form(f: dict) -> None:
    print(f"本书形态：{f['book']}")
    print(f"  已有章 md：{f['chapters']}    text/ 提取件：{f['text_files']}    引语块合计：{f['blocks']}")
    print(f"  H1 写法：{f['h1_forms']}")
    print(f"  导航项（众数，{len(f['nav_items'])} 项）：{' / '.join(f['nav_items']) or '—'}"
          + ("  ← 新书基线只约束**项数 5**，不约束项名" if f.get("baseline") == "default" else ""))
    print(f"  子项集（众数，{len(f['subitems'])} 项）：{' / '.join(f['subitems']) or '—'}")
    print(f"  每章块数：中位 {f['block_median']}，范围 {f['block_range'][0]}–{f['block_range'][1]}"
          + ("   （⚠️ 已有章 <3，用的是**体裁 profile 基线**）"
             if f.get("baseline") == "default" else ""))
    prof_subs = f.get("profile_subitems") or []
    prof_blocks = f.get("profile_blocks") or [0, 0]
    print(f"  体裁 profile：{f.get('profile', '_default')}（{f.get('profile_label', '')}）"
          f"｜子项 {len(prof_subs)} 项｜块数 {prof_blocks[0]}–{prof_blocks[1]}｜总览 {f.get('profile_overview', 3)} 篇")
    drift = []
    sub_d = _sub_drift(prof_subs, f.get("profile_optional"), f["subitems"])
    if sub_d:
        drift.append(sub_d)
    # 块数只在**新书**（还没有自己的中位）时按 profile 提示；
    # 已有书按 2026-10-18 拍板的「同书自校准」——中位 15 是这本书的体裁使然，不是缺陷。
    if f.get("baseline") == "default" and prof_blocks[1] and \
            not (prof_blocks[0] <= (f["block_median"] or 0) <= prof_blocks[1]):
        drift.append(f"块数中位 {f['block_median']} 出 {prof_blocks[0]}–{prof_blocks[1]}")
    if drift:
        print("  ⚠️ 与体裁 profile 不同：" + "；".join(drift) + "——**不算错**，在判定表写一行理由。")
    print("  ⚠️ 形态偏离本书众数不算错，写一行理由即可。")


def print_check(r: dict) -> None:
    print(f"单章体检：ch{r['chapter']:02d}  {Path(r['md']).name}")
    if r["verdict"] == "undecidable":
        print(f"  ❓ {r['reason']}")
        return
    c = r["counts"]
    print(f"  语料：{r['corpus']}")
    print("\n【逐字】")
    print(f"  引语块 {c['blocks']}，片段 {c['segments']}，查无 {c['segment_miss']}")
    for q in r["quotes"]:
        for s in q["segments"]:
            if not s["ok"]:
                print(f"    ❌ {q['block']}：{s['text']}")
    print("\n【对应】")
    print(f"  空引号 {c['empty_quote']}｜子项缺 {c['struct_bad']}｜关键词不成立 {c['keyword_bad']}｜中文过薄 {c['cjk_low']}")
    for e in r["issues"]["struct"]:
        print(f"    ❌ 子项缺：{e['block']} → {e['missing']}")
    for e in r["issues"]["empty_quote"]:
        print(f"    ❌ 空引号：{e}")
    for e in r["issues"]["keyword"]:
        print(f"    ❌ 关键词：{e['block']} → {e['bad']}")
    for e in r["issues"]["cjk"]:
        print(f"    ❌ 中文过薄：{e['block']} / {e['field']} 仅 {e['cjk']} 字（中文占比 {e['ratio']:.0%}）")
    print("\n【形态】")
    f = r["form"]
    print(f"  H1 {'✅' if f['h1_shape_ok'] else '⚠️ 与本书众数不同'}：{f['h1']}")
    print(f"  导航 {f['nav_count']} 项 {'✅' if f['nav_count_ok'] else '⚠️ 本书常见 ' + str(f['nav_counts'])}")
    if f["nav_missing"]:
        print(f"    缺：{f['nav_missing']}")
    print(f"  块数 {f['blocks']}（本书中位 {f['block_median']}，范围 {f['block_range'][0]}–{f['block_range'][1]}）")
    prof_subs = f.get("profile_subitems") or []
    if _sub_drift(prof_subs, f.get("profile_optional"), f.get("subitems_modal") or []):
        print(f"  ⚠️ 体裁 profile（{f.get('profile')}）的子项是 {'/'.join(prof_subs)}，"
              f"本书是 {'/'.join(f.get('subitems_modal') or []) or '—'}——**不算错**，判定表写一行理由")
    print("\n【断言】")
    print("  ❓ 机器不判「谁做的/什么关系/死因/数字」——留给 R1 素读 + R3 对账。")
    print(f"\n结论：{'❌ 有阻断' if r['verdict'] == 'blocked' else '✅ 机器层无阻断'}（档位四选一见审查表）")


def check_all(book: Path, as_json: bool = False) -> int:
    """整书体检：每章跑**与 `chapter.sh` 完全相同**的 check_chapter。

    为什么要它（2026-10-20）：单章入口 `chapter.sh` 与整书入口 `gate.sh` 原本是两套判据，
    单章查得出的缺陷整书可能查不出，反之亦然。这里让整书复用同一实现。

    ⚠️ **只报其他 lane 不查的维度**（空引号 / H1 形态 / 导航项数 / 块数越界）。
    引语逐字、子项缺、关键词、中文密度由 ①⑤⑥⑦⑩⑪⑫⑬⑲ 覆盖，本 lane **不重复报**
    ——否则同一处缺陷被数两遍，正门计数虚高（2026-10-02 以来反复踩的坑）。
    """
    mds = chapter_md_files(book)
    if not mds:
        print(f"  （{book.name} 下没有 chNN 章 md，本 lane 跳过）")
        return 0
    form = book_form(book)                 # 只算一次众数
    rows = [check_chapter(book, md, form) for md in mds]

    empty_ch, form_ch, und = [], [], []
    for r in rows:
        no = r["chapter"]
        if r["verdict"] == "undecidable":
            und.append(r)
            continue
        n_empty = len(r["issues"]["empty_quote"])
        if n_empty:
            empty_ch.append((no, n_empty))
        f = r["form"]
        dev = []
        if not f["h1_shape_ok"]:
            dev.append(f"H1「{f['h1']}」与本书众数不同")
        if not f["nav_count_ok"]:
            dev.append(f"导航 {f['nav_count']} 项（本书常见 {f['nav_counts']}）")
        if not (f["block_range"][0] <= f["blocks"] <= f["block_range"][1]):
            dev.append(f"块数 {f['blocks']} 越出本书范围 {f['block_range'][0]}–{f['block_range'][1]}")
        if dev:
            form_ch.append((no, dev))

    # 总览篇数按体裁 profile 核（**只报不判红**：在制书本来就没写总览）
    prof = profile_of(book)
    want_ov = prof.get("overview", 3)
    have_ov = len(list(book.glob("00_*.md")))
    if want_ov and have_ov < want_ov:
        ov_msg = (f"总览 {have_ov}/{want_ov} 篇——完工前必须补齐" if have_ov
                  else f"总览三篇未做（本体裁要求 {want_ov} 篇，完工前必须）")
    elif not want_ov and have_ov:
        ov_msg = f"本体裁 profile 不要求总览（短篇合集），本书已做 {have_ov} 篇——不判错"
    else:
        ov_msg = ""

    if as_json:
        print(json.dumps({"book": str(book), "chapters": len(rows),
                          "empty_quote": [{"ch": n, "n": k} for n, k in empty_ch],
                          "form_deviation": [{"ch": n, "dev": d} for n, d in form_ch],
                          "undecidable": [{"ch": r["chapter"], "reason": r["reason"]} for r in und],
                          "overview": ov_msg, "profile": genre_of(book)},
                         ensure_ascii=False, indent=2))
    else:
        print(f"  整书体检 {len(rows)} 章（与 `chapter.sh` 同一实现；只报其他 lane 不查的维度）")
        for no, k in empty_ch:
            print(f"  ❌ ch{no:02d}：分析层残留空引号 {k} 处（删英文引语没删引号，写成 `\"\"`）")
        for no, dev in form_ch:
            print(f"  ❌ ch{no:02d}：" + "；".join(dev))
        for r in und:
            print(f"  ❓ ch{r['chapter']:02d}：{r['reason']}")
        if ov_msg:
            print(f"  ℹ️ {ov_msg}")
        print(f"  汇总：空引号 {len(empty_ch)} 章 ｜ 形态偏离 {len(form_ch)} 章 ｜ 无法判定 {len(und)} 章"
              f"（引语/子项/关键词/中文密度另有 lane，本项不重复计）")
    bad = bool(empty_ch or form_ch)
    return 1 if bad else (2 if und else 0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--chapter", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--all", action="store_true", help="整书体检（每章都跑，判据同单章）")
    a = ap.parse_args()

    t = Path(a.target).expanduser().resolve()
    if a.chapter:
        md = Path(a.chapter).expanduser().resolve()
        book = t if t.is_dir() else md.parent
    elif t.is_file():
        md, book = t, t.parent
    else:
        md, book = None, t

    if md is None and a.all:
        return check_all(book, a.json)

    if md is None:
        f = book_form(book)
        if a.json:
            print(json.dumps(f, ensure_ascii=False, indent=2))
        else:
            print_form(f)
        return 0

    if not md.is_file():
        print(f"❌ 章 md 不存在：{md}", file=sys.stderr)
        return 2
    r = check_chapter(book, md)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print_check(r)
    return 0 if r["verdict"] == "ok" else (2 if r["verdict"] == "undecidable" else 1)


if __name__ == "__main__":
    sys.exit(main())
