#!/usr/bin/env python3
"""
check_entities.py — 故事梗概实体一致性检测

用法：
  python3 scripts/check_entities.py "<书目录>"

检查（对应根 AGENTS.md 核验规则第 4 条）：
  抽取每篇 "## 故事梗概" 段中的英文专名序列（人名/地名），逐一验证其
  存在于该书语料（text/*.txt 或 epub 展平全文）——抓《Lance》式整段
  情节编造、《Spring in Fialta》把 Nina 写成 Helena 的张冠李戴。

白名单：作者行、书名行、常见英文虚词/称谓、(可选) 书目录 whitelist.txt。
局限（诚实声明）：只能抓实体级硬伤，抓不了"人物对但事件编造"，那部分靠人工抽检。
退出码：存在 fail 则 1；**抽 0 个梗概段则 2（❓ 无法判定），不是 0**。

⚠️ 2026-10-18 堵「真空绿」：本工具此前在**一个梗概段都没抽到时照样打印
「0 个文件存在未知实体」并 exit 0** —— 报告读起来是「核过了、干净」，
实际是**一节都没进扫描集**（静默跳过型假绿 = AGENTS 三档分类缺的第四档）。
全库实测 487 个书目录中 **108 本抽 0 段**：non-fiction 65 / short-story-antheses 30 /
novels 10 / mystery-thriller 3。根因是口径只认 4 个 H2 标题
（`故事梗概|本章导航|本篇导航|梗概`），而库里主流形态是 **`概览`（1,962 处）**、
`全书梗概`（313）、`论证结构`（1,150，非虚构专用），另有 30 本短篇合集用
`概览` + `一句话总结` 体例。
  ⇒ 现改为 exit 2 + 「❓ 无法判定」并列出该书实际出现的 H2 标题（与
    `verify_quotes` 无 epub 时「退出码 2 + ❓ 无法判定，不产出计数」同口径）。
⚠️ 同日实测过「扩口径到 概览/全书梗概」并**否决**：0→真空绿的书可从 108 降到 15，
但报错文件数从 **232 涨到 969**（95 本由绿转红），新增报错大量是设计外的噪声——
`we-the-people` 报 `ISBN`/`Liveright Publishing Corporation`/`Norton`、
`black-is-the-body` 报 `ISBN`/`Borzoi Books`、`stet-an-editors-life` 报
`Grove Press`/`Granta Publications`。本工具的设计目的是抽**故事人名地名**，
出版信息不在其内 ⇒ 扩口径须先做一轮噪声剔除，**不与「堵真空绿」混做**。

⚠️ **2026-10-18 补第二个跳过型假绿：语料层不存在**。`load_corpus()` 在既无
`text/*.txt` 又无 `library/*.epub` 时返回**空串** ⇒ 「实体不在语料里」对**每一个**
实体都成立 ⇒ 全部报成未知实体。样本（`--wide` 回归撞出，四本均无 `text/` 也无 epub）：
`why-nothing-works-by-marc-dunkelman`（报 `Gallup`/`Warren Burger`）·
`letters-to-a-friend-by-diana-athill`（`DECUARY`）·
`dont-make-me-laugh-by-julia-raeside`（`Peters`）·
`in-a-rush-by-kate-canterbary`（`Contemporary Romance`）。
**在无真值时判「未知」是不出结论** ⇒ 与「抽 0 段」同口径：exit 2 + ❓ 无法判定。
⚠️ **我踩的坑（留作取证反面）**：撞出这个形态时我先断言上面四本「均无 `text/` 也无 epub」，
复核发现**全错**——它们分别有 10 / 18 / 40 / 43 个 `text/*.txt`（68 万 / 48 万 / 70 万 / 48 万字符），
错因是我用单一路径 `notes*/books/*/<slug>` 找书，而**体裁目录名不统一**
（`short-story-anthologies` vs `short-story-antheses`）、且书在 `notes/` 与 `notes1/` 下的归属不同。
⇒ **任何「某书没有 X」的全库统计，先把命中路径打出来看**——路径写错时结论会整体反向。
（顺带暴露第二个形态：`ENT_PAT` 允许连字符，于是中文的「Giles 与 Layla」被粘成
伪专名 `Giles-Layla`——这类假红已在 `--wide` 说明里标注为已知缺口。）

⚠️ **2026-10-18 补：噪声剔除已做完，做成 `--wide`（仍非默认）**
用法：`python3 scripts/check_entities.py "<书目录>" --wide`。
剔除不是靠词表硬剔，而是**行级剔书目元信息行**（`META_LINE`）——
因为实测最大一档（`来源/栏目：…（Contemporary Romance）`）是行内括注形态，
任何词表都会漏掉它。量化（483 本有 `text/` 的书、`概览` 节正文 47,637 行）：
- 元信息行 **5,544 行 = 11.6%**；剔掉后新增实体 **1,903 次 → 122 次**
  （作者/书名 990→3 · 出版信息 177→2 · 分部标签 126→11），涉及 **28 本**书。
- 残余 top：`contemporary romance` 38（`来源/栏目` 括注变体，见 META_LINE 已知缺口）·
  `andre deutsch`/`yaakov katz`/`cecil rhodes` 各 2（真人物名，值得看）·
  365-days 的 `higher standards`/`taking small steps` 等 20 条（书内概念短语，非专名）·
  `percy shelley`/`andrew bolkonsky`（引文内专名，真值命中但格式差异）。
**为什么不做成默认**：它会改判定口径（全库报错文件数会变），属「新增检查项」，
与 AGENTS 第 8 条「先问生产方式」同向，须用户单独裁决；`--wide` 只做取证。
"""
import re, sys, glob, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import flat_alpha, epub_flat_text

