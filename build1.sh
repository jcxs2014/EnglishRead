#!/bin/bash
# notes1 归档站构建脚本（CF Workers Builds: Worker "englishread1" 专用）
# 主站构建仍走 build.sh（notes/），两者互不干扰。
# CF 面板配置：
#   Build command  : bash build1.sh
#   Deploy command : npx wrangler deploy -c wrangler.notes1.jsonc
#   Build watch paths: notes1/**   （仅 notes1 变动时构建，其余 push 跳过）
set -e
cd site
npm install --legacy-peer-deps

# CF 构建机内存 8GB，但 Node 默认堆上限仅 2GB。notes1 约 12.8k 篇 md，
# Quartz 把全部 worker 解析结果反序列化进主进程，2GB 堆必然溢出（OOM）。
export NODE_OPTIONS="--max-old-space-size=6144"

# 构建机是临时环境：临时把 baseUrl 换成归档站域名（影响 sitemap/RSS/canonical），
# 构建结束立即还原，不污染仓库工作区（本地跑也安全）。
cp quartz.config.yaml quartz.config.yaml.bak
trap 'mv quartz.config.yaml.bak quartz.config.yaml' EXIT
sed -i.bak2 's|englishread\.jcxs2014\.workers\.dev|englishread1.jcxs2014.workers.dev|' quartz.config.yaml
rm -f quartz.config.yaml.bak2

# 内容源 notes1/，输出到独立目录 public1/（-o 参数），与主站 public/ 完全隔离
npx quartz build -d ../notes1 -o public1

# 去掉 contentIndex.json 中的 content 字段（文章全文），避免 Cloudflare Workers 25MB 单文件限制
python3 -c "
import json
with open('public1/static/contentIndex.json') as f:
    data = json.load(f)
slim = {k: {kk: vv for kk, vv in v.items() if kk != 'content'} for k, v in data.items()}
with open('public1/static/contentIndex.json', 'w') as f:
    json.dump(slim, f, ensure_ascii=False)
print(f'contentIndex.json slimmed: {len(slim)} entries, removed content field')
"

# 门禁：Workers 资源文件数上限 20000（Free 计划）。超限就地失败，
# 从 notes1-MANIFEST.md 尾部挪几本书回 notes/ 后重跑即可。
LIMIT=19000
count=$(find public1 -type f | wc -l | tr -d ' ')
if [ "$count" -gt "$LIMIT" ]; then
  echo "ERROR: public1 有 $count 个文件，超过安全阈值 $LIMIT（Workers 上限 20000）。" >&2
  echo "请从 notes1-MANIFEST.md 尾部移出若干本书回 notes/ 后重试。" >&2
  exit 1
fi
echo "OK: public1 共 $count 个文件（阈值 $LIMIT，Workers 上限 20000）"
