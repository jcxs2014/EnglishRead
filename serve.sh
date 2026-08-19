#!/bin/bash
# Quartz 本地预览脚本
# 用法：./serve.sh          启动预览（默认端口 8080）
#       ./serve.sh build    仅构建到 public/
#       ./serve.sh clean    清理构建产物

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SITE_DIR="$SCRIPT_DIR/site"
OUTPUT_DIR="$SITE_DIR/public"
PORT=8080

show_help() {
    echo "用法："
    echo "  ./serve.sh          启动预览服务器（端口 8080）"
    echo "  ./serve.sh build    仅构建静态文件到 public/"
    echo "  ./serve.sh clean    清理构建产物"
}

cmd_build() {
    echo "🔨 构建中..."
    cd "$SITE_DIR"
    npx quartz build 2>&1 | tail -5
    echo "✅ 构建完成"
}

cmd_serve() {
    [ ! -d "$SITE_DIR/node_modules" ] && echo "📦 安装依赖..." && cd "$SITE_DIR" && npm install 2>&1 | tail -3
    PID=$(lsof -ti :$PORT 2>/dev/null)
    [ -n "$PID" ] && echo "⚠️  端口 $PORT 被占用，释放中..." && kill $PID 2>/dev/null && sleep 1

    cd "$SITE_DIR"
    echo "🔨 构建中...（约 14 秒）"
    npx quartz build 2>&1 | tail -3
    echo "🚀 http://localhost:$PORT"
    echo "   Ctrl+C 停止"
    (sleep 2 && open "http://localhost:$PORT") &
    npx serve public -l $PORT
}

cmd_clean() {
    [ -d "$OUTPUT_DIR" ] && rm -rf "$OUTPUT_DIR" && echo "🧹 已清理" || echo "无需清理"
}

case "${1:-}" in
    -h|--help) show_help ;;
    build)     cmd_build ;;
    clean)     cmd_clean ;;
    "")        cmd_serve ;;
    *)         echo "未知参数：$1"; show_help; exit 1 ;;
esac