STOP = set("""The A An But And However Yes No Oh Ah His Her She He They Them What Why When Where How It In On At
For With Dear One Some Every Each Not So Then Now There This That These Those My Your Our Mr Mrs Dr Miss Sir
Madam Saint Lord Lady Captain Colonel General Professor Chapter Part Book Story God Jesus Christ Christmas
Easter Sunday Monday Tuesday Wednesday Thursday Friday Saturday January February March April May June July
August September October November December English Russian French German Spanish Italian Greek Latin Chinese
Japanese American British Irish Scottish Swedish Dutch Polish Portuguese Turkish Arabic Persian Hindu New Old
Great Little Good Bad True False First Second Third Last Next Every Other Same Another Such Many Much More Most
Less Least Very Quite Just Still Already Yet Even Only Ever Never Always Often Sometimes Here Now Today Tonight
Tomorrow Yesterday Yesterday Well Well Perhaps Maybe Surely Really Honest
Tropes POV
# 2026-10-21：本书十二个分部的标题是全大写（SATURDAY / SUNDAY / MONDAY / TUESDAY /
# WEDNESDAY / THURSDAY / FRIDAY），精读导航要按书里的原样引用；其中 TUESDAY 全书正文
# 从未出现（只在 epub 的分部页上），于是「词在书里」这条兜底失效、被判成未知实体。
# ⇒ 把分部标题的全大写形态一并收进 STOP（属工具口径，不是 md 缺陷）。
SUNDAY MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY
Brian-Mimi Mimi-Brian""".split())

ENT_PAT = re.compile(r"[A-Z][A-Za-z''\-]+(?:\s+[A-Z][A-Za-z''\-]+){0,3}")

# ⚠️ 2026-09-26 新增：题材/类型装饰词。`## 本章导航` 的「Tropes 兑现/反转」
# 字段大量使用英文类型词（`Fated Partners` / `Forbidden` / `Doomed Love` …），
# 它们是**类型名不是实体**，原实现一律当实体查语料 → 全库 411 次报警里
# 大头是这类。实测 that-first-flight 的 `Happy Beginning` 同理。
# 判据：**多词实体的每个词都是装饰词**才跳过；含任何非装饰词仍照常判
# （故 `Snowflower Suite`、`Andie-John` 这类真名不受影响）。
# ⚠️ 本集合在定义处**统一小写化**——比对方用的也是小写词（`words_low`）。
#    第一版按首字母大写书写，导致 `Fated Partners` / `Forbidden` 等
#    **一个都没被跳过**：大小写不一致在集合查找里是静默失效，不报错。
DECORATIVE_RAW = """Tropes Trope Tropus POV Partners Fated Forbidden Resolution Confrontation
Throuple Aftermath Explicit Damsel Villain Motivation Survivor Friendship Deception Flashback
Identity Reconciliation Mutual Pregnancy Brainwashing Gothic Sensory Backstory Love Romance
Tragedy Comedy Drama Action Suspense Mystery Horror Thriller Falling Rising Climb Return
Journey Transformation Breakthrough Moment Truth Lie Lies Secret Promise Hope Fear Home
Family Friend Enemies Rival Rivalry Redemption Revenge Betrayal Loss Grief Healing Recovery
Beginning Ending Start Change Turn Twist Climax Fall Rise Second First Third New Old
Break Breakup Comeup Face-off Standalone Spinoff Series Book Novel Tale Story Chapter
Enemies-to-Lovers Friends-to-Lovers Second Chance Age Gap Arranged Marriage Contract
Secret Baby Forbidden Love Dirty Late-night One-night Stand-alone Unrequited Instalust
Sibling Rival Parent Child Mother Father Son Daughter Brother Sister Husband Wife
Happy Beginning Ending Homecoming Revelation Rejection Bargain Bargaining Consequences Faustian
Doomed Temporary Separation PTSD Grief Ache Anguish Elation Serenity Chaos
"""
DECORATIVE = {w.lower() for w in DECORATIVE_RAW.split()}

