# 04 · Build with Jev

[← 03 · Setup](03-setup.md) · Next: [05 · Use cases →](05-use-cases.md)

How to get good answers out of Jev.
Based on TypeSafe's own guides and what builders learned in the first weeks.

---

## The 5 golden rules

**1. Code owns the flow.**

- Rules, math, side effects → your code.
- Only the "common sense" judgment → Jev.

**2. One question = one judgment.**

- ❌ "Is this urgent and angry and about billing?"
- ✅ 3 separate questions. They run in parallel anyway.

**3. Send only what the decision needs.**

- Extra, unrelated text makes Jev less accurate.
- Filter first in code. Then ask.

**4. Facts come from your database, not the model.**

- Put current prices, policies and user data **in the state**.
- Don't hope the model "knows" them.

**5. Let confidence decide what happens next.**

- Sure → act.
- Unsure → ask again, use a bigger model, or ask a human.

---

## Write options like a pro

Options (criteria) matter more than the question.

**Weak:**

```python
criteria={"billing": None, "technical": None, "other": None}
```

**Strong:**

```python
criteria={
    "billing": "Payments, invoices, refunds, double charges",
    "technical": "Bugs, errors, failed integrations, outages",
    "other": "Anything that isn't billing or technical",
}
```

Even better, describe each option with the same fields:

| Field | What to write |
|---|---|
| `what` | What this option covers |
| `not_for` | What it does **not** cover |
| `examples` | 1 or 2 real examples |
| `signals` | Words or clues that point to it |

Tips:

- Use the **same fields** for every option so Jev can compare them.
- Say what makes **similar options different**.
- For Score, describe what **each level** looks like.

---

## Structure your state

**Weak:** one long string.

```python
state = "Customer Ravi, premium plan, says: I was charged twice..."
```

**Strong:** nested JSON.

```python
state = {
    "customer": {"name": "Ravi", "plan": "premium"},
    "ticket": {"message": "I was charged twice for May."},
}
```

- Point a question at one field with a path: `` `ticket.message` ``
- Give each question only the data it needs.

---

## 4 patterns to know

### 1. Speculative fan-out

Ask **many** questions at once, even ones you might not need.
Let your code pick the answers it uses.

```
One ticket → 8 questions in 1 call
  department? urgent? refund? language? angry? VIP? legal risk? spam?
Code uses only what the next step needs.
```

- Parallel = no extra wait.
- Cheaper than asking one by one.

### 2. Confidence routing

Use confidence as a **second decision**.

```
confidence high    → do it automatically
confidence medium  → ask a follow-up or call a bigger LLM
confidence low     → send to a human
```

- TypeSafe suggests escalating when confidence is **between 0.4 and 0.6**.
- Find your real thresholds by plotting **confidence vs accuracy** on your own labeled data.

### 3. Composite scoring

Big judgment = many small scores, combined in code.

```
"Is this a good lead?"
  = 0.4 × fits our customer profile
  + 0.3 × shows buying intent
  + 0.3 × company size score
```

- Each piece is a simple question.
- The final math is yours. Easy to explain and tune.

### 4. Intent routing

First classify **what the user wants**.
Then send it to the right handler.

```
user message → Jev: intent?
   ├─ "refund"   → refund workflow
   ├─ "bug"      → create ticket
   ├─ "question" → RAG + LLM answer
   └─ unsure     → human
```

- Put this in front of expensive LLMs.
- Only the requests that need an LLM reach one.

Docs: [Patterns](https://docs.typesafe.ai/patterns.md) · [19 cookbooks](https://docs.typesafe.ai/cookbooks.md)

---

## Known weak spots (and fixes)

From TypeSafe's own [Jev 1.13 known issues](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md).

| Weak spot | What happens | Fix |
|---|---|---|
| Reads literally | Doesn't guess what you "meant" | Say the exact condition. Put edge cases in the options |
| Counting | Can't count letters, words or items well | Count in code |
| Numbers | Weak with hex, RGB, "how close are these numbers" | Convert in code. Send meaning ("dark red"), not raw values |
| Score math | Can't give exact numbers between levels | Use scores for thresholds only |
| Dates and times | Reads dates as text, not as order | Extract parts as choices. Compare dates in code |
| Tricky wording | Double negatives and multi-step logic confuse it | Ask directly. Name the field you mean |
| Long, unrelated context | Accuracy drops | Filter first. Send only needed fields |
| Prompt injection | Text inside the state can steer it | Clear criteria. Test before production |
| Mixed signals | Question and options disagree → confused answer | Make them match |
| Related questions | "yes" and "no" versions won't always add up | Don't assume math between answers |
| Writing text | It's not built to write | Use an LLM for writing. Turn fixed answer sets into Choices |

Two more from independent tests:

- **Option names matter.** Renaming options changed about 1 in 3 answers in one study. Name them clearly.
- **Non-English is weaker.** English is best. Test other languages first.

---

## Before you ship: checklist

- [ ] Each question asks **one** thing
- [ ] Every option has a **clear description**
- [ ] State has **only** what's needed, as JSON
- [ ] Counting, dates and math happen **in code**
- [ ] You tested on **50+ real, labeled examples**
- [ ] You picked thresholds from **your** data
- [ ] Low-confidence answers go to a **human or a bigger model**
- [ ] You **trace** decisions (LangSmith, Langfuse or your own logs)

Next: [05 · Use cases →](05-use-cases.md)
