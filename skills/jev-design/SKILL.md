---
name: jev-design
description: Turn a decision described in plain English into Jev (TypeSafe System One) questions and working code. Use when the user wants to classify, route, score, detect or verify something with Jev, or asks "how would I do X with Jev?".
---

# Design a Jev decision

The user describes a decision in plain words. You turn it into Jev questions and code that runs.

## Before you start

If you need the current API details, fetch `https://docs.typesafe.ai/llms.txt` and read the pages you need. Don't guess field names.

## Step 1: Understand the decision

Ask only what you can't infer:

- What's the **input**? (an email, a ticket, a log line, a web page as JSON)
- What **happens next** based on the answer? (route, block, escalate, rank)
- What does a **wrong answer** cost? (this sets how careful the thresholds must be)

## Step 2: Split it into atomic questions

One question = one judgment. Never combine two judgments in one question.

| If the answer is... | Use | Returns |
|---|---|---|
| One of N unordered options | `Choice` | `.choice`, `.probabilities`, `.confidence` |
| A level on an ordered scale | `Score` | `.score` (0 = first level), `.probabilities`, `.confidence` |
| Yes / no | `Noul` | `.noul` (probability 0 to 1) |

Questions run in parallel and don't see each other. If one depends on another, use two calls.
Ask speculative extra questions if they're cheap and useful (fan-out).

## Step 3: Write strong options

For every Choice option, use the same fields:

```python
"billing": {
    "what": "Money: charges, invoices, refunds, subscriptions",
    "not_for": "Payment pages that crash (that's technical)",
    "examples": ["Charged twice", "Refund not received"],
}
```

For Score, list levels from lowest to highest, each a short, clear description.
For Noul, write the instruction as a statement that's true or false.

## Step 4: Shape the state

- Prefer nested JSON over one long string.
- Include only what the decision needs. Extra text lowers accuracy.
- Put facts from the user's database in the state. Don't rely on model knowledge.
- Point questions at fields with backticks: `` "Is `ticket.message` about money?" ``

## Step 5: Write the code

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()  # reads TYPESAFE_API_KEY
response = client.system_one(state=state, questions=QUESTIONS)
answer = response.answers["name"]
```

- Code owns the control flow. Jev only judges.
- Add a confidence rule: act when sure, escalate (bigger model or human) when not.
- Do counting, dates and math in code, not in Jev.

## Step 6: Hand over

Give the user:

1. The questions, with one line on why each exists
2. The full runnable code
3. A starting threshold, and a note to tune it with `jev-threshold` on real labeled data

Keep explanations short and plain.
