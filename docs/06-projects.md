# 06 · Projects to build

[← 05 · Use cases](05-use-cases.md) · Next: [07 · Reality check →](07-reality-check.md)

15 projects. Beginner to advanced.
Each one says what you build, which Jev questions you use, the steps, and a real repo to learn from.

| Level | Projects |
|---|---|
| 🟢 Beginner | 1–5: one call, a few questions |
| 🟡 Intermediate | 6–10: Jev inside a bigger tool |
| 🔴 Advanced | 11–15: real-time agents and your own model |

---

## 🟢 Beginner

### 1. Support ticket router

**Build:** A script that reads support emails and sends each one to the right team.

**Jev questions:**
- `Choice` → billing / shipping / technical / general
- `Noul` → is it urgent?
- `Score` → how angry is the customer?

**Steps:**
1. Put 20 sample emails in a CSV.
2. Ask all 3 questions per email, in one call.
3. Confidence below your threshold → "needs human" pile.
4. Print a table: email, team, urgent, anger, confidence.

**Learn from:** [official quickstart](https://docs.typesafe.ai/introduction/quickstart) · [`examples/quickstart.py`](../examples/quickstart.py)

---

### 2. Product review feature ratings

**Build:** Ratings per feature from raw reviews. Camera 3.0. Battery 3.5. Display 3.7. Like big shopping sites show.

**Jev questions (per feature):**
- `Noul` → does the review talk about this feature?
- `Score` → how happy is the reviewer with it? (5 levels)

7 features × 2 = **14 questions per review. One call.**

**Steps:**
1. Collect 50 reviews of one product.
2. Pick features: camera, battery, display, design, performance, build quality, value for money.
3. Ask 14 questions per review.
4. Keep a feature's score only if "mentioned" is above 0.5.
5. Average per feature. Show how many reviews mention each one.
6. Bonus: click a feature → see the reviews that mention it.

**No training. No fine-tuning. About 100 lines.**

**Learn from:** [`examples/review_ratings.py`](../examples/review_ratings.py)

---

### 3. Spam and phishing checker

**Build:** Paste an email. Get "phishing: 0.93" and a verdict.

**Jev questions:**
- `Noul` → is this phishing?
- `Noul` → does it ask for passwords or payment?
- `Choice` → safe / spam / phishing / scam

**Steps:**
1. Get a public spam dataset.
2. Run 500 emails through Jev.
3. Compare with the real labels. Measure accuracy.
4. Plot confidence vs accuracy. Pick your threshold.

**Why it's a great first eval:** one independent test hit **98.33%** on 18,514 emails.

---

### 4. AI slop detector (browser extension)

**Build:** A Chrome extension that puts a red banner on LinkedIn posts that look AI-written.

**Jev questions:**
- `Noul` → does this read like generic AI-generated text?
- `Score` → how much real, specific detail does it have?

**Steps:**
1. Content script grabs each post's text as you scroll.
2. Send it to a tiny backend that calls Jev.
3. Above your threshold → add a red banner.
4. Fast enough to feel instant.

**Learn from:** a community demo that went viral in the launch week.

---

### 5. Your first CLI with the LLM tool

**Build:** Ask Jev yes/no questions from your terminal.

```bash
llm install llm-typesafe
llm keys set typesafe
llm -m jev 'Please refund my last payment.' \
  -s 'Does this message explicitly request a refund?'
```

**Then:** pipe your git log, logs or notes into it. "Is this a breaking change?"

**Learn from:** [simonw/llm-typesafe](https://github.com/simonw/llm-typesafe)

---

## 🟡 Intermediate

### 6. Model router for coding agents

**Build:** A router that sends each task to the cheapest model that can handle it.

**Jev questions:**
- `Score` → how hard is this task?
- `Choice` → which model: small / medium / frontier?
- `Noul` → does it need deep reasoning?

**Steps:**
1. Sit between your agent and the model APIs.
2. Ask Jev before every turn.
3. Log cost saved vs always using the big model.

**Learn from:** [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) (472 ⭐) · [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)

---

### 7. Smarter context compaction

**Build:** A plugin that cleans up a long agent session without losing important details.

**Jev questions (per old message):**
- `Choice` → keep / truncate / drop

**Steps:**
1. Take the last N tool calls and results.
2. Score all of them in one request.
3. Drop the stale ones. Keep the rest **word for word**. No lossy summary.

**Learn from:** [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) (7.1k ⭐)

---

### 8. Semantic code search

**Build:** A CLI. You ask "where do we send telemetry?" It returns the right files.

**Jev questions:**
- `Score` → how relevant is this file to the question?

**Steps:**
1. List candidate files (by name or folder).
2. Score them all in parallel.
3. Return the top 5 with their snippets.
4. Give it to your coding agent as a skill.

**Learn from:** [dzhng/jevgrep](https://github.com/dzhng/jevgrep) (1.3k ⭐)

---

### 9. Document classifier

**Build:** Upload a PDF. Each page gets labeled with its exact form type.

**Jev questions:**
- `Choice` → which form is this page? (up to 255 options)

**Steps:**
1. Write a JSON file describing every form type.
2. Extract text per page.
3. One Choice per page.
4. Low confidence → flag for review.

**The trick:** the "model" is just good option descriptions. Nothing is trained.

**Learn from:** [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) (473 ⭐), 261 IRS forms at ~$0.001/page

---

### 10. LLM guardrail + reranker for RAG

**Build:** A safety and quality layer in front of your chatbot.

**Jev questions:**
- `Noul` → is this a jailbreak or prompt injection?
- `Score` → how relevant is each retrieved passage?
- `Noul` → does the answer's source support the claim?

**Steps:**
1. Screen every user prompt **before** the LLM sees it.
2. Score retrieved passages. Keep the top ones.
3. After the LLM answers, check citations.

**Learn from:** TypeSafe cookbooks: [LLM guardrails](https://docs.typesafe.ai/cookbooks/llm_guardrails.md) · [Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages.md) · [Citation check](https://docs.typesafe.ai/cookbooks/citation_check.md)

---

## 🔴 Advanced

### 11. Browser agent

**Build:** An agent that completes tasks on real websites. Fast.

**Jev questions (every step):**
- `Choice` → which element to act on? (numbered page elements)
- `Choice` → which action: click / type / scroll / done?

**Steps:**
1. Turn the page into a numbered list of elements (text, not screenshots).
2. Jev picks the element and action.
3. Playwright does it.
4. An LLM only plans and verifies.

**Learn from:** [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) (21.1k ⭐) · [jev-browser-use](https://github.com/wy-coliney/jev-browser-use) · [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)

---

### 12. Game-playing agent

**Build:** An agent that plays Super Mario, Subway Surfers or Doom in real time.

**Jev questions (every frame):**
- `Choice` → left / right / jump / duck / wait

**Steps:**
1. Read the game state (positions, enemies, gaps) from the emulator.
2. Turn it into JSON.
3. Ask Jev for the next move ~10 times a second.
4. Log and replay runs to improve your state format.

**Learn from:** [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) (413 ⭐) · TypeSafe's Doom bot in the [launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

---

### 13. Live "shape-shifting" UI

**Build:** One text box that turns into the right form as you type.
"Call mom at 5" → a reminder card. "Pay rent 20k" → a payment form.

**Jev questions (on every keystroke pause):**
- `Choice` → which card? (reminder / payment / note / meeting...)
- `Noul` × many → is it urgent? is it a video call? is it recurring?

**Learn from:** [anishfn/shapeshift](https://github.com/anishfn/shapeshift) (722 ⭐), 14 questions in one call

---

### 14. Agent safety layer + MCP server

**Build:** An MCP server that any agent calls before risky actions.

**Jev questions:**
- `Score` → how likely is this shell command to destroy data?
- `Noul` → does this action match the user's request?

**Steps:**
1. Expose tools like `check_command` and `verify_claim` over MCP.
2. Agent calls them before running anything risky.
3. Above threshold → block and explain.

**Learn from:** [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) (443 ⭐) · the "Jev guard" in [AgentiLoop/Agent](https://github.com/AgentiLoop/Agent)

---

### 15. Train your own Jev-like model

**Build:** A small decision model that runs on your own GPU.

**Steps:**
1. Start from a small open model (for example Qwen).
2. Swap the output layer for an **answer head** over the options.
3. Train on synthetic question + options + answer data.
4. Add calibration (a proper scoring rule like the Brier score).
5. Test it on [JevBench](https://github.com/fstandhartinger/jevbench).

**Learn from:**
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) (2.3k ⭐): nano replica with the full training pipeline. **Start here.**
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) (7.6k ⭐): Jev-like models on Qwen you can train and run
- [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) (876 ⭐): turn any LLM into a Jev-style model, no training
- [Liuziyu77/Valen](https://github.com/Liuziyu77/Valen) (436 ⭐): a Jev-like model **with vision**

---

## Portfolio tip

For any project, show 3 numbers:

1. **Accuracy** on labeled examples
2. **Latency** per decision
3. **Cost** per 1,000 decisions, vs an LLM doing the same job

That's what makes it stand out.

Next: [07 · Reality check →](07-reality-check.md)
