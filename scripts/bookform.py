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
DEFAULT_NAV_ITEMS = ["一句话概括", "情感弧线位置", "人物弧线", "叙事手法"]  # 仅 profile 未给项名时兜底
# 引语长度：**只提示、不进退出码**。判据出处 = 创建卡 §3 硬线（1–3 句 / 30–70 词 / ≤4 行）。
# 为什么必须有提示（2026-10-21 don-t-leave 整本返工）：那一版引语中位 168 词、72% 超 100 词，
# 而 19 个 lane 全绿——长度这一层当时**没有任何探针**，只能靠人读到第 40 页才发现。
LONG_QUOTE_WORDS = 100

# 2026-10-21 用户拍板：块数不可「随意决定」——
#   新书：下限 2、上限 15 是**硬判据**（超上限判阻断，不判提示）；
#   已有 ≥3 章的书：上限取 max(15, 本书最高章)（2026-10-24 定案，见 blocks 判据处注释）；
#   中间按本章原文字数给建议区间：800 词 2 块就够，2000 词 4–6 块。
# 上限来历：ebenezer-scrooge ch03（1,731 词）被写到 11 块，用户嫌「读起来费劲」；
# 2026-10-21 先定 10，同日改为 **15**（用户：「那把上限改到 15 吧」）。
# 全库常规密度 2.5–3 块/千词。
MIN_BLOCKS = 2
MAX_BLOCKS = 15


def blocks_target(words: int) -> tuple:
    """按本章原文词数给出建议块数区间（两端都已夹到 2–15）。"""
    lo = max(MIN_BLOCKS, round(words / 550))
    hi = min(MAX_BLOCKS, max(lo, round(words / 320)))
    return lo, hi

# 模板套话：分析字段里出现这些串 = 「写了但没写」（2026-10-21 ebenezer-scrooge 实证：
# beam-free 模型 33 分钟写 40 章，中文理解抄英文原文、为什么这样写套「把 X 重新定义 as Y, not Z」696 次）。
# 判据是**退化特征**不是文风偏好：这些串只在模板循环产出里成片出现，正常精读里几乎不可能出现。
TEMPLATE_PATTERNS = (
    "重新定义 as",
    "本句描写了场景与人物的反应",
    "此句通过修辞与节奏把人物的内心状态外化",
    "把场景重新定义为",
    "为后续情节的转折埋下伏笔，保证",
)
REPEAT_SENTENCE_MIN = 3      # 同一字段里同一句重复 ≥3 次 → 模板循环
KEYWORD_MAX_WORDS = 8        # 单个关键词超过 8 个词 = 整句照抄（提示型）

# 残句（缺词）：`的` 后面直接跟动词/连词，说明「的」与宾语之间那个词被删掉了。
# 2026-10-21 finding-darla 实证：`把 吉隆坡 的 写成 南迪妮 的日常`、`把 新冠疫情 的 写成 失去（ + 祖母）`、
# `"祖母"的 词与并列` —— 修复方把 `""` 填了字，句子仍然读不通，而 check_chinese_layer 只数汉字，
# 于是门禁全绿。全库 551 本实测：本模式只命中该书 119 处 / 21 章，健康书 0 处。
HOLE_RE = re.compile(r"的[ \u3000]{1,}(写成|是|与|让|把|等|而非|成为|被|却|对|在|有|没|不|用)")

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


def has_empty_quote_span(text: str) -> bool:
    """真正为空的引号区（""/“”）才算残留空引号。

    旧判据 `re.search(r'""|“”', v)` 会把**相邻对白**（`"又一枚耳环。""像前几天的那枚？"`）
    误判为空引号 —— 实测本书 5 章 10 处报警全是这一形态，属假红。
    现在改为逐个引号区解析，只在区间内容确实为空时报警。
    """
    for m in re.finditer(r'"([^"]*)"|“([^”]*)”', text or ""):
        inner = m.group(1) if m.group(1) is not None else m.group(2)
        if not inner.strip():
            return True
    return False

from lib.chapters import chapter_files, chapter_no as _lib_chapter_no
from lib.text import (  # noqa: E402  统一原语，见 scripts/lib/text.py
    CJK, STOPWORDS, cjk_count, cjk_ratio, norm, split_segments, strip_quotes,
)

