# 05 · Writing great options

⏱ 15 min · 🎯 Beginner · 🧪 Code: [`code/weak_vs_strong_options.py`](code/weak_vs_strong_options.py)

[← 04 · Confidence and thresholds](../04-confidence-and-thresholds) · [All lessons](../README.md) · [06 · Many questions, one call →](../06-many-questions-one-call)

---

## What you'll learn

- Why options matter more than the question
- How to describe an option so Jev can't confuse it
- How to structure the state

---

## The big idea

Jev reads your options **very literally**.
It doesn't guess what you "meant".

So the #1 way to make Jev more accurate:
**describe every option clearly.**

---

## Weak vs strong

**Weak:**

```python
criteria={"billing": None, "shipping": None, "technical": None, "general": None}
```

Is "error at checkout" billing or technical? Jev has to guess.

**Better:**

```python
criteria={
    "billing": "Payments, invoices, refunds, subscriptions",
    "technical": "Bugs, errors, crashes, app problems",
}
```

**Best:** the same fields for every option.

```python
criteria={
    "billing": {
        "what": "Money: charges, invoices, refunds, subscriptions",
        "not_for": "Payment pages that crash (that's technical)",
        "examples": ["Charged twice", "Refund not received"],
    },
    "technical": {
        "what": "Software problems: bugs, errors, crashes, login issues",
        "not_for": "Feature requests (that's general)",
        "examples": ["App crashes", "Error at checkout"],
    },
}
```

---

## 4 fields that help most

| Field | What to write |
|---|---|
| `what` | What this option covers |
| `not_for` | What it does **not** cover. The tricky edge cases |
| `examples` | 1 or 2 real examples |
| `signals` | Words or clues that point to it |

Tips:

- Use the **same fields** for every option. Jev compares them side by side.
- Put edge cases in `not_for`. That's where mistakes happen.
- Give options **clear names**. In one study, renaming options changed about 1 in 3 answers.

---

## Structure the state too

**Weak:** one long string.

```python
state = "Customer Ravi, premium plan, says: I was charged twice..."
```

**Strong:** JSON with clear names.

```python
state = {
    "customer": {"name": "Ravi", "plan": "premium"},
    "ticket": {"message": "I was charged twice for May."},
}
```

- Send **only** what the decision needs. Extra text lowers accuracy.
- Point at a field in your question: `` "Is `ticket.message` about money?" ``
- Put facts from your database **in the state**. Don't rely on what the model remembers.

---

## Try it

```bash
python code/weak_vs_strong_options.py
```

It runs the same 8 tickets twice: once with weak options, once with strong ones.
Compare the accuracy and the confidence.

---

## Common mistakes

- **Options that overlap.** "Payments" and "Billing" as two options. Merge them or explain the difference.
- **Instructions and options that disagree.** The question says one thing, the options say another. Jev gets confused.
- **Double negatives.** "Is it not untrue that…" Just ask directly.

---

## Quiz

<details><summary>1. What's the fastest way to improve accuracy?</summary>

Write clear option descriptions, with what each one covers and what it doesn't.
</details>

<details><summary>2. Why add a "not_for" field?</summary>

It handles the edge cases where two options look similar. That's where most mistakes happen.
</details>

<details><summary>3. Your state has a 5-page document but the question is about one paragraph. What do you do?</summary>

Send only the paragraph that matters. Extra text lowers accuracy.
</details>

---

Next: [06 · Many questions, one call →](../06-many-questions-one-call)
