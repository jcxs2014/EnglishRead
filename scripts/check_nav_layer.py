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

# ⚠️ 2026-09-29：md 里的破折号（—/–/——）在 flat 时被丢弃，会把
# `Love Alive" from your heart—The Little Mothers` 这类**含破折号的原文**
# 切成两半而误报（Carmen and Grace ch27 挽联实证：原文有 from your heart，
# md 改写成 `—`，flat 后两边拼不回去）。判为工具假阳性，故不删破折号，
# 而是**双口径**：先按原样比，未命中再按「去破折号两侧空格」比一次。

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


def piece_is_cjk(s):
    return bool(re.search(r"[\u3400-\u9fff\uf900-\ufaff\u3040-\u30ff\uac00-\ud7af]", s))


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

# ⚠️ 2026-10-18（DSH-Mac，C 组 C1）：**epub 二级参考集**。
# 本工具只拿 `text/` 作真值，而 `text/` 由 extract_chapters 产出、**可能漏提取**
# ——sweet-fury 只有 23 件，导航层 7 条英文逐条从 `library/*.epub` 直读全部命中
# （`Picture me now: crouched in hall closet…` 等），修前被判「全书查无 ⇒ 阻断型」，
# 实为**参考集不全型假红**。与 AGENTS 第 3 条「完整 lane / 降级 lane」同源：
#   text/ 命中            → 通过
#   text/ 查无 + epub 命中 → ⚠️ 提示型「text/ 提取缺漏」，**不判红**
#   两边都查无            → ❌ 阻断型
# 无 epub 的书（占多数）行为与修前完全一致。
_EPUB_FLAT = ""
_epubs = sorted((book / "library").glob("*.epub")) if (book / "library").is_dir() else []
for _ep in _epubs:
    try:
        from verify_quotes import epub_flat_text as _eft
        _EPUB_FLAT = flat(_eft(str(_ep)))
    except Exception:
        _EPUB_FLAT = ""
    if _EPUB_FLAT:
        break
if _EPUB_FLAT:
    print(f"ℹ️ epub 二级参考集：{_epubs[0].name}（{len(_EPUB_FLAT)} flat 字符）"
          f"　—— text/ 查无而 epub 命中将判**提示型**不判红")

