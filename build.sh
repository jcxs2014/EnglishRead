#!/bin/bash
# 构建脚本（GitHub Actions / Cloudflare Pages 通用）
set -e

cd site
npm install --legacy-peer-deps
npx quartz build
