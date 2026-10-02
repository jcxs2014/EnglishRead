#!/usr/bin/env python3
"""
chapter_text_path.py — text/ 提取件定位的**唯一共用实现**

## 为什么要有这个文件（根因修复，不是又一处补丁）

本项目精读 md 的文件名规范是「唯一分隔符＝**单空格**」（根 AGENTS.md「文件命名约定」：
`ch<NN> <keyplot>.md`，**禁止** `_` `-` `'`），而 `text/` 提取件按同一约定命名
（`ch01 1 the house.txt`）。但多个门禁/生产工具各自内联了一份
「用 `_` 拼 glob」的定位代码，于是**同一处缺陷在一个批次里复发三次**：

| 工具 | 原写法 | 症状（假红型） |
|---|---|---|
| `vocab_candidates.py` | `re.match(r'^ch%s[_.]', f)` | ❌ text/ 里找不到 ch1 的提取件 → SystemExit |
| `check_chapter_quotes.py` | `re.match(rf'^ch{tag}_.*\\.txt$', f)` | missing ch01*.txt → SystemExit |
| `gen_overview.py` | `glob.glob(f"{book}/text/ch{n:0{w}d}_*.txt")` | ❌ text/ 里找不到 ch1 的提取件 → SystemExit |

三处都是**工具坏了而内容没问题**（AGENTS 第 3 条「假红型＝先修工具」）。
教训（与 Coral Bones「修好的证据是报警数变化」同源）：**同一判据散落三处时，
打补丁必然漏第四处**——必须收口成单一实现。

## 分隔符口径
- `_`（历史约定，本库多数书）、`.`、**空格**（AGENTS 规定的精读命名）
- 章号位数不定：2 位（`ch08`）/ 3 位（`ch076`，全书连号）/ 1 位，
  **真源是文件名自带的位数**，不是调用方传的整数的位数

## 用法
```python
from chapter_text_path import find_chapter_text
p = find_chapter_text(book_dir, n)      # 不存在则返回 None
p = require_chapter_text(book_dir, n)  # 不存在则 SystemExit（带可读原因）
```
`scripts/` 已在 PYTHONPATH（同目录 import 可用），故工具内直接
`from chapter_text_path import require_chapter_text`。
"""
import os
import re
import sys

# 分隔符：下划线 / 点 / 空格。空格是根 AGENTS.md 规定的精读命名分隔符。
_SEP = r"[_. ]"


def find_chapter_text(book_dir, n, suffix=".txt"):
    """定位 text/chNN*.txt；找不到返回 None。n 是不带前导零的整数。"""
    tdir = os.path.join(book_dir, "text")
    if not os.path.isdir(tdir):
        return None
    # ① 直接按「调用方给的位数」试（覆盖 ch8 / ch08 / ch008 三种写法）
    for width in (2, 3, 1, 4):
        tag = str(n).zfill(width)
        names = sorted(f for f in os.listdir(tdir)
                       if re.match(rf"^ch{tag}({_SEP}.*)?{re.escape(suffix)}$", f))
        if names:
            return os.path.join(tdir, names[0])
    # ② 兜底：扫描全部 chNN 前缀文件，按数字取第一个等于 n 的
    for f in sorted(os.listdir(tdir)):
        m = re.match(r"^ch(\d+)", f)
        if m and int(m.group(1)) == int(n) and f.endswith(suffix):
            return os.path.join(tdir, f)
    return None


def require_chapter_text(book_dir, n, suffix=".txt"):
    p = find_chapter_text(book_dir, n, suffix)
    if p is None:
        tdir = os.path.join(book_dir, "text")
        have = sorted(f for f in os.listdir(tdir) if f.startswith("ch")) \
            if os.path.isdir(tdir) else []
        sys.exit(
            "❌ text/ 里找不到 ch%s 的提取件。\n"
            "   目录：%s\n"
            "   该目录下现有 ch* 文件：%s\n"
            "   （分隔符已兼容 _ / . / 空格；请确认章号与 text/ 实际文件名是否对得上）"
            % (n, tdir, ", ".join(have[:12]) or "（无）")
        )
    return p


if __name__ == "__main__":
    # 自测：python3 scripts/chapter_text_path.py <book_dir> [章号...]
    book = sys.argv[1]
    ns = [int(x) for x in sys.argv[2:]] or list(range(1, 4))
    for n in ns:
        print(n, "→", find_chapter_text(book, n))
