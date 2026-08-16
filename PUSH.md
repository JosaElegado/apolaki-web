# Push this update

```bash
cd ~/Downloads/apolaki-web        # wherever this folder sits
git add -A
git commit -m "Fix links and add legal pages"   # only if git status shows changes
git push
```

If you already have the repo cloned somewhere else, copy these files over that
folder instead of replacing the `.git` directory.

## Turn on GitHub Pages

Repo → **Settings** → **Pages** → Source: **Deploy from a branch** →
Branch: **main**, folder: **/ (root)** → Save.

Give it about a minute. Your team's link:
`https://josaelegado.github.io/apolaki-web/`
