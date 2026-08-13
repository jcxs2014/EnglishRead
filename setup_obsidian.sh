#!/bin/bash
# 复用源 Obsidian vault 的插件/主题/配置到新 vault（symlink + 复制）
#
# 原理：
#   - plugins/ 与 themes/ 用 symlink 指向源 vault → 两库插件与主题实时一致，更新共享
#   - 配置文件（app.json 等）用复制 → 一次性偏好，不需实时同步
#   - workspace.json 保持独立 → 每个库布局各自保存，共享会串
#
# 使用方式：
#   ./setup_obsidian.sh <目标vault路径>
#   ./setup_obsidian.sh <源vault路径> <目标vault路径>
#   OBS_SOURCE=<源vault路径> ./setup_obsidian.sh <目标vault路径>
#   ./setup_obsidian.sh --check         仅检查，不执行
#
# 选项：
#   -h, --help    显示帮助信息
#   --check       仅显示将执行的操作，不修改
#   --no-config   只链接 plugins/themes，不复制配置文件
#
# 默认源 vault：
#   /Users/jcxs2014/Documents/PersonalNotes/Study/ObsFile
# 可通过环境变量 OBS_SOURCE 或第一个位置参数覆盖

set -e

# ============ 默认配置 ============
DEFAULT_SOURCE="/Users/jcxs2014/Documents/PersonalNotes/Study/ObsFile"

# 配置文件复制策略
#   always:   总是复制（覆盖目标已有）
#   missing:  仅当目标缺失时复制
#   默认 always 用于 community-plugins.json（启用列表需同步），
#   其余用 missing（保留目标自身偏好，缺什么补什么）
CONFIG_ALWAYS=(
    "community-plugins.json"
)
CONFIG_MISSING=(
    "app.json"
    "appearance.json"
    "core-plugins.json"
    "daily-notes.json"
    "graph.json"
    "hotkeys.json"
    "page-preview.json"
    "templates.json"
)
CONFIG_SKIP=(
    "workspace.json"
    "workspaces.json"
)

# 属性面板相关：确保 properties 核心插件启用 + types.json 定义属性类型
# "状态": "text"  → 属性栏可点击，基于历史值给出下拉建议（未读/阅读中/已读）
ENSURE_PROPERTIES=1
PROPERTY_TYPES_JSON='{
  "types": {
    "状态": "text"
  }
}'

# ============ 帮助 ============
show_help() {
    echo "=========================================="
    echo "  Obsidian vault 配置复用脚本"
    echo "=========================================="
    echo ""
    echo "用途：把源 vault 的插件/主题/配置复用到一个新的 vault"
    echo ""
    echo "使用方式："
    echo "  ./setup_obsidian.sh <目标vault路径>"
    echo "  ./setup_obsidian.sh <源vault路径> <目标vault路径>"
    echo "  OBS_SOURCE=... ./setup_obsidian.sh <目标vault路径>"
    echo ""
    echo "选项："
    echo "  -h, --help      显示此帮助信息"
    echo "  --check         仅显示将执行的操作，不修改"
    echo "  --no-config     只链接 plugins/themes，不复制配置文件"
    echo ""
    echo "默认源 vault: $DEFAULT_SOURCE"
    echo "通过环境变量覆盖: OBS_SOURCE=/path ./setup_obsidian.sh <目标>"
    echo ""
    echo "执行内容："
echo "  1. 链接 plugins/  → 源 vault 的 plugins/"
echo "  2. 链接 themes/   → 源 vault 的 themes/"
echo "  3. 复制 community-plugins.json（启用列表，始终同步）"
echo "  4. 补齐 app.json / core-plugins.json / hotkeys.json 等配置"
echo "  5. 启用 properties 核心插件 + 写入 types.json（属性下拉可用）"
echo "  6. workspace.json 保持独立，不做任何操作"
    echo ""
    exit 0
}

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    show_help
fi

# ============ 参数解析 ============
CHECK_MODE=0
NO_CONFIG=0

