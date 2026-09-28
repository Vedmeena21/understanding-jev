# 02 · Your first call

⏱ 10 min · 🎯 Beginner · 🧪 Code: [`code/`](code)

[← 01 · What is Jev](../01-what-is-jev) · [All lessons](../README.md) · [03 · Choice, Score and Noul →](../03-choice-score-noul)

---

## What you'll learn

- The shape of every Jev call
- How to call Jev from Python, TypeScript and curl
- How to read the answer

---

## Every call looks like this

```
state      (your text or JSON)
   +
questions  (each with a type and options)
   ↓
answers    (typed values + probabilities + confidence)
```

That's it. Nothing else.

---

## Python

```python
from typesafe_sdk import Choice, TypeSafeClient

client = TypeSafeClient()  # reads TYPESAFE_API_KEY

response = client.system_one(
    state="My package arrived damaged and I want a refund.",
    questions={
        "team": Choice(
            instructions="Which team should handle this",
            criteria={
                "billing": "Payments, invoices, charges",
                "shipping": "Delivery, damaged or lost packages",
                "technical": "Bugs or app problems",
                "general": "Anything else",
            },
        ),
    },
)

answer = response.answers["team"]
print(answer.choice)         # shipping
print(answer.probabilities)  # a probability for every option
print(answer.confidence)     # how sure it is, 0 to 1
```

Run it:

```bash
python code/first_call.py
```

---

## TypeScript

```bash
npm install @typesafe-ai/sdk
npx tsx code/first_call.ts
```

## curl (any language)

```bash
bash code/first_call.sh
```

---

## Read the answer

| Field | What it means |
|---|---|
| `.choice` | The option Jev picked |
| `.probabilities` | A probability for every option. They add up to 1 |
| `.confidence` | How sure Jev is, from 0 to 1 |

Try this:

- Change the message to *"I was charged twice this month."*
- Run it again.
- Watch the choice move to **billing**.

---

## Common mistakes

- **Forgetting the key.** Run `export TYPESAFE_API_KEY=...` in the same terminal.
- **Options with no descriptions.** `{"billing": None}` works, but good descriptions make answers better. (More in lesson 05.)
- **Asking Jev to write.** It can't. Ask it to pick.

---

## Quiz

<details><summary>1. What are the two things every call needs?</summary>

A `state` and at least one question.
</details>

<details><summary>2. Where do you find the picked option?</summary>

`response.answers["your-question-name"].choice`
</details>

<details><summary>3. Do the probabilities add up to 1?</summary>

Yes. One probability per option, and together they make 1.
</details>

---

Next: [03 · Choice, Score and Noul →](../03-choice-score-noul)
