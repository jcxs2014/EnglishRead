#!/bin/bash
# Quartz 本地预览脚本
# 用法：./serve.sh          启动预览（默认端口 8080）
#       ./serve.sh build    仅构建到 public/
#       ./serve.sh clean    清理构建产物

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SITE_DIR="$SCRIPT_DIR/site"
OUTPUT_DIR="$SITE_DIR/public"

# 颜色
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

show_help() {
    echo "=========================================="
    echo "  EnglishRead Quartz 本地预览"
    echo "=========================================="
    echo ""
    echo "用法："
    echo "  ./serve.sh          启动预览服务器（端口 8080）"
    echo "  ./serve.sh build    仅构建静态文件到 public/"
    echo "  ./serve.sh clean    清理构建产物"
    echo "  ./serve.sh -h       显示帮助"
    echo ""
    echo "首次运行会安装依赖（约1分钟），之后秒启。"
    echo ""
}

cmd_build() {
    echo -e "${GREEN}🔨 构建中...${NC}"
    cd "$SITE_DIR"
    
    # 确保 index.md 存在（Quartz 需要它生成首页）
    if [ ! -f "$SCRIPT_DIR/index.md" ]; then
        echo "ℹ️  创建 index.md 首页..."
        cat > "$SCRIPT_DIR/index.md" << 'EOF'
---
title: EnglishRead 精读
---

# EnglishRead 精读

中文母语者的英文逐句精读知识库。

## 来源

- [The Economist](economist/) - 经济学人期刊
- [The Paris Review](parisreview/) - 巴黎评论
- [Brain Pickings](brainpickings/) - 思想随笔
- [Literary Hub](lithub/) - 文学评论
- [Granta](granta/) - 文学季刊

## 阅读状态

使用 Obsidian 打开 vault，点击文档顶部的"状态"属性可切换阅读进度。
EOF
    fi
    
    npx quartz build 2>&1 | tail -5
    echo -e "${GREEN}✅ 构建完成：${OUTPUT_DIR}${NC}"
    echo "   文件数：$(find "$OUTPUT_DIR" -name '*.html' | wc -l | tr -d ' ') 个 HTML"
}

cmd_serve() {
    if [ ! -d "$SITE_DIR/node_modules" ]; then
        echo -e "${YELLOW}📦 首次运行，安装依赖...${NC}"
        cd "$SITE_DIR" && npm install 2>&1 | tail -3
    fi
    # 自动释放端口
    EXISTING_PID=$(lsof -ti :8080 2>/dev/null)
    if [ -n "$EXISTING_PID" ]; then
        echo -e "${YELLOW}⚠️  端口 8080 被占用，正在释放...${NC}"
        kill "$EXISTING_PID" 2>/dev/null
        sleep 1
    fi
    echo -e "${GREEN}🚀 构建并启动预览服务器（端口 8080）${NC}"
    cd "$SITE_DIR"
    npx quartz build 2>&1 | tail -3
    echo -e "${GREEN}✅ 构建完成，启动服务器...${NC}"
    echo "   浏览器即将打开：http://localhost:8080"
    echo "   Ctrl+C 停止"
    # 延迟打开浏览器（等服务器就绪）
    (sleep 3 && open http://localhost:8080) &
    npx serve public -l 8080
}

cmd_clean() {
    if [ -d "$OUTPUT_DIR" ]; then
        rm -rf "$OUTPUT_DIR"
        echo -e "${GREEN}🧹 已清理 ${OUTPUT_DIR}${NC}"
    else
        echo "无需清理"
    fi
}

# 解析参数
case "${1:-}" in
    -h|--help) show_help ;;
    build)     cmd_build ;;
    clean)     cmd_clean ;;
    "")        cmd_serve ;;
    *)         echo "未知参数：$1"; show_help; exit 1 ;;
esac
