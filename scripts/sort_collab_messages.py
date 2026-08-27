"""将 COLLABORATION.md 的「消息列表」按时间戳降序重排（最新在前）。

同时处理越位消息：若消息块出现在「消息列表」段之后，统一归并到「消息列表」段再排序。
"""
import re
from datetime import datetime, timezone

path="COLLABORATION.md"
raw=open(path).read()
lines=raw.split('\n')

# 1) 找到「消息列表」heading
msg_hdr_line=None
for i,l in enumerate(lines):
    if l.startswith("## ") and "消息列表" in l:
        msg_hdr_line=i; break
assert msg_hdr_line is not None, "消息列表 heading not found"

# 2) 找下一 top-level heading（## X 但非 消息列表）作为段尾
def next_top(start):
    for i in range(start+1,len(lines)):
        if lines[i].startswith("## ") and "消息列表" not in lines[i]:
            return i
    return len(lines)
msg_end=next_top(msg_hdr_line)

# 3) 消息 = 以 `### [20` 开头的块，延伸到下一个同类块或段尾
def collect(start,end):
    out=[]; cur=None
    for i in range(start,end):
        if lines[i].startswith("### [20"):
            if cur is not None: out.append(cur)
            cur=lines[i]
        elif cur is not None:
            cur+='\n'+lines[i]
    if cur is not None: out.append(cur)
    return out

intro_end=None
for i in range(msg_hdr_line+1,msg_end):
    if lines[i].startswith("### [20"):
        intro_end=i; break
intro=lines[msg_hdr_line+1:intro_end] if intro_end else lines[msg_hdr_line+1:msg_end]

messages=collect(msg_hdr_line+1, msg_end)
strays=collect(msg_end, len(lines))
print(f"section messages={len(messages)}, strays={len(strays)}")
for s in strays: print('  stray:',s.split('\n',1)[0])

# 4) 解析时间戳
def parse_ts(block):
    m=re.search(r'\[(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):([xX\d]{2})\s+UTC',block)
    if not m: return None
    Y,M,D,H=int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4))
    MN_S=m.group(5).upper()
    MN=int(MN_S) if MN_S.isdigit() else 0
    if H==24:
        D+=1; H=0
    from datetime import date
    dd=date(Y,M,D); return datetime(dd.year,dd.month,dd.day,H,MN,tzinfo=timezone.utc)

all_msgs=messages+strays
with_ts=[(parse_ts(b),b) for b in all_msgs]
unparsed=[b for ts,b in with_ts if ts is None]
if unparsed:
    print(f"WARN unparseable={len(unparsed)}")
    for b in unparsed: print(' ',b.split('\n',1)[0])
with_ts=[(ts,b) for ts,b in with_ts if ts is not None]
with_ts.sort(key=lambda x:x[0], reverse=True)

# 5) 重建文件：头+消息heading+intro+排序后的消息+tail（去掉 strays）
tail_lines=lines[msg_end:]
# 标记要被移除的 stray 行号（在 tail_lines 内）
remove=set()
for s in strays:
    fln=s.split('\n',1)[0]
    for j,l in enumerate(tail_lines):
        if l==fln and j not in remove:
            nl=s.count('\n')+1
            for k in range(j,j+nl): remove.add(k)
            break
new_tail=[l for j,l in enumerate(tail_lines) if j not in remove]

out=[]
out.extend(lines[:msg_hdr_line+1])
out.extend(intro)
for ts,b in with_ts:
    out.append(b)
out.extend(new_tail)

open(path,'w').write('\n'.join(out))
print(f"done. total messages written={len(with_ts)}")
print("newest 3:",[with_ts[i][1].split('\n',1)[0] for i in range(min(3,len(with_ts)))])
