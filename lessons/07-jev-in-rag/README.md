# 07 · Jev in RAG

⏱ 20 min · 🎯 Intermediate · 🧪 Code: [`code/rag_with_jev.py`](code/rag_with_jev.py)

[← 06 · Many questions, one call](../06-many-questions-one-call) · [All lessons](../README.md) · [08 · Jev in agents →](../08-jev-in-agents)

---

## What you'll learn

- 3 places Jev fits in a RAG app
- How to filter retrieved passages
- How to check if an answer is backed by sources

---

## Quick reminder: what is RAG?

**RAG** = Retrieval-Augmented Generation.

1. A question comes in.
2. You **retrieve** some passages from your documents.
3. An LLM **writes** an answer using those passages.

The LLM does the writing. But there are small decisions all around it.
That's where Jev fits.

---

## 3 places to use Jev

```
question
   ↓
① ROUTE     Jev: company docs? web search? no lookup?
   ↓
retrieve passages
   ↓
② FILTER    Jev: which passages actually help?
   ↓
LLM writes the answer
   ↓
③ CHECK     Jev: is every claim backed by a source?
```

### ① Route

- Not every question needs a search.
- Jev picks: **company docs**, **web search**, or **no lookup**.
- Fewer wasted searches. Fewer LLM calls.

### ② Filter

- Retrieval brings back 10 passages. Maybe 3 help.
- Jev **scores each one** for relevance. In one call.
- Only the good ones go to the LLM.
- Less noise. Better answers. Cheaper LLM call.

### ③ Check

- After the LLM answers, ask Jev:
  *"Is every claim in this answer supported by the sources?"*
- Low score → don't show it, or regenerate.

---

## Point at parts of the state

Put everything in JSON and point at it by name:

```python
state = {"question": question, "passages": passages}

Score(instructions="How useful is `passages[2]` for answering `question`", ...)
```

- Backticks tell Jev exactly which part to look at.
- One Score per passage. All in one call.

---

## Try it

```bash
python code/rag_with_jev.py
```

It routes one question, filters 4 passages, and checks a sample answer.

---

## Real-world versions

- [TypeSafe cookbook: classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages.md)
- [TypeSafe cookbook: citation check](https://docs.typesafe.ai/cookbooks/citation_check.md)
- [TypeSafe cookbook: rerank](https://docs.typesafe.ai/cookbooks/rerank_typesafe.md)

---

## Quiz

<details><summary>1. Name the 3 places Jev fits in a RAG app.</summary>

Routing the question, filtering passages, and checking the final answer.
</details>

<details><summary>2. Why filter passages before the LLM?</summary>

Less noise means better answers, and fewer tokens means a cheaper LLM call.
</details>

<details><summary>3. Can Jev write the final answer?</summary>

No. The LLM writes. Jev decides and checks.
</details>

---

Next: [08 · Jev in agents →](../08-jev-in-agents)
