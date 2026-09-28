# 11 · Cost and speed math

⏱ 10 min · 🎯 Intermediate · 🧪 Code: [`code/cost_calculator.py`](code/cost_calculator.py) (no API key needed)

[← 10 · Evals and tracing](../10-evals-and-tracing) · [All lessons](../README.md) · [12 · How Jev works inside →](../12-how-jev-works-inside)

---

## What you'll learn

- Why Jev is so cheap
- How to work out the savings for your own app
- Why it's fast

---

## Why it's cheap

With an LLM you pay for 2 things:

- **Input** tokens (what you send)
- **Output** tokens (what it writes). Usually much more expensive.

With Jev:

- **Input:** $0.042 per 1 million tokens
- **Output:** **free**. It doesn't write, so there's nothing to charge for.

---

## Let's do the math

You sort **10,000 support emails a day**.

- Each email ≈ 1,000 input tokens
- The LLM writes ≈ 200 output tokens per answer
- LLM price in this example: $1.25 in / $10 out per 1M tokens

| | Per decision | Per day | Per year |
|---|---|---|---|
| LLM | $0.00325 | $32.50 | $11,862 |
| Jev | $0.000042 | $0.42 | $153 |

**About 77x cheaper.** Less than $13 a month.

---

## Try it with your numbers

```bash
python code/cost_calculator.py
python code/cost_calculator.py --per-day 50000 --tokens-in 800 --llm-out 150
```

| Flag | Meaning |
|---|---|
| `--per-day` | Decisions per day |
| `--tokens-in` | Input tokens per decision |
| `--llm-out` | Tokens the LLM writes per decision |
| `--llm-in-price` / `--llm-out-price` | Your LLM's prices per 1M tokens |

---

## Why it's fast

An LLM writes **one token at a time**. 200 tokens = 200 steps.
Jev answers in **one step**. No writing.

| | LLM | Jev |
|---|---|---|
| Steps per answer | One per token | One |
| Typical time | ~3 to 30 seconds | 70 to 500 ms (TypeSafe's number) |
| 5 questions | 5 answers to write | All 5 in parallel |

---

## Be honest with the numbers

- TypeSafe's claims come from its own tests.
- Independent tests found smaller, but still big, gains: about **2.9x faster** and **12x cheaper** than Claude Haiku 4.5.
- Against very cheap models, the savings can be small.
- Always measure on your own data (lesson 10).

---

## Quiz

<details><summary>1. Why are Jev's output tokens free?</summary>

It doesn't generate text. It returns a picked option and probabilities.
</details>

<details><summary>2. Why is Jev faster than an LLM for decisions?</summary>

An LLM writes token by token. Jev answers in one step.
</details>

<details><summary>3. Should you trust "200x faster" without testing?</summary>

No. Measure on your own data. Independent tests show smaller gains.
</details>

---

Next: [12 · How Jev works inside →](../12-how-jev-works-inside)
