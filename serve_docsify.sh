#!/bin/bash
# Docsify 本地预览服务器
# 用法：./serve_docsify.sh [端口号]

PORT="${1:-3000}"

echo "🚀 启动 Docsify 预览服务器"
echo "   地址: http://localhost:${PORT}"
echo "   按 Ctrl+C 停止"
echo ""

docsify serve . -p "$PORT"
