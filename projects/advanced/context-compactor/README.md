# Context compactor

🔴 Advanced · Uses: Choice (one per message, all in one call)

Long agent sessions fill up the model's memory (the **context**).
When it fills up, answers get worse.

Most tools fix this with a **summary**. Summaries lose details.
This compactor does something else:

- Jev looks at **every** message in **one** call.
- Each one gets: **keep**, **shorten** or **drop**.
- What's kept stays **word for word**.

---

## What it does

```
 0 keep     user        The login test in auth/ is failing since yesterday…
 1 drop     assistant   I'll look at the auth service. Let me list the files first.
 2 shorten  list_files  auth/login.py
 4 drop     read_file   # Acme Platform
 6 keep     run_tests   FAILED auth/tests/test_login.py::test_login_with_expired…
 8 keep     read_file   def decode_token(raw):
10 drop     read_file   def make_invoice(order):
...
14 → 8 messages · ~740 → ~310 tokens (58% smaller)
Saved compacted.json
```

(Example. Your results will differ.)

- The README and the unrelated billing file get **dropped**.
- The error, the buggy code and the fix are **kept**.

---

## The Jev question

For every message `i`:

| Question | Type |
|---|---|
| For reaching the goal, what should we do with `messages[i]`? | Choice: keep / shorten / drop |

All questions go in **one** request. That's the fan-out pattern ([lesson 06](../../../lessons/06-many-questions-one-call)).

## Rules in code

- The first message (the user's request) is always kept.
- The last 3 messages are always kept.
- "Shorten" keeps the first 160 characters.

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"

python main.py                      # the sample coding session
python main.py my_session.json      # {"goal": "...", "messages": [{"role": ..., "content": ...}]}
```

---

## Make it yours

- Hook it into your own agent: compact when the context is 80% full.
- Try "shorten" as a smarter truncation: keep the first and last lines.
- Measure: does the agent still finish the task after compaction?

---

## Inspired by

[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) does this inside Claude Code as a plugin. This project is a small, from-scratch version to learn the idea.
