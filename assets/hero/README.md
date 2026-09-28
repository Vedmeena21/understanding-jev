# How the hero GIF was made

![LLM vs Jev](../hero.gif)

One HTML file. SVG + JavaScript. Rendered to a GIF.
No video editor.

---

## The idea

Show the whole point of Jev in 9 seconds:

- Same ticket, same question.
- The LLM **writes** its answer, word by word.
- Jev **picks** its answer, in one step.

---

## How we made it

1. **Pick one motion.** A race: one side types, the other side decides.
2. **Name every state.** Write down what's on screen, second by second (below).
3. **Ask Claude for one HTML file with SVG.** Everything is drawn by a `__render(t)` function, so any second can be frozen.
4. **Render stills of each state.** Look at every frame like a reviewer.
5. **Fix it, round by round.** Round 1: the status pills overlapped the subtitles. Round 2: the option chips were spaced unevenly.
6. **Render the GIF.** 180 frames, 20 fps, 0.6 MB.

---

## Every state

| Time | State | What you see |
|---|---|---|
| 0.0 – 1.0 s | **Ask** | The ticket and the 4 team options appear |
| 1.0 – 1.4 s | **Send** | Both panels open. Timers start |
| 1.4 – 1.9 s | **Jev picks** | All 4 bars fill together. Shipping wins. 3 more answers pop in. Timer stops at **0.47 s** |
| 1.4 – 5.6 s | **LLM writes** | "thinking…", then the answer types out. Timer stops at **4.20 s** |
| 5.6 – 6.2 s | **Parse** | The LLM's text still has to be turned into "Shipping". An extra step |
| 6.2 – 8.6 s | **Verdict** | "LLMs write. Jev decides." |
| 8.6 – 9.0 s | **Reset** | Fade out, so the loop is smooth |

The timings come from one real side-by-side test. Yours will vary.

---

## Make your own

```bash
cd assets/hero
npm i playwright-core                          # needs Google Chrome + ffmpeg

node render.mjs stills hero.html stills 1.9,5.7,7.5   # check single moments
node render.mjs gif hero.html ../hero 9 20            # 9 s loop, 20 fps → ../hero.gif
```

Open `hero.html` in Chrome to watch it live.

## Files

| File | What it is |
|---|---|
| `hero.html` | The animation. Change the text, colors or timings here |
| `render.mjs` | Turns the HTML into a GIF, still frames, or a PNG |
