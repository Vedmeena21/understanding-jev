# 03 · Choice, Score and Noul

⏱ 15 min · 🎯 Beginner · 🧪 Code: [`code/three_types.py`](code/three_types.py)

[← 02 · Your first call](../02-your-first-call) · [All lessons](../README.md) · [04 · Confidence and thresholds →](../04-confidence-and-thresholds)

---

## What you'll learn

- The 3 question types
- When to use each one
- What each one gives back

---

## Think of them like code

| Type | Like | Use it when the answer is... | You get back |
|---|---|---|---|
| **Choice** | a `switch` | one of N options (up to 255) | `.choice`, `.probabilities`, `.confidence` |
| **Score** | a rating | a level on a scale (2 to 10 levels) | `.score`, `.probabilities`, `.confidence` |
| **Noul** | an `if` | yes or no | `.noul` (0 to 1) |

"Noul" comes from **Bernoulli**, a yes/no probability.

---

## Choice: pick one

> Which team should handle this?

```python
Choice(
    instructions="Which team should handle this",
    criteria={
        "billing": "Payments, invoices, refunds",
        "technical": "Bugs, outages, integrations",
        "sales": "Pricing, upgrades, new accounts",
    },
)
```

- `.choice` → `"billing"`
- `.probabilities` → `{"billing": 0.88, "technical": 0.12, "sales": 0.0}`

---

## Score: rate it on a scale

> How frustrated is the customer?

```python
Score(
    instructions="How frustrated the customer is",
    criteria=["Calm", "Frustrated", "Very angry"],
)
```

- Levels go from **lowest to highest**.
- Level numbers start at 0: Calm = 0, Frustrated = 1, Very angry = 2.
- `.score` is the **average level**, weighted by probability.
- So `1.05` means "about Frustrated".

---

## Noul: yes or no

> Does this message sound urgent?

```python
Noul(instructions="The message conveys urgency or time-sensitivity")
```

- `.noul` → `0.95` means "very likely yes".
- Tip: write it as a **statement** that is true or false.

---

## Which one should I use?

| Your question | Type |
|---|---|
| Which department? Which tool? Which model? | Choice |
| How relevant? How severe? How happy? | Score |
| Is it spam? Is it safe? Does it mention X? | Noul |

Not sure? Ask yourself: **"How many possible answers are there?"**

- 2 (yes/no) → Noul
- A few, with an order → Score
- A few, with no order → Choice

---

## Try it

```bash
python code/three_types.py
```

It sends **one** message with **all 3** question types in **one** call.

---

## Common mistakes

- **Using Choice for a scale.** "Low / Medium / High" has an order. Use Score.
- **Putting two questions in one.** "Is it urgent and angry?" → make 2 Nouls.
- **Doing math with `.score`.** Use it for thresholds ("above 1.5?"). Not for exact numbers.

---

## Quiz

<details><summary>1. "Which of these 5 tools should the agent use?" Which type?</summary>

Choice.
</details>

<details><summary>2. A Score with levels ["Bad", "OK", "Great"] returns 1.9. What does it mean?</summary>

Close to "Great" (level 2). Mostly great, a little OK.
</details>

<details><summary>3. What does Noul return?</summary>

A probability from 0 to 1 that the statement is true.
</details>

---

Next: [04 · Confidence and thresholds →](../04-confidence-and-thresholds)
