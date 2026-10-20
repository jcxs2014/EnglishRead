#!/usr/bin/env python3
"""raw-gates 留存策略的机械执行者。

策略（2026-10-20 定，见 docs/rules/PLAN.md 步骤 5）：
    `.memory/raw-gates/<书 slug>/` 每本书**只保留最近一次运行**（按文件名日期前缀
    `YYYY-MM-DD` 判定），更早的运行从工作树与索引中移除——**git 历史仍可取证**：

        git log --oneline -- .memory/raw-gates/<slug>/
        git show <commit>:.memory/raw-gates/<slug>/<文件名>

为什么不是「保留 30 天」：本库是活跃库，177 个书目录的最新一次运行全部在
30 天内（2026-10-20 实测最早 10-11），按天数剪枝**永远剪不到**，等于没策略。
按「每本书最新一次」才是有界的。

引用保护（2026-10-20 实测后加）：文档与工作日志里有 **193 处**按「目录/文件名」
    引用了具体某一次运行的原件（如 `.memory/raw-gates/<slug>/2026-10-01-final_gates.txt`）。
    删掉被引用的文件会**当场断链**，所以本脚本默认**跳过被引用者**；`--no-ref-check`
    才忽略这一点（不建议）。

安全：
- 默认 **dry-run**，只打印将要删除的清单与统计，不动任何文件。
- `--apply` 才真正 `git rm`（同时删工作树）。删除前会校验路径都在 `.memory/raw-gates/` 下。
- 无日期前缀的文件（如 `README.md`、手工笔记）**一律保留**。
- 某本书目录若最新一天的文件数 < 2，跳过该目录（避免「最新那次只落了一个文件」
  把上一次完整运行清掉）。

用法：
    python3 scripts/prune_raw_gates.py            # 看清单
    python3 scripts/prune_raw_gates.py --apply    # 执行
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GATES = ROOT / ".memory" / "raw-gates"
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")


def git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"git {' '.join(args)} 失败：{out.stderr.strip()}")
    return out.stdout


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="真正删除（默认只演练）")
    ap.add_argument("--no-ref-check", action="store_true", help="不检查文档引用（不建议）")
    args = ap.parse_args()

    if not GATES.is_dir():
        sys.exit(f"找不到 {GATES}")

    cited: set[tuple[str, str]] = set()
    if not args.no_ref_check:
        import re as _re
        pat = _re.compile(r"raw-gates/([^/\s`)]+)/([^/\s`)]+)")
        for base in ["docs", ".memory/daily", ".memory/log", "COLLABORATION.md", "AGENTS.md"]:
            b = ROOT / base
            files = [b] if b.is_file() else ([p for p in b.rglob("*.md")] if b.is_dir() else [])
            for f in files:
                try:
                    cited.update(pat.findall(f.read_text(errors="ignore")))
                except OSError:
                    pass

    drop: list[Path] = []
    protected: list[Path] = []
    kept_files = 0
    skipped: list[str] = []

    for d in sorted(p for p in GATES.iterdir() if p.is_dir()):
        files = [f for f in d.rglob("*") if f.is_file()]
        if not files:
            continue
        dated = [(f, m.group(1)) for f in files if (m := DATE_RE.match(f.name))]
        undated = [f for f in files if not DATE_RE.match(f.name)]
        kept_files += len(undated)
        if not dated:
            continue
        latest = max(day for _, day in dated)
        newest = [f for f, day in dated if day == latest]
        oldest = [f for f, day in dated if day != latest]
        if len(newest) < 2:
            skipped.append(f"{d.name}（最新 {latest} 仅 {len(newest)} 个文件）")
            kept_files += len(files) - len(undated)
            continue
        kept_files += len(newest)
        for f in oldest:
            if (d.name, f.name) in cited:
                protected.append(f)
            else:
                drop.append(f)

    # 安全校验：只允许 .memory/raw-gates/ 之下
    for f in drop:
        if GATES not in f.parents:
            sys.exit(f"拒绝操作越界路径：{f}")

    total = sum(1 for d in GATES.iterdir() if d.is_dir())
    print(f"书目录 {total} 个；文件保留 {kept_files}，引用保护 {len(protected)}，将删除 {len(drop)}")
    if skipped:
        print(f"跳过 {len(skipped)} 个目录（最新一次不完整）：")
        for s in skipped[:10]:
            print("  -", s)
    for f in drop[:20]:
        print("  drop", f.relative_to(ROOT))
    if len(drop) > 20:
        print(f"  … 其余 {len(drop) - 20} 个")

    if not args.apply:
        print("\n（演练模式，未改动任何文件；加 --apply 执行）")
        return 0
    if not drop:
        print("无需删除。")
        return 0

    rel = [str(f.relative_to(ROOT)) for f in drop]
    git("rm", "-q", "--", *rel)
    print(f"\n已 git rm {len(rel)} 个文件（git 历史仍可取证）。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
