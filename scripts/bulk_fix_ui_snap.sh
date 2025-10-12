#!/usr/bin/env bash
# Bulk fix ui:snap -> ui-snap typo across multiple repositories
# Usage: ./bulk_fix_ui_snap.sh repo1 repo2 repo3 ...

set -euo pipefail

GITHUB_USER="${GITHUB_USER:-NishizukaKoichi}"
BRANCH_NAME="chore/guard-ui-snap"

if [ $# -eq 0 ]; then
  echo "Usage: $0 <repo1> <repo2> <repo3> ..."
  echo "Example: $0 ai-cage-driven-dev another-repo"
  exit 1
fi

for REPO in "$@"; do
  echo ""
  echo "================================================"
  echo "Processing: $REPO"
  echo "================================================"

  REPO_DIR="/tmp/$REPO-fix"
  rm -rf "$REPO_DIR"

  # Clone
  if ! git clone --depth=1 "git@github.com:$GITHUB_USER/$REPO.git" "$REPO_DIR"; then
    echo "⚠️  Failed to clone $REPO, skipping..."
    continue
  fi

  pushd "$REPO_DIR" > /dev/null

  # Create branch
  git switch -c "$BRANCH_NAME"

  # Fix workflow files
  CHANGED=0
  if [ -d ".github/workflows" ]; then
    if grep -l "ui:snap" .github/workflows/*.yml 2>/dev/null; then
      sed -i '' 's/make ui:snap/make ui-snap/g' .github/workflows/*.yml
      CHANGED=1
    fi
  fi

  # Fix Makefile
  if [ -f "Makefile" ]; then
    if grep -q "ui:snap" Makefile; then
      sed -i '' 's/ui:snap/ui-snap/g' Makefile
      CHANGED=1
    fi
  fi

  if [ $CHANGED -eq 0 ]; then
    echo "✅ No changes needed for $REPO"
    popd > /dev/null
    continue
  fi

  # Commit and push
  git add -A
  git commit -m "chore(ci): guard/replace ui:snap -> ui-snap

Replace all occurrences of 'ui:snap' with 'ui-snap' to fix Makefile
target syntax and prevent future typos.

Related: NishizukaKoichi/ai-cage-driven-dev#1"

  if git push -u origin "$BRANCH_NAME"; then
    echo ""
    echo "✅ Changes pushed to $REPO"
    echo "🔗 Open PR: https://github.com/$GITHUB_USER/$REPO/compare/main...$BRANCH_NAME?expand=1"
  else
    echo "⚠️  Failed to push to $REPO"
  fi

  popd > /dev/null

  # Cleanup
  rm -rf "$REPO_DIR"
done

echo ""
echo "================================================"
echo "✅ Bulk fix completed!"
echo "================================================"
