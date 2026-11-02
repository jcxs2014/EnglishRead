#!/bin/bash
# usage: commit_ch.sh <章 md 相对路径> <commit message>
# 作用：跑 chapter.sh 断言无阻断，然后只提交该路径（pathspec 隔离他实例改动）
set -u
cd /Users/jcxs2014/Documents/Works/EnglishRead || exit 1
p="$1"; m="$2"
out=$(bash scripts/chapter.sh "$p" 2>&1); rc=$?
echo "$out" | tail -6
if [ $rc -ne 0 ] || ! echo "$out" | grep -q "结论：✅"; then
  echo "GATE_FAIL rc=$rc"; exit 1
fi
git add -- "$p" || exit 1
git commit -q -m "$m" -- "$p" || exit 1
git log --oneline -1 -- "$p"
