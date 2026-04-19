#!/bin/bash
# shell_scripts/git_lazy.sh
# 外星小怪荣誉出品的 Git 懒人一键三连脚本

# 设置颜色输出，让信息更友好
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo "🚀 外星小怪的懒人Git脚本启动..."

# 检查是否提供了提交信息
if [ -z "$1" ]; then
    echo "${YELLOW}⚠️  警告: 未提供提交信息。将使用默认信息 'Update files'。${NC}"
    COMMIT_MSG="Update files"
else
    COMMIT_MSG="$1"
fi

echo "📝 提交信息: ${COMMIT_MSG}"

# 执行 git add .
echo "📦 添加所有改动..."
git add .

# 执行 git commit
echo "💾 提交改动..."
git commit -m "${COMMIT_MSG}"

# 检查 commit 是否成功
if [ $? -ne 0 ]; then
    echo "❌ 提交失败，可能有冲突或没有改动。脚本终止。"
    exit 1
fi

# 执行 git push
echo "☁️  推送到远程仓库..."
git push

if [ $? -eq 0 ]; then
    echo "${GREEN}✅ 完成！代码已成功推送到 GitHub！${NC}"
else
    echo "❌ 推送失败，请检查网络或远程仓库配置。"
    exit 1
fi