def chapter_md_files(book: Path) -> list[Path]:
    # 兼容 `chNN …` 与 `NN 标题.md` 两套命名（见 scripts/lib/chapters.py）
    return chapter_files(book)


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
    # 兼容 `chNN …` 与 `NN 标题.md`（旧格式 29 本）
    m = re.match(r"^(?:ch)?(\d{1,3})(?![0-9])", path.name, re.I)
    return int(m.group(1)) if m else None


def parse_md(path: Path) -> dict:
    txt = path.read_text(encoding="utf-8", errors="replace")
    h1, nav, blocks = "", [], []
    lines = txt.splitlines()
    # 有书没有「## 精读」节，块直接挂在顶层。此前一律要求「精读」字样在标题里，
    # 这类书会解析出 **0 块** 而报告写「块数 0 低于下限」——理由错，修法也错
    # （2026-10-24 复核发现 6 本：bruja-s-nest / under-the-same-stars / sweet-fury /
    #   armor-for-liars / star-circle / the-ancient-things）。
    has_body_sec = any(ln.startswith("## ") and "精读" in ln for ln in lines)
    in_nav = False
    in_body = not has_body_sec          # 无显式精读节 ⇒ 全文都按正文收
    cur: dict | None = None
    cur_sub: str | None = None

    for ln in lines:
        if not h1:
            m = H1_RE.match(ln)
            if m:
                h1 = m.group(1)
                continue
        if ln.startswith("## "):
            in_nav = "导航" in ln
            in_body = True if not has_body_sec else ("精读" in ln)
            cur, cur_sub = None, None
            continue
        if in_nav:
            m = NAV_RE.match(ln)
            if m:
                nav.append(m.group(1).strip())
            if has_body_sec:
                continue
            # 没有独立的「精读」节时，块常直接排在「本章导航」之后 ⇒ 不能整段跳过。
            # 导航行本身不会误收：此时 cur 还是 None，下面的正文解析会忽略它们。
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
            # 分隔线也结束导航区，否则后面所有 `**字段**：` 都会被数成导航项
            cur, cur_sub, in_nav = None, None, False
            continue
        m = SUB_RE.match(ln)
        if m:
            label = (m.group("b") or m.group("p") or "").strip()
            cur_sub = label
            cur["subs"][label] = m.group("v").strip()
            continue
        if cur_sub and ln.strip():
            cur["subs"][cur_sub] += " " + ln.strip()

    # 一致性自检：原文里明明有「原句 N」行，却一个块都没解析出来 ⇒ 解析盲区。
    # 用**宽松**模式数「原句行」：块头写法坏了（如 `> 原句 1：`）也算，
    # 否则盲区自检和解析器用的是同一个正则，一起瞎。
    RAW_QUOTE_RE = re.compile(r"^\s*>\s*\**\s*原句\s*\d+")
    raw_quote_lines = sum(1 for ln in lines if RAW_QUOTE_RE.match(ln))
    blind = raw_quote_lines if (raw_quote_lines and not blocks) else 0
    return {"path": path, "h1": h1, "nav": nav, "blocks": blocks, "blind": blind}


def h1_shape(h1: str) -> str:
    """形态只记「编号前缀」——标题每章不同，不参与分组。"""
    m = re.match(r"^(\d+)([.、:：]?)", h1.strip())
    return "N" + (m.group(2) or "") if m else "无编号"



def split_keywords(kw: str) -> list[str]:
    """按 `/ 、 , ；` 切分关键词，但**括号内的分隔符不切**，并丢掉纯中文注解残片。

    2026-10-21 实证（finding-darla ch03 / nine-perfect-strangers ch26）：
    `paati（祖母，Tamil）` 被切成 `paati（祖母` + `Tamil）`，后半段变成「关键词不成立」——
    这是**工具假红**，不是内容缺陷；全库 2,232 个文件、5,874 处注解都带这种括号分隔符。
    """
    out, buf, depth = [], [], 0
    for ch in kw:
        if ch in "（(":
            depth += 1
        elif ch in "）)":
            depth = max(0, depth - 1)
        if depth == 0 and ch in "/、,，;；":
            out.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    out.append("".join(buf))
    items = [w.strip() for w in out if w.strip()]
    latin = [w for w in items if re.search(r"[A-Za-z]", w)]
    return latin or items   # 全是中文时原样返回，交给 kw_problems 报出来（不静默放行）

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