def load_corpus(book_dir):
    texts = sorted(glob.glob(os.path.join(book_dir, 'text', '*.txt')))
    if texts:
        return flat_alpha(''.join(open(p, encoding='utf-8', errors='ignore').read() for p in texts))
    epubs = glob.glob(os.path.join(book_dir, 'library', '*.epub'))
    return flat_alpha(epub_flat_text(epubs[0])) if epubs else ''

def whitelist(book_dir):
    wl = os.path.join(book_dir, 'whitelist.txt')
    extra = set()
    if os.path.exists(wl):
        for l in open(wl, encoding='utf-8'):
            l = l.strip()
            if l and not l.startswith('#'):
                extra.add(flat_alpha(l)); extra.add(l)
    return extra

def extract_synopses(txt, wide=False):
    """返回 [(章节号, 梗概段文本)]——兼容 故事梗概 / 本章导航 / 本篇导航 三类标题。

    ⚠️ 2026-09-27 五步审查（Real Life Butala）新增 `本篇导航`：短篇合集与部分
    一次一佳作书用 `## 本篇导航`，此前不在口径内 ⇒ `check_entities` 对这批文件
    **抽出 0 个梗概段却照报「0 个文件存在未知实体」**（真空绿）。全库实测：
    `## 本篇导航` 32 个文件 / 3 本书（Best British Short Stories 2023、
    real-life-short-stories-2002-anthology、the-passing-of-the-dragon-by-ken-liu），
    而 `## 本章导航` 7589 个文件 —— 即本条口径漏掉的是少数派书型，但漏掉时
    门禁**静默通过**，比报错更危险。

    ⚠️ 2026-10-18 复核（这条坑又以另一种形态复发）：同族漏收已发生过两次
    （`本篇导航` / `## 节点N` 形态），本函数的口径**至今仍只有这 4 个标题**，
    而库里主流形态是 `概览`（1,722 处）与 `全书梗概`（313 处）⇒ 108 本书
    抽 0 段。**处置：默认口径不扩**（扩了会引入 ISBN/出版社噪声，见文件头
    2026-10-18 记录），改为抽 0 段时 exit 2「❓ 无法判定」，由 `check_book`
    返回段数、`main` 据此分流。
    **扩口径已做成 `--wide`（非默认，取证用）**：加 `概览/论证结构/…` 并**行级剔书目
    元信息行**，噪声 1,903 次 → 122 次。**是否转默认待用户裁决**（改判定口径＝新增
    检查项）。

    ⚠️ 2026-10-18 投毒抓出、**已修**：相邻两个梗概层标题会**静默丢弃上一节**——
    「遇到新梗概标题」这条分支无条件 `buf = []; continue`，上一节永远走不到 append。
    该缺陷早于 `--wide`，但默认口径下 `故事梗概`/`本章导航` 紧邻罕见；
    `--wide` 收进 `概览`(1,722)/`论证结构`(1,133) 后，「概览后紧跟论证结构」成常态。
    **教训：`--wide` 这类「扩大扫描集」的改动，必须配一次投毒测试**——
    扩大扫描集最可能的失败形态不是「多报错」，而是「看似收进来了其实没收到」。
    """
    out = []
    cur_num, buf, in_syn = None, [], False
    num_pat = re.compile(r'^#+\s*(\d+[\.\s]|Prologue|Epilogue)', re.I)
    syn_pat = re.compile(r'^##\s*(故事梗概|本章导航|本篇导航|梗概)')
    # ⚠️ 2026-10-18 `--wide`：非虚构书的梗概层标题是 `概览`/`论证结构`
    # （1,722 + 1,133 处），短篇合集也用 `概览`。默认**不收**（见文件头）。
    syn_pat_wide = re.compile(
        r'^##\s*(故事梗概|本章导航|本篇导航|梗概|概览|论证结构'
        r'|本章概览|全书梗概|内容概览|章节概览|本篇概览|论证脉络)')
    # ⚠️ 书目元信息行——**行级剔除**，不靠词表（见文件头量化）。这些标签在 md 里
    # 常被 `**` 包裹（`- **作者**：X`）或带中文冒号，故两处标点都收。
    META_LINE = re.compile(
        r'^\s*[-*]?\s*\**\s*(?:出处|作者|来源|栏目|来源栏目|字数|字符数'
        r'|篇目|篇目来源|原文出处|章节定位|体裁|文本体裁|书籍信息|出版信息'
        r'|系列)\s*\**\s*[:：/]')
    head_pat = re.compile(r'^##\s')
    for line in txt.splitlines():
        hm = head_pat.match(line.strip())
        nm = num_pat.match(line.strip())
        if nm and not line.strip().startswith('#'):
            pass
        if num_pat.match(line.strip()) and line.strip().startswith('#'):
            cur_num = line.strip().lstrip('#').strip()[:24]
        if (syn_pat_wide if wide else syn_pat).match(line.strip()):
            # ⚠️ 2026-10-18 修：相邻两个梗概层标题会**静默丢弃上一节**。
            # 原实现无条件 `buf = []; continue`，上一节永远走不到下面的 append。
            # 投毒实证：`## 概览` 下插虚构实体行，`--wide` 跑出该节**未进扫描集**。
            # 库内 `概览`(1,722) 紧跟 `论证结构`(1,133) 是常态 ⇒ `--wide` 下高发。
            if in_syn and buf:
                out.append((cur_num or '?', ' '.join(buf)))
            in_syn = True; buf = []; continue
        if in_syn:
            if head_pat.match(line.strip()):
                out.append((cur_num or '?', ' '.join(buf)))
                in_syn = False; buf = []
            elif META_LINE.match(line):
                continue          # ⚠️ 剔书目元信息行（见上）
            else:
                buf.append(line)
    if in_syn and buf:
        out.append((cur_num or '?', ' '.join(buf)))
    return out

