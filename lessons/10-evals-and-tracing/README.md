# 10 · Evals and tracing

⏱ 20 min · 🎯 Intermediate · 🧪 Code: [`code/mini_eval.py`](code/mini_eval.py)

[← 09 · Guardrails and safety](../09-guardrails-and-safety) · [All lessons](../README.md) · [11 · Cost and speed math →](../11-cost-and-speed-math)

---

## What you'll learn

- How to measure Jev on **your** data
- The 3 numbers that matter
- How to trace Jev decisions in production

---

## Don't trust claims. Measure.

TypeSafe says Jev is **40x–200x faster** than LLMs.
The most careful independent test found about **2.9x faster** and **12x cheaper** than Claude Haiku 4.5.

Both can be true. It depends on the task.
The only number that matters is **yours**.

---

## The 3 numbers

| Number | Question it answers |
|---|---|
| **Accuracy** | How often is it right? |
| **Latency** | How fast is it? |
| **Cost** | What does 1,000 decisions cost? |

Bonus: look at every **mistake**. That's where you learn.

---

## How to run an eval

1. Collect 20–200 real examples.
2. Write the **right answer** next to each one (the label).
3. Run them all through Jev.
4. Count what it got right. Time it. Add up the tokens.
5. Read the mistakes. Fix your options (lesson 05). Run again.

---

## Try it

```bash
python code/mini_eval.py
```

It runs 20 labeled messages through a spam check and prints:

```
Examples:        20
Accuracy:        …
Median latency:  … ms
Input tokens:    …
Cost:            $…  (≈ $… per 1,000 decisions)
Mistakes to look at: …
```

Use your own data: `python code/mini_eval.py my_data.csv`

---

## Compare with an LLM

TypeSafe's official [system-one-adapter](https://github.com/typesafe-ai/system-one-adapter-python) runs the **same Jev code on an LLM**.

```bash
pip install 'system-one-adapter[openai]'
```

- Same questions. Same data.
- Swap `TypeSafeClient` for `SystemOneAdapterClient`.
- Compare accuracy, speed and cost side by side.

---

## Tracing in production

Log every decision so you can check it later.

| Tool | What it gives you |
|---|---|
| [LangSmith](https://www.langchain.com/blog/jev-is-now-available-in-langsmith-evals) | Traces every Jev call inside your agent. Jev can also be an eval judge |
| [Langfuse](https://langfuse.com/integrations/model-providers/typesafe) | Open-source tracing for Jev calls |
| Your own logs | Save state, question, answer, confidence and time |

---

## Quiz

<details><summary>1. What are the 3 numbers every eval should report?</summary>

Accuracy, latency and cost.
</details>

<details><summary>2. Why read the mistakes?</summary>

They show which options are confusing, so you know what to fix.
</details>

<details><summary>3. How can you compare Jev with an LLM using the same code?</summary>

Use TypeSafe's system-one-adapter, which runs the same questions on an LLM.
</details>

---

Next: [11 · Cost and speed math →](../11-cost-and-speed-math)
