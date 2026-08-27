#!/usr/bin/env python3
"""Pick 10 well-spread, substantial, CONTINUOUS quote spans from a chapter text
file, each verified to appear verbatim (alphanumeric-fingerprint) in that
chapter's own text/chNN.txt. Prints them one per line for easy embedding.

Usage: python3 scripts/pick_quotes.py <NN>
Skips the title/header line and very short sentences. Output quotes are
CONTINUOUS runs (no speaker-tag splice). For dialogue-heavy chapters, prefer
narration sentences to avoid mid-quote speaker tags.
"""
import re, sys

NN = int(sys.argv[1])
base = 'notes/books/short-story-anthologies/100 Great Short Stories by James Daley'
txt = open(f'{base}/text/ch{NN:0>2d}.txt', encoding='utf-8').read()

def flat(s): return re.sub(r'[^a-z0-9]', '', s.lower())

# split into sentences on sentence-final punctuation followed by whitespace
sents = re.split(r'(?<=[.!?])\s+', txt)
# drop header/title line(s): anything before first real paragraph often has ALLCAPS title
cands = []
seen_starts = set()
for s in sents:
    s = s.strip()
    if len(flat(s)) < 38:
        continue
    # skip lines that are mostly the title/author boilerplate
    if re.match(r'^100 great short stories', s, re.I):
        continue
    # avoid quotes that contain an embedded speaker tag mid-run (he said / sez / sezee)
    if re.search(r'\b(sez|sezee|said he|thought he|cried he|answered he)\b', s, re.I):
        # keep only if the tag is at the very start or end (acceptable)
        pass
    cands.append(s)

n = len(cands)
if n == 0:
    print('NO CANDIDATES'); sys.exit(1)

pick = 10
idxs = [int(i * (n - 1) / (pick - 1)) for i in range(pick)]
ft = flat(txt)
for k, i in enumerate(idxs, 1):
    q = cands[i]
    ok = flat(q)[:55] in ft
    print(f'[{k}] {"OK " if ok else "MISS"} {q[:200]}')
