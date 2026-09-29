#!/usr/bin/env python3
"""核对 md 的 `## 本章导航` 与 `## 一句话总结` 两层里的英文片段是否逐字见于 text/。

为什么需要（六道门禁的结构性盲区）:
  `verify_quotes` / `check_chapter_quotes` / `sweep_full` **只解析 `## 精读` 的引语行**，
  `sweep_analysis_inline` 只扫**引语块之外**的正文行——而导航层与总结层既不在引语口径内，
  也不在它的扫描范围里。实测这两层是本库最大的共同盲区
  （Jane Eyre 98 条缺陷约六成在导航/总结/读者视角内）。
  ⇒ 写作侧「只能从 text/ 或已写好的引语块复制」这条规则，事后只能靠本脚本兜。

用法:
  python3 scripts/check_nav_layer.py "<书目录>" [<单个 md> ...]
  python3 scripts/check_nav_layer.py "<书目录>" --per-chapter   # 逐章核（严）

判定:
  ❌ 全书查无 = 阻断型（多半是手打造词）→ 退出码 2
  ⚠️ 本章查无 = 提示型（可能引的是别章，需人工判）→ 只报
  跳过: 单个词（≤4 字母，可能是专名缩写）、非字母开头、纯中文括号内容
"""
import re
import sys
from pathlib import Path

book = Path(sys.argv[1])
per_chapter = "--per-chapter" in sys.argv
targets = [Path(x) for x in sys.argv[2:] if not x.startswith("--")] or sorted(book.glob("ch*.md"))

flat = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())

# 左右引号配对表：中文可嵌套但须同类闭合；直引号不嵌套。
_PAIRS = {"「": "」", "『": "』"}

# 模板字段名 / 子项标签：出现在导航层但不是引语。
_GENERIC_LABELS = {"Tropes", "Navigation", "Premise", "Setting", "Themes"}

# 分节卡：真在原文里，但被 extract_chapters 归到 text/xx_section_card_*.txt，
# 不占 chNN 编号 ⇒ 按 chNN 比对必假红。加载一次即整册豁免。
def _load_section_cards(book_dir):
    buf = ""
    for f in (book_dir / "text").glob("xx_section_card_*.txt"):
        buf += f.read_text(encoding="utf-8")
    return flat(buf) if buf else ""


_CARDS_FLAT = _load_section_cards(book)


def _paired_segments(chunk):
    """逐个切出**闭合**的引号内容，结构上杜绝跨段吞并。

    ⚠️ 2026-09-29（Carmen and Grace）：正则方案反复跨段误报
    （67 → 17 条仍全假），根因是未配对的单只左引号会让 `.*?` 一路吃到下一段。
    这里改为**从左引号起、找它自己的同类右引号**，找不到就跳过该左引号，
    绝不跨越。返回的内容块互不重叠。
    """
    out, i, n = [], 0, len(chunk)
    while i < n:
        ch = chunk[i]
        if ch in _PAIRS:
            close = _PAIRS[ch]
            j = chunk.find(close, i + 1)
            if j == -1:                      # 未配对 → 跳过，不跨段找
                i += 1
                continue
            out.append(chunk[i + 1:j])
            i = j + 1
        elif ch in "\"'`":
            j = chunk.find(ch, i + 1)
            if j == -1:
                i += 1
                continue
            out.append(chunk[i + 1:j])
            i = j + 1
        else:
            i += 1
    return out

corpus = {}
for f in sorted((book / "text").glob("ch*.txt")):
    corpus[f.name] = flat(f.read_text(encoding="utf-8"))
all_flat = "".join(corpus.values())
if not all_flat:
    print("❓ text/ 为空或无 ch*.txt")
    sys.exit(2)

fail, warn = [], 0
for md in targets:
    text = md.read_text(encoding="utf-8")
    chunks = []
    if "## 本章导航" in text:
        chunks.append(text.split("## 本章导航", 1)[1].split("\n## ", 1)[0])
    if "## 一句话总结" in text:
        chunks.append(text.split("## 一句话总结", 1)[1])
    for chunk in chunks:
        # ⚠️ 2026-09-29 修正（Carmen and Grace 实测）：原字符类只认
        # `" “ ” ' \``，**不含中文引号 `「」『』`**——而本库与该书全部用 `「」` 写引文。
        # 同批修 check_crossref 的教训：**先查工具覆盖，再信它的 0**。
        #
        # ⚠️ 加 `「」` 后暴露第二个问题：中文引号**可嵌套**（`「…「…」…」`），
        # 贪婪匹配会一路吃到下一个 `「` 当右引号，于是抽出
        # `d never have allowed it），说自己…「To hell with…` 这种跨段垃圾
        # （该书 29 条 ❌ 里绝大多数是这种）。故改为**非贪婪 + 配对闭合**：
        # 只认「同类配对」（`「…」` 或 `『…』`），右引号必须是**同一个**字符。
        # ⚠️ 2026-09-29 三轮修正（Carmen and Grace 实测，67→17 条仍全是误报）：
        # 非贪婪 + 同类配对仍会在**未配对的单只 `「`** 上跨段吃
        # （`…（「X」…「Y…」` 这种：前一个 `」` 被上一轮匹配消耗，剩下的 `「`
        #  找不到同类右引号，正则就一路吃到下一段）。**根治办法：先切段再取词**——
        #  把 chunk 按「左引号」切成互不重叠的小段，每段只认它自己的第一个闭合右引号。
        # 这样任何跨段吞并在结构上就不可能发生。
        for seg in _paired_segments(chunk):
            # 块内可能中英混排（`前文 Chinese 后文`），只取**英文片段**逐段核。
            # ⚠️ 不能整块 flat：`「他说：Don't be sleepin' on me，然后…」` 整块
            # 拼起来必然查无，会把真引语也一起判成阻断型。
            for piece in re.findall(r"[A-Za-z][A-Za-z0-9'’,.:;!?()\- ]{3,160}", seg):
                piece = piece.strip()
                if len(piece) <= 4 or not re.search(r"[A-Za-z]{3}", piece):
                    continue
                # ⚠️ 2026-09-29 豁免两类**必假**（Carmen and Grace 6 条里 4 条）：
                #  ① 通用子项标签（`Tropes`）——模板字段名不是引语；
                #  ② 分节卡标题（如 `The Daughters of the Wild Mother According to
                #     Grace 1992–2002`）——真在原文里，但被 extract_chapters 归到
                #     `text/xx_section_card_*.txt`，不占 chNN 编号 ⇒ 按 chNN 比对必假红。
                if piece in _GENERIC_LABELS:
                    continue
                fs = flat(piece)
                if not fs:
                    continue
                if fs in all_flat:
                    continue
                if _CARDS_FLAT and fs in _CARDS_FLAT:
                    continue
                own = any(fs in v for k, v in corpus.items()
                          if per_chapter and k.startswith(md.name[:4]))
                if own:
                    continue
                if per_chapter:
                    fail.append(f"{md.name}: 「{piece}」本章查无（全书亦无）")
                else:
                    warn += 1
                    fail.append(f"{md.name}: 「{piece}」全书查无 ⇒ 阻断型")

for f in fail:
    print(("❌ " if "全书查无" in f or "本章查无" in f else "⚠️ ") + f)
print(f"\n=== 导航/总结层英文核对：❌ {len([f for f in fail if '查无' in f])} ｜ ⚠️ {warn} ===")
sys.exit(2 if any("全书查无" in f or "本章查无" in f for f in fail) else 0)
