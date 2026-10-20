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


BROKEN_MARKS = (
    "can't open file", "No such file or directory", "ModuleNotFoundError",
    "ImportError", "command not found", "Traceback (most recent call last)",
)


def script_paths(cmd: list[str]) -> list[str]:
    """从命令里挑出脚本路径（scripts/…\.py|\.sh），用来做"文件还在不在"的前置校验。"""
    out = []
    for tok in cmd:
        if tok.startswith("scripts/") and (tok.endswith(".py") or tok.endswith(".sh")):
            out.append(tok)
    return out


def run(cmd: list[str]) -> tuple[int, str]:
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def looks_broken(out: str) -> str | None:
    """输出里出现"根本没跑起来"的痕迹就返回命中的标记。

    ⚠️ 2026-10-20 第三方复核抓到的假绿：脚本被搬走后，基线里那 10 条 case 的命令
    仍然指向旧路径，跑出来是 `can't open file …`，而 runner 只比 rc+sha ⇒ 照样 ✅。
    **rc 相同不等于跑过**——所以要先认"没跑起来"的形态。
    """
    for mark in BROKEN_MARKS:
        if mark in out:
            return mark
    return None


def book_stamp(book: str) -> str:
    """书目录最后一次 commit —— 基线绑「书的状态 + 工具行为」两者。

    书在并行实例手里持续变动，只绑工具行为不够：同一工具、同一书，内容改了输出就该变。
    所以基线记下录制时的书 commit，对比时先比它：变了就判「基线过期（书在动）」跳过，
    而不是报工具回归。
    """
    r = subprocess.run(["git", "log", "-1", "--format=%H", "--", book],
                       cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip()[:12]


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
        missing = [s for s in script_paths(c["cmd"]) if not (ROOT / s).exists()]
        if missing:
            skipped += 1
            print(f"⏭  {c['id']}  （脚本已不存在：{', '.join(missing)}，基线失效，跳过）")
            continue
        rc, out = run(c["cmd"])
        broken = looks_broken(out)
        if broken:
            bad += 1
            print(f"❌ {c['id']}  **没跑起来**（输出含 {broken!r}）——不是判定结果，先修命令")
            continue
        rec = {"id": c["id"], "book": c["book"], "cmd": c["cmd"], "head": book_stamp(c["book"]),
               "rc": rc, "sha": fingerprint(out), "tail": tail_lines(out)}
        if a.record:
            new.append(rec)
            print(f"📝 {c['id']}: rc={rc} sha={rec['sha']}")
            continue
        if "rc" not in c or "sha" not in c:
            bad += 1
            print(f"❌ {c['id']}  **基线里没有这一条**（新增 case 必须先 --record）")
            continue
        if c.get("head") and rec["head"] != c["head"]:
            print(f"⏭  {c['id']}  （书已变：{c['head']}→{rec['head']}，基线过期，跳过）")
            skipped += 1
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
