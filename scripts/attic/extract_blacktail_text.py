#!/usr/bin/env python3
"""
一次性脚本（attic）：为 Blacktail 重新提取 text/，关闭 extract_chapters.py 的 dropcap 修复正则。

原因：extract_chapters.py 的 clean() 含 dropcap 修连正则
    re.sub(r'\\b([A-Z])\\s+([A-Z][a-z]+|[A-Z]{2,})\\b', merge, t)
该书正文无 dropcap span（grep class=dropcap 仅命中书末样章 021_exc_1_sup.xhtml），
该正则在本书只会误伤，例如 "Mommy was In A Mood" → "Mommy was In AMood"（虚构连字）。
本脚本复用 extract_chapters 的清洗流程但去掉该正则，输出与 epub 逐字一致。

用法：python3 scripts/attic/extract_blacktail_text.py
"""
import re, html, os, zipfile, posixpath
from urllib.parse import unquote

EPUB = "notes/books/novels/blacktail-by-scott-hawkins/library/Blacktail A Novel (Scott Hawkins) (z-library.sk, 1lib.sk, z-lib.sk).epub"
OUT = "notes/books/novels/blacktail-by-scott-hawkins/text"

# c001..c010 = 正文 10 单元；其余为封面/版权/目录/致谢/样章/宣传页
CONTENT_IDS = [f"c{i:03d}" for i in range(1, 11)]
NAMES = {
    "c001": "ch01_prologue_hate",
    "c002": "ch02_chapter_one_love",
    "c003": "ch03_chapter_two_the_son_of_snow",
    "c004": "ch04_chapter_three_dominion",
    "c005": "ch05_chapter_four_the_god_of_the_lost",
    "c006": "ch06_chapter_five_fatberry",
    "c007": "ch07_chapter_six_mercy",
    "c008": "ch08_chapter_seven_the_fire_of_god",
    "c009": "ch09_chapter_eight_the_place_of_the_skull",
    "c010": "ch10_chapter_nine_the_far_hill",
}


def clean(raw: str) -> str:
    t = re.sub(r'<(p|div|h[1-6]|li|br)\b[^>]*>', '\n', raw)
    t = re.sub(r'</(p|div|h[1-6])>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
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


def main():
    root = os.getcwd()
    z = zipfile.ZipFile(os.path.join(root, EPUB))
    container = z.read('META-INF/container.xml').decode('utf-8', 'ignore')
    opf_file = re.search(r'full-path="([^"]+)"', container).group(1)
    opf_path = posixpath.dirname(opf_file)
    opf = z.read(opf_file).decode('utf-8', 'ignore')

    manifest = {}
    for it in re.findall(r'<item\b[^>]*/?>', opf):
        idm = re.search(r'id="([^"]+)"', it)
        hm = re.search(r'href="([^"]+)"', it)
        if idm and hm:
            manifest[idm.group(1)] = posixpath.normpath(posixpath.join(opf_path, unquote(hm.group(1))))

    out_dir = os.path.join(root, OUT)
    os.makedirs(out_dir, exist_ok=True)
    for cid in CONTENT_IDS:
        path = manifest[cid]
        body = clean(z.read(path).decode('utf-8', errors='ignore'))
        target = os.path.join(out_dir, NAMES[cid] + ".txt")
        open(target, 'w').write(body + "\n")
        nchars = len(re.sub(r'\s+', '', body))
        print(f"{NAMES[cid]:<48s} {nchars:>7} 字符")


if __name__ == "__main__":
    main()
