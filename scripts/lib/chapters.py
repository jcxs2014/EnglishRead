"""章节 md 发现：兼容两套命名。

库内并存两种章文件名：

- `ch01 rita meets lily.md`（主流，201 本）
- `01 Prologue.md` / `02 Chapter One.md`（29 本，多为早中期成品与企鹅版）

所有按章取文件的检查器都应走 `chapter_files()`，否则第二种命名整层落空——
2026-10-22 实测：这 29 本在 ②⑦⑯⑱⑲ 五个 lane 上全部按「无 ch*.md」跳过或报错。
"""

from __future__ import annotations

import re
from pathlib import Path

# ch01 / ch1 / 01 / 1 开头，后面不能紧跟数字（避免 ch180 被读成 ch18）
_NO = re.compile(r"^(?:ch)?(\d{1,3})(?![0-9])", re.I)

# 总览三篇的命名（中英双口径），不算章节
_OVERVIEW_ZH = re.compile(r"^\d+_|^(?:\d+\s*[_.\-\s]?)?(?:概述|金句精选|金句集|情感节点|总结|论证节点)[.\s_]*\.md$")
_OVERVIEW_EN = re.compile(
    r"^(?:\d+\s*[_\-\s]?)"
    r"(?:overview|quotes?|golden[_\s-]*quotes?|emotional[_\s-]*(?:nodes?|moments?)"
    r"|summar\w*|highlights?)[_\s-]*\.md$",
    re.I,
)


def _is_overview(name: str) -> bool:
    return bool(_OVERVIEW_ZH.match(name) or _OVERVIEW_EN.match(name))


def chapter_no(name: str) -> int | None:
    """从文件名取章号；不是章文件返回 None。"""
    if _is_overview(name):
        return None
    m = _NO.match(name)
    return int(m.group(1)) if m else None


def chapter_files(book) -> list[Path]:
    """按章号升序返回章节 md；同名同号时优先 `ch*` 形式。"""
    book = Path(book)
    got: dict[int, Path] = {}
    for p in sorted(book.glob("*.md")):
        n = chapter_no(p.name)
        if n is None:
            continue
        cur = got.get(n)
        if cur is None or (not cur.name.lower().startswith("ch")
                           and p.name.lower().startswith("ch")):
            got[n] = p
    return [got[k] for k in sorted(got)]


def legacy_format(book) -> bool:
    """旧格式章节：有章文件但通篇没有 `原句 N` 引语标记。

    这类书（2026-10-22 实测 29 本）的 ②⑦⑱⑲⑳ 判据结构上不适用，
    调用方应报「❓ 旧格式·不适用」而不是判红或静默跳过。
    """
    files = chapter_files(book)
    if not files:
        return False
    for p in files:
        try:
            if "原句" in p.read_text(encoding="utf-8", errors="replace"):
                return False
        except OSError:
            continue
    return True