_BOOK_BLOCKS_CACHE: dict = {}


def book_block_stats(book: Path, exclude: Path) -> list[int]:
    """同书其他章的引语块数（不含本章）。用于「同书自校准」判块数。

    缓存键含每个文件的 mtime，任一章改动即重算——否则跑完整书期间新写的章
    会沿用旧分布（2026-10-24 加书基线时一并处理）。
    """
    files = sorted(p for p in book.glob("*.md") if p.name != exclude.name)
    sig = tuple((str(p), p.stat().st_mtime_ns) for p in files)
    hit = _BOOK_BLOCKS_CACHE.get(str(book))
    if hit and hit[0] == sig:
        return hit[1]
    counts = []
    for p in files:
        try:
            d = parse_md(p)
        except Exception:
            continue
        n = sum(1 for b in d["blocks"] if b["quote_no"] is not None)
        if n:
            counts.append(n)
    _BOOK_BLOCKS_CACHE[str(book)] = (sig, counts)
    return counts


def check_chapter(book: Path, md: Path, form: dict | None = None) -> dict:
    no = chapter_no(md)
    # ⚠️ 不能写 `if no` —— ch00 的 no == 0 是合法章号，falsy 判断会把序章语料丢掉，
    # 结果 ch00 被判「无法判定」（假红）。2026-10-20 审查 don-t-leave-her-alone 时修。
    corpus = find_corpus(book, no) if no is not None else None
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
    # ⚠️ 2026-10-21：本项**必须大小写不敏感**。
    # 本库其余全部引语门禁（verify_quotes.flat_alpha / quotecheck.chapter.flat_with_bounds /
    # overviewcheck.full.flat_alpha）都走 `.lower()` 口径；只有本文件原先是大小写敏感，
    # 于是「原文句首大写、md 写成小写」被判「查无」——假红。
    # 实测全库 47 本书、217 段属这一形态（本书 ch06/ch10 各 1 段）。
    # 判据依据：AGENTS 第 2 条「引文逐字」的排版差异豁免口径（弯/直引号、句末标点、
    # 大小写均视为正常，见第 9 条 d2 对「大小写改写是本库普遍做法」的认定）。
    corpus_lc = corpus_n.lower()
    miss = 0
    for b in d["blocks"]:
        if b["quote_no"] is None:
            continue
        rec = {"block": b["header"] or f"原句{b['quote_no']}", "no": b["quote_no"], "segments": [],
               "words": len((b["quote"] or "").split())}
        for seg in split_segments(b["quote"]):
            ns = norm(seg)
            ok = ns.lower() in corpus_lc
            rec["segments"].append({"text": seg[:120], "ok": ok, "pos": corpus_lc.find(ns.lower())})
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
            if has_empty_quote_span(v):
                empty_quote.append(f"{name}/{k}（分析里残留空引号）")
        kws = split_keywords(b["subs"].get("关键词", ""))
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

    tpl_bad, kw_long, hole_bad = [], [], []
    for b in d["blocks"]:
        if b["quote_no"] is None:
            continue
        name = b["header"] or f"原句{b['quote_no']}"
        for k, v in b["subs"].items():
            for pat in TEMPLATE_PATTERNS:
                if pat in v:
                    tpl_bad.append({"block": name, "field": k, "pattern": pat})
            for m in HOLE_RE.finditer(v):
                hole_bad.append({"block": name, "field": k, "frag": v[max(0, m.start() - 12):m.end() + 10]})
            sents = [x.strip() for x in re.split(r"[。！？]", v) if len(x.strip()) >= 12]
            if sents:
                top = max(set(sents), key=sents.count)
                if sents.count(top) >= REPEAT_SENTENCE_MIN:
                    tpl_bad.append({"block": name, "field": k,
                                    "pattern": f"同一句重复 {sents.count(top)} 次"})
        for k in split_keywords(b["subs"].get("关键词", "")):
            if len(k.split()) > KEYWORD_MAX_WORDS:
                kw_long.append({"block": name, "kw": k[:60], "words": len(k.split())})

    # ── 块数判据（2026-10-24 定案，用户选 (a)）：
    #    有 ≥3 章基线的书 → 按本书自己的分布判（上限 = max(15, 本书最高章)）；
    #    无基线的新书 → 2–15 硬门（这才是「新书不许随意堆块」的落点）。
    #    理由：同书自校准管「跟着本书走」，2–15 管「新书别堆」，两者管的不是同一批书。
    n_blocks = sum(1 for b in d["blocks"] if b["quote_no"] is not None)
    words = len(corpus_n.split())
    lo, hi = blocks_target(words)
    sib = book_block_stats(book, md)
    bcount_bad: list = []
    bcount_hint = ""
    if len(sib) >= 3:
        med = sorted(sib)[len(sib) // 2]
        top = max(sib)
        hi_eff = max(MAX_BLOCKS, top)
        basis = f"本书 {len(sib)} 章中位 {med:g}、最高 {top}（同类书按本书分布判）"
        if n_blocks > hi_eff:
            bcount_bad.append(f"块数 {n_blocks} 超本书上限 {hi_eff}（{basis}）")
        elif n_blocks < MIN_BLOCKS:
            bcount_bad.append(f"块数 {n_blocks} 低于下限 {MIN_BLOCKS}")
        elif not (med * 0.5 <= n_blocks <= max(med * 1.5, med + 2)):
            bcount_hint = (f"块数 {n_blocks} 偏离本书常见区间 "
                           f"{max(MIN_BLOCKS, round(med * 0.5))}–{round(max(med * 1.5, med + 2))}（{basis}）")
    else:
        basis = f"新书（基线 {len(sib)} 章 <3，按 2–{MAX_BLOCKS} 硬门）"
        if n_blocks > MAX_BLOCKS:
            bcount_bad.append(f"块数 {n_blocks} 超上限 {MAX_BLOCKS}（拆得过碎，读起来费劲；{basis}）")
        elif n_blocks < MIN_BLOCKS:
            bcount_bad.append(f"块数 {n_blocks} 低于下限 {MIN_BLOCKS}（{basis}）")
        elif not (lo <= n_blocks <= hi):
            bcount_hint = f"块数 {n_blocks} 偏离本章篇幅建议 {lo}–{hi}（本章 {words} 词）"
        hi_eff = MAX_BLOCKS

    res["block_limit"] = {"lo": MIN_BLOCKS, "hi": hi_eff, "basis": basis}
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
    long_q = [{"block": q["block"], "words": q["words"]} for q in res["quotes"]
              if q["words"] > LONG_QUOTE_WORDS]
    res["counts"] = {"blocks": len(res["quotes"]), "quote_long": len(long_q),
                     "segments": sum(len(q["segments"]) for q in res["quotes"]),
                     "segment_miss": miss, "struct_bad": len(struct_bad),
                     "empty_quote": len(empty_quote), "keyword_bad": len(kw_bad),
                     "cjk_low": len(cjk_bad), "template": len(tpl_bad),
                     "keyword_long": len(kw_long), "hole": len(hole_bad),
                     "block_count": len(bcount_bad), "words": words,
                     "block_target": [lo, hi], "block_hint": bcount_hint}
    if d.get("blind") and not n_blocks:
        # 原文有「原句 N」行却解析出 0 块：这是解析盲区，不是「块数 0」。
        # 报成「低于下限 2」会把修的人引向完全错误的动作（2026-10-24 复核）。
        res["verdict"] = "blocked"
        res["reason"] = (f"解析盲区：本章 {d['blind']} 个「原句 N」块未被解析"
                         f"（检查块头是否为 `> **原句 N:** \"…\"`，或是否缺分隔）")
        res["block_limit"] = {"lo": MIN_BLOCKS, "hi": MAX_BLOCKS, "basis": "解析失败，块数判据不成立"}
        res["issues"] = {"struct": [], "empty_quote": [], "keyword": [],
                         "block_count": [res["reason"]], "quote_long": [], "chinese": []}
        return res
    res["issues"] = {"struct": struct_bad, "empty_quote": empty_quote,
                     "keyword": kw_bad, "cjk": cjk_bad, "quote_long": long_q,
                     "template": tpl_bad, "keyword_long": kw_long, "hole": hole_bad,
                     "block_count": bcount_bad}
    blocked = (miss or struct_bad or empty_quote or kw_bad or cjk_bad
               or tpl_bad or hole_bad or bcount_bad)
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


def print_contract(book: Path) -> None:
    """打印「这本书的写作契约」：会判红的、不判红的、以及一章的骨架。

    存在的理由：形态与阈值原先只能靠读 scripts/ 源码反推（2026-10-21 实测某会话
    为写第 1 章读了 58 次检查器源码、0 字产出）。契约应当一条命令吐出来。
    """
    profs = load_profiles()
    key = genre_of(book)
    prof = profs.get(key) or profs.get("_default") or {}
    label = prof.get("label", "")
    subs = prof.get("subitems") or DEFAULT_SUBITEMS
    opt = prof.get("optional_subitems") or []
    blocks = prof.get("blocks") or list(DEFAULT_BLOCK_RANGE)
    nav_items = (prof.get("nav") or {}).get("items") or DEFAULT_NAV_ITEMS
    nav_n = (prof.get("nav") or {}).get("count") or DEFAULT_NAV_COUNT
    f = book_form(book)
    have = f.get("chapters", 0)
    mode = f"按 profile 判（满 {MIN_CHAPTERS_FOR_MODAL} 章后切本书众数）" if have < MIN_CHAPTERS_FOR_MODAL \
        else f"按本书众数判（已有 {have} 章；块数中位 {f['block_median']}，范围 {f['block_range'][0]}–{f['block_range'][1]}）"

    print(f"契约 · {book.name}")
    print(f"  体裁 {key}（{label}）｜{mode}")
    print()
    print("【会判红】bash scripts/chapter.sh \"<章 md>\"   （1–3 秒，退出码 0/1/2）")
    print("  1 引语逐字   每块 `> **原句 N:** \"…\"`；含 `…` 的分段各自独立回 text/chNN_*.txt 取证")
    print("               （大小写、弯直引号不算差异；任一段查无即红）")
    print("  2 空引号     `\"\"` 或分析里残留空引号")
    print(f"  3 子项齐全   {' / '.join(subs)}" + (f"（可加：{'、'.join(opt)}）" if opt else ""))
    print("  4 关键词     每个词必须出现在本块引语或本章原文里（按 / 、 , ； 切分）")
    print("  5 中文       中文理解 ≥6 汉字；为什么这样写 ≥8 汉字且中文占比 ≥15%")
    print("  6 模板套话   「本句描写了场景与人物的反应」「把 X 重新定义 as Y」「此句通过修辞与节奏把人物的")
    print("               内心状态外化」「为后续情节的转折埋下伏笔」等；同一句在同一字段重复 ≥3 次也算")
    print("  7 残句缺词   `的` 后直接跟动词（`把 X 的 写成…`、`\"祖母\"的 词与并列`）= 名词被删掉了，读不通")
    print(f"  8 块数       新书每章 {MIN_BLOCKS}–{MAX_BLOCKS} 块（>{MAX_BLOCKS} 或 <{MIN_BLOCKS} 判红）；"
          f"已有 ≥3 章的书按本书分布判：上限 = max({MAX_BLOCKS}, 本书最高章)"
          f"（本章按词数的建议区间见 chapter.sh 输出；genre profile 只作参照，不覆盖上面的判据）")
    print()
    print("【只提示、不判红，但会毁掉这本书】")
    print(f"  · 引语长度   1–3 句 / 30–70 词 / ≤4 行（创建卡 §3）；块 >{LONG_QUOTE_WORDS} 词时 chapter.sh 打 ⚠️，退出码仍 0")
    print("               ⚠️ 上一版这本书引语中位 168 词、72% 超 100 词，全部 lane 曾经全绿 ⇒ 不要等红灯")
    print(f"  · 块数偏离   在 {MIN_BLOCKS}–{MAX_BLOCKS} 之内、但偏离本章篇幅建议区间时只打 ⚠️")
    print("  · 关键词整句 单个关键词超过 8 个词 = 没选词、整句照抄（提示型，但一眼假）")
    print("  · 谁做的 / 谁欠谁 / 数字 / 关系 / 漏掉的段落   机器结构上查不到（审查表 R1 素读 + R3 对账）")
    print()
    print("【一章的骨架】")
    print("---")
    print("状态: 未读")
    print('modified: "YYYY-MM-DD"')
    print("---")
    print()
    print("# NN. 章标题")
    print()
    print("## 本章导航")
    for it in nav_items[:nav_n]:
        print(f"- **{it}**：…")
    print()
    print("## 精读")
    print('> **原句 1:** "…"')
    for sb in subs:
        print(f"**{sb}**：…")
    print()
    print("## 本章词汇")
    for tier in ("⭐⭐⭐ 高级", "⭐⭐ 进阶", "⭐ 常用"):
        print(f"### {tier}")
        print("| 词/短语 | 释义 | 例句 |")
        print("|---|---|---|")
        print("| … | … | …（必须是本章 text/ 里的逐字原句） |")
        print()
    print("## 一句话总结")
    print("…")
    print()
    print("【顺序】先读本章 text/ 全文 → 写 → 立刻 chapter.sh，红了照它的话改（它会点名哪块哪项）。")
    print("        不要读 scripts/ 源码反推判据：契约就是上面这些，源码只是它的实现。")


def print_check(r: dict) -> None:
    print(f"单章体检：ch{r['chapter']:02d}  {Path(r['md']).name}")
    if r["verdict"] == "undecidable":
        print(f"  ❓ {r['reason']}")
        return
    c = r["counts"]
    print(f"  语料：{r['corpus']}")
    lo, hi = c.get("block_target") or (MIN_BLOCKS, MAX_BLOCKS)
    bl = r.get("block_limit") or {"lo": MIN_BLOCKS, "hi": MAX_BLOCKS, "basis": ""}
    print(f"  块数 {c['blocks']}（本章 {c['words']} 词，建议 {lo}–{hi} 块；"
          f"硬限 {bl['lo']}–{bl['hi']}｜{bl['basis']}）")
    for e in (r["issues"].get("block_count") or []):
        print(f"    ❌ 块数：{e}")
    if c.get("block_hint"):
        print(f"    ⚠️ {c['block_hint']}")

    print("\n【逐字】")
    print(f"  引语块 {c['blocks']}，片段 {c['segments']}，查无 {c['segment_miss']}")
    for q in r["quotes"]:
        for s in q["segments"]:
            if not s["ok"]:
                print(f"    ❌ {q['block']}：{s['text']}")
    print("\n【对应】")
    print(f"  空引号 {c['empty_quote']}｜子项缺 {c['struct_bad']}｜关键词不成立 {c['keyword_bad']}｜中文过薄 {c['cjk_low']}｜模板套话 {c['template']}｜残句缺词 {c['hole']}")
    long_q = r["issues"].get("quote_long") or []
    if long_q:
        ex = "；".join(f"{x['block']}（{x['words']} 词）" for x in long_q[:5])
        more = f" 等 {len(long_q)} 块" if len(long_q) > 5 else ""
        print(f"  ⚠️ 引语偏长 {len(long_q)} 块 >{LONG_QUOTE_WORDS} 词（建议 30–70，创建卡 §3）：{ex}{more}")
    else:
        print(f"  ✅ 引语长度：全部 ≤{LONG_QUOTE_WORDS} 词")
    for e in r["issues"]["struct"]:
        print(f"    ❌ 子项缺：{e['block']} → {e['missing']}")
    for e in r["issues"]["empty_quote"]:
        print(f"    ❌ 空引号：{e}")
    for e in r["issues"]["keyword"]:
        print(f"    ❌ 关键词：{e['block']} → {e['bad']}")
    for e in r["issues"]["cjk"]:
        print(f"    ❌ 中文过薄：{e['block']} / {e['field']} 仅 {e['cjk']} 字（中文占比 {e['ratio']:.0%}）")
    tpl = r["issues"].get("template") or []
    if tpl:
        for e in tpl[:5]:
            print(f"    ❌ 模板套话：{e['block']} / {e['field']} → 「{e['pattern']}」")
        if len(tpl) > 5:
            print(f"    … 另有 {len(tpl) - 5} 处")
    for e in (r["issues"].get("hole") or [])[:5]:
        print(f"    ❌ 残句缺词：{e['block']} / {e['field']} → 「…{e['frag']}…」")
    kwl = r["issues"].get("keyword_long") or []
    if kwl:
        print(f"  ⚠️ 关键词整句 {len(kwl)} 处（建议 3–5 个词；整句照抄＝没选词）")
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

    empty_ch, form_ch, und, long_ch, tpl_ch, hole_ch, bc_ch = [], [], [], [], [], [], []
    for r in rows:
        no = r["chapter"]
        if r["verdict"] == "undecidable":
            und.append(r)
            continue
        n_empty = len(r["issues"]["empty_quote"])
        if n_empty:
            empty_ch.append((no, n_empty))
        n_hole = r["counts"].get("hole", 0)
        if n_hole:
            hole_ch.append((no, n_hole))
        n_tpl = r["counts"].get("template", 0)
        if n_tpl:
            tpl_ch.append((no, n_tpl))
        if r["issues"].get("block_count"):
            bc_ch.append((no, r["issues"]["block_count"]))
        n_long = r["counts"].get("quote_long", 0)
        if n_long:
            long_ch.append((no, n_long))
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
                          "template": [{"ch": n, "n": k} for n, k in tpl_ch],
                          "hole": [{"ch": n, "n": k} for n, k in hole_ch],
                          "form_deviation": [{"ch": n, "dev": d} for n, d in form_ch],
                          "undecidable": [{"ch": r["chapter"], "reason": r["reason"]} for r in und],
                          "overview": ov_msg, "profile": genre_of(book)},
                         ensure_ascii=False, indent=2))
    else:
        print(f"  整书体检 {len(rows)} 章（与 `chapter.sh` 同一实现；只报其他 lane 不查的维度）")
        for no, k in empty_ch:
            print(f"  ❌ ch{no:02d}：分析层残留空引号 {k} 处（删英文引语没删引号，写成 `\"\"`）")
        for no, k in tpl_ch:
            print(f"  ❌ ch{no:02d}：模板套话 {k} 处（分析字段是模板循环，不是分析——见 docs/rules/创建卡.md §3）")
        for no, k in hole_ch:
            print(f"  ❌ ch{no:02d}：残句缺词 {k} 处（`的 写成` 这类——补字不等于补内容）")
        for no, msgs in bc_ch:
            print(f"  ❌ ch{no:02d}：" + "；".join(msgs))
        for no, dev in form_ch:
            print(f"  ❌ ch{no:02d}：" + "；".join(dev))
        for r in und:
            print(f"  ❓ ch{r['chapter']:02d}：{r['reason']}")
        if ov_msg:
            print(f"  ℹ️ {ov_msg}")
        if long_ch:
            worst = sorted(long_ch, key=lambda x: -x[1])[:5]
            print(f"  ⚠️ 引语偏长（提示型，不判红）：{len(long_ch)} 章有块 >{LONG_QUOTE_WORDS} 词 —— "
                  + "、".join(f"ch{no:02d} {n} 块" for no, n in worst)
                  + (f" 等 {len(long_ch)} 章" if len(long_ch) > 5 else ""))
        print(f"  汇总：空引号 {len(empty_ch)} 章 ｜ 模板套话 {len(tpl_ch)} 章 ｜ 残句 {len(hole_ch)} 章 ｜ 块数越界 {len(bc_ch)} 章 ｜ 形态偏离 {len(form_ch)} 章 ｜ 无法判定 {len(und)} 章"
              f"（引语/子项/关键词/中文密度另有 lane，本项不重复计）")
    bad = bool(empty_ch or form_ch or tpl_ch or hole_ch or bc_ch)
    return 1 if bad else (2 if und else 0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--chapter", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--all", action="store_true", help="整书体检（每章都跑，判据同单章）")
    ap.add_argument("--contract", action="store_true", help="打印本书的写作契约：会判红的/不判红的/一章骨架")
    a = ap.parse_args()

    t = Path(a.target).expanduser().resolve()
    if a.chapter:
        md = Path(a.chapter).expanduser().resolve()
        book = t if t.is_dir() else md.parent
    elif t.is_file():
        md, book = t, t.parent
    else:
        md, book = None, t

    if a.contract:
        print_contract(book)
        return 0

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
