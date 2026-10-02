#!/usr/bin/env python3
"""按 JSON 规格生成一章精读 md，引语**逐字**从 text/ 抽取（禁令 1 的机械化）。

为什么不手写引语
----------------
AGENTS 8.2 禁令 1：「引语、词表例句、分析层里作证据的英文，一律复制粘贴」。
实测本库手打引语的缺陷率远高于复制粘贴，而本项目已多次出现
「引语逐字正确但与分析层说的事不是同一句」（8.1 a2）。

本脚本的判据
------------
每条引语给 `start` / `end` 两个**锚点**（各取引语首尾几个词），
脚本在 text/chNN_*.txt 里定位 `[start, end]` 的完整区间并原样取出，
**取不到即退出码 2、不产出文件**（fail-closed，不留半成品）。

用法
----
    python3 astarion_build.py <book_dir> <spec.json> <out.md>
"""
import json
import os
import re
import sys

FRONTMATTER = "---\n状态: 未读\nmodified: \"{date}\"\n---\n"


def load_chapter(book_dir, ch):
    tdir = os.path.join(book_dir, "text")
    hits = sorted(
        f for f in os.listdir(tdir)
        if f.startswith(f"ch{int(ch):02d}_") and f.endswith(".txt")
    )
    if len(hits) != 1:
        sys.exit("text/ch%02d_*.txt 命中 %d 件（期望 1）" % (int(ch), len(hits)))
    return open(os.path.join(tdir, hits[0]), encoding="utf-8").read()


def grab(text, start, end):
    """按首尾锚点抽取逐字原文片段（跨段落也取整段，不断句）。"""
    i = text.find(start)
    if i < 0:
        return None, "start 锚点查无: %r" % start
    j = text.find(end, i)
    if j < 0:
        return None, "end 锚点查无: %r" % end
    # 延伸到句末：锚点通常写在最后一个实词上（"…shade of pink"），句末标点
    # 在它之后。不延伸的话引语会停在句中——逐字比对照样全绿（子串仍成立），
    # 但引语本身是残句。延伸范围＝句末标点 + 紧随其后的闭引号。
    k = j + len(end)
    while k < len(text) and text[k] in ".!?…":
        k += 1
    while k < len(text) and text[k] in "”’」』\"":
        k += 1
    return text[i:k], None


def bad_edges(quote):
    """引语首尾形态守卫。返回 '' 表示通过，否则返回人可读的原因。

    ⚠️ 这一类缺陷**逐字比对全部通过**：锚点只是把 `start` 写在原文开引号
    **之后**，抽出来的仍是原文的连续子串，所以 verify_quotes / sweep_full /
    check_chapter_quotes 三道全绿。唯一症状是引语在排版上是错的——
    以右引号或小写字母开头、以左引号结尾（本批 26 块里 11 块命中）。
    ⇒ 只能靠「切之前先看形态」拦，本守卫就是那道拦。
    """
    q = quote.strip()
    if not q:
        return "空引语"
    if q[0] in "”’」』":
        return "首字符是右引号/右括号（锚点跳过了原文的开引号）"
    if q[0].islower():
        return "首字符是小写字母（引语从句子中间开始）"
    if q[0] != "“" and not q[0].isupper():
        return "首字符既不是开引号也不是大写字母: %r" % q[0]
    if q[-1] in "“‘「『":
        return "末字符是左引号/左括号（引语在引号中间截断）"
    if q[-1] in ",;:-—":
        return "末字符是连接符/标点（引语在半句处截断）"
    if q[-1].islower():
        return "末字符是小写字母（引语在句中截断）"
    return ""


def main():
    book_dir, spec_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    spec = json.loads(open(spec_path, encoding="utf-8").read())
    text = load_chapter(book_dir, spec["ch"])

    lines = [FRONTMATTER.format(date=spec.get("date", "2026-10-02")), ""]
    lines.append("# %s" % spec["h1"])
    lines.append("")

    nav = spec["nav"]
    lines.append("## 本章导航")
    lines.append("")
    for item in nav:
        lines.append("- **%s**：%s" % (item[0], item[1]))
    lines.append("")

    lines.append("## 精读")
    lines.append("")
    quotes = []
    missing = []
    # ⚠️ 2026-10-02 五步审查：worker 常按「哪句最值得讲」挑块，写进 spec 的顺序
    # 与它们在 text/ 里的先后不一致 ⇒ md 的分析块**不按原文段落骨架排列**，
    # 而且块内的邻近性引用（「上一块」「下一段」「本节结束前」）会被打假
    # （实测 6/29 章：ch01/ch02/ch06/ch20/ch21/ch22）。
    # ⇒ 抽完后**按原文位次重排再编号**，邻近性引用随之自动对上原文。
    staged = []
    for n, blk in enumerate(spec["blocks"], 1):
        quote, err = grab(text, blk["start"], blk["end"])
        if err:
            missing.append("块 %d: %s" % (n, err))
            continue
        quote = re.sub(r"\s+", " ", quote).strip()
        bad = bad_edges(quote)
        if bad:
            missing.append("块 %d: %s —— 引语: %r" % (n, bad, quote[:60]))
            continue
        staged.append((text.find(quote), blk, quote))
    staged.sort(key=lambda t: t[0])
    for _, blk, quote in staged:
        quotes.append(quote)

    if missing:
        print("抽取/边界检查失败，未产出：\n  " + "\n  ".join(missing), file=sys.stderr)
        sys.exit(2)

    for n, quote in enumerate(quotes, 1):
        lines.append('> **原句 %d:** "%s"' % (n, quote))
        lines.append("")
        for label in ("中文理解", "关键词", "为什么这样写", "读者视角提示"):
            lines.append("- **%s**：%s" % (label, staged[n - 1][1][label]))
        lines.append("")

    if missing:
        print("锚点抽取失败，未产出：\n  " + "\n  ".join(missing), file=sys.stderr)
        sys.exit(2)

    # 词表由 build_vocab_table.py 产出后作为 --vocab-file 注入（fail-closed）
    if spec.get("vocab_file"):
        vocab = open(spec["vocab_file"], encoding="utf-8").read().strip()
        lines.append("## 本章词汇")
        lines.append("")
        lines.append(vocab)
        lines.append("")

    lines.append("## 一句话总结")
    lines.append("")
    lines.append(spec["summary"])
    lines.append("")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("written %s (%d 引语块)" % (out_path, len(spec["blocks"])))


if __name__ == "__main__":
    main()