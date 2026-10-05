#!/usr/bin/env python3
"""**总览中英配对检测器**（e 步专用；补 `check_overview_full` / `check_overview_labels` 的共同盲区）。

为什么需要它：那两个工具**只验「引语逐字 + 标注章」**，对**中文分析说的是不是
这条引语**零覆盖——正是 AGENTS 第 10 条点名的「标签对 ≠ 内容对」。
2026-10-05 五步审查在 I Am Not Jessica Chen 实测抓到 6 条**英文引语与中文整段错配**
（模板里的 `{Q:chNN:seq}` 按记忆中的块号填写，而写作方事后又删过块，seq 已前移）。

判据（可机械、不需人判）：
  总览里每条的中文字段，是**手写**的；池里同一条引语的 `中文理解` 是**写作时写的**。
  二者本应描述同一句话。做法：把总览的中文字段与池的中文理解做 **字符重合率**，
  低于阈值即报「疑似漂移」，交人判。

⚠️ **报的是「疑似」，不是「缺陷」**——人判时要读两段文本确认（纪律：报警≠缺陷）。
本脚本的价值是**把 15 条缩到 3–4 条**，不是替人判。

用法：python3 scripts/attic/check_overview_zh_anchor.py "<书目录>" [--thr 0.30]
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from gen_overview import build_pool  # noqa: E402

ENT = re.compile(r"^([①-⑳])\s+(.+?)（ch(\d\d)）\s*$")
ZH = re.compile(r"^\*\*(中文|上下文)\*\*[：:]\s*(.+?)\s*$")


def shingles(s: str, k: int = 6):
    s = re.sub(r"[^一-鿿]", "", s)
    return {s[i:i + k] for i in range(max(0, len(s) - k + 1))}


def overlap(a: str, b: str) -> float:
    A, B = shingles(a), shingles(b)
    if not A:
        return 1.0
    return len(A & B) / len(A)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    thr = 0.30
    if "--thr" in sys.argv:
        thr = float(sys.argv[sys.argv.index("--thr") + 1])
    bd = Path(args[0])
    pool = build_pool(str(bd))
    by_quote = {}
    for (n, s), (q, zh) in pool.items():
        by_quote.setdefault(q, (n, s, zh))

    flagged = 0
    for md in sorted(bd.glob("00_*.md")):
        L = md.read_text(encoding="utf-8").split("\n")
        for i, l in enumerate(L):
            m = ENT.match(l.strip())
            if not m:
                continue
            q = m.group(2).strip()
            hit = by_quote.get(q)
            n, s, pool_zh = hit if hit else (None, None, None)
            zh = ctx = ""
            for k in range(i + 1, min(i + 5, len(L))):
                mz = ZH.match(L[k].strip())
                if mz:
                    if mz.group(1) == "中文" and not zh:
                        zh = mz.group(2)
                    elif mz.group(1) == "上下文" and not ctx:
                        ctx = mz.group(2)
            if pool_zh is None:
                print(f"❌ {md.name} {m.group(1)} 引语不在池中（疑非逐字）")
                flagged += 1
                continue
            ov = overlap(zh, pool_zh)
            mark = "✅" if ov >= thr else f"❌ 重合率 {ov:.0%}"
            if ov < thr:
                flagged += 1
            print(f"{mark}  {md.name} {m.group(1)} → ch{n:02d}#{s}")
            print(f"      总览中文: {zh[:70]}")
            print(f"      池中文解: {pool_zh[:70]}")
    print(f"\n疑似漂移 {flagged} 处（阈值 {thr:.0%}）；⚠️ 需人判，报警≠缺陷")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())