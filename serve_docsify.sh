#!/bin/bash
# Docsify 本地预览服务器
# 用法：./serve_docsify.sh [端口号]

PORT="${1:-3000}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 自动释放端口
EXISTING_PID=$(lsof -ti :"$PORT" 2>/dev/null)
if [ -n "$EXISTING_PID" ]; then
  echo "⚠️  端口 $PORT 被占用，正在释放..."
  kill "$EXISTING_PID" 2>/dev/null
  sleep 1
fi

echo "🚀 启动 Docsify 预览服务器"
echo "   地址: http://localhost:${PORT}"
echo "   按 Ctrl+C 停止"
echo ""

cd "$SCRIPT_DIR"
docsify serve . -p "$PORT"
