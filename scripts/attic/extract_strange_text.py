#!/usr/bin/env python3
"""
extract_strange_text.py — Strange Is the Light (Sarah Maria Griffin) 专用提取器

背景：extract_chapters.py 的 dropcap 修连正则
    r'\b([A-Z])\s+([A-Z][a-z]+|[A-Z]{2,})\b'
会把正常正文误连（单字母 I / A 后接大写词即触发），如
"A Summer"→"ASummer"、"I Thought"→"IThought"。
本 epub 全部 xhtml 实测 class 中零 dropcap/initial/small-caps 结构，故本脚本
复用 extract_chapters 的其余逻辑，仅关闭该修连正则。

用法：
  python3 scripts/attic/extract_strange_text.py "<epub>" --out-dir <text目录> --min-len 600
"""
import re, os, importlib.util

_spec = importlib.util.spec_from_file_location(
    "extract_chapters",
    os.path.join(os.path.dirname(__file__), "..", "extract_chapters.py"),
)
ec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ec)


def clean_no_dropcap(raw: str) -> str:
    t = re.sub(r'<(p|div|h[1-6]|li|br)\b[^>]*>', '\n', raw)
    t = re.sub(r'</(p|div|h[1-6])>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    import html as _html
    t = _html.unescape(t)
    t = t.replace('\u00a0', ' ')
    lines = []
    for l in t.split('\n'):
        l = l.strip()
        if not l:
            lines.append('')
        elif lines and lines[-1] and not l[0].isupper() and not re.match(r'^[\u201c\u201d\'"(\-—*\d]', l):
            lines[-1] += ' ' + l
        else:
            lines.append(l)
    return '\n'.join(lines).strip()


ec.clean = clean_no_dropcap

if __name__ == "__main__":
    ec.main()
