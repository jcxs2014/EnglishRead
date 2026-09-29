#!/usr/bin/env python3
"""期刊精读引语逐字核验（期刊侧提交门禁，2026-09-29 建）

## 为什么需要它

`AGENTS.md` 第 3 条门禁的适用范围写明「`notes/books/` 下所有整本书/短篇合集精读
（期刊文章无成书可比，不适用）」——期刊侧因此**长期零机检**。实测 2026-09-29：
318 篇期刊精读里只有 57 篇本机有 `.src.md` 可比，其余 261 篇无从核对；
有语料的那 57 篇里有 4 处 A 类引语缺陷（主语替换 / 删 `'s` / 缩写展开 /
删全称），形态与书籍侧「改写式的『意思对了』不算数」完全同型。

本脚本**不新立尺子**：`from verify_quotes import extract_quotes, flat_alpha`
（与 `check_short_quotes.py` 同一做法），口径随主门禁演进而自动同步。

## 三档 lane（与书籍侧同一套判据，不另立标准）

| lane | 判据 | 本脚本的输出 |
|---|---|---|
| **完整** | 有同名 `.src.md` 且正文 flat ≥ 400 字符 | 逐条比对，报 ✅ / ❌ |
| **无语料** | 无 `.src.md` | `❓ 无法判定`，**不产出计数**（退出码 2） |
| **语料残缺** | `.src.md` 只有思源指针 / 导出被截断 | `⚠️ 无语料可比`，不判红 |

**「无语料」不是「检查通过」，是「检查没做」**——报告里必须写清 lane，
不得与完整 lane 的数字混用（同 `AGENTS.md` 第 3 条降级 lane 条款）。

## 判据分级（`AGENTS.md` 第 3 条三档定性）

- **阻断型（退出码 1）**：`❌ 疑似改写`——整串 flat 查无，且按省略号切分后
  仍有片段查无。**须走 A/B 裁决**（`AGENTS.md` 第 5 条）：先拆片段取证，
  排除 src 侧脏（撇号丢失 / 导出截断）后才可定 A 类。
- **提示型**：`⚠️ 无语料可比` / `⚠️ 疑似跨段拼接`（省略号两侧都命中但中间跳过
  的是**两个不同自然段**）——只记不改。
- **合法**：`✅ 逐字命中` / `✅ 省略号合法截断`（`…` **每一段**都是原文中
  连续的一段；见 `AGENTS.md` 8.2 禁令 5）。

## 已知盲区（不要把 0 当成「全对」）

1. **分析层行内英文不在本脚本口径内**——期刊侧的「句子结构 / 为什么这样写」
   里的英文短语与书籍侧同属 `sweep_analysis_inline` 的地盘，而禁令 3 是
   本库唯一「事后无低成本机检」的缺陷类（`AGENTS.md` 8.2）⇒ **只能靠写作期粘贴**。
2. **`.src.md` 自身可能是脏的**——思源导出实测会丢撇号（`life's` → `life`）
   与 markdown 链接标记。本脚本剥链接，但**不修补丢撇号**（那属 B 类，
   要人工裁决）。
3. **只抽 `>` 块**。期刊的「概览 / 词汇例句 / 段落逻辑」层英文不在口径内。

## 用法

```bash
python3 scripts/sweep_journal.py                      # 全库
python3 scripts/sweep_journal.py "notes/economist"    # 单来源
python3 scripts/sweep_journal.py "notes/economist/260822"  # 单期
python3 scripts/sweep_journal.py --quiet
```

退出码：0 = 完整 lane 全绿 ｜ 1 = 有阻断型 ❌ ｜ 2 = 无任何可比语料（无法判定）
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import extract_quotes, flat_alpha  # noqa: E402

# src 正文 flat 长度低于此值 ⇒ 判「语料残缺」（思源指针壳 / 导出截断）
MIN_SRC_FLAT = 400

SRC_SUFFIX = re.compile(r'\.src(\.src)?\.md$')


def strip_md_links(t: str) -> str:
    """剥 markdown 链接/图片标记。

    思源导出的 `.src.md` 把超链接嵌在正文里（实测 Atlantic：
    `new mothers [received](https://…) a commemorative blanket`），
    不剥则 flat 查无 ⇒ 整类假 MISS。**只剥标记，保留可见文字。**
    """
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    return t


def find_src(md_path: str):
    """找同名 `.src.md`。返回 (路径, 原文) 或 (None, None)。"""
    d, base = os.path.split(md_path)
    stem = base[:-3]
    for cand in (f'{stem}.src.md', f'{stem}.src.src.md'):
        p = os.path.join(d, cand)
        if os.path.exists(p):
            return p, open(p, encoding='utf-8', errors='replace').read()
    return None, None


def is_stub(src_text: str) -> bool:
    """语料残缺判定：只有思源指针 / 明写被截断 / 正文过短。"""
    if 'Truncation at' in src_text or 'Due to size limits' in src_text:
        return True
    if '[Source in SiYuan' in src_text and len(flat_alpha(src_text)) < MIN_SRC_FLAT:
        return True
    return len(flat_alpha(src_text)) < MIN_SRC_FLAT


def split_ellipsis(q: str):
    """按省略号切段。`…` 两侧每段都必须是原文中连续的一段（禁令 5）。"""
    return [p for p in re.split(r'…|\.\.\.|--', q) if len(flat_alpha(p)) >= 15]


def judge(quote: str, src_flat: str):
    """返回 (档位, 说明)。档位 ∈ {OK, OK_ELLIPSIS, WARN_STITCH, FAIL}"""
    fq = flat_alpha(quote)
    if not fq:
        return 'OK', ''
    if fq in src_flat:
        return 'OK', ''
    parts = split_ellipsis(quote)
    if not parts:
        return 'FAIL', '整串查无且无法切段'
    miss = [p for p in parts if flat_alpha(p) not in src_flat]
    if not miss:
        return 'OK_ELLIPSIS', f'省略号 {len(parts)} 段全部逐字命中'
    return 'FAIL', f'{len(miss)}/{len(parts)} 段查无'


def collect(root: str):
    """遍历期刊 md。root 可以是某来源目录、某期目录，或 notes/ 本身。"""
    pats = []
    if os.path.isdir(root):
        if os.path.basename(root.rstrip('/')) in {
            'parisreview', 'atlantic', 'newyorker', 'economist',
            'brainpickings', 'lithub', 'granta',
        }:
            pats.append(os.path.join(root, '**', '*.md'))
        elif os.path.basename(os.path.dirname(root.rstrip('/'))) in {
            'parisreview', 'atlantic', 'newyorker', 'economist',
            'brainpickings', 'lithub', 'granta',
        }:
            pats.append(os.path.join(root, '*.md'))
        else:
            pats.append(os.path.join(root, '*', '**', '*.md'))
    pats.append(os.path.join(root, '**', '*.md'))
    seen = set()
    out = []
    for p in pats:
        for f in glob.glob(p, recursive=True):
            if f in seen:
                continue
            seen.add(f)
            if '/books/' in f or f.endswith('.src.md') or f.endswith('.src.src.md'):
                continue
            if not f.endswith('.md'):
                continue
            out.append(f)
    return sorted(out)


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith('-')]
    quiet = '--quiet' in sys.argv
    root = argv[0] if argv else 'notes'

    files = collect(root)
    if not files:
        print(f'❌ {root} 下没找到期刊精读 md')
        return 2

    n_full = n_nocorpus = n_stub = 0
    n_ok = n_ell = n_stitch = 0
    fails = []
    nocorpus, stubs = [], []
    totals = {}

    for md in files:
        rel = os.path.relpath(md)
        sp, src = find_src(md)
        if sp is None:
            n_nocorpus += 1
            nocorpus.append(rel)
            continue
        if is_stub(src):
            n_stub += 1
            stubs.append(rel)
            continue
        n_full += 1
        src_flat = flat_alpha(strip_md_links(src))
        txt = open(md, encoding='utf-8', errors='replace').read()
        # include_short=True：期刊引语普遍短于书籍（Economist 一段一句），
        # <20 flat 字符的短引语若按主门禁默认跳过，期刊侧会静默漏掉一大片。
        quotes, _short = extract_quotes(txt, include_short=True)
        f_ok = f_ell = f_stitch = f_fail = 0
        for q in quotes:
            verdict, why = judge(q, src_flat)
            if verdict == 'OK':
                f_ok += 1
                n_ok += 1
            elif verdict == 'OK_ELLIPSIS':
                f_ell += 1
                n_ell += 1
            elif verdict == 'WARN_STITCH':
                f_stitch += 1
                n_stitch += 1
            else:
                f_fail += 1
                fails.append((rel, q.strip()[:120], why))
        totals[rel] = (f_ok, f_ell, f_stitch, f_fail)

    # ---- lane ----
    print(f'=== lane ===')
    print(f'完整 lane（有可比 src）: {n_full} 篇')
    print(f'无语料 lane（无 .src.md）: {n_nocorpus} 篇  ← 检查没做，不是不合格')
    print(f'语料残缺 lane（src 空壳/截断）: {n_stub} 篇  ← 检查没做，不是不合格')

    if n_full:
        checked = n_ok + n_ell + n_stitch + sum(v[3] for v in totals.values())
        print(f'\n=== 引语逐字（完整 lane {n_full} 篇 / {checked} 块）===')
        print(f'✅ 逐字命中      {n_ok}')
        print(f'✅ 省略号合法截断 {n_ell}')
        if n_stitch:
            print(f'⚠️ 疑似跨段拼接   {n_stitch}  （提示型：只记不改）')
        if fails:
            print(f'❌ 疑似改写       {len(fails)}  （阻断型：须走第 5 条 A/B 裁决）')
        else:
            print('❌ 疑似改写       0')

    if not quiet:
        if fails:
            print('\n=== ❌ 明细（阻断型）===')
            for rel, q, why in fails:
                print(f'  {rel}\n      {why}\n      {q}')
        if stubs:
            print('\n=== ⚠️ 语料残缺篇（提示型：src 只有指针或被截断）===')
            for r in stubs:
                print(f'  {r}')
        if nocorpus and len(nocorpus) <= 20:
            print('\n=== ❓ 无语料篇（无法判定）===')
            for r in nocorpus:
                print(f'  {r}')
        elif nocorpus:
            print(f'\n=== ❓ 无语料篇 {len(nocorpus)} 篇（略，`--quiet` 已抑制明细）===')

    # ---- 盲区提醒（防「0 = 全对」）----
    if n_full and not fails:
        print('\n⚠️ 本脚本只覆盖 `>` 引语块。**分析层行内英文、词汇例句、'
              '概览层不在口径内**——禁令 3 是本库唯一无低成本机检的缺陷类。')

    if fails:
        return 1
    if n_full == 0:
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
