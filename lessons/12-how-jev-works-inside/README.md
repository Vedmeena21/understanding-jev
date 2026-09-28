# 12 · How Jev works inside

⏱ 20 min · 🎯 Advanced · 🧪 Code: [`code/toy_answer_head.py`](code/toy_answer_head.py) (no API key needed)

[← 11 · Cost and speed math](../11-cost-and-speed-math) · [All lessons](../README.md)

---

## What you'll learn

- How an LLM answers, in 2 stages
- The one change that (likely) makes Jev different
- How Jev was probably trained

---

## First, an honest note

TypeSafe hasn't published a paper, a dataset or its architecture.
So this lesson is **informed guessing** from public clues.
It could turn out wrong.

You don't need this to use Jev. But it's fun, and it explains a lot.

---

## The 8 clues we have

1. It's **transformer-based**.
2. It has **broad world knowledge**. You can ask it about anything.
3. It's built for **System 1 tasks**. Not a giant model.
4. It's trained on **synthetic data** (TypeSafe says so).
5. It's **non-autoregressive**. It doesn't write word by word.
6. Output is **schema-constrained**. Only your options.
7. Questions run **in parallel**.
8. Confidence is **calibrated** with **RLCD**.

---

## How an LLM answers: 2 stages

**Stage 1: Prefill**

- Your question goes through the model's layers.
- It becomes numbers (vectors) the model understands.
- Goal: **understand the question**.

**Stage 2: Decode**

- Now it writes. **One token at a time.**

```
What is the capital of India?
→ "The" → "capital" → "is" → "New" → "Delhi" → "."
```

- At every step, the **LM head** scores **every word it knows**.
- The top word wins. Then it repeats.
- A **softmax** turns scores into probabilities that add up to 1.

---

## What Jev (likely) changes

- **Prefill stays.** Jev still understands your question.
- The LM head is **swapped** for an **answer head**.
- The answer head scores **only your options**.
- Softmax over those options → probabilities.
- **One step.** No writing loop.

```
                      ┌─ LLM: LM head → score every word → repeat, word by word
state + question → prefill
                      └─ Jev: answer head → score only your options → done
```

That one change explains:

| Clue | Why |
|---|---|
| Fast | One step instead of many |
| Output is free | There's no generated text |
| Always one of your options | The head only scores your options |

---

## Encoder or decoder?

- Jev **classifies**, like BERT (an encoder).
- But BERT needs fine-tuning for every task. Jev doesn't.
- One independent analysis reported about **84.6% on MMLU**, a world-knowledge test.
- Knowledge like that usually comes from big **decoder** models (GPT-style).

Best guess: **a decoder-based transformer that doesn't generate text.**

---

## How it was (probably) trained

1. Start from a strong **open-source pre-trained model**.
2. Keep the "understanding" layers.
3. Replace the output layer with an **answer head**.
4. Train on **synthetic** examples: question + options + right answer.
5. Train again with **RLCD**, so confidence becomes honest.

Why only synthetic data?
Training a model from scratch needs huge amounts of real-world text.
"Only synthetic" suggests they started from an existing model.

The founder calls TypeSafe **"a data lab, not a model lab"**.

---

## RLHF vs RLCD

| | RLHF | RLCD |
|---|---|---|
| Full name | RL from Human Feedback | RL for Calibrated Decisions |
| Rewards | Answers people like | Honest probabilities |
| Made | ChatGPT good at chatting | Jev honest about how sure it is |

Exact RLCD details aren't public.
Open versions like [Laya](https://github.com/NandhaKishorM/laya) use **proper scoring rules** (like the Brier score) that punish confident wrong answers.

---

## Try it

```bash
python code/toy_answer_head.py
```

A tiny toy, no key needed:

- The "LLM" writes *The capital is New Delhi.* in **6 steps**.
- The "answer head" scores 4 cities in **1 step**.

---

## Go deeper

Read and run open versions of the same idea:

- [NanoJev](https://github.com/TianyuCodings/NanoJev): a tiny Jev replica with a full training pipeline. **Start here.**
- [kev](https://github.com/jaredpalmer/kev): Jev-like models on Qwen you can train and run
- [Laya](https://github.com/NandhaKishorM/laya): an open decision model that did this before Jev
- Build one yourself: [projects/advanced/mini-jev](../../projects/advanced/mini-jev)

---

## Quiz

<details><summary>1. What are the 2 stages of an LLM answering?</summary>

Prefill (understand the question) and decode (write the answer token by token).
</details>

<details><summary>2. What does the answer head score?</summary>

Only the options you gave, not every word the model knows.
</details>

<details><summary>3. Why does this make the output free?</summary>

No text is generated, so there are no output tokens to pay for.
</details>

---

🎉 You finished the lessons. Now build something: [projects →](../../projects)
