#!/bin/bash
# Usage: ./git-quickstart.sh <repo-name>
# Example: ./git-quickstart.sh my-projects

# Exit on error
set -e

# Check arguments
if [ -z "$1" ]; then
  echo "❌ Please provide a GitHub repo name!"
  echo "Usage: $0 <repo-name>"
  exit 1
fi

REPO_NAME=$1
USERNAME="<your-github-username>"   # <-- CHANGE THIS ONCE
BRANCH="main"

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

# Freeze Python dependencies (optional, won't break if pip not found)
pip freeze > requirements.txt || echo "⚠️ Skipped pip freeze (no pip?)"

# Stage and commit
git add .
git commit -m "Initial commit"

# Add remote & push (SSH)
git remote add origin git@github.com:$USERNAME/$REPO_NAME.git
git push -u origin $BRANCH

echo "✅ Done! Repo live at: https://github.com/$USERNAME/$REPO_NAME"

