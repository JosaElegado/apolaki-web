# How we work on this site

**This folder is the single source of truth.**
`~/Documents/Apolaki/apolaki-web`

Do not keep another copy in Downloads. If one is there, delete it.

## The loop

1. You ask for a change in Cowork.
2. Claude edits the files in this folder directly. No zips, no downloads.
3. You run one command:

   ```bash
   ~/Documents/Apolaki/apolaki-web/push.sh "what changed"
   ```

4. GitHub Pages updates in about a minute.
   https://josaelegado.github.io/apolaki-web/

## Why you still run the push

The Cowork sandbox can reach your files but not the internet through them,
and it will not handle your GitHub credentials. So the last step is yours.
It is one command.

## What is in here

| Path | What it is |
|---|---|
| `index.html` and the other `.html` files | The live site, one file per page |
| `apolaki.html` | The whole site as a single self-contained file, for sharing |
| `assets/` | CSS, fonts, logos |
| `src/` | The Python builders that generate the HTML. Edit these, not the HTML |
| `docs/` | Design notes and the SEO audit |
| `push.sh` | The one command above |

## Rebuilding by hand

```bash
cd src
python3 build_pages.py && python3 build_legal.py
python3 build_homeowners.py && python3 build_installers.py && python3 build_financing.py
python3 build_single.py
```

Then copy the generated HTML up one level. Claude normally does this for you.

## Live URLs

- Team preview: https://josaelegado.github.io/apolaki-web/
- Production (later): https://apolaki.ai
