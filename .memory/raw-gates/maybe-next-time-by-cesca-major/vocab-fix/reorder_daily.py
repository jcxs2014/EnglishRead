#!/usr/bin/env python3
"""daily 的 Maybe Next Time 节重组：去重 + 时序校正。

现状（2026-10-19）：
  节内容 = [A 我的旧版完工通报（含已失效的「留待主会话裁定」）]
         + [B DSH-Mac 复核记录]
         + [C 我的完工+裁定定稿]
  ⇒ 我的内容**重复两次**，且 DSH-Mac 的复核夹在中间（时序颠倒）。

目标：节内容 = [C 完工+裁定定稿] + [B DSH-Mac 复核]
  （规则：完工在前、审查在后；每书一条节内不重复）

行级操作（不按字符索引切片），原子落盘。
"""
import os
import re
import tempfile

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
P = os.path.join(_ROOT, ".memory", "daily", "2026-10-19.md")

text = open(P, encoding="utf-8").read()
lines = text.split("\n")

# 定位节范围：## Maybe Next Time → 下一个 ##
start = next(i for i, l in enumerate(lines) if l.strip() == "## Maybe Next Time")
end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
sec = lines[start:end]

def find(pred):
    return [i for i, l in enumerate(sec) if pred(l)]

i_a = find(lambda l: l.startswith("《Maybe Next Time》") and "词表重建完工" in l)
i_c = find(lambda l: l.startswith("《Maybe Next Time》") and "三项裁定落地完工" in l)
i_b = find(lambda l: l.startswith("DSH-Mac 复核 maybe-next-time-by-cesca-major"))
assert len(i_a) == 1 and len(i_c) == 1 and len(i_b) == 1, (i_a, i_c, i_b)

# 各段边界：到下一个非空行起始的「段首」或节末
starts = sorted([i_a[0], i_b[0], i_c[0]])
def seg_range(si):
    nxt = [s for s in starts if s > si]
    e = nxt[0] if nxt else len(sec)
    while e > si and sec[e - 1].strip() == "":
        e -= 1
    return si, e

a_s, a_e = seg_range(i_a[0])
b_s, b_e = seg_range(i_b[0])
c_s, c_e = seg_range(i_c[0])
A = sec[a_s:a_e]
B = sec[b_s:b_e]
C = sec[c_s:c_e]
print(f"段 A（旧版完工）{len(A)} 行 ｜ 段 B（DSH-Mac 复核）{len(B)} 行 ｜ 段 C（定稿）{len(C)} 行")

new_sec = sec[:c_s] + C + [""] + B + [""] + sec[c_e:]
# 去掉旧的 A 段（位置在 c_s 之前）
new_sec = new_sec[:a_s] + new_sec[a_s + (c_s - a_s) - len(A):] if False else new_sec
# 正确做法：直接按 sec 的下标重组
out = []
out.extend(sec[:a_s])          # 节标题 + 空行
out.extend(C)                  # 定稿在前
out.append("")
out.extend(B)                  # 复核在后
out.extend(sec[c_e:])          # 节余下部分（原 C 之后）

new_text = "\n".join(lines[:start] + out + lines[end:])
assert new_text.count("\n") <= text.count("\n"), "行数不应增加"

# 幂等 + 断言：定稿段只出现 1 次
assert new_text.count("三项裁定落地完工") == 1, "定稿段应唯一"
assert new_text.count("词表重建完工") == 0, "旧版段应已删除"
assert new_text.count("DSH-Mac 复核 maybe-next-time") == 1, "复核段应唯一"

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix=".tmp")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    f.write(new_text)
os.replace(tmp, P)
print(f"✅ 已重组：{len(sec)} 行 → {len(out)} 行（完工+裁定在前 · DSH-Mac 复核在后 · 无重复）")
