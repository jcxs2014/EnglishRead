#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""块作用域内的中文层字段改写器（Maybe Next Time 中文层重写专用）

为什么要有这个工具
------------------
本库禁止「按字符索引切片」的改法（记忆 #1965），也禁止整文件 write 覆盖
（整文件写入会误伤引语行 / 关键词行 / 词表）。而手工用 `edit` 逐块替换
350+ 块 × 3 字段 = 1000+ 次调用，慢且容易 oldString 不唯一。

⇒ 本工具做**块作用域内的行级替换**：
  1. 按 `> **原句 N:**` 切块；
  2. **只在目标块内**替换 `**中文理解**：` / `**为什么这样写**：` /
     `**读者视角提示**：` 三行；缺失则按样板顺序插入；
  3. 文件级 `## 读者视角提示` 小节整节替换（可选）；
  4. 引语行 / 关键词行 / 词表 / 导航 / frontmatter **一概不动**。

落盘用 tempfile + os.replace（记忆 #2042：`open(path,"w")` 失败会把文件截成 0 字节），
且落盘前做三项断言：块数不变、引语行逐字不变、关键词行逐字不变。

用法
----
    python3 scripts/rewrite_zh_fields.py <book_dir> <spec.json> [--dry-run]

spec.json 格式::

    {
      "ch14 the accident.md": {
        "3": {                      # 原句编号（字符串或整数）
          "中文理解": "……",          # 给了就替换（允许空串＝删掉该行）
          "为什么这样写": "……",      # 缺该键＝不动
          "读者视角提示": "……"
        },
        "_tail_": "……新的文件级 ## 读者视角提示 小节正文……"
      }
    }

