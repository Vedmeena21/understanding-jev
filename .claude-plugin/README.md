# Plugin files

These 2 files make this repo installable as a Claude Code plugin.

| File | What it does |
|---|---|
| `marketplace.json` | Lets people add this repo as a plugin source |
| `plugin.json` | Lists the 6 skills in [`skills/`](../skills) |

Install:

```bash
claude plugin marketplace add Vedmeena21/understanding-jev
claude plugin install jev-skills@vedmeena21
```
