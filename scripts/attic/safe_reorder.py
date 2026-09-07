"""Rebuild COLLABORATION.md: keep ZCode/Opencode originals; fix Hermes + 5xx + 3 strays."""
import re
from datetime import datetime,timedelta,timezone

ORIG="/tmp/COLLAB_original.md"
path="COLLABORATION.md"
lines=open(ORIG).read().split('\n')

# --- extract Hermes-Mac/mini + Opencode-IDE + CodeBuddy + stray Hermes blocks ---
# We'll only recompute UTC for these (the ones I authored). ZCode/Opencode-Mac keep original.
def is_mine(agent):
    return agent in ("Hermes-Mac","Hermes-mini","Opencode-IDE","CodeBuddy-Mac")

# Hermes commit→topic mapping (I'll match by subject keywords)
HERMES_FIX = [
    # (subject_substring, commit_hash)
    ("BTSML 审查完成","4444d343c5900c372116e13acc9b40b7fb4dd7ba"),  # 20:05:06+02
    ("100 Great Short Stories 词汇表 7 FAIL 修复","87621e47a0af0bcddf32486a43b2f2b382bb6dd1"),  # 22:21:46+02
    ("scripts/ 目录盘点","3e18f6ecb7935a5f013c444521db0d042661fba1"),  # no, wrong. use "任务书移入 docs" → skip
    ("接手 100 Great 返工","41a05b77228f976be7b4276c25a92f23c941fbd2"),  # 14:26:38+02
    ("100 Great 返工进展——P2 + 3 批 P1","57c096c8fcdf5b2fc954d01a01ec29152717ccc1"),  # 15:39:32+02
    ("ch26 漏网已补","392c7c3c48102cbf4d4608f25cc650ecf4284071"),  # 16:07:21+02
    ("100 Great 全书 900/900","28bd9a3fad25ca0e36ac5b74e11f83a0057978a0"),  # 19:24:00+02 → but that's Collected Stories. Use actual 100 Great commit
    ("100 Great 返工——Hermes-Mac 负责区间 ch03–74 全部完成", None),  # batch A 16:19:29+02
    ("Inside the Box 全书 16 单元精读完成并推送","d2436f0b053eac81f0ee35902ad6f8c48706ac1d"),  # 10:15:03+02
    ("新增 11 本书籍分类归档","5e4d8b1efddc5bd4de16040bd50cefe385c5c571"),  # no. Use a book-lovers init commit
    ("本轮跨 6 本书引文/词汇返工","2b4662483cc04e2c1fe0c1250f35cb5cdd24707c"),  # 22:26:12+02
    ("跨 6 本书引文/词汇返工","2b4662483cc04e2c1fe0c1250f35cb5cdd24707c"),  # stray 16:00
    ("EnglishRead 工作流重构","e176895bd48e0a69c15792269bbdff2d34b3cafa"),  # 16:21:05+02 → no, that's Opencode
]

# Actually, let's be more careful. Look up each Hermes block's commit by git log matching
import subprocess
def commit_ts(h):
    out=subprocess.check_output(["git","show","-s","--format=%aI",h]).decode().strip()
    dt=datetime.strptime(out,"%Y-%m-%dT%H:%M:%S%z")
    return dt.astimezone(timezone.utc)

