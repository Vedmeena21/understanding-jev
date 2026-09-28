// Turns hero.html into hero.gif (or into still PNGs to check single moments).
// One-time setup in this folder: npm i playwright-core   (needs Google Chrome + ffmpeg)
//
//   node render.mjs gif hero.html ../hero 9 20        → ../hero.gif  (9 s loop, 20 fps)
//   node render.mjs stills hero.html stills 1.9,5.7,7  → stills/t1.90.png ...
//   node render.mjs png cheatsheet.html ../cheatsheet  → ../cheatsheet.png
import { chromium } from 'playwright-core';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs'; import os from 'node:os'; import path from 'node:path';

const [mode, html, out, a, b] = process.argv.slice(2);
const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const page = await browser.newPage({ viewport: { width: 1400, height: 1800 }, deviceScaleFactor: mode === 'png' ? 2 : 1 });
page.on('pageerror', e => console.log('page error:', e.message));
await page.goto('file://' + path.resolve(html) + '?capture');
await page.waitForFunction(() => window.__ready === true, null, { timeout: 30000 });
const poster = page.locator('#poster');

if (mode === 'png') {
  await poster.screenshot({ path: out + '.png' });
  console.log(path.basename(out) + '.png', (fs.statSync(out + '.png').size / 1e6).toFixed(2) + ' MB');
} else if (mode === 'stills') {
  fs.mkdirSync(out, { recursive: true });
  for (const t of a.split(',').map(Number)) {
    await page.evaluate(t => window.__render(t), t);
    await poster.screenshot({ path: `${out}/t${t.toFixed(2)}.png` });
  }
} else {
  const dur = +a, fps = +b, TMP = fs.mkdtempSync(path.join(os.tmpdir(), 'hero-'));
  for (let i = 0; i < dur * fps; i++) {
    await page.evaluate(t => window.__render(t), i / fps);
    await poster.screenshot({ path: `${TMP}/f${String(i).padStart(4, '0')}.png` });
  }
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', String(fps), '-i', `${TMP}/f%04d.png`,
    '-vf', 'split[x][y];[x]palettegen=max_colors=128:stats_mode=full[p];[y][p]paletteuse=dither=none:diff_mode=rectangle',
    '-loop', '0', out + '.gif']);
  fs.rmSync(TMP, { recursive: true, force: true });
  console.log(path.basename(out) + '.gif', (fs.statSync(out + '.gif').size / 1e6).toFixed(1) + ' MB');
}
await browser.close();
