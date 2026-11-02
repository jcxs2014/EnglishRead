# R1 ch23 verifier: re-checks every recorded anchor against the raw text.
# Run: python3 -I .../review/ch23/1-suread.verify.py
import json
import sys

HERE = "/Users/jcxs2014/Documents/Works/EnglishRead/.memory/raw-gates/waiting-on-a-friend-by-natalie-adler/review/ch23"

with open(HERE + "/1-suread.json", encoding="utf-8") as f:
    d = json.load(f)
with open(d["text_file"], encoding="utf-8") as f:
    t = f.read()

entries = []
for fact in d["facts"]:
    entries.append(("fact%d" % fact["id"], fact["anchor"], fact["start"], fact["end"]))
    for ex in fact.get("extra_anchors", []):
        entries.append(("fact%d.extra" % fact["id"], ex["anchor"], ex["start"], ex["end"]))
for i, r in enumerate(d["relations"]):
    entries.append(("relation%d" % i, r["anchor"], r["start"], r["end"]))
for i, n in enumerate(d["numbers"]):
    entries.append(("number%d" % i, n["anchor"], n["start"], n["end"]))

hit = 0
for name, anchor, start, end in entries:
    assert t.find(anchor) >= 0, "%s: find<0 for %r" % (name, anchor)
    assert t[start:end] == anchor, "%s: slice mismatch for %r" % (name, anchor)
    hit += 1

assert hit == d["anchors_hit"] == d["anchors_total"], "count mismatch: %d vs json %d/%d" % (
    hit, d["anchors_hit"], d["anchors_total"])
assert len(t) == d["chars"], "chars mismatch"
print("anchors_hit=%d/%d  chars=%d  facts=%d relations=%d numbers=%d" % (
    hit, d["anchors_total"], len(t), len(d["facts"]), len(d["relations"]), len(d["numbers"])))
sys.exit(0)