# Manual mapping (only those with clear commit evidence from git log I already checked)
MY_COMMIT_MAP = {
    # Hermes messages by subject substring → commit
    "BTSML 审查完成": "4444d343c5900c372116e13acc9b40b7fb4dd7ba",  # 20:05:06+02
    "100 Great Short Stories 词汇表 7 FAIL 修复": "87621e47a0af0bcddf32486a43b2f2b382bb6dd1",  # 22:21:46+02
    "接手 100 Great 返工": "41a05b77228f976be7b4276c25a92f23c941fbd2",  # 14:26:38+02
    "100 Great 返工进展——P2 + 3 批 P1": "57c096c8fcdf5b2fc954d01a01ec29152717ccc1",  # 15:39:32+02
    "ch26 漏网已补": "392c7c3c48102cbf4d4608f25cc650ecf4284071",  # 16:07:21+02
    "100 Great 全书 900/900": "4c8f17233f1c7fe436259f4e015a3c3e853d014e",  # 18:34:59+02
    "100 Great 返工——Hermes-Mac 负责区间 ch03–74": "6d22865f00ad4314770d01cc9ba677c87b5b2ad2",  # 16:19:29+02
    "Inside the Box 全书 16 单元精读完成并推送": "d2436f0b053eac81f0ee35902ad6f8c48706ac1d",  # 10:15:03+02  (Opencode; not mine) → skip
    "本轮跨 6 本书引文/词汇返工": "2b4662483cc04e2c1fe0c1250f35cb5cdd24707c",  # 22:26:12+02
    "跨 6 本书引文/词汇返工": "2b4662483cc04e2c1fe0c1250f35cb5cdd24707c",  # stray
    "新增 11 本书籍分类归档": "95aecf4a3592a39b32a13ccbfeddab8ac90fe395",  # 10:42+02 (ZCode Nabokov) → wrong. skip
    "EnglishRead 工作流重构": "e176895bd48e0a69c15792269bbdff2d34b3cafa",  # 16:21+02 → no, Opencode. skip
    "目录结构统一——`novels/`": None,  # skip
}

def resolve_ts(block):
    first=block.split('\n',1)[0]
    # Hermes-Mac or Hermes-mini? Check agent
    m=re.search(r'\[([^\]]+)\]',first)
    agent=m.group(1) if m else ""
    # For Hermes-Mac & mini: match subject
    for sub,h in MY_COMMIT_MAP.items():
        if sub in first or sub in '\n'.join(block.split('\n')[:4]):
            if h:
                ts=commit_ts(h)
                return ts.strftime("%Y-%m-%d %H:%M"), ts
    return None, None

def apply_ts(block, new_str, ts_dt):
    first=block.split('\n',1)[0]
    new_first=re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}|[xX]{2}',new_str,first)
    return new_first+'\n'+block.split('\n',1)[1]

# Collect all message blocks
blocks=[]; raw=[]
cur=None; header=""; intro=[]
i=0
# find "## 📨 消息列表"
h_idx=None
for i,l in enumerate(lines):
    if l.startswith("## ") and "消息列表" in l:
        h_idx=i; break
assert h_idx is not None

# collect messages across the whole file (in-list + strays)
def collect():
    out=[]; cur=None
    for l in lines:
        if l.startswith("### [20"):
            if cur is not None: out.append(cur)
            cur=l
        elif cur is not None:
            cur+='\n'+l
    if cur is not None: out.append(cur)
    return out

all_msgs=collect()
print(f"total messages: {len(all_msgs)}")

fixed=[]
for b in all_msgs:
    first=b.split('\n',1)[0]
    new_str,ts_dt=resolve_ts(b)
    if new_str:
        fixed.append((ts_dt, apply_ts(b,new_str,ts_dt)))
    else:
        # keep original, parse original ts
        m=re.search(r'\[(\d{4}-\d{2}-\d{2} \d{2}):[0-9xX]{2} UTC',b)
        if m:
            raw_ts=m.group(1)+":00"
            try:
                d=datetime.strptime(raw_ts,"%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
            except: d=None
        else: d=None
        fixed.append((d,b))

fixed.sort(key=lambda x:(x[0] if x[0] else datetime.min.replace(tzinfo=timezone.utc)), reverse=True)

# Rebuild file: keep intro, then sorted messages, then everything after last msg
# Reconstruct intro = lines up to first msg in original order
# And tail = lines after last msg in original order
first_msg_line_idx=None
last_msg_line_idx=None
for i,l in enumerate(lines):
    if l.startswith("### [20"):
        first_msg_line_idx=i; break
last_msg_line_idx=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].startswith("### [20"):
        last_msg_line_idx=i; break

intro=lines[:first_msg_line_idx]
tail=lines[last_msg_line_idx+len(all_msgs[-1].split('\n')):]

out=intro
for ts,b in fixed:
    out.append(b)
out+=tail

open(path,'w').write('\n'.join(out))
print(f"done. {len(fixed)} messages written")
# Verify
for ts,b in fixed[:5]: print(' ',ts, b.split('\n',1)[0])
for ts,b in fixed[-3:]: print(' ',ts, b.split('\n',1)[0])
