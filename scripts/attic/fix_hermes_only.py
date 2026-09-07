"""只修正 Hermes-Mac 作者消息的时间戳 + 5 条 xx 占位 + 归并 3 条越位 Hermes。
ZCode / Opencode 消息一律保持原时间戳不动。
按时间戳倒序重排消息列表。"""
import re, subprocess
from datetime import datetime, timezone, timedelta

SRC = "/tmp/COLLAB_orig.md"
DST = "COLLABORATION.md"

MY_MAP = {
    "BTSML 审查完成": "4444d343c5900c372116e13acc9b40b7fb4dd7ba",
    "100 Great Short Stories 词汇表 7 FAIL 修复": "87621e47a0af0bcddf32486a43b2f2b382bb6dd1",
    "接手 100 Great 返工": "41a05b77228f976be7b4276c25a92f23c941fbd2",
    "100 Great 返工进展——P2 + 3 批 P1": "6d22865f00ad4314770d01cc9ba677c87b5b2ad2",
    "ch26 漏网已补": "392c7c3c48102cbf4d4608f25cc650ecf4284071",
    "100 Great 全书 900/900": "4c8f17233f1c7fe436259f4e015a3c3e853d014e",
    "100 Great 返工——Hermes-Mac 负责区间 ch03": "11e6800672dd4a6c50186a9092f679013b0cb0a9",
    "Inside the Box 全书 16 单元精读完成": "bdb4c641ce478b82286657476bb4ca00104b9123",
    "本轮跨 6 本书引文": "2b4662483cc04e2c1fe0c1250f35cb5cdd24707c",
    "跨 6 本书引文": "2b4662483cc04e2c1fe0c1250f35cb5cdd24707c",
    "新增 11 本书籍分类归档": "2a24f6952e7147597db698bf62b954392ef6afc7",
    "EnglishRead 工作流重构": "64a31e45b41c37887e3c92081e2ea47b7484213e",
}

def git_ts(h):
    raw = subprocess.check_output(["git", "show", "-s", "--format=%aI", h]).decode().strip()
    dt = datetime.strptime(raw, "%Y-%m-%dT%H:%M:%S%z")
    return dt.astimezone(timezone.utc)

def rewrite_ts(block, new_ts):
    first = block.split('\n', 1)[0]
    new_first = re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', new_ts, first)
    return new_first + '\n' + block.split('\n', 1)[1]

def parse_ts(block):
    m = re.search(r'\[(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})\s+UTC', block)
    if not m: return None
    Y, Mo, D, H, MN = (int(m.group(i)) for i in range(1, 6))
    if H == 24:
        return datetime(Y, Mo, D, 0, 0, tzinfo=timezone.utc) + timedelta(days=1)
    return datetime(Y, Mo, D, H, MN, tzinfo=timezone.utc)

def fix_xx(block):
    m = re.search(r'\[(\d{4}-\d{2}-\d{2}) (\d{2}):[xX]{2} UTC\]', block)
    if not m: return None
    dt = datetime.strptime(m.group(1)+" "+m.group(2)+":00", "%Y-%m-%d %H:%M").replace(tzinfo=timezone(timedelta(hours=2)))
    ts = dt.astimezone(timezone.utc)
    return rewrite_ts(block, ts.strftime("%Y-%m-%d %H:%M")), ts

src = open(SRC).read()
lines = src.split('\n')

# 找 "## 📨 消息列表" 段
h_start = None
for i, l in enumerate(lines):
    if l.startswith("## ") and "消息列表" in l:
        h_start = i; break
h_end = len(lines)
for k in range(h_start+1, len(lines)):
    if lines[k].startswith("## "):
        h_end = k; break

intro = lines[:h_start]
outro = lines[h_end:]
body = lines[h_start:h_end]

# 从 body 和 outro 中收集所有消息块（含越位）
all_lines = lines[h_start:]
msgs = []
cur = None
for l in all_lines:
    if l.startswith("### [20"):
        if cur is not None: msgs.append(cur)
        cur = l
    elif cur is not None:
        if l.startswith("---"):
            # 分隔符，结束当前 block
            msgs.append(cur)
            cur = None
        elif l.startswith("## "):
            msgs.append(cur)
            cur = None
            break
        else:
            cur += '\n' + l
if cur is not None: msgs.append(cur)

# body 中非消息行（header + 格式说明 + 分隔符）
body_non_msg = [l for l in body if not l.startswith("### [20")]

# 应用修正
final = []
for b in msgs:
    first = b.split('\n', 1)[0]
    agent_m = re.search(r'\[([^\]]+)\]', first)
    agent = agent_m.group(1) if agent_m else ""

    if agent == "Hermes-Mac":
        head = '\n'.join(b.split('\n')[:4])
        for sub, h in MY_MAP.items():
            if sub in first or sub in head:
                ts = git_ts(h).strftime("%Y-%m-%d %H:%M")
                b = rewrite_ts(b, ts)
                print(f"FIX Hermes: {first[:70]:70s} → {ts}")
                break

    r = fix_xx(b)
    if r:
        b, dt = r
        print(f"FIX xx:    {first[:70]:70s} → {dt.strftime('%Y-%m-%d %H:%M')}")

    final.append((parse_ts(b), b))

parseable = [(ts, b) for ts, b in final if ts is not None]
unparseable = [(None, b) for ts, b in final if ts is None]
if unparseable:
    for _, b in unparseable:
        print(f"WARN unparseable: {b.split(chr(10),1)[0]}")

parseable.sort(key=lambda x: x[0], reverse=True)

# Rebuild
out = intro
out.extend(body_non_msg)
for ts, b in parseable:
    out.append(b)
for _, b in unparseable:
    out.append(b)
out.extend(outro)

open(DST, 'w').write('\n'.join(out))

print(f"\nmsgs={len(msgs)} (parseable={len(parseable)} unparseable={len(unparseable)})")
print("first 5:")
for ts, b in parseable[:5]:
    print(f"  {ts} | {b.split(chr(10),1)[0]}")
print("last 3:")
for ts, b in parseable[-3:]:
    print(f"  {ts} | {b.split(chr(10),1)[0]}")
