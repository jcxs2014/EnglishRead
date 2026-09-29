#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""post_collab.py 修复回归：mode 分流 + daily 净减守卫。

隔离办法：在临时目录建一个**自带 git 基线**的仓库副本（门禁 3 会查 `git log -1 -- <file>`，
所以副本必须在一个 git 仓库里、且目标文件已提交过），用 POST_COLLAB_BOARD /
POST_COLLAB_LOGDIR 两个环境变量把路径指过去（默认值不变，对其他实例零影响）。
"""
import os
import shutil
import subprocess
import sys
import tempfile

REAL = "/Users/jcxs2014/Documents/Works/EnglishRead"
T = os.environ.get("POST_COLLAB_TEST_TMP",
                   os.path.join(tempfile.gettempdir(), "post_collab_regress"))
R = os.path.join(T, "repo")

os.makedirs(os.path.join(R, "scripts"), exist_ok=True)
os.makedirs(os.path.join(R, ".memory/daily"), exist_ok=True)
B = os.path.join(R, "COLLABORATION.md")
TG = os.path.join(R, ".memory/daily/2026-09-29.md")
SCRIPT = os.path.join(R, "scripts/post_collab.py")
if not os.path.isdir(os.path.join(R, ".git")):
    shutil.copy(os.path.join(REAL, "scripts/collab_identities.json"),
                os.path.join(R, "scripts/collab_identities.json"))
    subprocess.run(["git", "init", "-q", "."], cwd=R, capture_output=True)
BOOK = "The Lonely Hearts Book Club"


def reset():
    shutil.copy(os.path.join(REAL, "COLLABORATION.md"), B)
    shutil.copy(os.path.join(REAL, ".memory/daily/2026-09-29.md"), TG)
    shutil.copy(os.path.join(REAL, "scripts/post_collab.py"),
                os.path.join(R, "scripts/post_collab.py"))
    subprocess.run(["git", "add", "-A"], cwd=R, capture_output=True)
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t",
                    "commit", "-qm", "reset"], cwd=R, capture_output=True)


def run(mode, body, book=BOOK, extra=()):
    f = os.path.join(T, "body.md")
    open(f, "w", encoding="utf-8").write(body)
    env = dict(os.environ, POST_COLLAB_BOARD=B,
               POST_COLLAB_LOGDIR=os.path.join(R, ".memory/daily"))
    return subprocess.run([sys.executable, SCRIPT, mode, f, "--book", book,
                           "--me", "Opencode-Mac"] + list(extra),
                          capture_output=True, text=True, env=env, cwd=R)


res = []


def t(name, expect_ok, out, frag=""):
    txt = out.stdout + out.stderr
    rc_ok = (out.returncode == 0) if expect_ok else (out.returncode == 2)
    frag_ok = (frag in txt) if frag else True
    good = rc_ok and frag_ok
    res.append(good)
    print("%s %-54s rc=%d %s" % ("✅" if good else "❌", name, out.returncode,
                                 txt.strip().split("\n")[0][:80]))
    if not good:
        print("     期望 rc=%s，片段 %r 命中=%s" % (0 if expect_ok else 2, frag, frag in txt))
    return good


# ① 板：对既有条目追加，**片段自身 ≤20 行、合并后 >20 行** ⇒ 必须走「合并门禁」拒收。
#    （片段自身就 >20 行时会被更早的「门禁 1」拦掉，走不到这里——两处都要保留）
reset()
mid = "**补** The Lonely Hearts Book Club\n" + "x\n" * 12      # 13 行：过门禁 1
t("板 追加(13 行)→合并后 >20 行 ⇒ 拒收", False,
  run("board", mid, book="The Lonely Hearts Book Club", extra=["--append"]),
  "--replace 整体重写")

# ② 板：合规追加 ⇒ 成功
reset()
t("板 追加 3 行 ⇒ 成功", True,
  run("board", "**追加** " + BOOK + "\n\n补一句。\n", extra=["--append"]))

# ③ daily：追加到 521 行存档节 ⇒ 修前必拒，修后应可写
reset()
ANCHOR = "the-lonely-hearts-book-club-by-lucy-gilmore"   # 只在节112 抬头出现 ⇒ 唯一命中
t("daily 追加到 521 行存档节 ⇒ 成功", True,
  run("daily", "**补充** " + ANCHOR + "\n\n追加一句。\n", book=ANCHOR, extra=["--append"]))

# ④ daily：--replace 压没 520 行 ⇒ 净减守卫须拦下
reset()
t("daily --replace 压没 520 行 ⇒ 拒收", False,
  run("daily", "只剩一行 " + ANCHOR + "\n", book=ANCHOR, extra=["--replace"]),
  "拒绝，存档被压没过")

# ⑤ 同上 + --force ⇒ 放行
reset()
reset()
t("daily --replace --force ⇒ 放行", True,
  run("daily", "只剩一行 " + ANCHOR + "\n", book=ANCHOR, extra=["--replace", "--force"]))

# ⑥ daily：--replace 增补（不净减）⇒ 放行
reset()
old = open(TG, encoding="utf-8").read()
B2 = ANCHOR
i = old.index("## The Lonely Hearts Book Club")
j = old.index("\n## ", i + 10)
big = os.path.join(T, "big.md")
open(big, "w", encoding="utf-8").write(
    old[i:j] + "\n\n**新增一节** " + B2 + "\n\n补一句。\n")
t("daily --replace 增补不净减 ⇒ 放行", True,
  run("daily", big, extra=["--replace"]) if False else
  subprocess.run([sys.executable, SCRIPT, "daily", big, "--book", B2,
                  "--me", "Opencode-Mac", "--replace"],
                 capture_output=True, text=True,
                 env=dict(os.environ, POST_COLLAB_BOARD=B,
                          POST_COLLAB_LOGDIR=os.path.join(R, ".memory/daily")),
                 cwd=R))

# ⑦ 板新建超限 ⇒ 仍拒
reset()
t("板 新建 25 行 ⇒ 拒收", False,
  run("board", "x\n" * 25, book="新书测试XYZ", extra=["--at", "2026-09-29 10:00 UTC"]))

# ⑧ daily 新建节（hit 为空，绕过合并门禁）⇒ 仍应成功，且不受行数门禁
reset()
t("daily 新建节 30 行 ⇒ 成功（存档可长）", True,
  run("daily", "## 新书测试XYZ\n\n" + "内容行\n" * 30, book="新书测试XYZ"))

print()
print("回归：%d/%d 通过" % (sum(res), len(res)))
sys.exit(0 if all(res) else 1)
