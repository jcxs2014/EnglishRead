#!/bin/bash
set -e
cd site
npm install --legacy-peer-deps
npx quartz build -d ../notes

# 去掉 contentIndex.json 中的 content 字段（文章全文），避免 Cloudflare Workers 25MB 限制
python3 -c "
import json
with open('public/static/contentIndex.json') as f:
    data = json.load(f)
slim = {k: {kk: vv for kk, vv in v.items() if kk != 'content'} for k, v in data.items()}
with open('public/static/contentIndex.json', 'w') as f:
    json.dump(slim, f, ensure_ascii=False)
print(f'contentIndex.json slimmed: {len(slim)} entries, removed content field')
"
