#!/bin/bash
# Push the current state of the site to GitHub.
# Usage:  ./push.sh "what changed"
cd "$(dirname "$0")" || exit 1

# Cowork's sandbox cannot delete files, so it leaves git lock files behind.
# Clearing them here is safe: nothing else is using this repo.
find .git -name '*.lock' -delete 2>/dev/null
find .git/objects -name 'tmp_obj_*' -delete 2>/dev/null

MSG="${1:-Update site}"
git add -A
git commit -m "$MSG" || echo "Nothing new to commit."
git push || exit 1

echo
echo "Pushed. Live in about a minute:"
echo "  https://josaelegado.github.io/apolaki-web/"
echo "Hard-refresh with Cmd+Shift+R, the browser caches the old HTML."
