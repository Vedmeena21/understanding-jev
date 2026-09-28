---
name: jev-threshold
description: Pick confidence thresholds for Jev decisions from labeled data, so the app knows when to act automatically, when to double-check and when to ask a human. Use when the user asks what confidence cutoff to use, how much to automate, or how calibrated Jev is on their data.
---

# Pick confidence thresholds from real data

Never guess a threshold. Measure it on the user's labeled examples.

## Step 1: Get labeled data

- A CSV or JSONL with the input and the **right answer**, 50+ rows if possible (20 at minimum).
- If there's none, help the user label a small sample first. Real examples beat synthetic ones here.
- Ask what accuracy they need for automatic actions (for example 95% for routing, 99% for refunds).

## Step 2: Write and run a script

The script should:

1. Run every example through the user's real Jev question (same criteria as production).
2. Record `choice` (or `noul` / `score`), `confidence`, and whether it was right.
3. For thresholds 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, print:
   - **coverage**: share of examples at or above the threshold (handled automatically)
   - **accuracy**: share of those that were right
4. Print a calibration table: confidence buckets vs actual accuracy.

For `Noul`, use `abs(noul - 0.5) * 2` as a rough "how decided" value, or test cut-offs on `noul` directly.

Reference: `lessons/04-confidence-and-thresholds/code/find_threshold.py` in the understanding-jev repo.

## Step 3: Recommend 3 zones

```
confidence ≥ 0.85  → act automatically        (covers 78%, 97% accurate)
0.60 – 0.85        → double-check with a bigger model or a follow-up question
< 0.60             → send to a human
```

- Pick the **lowest** automatic threshold that meets the user's accuracy target.
- TypeSafe suggests escalating when confidence sits between 0.4 and 0.6.
- Use a separate threshold for each question.

## Step 4: Warn about

- Small samples: thresholds from 20 rows are rough. Re-check with more data.
- Other languages: calibration is best in English.
- Drift: re-run when the data or the options change.
- If calibration is off, fitting a simple temperature on a few hundred labels can help a lot.
