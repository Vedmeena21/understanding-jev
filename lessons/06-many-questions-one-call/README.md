# 06 · Many questions, one call

⏱ 15 min · 🎯 Beginner · 🧪 Code: [`code/many_questions.py`](code/many_questions.py)

[← 05 · Writing great options](../05-writing-great-options) · [All lessons](../README.md) · [07 · Jev in RAG →](../07-jev-in-rag)

---

## What you'll learn

- How Jev answers many questions at the same time
- Why that saves time and money
- The "fan-out" pattern

---

## One email, 8 questions

With an LLM, you usually ask **one question at a time**.

With Jev, you ask **all of them together**:

| Question | Type |
|---|---|
| Which team? | Choice |
| Wants a refund? | Noul |
| Urgent? | Noul |
| Contacted us before? | Noul |
| Legal risk? | Noul |
| Damaged item? | Noul |
| How angry? | Score |
| How soon to reply? | Score |

- **1 call.**
- All 8 answered **in parallel**.
- About the same time as **1 question**.

---

## Why it's fast

- Each question is handled **on its own**, side by side.
- Question 1 doesn't wait for question 2.
- Question 1 doesn't even see question 2.

## Why it's cheap

- You send the email **once**, not 8 times.
- Output is free anyway.
- 8 separate calls = the email's tokens paid 8 times.

---

## The fan-out pattern

Ask **more** questions than you think you need.
Let your code decide which answers to use.

```
one ticket → 8 questions in 1 call
code: if legal_risk > 0.7 → escalate
      elif wants_refund > 0.8 → refund flow
      else → route by team
```

TypeSafe calls this **speculative fan-out**.
In one of their cookbooks, batching made a task **12.2x cheaper and 10x faster**.

---

## Try it

```bash
python code/many_questions.py
```

It asks the same 8 questions two ways:

- 1 call with 8 questions
- 8 calls with 1 question each

Then prints the time and input tokens for both.

---

## Common mistakes

- **Chaining calls you don't need to.** If questions don't depend on each other, send them together.
- **Expecting answers to "agree".** Each question is independent. "Urgent" and "reply today" won't always match.
- **Too much state.** 20 questions on a 30-page document is slow. Send only what's needed.

---

## Quiz

<details><summary>1. Does asking 8 questions take 8x longer?</summary>

No. They run in parallel, so it's close to the time of 1.
</details>

<details><summary>2. Why is 1 call with 8 questions cheaper than 8 calls?</summary>

You pay for the input once, not 8 times. Output is free.
</details>

<details><summary>3. Can question 3 use the answer to question 1?</summary>

No. Questions are independent. If one depends on another, make two calls.
</details>

---

Next: [07 · Jev in RAG →](../07-jev-in-rag)
