#!/usr/bin/env python3
"""协作板 / 工作日志的发消息工具——把两条老规则从「文档里的叮嘱」变成「写入时的硬门禁」。

它替代的动作是**裸手 Write 进一个共享文件**。实测该动作的缺陷率极高（2026-09-28 量：
板上 48 条里 19 条超 20 行、占全板 56%），且出现过「板上有、HEAD 上无」的整条丢失。
再写一条检查型规则没用（第 8 条早就写过），治法是换生产方式。

硬门禁（任一不满足 → 退出码 2，**不写入**）：
  1. **板消息长度**：默认 ≤20 行且 ≤2500 B，超出即拒收，并提示把细节挪到工作日志
  2. **每书一条**：板与日志**各自**独立判重；同一本书已有条目时只允许 --append 就地追加，
     不允许再开新条目
  3. **基线检查**：写前 `git log -1 -- <file>` 必须存在（防「板上有、HEAD 上无」）
  4. **写后自查**：新条目/追加内容确实在文件里，且条目数没有意外增加

用法：
  # 新建（板）
  python3 scripts/post_collab.py board  <body.md> --book two-wars-and-a-wedding-by-lauren-willig
  # 新建（日志）：就地追加到该书当日条目；当日没有则新建
  python3 scripts/post_collab.py daily  <body.md> --book "Two Wars and a Wedding"
  # 就地追加到已有条目
  python3 scripts/post_collab.py board  <body.md> --book <key> --append
  # 只体检，不改
  python3 scripts/post_collab.py check
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

BOARD = "COLLABORATION.md"
LOGDIR = ".memory/daily"
REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "collab_identities.json")
ENTRY = re.compile(r"^#{2,3} .*$", re.M)


def load_identities():
    """身份登记表：canonical 规范名 + aliases（确定别名）+ inferred_aliases（推断别名）。
    别名一律归一到 canonical，**板面抬头由本脚本写，agent 不再手打自己的名字**。"""
    spec = json.load(open(REGISTRY, encoding="utf-8"))
    canon, infer = {}, {}
    for e in spec["identities"]:
        canon[e["canonical"].lower()] = e["canonical"]
        for a in e.get("aliases", []):
            canon[a.lower()] = e["canonical"]
        for a in e.get("inferred_aliases", {}):
            canon[a.lower()] = e["canonical"]
            infer[a.lower()] = e["canonical"]
    return canon, infer


def resolve(me):
    canon, infer = load_identities()
    k = me.strip().lower()
    if k not in canon:
        print(f"❌ 身份「{me}」不在登记表内——新增一条再发，别临时起名。\n"
              f"   已登记：{', '.join(sorted(set(canon.values())))}\n"
              f"   登记表：{REGISTRY}")
        return None, None
    c = canon[k]
    if k in infer and k != c.lower():
        print(f"⚠️ 「{me}」是**推断别名**（{c} 的历史写法），尚未经实例确认；"
              f"确认后把 {REGISTRY} 里该条 confirmed 置 true。")
    return c, c.lower()


def heading_identity(head):
    """把 `### [ts] [身份] → All` 里的身份字段解析成**规范名**。
    ⚠️ 不能用子串比较：板上 8 条历史条目的抬头写的是 `DSHarness`，而它们属于 `DSH-Mac`——
    逐字比对会认不出自己的旧条目，`--append` 归属门禁也会把合法追加误拒。"""
    canon, _ = load_identities()
    m = re.findall(r"\[([^\]]+)\]", head)
    for cand in m[1:]:                       # [0] 是时间戳
        k = cand.strip().lower()
        if k in canon:
            return canon[k]
    return None


def now_stamp():
    """时间戳由脚本查实，不接受调用方传入（2026-08-31 捏造时间戳事故的根因）。"""
    return subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M UTC"],
                          capture_output=True, text=True).stdout.strip()


def board_entries(text):
    """板上条目块：每条以 `### [时间戳] [身份] → 收件人` 开头，到下一条为止。"""
    idx = [m.start() for m in re.finditer(r"^### \[", text, re.M)]
    out = []
    for k, s in enumerate(idx):
        e = idx[k + 1] if k + 1 < len(idx) else len(text)
        out.append(text[s:e])
    return out


def log_path(book):
    d = datetime.date.today().isoformat()
    return f"{LOGDIR}/{d}.md"


def check_baseline(path):
    """AGENTS 8.1 第 7e 步：写前确认基线存在，否则「写完看不见」无从查起。"""
    r = subprocess.run(["git", "log", "-1", "--format=%h", "--", path],
                       capture_output=True, text=True)
    if not r.stdout.strip():
        print(f"❓ {path} 从未提交过——无基线可比对；"
              f"先确认它是否被 .gitignore 覆盖，再决定要不要写。")
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["board", "daily", "check", "mine"])
    ap.add_argument("body", nargs="?")
    ap.add_argument("--book", help="书标识：板用目录 slug，日志用书名；会出现在条目里用于判重")
    ap.add_argument("--me", help="本实例身份（任意已知写法，自动归一到规范名）")
    ap.add_argument("--to", default="All", help="收件人（默认 All）")
    ap.add_argument("--note", help="抬头里的补充标记，如 '审查结论'")
    ap.add_argument("--append", action="store_true", help="就地追加到已有条目，而不是新建")
    ap.add_argument("--limit", type=int, default=20, help="板消息行数上限（默认 20）")
    ap.add_argument("--maxbytes", type=int, default=2500)
    a = ap.parse_args()

    if a.mode == "check":
        return check_all(a.limit)
    if a.mode == "mine":
        if not a.me:
            ap.error("--mine 需要 --me")
        c, ck = resolve(a.me)
        if not c:
            return 2
        t = open(BOARD, encoding="utf-8").read()
        hits = [e for e in board_entries(t)
                if heading_identity(e.split("\n")[0]) == c]
        print(f"=== {c} 发过的条目 {len(hits)} 条 ===")
        for e in hits:
            print(f"  {e.split(chr(10))[0][:88]}")
        return 0

    if not (a.body and a.book):
        ap.error("需要 <body.md> 与 --book")
    body = open(a.body, encoding="utf-8").read().rstrip()
    if body.lstrip().startswith("### ["):
        print("❌ 正文里不要自己写抬头——身份与时间戳由本脚本生成（防止写错身份/捏造时间戳）。\n"
              f"   请只给正文，身份用 --me {a.me or '（必填）'} 传入。")
        return 2
    if a.mode == "board":
        if not a.me:
            print("❌ 板消息必须给 --me（身份由脚本查登记表归一，不手打）。")
            return 2
        ident, ikey = resolve(a.me)
        if not ident:
            return 2
        stamp = now_stamp()
        note = f" / {a.note} {now_stamp()}" if a.note else ""
        body = f"### [{stamp}{note}] [{ident}] → {a.to}\n\n" + body

    path = BOARD if a.mode == "board" else log_path(a.book)
    if not check_baseline(path):
        return 2

    # 门禁 1：长度
    n, b = body.count("\n") + 1, len(body.encode())
    if a.mode == "board" and (n > a.limit or b > a.maxbytes):
        print(f"❌ 板消息 {n} 行 / {b} B，超出 {a.limit} 行 / {a.maxbytes} B —— 未写入。\n"
              f"   板上只放：文件数 · 门禁数字 · 结论 · commit 计数 · 一行日志指引。\n"
              f"   逐行输出、三档定性、原文支撑行号等明细请用 --mode daily 写进工作日志。")
        return 2

    if a.book not in body:
        print(f"❌ 正文里找不到书标识「{a.book}」——判重与写后自查都靠它。"
              f"请在条目抬头或首行写上本书的目录 slug / 书名。\n未写入。")
        return 2

    text = open(path, encoding="utf-8").read()
    ents = board_entries(text) if a.mode == "board" else _log_sections(text)
    hit = [e for e in ents if a.book in e]

    # 门禁 2：每书一条
    if hit and not a.append:
        print(f"❌ 「{a.book}」在 {path} 已有 {len(hit)} 条条目——每书只应一条。\n"
              f"   追加结论请用 --append 就地并入既有条目（AGENTS：就地编辑，不新开条目）。\n"
              f"   既有条目前 80 字：{hit[0][:80].strip()}")
        return 2

    before = len(ents)
    if hit and a.append and a.mode == "board":
        head = hit[0].split("\n")[0]
        if heading_identity(head) != ident:
            print(f"❌ 该条目不属于 {ident}（抬头：{head[:70]}）——"
                  f"**不得修改其他实例的消息**。\n   如需补充，在自己名下另发一条并注明指向。")
            return 2
    if hit and a.append:
        s = text.index(hit[0])
        e = s + len(hit[0])
        merged = hit[0].rstrip() + "\n\n" + body.split("\n", 1)[1].lstrip() + "\n\n"
        if text[e:e + 1] == "\n":
            e += 1
        new = text[:s] + merged + text[e:]
        act = "已就地并入既有条目"
    else:
        if a.mode == "board":
            # 插入点：消息列表 heading 之后、首个既有条目之前；板上还没有条目时退到 heading 后
            m = re.search(r"^### .*消息列表.*$", text, re.M)
            first = re.search(r"^### \[", text, re.M)
            if first:
                i = first.start()
            elif m:
                i = m.end() + 1
            else:
                i = len(text.rstrip()) + 1
            new = text[:i].rstrip("\n") + "\n\n" + body + "\n\n" + text[i:].lstrip("\n")
        else:
            new = text.rstrip() + "\n\n" + body + "\n"
        act = "已新建条目"

    # 门禁 4：**先在内存里验证，再落盘**——否则返回 2 时文件已被改动，
    # 会留下「工具说失败、内容却在」的半成品（2026-09-28 注入自证抓到）
    _postcheck(new, path, a.book)
    open(path, "w", encoding="utf-8").write(new)
    print(f"✅ {act}：{path}（{n} 行 / {b} B）")
    return 0


def _log_sections(text):
    idx = [m.start() for m in re.finditer(r"^#{1,3} .*$", text, re.M)]
    out = []
    for k, s in enumerate(idx):
        e = idx[k + 1] if k + 1 < len(idx) else len(text)
        out.append(text[s:e])
    return out


def _postcheck(new_text, path, book):
    """写前在内存里断言：预期条目确实在、且同书条目数符合预期。"""
    ents = board_entries(new_text) if path == BOARD else _log_sections(new_text)
    hit = [e for e in ents if book in e]
    if not hit:
        print(f"❌ 写前自查失败：新文本里找不到「{book}」的条目——**未落盘**，文件保持原样。")
        raise SystemExit(2)
    if len(hit) > 1:
        print(f"❌ 写前自查失败：「{book}」会出现 {len(hit)} 条——**未落盘**。")
        raise SystemExit(2)


def check_all(limit):
    t = open(BOARD, encoding="utf-8").read()
    ents = board_entries(t)
    rows = sorted(((e.count("\n") + 1, len(e.encode()), e.split("\n")[0][:46]) for e in ents),
                  reverse=True)
    over = [r for r in rows if r[0] > limit]
    print(f"=== 协作板体检：{len(ents)} 条｜超 {limit} 行的 {len(over)} 条 ===")
    for n, b, h in rows:
        print(f"  {'❌' if n > limit else '  '} {n:4} 行 {b:6} B  {h}")
    if over:
        print(f"\n超线合计 {sum(r[0] for r in over)} 行 / {sum(r[1] for r in over)} B"
              f"，占全板 {sum(r[1] for r in over) * 100 // max(len(t.encode()), 1)}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
