# 04 · Confidence and thresholds

⏱ 20 min · 🎯 Beginner · 🧪 Code: [`code/`](code)

[← 03 · Choice, Score and Noul](../03-choice-score-noul) · [All lessons](../README.md) · [05 · Writing great options →](../05-writing-great-options)

---

## What you'll learn

- What "confidence" really means
- How to let confidence decide what your app does
- How to pick a threshold from your own data

---

## Confidence = how sure Jev is

Every Choice and Score answer comes with a **confidence** from 0 to 1.

The special thing about Jev:

- It's trained to be **honest** about it.
- The training method is called **RLCD** (Reinforcement Learning for Calibrated Decisions).
- If Jev says **80% sure**, it should be right about **80% of the time**.

That's called being **calibrated**.

LLMs often sound very sure even when they're wrong.
Jev is trained not to.

---

## Picture it

- X-axis: how sure Jev **says** it is.
- Y-axis: how often it's **actually right**.
- Perfect = a straight diagonal line.

```
actual
accuracy
  1.0 |                 ●
      |             ●
      |         ●            ● = Jev (ideally on the line)
      |     ●
  0.0 |●_______________
      0.0             1.0   stated confidence
```

---

## Let confidence decide

This is the most useful pattern in all of Jev.

| Confidence | What your app does |
|---|---|
| **High** (e.g. above 0.9) | Act on it. Send the email to Billing |
| **Medium** (e.g. 0.6 to 0.9) | Ask a follow-up question, or call a bigger LLM |
| **Low** (e.g. below 0.6) | Send it to a human |

```python
answer = response.answers["team"]

if answer.confidence >= 0.9:
    route_to(answer.choice)
elif answer.confidence >= 0.6:
    ask_bigger_model(ticket)
else:
    send_to_human(ticket)
```

TypeSafe's own tip: escalate when confidence is **between 0.4 and 0.6**.

---

## Don't guess the threshold. Measure it.

The numbers above are examples.
Your real threshold depends on **your** data.

How:

1. Collect 20+ real examples with the **right answer** (labels).
2. Run them all through Jev.
3. For each threshold, check:
   - **Coverage:** how many Jev handles on its own
   - **Accuracy:** how many of those it gets right
4. Pick the lowest threshold that's accurate enough for you.

`code/find_threshold.py` does this for you.

---

## Try it

```bash
python code/confidence_router.py        # routes 5 tickets by confidence
python code/find_threshold.py           # finds a threshold on 24 labeled tickets
```

What the output of `find_threshold.py` looks like (your numbers will differ):

```
threshold  coverage  accuracy
   0.50      100%      92%
   0.70       88%      95%
   0.90       67%     100%
→ Lowest threshold with ≥ 95% accuracy: 0.70
```

---

## Common mistakes

- **Using one threshold for everything.** Each question needs its own.
- **Trusting confidence on new languages.** Calibration is best in English. Test first.
- **Never checking.** Re-run `find_threshold.py` when your data changes.

---

## Quiz

<details><summary>1. What does "calibrated" mean?</summary>

When Jev says it's X% sure, it's right about X% of the time.
</details>

<details><summary>2. Confidence is 0.45 on a refund decision. What should your app do?</summary>

Don't act automatically. Send it to a human (or a bigger model).
</details>

<details><summary>3. How do you choose a threshold?</summary>

Run labeled examples through Jev. Pick the lowest threshold that still gives the accuracy you need.
</details>

---

Next: [05 · Writing great options →](../05-writing-great-options)
