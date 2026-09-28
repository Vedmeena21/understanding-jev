# 07 · Reality check

[← 06 · Projects to build](06-projects.md) · [Back to README](../README.md)

What's real. What's hype. What's next.

---

## Official claims vs independent tests

| Claim | TypeSafe says | Independent tests found |
|---|---|---|
| **Speed** | 40x–200x faster than LLMs on System One tasks | **2.9x** faster than Claude Haiku 4.5. **9.9x** faster than Claude Fable 5.1. About the same as GPT-5.6 Luna. Slower than a local Gemma 4 26B |
| **Cost** | Up to 444x cheaper in their evals | **12x** cheaper than Haiku 4.5. **18.6x** cheaper than the median of 19 LLMs. Dearer than DeepSeek on one task |
| **Accuracy** | Similar to frontier LLMs on System One tasks | Level with **mid-price LLMs**. Behind the frontier. **11.6 F1 points** behind the best LLM per task in a 7,977-item study |
| **Valid output** | Type errors "mathematically impossible" | **0 invalid answers** in 23,703 calls ✅ |
| **Calibration** | Honest probabilities | Best out-of-the-box on familiar English tasks. Over- or under-confident on others |
| **Hallucination** | Zero | Can't break format. **Can** be confidently wrong |

Sources: [TypeSafe launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · [8 days of independent tests](https://dev.to/aws-builders/jev-after-eight-days-of-independent-tests-level-with-mid-price-llms-behind-the-frontier-1c60)

**Bottom line:**

- Fast and cheap? **Yes.** Just not 200x in most real tests.
- As smart as the best LLMs? **No.** Mid-level.
- Always a valid answer? **Yes.**
- Never wrong? **No.**

TypeSafe itself says its speed numbers come from its own team's workflow evals, and that its "zero hallucination" claim isn't empirical.

---

## "Can't hallucinate"? Not quite.

The most debated claim at launch.

- Jev **can't** invent an option. Output always fits your schema. ✅
- But it **can** pick the wrong option with high confidence. ❌
- Example from testing: asked about a fair die roll that wasn't in the text, it said **83%** when the true answer was **17%**.

So:

- No **format** errors.
- Still **judgment** errors.
- Always keep a human or a bigger model for low confidence.

---

## Where Jev is strong

- Yes/no and few-option decisions
- Familiar English tasks
- Spam and phishing: **98.33%** on 18,514 emails
- Reranking: **0.692** vs 0.691 for a dedicated reranker
- Stable: only 1–2% of answers change between identical runs
- Huge volume at tiny cost

## Where Jev is weak

- **Option names:** renaming options changed ~32.5% of answers in one study
- **Non-English:** Russian dropped 11 points, Spanish 3–6 points
- **Counting, numbers, dates:** do these in code
- **Missing info:** confidently guesses when the answer isn't in the text
- **Big multi-class sets:** tends to be overconfident

Fix for calibration: fit a simple "temperature" on 50 to a few hundred of your own labeled examples. It cut calibration error by about 74% in testing.

---

## The downsides

**1. Black box**

- No reasoning. No explanation.
- Just a number.
- You can't see **why** it chose something.

**2. Bias risk**

- Simon Willison warns about using it for high-stakes calls like **hiring**.
- A model that returns only a score can hide bias.
- Don't use it alone for loans, jobs or legal decisions.

**3. Closed**

- No paper. No dataset. No model size. No base model. No RLCD details.
- Just a website and an API.
- Open alternatives are catching up fast.

**4. Text only**

- No images, audio or video yet.
- Workaround: turn screens and states into text or JSON.

**5. No web search**

- It only knows what it learned in training.
- Put fresh facts in the state yourself.

**6. Not very intelligent**

- It's a System 1 model by design.
- Fast, cheap, good enough for small calls.
- Not for deep reasoning.

---

## Jev wasn't the first

- **Laya** by **Nandakishor Mukkunnoth** (Convai Innovations, India) did a similar thing earlier.
- A non-autoregressive decision model trained with RL against proper scoring rules.
- Research from **March 2025**. Open weights and a dataset.
- He wrote: [I built non-autoregressive decision models a year ago. Then a frontier lab called it a "breakthrough"](https://dev.to/nandakishor_m_6cc0adfde9f/i-built-non-autoregressive-decision-models-a-year-ago-then-a-frontier-lab-called-it-a-18me)
- Jev got the spotlight partly because of its founder's OpenAI background.

Laya today → [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) (27.6k ⭐)

---

## What happens next

My predictions for the next 6 months to 2 years.

**1. Everyone copies it.**
Open-source versions appeared within days. Expect OpenAI, Anthropic and others to ship their own decision models.

**2. It disappears into platforms.**
Cloud and dev platforms will use decision models behind the scenes. You won't even know.

**3. LLMs + decision models become the standard stack.**
A big model plans. Cheap decision models run every step. In agents, RAG apps and normal software.

**4. Tooling grows around it.**
Tracing, evals, threshold tuning. LangSmith and Langfuse already support Jev.

**5. A new role: decision engineer.**
Someone who decides where to use decision models, which options to give, and what thresholds to set.

**6. Multimodal and more.**
TypeSafe has said multimodal, computer use and real-time work are priorities. A reasoning version ("ReasoningJev") has been teased.

**7. A new kind of software.**
Decisions so cheap they run on **every click and keystroke**. Apps that react to what you mean, instantly.

---

## Final thought

- Before: we used slow, costly LLMs for every small decision.
- Now: fast, cheap decisions are unlocked.
- The skill that matters is knowing **which decisions to hand over**.

**Not noise. Signal.**

[Back to README](../README.md)
