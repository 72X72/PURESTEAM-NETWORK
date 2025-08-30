#!/bin/bash
# ===============================
# PURESTEAM NETWORK: Termux → GitHub Auto-Push
# ===============================

# Change to project directory
PROJECT_DIR=~/shared/empress-deploy-core
cd $PROJECT_DIR || { echo "Project directory not found!"; exit 1; }

# Check for changes
if [ -z "$(git status --porcelain)" ]; then
    echo "No changes to commit ✅"
    exit 0
fi

# Commit changes
COMMIT_MSG="Auto-push: $(date +'%Y-%m-%d %H:%M:%S')"
git add .
git commit -m "$COMMIT_MSG"

# Push to GitHub
git push origin main

# Optional: Notification (Termux API required)
if command -v termux-notification >/dev/null 2>&1; then
    termux-notification --title "PURESTEAM NETWORK" --content "Changes pushed to GitHub successfully ✅"
fi

echo "Push complete ✅"
