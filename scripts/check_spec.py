#!/usr/bin/env python3
"""check_spec.py — mkchapter.py 的 spec JSON 预检器（并可自动补一处低级失误）。

为什么需要（2026-10-01 The Death of Us 实测连踩三次）
------------------------------------------------------
我自己手写喂给 `mkchapter.py` 的 spec JSON **反复漏掉 `nav` 数组的闭合方括号**，
而 `mkchapter.py` 直接 `json.loads` 后抛 JSONDecodeError —— **不生成文件、也不产出
任何可读报错**，看上去像工具坏了（ch08/ch10/ch11 三次，每次多花两轮）。

本脚本做三件事，任一不满足即退出码 2：
  1. `json.loads` 成功；失败且文件以 `"\n}` 结尾（典型的漏 `]`）⇒ 自动补 `  ]`；
  2. 必备字段齐全：book / ch / h1 / nav / summary / quotes / blocks；
  3. nav 恰好 5 项、quotes 与 blocks 条数相等且 ≥3。

用法:
  python3 scripts/check_spec.py <spec.json> [...]
  python3 scripts/check_spec.py --patch <patch.py> <spec.json> [...]
      --patch 传入的 .py 文件在**已解析对象 d 上** exec（可一次性补 quotes/blocks/
      summary 等长字段，避免再手写一遍 JSON 字符串）
"""
import json
import sys
from pathlib import Path

REQUIRED = {"book", "ch", "h1", "nav", "summary", "quotes", "blocks"}


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
        flag = "✅" if not problems else "❌"
        print(f"{flag} {p.name}: nav={len(d.get('nav', []))} quotes={nq} blocks={nb}"
              + ("　｜ " + "；".join(problems) if problems else ""))
        if problems:
            rc = 2
    sys.exit(rc)


if __name__ == "__main__":
    main()