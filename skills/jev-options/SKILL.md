---
name: jev-options
description: Improve the options (criteria) and instructions of existing Jev questions so answers get more accurate and less confused. Use when Jev answers are wrong or low-confidence, when two options get mixed up, or when the user asks to review their Jev questions.
---

# Improve Jev options

Jev reads options very literally. Better option descriptions are the fastest way to better accuracy.

## Step 1: Collect

- The current questions (`Choice`, `Score`, `Noul`) and their criteria
- If available: examples Jev got wrong, and what the right answer was

## Step 2: Check each question against this list

1. **One judgment per question.** Split "urgent and angry" into two questions.
2. **Every option has a description.** `None` or a bare name is weak.
3. **Same fields for every option:** `what`, `not_for`, `examples`, `signals`.
4. **Edge cases are named.** The look-alike cases go in `not_for`.
5. **No overlap.** If two options can both be right, merge them or explain the difference.
6. **Instructions and options agree.** Don't ask about "department" and list moods.
7. **No double negatives or indirect wording.** Ask directly.
8. **Clear option names.** Renaming options can change answers a lot. Use plain, specific names.
9. **Score levels are ordered** lowest to highest, each clearly different.
10. **Noul is a statement** that's true or false, not a vague question.
11. **The state holds only what's needed**, as JSON, with backtick paths in the instructions.

## Step 3: Rewrite

Show before and after, for example:

```python
# before
criteria={"billing": None, "technical": None}

# after
criteria={
    "billing": {
        "what": "Money: charges, invoices, refunds, subscriptions",
        "not_for": "Checkout pages that crash (that's technical)",
        "examples": ["Charged twice", "Refund not received"],
    },
    "technical": {
        "what": "Software problems: bugs, errors, crashes, login issues",
        "not_for": "Feature requests",
        "examples": ["App crashes on launch", "Error at checkout"],
    },
}
```

If there are wrong examples, explain which change fixes which mistake.

## Step 4: Prove it

Suggest re-running the same labeled examples before and after (see `jev-eval`), and comparing accuracy and average confidence.
