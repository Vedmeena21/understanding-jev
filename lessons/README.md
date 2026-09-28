# Lessons

13 short lessons. From "what is Jev?" to "how does it work inside?".
Each lesson has a simple explanation, code you can run, and a 3-question quiz.

![The Jev roadmap](../assets/roadmap.svg)

---

## Track 1 · Use it

| # | Lesson | Time | You'll learn |
|---|---|---|---|
| 00 | [Setup](00-setup) | 10 min | Get a key. Install. Check it works |
| 01 | [What is Jev](01-what-is-jev) | 15 min | LLM vs Jev. System 1 vs System 2. Why it exists |
| 02 | [Your first call](02-your-first-call) | 10 min | One call in Python, TypeScript and curl |
| 03 | [Choice, Score and Noul](03-choice-score-noul) | 15 min | The 3 question types and what they return |
| 04 | [Confidence and thresholds](04-confidence-and-thresholds) | 20 min | When to trust an answer. How to pick a threshold |
| 05 | [Writing great options](05-writing-great-options) | 15 min | The #1 way to make Jev more accurate |
| 06 | [Many questions, one call](06-many-questions-one-call) | 15 min | Ask 10 questions for the price and time of 1 |

## Track 2 · Build with it

| # | Lesson | Time | You'll learn |
|---|---|---|---|
| 07 | [Jev in RAG](07-jev-in-rag) | 20 min | Route questions. Filter passages. Check citations |
| 08 | [Jev in agents](08-jev-in-agents) | 20 min | Pick tools. Check steps. Route models |
| 09 | [Guardrails and safety](09-guardrails-and-safety) | 15 min | Catch jailbreaks before your LLM sees them |
| 10 | [Evals and tracing](10-evals-and-tracing) | 20 min | Measure accuracy, speed and cost on your data |
| 11 | [Cost and speed math](11-cost-and-speed-math) | 10 min | Work out what Jev saves you. No key needed |

## Track 3 · Understand it

| # | Lesson | Time | You'll learn |
|---|---|---|---|
| 12 | [How Jev works inside](12-how-jev-works-inside) | 20 min | Prefill, decode, and the "answer head". No key needed |

---

## How each lesson works

1. **Read** the lesson README. Short lines. No heavy math.
2. **Run** the code in its `code/` folder.
3. **Change one thing** and run it again.
4. **Take the quiz** at the bottom. Answers are hidden. Click to see them.

## Before you start

- Python 3.10 or newer
- `pip install typesafe-sdk`
- A TypeSafe API key in `TYPESAFE_API_KEY` (see [lesson 00](00-setup))

Lessons 11 and 12 run without a key.
