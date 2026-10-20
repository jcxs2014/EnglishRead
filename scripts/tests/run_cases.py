#!/usr/bin/env python3
"""已完工书做回归测试集：锁住「今天的判定」，合并/改口径后必须一字不差。

背景：551 本已完工书 + 26 份缺陷档案是带标注的语料，但过去只靠"挑几本跑跑看"验新工具。
本脚本把「书 × 命令」的组合录成基线（rc + 输出指纹 + 尾部关键行），之后任何合并/改判据
都必须先过这一关——**假红与漏报都可量化，而不是"我看还行"**。

用法：
    python3 scripts/tests/run_cases.py            # 跑全部，与基线对比
    python3 scripts/tests/run_cases.py --record   # 重新录制基线（改动经人确认后才可录）
    python3 scripts/tests/run_cases.py -k quotes  # 只跑 id 含 quotes 的

退出码：0 全部一致；1 有差异；2 基线文件缺失。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CASES = Path(__file__).resolve().parent / "cases.json"


def run(cmd: list[str]) -> tuple[int, str]:
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def fingerprint(out: str) -> str:
    return hashlib.sha256(out.encode("utf-8")).hexdigest()[:16]


def tail_lines(out: str, n: int = 3) -> list[str]:
    keep = [l.rstrip() for l in out.splitlines()
            if l.strip() and (l.lstrip().startswith(("✅", "❌", "⚠️", "❓", "══", "=== 汇总"))
                              or "正门结论" in l)]
    return (keep[-n:] if keep else [l.rstrip() for l in out.splitlines() if l.strip()][-n:])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", action="store_true")
    ap.add_argument("-k", default=None)
    a = ap.parse_args()

    if not CASES.exists() and not a.record:
        print(f"❌ 没有基线文件 {CASES}；先跑 --record", file=sys.stderr)
        return 2
    cases = json.loads(CASES.read_text(encoding="utf-8")) if CASES.exists() else []
    if a.k:
        cases = [c for c in cases if a.k in c["id"]]

    bad = skipped = 0
    new = []
    for c in cases:
        if not (ROOT / c["book"]).exists():
            print(f"⏭  {c['id']}  （书目录不存在，跳过）")
            skipped += 1
            continue
        rc, out = run(c["cmd"])
        rec = {"id": c["id"], "book": c["book"], "cmd": c["cmd"],
               "rc": rc, "sha": fingerprint(out), "tail": tail_lines(out)}
        if a.record:
            new.append(rec)
            print(f"📝 {c['id']}: rc={rc} sha={rec['sha']}")
            continue
        same = rc == c["rc"] and rec["sha"] == c["sha"]
        if same:
            print(f"✅ {c['id']}")
        else:
            bad += 1
            print(f"❌ {c['id']}  rc {c['rc']}→{rc}  sha {c['sha']}→{rec['sha']}")
            print(f"   期望尾行: {c['tail']}")
            print(f"   实际尾行: {rec['tail']}")

    if a.record:
        CASES.write_text(json.dumps(new, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"\n已录制 {len(new)} 条基线 → {CASES.relative_to(ROOT)}")
        return 0

    print(f"\n合计 {len(cases) - skipped} 条：一致 {len(cases) - skipped - bad}，不一致 {bad}，跳过 {skipped}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
