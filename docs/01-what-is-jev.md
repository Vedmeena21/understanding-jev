# 01 · What is Jev?

[← Back to README](../README.md) · Next: [02 · How Jev works →](02-how-jev-works.md)

---

## The one-line answer

Jev is an AI model by **TypeSafe AI**.
But it's **not an LLM**.

- An LLM (ChatGPT, Claude, Gemini) **writes**.
- It generates text, token by token.
- Jev **decides**.
- It can't write text at all.

> TypeSafe calls it "a frontier-intelligence function call:
> unstructured state in, typed probabilistic decisions out."

---

## A simple example

A customer writes to your support bot:

> "My package arrived damaged and I want a refund."

You send Jev 3 things:

| What you send | Example |
|---|---|
| **State** (the context) | The customer's message |
| **Question** | Which team should handle this? |
| **Options** | Billing / Shipping / Technical / General |

Jev replies: **Shipping.**

How?

- It gives every option a **probability**.
- The highest one wins.
- It also tells you how **confident** it is overall.

Did you train it on your data? **No.**
You just gave it text, a question and options.

---

## "Isn't that just a classifier?"

Yes. But a **generalized** one.

| Old classifiers | Jev |
|---|---|
| Collect your data | Send your text |
| Label it | Send your question |
| Train a model | Send your options |
| Then predict | Get the answer |

- Old classifiers (logistic regression, BERT) needed training for every task.
- Jev already knows about the world.
- Ask any question. Give any options.
- **Classification as a service.**

---

## "An LLM can do this too"

True.
Give an LLM the same message and 4 options.
It will answer too.

So why Jev?

| | LLM | Jev |
|---|---|---|
| Output | A string you have to parse | A typed value: choice, score or yes/no |
| Speed | Seconds | Milliseconds |
| Cost | Pay for input + output | Pay for input. Output is free |
| Many questions | One at a time | All at once, in parallel |
| Confidence | Often faked | Trained to be honest (RLCD) |
| Wrong format | Possible ("Returns & Refunds", extra JSON) | Impossible. Always one of your options |

---

## System 1 vs System 2

This idea comes from the book ***Thinking, Fast and Slow*** by **Daniel Kahneman**.

Your brain has 2 modes:

| | System 1 | System 2 |
|---|---|---|
| Speed | Fast | Slow |
| How | Instinct | Deep reasoning |
| Example | A car cuts in front of your bike. You swerve. | "Where do I want my career in 5 years?" |

- Today's LLMs are **System 2** models.
- They reason, plan, then answer.
- But most decisions inside software are small:
  - Send this email to billing or support?
  - Which AI model should answer this question?
  - Which of my agent's 10 tools fits this task?
  - Is this comment spam?

No deep reasoning needed. Just a quick, correct call.

Using an LLM there means:

- More time
- More tokens
- More money

TypeSafe's core idea:

> Software needs **System One** thinking.
> We keep building **System Two**.

**Jev = System 1 for software.**

---

## Who built it?

- **Diogo Almeida**, founder of TypeSafe AI.
- Ex-OpenAI researcher.
- Worked on **InstructGPT** and **RLHF**, the work behind ChatGPT.
- TypeSafe ran in **stealth for about 2 years**.
- Jev launched on **15 September 2026**, with a **$40M seed round** led by DCVC.

---

## Why did he build it?

His question:

> Models have been superhuman at chat for years.
> So where is all the automation?

- LLMs got great at talking to **humans**.
- Software needs something that talks to **code**.
- Reasoning models can solve very hard problems.
- But they still fail to reliably automate basic work.

His phrase for it: **"Prod, not God."**

- Jev isn't trying to be a genius.
- It's built to run inside production software.
- Millions of times. Cheaply. Reliably.

---

## What changes because of Jev?

**1. AI becomes an `if` statement**

```python
# the idea
if is_angry(email).confidence > 0.9:
    escalate(email)
```

- Today, adding AI to software is a big deal.
- Slow calls. Token costs. Parsing.
- With Jev, a decision is just a function call.

> AI stops being the product.
> It becomes the plumbing.

**2. LLMs and Jev work together**

| Job | Who does it |
|---|---|
| Plan the task | LLM |
| Write text, code, emails | LLM |
| Pick a tool | Jev |
| Route to a model | Jev |
| "Is this step safe?" | Jev |
| Filter, sort, score, verify | Jev |

> A big model plans.
> Cheap decision models run every step in between.

**3. The trade-off is your job**

- Fast thinking → more mistakes possible.
- Slow thinking → fewer mistakes, more time.
- Jev is fast, not super smart.
- LLMs are smart, not fast.
- Knowing where each one goes is the new skill.

---

## Quick recap

- Jev is a **decision model**, not a text generator.
- You send **state + questions + options**.
- You get **typed answers + probabilities + confidence**.
- It's a **generalized classifier**. No training needed.
- Built for **System 1** tasks: fast, small, repeated decisions.
- It works **with** LLMs, not instead of them.

Next: [02 · How Jev works →](02-how-jev-works.md)
