#!/bin/bash
# Push the current state of the site to GitHub.
# Usage:  ./push.sh "what changed"
cd "$(dirname "$0")"
MSG="${1:-Update site}"
git add -A
git commit -m "$MSG" || echo "Nothing to commit."
git push
echo
echo "Live in ~1 min: https://josaelegado.github.io/apolaki-web/"
echo "Hard-refresh with Cmd+Shift+R to skip the browser cache."