键名说明：块内三字段用「中文理解 / 为什么这样写 / 读者视角提示」；
特殊键 `_tail_` 表示文件末尾 `## 读者视角提示` 小节整节替换。
值为 null 或省略 = 该项不动。
"""
from __future__ import annotations

import json
import os
import re
import sys
import tempfile

BLOCK_RE = re.compile(r'^> \*\*原句 (\d+):\*\*')
FIELD_LABELS = ("中文理解", "为什么这样写", "读者视角提示")
# 字段行可能带粗体：`**中文理解**：` / `**中文理解：**` / `**中文理解**：`
FIELD_LINE_RE = {
    lab: re.compile(r'^\*\*' + re.escape(lab) + r'\*{0,2}\s*[：:]')
    for lab in FIELD_LABELS
}
TAIL_HEADING = "## 读者视角提示"


def split_blocks(lines):
    """返回 [(block_start, block_end)]，block_end 为下一块起点或文末。"""
    starts = [i for i, l in enumerate(lines) if BLOCK_RE.match(l)]
    ends = starts[1:] + [len(lines)]
    return list(zip(starts, ends))


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().split("\n")


def rewrite_block(lines, s, e, fields):
    """在 [s, e) 块内按 FIELD_LABELS 顺序替换/插入字段行。返回新 lines（就地修改列表）。"""
    seg = lines[s:e]
    # 定位已有字段行
    idx = {}
    for i, l in enumerate(seg):
        for lab in FIELD_LABELS:
            if lab in idx:
                continue
            if FIELD_LINE_RE[lab].match(l):
                idx[lab] = i
    # 逐字段替换 / 插入
    for lab in FIELD_LABELS:
        if lab not in fields or fields[lab] is None:
            continue
        new_text = fields[lab]
        if lab in idx:
            i = idx[lab]
            if new_text == "":
                del seg[i]
                for k in list(idx):
                    if k != lab and idx[k] > i:
                        idx[k] -= 1
            else:
                seg[i] = f"**{lab}**：{new_text}"
        else:
            # 插入位置：紧跟已有的最后一个字段行之后；否则块末
            pos = max(idx.values()) + 1 if idx else len(seg)
            # 若块末有空行，插到空行之前
            while pos > 0 and seg[pos - 1].strip() == "":
                pos -= 1
            seg.insert(pos, f"**{lab}**：{new_text}")
            for k in list(idx):
                if idx[k] >= pos:
                    idx[k] += 1
            idx[lab] = pos
    lines[s:e] = seg
    return lines


def rewrite_tail(lines, new_body):
    """替换文件级 `## 读者视角提示` 小节正文（保留标题行本身）。

    ⚠️ 2026-10-19 修正：若 `new_body` 自带标题行（子代理常把
    「## 读者视角提示」一起写进 spec），会出现**重复标题**——
    实测 B11 批 ch44–ch47 各出现 4 个 `## 读者视角提示`，
    而 `check_chinese_layer` 的解析器会把**最后一个**当标签行、
    **前面几个**当普通行 ⇒ 小节内容被误并进上一个引语块的 tip。
    ⇒ 此处自动剥掉开头的标题行（幂等）。
    """
    try:
        h = next(i for i, l in enumerate(lines) if l.strip() == TAIL_HEADING)
    except StopIteration:
        return lines
    # 剥掉 new_body 开头的标题行（可能有多个）
    body_lines = new_body.strip("\n").split("\n")
    while body_lines and body_lines[0].strip() == TAIL_HEADING:
        body_lines.pop(0)
    new_body = "\n".join(body_lines)
    # 小节范围：到下一个 `## ` 标题或文末
    e = len(lines)
    for j in range(h + 1, len(lines)):
        if lines[j].startswith("## "):
            e = j
            break
    body = new_body.strip("\n").split("\n")
    lines[h + 1:e] = body + [""]
    return lines


def snapshot(lines):
    """用于断言：引语行、关键词行、块数。"""
    quotes = [l for l in lines if BLOCK_RE.match(l)]
    kws = [l for l in lines if l.startswith("**关键词**：")]
    return quotes, kws, len(quotes)


def apply_one(path, spec):
    orig_lines = read_lines(path)
    orig_quotes, orig_kws, orig_nblocks = snapshot(orig_lines)

    lines = list(orig_lines)
    # 从后往前改，避免行号漂移
    blocks = split_blocks(lines)
    for s, e in reversed(blocks):
        m = BLOCK_RE.match(lines[s])
        num = m.group(1)
        fields = spec.get(num) or spec.get(int(num)) if (num in spec or int(num) in spec) else None
        if not fields:
            continue
        rewrite_block(lines, s, e, fields)
    if "_tail_" in spec and spec["_tail_"] is not None:
        lines = rewrite_tail(lines, spec["_tail_"])

    new_quotes, new_kws, new_nblocks = snapshot(lines)
    if new_quotes != orig_quotes:
        raise SystemExit(f"✗ {path}: 引语行被改动（禁止）")
    if new_kws != orig_kws:
        raise SystemExit(f"✗ {path}: 关键词行被改动（禁止）")
    if new_nblocks != orig_nblocks:
        raise SystemExit(f"✗ {path}: 块数变化 {orig_nblocks} -> {new_nblocks}")
    return orig_lines, lines


def write_atomic(path, lines):
    d = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    book_dir, spec_path = sys.argv[1], sys.argv[2]
    dry = "--dry-run" in sys.argv
    spec = json.load(open(spec_path, encoding="utf-8"))

    touched = 0
    for fname, fspec in spec.items():
        path = os.path.join(book_dir, fname)
        if not os.path.exists(path):
            print(f"❓ 文件不存在：{path}")
            continue
        orig, new = apply_one(path, fspec)
        if orig == new:
            print(f"· {fname}: 无变化")
            continue
        if not dry:
            write_atomic(path, new)
        diff = sum(1 for a, b in zip(orig, new) if a != b) + abs(len(orig) - len(new))
        print(f"✏️  {fname}: {diff} 行差异")
        touched += 1
    print(f"=== 改写 {touched} 个文件{'（dry-run，未落盘）' if dry else ''} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
