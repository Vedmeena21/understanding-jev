# 01 · What is Jev?

⏱ 15 min · 🎯 Beginner · 🧪 No code in this lesson

[← 00 · Setup](../00-setup) · [All lessons](../README.md) · [02 · Your first call →](../02-your-first-call)

---

## What you'll learn

- What Jev is, in one line
- How it's different from an LLM
- Why it was built (System 1 vs System 2)

---

## The one-line answer

Jev is an AI model by **TypeSafe AI**.
But it's **not an LLM**.

- An LLM (ChatGPT, Claude, Gemini) **writes**. Word by word.
- Jev **decides**. It can't write text at all.

---

## Let me explain with an example

A customer writes to your support bot:

> "My package arrived damaged and I want a refund."

You send Jev 3 things:

| You send | Example |
|---|---|
| **State** (the context) | The customer's message |
| **Question** | Which team should handle this? |
| **Options** | Billing / Shipping / Technical / General |

Jev replies: **Shipping.**

How?

- It gives every option a **probability**.
- The highest one wins.
- It also says how **sure** it is.

Did you train it on your data? **No.**
You just gave it text, a question and options.

---

## "Isn't that just a classifier?"

Yes. But a **generalized** one.

| Old classifiers | Jev |
|---|---|
| Collect data | Send your text |
| Label it | Send your question |
| Train a model | Send your options |
| Then predict | Get the answer |

Old classifiers needed training for every new task.
Jev already knows about the world.

**Classification as a service.**

---

## "But an LLM can do this too"

True. So why Jev?

| | LLM | Jev |
|---|---|---|
| Answer | Text you must parse | A typed value |
| Speed | Seconds | Milliseconds |
| Cost | Pay for input + output | Pay for input. Output is free |
| Many questions | One at a time | All at once |
| Confidence | Often faked | Trained to be honest |
| Wrong format | Possible | Impossible. Always one of your options |

---

## Why it was built: System 1 vs System 2

This idea comes from the book ***Thinking, Fast and Slow*** by Daniel Kahneman.

| | System 1 | System 2 |
|---|---|---|
| Speed | Fast | Slow |
| How | Instinct | Deep thinking |
| Example | A car cuts in front of your bike. You swerve. | "Where do I want my career in 5 years?" |

- LLMs are **System 2**. They think, plan, then answer.
- But most decisions inside software are small:
  - Send this email to billing or support?
  - Which AI model should answer this?
  - Is this comment spam?

Using an LLM there = more time, more tokens, more money.

TypeSafe's big idea:

> Software needs **System One** thinking.
> We keep building **System Two**.

**Jev = System 1 for software.**

---

## Who built it

- **Diogo Almeida**, ex-OpenAI researcher.
- Worked on **InstructGPT** and **RLHF**, the work behind ChatGPT.
- TypeSafe AI worked in secret for about 2 years.
- Jev launched on **15 September 2026**.

His question:

> Models have been superhuman at chat for years.
> So where is all the automation?

His phrase for Jev: **"Prod, not God."**
Not a genius. A reliable part you run a million times.

---

## What this changes

**AI becomes an `if` statement.**

```python
# the idea
if jev_says_angry(email).confidence > 0.9:
    escalate(email)
```

**LLMs and Jev work together.**

| Job | Who |
|---|---|
| Plan, write, explain | LLM |
| Pick, route, filter, check | Jev |

> A big model plans.
> Cheap decision models run every step in between.

---

## Quiz

<details><summary>1. What's the biggest difference between Jev and an LLM?</summary>

An LLM writes text. Jev can't write. It picks from the options you give it.
</details>

<details><summary>2. What 3 things do you send Jev?</summary>

The state (context), a question, and the options.
</details>

<details><summary>3. Is Jev System 1 or System 2? Why does that matter?</summary>

System 1: fast, small decisions. Most decisions in software are small, so a fast decision model saves time and money.
</details>

---

Next: [02 · Your first call →](../02-your-first-call)
