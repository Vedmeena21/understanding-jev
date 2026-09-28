---
name: jev-eval
description: Build and run an eval comparing Jev with the user's current LLM on accuracy, latency and cost, using their own labeled data. Use when the user asks "is Jev good enough for this?", "Jev vs GPT/Claude", or wants proof before switching.
---

# Eval: Jev vs your current LLM

Decide with numbers from the user's own data, not with marketing claims.

## Step 1: Set up

- **Data:** labeled examples (input + right answer). 50+ rows is good. Keep a few hard ones.
- **Question:** the exact Jev question(s) they'd use in production.
- **Baseline:** the LLM they use today, with its real prices.

## Step 2: Run both with the same code

TypeSafe's official adapter runs the same questions on an LLM:

```bash
pip install typesafe-sdk 'system-one-adapter[openai]'   # or [anthropic], [gemini]
```

```python
from typesafe_sdk import TypeSafeClient
from system_one_adapter import SystemOneAdapterClient

jev = TypeSafeClient()
llm = SystemOneAdapterClient(structured_outputs=True, llm_answer_mode="probabilities", normalize_probabilities=True)

jev.system_one(state=s, questions=q)
llm.system_one(state=s, questions=q, provider="openai", model="their-model")
```

If the adapter doesn't fit, call their LLM the way they do today.

## Step 3: Measure

For each client:

| Metric | How |
|---|---|
| Accuracy | right / total |
| Latency | median and p95, measured per call |
| Cost | input tokens × price (+ output tokens × price for the LLM). Jev output is free, input is $0.042 per 1M tokens |
| Invalid answers | how often the answer wasn't one of the options |
| Calibration | confidence buckets vs actual accuracy |

## Step 4: Report

```
                 Jev        your LLM
accuracy         94%        96%
median latency   180 ms     2.1 s
cost / 1k        $0.04      $3.10
invalid answers  0          3
```

Then give a plain verdict:

- Where Jev is good enough, and what it saves per month at their volume.
- Where it's worse, with 3 real examples of mistakes.
- A hybrid if it fits: Jev first, LLM only when Jev's confidence is low.

Be honest: independent tests put Jev level with mid-price LLMs and behind the frontier. Say so if their data agrees.
