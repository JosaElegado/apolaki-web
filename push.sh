#!/usr/bin/env bash
# Push the current state of this folder to GitHub Pages.
#   cd ~/Downloads/apolaki-web && ./push.sh "optional commit message"
set -euo pipefail
cd "$(dirname "$0")"

# Cowork writes into this folder over a mount that cannot delete files, so git
# leaves stale locks and half-written objects behind. Your own shell can remove
# them, so clear them first — otherwise git refuses to run.
rm -f .git/*.lock
find .git/objects -name 'tmp_obj_*' -delete 2>/dev/null || true
rm -rf _to_delete _stage _incoming.tgz

MSG="${1:-Site update}"
git add -A
if git diff --cached --quiet; then
  echo "Nothing new to commit."
else
  git commit -m "$MSG"
fi
git push
echo
echo "Pushed. Live in about a minute:"
echo "  https://josaelegado.github.io/apolaki-web/"
