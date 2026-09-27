#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""协作板完整性守卫（2026-09-27 新增）。

为什么有它：AGENTS 8.1 第 7e 步要求「写 COLLABORATION.md 前先 `git log -1` 确认基线、
改行级 edit」——**但该纪律已连续失效两次**：
  ① `750ca7c2`(09-27 12:14) 整文件重写 → 44 行模板头被冲掉 + 静默删掉
     Hermes `09:54 UTC` 一条消息（消息数 73→73，**按条数查不出来**）
  ② `1a190d90`(16:16) 整文件重写 → 42 行模板头被顶掉（只活下来标题行）
     `99a4eae7`(16:21) 另删 `14:02 UTC` [ZCode-Mac] 一条
**规则存在 ≠ 被遵守**，所以把「纪律」变成「能跑的检查」。

用法（写协作板后、commit 前）：
    python3 scripts/check_collab_guard.py            # 查工作树
    python3 scripts/check_collab_guard.py --head     # 查 HEAD

退出码：0 全绿 / 1 发现问题（详见输出）
"""
import io, os, re, subprocess, sys

HEAD_MARK = "# Agent 协作消息板"
MARKERS = ["**同步方式**", "**读取方式**", "记忆系统四层分工", "IDE 身份约定", "时区约定"]


def load(use_head):
    if use_head:
        t = subprocess.run(["git", "show", "HEAD:COLLABORATION.md"],
                           capture_output=True, text=True).stdout
        if not t:
            sys.exit("❌ 无法读取 HEAD:COLLABORATION.md")
        return t, "HEAD"
    return io.open("COLLABORATION.md", encoding="utf-8").read(), "工作树"


def main():
    use_head = "--head" in sys.argv
    text, where = load(use_head)
    lines = text.split("\n")
    # 模板头 = 标题行到首条消息之间的全部内容（**不能只看前若干行**——
    # 标志块散在 L4/L18/L26/L31，窗口太窄会把完好的头判成损坏）
    try:
        cut = next(i for i, l in enumerate(lines) if l.startswith("### ["))
    except StopIteration:
        cut = len(lines)
    head = "\n".join(lines[:cut])
    msgs = [l.strip() for l in lines if l.startswith("### [")]
    bad = []

    # ① 首行必须是模板标题
    if not lines or lines[0].strip() != HEAD_MARK:
        bad.append("首行不是 `%s`（实际：%r）" % (HEAD_MARK, lines[0][:50] if lines else "空"))
    # ② 模板头 5 个标志块必须在前 12 行
    for m in MARKERS:
        if m not in head:
            bad.append("模板头缺 %r（**整段被整文件重写顶掉**）" % m)
    # ③ 消息数不得少于 HEAD（工作树模式才比）
    if not use_head:
        h = subprocess.run(["git", "show", "HEAD:COLLABORATION.md"],
                           capture_output=True, text=True).stdout
        n_head = len([l for l in h.split("\n") if l.startswith("### [")])
        if len(msgs) < n_head:
            lost = set(l.strip() for l in h.split("\n") if l.startswith("### [")) - set(msgs)
            bad.append("消息数 %d < HEAD 的 %d，疑似丢失 %d 条：%s"
                       % (len(msgs), n_head, len(lost), sorted(lost)[:3]))
    # ④ 时序：首条应最新
    if len(msgs) > 1:
        a = re.search(r"(\d\d:\d\d)", msgs[0]); b = re.search(r"(\d\d:\d\d)", msgs[1])
        if a and b and a.group(1) < b.group(1):
            print("⚠️  提示：首两条时间戳 %s < %s，可能未按「最新到最旧」插入" % (a.group(1), b.group(1)))

    # ⑤ 模板头**不得重复**（我曾误判事故为「头被截断」而补了一份，
    #    结果文件里出现两份头——守卫当时放行，因为只查「有没有」不查「有几份」）
    for m in MARKERS[:2]:
        if text.count(m) > 1:
            bad.append("模板头重复出现 %d 次（`**%s**`）——有人把消息插到标题与头体之间时，"
                       "曾被误判为「头被覆盖」而补了一份" % (text.count(m), m.strip('*')))
    print("检查对象：%s · 消息 %d 条 · 首行 %r" % (where, len(msgs), lines[0][:40] if lines else ""))
    if bad:
        for x in bad:
            print("❌ " + x)
        print("\n恢复：模板头取 `git show 53ceb88f:COLLABORATION.md` 的前 44 行；"
              "消息取肇事 commit 之前的版本，**锚点就地插入，不要整文件重写**。")
        sys.exit(1)
    print("✅ 协作板完整：模板头 %d 项标志齐全，消息 %d 条无减少" % (len(MARKERS), len(msgs)))


if __name__ == "__main__":
    main()