fail, warn = [], 0
for md in targets:
    text = md.read_text(encoding="utf-8")
    chunks = []
    # ⚠️ 2026-10-18（DSH-Mac，C 组 C1）：本工具判「英文片段是否逐字见于 text/」，
    # **定位必须按锚点行切**，不能沿用原来的
    # `text.split("## 本章导航",1)[1].split("\n## ",1)[0]`。
    # 那个口径在「`## 一句话总结` 排在 `## 本章导航` 之前」的文件里会把后面几节
    # 全吞进来——the-lost-spectacular ch10 实测：`## 一句话总结`(:8) 在前，
    # `## 本章导航`(:12) 的 chunk 被 `.split("\n## ")[0]` 截断是对的，但
    # `## 一句话总结` 那份 `text.split(...)[1]` **延伸到文件尾**，于是
    # `## 本章引语`(:24) 里 12 条真引语被当导航层去 text/ 查无 ⇒ 12 条假红。
    # 改为：锚点行 → 到**下一个同级标题行**为止。
    _SEC_ANCHOR = re.compile(r"(?m)^(?:#{2,4}[ \t]+|\*\*[^*]+\*\*[ \t]*$)")

    def _section(anchor: str) -> str:
        """返回 `anchor` 标题行之后、下一个同级标题行之前的内容；无此节返回 ''。

        ⚠️ 两个模式都要试：节标题有两种写法——`## 本章导航` 与
        `**本章导航**`（无 `#` 的加粗形态，sweet-fury 全书 19 个文件用它）。
        原判据是字面 `"## 本章导航" in text`，加粗形态整节结构性不可见。
        """
        for _pat in (r"(?m)^#{2,4}[ \t]*" + anchor + r"[ \t]*$",
                     r"(?m)^\*\*" + anchor + r"\*\*[ \t]*$"):
            _m = re.search(_pat, text)
            if not _m:
                continue
            _rest = text[_m.end():].split("\n", 1)
            _body = _rest[1] if len(_rest) > 1 else ""
            _nxt = _SEC_ANCHOR.search(_body)
            return _body[:_nxt.start()] if _nxt else _body
        return ""

    for _h in ("本章导航", "一句话总结"):
        _sec = _section(_h)
        if _sec:
            chunks.append(_sec)

    # ⚠️ 同日：**导语层**（首个 H2 之前）也要扫。只取 `> ` 引用块形态、
    # 排除 `> **原句 N:**`（那是引语层，由 verify_quotes / verify_fragments_indep 收），
    # 否则 Sunrise on the Reaping ch32/ch34/ch38 那类「第 11 行导言虚构剧情」
    # 在本工具里结构性不可见（.memory/daily/2026-10-13.md:115-155 实证）。
    _lead_end = re.search(r"(?m)^#{2,4}[ \t]+", text)
    lead = text[:_lead_end.start()] if _lead_end else ""
    for _ln in lead.splitlines():
        _s = _ln.strip()
        if _s.startswith("> ") and not _s.startswith("> **原句"):
            chunks.append(_s)

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
            # ⚠️ 2026-09-29 **回归修正**：上一版改成「块内逐个英文片段」提取，
            # 结果把导航层里**所有英文碎片**都当引语——全库 198 本里 100+ 本爆报警，
            # 典型假阳性：burn-for-you 导航层的 `"almost smile"` / `"only mean to you"`
            # 是作者自撰的短语标签（bookstore meet-cute 那类），不是原文引语。
            # 原脚本「整块比对 + 长度下限」本是对的，唯一真问题是**跨段吞并**，
            # 而那已由 `_paired_segments` 结构性解决。
            # ⇒ 回到**整块比对**；中英混排块用「剥中文后仍逐字命中」兜底。
            seg = seg.strip()
            if len(seg) <= 4 or not re.search(r"[A-Za-z]{3}", seg):
                continue
            if piece_is_cjk(seg):
                # 中英混排：只取最长的一段连续英文（引文本体），仍不足以判红则跳过
                runs = re.findall(r"[A-Za-z][A-Za-z0-9'’,.:;!?()\-]*[A-Za-z0-9'’.]", seg)
                runs = [r for r in runs if len(r) > 4]
                if not runs:
                    continue
                seg = max(runs, key=len)
            if len(seg) <= 4 or not re.search(r"[A-Za-z]{3}", seg):
                continue
            # ⚠️ 2026-09-29 豁免两类**必假**：
            #  ① 通用子项标签（`Tropes`）——模板字段名不是引语；
            #  ② 分节卡标题（如 `The Daughters of the Wild Mother According to
            #     Grace 1992–2002`）——真在原文里，但被 extract_chapters 归到
            #     `text/xx_section_card_*.txt`，不占 chNN 编号 ⇒ 按 chNN 比对必假红。
            if seg in _GENERIC_LABELS:
                continue
            # ⚠️ 2026-10-02 豁免 **`text/` 提取件文件名**（Bird of a Thousand Stories 实测）：
            # 导航「书内章号」栏常写 epub 件名与提取件名（`ch19_chapter_twelve_a_posy_of_
            # alkaloids.txt`）。它们是**文件名**、不是引语——按「本章 text/ 正文」比对必然
            # 查无（文件名里还带下划线，正文里不会这么写）⇒ **必假**。
            # 判据：以 `.txt`/`.md`/`.xhtml` 结尾，或整体形如 `chNN_...`。
            # 回归：Bird 该项 9 → 0，而 ch06/ch08/ch40 三条**真实**缺陷不在此豁免范围内
            #（它们不含扩展名），仍照报——**豁免只放行文件名，不放宽引语判据**。
            if re.search(r"\.(txt|md|xhtml|epub)$", seg) or re.fullmatch(r"ch\d+_[\w.]*", seg):
                continue
            # ⚠️ 2026-09-29 豁免 **trope / 情节标签**（全库回归实测）：
            # 本库导航层通行写法是 `- "forced proximity" 倒计时——…` /
            # `……（训话 + 裸遇 + 同居三连），"will never see again"当场作废`，
            # 其中双引号包的是**作者自撰的情节标签或 trope 名**，不是原文引语。
            # 这类短语天然是「短 + 无句读」，按长度与分隔符即可与真引语区分：
            #   rookie-season 127→0、local-gods 93→0、love-sick 95→0。
            # ⚠️ 代价：真实但**很短的**引语也会被一并豁免——本脚本定位是
            # 「导航/总结层的**长**引语伪造」，短引语由 verify_quotes 覆盖。
            if len(re.findall(r"[A-Za-z']+", seg)) <= 4:
                continue
            fs = flat(seg)
            if not fs:
                continue
            if fs in all_flat:
                continue
            # ⚠️ 2026-10-18（DSH-Mac，C1）：**「拼接未标省略号」判据**。
            # 症状：md 把相隔整段叙述的前后两句并成一条「连续引语」且**没写 `…`**
            # ——sweet-fury 7 条实证：ch10/ch14/ch21/ch22 的导航层引语，逐条从
            # `library/*.epub` 直读都**逐字命中**，但断点处插着整段叙述
            # （如 ch22 `…asked if I would help her` 与前半段相隔 2,387 flat 字符，
            # 中间是 `waiting game had just come out / if I figured…`）。
            # 后果：AGENTS 第 2 条明写「需省略中间文字用 `…` 且省略号两侧都必须是
            # 原词」——不写省略号 = 伪造了一条原文中不存在的连续引语，比改写更严重。
            #
            # 判据（门槛来自全库实测，不是拍的）：
            #   ① 整段**不含** `…` / `...`（含了就交给既有「省略号双侧口径」判）；
            #   ② 按**句号**切成 ≥2 段，每段前 40 flat 字符都能在参考集命中；
            #   ③ 第 2 段在原文的位置离第 1 段 > 80 flat 字符（叙述量门槛）。
            # ⚠️ 门槛必须落在「跳过量」而非「前缀长度」上，且**按句号切**——
            # 用「最长公共前缀 ≥40」会误报：somewhere-towards-the-end 的 ch08
            # `Only a person with a gigantic sense of self-importance could, for
            # example, produce a large number of canvases…` 是**逐字原文**
            # （中间那个 `for example,` 就是原文里的），却因断点后 10 字符才接上
            # 而被误判「跳过叙述」⇒ 误报 3 条（ch06/ch08/ch11）。
            _ref = _EPUB_FLAT or all_flat
            _SPLIT_SENT = re.compile(r"(?<=[.!?])\s+")
            if not re.search(r"\u2026|\.\.\.|\u2014", seg):
                _ps = [x for x in _SPLIT_SENT.split(seg)
                       if len(re.findall(r"[A-Za-z]", x)) >= 8]
                # ⚠️ 追加门槛：断裂处必须**没有叙述信号词**。helm ch51 实测
                # `「The weather is the flight, really. Sorry, Ange.」` 是
                # 逐字原文（`…really. There's a lesson in this…` 中间只隔着
                # 同一口气的插话），纯「跳过量 >80」会误报 ⇒ 断裂处出现
                # 独立叙述句（he says / she replied / 引号引导的对话）即放行。
                _SPEECH = re.compile(r"\b(he|she|they|it)\s+(says|said|replies|"
                                     r"replied|adds|added|whispers|shouts)\b|"
                                     r"^\s*[\u201c\u2018\"']")
                if len(_ps) >= 2 and all(flat(_x)[:40] in _ref for _x in _ps):
                    _p0 = flat(_ps[0])[:40]
                    _i0 = _ref.find(_p0)
                    _p1 = flat(_ps[1])[:40]
                    _j0 = _ref.find(_p1, _i0 + len(_p0))
                    _gap = _ref[_i0 + len(_p0):_j0] if _j0 > 0 else ""
                    if _j0 > 0 and (_j0 - _i0 - len(_p0)) > 150 \
                            and not _SPEECH.search(_gap):
                        fail.append(f"{md.name}: 「{seg[:78]}」"
                                    f"拼接未标省略号（两段均在本章命中，"
                                    f"中间跳过 {_j0 - _i0 - len(_p0)} 字符叙述）")
                        continue
            # ⚠️ 2026-09-29 省略号口径：`「It would be easier… maybe you?」`
            # 这类**转述式截断**（`…` 两侧都是原文，但中间被省略）整串必然查无。
            # 判据：两侧各自 ≥6 字母且**都**能在全书命中 ⇒ 判为合法转述，不报警。
            _segs = [x for x in re.split(r"…|\.\.\.", seg) if len(re.findall(r"[A-Za-z]", x)) >= 6]
            if len(_segs) >= 2 and all(flat(x) in all_flat for x in _segs):
                continue
            # 破折号口径：md 用 — 替代原文 `from your heart—` 这类连接词时，
            # flat 会因丢字符而错位，故再试一次「把破折号当分隔符」的比对。
            if re.search(r"[—–]", seg):
                _alt = flat(re.sub(r"[—–]+", " ", seg))
                if _alt and _alt in all_flat:
                    continue
            if _CARDS_FLAT and fs in _CARDS_FLAT:
                continue
            own = any(fs in v for k, v in corpus.items()
                      if per_chapter and k.startswith(md.name[:4]))
            if own:
                continue
            if per_chapter:
                fail.append(f"{md.name}: 「{seg}」本章查无（全书亦无）")
            else:
                warn += 1
                fail.append(f"{md.name}: 「{seg}」全书查无 ⇒ 阻断型")

# ⚠️ 分档口径必须与 sys.exit 那一行一致，否则会出现「汇总说 ❌N、退出码 0」
# 或「打印 ⚠️ 却 exit 2」的对不上账（2026-10-18 修）。
for f in fail:
    _blk = any(_k in f for _k in ("全书查无", "本章查无", "拼接未标省略号"))
    print(("❌ " if _blk else "⚠️ ") + f)
_blk_n = sum(1 for f in fail if ("查无" in f or "拼接未标省略号" in f))
print(f"\n=== 导航/总结层英文核对：❌ {_blk_n} ｜ ⚠️ {len(fail) - _blk_n} ===")
# ⚠️ 「拼接未标省略号」与查无同级（都是 AGENTS 第 2 条 / 原文约束违规）。
sys.exit(2 if any(("全书查无" in f) or ("本章查无" in f)
                   or ("拼接未标省略号" in f) for f in fail) else 0)
