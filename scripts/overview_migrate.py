#!/usr/bin/env python3
"""总览层「口径外」引语迁移器。

两类问题分开处理：

1. **列表项引语**（`- "…"（ch01）` / `1. "…"（ch01）`）
   —— 纯格式问题，引语本身已带章号，只是不在 `>` 引用块里。
   `--apply` 时**自动**改成 `> "…"（ch01）`。

2. **行内引语**（中文段落里夹着英文引语）
   —— 需要判断「这句是引语还是转述」，**一律不自动改**，只出清单：
   能在 `text/` 里唯一定位到章的，给出建议块；定位不到的标「疑似转述」。

用法：
    python3 scripts/overview_migrate.py <书目录> [<书目录>…]          # 只出报告
    python3 scripts/overview_migrate.py <书目录> --apply              # 迁移第 1 类
    python3 scripts/overview_migrate.py <书目录> --json               # 机器可读

退出码：0 无待判项；1 有待判行内引语（不代表失败，表示还需人判）。
"""
import sys, os, re, glob, json, argparse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/scripts")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from overviewcheck.names import is_overview  # noqa: E402

MARK = re.compile(r'^(\s*)(?:[-*+]|\d{1,2}[.)、])\s+(.+)$')
CH = re.compile(r'[（(]\s*ch\s*(\d{1,3})\s*[)）]\s*$', re.I)
QUOTED = re.compile(r'"([^"]{15,})"')
CJK = re.compile(r'[\u4e00-\u9fff]')


def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())


def load_corpus(book):
    corpus = {}
    for f in sorted(glob.glob(os.path.join(book, "text", "*.txt"))):
        m = re.search(r'ch(\d{1,3})', os.path.basename(f), re.I)
        if not m:
            continue
        corpus[norm(open(f, encoding="utf-8", errors="replace").read())] = int(m.group(1))
    return corpus


def chapter_of(quote, corpus):
    key = norm(quote)
    if len(key) < 15:
        return None
    hits = {ch for text, ch in corpus.items() if key in text}
    return hits.pop() if len(hits) == 1 else None


def migrate_book(book, apply=False):
    corpus = load_corpus(book)
    stats = {"books": book, "list_moved": 0, "inline": [], "files": []}
    for path in sorted(glob.glob(os.path.join(book, "*.md"))):
        if not is_overview(path):
            continue
        lines = open(path, encoding="utf-8").read().splitlines()
        out, changed = [], False
        for i, ln in enumerate(lines, 1):
            s = ln.strip()
            if s.startswith(">") or s.startswith("#") or not s:
                out.append(ln)
                continue
            m = MARK.match(ln)
            if m and CH.search(m.group(2).strip()):
                body = m.group(2).strip()
                if body.startswith('"'):
                    out.append("> " + body)
                    stats["list_moved"] += 1
                    changed = True
                    continue
            for q in QUOTED.findall(ln):
                if not re.search(r'[a-zA-Z]{3}', q):
                    continue
                ch = chapter_of(q, corpus)
                if ch is None:
                    stats["inline"].append(
                        {"file": os.path.basename(path), "line": i,
                         "quote": q[:90], "chapter": None,
                         "verdict": "疑似转述/改写（原文找不到）"})
                else:
                    stats["inline"].append(
                        {"file": os.path.basename(path), "line": i,
                         "quote": q[:90], "chapter": ch,
                         "verdict": "可定位，建议抽成引用块"})
            out.append(ln)
        if changed:
            stats["files"].append(os.path.basename(path))
            if apply:
                open(path, "w", encoding="utf-8").write("\n".join(out))
    return stats


def render(stats):
    b = os.path.basename(os.path.abspath(stats["books"]))
    print(f"## {b}")
    print(f"- 列表项迁移：{stats['list_moved']} 条"
          + (f"（文件：{', '.join(stats['files'])}）" if stats["files"] else ""))
    print(f"- 待判行内引语：{len(stats['inline'])} 条")
    for it in stats["inline"][:20]:
        tag = f"ch{it['chapter']:02d}" if it["chapter"] else "未定位"
        print(f"  - {it['file']}:{it['line']} [{tag}] {it['quote']}")
    return len(stats["inline"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("books", nargs="+")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    allstats = [migrate_book(b, a.apply) for b in a.books]
    if a.json:
        print(json.dumps(allstats, ensure_ascii=False, indent=1))
    else:
        pending = sum(render(s) for s in allstats)
        print(f"\n=== 合计：迁移 {sum(s['list_moved'] for s in allstats)} 条；待判 {pending} 条 ===")
    return 1 if any(s["inline"] for s in allstats) else 0


if __name__ == "__main__":
    sys.exit(main())
