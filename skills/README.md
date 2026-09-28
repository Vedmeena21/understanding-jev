# Skills

6 skills that teach your coding agent how to build with Jev.
Install once. Then just ask.

| Skill | Ask it to... |
|---|---|
| [`jev-design`](jev-design/SKILL.md) | Turn a decision in plain English into Jev questions and working code |
| [`jev-audit`](jev-audit/SKILL.md) | Find LLM calls in your codebase that should be Jev calls, with savings |
| [`jev-options`](jev-options/SKILL.md) | Fix weak option descriptions so answers get more accurate |
| [`jev-threshold`](jev-threshold/SKILL.md) | Pick confidence thresholds from your labeled data |
| [`jev-eval`](jev-eval/SKILL.md) | Compare Jev with your current LLM: accuracy, speed, cost |
| [`jev-migrate`](jev-migrate/SKILL.md) | Rewrite one LLM call into a Jev call, safely |

---

## Install

**Claude Code**

```bash
claude plugin marketplace add Vedmeena21/understanding-jev
claude plugin install jev-skills@vedmeena21
```

**Codex, Cursor, Gemini CLI and others**

```bash
npx skills add Vedmeena21/understanding-jev
```

Pick your agent when asked. Add `-g` to install for all projects.

---

## Use

Just describe what you want. For example:

> Use jev-audit on this repo and tell me which LLM calls could move to Jev.

> Use jev-design: I want to route incoming emails to sales, support or spam, and send unsure ones to a human.

> Use jev-threshold on data/labeled_tickets.csv. I need 95% accuracy for auto-routing.

In Claude Code you can also call a skill by name, for example `/jev-audit`. Plugin skills may show up as `/jev-skills:jev-audit`.

---

## A good order

```
jev-audit     → find where Jev fits
jev-design    → design the questions        (or jev-migrate for existing code)
jev-options   → sharpen the options
jev-threshold → pick when to trust it
jev-eval      → prove it beats what you have
```

## These skills vs TypeSafe's official skill

TypeSafe ships one general skill: [typesafe-ai/skills](https://github.com/typesafe-ai/skills). Install it too.
These 6 are smaller and focused on single jobs. They work well together.