def check_book(book_dir, wide=False):
    corpus = load_corpus(book_dir)
    wl = whitelist(book_dir)
    fails, checked = [], 0
    seg_total, h2 = 0, {}
    corpus_len = len(corpus)
    h2_pat = re.compile(r'^##\s+(.*?)\s*$')
    for f in sorted(glob.glob(os.path.join(book_dir, '*.md'))):
        name = os.path.basename(f)
        txt = open(f, encoding='utf-8').read()
        for ln in txt.splitlines():
            hm2 = h2_pat.match(ln.strip())
            if hm2:
                h2[hm2.group(1)[:24]] = h2.get(hm2.group(1)[:24], 0) + 1
        mauthor = re.search(r'\*\*作者\*\*[:：](.+)', txt) or re.search(r'来源[:：](.+)', txt)
        author_str = flat_alpha(mauthor.group(1)) if mauthor else ''
        unknown = []
        seen_in_file = set()
        segs = extract_synopses(txt, wide=wide)
        seg_total += len(segs)
        for _, syn in segs:
            for ent_m in ENT_PAT.finditer(syn):
                ent_raw = ent_m.group(0).strip()
                # 2026-10-23：人名所有格归一（`Annette's` → `Annette`）。
                # 不归一 ⇒ flat 成 `annettes`，在语料里查无，把真人物报成未知实体
                # （the-art-of-a-lie ch18 实证：Annette 在 text/ch18 出现 4 次）。
                ent = re.sub(r"['’]s$", "", ent_raw)
                key = flat_alpha(ent)
                if len(key) < 4 or ent in STOP:
                    continue
                words_raw = ent.split()
                # ⚠️ 两个比较空间必须分开（本实现第一版就栽在这里）：
                #    corpus / wl 存的是 **flat 小写**键；STOP / DECORATIVE 存的是
                #    **原形小写**词。拿原始大小写的词去查 flat 语料恒不成立，
                #    新判据会全部失效且看不出异常——静默失效比报错更坏。
                words_flat = [flat_alpha(w) for w in words_raw]
                words_low = [w.lower() for w in words_raw]
                # (1) 逐词放过：命中 flat 语料/白名单，或该词本身是虚词/装饰词
                #     ⚠️ 三个比较空间各不相同，混用就会**静默失效**：
                #       corpus / wl  → flat 全小写键（`flat_alpha`）
                #       STOP          → **首字母大写**（`POV` / `The` / `Story`）
                #       DECORATIVE    → 全小写（本文件内定义）
                #     ⚠️ 循环变量**不可**叫 `wl`——外层 `wl` 是白名单集合，
                #     一旦遮蔽，`wf in wl` 就变成 `'bailey' in 'bailey'` 恒真，
                #     **所有单词实体一律放过**，工具的核心能力（抓人名张冠李戴）
                #     被静默关闭。本实现第一版就栽在这里（`check_entities` 的 `wl`
                #     与 `verify_quotes` 的 `bad` 是同一类错，一天内两次）。
                if all(wf in corpus or wf in wl or wraw in STOP or wlow in DECORATIVE
                       for wf, wraw, wlow in zip(words_flat, words_raw, words_low)):
                    continue
                # (2) 纯装饰词组成的类型名（`Fated Partners` / `Doomed Love`）
                if all(wlow in DECORATIVE for wlow in words_low):
                    continue
                # (3) 作者名（`Olivie Blake` 之类）
                if key[:30] in author_str or ent in author_str:
                    continue
                # (4) 原判定保留
                if all(wf in corpus or wf in wl for wf in words_flat):
                    continue
                sig = f"{name}:{ent}"
                if sig in seen_in_file: continue
                seen_in_file.add(sig)
                if (key[:30] not in corpus and key[:30] not in author_str and key not in wl):
                    unknown.append(ent_raw)
                    checked += 1
        if unknown:
            fails.append((name, sorted(set(unknown))))
    return {'fails': fails, 'seg_total': seg_total, 'h2': h2,
            'corpus_len': corpus_len}

