# Assets

The pictures used in this repo. Free to share. Please link back.

| File | What it is |
|---|---|
| [`hero.gif`](hero.gif) | LLM vs Jev in 9 seconds. The LLM writes, Jev decides |
| [`roadmap.svg`](roadmap.svg) | The 3-track learning path: use it, build with it, understand it |
| [`cheatsheet.png`](cheatsheet.png) | Everything about Jev on one page. Great to save or share |

## Folders

| Folder | What's inside |
|---|---|
| [`hero/`](hero) | The HTML that draws the GIF, the render script, and how it was made |
| [`cheatsheet/`](cheatsheet) | The HTML behind the cheatsheet |

## Change something

- Edit the HTML file.
- Render it again with `hero/render.mjs`:

```bash
cd assets/hero
npm i playwright-core                                   # one time. Needs Chrome + ffmpeg
node render.mjs gif hero.html ../hero 9 20              # → hero.gif
node render.mjs png ../cheatsheet/cheatsheet.html ../cheatsheet   # → cheatsheet.png
```
