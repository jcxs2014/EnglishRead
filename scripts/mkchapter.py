#!/usr/bin/env python3
"""mkchapter.py — 以 JSON 规格生成一章（避免 shell 引号转义层）。

用法:
  python3 scripts/mkchapter.py <spec.json>

spec.json 字段:
  book    书目录（相对仓库根）
  ch      章号字符串，如 "02"
  h1      H1 标题
  nav     [一句话概括, 情感弧线位置, Tropes 兑现/反转, 人物弧线, 叙事手法]
  summary 一句话总结正文（必填）
  quotes  "Q1=@prefix;Q2=@prefix*"  （不写 -- 前缀，脚本自己加）
  blocks  "Q1|中文理解|关键词|为什么这样写|读者视角提示; ..."（5 段，不写 Q 编号以外的竖线）

⚠️ 本脚本**不做任何验证**，只负责把 JSON 变成 new_chapter.py 的 argv。
   逐字注入与硬断言仍由 new_chapter.py / inject_by_para.py / build_vocab_section.py 负责。
"""
import json
import subprocess
import sys
from pathlib import Path

spec_path = Path(sys.argv[1])
spec = json.loads(spec_path.read_text(encoding="utf-8"))
root = Path(__file__).resolve().parent.parent

argv = [
    "python3", "scripts/new_chapter.py",
    spec["book"], str(spec["ch"]), spec["h1"],
    *spec["nav"],
    spec["summary"],
    "--quotes=" + spec["quotes"],
    "--blocks=" + spec["blocks"],
]
r = subprocess.run(argv, cwd=root, capture_output=True, text=True)
sys.stdout.write(r.stdout)
sys.stderr.write(r.stderr)
sys.exit(r.returncode)
