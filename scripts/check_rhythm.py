#!/usr/bin/env python3
"""check_rhythm.py —— 写作节律探针（过程信号，不判内容）

为什么要有它（2026-10-21）
--------------------------
`ebenezer-scrooge-by-j-s-barnes` 曾出现 **40 章在 33 分钟内提交**（约 50 秒一章），
产出是模板套话（中文密度 5%、866 条阻断）。当时没有任何信号提示「这不对劲」——
`gate.sh` 只在写完之后跑，跑出来是红的，但已经写了 40 章。

反向的情况同样看不见：`session-8bb4ff97` 连续 2 小时没有一次提交，
外部只能靠翻会话日志才知道它在跑脚本而不是在写。

本工具只回答三个过程问题：
1. 相邻两次提交间隔是否过短（疑似批量生成）；
2. 是否长时间没有提交（疑似停滞或空转）；
3. 本书目录是否有已写未提交的 md。

**它不判内容对错**，也不进门禁（退出码恒 0）。用途是给执行方自己一个节律报警，
给审查方一个「这本书是怎么写出来的」的旁证。

用法：
    python3 scripts/check_rhythm.py "<书目录>" [--min-minutes 5] [--max-gap-hours 6]
    python3 scripts/check_rhythm.py "<书目录>" --last 40
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def _git(*args: str, cwd: Path) -> str:
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return r.stdout


def _repo_root(p: Path) -> Path:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=p,
                         capture_output=True, text=True).stdout.strip()
    return Path(out or p.parents[3])


def commits_of(book: Path) -> list[dict]:
    """本书目录的提交，按时间正序。"""
    repo = _repo_root(book)
    rel = book.relative_to(repo)
    raw = _git("log", "--date=iso-strict", "--format=%H|%ad|%s", "--", str(rel), cwd=repo)
    out = []
    for line in raw.splitlines():
        parts = line.split("|", 2)
        if len(parts) < 3:
            continue
        sha, when, subject = parts
        try:
            t = datetime.fromisoformat(when.replace("Z", "+00:00"))
        except ValueError:
            continue
        rows = _git("show", "--name-status", "--format=", sha, cwd=repo).splitlines()
        md, added = [], []
        for row in rows:
            parts = row.split("\t")
            if len(parts) < 2:
                continue
            st, f = parts[0][:1], parts[-1]
            if not (f.startswith(str(rel) + "/") and f.endswith(".md")):
                continue
            if not re.match(r"ch\d", f.rsplit("/", 1)[-1]):
                continue
            md.append(f)
            if st == "A":
                added.append(f)
        out.append({"sha": sha[:9], "time": t, "subject": subject,
                    "md": md, "added": added})
    out.sort(key=lambda c: c["time"])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--min-minutes", type=float, default=2.0,
                    help="逐章提交间隔短于该分钟数判「过快」（默认 2）")
    ap.add_argument("--max-gap-hours", type=float, default=6.0,
                    help="距上次提交超过该小时数且有未提交 md 判「停滞」（默认 6）")
    ap.add_argument("--last", type=int, default=12, help="明细最多列多少条（默认 12）")
    a = ap.parse_args()

    book = Path(a.book).resolve()
    if not book.is_dir():
        print(f"✗ 不是目录：{book}")
        return 2

    commits = commits_of(book)
    if not commits:
        print(f"⚠️ 本书目录还没有任何提交：{book.name}")
        return 0

    ch_commits = [c for c in commits if c["added"]]
    gaps = [(b["time"] - a2["time"]).total_seconds() / 60.0
            for a2, b in zip(ch_commits, ch_commits[1:])]
    fast = [(g, c) for g, c in zip(gaps, ch_commits[1:]) if g < a.min_minutes]
    bulk = [c for c in ch_commits if len(c["added"]) >= 5]
    median = sorted(gaps)[len(gaps) // 2] if gaps else None

    print(f"=== 写作节律：{book.name} ===")
    print(f"提交 {len(commits)} 次 ｜ 首个 {commits[0]['time']:%Y-%m-%d %H:%M} "
          f"｜ 最近 {commits[-1]['time']:%Y-%m-%d %H:%M}")
    if median is not None:
        print(f"相邻间隔：中位 {median:.1f} 分钟 ｜ 最短 {min(gaps):.1f} ｜ 最长 {max(gaps):.1f}")

    print(f"新增章的提交 {len(ch_commits)} 次")
    if bulk:
        print(f"⚠️ 一次新增 ≥5 章：{len(bulk)} 次（批量生成特征）")
        for c in bulk[-a.last:]:
            print(f"   - {c['time']:%m-%d %H:%M} 新增 {len(c['added'])} 章：{c['subject'][:44]}")
    if fast:
        print(f"⚠️ 逐章间隔过快：{len(fast)} 次 < {a.min_minutes:g} 分钟"
              f"（一章正文含 5 块分析，正常不会这么快）")
        for g, c in fast[-a.last:]:
            print(f"   - {c['time']:%m-%d %H:%M} 间隔 {g:.1f} 分钟：{c['subject'][:52]}")
    else:
        print(f"✅ 没有间隔 < {a.min_minutes:g} 分钟的提交")

    # 未提交 md
    porcelain = _git("status", "--porcelain", "--", str(book.relative_to(_repo_root(book))),
                     cwd=_repo_root(book)).splitlines()
    dirty = [l for l in porcelain if l.endswith(".md") or ".md" in l]
    last_t = commits[-1]["time"].astimezone()
    idle_h = (datetime.now(last_t.tzinfo) - last_t).total_seconds() / 3600.0
    if dirty:
        print(f"ℹ️ 有 {len(dirty)} 个未提交的 md（最近一次提交在 {idle_h:.1f} 小时前）")
        for l in dirty[:a.last]:
            print(f"   - {l}")
        if idle_h > a.max_gap_hours:
            print(f"⚠️ 停滞：已 {idle_h:.1f} 小时没有提交，但还有未落盘的 md")
    else:
        print("✅ 本书目录无未提交 md")

    print("\n明细（最近 %d 次提交）：" % min(a.last, len(commits)))
    for c in commits[-a.last:]:
        print(f"  {c['time']:%m-%d %H:%M} {c['sha']} md×{len(c['md']):<2} {c['subject'][:60]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