def main():
    book_dir = sys.argv[1]
    # `--wide`：额外收 `概览/论证结构/…` 这类非虚构梗概层标题（剔书目元信息行）。
    # ⚠️ **非默认**：它会改判定口径（全库报错文件数会变），取证用，须用户裁决。
    wide = '--wide' in sys.argv[2:]
    r = check_book(book_dir, wide=wide)
    tag = '（宽口径 --wide）' if wide else ''
    print(f"=== 实体一致性检测：{r['seg_total']} 个梗概段 / "
          f"{len(r['fails'])} 个文件存在未知实体{tag} ===")
    for name, ents in r['fails']:
        print(f"  ❌ {name}: {', '.join(ents)}")
    # ⚠️ 2026-10-18：抽 0 段**不是通过**。此前这里照打「0 个文件存在未知实体」
    # 并 exit 0，报告读起来是「核过了、实体层干净」，实际一节都没进扫描集
    # （静默跳过型假绿，第四档）。现与 `verify_quotes` 无 epub 时同口径：
    # **退出码 2 + ❓ 无法判定 + 不产出「0 未知实体」这个结论**。
    if r['corpus_len'] == 0:
        print('  ⚠️ 本书既无 `text/*.txt` 也无 `library/*.epub` ⇒ **语料层不存在**。')
        print('  ❓ 无法判定：没有真值可比，任何实体都会被报成「未知」——'
              '本层**未被核对**（不是「干净」）')
        print('  · 修法：补 `text/` 提取件（见 AGENTS 第 1 条原文先行），'
              '或把 `library/*.epub` 放回本书目录。')
        sys.exit(2)
    if r['seg_total'] == 0:
        top = sorted(r['h2'].items(), key=lambda kv: -kv[1])[:8]
        if top:
            print('  · 本书实际出现的 H2 标题（计数）：'
                  + '、'.join(f'{t}×{n}' for t, n in top))
        print('  ⚠️ 口径只认 H2「故事梗概 / 本章导航 / 本篇导航 / 梗概」；'
              '非虚构常用「概览 / 全书梗概 / 论证结构」，短篇合集常用「概览」'
              '——**都不在本工具口径内**。')
        print('  ❓ 无法判定：0 个梗概段进扫描集，实体层**未被核对**（不是「干净」）')
        sys.exit(2)
    sys.exit(1 if r['fails'] else 0)

if __name__ == "__main__":
    main()
