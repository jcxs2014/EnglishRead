#!/usr/bin/env bash
# 单章门禁 —— 写完一章立刻跑，别等整本。
#
# 用法：
#   bash scripts/chapter.sh "<章 md>"
#   bash scripts/chapter.sh "<章 md>" --json     # 机器层明细（2-machine.json 的内容）
#
# 做四件事：引语逐字（按 … 拆段独立取证）/ 块结构与关键词 / 中文密度 / 形态对比本书众数。
# 「谁做的、什么关系、死因、数字」这一类机器不判——那是审查表 R1 素读 + R3 对账的活。
# 退出码：0 无阻断；1 有阻断；2 无法判定（缺语料）。
set -uo pipefail

if [ $# -lt 1 ]; then
  echo "用法: bash scripts/chapter.sh \"<章 md>\" [--json]" >&2
  exit 2
fi

here="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$here/bookform.py" "$@"
