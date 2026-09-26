#!/usr/bin/env python3
"""
corruption_scan.py — 编辑损坏扫描（方案 P1 第 8 个脚本）

为什么需要
----------
脚本化行编辑（正则批量替换）重跑在已替换的行上，会复制前缀或从句，
而**门禁只盯引语行**，这种损坏没人发现。本脚本按行扫 4 类损坏 +
1 类占位崩坏。

按实测证据分严重度（2026-09-26，全库 9817 个 md）
------------------------------------------------------
| 检查         | 全库命中 | 真阳率 | 处置 |
|--------------|---------|--------|------|
| U+FFFD       |  11 行  | 11/11  | **FAIL**（`压到他们头上��`、`婚���的终结`，无一例外） |
| 双句号 `。。` |   1 行  |  1/1   | **FAIL**（中文不用 `。。`；实测那行是 `派对。。` 机器人编辑残留） |
| 中文重复片段 |   8 处  | ~50%   | **只报告不判红**——见下 |
| 句中插入     |   0 处  | 无样本 | 保留（全库从未触发，无实测依据调整） |
| 占位崩坏     | 逐书     | —      | **只报告**（与 check_vocab 的存量待清段重叠） |

**「中文重复片段」为何不判红**：实测 8 处里约一半是**合法重复**——
同一行里先给英文原句的译文、再做拆解时，译文短语会出现两次
（`books-that-saved-my-life` ch32:30 实证）。而另一半是**真损坏**且很严重
（`home-sick` ch41:65：`你需要保护自己免受她的伤害。你需要保护自己免受自己的
伤害。不，…` 同一句重复四遍还多出 `她。你自己。她。你自己。`）。
工具无法区分二者，故**报出让人判，不替人定性**。

来源：收敛自 `attic/corruption_scan.py`（39 行）＋ `fix_mojibake.py` 的教训
（后者是**写死路径的一次性修复脚本**，不提升为工具）。
本版新增 attic 版缺失的两项：**U+FFFD** 与**占位崩坏**（方案 §五 P1 要求）。

用法
----
    python3 scripts/corruption_scan.py "<书目录>" [--quiet]

退出码：存在 **FAIL 级**损坏则非 0（报告级不影响退出码）。
"""
import re
import sys
import glob
import os

# ── FAIL 级：实测零假阳 ────────────────────────────────────────────────
FFFD = '�'                      # U+FFFD 替换字符，提取环节的典型残留
DBL_PERIOD = '。。'              # 双句号
# ── 报告级：存在合法命中，只报不判 ─────────────────────────────────────
# 一行内重复出现的长中文串（≥14 字）。英文重复在精读笔记里是常态
# （术语复述），中文重复才可疑——但译文+拆解会合法重复，故只报。
CN_RUN = re.compile(r'([一-鿿]{14,60})')
SPLICE = re.compile(r'。\s*[-:]\s*')      # 句中插入破折号/冒号
# 占位崩坏：词表行里例句列为空 / 纯破折号 / 未见于原文类占位
PLACEHOLDER = re.compile(
    r'^\s*\|[^|]*\|[^|]*\|\s*(?:—|--|—\s*)?\s*\|\s*$'          # 末列为空或纯破折号
    r'|未见于原文|本章无此搭配|暂缺|待补|^\s*\|\s*\|\s*\|')


def scan_file(path):
    """返回 (fail_hits, report_hits)；每项 (行号, 类型, 说明)。"""
    fails, reports = [], []
    with open(path, encoding='utf-8', errors='ignore') as fh:
        for i, ln in enumerate(fh.read().split('\n'), 1):
            if len(ln) < 20:
                continue
            if FFFD in ln:
                fails.append((i, 'U+FFFD', '替换字符——提取/编码环节残留'))
            if DBL_PERIOD in ln:
                fails.append((i, '双句号', '中文不用「。。」，机器人编辑残留'))
            for m in CN_RUN.finditer(ln):
                frag = m.group(1)
                if ln.count(frag) > 1:
                    reports.append((i, '中文重复片段',
                                    '%s（**可能是译文+拆解的合法重复，需人判**）' % frag[:26]))
                    break
            if SPLICE.search(ln):
                reports.append((i, '句中插入', '句中出现破折号/冒号——疑似半拼接'))
            if ln.strip().startswith('|') and PLACEHOLDER.search(ln):
                reports.append((i, '占位崩坏', '词表行例句列为空或占位'))
    return fails, reports


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    quiet = '--quiet' in sys.argv
    if not args:
        raise SystemExit('用法: corruption_scan.py "<书目录>" [--quiet]')
    book = args[0]
    mds = sorted(glob.glob(os.path.join(book, '*.md')))
    if not mds:
        print('该目录下无 md 文件：%s' % book)
        return 0

    nf = nr = 0
    for md in mds:
        name = os.path.basename(md)
        fails, reports = scan_file(md)
        for i, kind, detail in fails:
            nf += 1
            print('%s:%d ❌ %s —— %s' % (name, i, kind, detail))
        for i, kind, detail in reports:
            nr += 1
            if not quiet:
                print('%s:%d ⚠️ %s —— %s' % (name, i, kind, detail))

    print('\n=== 编辑损坏扫描（%s）===' % os.path.basename(book.rstrip('/')))
    print('  FAIL %d 处（U+FFFD / 双句号）' % nf)
    print('  报告 %d 处（中文重复片段 / 句中插入 / 占位崩坏）——**不判红，需人工判**' % nr)
    if nr:
        print('  提示：「中文重复片段」实测假阳率约 50%（同一行里译文与拆解会合法重复），')
        print('        真损坏样例见 home-sick ch41:65（同一句重复四遍）。')
    return 1 if nf else 0


if __name__ == '__main__':
    sys.exit(main())
