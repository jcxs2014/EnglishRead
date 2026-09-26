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
退出码：存在 fail 则非 0。
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
    """返回 [(章节号, 梗概段文本)]——兼容 故事梗概 / 本章导航 两类标题。"""
    out = []
    cur_num, buf, in_syn = None, [], False
    num_pat = re.compile(r'^#+\s*(\d+[\.\s]|Prologue|Epilogue)', re.I)
    syn_pat = re.compile(r'^##\s*(故事梗概|本章导航|梗概)')
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
    for f in sorted(glob.glob(os.path.join(book_dir, '*.md'))):
        name = os.path.basename(f)
        txt = open(f, encoding='utf-8').read()
        mauthor = re.search(r'\*\*作者\*\*[:：](.+)', txt) or re.search(r'来源[:：](.+)', txt)
        author_str = flat_alpha(mauthor.group(1)) if mauthor else ''
        unknown = []
        seen_in_file = set()
        for _, syn in extract_synopses(txt):
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
    return {'fails': fails}

def main():
    book_dir = sys.argv[1]
    r = check_book(book_dir)
    print(f"=== 实体一致性检测：{len(r['fails'])} 个文件存在未知实体 ===")
    for name, ents in r['fails']:
        print(f"  ❌ {name}: {', '.join(ents)}")
    sys.exit(1 if r['fails'] else 0)

if __name__ == "__main__":
    main()
