#!/usr/bin/env python3
"""协作板 / 工作日志的发消息工具——把两条老规则从「文档里的叮嘱」变成「写入时的硬门禁」。

它替代的动作是**裸手 Write 进一个共享文件**。实测该动作的缺陷率极高（2026-09-28 量：
板上 48 条里 19 条超 20 行、占全板 56%），且出现过「板上有、HEAD 上无」的整条丢失。
再写一条检查型规则没用（第 8 条早就写过），治法是换生产方式。

硬门禁（任一不满足 → 退出码 2，**不写入**）：
  1. **板消息长度**：默认 ≤20 行且 ≤5000 B（2026-09-29 由 2500 上调，字节是失控兜底），
     超出即拒收，并提示把细节挪到工作日志。
     ⚠️ 口径 = **只算正文**（`count_text(entry_body(...))`）：自动抬头那 2 行、
     条目之间的分隔空行都不计入，**写入端与 `check` 体检端共用同一个函数**
     （2026-09-30 修；此前两把尺子，见 `count_text` 的注释）
  2. **每书一条**：板与日志**各自**独立判重；同一本书已有条目时只允许 --append 就地追加，
     不允许再开新条目
  3. **基线检查**（2026-09-30 按 mode 分流）：`board` 要求 `git log -1 -- <file>` 存在
     （防「板上有、HEAD 上无」）；`daily` 放行「当天首条、文件还没提交过」（原先必拒，
     每天的人肉绕行），但仍**一律拒被 `.gitignore` 覆盖的路径**（写了也看不见）
  4. **写后自查**：新条目/追加内容确实在文件里，且条目数没有意外增加

daily（工作日志）是**长期存档档**，与板不同：
  - **不设行数上限**（2026-09-29 修：板上 20 行的阈值原先也被套在存档节上，
    既有节 >20 行即一律拒收）；改用「净减守卫」拦 `--replace` 把存档压没
  - **一书一节**：判重与定位只认 `^## ` 二级标题；**新建时若正文没有 `## ` 标题，
    工具自动补 `## <书名>`**——缺了标题，这段会按位置落进别人的节里

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

BOARD = os.environ.get("POST_COLLAB_BOARD", "COLLABORATION.md")
LOGDIR = os.environ.get("POST_COLLAB_LOGDIR", ".memory/daily")
REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "collab_identities.json")
# 2026-09-29 删：ENTRY = re.compile(r"^#{2,3} .*$") —— `_log_sections` 改为只认 `^## ` 后
# 全仓再无引用。留着更坏：它字面写着 `#{2,3}`，与真实规则恰好相反，读的人会以为
# 三级标题也算一节（The Last Lifeboat 的审查明细就是 `###` 才被算进隔壁书的节）。


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
    return subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M UTC"],
                          capture_output=True, text=True).stdout.strip()


def check_at(at):
    """--at 传的是**完工时间**（语义值，脚本无从推断），因此校验而非代填。
    ⚠️ 这与「捏造时间戳」事故不是一回事：那次是**发帖时间**被编造，
    而发帖时间本就该由脚本查 `date -u`；完工时间只有做事的人知道。"""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC", at or ""):
        print(f"❌ --at 格式须为 `YYYY-MM-DD HH:MM UTC`，收到 {at!r}。")
        return None
    try:
        d = datetime.datetime.strptime(at, "%Y-%m-%d %H:%M UTC")
    except ValueError:
        print(f"❌ --at 不是合法时间：{at!r}")
        return None
    now = datetime.datetime.strptime(now_stamp(), "%Y-%m-%d %H:%M UTC")
    if d > now:
        print(f"❌ 完工时间 {at} 晚于当前时间 {now_stamp()}——不能给还没做完的事打完工戳。")
        return None
    return at


def board_entries(text):
    """板上条目块：每条以 `### [时间戳] [身份] → 收件人` 开头，到下一条为止。"""
    idx = [m.start() for m in re.finditer(r"^### \[", text, re.M)]
    out = []
    for k, s in enumerate(idx):
        e = idx[k + 1] if k + 1 < len(idx) else len(text)
        out.append(text[s:e])
    return out


# ── 长度口径：全脚本唯一 ────────────────────────────────────────────────────────
# 2026-09-30 修。此前同一份内容在三个地方量出三个数：
#   ① 门禁 1 数**裸正文**（`body.count("\n")+1`，那时还没拼自动抬头）；
#   ② 新建 board 时把抬头拼上后**又数一遍**（含抬头 2 行）；
#   ③ `check` 体检数 `board_entries` 切片——除抬头外，切片还天然带着
#      「本条抬头 → 下一条抬头」之间的**分隔空行**（2 个 `\n`）。
# 实测后果：正文 12 行 → 写入门禁读 12、体检读 16；正文 17 行 → 门禁放行、
# `check` 报 21 行判 ❌。于是「照写入端的 20 行写」会**稳定**产出体检红条，
# 真实安全线被压到 16 行 —— 一把尺子两个刻度，且两处都"没写错"。
# 现在统一到 `count_text(entry_body(x))`：**只算正文**，入参是裸正文还是整条目
# 都得到同一个数字。阈值仍是 20 行 / 5000 B（即正文 20 行），不再被虚高吃掉 4 行。


def entry_body(entry):
    """剥掉**自动抬头**，只留正文。

    只对 `board_entries` / `_log_sections` 的切片调用——切片首行必然是脚本自己
    写的抬头（板只切 `^### [`、日志只切 `^## `），所以**不存在误剥**正文的风险。

    ⚠️ 不要拿它去处理调用方传进来的裸正文：那段正文若自己以 `## ` 开头
    （`daily` 新建允许自带标题），会被剥掉，反而与写入端量出的数不一致。
    """
    lines = entry.split("\n")
    if lines and (lines[0].startswith("### [") or lines[0].startswith("## ")):
        k = 1
        while k < len(lines) and not lines[k].strip():   # 跳过抬头与正文之间的空行
            k += 1
        return "\n".join(lines[k:])
    return entry


def count_text(t):
    """长度口径（唯一）：**(行数, 字节数)**，只算正文。

    先 `rstrip("\\n")` 再数——切片尾部带着条目之间的分隔空行（通常 2 个 `\n`），
    而写入端拿到的是刚拼好的 body（尾部已被 `rstrip`）；不剥就会稳定差 2 行。
    """
    t = t.rstrip("\n")
    return (t.count("\n") + 1 if t else 0), len(t.encode())


def log_path(book):
    d = datetime.date.today().isoformat()
    return f"{LOGDIR}/{d}.md"


def check_baseline(path, mode):
    """AGENTS 8.1 第 7e 步：写前确认基线存在，否则「写完看不见」无从查起。

    ⚠️ 2026-09-30：这道门原先对**新一天的首条日志**也生效——目标文件必然没有 git 历史
    ⇒ `daily` 每天的第一条**必被拒**（退出码 2，`--force` 也不绕；实测原文：
    `❓ .memory/daily/<今天>.md 从未提交过——无基线可比对`）。当时只能「先手写标题行
    单独提交一次」来建基线，**每天都要人肉绕一次**。
    现在按 mode 分流：
      - `board`（全站唯一一份，出事即全板可见）⇒ **保持严格**：无历史一律拒；
      - `daily`（一天一份，当天首条本就无历史）⇒ 只拒**真危险**的那一种——被
        `.gitignore` 覆盖（写了也看不见），未提交的新文件放行并提示提交。
    """
    if subprocess.run(["git", "log", "-1", "--format=%h", "--", path],
                      capture_output=True, text=True).stdout.strip():
        return True
    if subprocess.run(["git", "check-ignore", "-q", path],
                      capture_output=True).returncode == 0:
        print(f"❌ {path} 被 .gitignore 覆盖——写进去也看不见，先查 ignore 规则。")
        return False
    if mode == "daily":
        print(f"ℹ️ {path} 尚无 git 历史（当天首条日志）——已放行新建；"
              f"写完**记得提交**，否则下次仍无基线可比对。")
        return True
    print(f"❓ {path} 从未提交过——无基线可比对；"
          f"先确认它是否被 .gitignore 覆盖，再决定要不要写。")
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["board", "daily", "check", "mine", "verify"])
    ap.add_argument("body", nargs="?")
    ap.add_argument("--book", help="书标识：板用目录 slug，日志用书名；会出现在条目里用于判重")
    ap.add_argument("--topic", help="非书主题（工具变更/规则调整等），与 --book 二选一；"
                                    "板与日志通用。建议写成「【工具变更】」这样的可检索前缀")
    ap.add_argument("--me", help="本实例身份（任意已知写法，自动归一到规范名）")
    ap.add_argument("--to", default="All", help="收件人（默认 All）")
    ap.add_argument("--note", help="抬头里的补充标记，如 '审查结论'")
    ap.add_argument("--at", help="完工时间 `YYYY-MM-DD HH:MM UTC`（新建板消息必填；追加时不需要，标题不动）")
    ap.add_argument("--append", action="store_true", help="就地追加到已有条目，而不是新建")
    ap.add_argument("--replace", action="store_true",
                    help="整体重写我已有的那一条（完工+审查合并压缩时用）；标题里的完工时间原样保留")
    ap.add_argument("--limit", type=int, default=20,
                    help="**板消息正文**行数上限（默认 20）。口径=只算正文，自动抬头与条目间"
                         "空行不计（写入端与 check 共用 count_text）。⚠️ 2026-09-29 起这道门"
                         "只对 board 生效，daily 是长期存档档、不设行数上限；"
                         "daily 改用「--replace 净减守卫」")
    # 5000 B（2026-09-29 由 2500 上调）：字节不是与行数平级的门槛，而是**失控兜底**——
    # 行数数「要读几件事」，字节数在本库（CJK 1 字 3 B）只反映「写得密不密」，
    # 惩罚密度会误伤结构良好的紧凑通报。实测全板：行数达标者最大 4,359 B、
    # 真正的失控条目最小 6,029 B，**5,000–6,000 之间无条目** ⇒ 阈值落在这道空隙里。
    ap.add_argument("--maxbytes", type=int, default=5000,
                    help="**板消息正文**字节兜底阈值（默认 5000；超出行数限制才是主要信号）。"
                         "口径同 --limit（只算正文），也只对 board 生效")
    ap.add_argument("--force", action="store_true",
                    help="daily --replace 的净减守卫：确属有意精简时强推（默认拒收净掉 30%%／20 行以上的重写）")
    a = ap.parse_args()

    if a.mode == "check":
        return check_all(a.limit, a.maxbytes)
    if a.mode == "verify":
        if not a.book:
            ap.error("--verify 需要 --book")
        return verify(a.book, datetime.date.today().isoformat())
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

    if not a.body:
        ap.error("需要 <body.md>")
    if a.topic:
        a.book = a.topic
    elif not a.book:
        ap.error("需要 --book（书标识）或 --topic（非书主题）")
    body = open(a.body, encoding="utf-8").read().rstrip()
    if body.lstrip().startswith("### ["):
        print("❌ 正文里不要自己写抬头——身份与时间戳由本脚本生成（防止写错身份/捏造时间戳）。\n"
              f"   请只给正文，身份用 --me {a.me or '（必填）'} 传入。")
        return 2
    ident = ikey = None
    if a.mode == "board":
        if not a.me:
            print("❌ 板消息必须给 --me（身份由脚本查登记表归一，不手打）。")
            return 2
        ident, ikey = resolve(a.me)
        if not ident:
            return 2

    path = BOARD if a.mode == "board" else log_path(a.book)
    if not check_baseline(path, a.mode):
        return 2

    # 门禁 1：长度（此时 body 还是裸正文，尚无自动抬头；`count_text` 对裸正文与
    # 整条目给出同一数字，所以「只算正文」在这里就是**原样计数**）
    n, b = count_text(body)
    if a.mode == "board" and (n > a.limit or b > a.maxbytes):
        print(f"❌ 板消息正文 {n} 行 / {b} B，超出 {a.limit} 行 / {a.maxbytes} B —— 未写入。\n"
              f"   板上只放：文件数 · 门禁数字 · 结论 · commit 计数 · 一行日志指引。\n"
              f"   逐行输出、三档定性、原文支撑行号等明细请用 --mode daily 写进工作日志。")
        return 2

    if a.book not in body:
        print(f"❌ 正文里找不到书标识「{a.book}」——判重与写后自查都靠它。"
              f"请在条目抬头或首行写上本书的目录 slug / 书名。\n未写入。")
        return 2

    # ⚠️ 文件可能还不存在（当天的首条日志）：`check_baseline` 已放行这种情形，
    # 这里必须按空文本处理——否则会在 `open()` 处抛 FileNotFoundError（2026-09-30 实测，
    # 基线门禁刚放行就撞上同一个「假设文件已存在」的病灶，两处必须一起改）。
    text = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    ents = board_entries(text) if a.mode == "board" else _log_sections(text)
    hit = [e for e in ents if a.book in e]

    # 门禁 2：每书一条
    if hit and not (a.append or a.replace):
        kind = "每主题只应一条" if a.topic else "每书只应一条"
        print(f"❌ 「{a.book}」在 {path} 已有 {len(hit)} 条条目——{kind}。\n"
              f"   追加结论请用 --append 就地并入既有条目（AGENTS：就地编辑，不新开条目）。\n"
              f"   既有条目前 80 字：{hit[0][:80].strip()}")
        return 2

    before = len(ents)
    # 抬头只在**新建**时生成；追加路径标题原样保留（完工时间不变，审查时间写进正文）
    if a.mode == "board" and not (hit and (a.append or a.replace)):
        if not a.at:
            print("❌ 新建板消息必须给 --at「<完工时间 YYYY-MM-DD HH:MM UTC>」——\n"
                  "   板上按完工时间排序（最新在前），不是按发帖时间；"
                  "追加审查结论用 --append，此时不需要 --at。")
            return 2
        stamp = check_at(a.at)
        if not stamp:
            return 2
        note = f" / {a.note} {now_stamp()}" if a.note else ""
        body = f"### [{stamp}{note}] [{ident}] → {a.to}\n\n" + body
        # ⚠️ 此处**不再复检长度**：拼上抬头前后量的是同一份正文，门禁 1 已经用
        # `count_text` 查过。原先是「拼完抬头再数一遍」的第二道门，含抬头 2 行 ⇒
        # 与门禁 1 差 2 行；三处口径正是从这种"顺手再数一次"长出来的（2026-09-30 修）。

    if hit and (a.append or a.replace) and a.mode == "board":
        head = hit[0].split("\n")[0]
        if heading_identity(head) != ident:
            print(f"❌ 该条目不属于 {ident}（抬头：{head[:70]}）——"
                  f"**不得修改其他实例的消息**。\n   如需补充，在自己名下另发一条并注明指向。")
            return 2
    if hit and (a.append or a.replace):
        # 追加/重写只动正文，**标题（完工时间 + 身份）原样保留**——审查结论的时间写进正文
        s = text.index(hit[0])
        e = s + len(hit[0])
        # ⚠️ 正文里**没有抬头**（抬头只在新建时生成），所以这里直接用 body 原样追加。
        # 早前写成 body.split("\n", 1)[1] 是为了剥掉自动抬头，改版后它会**吃掉正文第一行**，
        # 单行正文还会 IndexError——2026-09-29 自测抓到。
        if a.replace:
            # 整体重写：保留原抬头（完工时间与身份不动），只换正文
            old_head = hit[0].split("\n", 1)[0]
            merged = old_head + "\n\n" + body.strip() + "\n\n"
        else:
            merged = hit[0].rstrip() + "\n\n" + body.strip() + "\n\n"
        if text[e:e + 1] == "\n":
            e += 1
        # ⚠️ 长度门禁必须查**合并结果**：完工那条本就占掉一半额度，
        # 只查追加片段的话，完工 18 行 + 审查 18 行 = 36 行照样「成功」
        # （2026-09-28 实测板上 16 条超限里 11 条正是这样来的）
        #
        # ⚠️ 这道门**只对 board 生效**（2026-09-29 修）。它写在 mode 分流之外时，
        # 板上 20 行的阈值被套在 daily 的**长期存档节**上：既有节 >20 行就一律拒收，
        # 而存档节本来就该长 ⇒ 当日日志 140 节里 52 节永久无法 --append；
        # 且「新建」分支（hit 为空）根本不走这道门，于是**能不能写入取决于
        # 书名有没有被别处提到**，与内容长度无关（见 _log_sections 的分节问题）。
        # 报错文案当时还是板口径「请用 --replace 整体重写」——对 47 行的存档节，
        # 那条建议会把存档压没（实测真发生过：387 行完工记录被 132 行新片段覆盖）。
        mn, mb = count_text(entry_body(merged))
        if a.mode == "board" and (mn > a.limit or mb > a.maxbytes):
            act = "重写" if a.replace else "追加"
            on, _ = count_text(entry_body(hit[0]))
            an, _ = count_text(body)
            print(f"❌ {act}后正文 {mn} 行 / {mb} B，超出 {a.limit} 行 / {a.maxbytes} B —— 未写入。\n"
                  f"   现有正文 {on} 行，本次新增 {an} 行（口径：不含自动抬头与条目间空行）。\n"
                  f"   **请把完工要点与审查结论合并压缩到 {a.limit} 行以内，用 --replace 整体重写**：\n"
                  f"     python3 scripts/post_collab.py board <新正文> --book \"<书>\" --me \"<身份>\" --replace\n"
                  f"   压缩时必须两段都在——完工的门禁数字与审查的缺陷数是后来者唯一的入口。")
            return 2
        if a.mode == "daily" and a.replace:
            # daily 档没有行数上限，但 **--replace 只换正文、保留抬头** ⇒ 新正文
            # 必须自带原内容，否则整段被覆盖（上面那条实测）。这道守卫替代行数门禁，
            # 拦的正是那次事故：净掉 30% 以上或 20 行以上即拒，--force 可强推。
            # 口径同 `count_text`：新旧都剥掉节标题（`## <书名>`）后比正文，
            # 否则 1 行标题的差会混进净减量（2026-09-30 统一）
            on, ob = count_text(entry_body(hit[0]))
            nn, nb = count_text(entry_body(body))
            dn, db = on - nn, ob - nb
            if (dn > 20 or db > 0) and (dn > 0.3 * on or db > 0.3 * max(1, ob)):
                if not a.force:
                    print(f"❌ --replace 会让该节净掉 {dn} 行 / {db} B"
                          f"（现有正文 {on} 行 → {nn} 行）—— 拒绝，存档被压没过。\n"
                          f"   **--replace 只换正文、抬头自动保留**，所以新正文必须自带原有全部内容。\n"
                          f"   先 git show HEAD:{path} 取回既有正文，与新片段拼接后再提交；"
                          f"确属有意精简才加 --force。\n未写入。")
                    return 2
                print(f"⚠️ --force：按要求精简该节（净掉 {dn} 行 / {db} B）。")
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
            # daily 新建：**必须自带二级标题**——`_log_sections` 只认 `^## ` 切节，
            # 而调用方通常只写正文（指令第 4 步曾写「不涉及抬头」）。
            # 缺了标题，这段就按位置落进**别人**的节里：`verify` 报「0 个二级节」、
            # 读者扫标题也看不见。2026-09-29 实测：5 段压条记录全落在 Opencode-Mac 节内，
            # 而 `###` 开头同样落此下场（The Last Lifeboat 的审查明细 56 行因此被算进
            # 隔壁《The Cafe at Beach End》的节）。调用方自带 `## ` 标题时原样保留。
            if not re.match(r"^## ", body):
                body = f"## {a.book}\n\n" + body
            new = text.rstrip() + "\n\n" + body + "\n"
        act = "已新建条目"
        # 回执口径与 `check` 一致（只算正文）；新建时等价于正文行数
        n, b = count_text(entry_body(body))

    if act != "已新建条目":
        # ⚠️ 2026-09-30：追加/重写的回执原先**沿用门禁 1 量过的「本次片段」**
        # （`n, b` 在门禁 1 处算好后，合并分支里再没更新）⇒ 实测回执 `1 行 / 56 B`，
        # 而同一条 `check` 读作 `12 行 / 308 B`。门禁本身查的是**合并结果**（正确），
        # 但**回执读数两份**会让人以为那条只剩 1 行——与「三处口径」同一病灶的残留。
        # 现在回执也报**合并后整条**，并显式标注量的是哪一份。
        n, b = count_text(entry_body(merged))

    # 门禁 4：**先在内存里验证，再落盘**——否则返回 2 时文件已被改动，
    # 会留下「工具说失败、内容却在」的半成品（2026-09-28 注入自证抓到）
    _postcheck(new, path, a.book)
    open(path, "w", encoding="utf-8").write(new)
    tag = "本条" if act == "已新建条目" else "合并后整条"
    print(f"✅ {act}：{path}（{tag} {n} 行 / {b} B）")
    return 0


def _log_sections(text):
    """工作日志的「条目」＝ 一本书的当日归档节。

    ⚠️ 2026-09-29 修：原先按 `^#{1,3} ` 切，一本书只要自己带 `###` 子标题就被切成
    N 节 ⇒ ① `hit[0]` 静默取第一节，追加内容落到哪节取决于书写顺序而非人指定；
    ② 写后自查按节计数，同一本书本来就 >1 节 ⇒ **daily --append 一律被拦**
    （实测：LHBC 那本书名命中 4 节、Cafe 3 节、Paris Deception 3 节）。
    判重与定位都只认 **`^## ` 二级标题**（书的归档节），子标题归节内内容。
    """
    idx = [m.start() for m in re.finditer(r"^## .*$", text, re.M)]
    out = []
    for k, s in enumerate(idx):
        e = idx[k + 1] if k + 1 < len(idx) else len(text)
        out.append(text[s:e])
    return out


def _postcheck(new_text, path, book):
    """写前在内存里断言：预期条目确实在、同书条目数符合该档的预期。

    ⚠️ 2026-09-29 修：**「恰 1 条」是板的要求，不是日志的**。工作日志里一本书
    当天本来就会有多个二级节（完工一节、审查一节），套用板的恰 1 条 ⇒
    daily 追加一律被写后自查拦下（当时 19 节里有 8 本命中 ≥2 节）。
    """
    ents = board_entries(new_text) if path == BOARD else _log_sections(new_text)
    hit = [e for e in ents if book in e]
    if not hit:
        print(f"❌ 写前自查失败：新文本里找不到「{book}」的条目——**未落盘**，文件保持原样。")
        raise SystemExit(2)
    if path == BOARD and len(hit) > 1:
        print(f"❌ 写前自查失败：板上会出现 {len(hit)} 条含「{book}」的条目——**未落盘**。")
        raise SystemExit(2)


def verify(book, day):
    """写后自查：该书在板上恰有 1 条、在当日日志里 ≥1 条。
    ⚠️ 不要用 `mine | grep 书名` 自查——mine 只列抬头，书名在正文里，恒返回 0。"""
    bt = open(BOARD, encoding="utf-8").read()
    ents = board_entries(bt)
    bc = sum(1 for e in ents if book in e)
    lp = f"{LOGDIR}/{day}.md"
    # 日志按**二级标题切节**统计（同 `_log_sections`）：子标题不算另开条目。
    # 2026-09-29 修：原先按 `^#{1,3} ` 切，一本书带 `###` 子标题就被算成多节，
    # 于是 `verify` 报「5 处」——数字虚高且与「每书一条」的语义无关。
    ltxt = open(lp, encoding="utf-8").read() if os.path.exists(lp) else ""
    lc = sum(1 for e in _log_sections(ltxt) if book in e)
    ok = bc == 1
    print(f"板：{bc} 条（须恰为 1）{'✅' if ok else '❌'}")
    print(f"日志 {lp}：{lc} 个二级节（须 ≥1）{'✅' if lc >= 1 else '❌'}"
          + ("（同书多节＝当天完工与审查各一节，正常）" if lc > 1 else ""))
    if not ok:
        print(f"\n❌ 板上有 {bc} 条含「{book}」的条目——每{'主题' if book.startswith('【') else '书'}只应一条。"
              f"多的那条多半是别人发的或历史遗留，**不要去删别人的**；"
              f"把自己的那条用 --append 补齐即可。")
    return 0 if ok and lc >= 1 else 2


def check_all(limit, maxbytes):
    """全板体检。**行数与字节两维都判**，口径与写入端**逐字相同**（`count_text`）——

    ① 写入路径（`board`）判的是 `n > limit or b > maxbytes`；若体检只判行数，
       就会**漏报「只超字节」的条目**：实测 2026-09-29 有 6 条行数达标、
       字节 2.6–5.4 KB，`check` 却一直显示正常。
    ② 更隐蔽的是**行数口径**：体检原先直接数 `board_entries` 切片，自带抬头 2 行
       与条目间空行 2 行 ⇒ 比写入端**稳定多 4 行**。后果是体检红条与写入拒收指的不是
       同一件事：写入端放行的「正文 20 行」，体检报 24 行 ❌，于是运维的人把安全线
       手动压到 16 行。2026-09-30 起两端共用 `count_text(entry_body(...))`。
    ⇒ 体检与写入必须用同一把尺子，否则体检没有意义。
    """
    t = open(BOARD, encoding="utf-8").read()
    ents = board_entries(t)
    rows = []
    for e in ents:
        n, b = count_text(entry_body(e))
        rows.append((n, b, e.split("\n")[0][:46]))
    rows.sort(reverse=True)
    over_n = [r for r in rows if r[0] > limit]
    over_b = [r for r in rows if r[1] > maxbytes]
    over = [r for r in rows if r[0] > limit or r[1] > maxbytes]
    print(f"=== 协作板体检：{len(ents)} 条｜超线 {len(over)} 条"
          f"（行 {len(over_n)} · 字节 {len(over_b)}）"
          f"｜阈值 {limit} 行 / {maxbytes} B（只算正文；抬头与条目间空行不计）===")
    for n, b, h in rows:
        why = "、".join(x for x, bad in (("行", n > limit), ("字节", b > maxbytes)) if bad)
        print(f"  {'❌' if why else '  '} {n:4} 行 {b:6} B  {h}"
              + (f"   ← 超{why}" if why else ""))
    if over:
        print(f"\n超线合计 {sum(r[0] for r in over)} 行 / {sum(r[1] for r in over)} B"
              f"，占全板 {sum(r[1] for r in over) * 100 // max(len(t.encode()), 1)}%")
        print("  压条：明细搬进当日工作日志，板用 --replace 整体重写"
              "（完工时间与身份不动，**完工要点与审查结论两段都必须保留**）——"
              "见 `docs/协作板更新指令.md` 第 3 步。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
