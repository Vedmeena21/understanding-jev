---
name: jev-audit
description: Scan a codebase for LLM calls that are really decisions (classify, route, yes/no, score, pick one) and could move to Jev, TypeSafe's decision model, with estimated savings. Use when the user asks where Jev could help, how to cut LLM costs, or to audit LLM usage.
---

# Audit a codebase for Jev opportunities

Find LLM calls that only **decide**, not **write**. Those can move to Jev: faster, cheaper, always a valid answer.

## Step 1: Find every LLM call

Search for common SDK calls and prompts, for example:

- `chat.completions.create`, `responses.create`, `messages.create`, `generate_content`
- `ChatOpenAI`, `ChatAnthropic`, `llm.invoke`, `generateText`, `generateObject`
- Prompt strings containing: "classify", "categorize", "which of", "choose", "yes or no", "true or false", "rate", "score", "is this", "does this", "respond with one of"

## Step 2: Sort each call

| Signal | Verdict |
|---|---|
| Output is one label from a fixed list | ✅ Strong Jev candidate (Choice) |
| Output is yes/no, true/false | ✅ Strong candidate (Noul) |
| Output is a rating on a fixed scale | ✅ Strong candidate (Score) |
| Structured output with only enums/booleans | ✅ Strong candidate (several questions, one call) |
| Output is parsed with regex or `.strip().lower()` into a label | ✅ Strong candidate |
| Writes text, code, summaries, explanations | ❌ Keep the LLM |
| Needs multi-step reasoning or tools | ❌ Keep the LLM |
| Needs images, audio or video | ❌ Keep the LLM (Jev is text only) |
| Counting, dates, math | ⚠️ Do it in code instead |

## Step 3: Estimate the savings

For each candidate, estimate calls per day (ask, or look for loops, queues, cron jobs).
Jev pricing: $0.042 per 1M input tokens, output free. Speed: roughly 70–500 ms per request (TypeSafe's number).
Say clearly that savings are estimates, and that independent tests show smaller gains than TypeSafe's headline claims.

## Step 4: Report

```
Jev audit: 4 candidates, 2 to keep on the LLM

✅ app/support/router.py:42     classify ticket → 5 teams        Choice      ~20k calls/day
✅ app/moderation/check.py:18   "is this toxic? yes/no"          Noul        ~80k calls/day
✅ app/search/rerank.py:77      "rate relevance 1-5" per result  Score ×10   ~5k calls/day
⚠️ app/billing/due.py:30        "is the invoice overdue?"        → do the date math in code
❌ app/emails/reply.py:55       writes the reply                 keep the LLM
```

Then suggest the first one to migrate: the highest volume with the simplest options.
Offer to run `jev-migrate` on it.
