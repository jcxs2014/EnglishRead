#!/bin/bash
set -e
cd site
npm install --legacy-peer-deps

# CF 构建机内存 8GB，但 Node 默认堆上限仅 2GB。books 增长到 ~5500 篇后，
# Quartz 把全部 worker 解析结果反序列化进主进程，2GB 堆溢出（OOM）。
# 上调到 6GB（留余量给 worker 线程与系统），按 ~0.8GB/2600 篇外推可撑到约 15000 篇。
export NODE_OPTIONS="--max-old-space-size=6144"

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
