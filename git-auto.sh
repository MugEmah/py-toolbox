#!/bin/bash
# Usage: ./git-auto.sh <repo-name> [--private]
# Example: ./git-auto.sh my-projects --private

set -e

if [ -z "$1" ]; then
  echo "❌ Please provide a GitHub repo name!"
  echo "Usage: $0 <repo-name> [--private]"
  exit 1
fi

REPO_NAME=$1
VISIBILITY="public"
[ "$2" == "--private" ] && VISIBILITY="private"
BRANCH="main"

# Check GitHub CLI
if ! command -v gh &> /dev/null; then
  echo "❌ GitHub CLI not installed. Install from: https://cli.github.com/"
  exit 1
fi

# Initialize Git
git init -b $BRANCH

# Create .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*.pyo
.venv/
venv/
env/
build/
dist/
*.egg-info/
.vscode/
.idea/
.DS_Store
Thumbs.db
EOF

# Create README
printf "# $REPO_NAME\n\nProject description here.\n" > README.md

# Freeze Python dependencies (optional)
pip freeze > requirements.txt || echo "⚠️ No pip environment detected"

# Stage and commit
git add .
git commit -m "Initial commit"

# Create GitHub repo using gh CLI
echo "🚀 Creating $VISIBILITY repo '$REPO_NAME' on GitHub..."
gh repo create "$REPO_NAME" --"$VISIBILITY" --source=. --remote=origin --push

echo "✅ Done! Repo live at: https://github.com/$(gh api user | jq -r .login)/$REPO_NAME"

