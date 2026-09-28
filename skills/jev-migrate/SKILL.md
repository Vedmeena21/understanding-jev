---
name: jev-migrate
description: Rewrite an existing LLM classification, routing, yes/no or scoring call into a Jev (TypeSafe System One) call, keeping the rest of the code working. Use when the user wants to replace a specific LLM call with Jev.
---

# Migrate an LLM call to Jev

Replace one LLM "decision" call with Jev, without breaking anything around it.

## Step 1: Read the current call

Find out:

- The prompt, and the **set of allowed answers** (often hidden in the prompt or a regex)
- How the answer is **parsed** and **used** afterwards
- What happens when the answer is invalid today
- How often it runs

If it writes free text, stop. It's not a Jev call. Say why.

## Step 2: Map it to Jev

| Old pattern | Jev |
|---|---|
| "Reply with one of: A, B, C" | `Choice` with A, B, C, each with a description |
| "Answer yes or no" / `bool` field | `Noul` |
| "Rate 1–5" / severity levels | `Score` with described levels |
| JSON schema with several enums/bools | Several questions in one `system_one` call |
| Prompt context / user message | `state` (prefer JSON) |

Move examples and definitions from the old prompt into option descriptions (`what`, `not_for`, `examples`).

## Step 3: Write the new code

```python
from typesafe_sdk import Choice, TypeSafeClient

client = TypeSafeClient()  # reads TYPESAFE_API_KEY

def classify_ticket(message: str) -> str:
    answer = client.system_one(
        state={"message": message},
        questions={"team": TEAM_QUESTION},
    ).answers["team"]
    if answer.confidence < THRESHOLD:
        return old_llm_classify(message)   # keep the LLM as a fallback at first
    return answer.choice
```

- Keep the **same function signature** so callers don't change.
- Remove regex parsing: Jev's answer is always one of the options.
- Start with the old LLM as a **fallback** for low confidence. Remove it later if the numbers allow.
- Add `typesafe-sdk` to the project's dependencies and `TYPESAFE_API_KEY` to its env docs.

## Step 4: Check

- Run the existing tests.
- Run 20+ real examples through old and new, and compare (or use `jev-eval`).
- Pick the threshold with `jev-threshold`.

Show the user a short diff summary: what changed, what stayed, and how to roll back.
