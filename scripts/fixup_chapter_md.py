#!/usr/bin/env python3
"""fixup_chapter_md.py — 收尾新生成的章节 md（new_chapter.py 写死的内容必须改掉的三处）。

为什么需要
----------
`new_chapter.py`（也就是 `mkchapter.py` 的底座）**写死**了三件与具体书、与具体档位
有关的东西，而它自己不知道这些：

  1. frontmatter 的 `modified: "2026-09-29"` —— 记忆 #1800 规定该字段必须是**本书
     首 commit 日期**，写错会让 Quartz 的 created-modified-date 插件改读 filesystem
     mtime，章节顺序就乱成 date-desc；
  2. 第三个导航项的标签写死为 `Tropes 兑现/反转` —— 那是**言情档**的字段；推理／悬疑
     档本库主流写「线索结构」（AGENTS 8.3：三档是分类不是配额，格式自成一派是合法的，
     但硬填 Tropes 是硬伤）；
  3. 导航项不带 `- ` 前缀 —— gate.sh ⑬ 的判据是 `^[-*]?\\s*\\*\\*([^*]+)\\*\\*[：:]`，
     两种都过，但与本 genre 目录既有书（The Burnings）形态不一致。

这三处每章都要改、又极容易忘，所以固化成一步。

用法:
  python3 scripts/fixup_chapter_md.py "<书目录>/chNN xxx.md" [...]
      [--date YYYY-MM-DD]      # 默认 2026-10-01
      [--nav-label 线索结构]    # 第三个导航项的新标签
"""
import argparse
from pathlib import Path

OLD_DATE = 'modified: "2026-09-29"'
HARDCODED_LABEL = "Tropes 兑现/反转"
NAV_LABELS = ("一句话概括", "情感弧线位置", HARDCODED_LABEL, "人物弧线", "叙事手法")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--date", default="2026-10-01")
    ap.add_argument("--nav-label", default="线索结构")
    args = ap.parse_args()

    for a in args.files:
        p = Path(a)
        t = p.read_text(encoding="utf-8")
        before = t
        t = t.replace(OLD_DATE, f'modified: "{args.date}"')
        for lbl in NAV_LABELS:
            t = t.replace(f"\n**{lbl}**：", f"\n- **{lbl}**：")
        t = t.replace(f"- **{HARDCODED_LABEL}**：", f"- **{args.nav_label}**：")
        if t != before:
            p.write_text(t, encoding="utf-8")
            print(f"✅ {p.name}: frontmatter + 导航标签已改（{args.date} / {args.nav_label}）")
        else:
            print(f"– {p.name}: 无需改动")


if __name__ == "__main__":
    main()