parse_args() {
    local args=()
    for a in "$@"; do
        case "$a" in
            --check) CHECK_MODE=1 ;;
            --no-config) NO_CONFIG=1 ;;
            *) args+=("$a") ;;
        esac
    done

    if [ ${#args[@]} -ge 2 ]; then
        SOURCE="${args[0]}"
        TARGET="${args[1]}"
    elif [ ${#args[@]} -eq 1 ]; then
        SOURCE="${OBS_SOURCE:-$DEFAULT_SOURCE}"
        TARGET="${args[0]}"
    else
        echo "❌ 缺少目标 vault 路径"
        echo "   用法: ./setup_obsidian.sh <目标vault路径>"
        echo "   查看: ./setup_obsidian.sh --help"
        exit 1
    fi
}

parse_args "$@"

# ============ 路径检查 ============
SOURCE_OBS="$SOURCE/.obsidian"
TARGET_OBS="$TARGET/.obsidian"

echo "=========================================="
echo "  Obsidian vault 配置复用"
echo "=========================================="
echo "📂 源 vault:   $SOURCE"
echo "📂 目标 vault: $TARGET"
echo ""

if [ ! -d "$SOURCE_OBS" ]; then
    echo "❌ 源 vault 缺少 .obsidian 目录: $SOURCE_OBS"
    exit 1
fi

if [ ! -d "$TARGET_OBS" ]; then
    echo "ℹ️  目标 vault 尚无 .obsidian，先创建"
    mkdir -p "$TARGET_OBS"
fi

# ============ 显示将执行的操作 ============
echo "📋 计划执行："
echo "  1. 链接 plugins/"
if [ -d "$TARGET_OBS/plugins" ]; then
    echo "     → 目标已有 plugins/（$(ls "$TARGET_OBS/plugins" 2>/dev/null | wc -l | tr -d ' ') 个插件），将被替换为 symlink"
fi
echo "  2. 链接 themes/"
if [ -d "$TARGET_OBS/themes" ]; then
    echo "     → 目标已有 themes/，将被替换为 symlink"
fi
if [ $NO_CONFIG -eq 0 ]; then
    echo "  3. 复制配置文件（跳过 workspace.json）"
else
    echo "  3. 跳过配置文件复制（--no-config）"
fi
echo ""

if [ $CHECK_MODE -eq 1 ]; then
    echo "🔍 --check 模式：以上仅为预览，未做任何修改"
    exit 0
fi

# ============ 执行：链接 plugins/themes ============
link_dir() {
    local name="$1"
    local src="$SOURCE_OBS/$name"
    local dst="$TARGET_OBS/$name"

    if [ ! -e "$src" ]; then
        echo "ℹ️  源 vault 无 $name/，跳过"
        return
    fi

    # 目标已有内容：若是 symlink 且指向源，无需处理；否则移除后重建链接
    if [ -L "$dst" ]; then
        local link_target
        link_target="$(readlink "$dst")"
        if [[ "$link_target" == *"$name" ]]; then
            echo "✅ $name/ 已是链接，无需处理"
            return
        fi
        rm "$dst"
    elif [ -e "$dst" ]; then
        local backup="$dst.backup.$(date +%Y%m%d%H%M%S)"
        echo "♻️  $name/ 已有内容，备份为 $backup"
        mv "$dst" "$backup"
    fi

    ln -s "$src" "$dst"
    echo "🔗 已链接: $dst → $src"
}

link_dir "plugins"
link_dir "themes"

# ============ 执行：复制配置文件 ============
if [ $NO_CONFIG -eq 1 ]; then
    echo ""
    echo "✅ 完成（跳过配置复制）"
    exit 0
fi

echo ""
echo "📝 复制配置文件："

copy_config() {
    local name="$1"
    local src="$SOURCE_OBS/$name"
    local dst="$TARGET_OBS/$name"

    if [ ! -f "$src" ]; then
        return
    fi

    if [ -f "$dst" ]; then
        # 始终同步的配置（如启用列表）直接覆盖
        echo "   ✏️  $name (覆盖)"
        cp "$src" "$dst"
    else
        echo "   ➕ $name (新增)"
        cp "$src" "$dst"
    fi
}

for name in "${CONFIG_ALWAYS[@]}"; do
    copy_config "$name"
done

for name in "${CONFIG_MISSING[@]}"; do
    if [ -f "$TARGET_OBS/$name" ]; then
        echo "   · $name (已存在，跳过)"
    elif [ -f "$SOURCE_OBS/$name" ]; then
        echo "   ➕ $name (新增)"
        cp "$SOURCE_OBS/$name" "$TARGET_OBS/$name"
    fi
done

# ============ 确保属性面板可用 ============
if [ $ENSURE_PROPERTIES -eq 1 ]; then
    echo ""
    echo "📋 配置属性面板（Properties）"

    # 1. 启用 properties 核心插件（core-plugins.json 中 properties: true）
    if [ -f "$TARGET_OBS/core-plugins.json" ]; then
        python3 -c "
import json, sys
p = '$TARGET_OBS/core-plugins.json'
with open(p) as f:
    data = json.load(f)
data['properties'] = True
with open(p, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('   ✅ core-plugins.json: properties 已启用')
" 2>/dev/null || echo "   ⚠️  python3 不可用，请手动启用 properties 插件"
    fi

    # 2. 写入 types.json（属性类型定义）
    if [ -n "$PROPERTY_TYPES_JSON" ]; then
        echo "$PROPERTY_TYPES_JSON" > "$TARGET_OBS/types.json"
        echo "   ✅ types.json: 已写入（状态属性 → text）"
    fi
fi

# ============ 完成 ============
echo ""
echo "✅ 完成！"
echo "   - plugins/themes 已链接源 vault（共享更新）"
echo "   - 配置文件已复制/补齐"
echo "   - workspace.json 保持独立（两库布局不串）"
echo ""
echo "📌 提示："
echo "   - 若 Obsidian 已打开目标 vault，需重启一次以加载新插件"
echo "   - 之后源 vault 插件更新，目标 vault 自动共享（symlink）"
echo "   - 新增 vault 复用：./setup_obsidian.sh <新vault路径>"
