#!/usr/bin/env python3
"""规则文档健康检查 —— 防「重构完三个月又长回 171KB」。

为什么需要它
------------
2026-10-20 的重构把「开工必读」从 171,990 字符压到 6,019 字符，靠的是**拆分 + 删重**。
但历史上同一件事失败过四次（`docs/实测档案/X_2026-10-20_规则体系审计与重构依据.md`）：
模板从 20,817 B 长到 226,721 B，期间文件头写着 9 处「唯一副本」而 4 处已失效。
**拆分只是把乱麻剪开，不设守卫就会重新缠上。**

三条判据（都是「当场可数」的，不做语义判断）
--------------------------------------------
1. **注入预算**：`AGENTS.md` 字符数必须 ≤ 4,882（三次实测的最小自动注入预算）。
   超了就等于「有人要背一段看不见的规则」——这是唯一硬指标。
2. **路由可达**：`docs/rules/*.md` 每一份都必须在 `AGENTS.md` 的路由表里出现（按 basename），
   否则它就是一份**没有入口的规则**——写了也没人会读。
3. **引用不悬空**：`docs/`、`.memory/`、`scripts/` 下的路径引用必须真实存在。
   2026-10-20 拆分当场扫出 8 处悬空引用。
4. **脚本有归口**：`scripts/*.py` 每个都必须在 `docs/rules/工具登记.md` 里登记一行；
   书目录 / `docs/` / 根目录**不许出现 .py**（一次性脚本用完进 `scripts/attic/`）。
   2026-10-20 实测：30 天内新增 92 个脚本、`scripts/attic/` 已堆 564 个 ⇒ 不设归口，
   脚本库只会越滚越大，而且没人说得清哪个还在用。

退出码：0 全部通过；1 有阻断（预算超标 / 路由缺失 / 悬空引用）。
提示型（硬编码数字）不阻塞，只列出来。
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS = ROOT / "AGENTS.md"
RULES_DIR = ROOT / "docs" / "rules"
INJECT_BUDGET = 4882  # 字符数，不是字节

# 只查这几种前缀，避免把书里的相对路径误判成文档引用
PATH_RE = re.compile(r"`((?:docs|\.memory|scripts)/[^`\s]+?)(?:#L\d+(?:-L\d+)?)?`")
NUM_RE = re.compile(r"(\d+)\s*(?:个|条)\s*(?:lane|检查器)")
# 这两份是**过程文档**（怎么重构 / 迁移进度），不是运行期规则，不需要 AGENTS 入口
NOT_ROUTED = {"PLAN.md", "MIGRATION.md"}
REGISTRY = ROOT / "docs" / "rules" / "工具登记.md"


def strip_code_blocks(text: str) -> str:
    """去掉 ``` 代码块：里面的路径是给人复制的命令示例，不是文档引用。"""
    return re.sub(r"```.*?```", "", text, flags=re.S)


def main() -> int:
    bad: list[str] = []
    warn: list[str] = []

    if not AGENTS.exists():
        print("❌ 找不到 AGENTS.md")
        return 1
    agents = AGENTS.read_text(encoding="utf-8")

    # —— 1. 注入预算 ——
    n = len(agents)
    if n > INJECT_BUDGET:
        bad.append(f"AGENTS.md {n} 字符 > 预算 {INJECT_BUDGET}（超出 {n - INJECT_BUDGET}）")
    else:
        print(f"✅ AGENTS.md {n} 字符 / 预算 {INJECT_BUDGET}")

    # —— 2. 路由可达 ——
    missing_route = []
    for f in sorted(RULES_DIR.glob("*.md")):
        if f.name in NOT_ROUTED:
            continue
        if f.name not in agents:
            missing_route.append(f.name)
    if missing_route:
        bad.append("docs/rules/ 下没有入口（AGENTS.md 路由表未提及）：" + "、".join(missing_route))
    else:
        # ⚠️ 2026-10-20 第三方复核 P-8：原消息按 glob 计数说「8 份全部有入口」，
        # 而 NOT_ROUTED 的 2 份其实被跳过了——✅ 里不能出现"我查了 N 份"的虚数。
        _routed = [f for f in RULES_DIR.glob("*.md") if f.name not in NOT_ROUTED]
        print(f"✅ docs/rules 需路由的 {len(_routed)} 份全部有入口"
              f"（{', '.join(sorted(NOT_ROUTED))} 为过程文档，按设计豁免）")

    # —— 3. 引用不悬空 ——
    dangling = []
    for f in [AGENTS, *sorted(RULES_DIR.glob("*.md"))]:
        text = strip_code_blocks(f.read_text(encoding="utf-8"))
        for m in PATH_RE.finditer(text):
            p = m.group(1).rstrip("，。；、)")
            if p.endswith("/") or any(c in p for c in "<>*…"):
                continue  # 占位符/通配符不是真引用
            if not (ROOT / p).exists():
                dangling.append(f"{f.name} → {p}")
    if dangling:
        bad.append("悬空引用：" + "；".join(sorted(set(dangling))[:8]))
    else:
        print("✅ 路径引用全部存在")

    # —— 4. 脚本有归口 ——
    def _git(*args):
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
        return r.stdout.splitlines() if r.returncode == 0 else []

    tracked = _git("ls-files", "scripts")
    tracked_py = [x for x in tracked if x.endswith(".py") and not x.endswith("__init__.py")]
    reg = REGISTRY.read_text(encoding="utf-8") if REGISTRY.exists() else ""
    if not REGISTRY.exists():
        bad.append("缺少 docs/rules/工具登记.md（新增脚本无处登记）")
    else:
        unregistered = [x.split("/")[-1] for x in tracked_py
                        if f"`{x.split('/')[-1]}`" not in reg]
        if unregistered:
            bad.append(f"{len(unregistered)} 个**已入库**脚本未登记：{', '.join(unregistered[:6])}"
                       + ("…" if len(unregistered) > 6 else "")
                       + " → 在 docs/rules/工具登记.md 补一行")
        else:
            print(f"✅ scripts/ 已入库的 {len(tracked_py)} 个脚本全部登记")

    scratch = [x for x in _git("ls-files", "--others", "--exclude-standard", "scripts")
               if x.endswith(".py")]
    if scratch:
        warn.append("scripts/ 下有未入库的临时脚本（用完请删或进 attic）：" + "、".join(scratch[:5]))

    allow = ("scripts/", "site/", ".memory/tools/", ".memory/raw-gates/")
    seen = _git("ls-files") + _git("ls-files", "--others", "--exclude-standard")
    stray = [x for x in dict.fromkeys(seen)
             if x.endswith(".py") and not x.startswith(allow)]
    if stray:
        bad.append("书目录/文档目录里出现 .py（脚本进 scripts/；书内脚手架只能放 gitignore 的 `.build/`）："
                   + "、".join(stray[:5]))
    else:
        print("✅ 书/文档目录内无散落脚本（.build/ 与 raw-gates 证据除外）")

    rg = [x for x in tracked if x.endswith(".py")]
    if rg:
        warn.append(f".memory/raw-gates/ 里有 {len(rg)} 个审查期一次性脚本（作为证据保留，不参与工具库统计）")

    # —— 5. 回归基线不许指向已不存在的脚本 ——
    # ⚠️ 2026-10-20 第三方复核抓到：脚本搬走后基线里仍有 10 条 case 指向旧路径，
    #   跑出来是 `can't open file …`，而 runner 只比 rc+sha ⇒ 照样 ✅（假绿）。
    #   这里做**静态**检查，不依赖 runner 是否被跑过。
    cases_path = ROOT / "scripts" / "tests" / "cases.json"
    if cases_path.exists():
        import json as _json
        try:
            _cases = _json.loads(cases_path.read_text(encoding="utf-8"))
        except Exception as e:
            bad.append(f"cases.json 解析失败：{e}")
            _cases = []
        dead = []
        for c in _cases:
            for tok in c.get("cmd", []):
                if isinstance(tok, str) and tok.startswith("scripts/") and tok.endswith((".py", ".sh")):
                    if not (ROOT / tok).exists():
                        dead.append(f"{c.get('id','?')} → {tok}")
        if dead:
            bad.append(f"回归基线里有 {len(dead)} 条命令指向已不存在的脚本（假绿源头）："
                       + "、".join(dead[:4]) + ("…" if len(dead) > 4 else ""))
        else:
            print(f"✅ 回归基线 {len(_cases)} 条的脚本路径全部存在")

    # —— 提示型：硬编码数字 ——
    for f in [AGENTS, *sorted(RULES_DIR.glob("*.md"))]:
        text = strip_code_blocks(f.read_text(encoding="utf-8"))
        for m in NUM_RE.finditer(text):
            line = text[: m.start()].count("\n") + 1
            warn.append(f"{f.name}:{line} 硬编码「{m.group(0)}」→ 改成「以现场为准」或去掉数字")

    print()
    for w in warn[:10]:
        print(f"⚠️  {w}")
    if len(warn) > 10:
        print(f"⚠️  …另有 {len(warn) - 10} 处")
    for b in bad:
        print(f"❌ {b}")
    print()
    if bad:
        print("结论：❌ 有阻断（规则文档正在重新变胖 / 丢入口 / 断链）")
        return 1
    print("结论：✅ 规则文档健康")
    return 0


if __name__ == "__main__":
    sys.exit(main())
