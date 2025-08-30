#!/bin/bash

# Navigate to your project folder
cd ~/storage/shared/empress-deploy-core || exit

# Pull latest changes from GitHub
echo "🔄 Pulling latest updates from GitHub..."
git pull origin main --rebase

# Stage all changes
git add .

# Commit with a timestamped message
commit_msg="EMPRESS update: $(date +'%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_msg"

# Push to GitHub
echo "🚀 Pushing changes to GitHub..."
git push origin main

echo "✅ Done. Repository is up-to-date and synced!"
