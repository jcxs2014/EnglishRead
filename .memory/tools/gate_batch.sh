#!/usr/bin/env bash
# 分批门禁：在**暂存目录**里只放「本次要提交的章节」的 md + 完整 text/ + library/，
# 再跑 scripts/gate.sh，得到**只针对这批章节**的权威读数。
#
# 为什么需要它（2026-10-20 实测）：
#   `scripts/gate.sh "<书目录>"` 会扫该目录下**全部** ch*.md。本书有 4 个 worker
#   在并行写 ch24+，主目录里时刻混着「别人的半成品」⇒ 直接跑门禁会把
#   **尚未写完的章节**算成本批的阻断型，读数不可用（假红）。
#   ⇒ 暂存目录把「这一批要提交的章节」与「别人正在写的章节」物理隔开。
#
# 用法:
#   bash .memory/tools/gate_batch.sh "<书目录>" <输出日志路径> <章节号...>
# 例:
#   bash .memory/tools/gate_batch.sh notes/books/novels/the-dues-don-ts-of-magic-by-delemhach \
#        .memory/raw-gates/the-dues-don-ts-of-magic-by-delemhach/2026-10-20-ch23_gate_batch.txt \
#        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
set -u
BOOK_ABS="$(cd "$1" && pwd)"
OUT="$2"; shift 2
CHARS="$*"

STAGE="$(mktemp -d "${TMPDIR:-/tmp}/er_gate_stage.XXXXXX")"
trap 'rm -rf "$STAGE"' EXIT

# text/ 与 library/ 用符号链接（只读、体量大）；md 用实体拷贝（会被 gate 读写的只有 md）。
ln -s "$BOOK_ABS/text" "$STAGE/text"
ln -s "$BOOK_ABS/library" "$STAGE/library"
for n in $CHARS; do
  nn=$(printf "%02d" "$n")
  found=0
  for f in "$BOOK_ABS"/ch"$nn"*.md; do
    [ -e "$f" ] || continue
    cp "$f" "$STAGE/$(basename "$f")"
    found=1
  done
  [ "$found" = 1 ] || echo "⚠️  ch$nn 在书目录里没有 md 文件" >&2
done

mkdir -p "$(dirname "$OUT")"
bash "$(git rev-parse --show-toplevel)/scripts/gate.sh" "$STAGE" > "$OUT" 2>&1
RC=$?
echo "EXIT=$RC  （日志：$OUT）"
echo "—— 本批章节的阻断型 ——"
grep -E '❌' "$OUT" | grep -vE 'FAIL 0 处|结构缺陷 0|凭空造词 0 处|未知实体 0|❌ 0' || echo "（无）"
exit $RC
