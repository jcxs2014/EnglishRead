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

def extract_synopses(txt):
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
    而库里主流形态是 `概览`（1,962 处）与 `全书梗概`（313 处）⇒ 108 本书
    抽 0 段。**处置：不扩口径（扩了会引入 ISBN/出版社噪声，见文件头 2026-10-18
    记录），改为抽 0 段时 exit 2「❓ 无法判定」**，由 `check_book` 返回段数、
    `main` 据此分流。扩口径这件事仍开着，须先做噪声剔除。
    """
    out = []
    cur_num, buf, in_syn = None, [], False
    num_pat = re.compile(r'^#+\s*(\d+[\.\s]|Prologue|Epilogue)', re.I)
    syn_pat = re.compile(r'^##\s*(故事梗概|本章导航|本篇导航|梗概)')
    head_pat = re.compile(r'^##\s')
    for line in txt.splitlines():
        hm = head_pat.match(line.strip())
        nm = num_pat.match(line.strip())
        if nm and not line.strip().startswith('#'):
            pass
        if num_pat.match(line.strip()) and line.strip().startswith('#'):
            cur_num = line.strip().lstrip('#').strip()[:24]
        if syn_pat.match(line.strip()):
            in_syn = True; buf = []; continue
        if in_syn:
            if head_pat.match(line.strip()):
                out.append((cur_num or '?', ' '.join(buf)))
                in_syn = False; buf = []
            else:
                buf.append(line)
    if in_syn and buf:
        out.append((cur_num or '?', ' '.join(buf)))
    return out

def check_book(book_dir):
    corpus = load_corpus(book_dir)
    wl = whitelist(book_dir)
    fails, checked = [], 0
    seg_total, h2 = 0, {}
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
        segs = extract_synopses(txt)
        seg_total += len(segs)
        for _, syn in segs:
            for ent_m in ENT_PAT.finditer(syn):
                ent = ent_m.group(0).strip()
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
                    unknown.append(ent)
                    checked += 1
        if unknown:
            fails.append((name, sorted(set(unknown))))
    return {'fails': fails, 'seg_total': seg_total, 'h2': h2}

def main():
    book_dir = sys.argv[1]
    r = check_book(book_dir)
    print(f"=== 实体一致性检测：{r['seg_total']} 个梗概段 / "
          f"{len(r['fails'])} 个文件存在未知实体 ===")
    for name, ents in r['fails']:
        print(f"  ❌ {name}: {', '.join(ents)}")
    # ⚠️ 2026-10-18：抽 0 段**不是通过**。此前这里照打「0 个文件存在未知实体」
    # 并 exit 0，报告读起来是「核过了、实体层干净」，实际一节都没进扫描集
    # （静默跳过型假绿，第四档）。现与 `verify_quotes` 无 epub 时同口径：
    # **退出码 2 + ❓ 无法判定 + 不产出「0 未知实体」这个结论**。
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
