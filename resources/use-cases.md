# Use cases

[← Back to README](../README.md) · [All resources](README.md)

Where Jev fits. Where people already use it.

---

## The simple test

Use Jev when the answer is:

- ✅ **one of a few options** (which team? which tool?)
- ✅ **yes or no** (spam? safe? urgent?)
- ✅ **a rating on a scale** (how angry? how relevant?)
- ✅ needed **fast**, **cheap** or **millions of times**

Don't use Jev when you need:

- ❌ written text, code or summaries
- ❌ an explanation of **why**
- ❌ long multi-step reasoning
- ❌ images, audio or video (text only for now)

---

## 5 big areas

| Area | What Jev does there |
|---|---|
| **AI automation** | Small AI decisions inside normal software. Run a million times, no human watching |
| **Real-time apps** | Games, live UI, voice. Decisions in ~150 ms |
| **AI over big data** | Classify, search and tag huge datasets at a fraction of LLM cost |
| **Verification** | Check prompts, extractions, tool calls and outputs of other AIs |
| **Harness engineering** | Route models, pick context, catch errors around your LLM |

Source: [TypeSafe use-case map](https://docs.typesafe.ai/concepts/use-case-map.md)

---

## 10 decision types

| Type | Question it answers | Examples |
|---|---|---|
| **Classification** | Which category? | Intent, topic, department, risk type |
| **Detection** | Is this property there? | Spam, fraud, urgency, jailbreaks, sensitive data |
| **Scoring** | How much, on a scale? | Severity, relevance, quality, frustration |
| **Routing** | Where next? | Tool, model, support queue, escalation |
| **Search** | Which items match? | Semantic search, document discovery |
| **Retrieval** | Which context is most useful? | RAG passages, evidence |
| **Ranking** | What order? | Search results, candidates, recommendations |
| **Verification** | Did something go wrong? | Citation support, policy breaks, tool errors |
| **ML features** | What signals are in this text? | Purchase intent, churn risk |
| **Data extraction** | Which known value is it? | Order fields, document labels |

---

## By industry

| Industry | What Jev decides |
|---|---|
| **Customer support** | Ticket category. Urgency. Which queue. Is the reply correct? |
| **E-commerce** | Clean up listings. Pull product attributes. Spot rule-breaking items. Rank products |
| **Moderation / trust & safety** | Toxic or not. How severe. Allow or block |
| **LLM guardrails** | Jailbreak? Prompt injection? Policy break? Tool error? |
| **Model routing** | Which model? How hard is this request? Escalate? |
| **Search and retrieval** | Score relevance. Rerank results. Choose context for RAG |
| **Coding tools** | Semantic code linting in CI. Find relevant files. Review diffs |
| **Recruiting** | Resume fit. Experience level. Skills score |
| **Lead generation** | Matches ideal customer? Buying intent? Priority? |
| **Insurance claims** | Claim type. How complex. How risky |
| **Financial crime** | Suspicious transaction? Same entity? Which alerts first? |
| **Legal and compliance** | Document type. Violation? Requirement met? |
| **Advertising** | Brand-safe? Compliant? Creative quality? |
| **Gaming** | Chat moderation. Abuse. Churn signals. Game-playing agents |
| **Research / science** | Screen papers. Label transcripts. Verify citations |
| **Risk assessment** | Turn reports into risk scores and types |
| **Demand forecasting** | Pull intent and themes from text as model features |
| **Knowledge graphs** | Label relationships. Spot contradictions. Walk the graph |
| **ML teams** | Turn text into probability features for classic ML models |

---

## Inside AI agents

Agents make lots of small decisions.
Each one is a Jev question.

| Agent step | Who does it |
|---|---|
| Understand the goal and plan | LLM |
| Write the tool arguments | LLM |
| **Pick which tool to use** | Jev |
| **Before each step: is this safe? is it right?** | Jev |
| **Route to a cheap or a strong model** | Jev |
| **Decide what old context to drop** | Jev |
| Write the final answer | LLM |

**Agentic RAG example.** A question comes in. Jev decides:

- search internal docs?
- search the web?
- or answer directly?

Small decision. No LLM needed for it.

**Query routing with vector store info.** Give Jev a short description of each store. It picks where to look. Fewer LLM calls.

---

## Real demos people built

| Demo | What Jev decides | Link |
|---|---|---|
| **Web agent** | Which element to click next. Fastest, cheapest web agent | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) |
| **Flight booking agent** | Every click to book Zurich → London, in about 7 seconds | Community demo |
| **Voice browser** | Your intent and target, ~300 ms per spoken word | [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) |
| **Context compaction** | Which old messages to keep or drop in Claude Code | [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) |
| **Code search** | Which files match "what does this do?" | [jevgrep](https://github.com/dzhng/jevgrep) |
| **Code review** | Staged review of diffs, with a dashboard | [jev-review](https://github.com/devagrawal09/jev-review) |
| **Tax forms** | Which of 261 IRS forms a page is. ~$0.001/page | [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) |
| **Morphing input** | What you mean as you type. The box turns into the right UI | [shapeshift](https://github.com/anishfn/shapeshift) |
| **Shell safety** | Could this command destroy data? Block if risky | [AgentiLoop/Agent](https://github.com/AgentiLoop/Agent) |
| **Memory search** | Rerank which memories are relevant | [memsearch](https://github.com/zilliztech/memsearch) |
| **Trading** | Pre-trade go / no-go decisions | [QuantDinger](https://github.com/OpenByteInc/QuantDinger) |
| **Super Mario** | Next move from game state | [typesafe-mario](https://github.com/fhshaik/typesafe-mario) |
| **Doom** | Real-time moves, ~10 decisions/sec, ~$7/hour | [TypeSafe launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) |
| **Wikiracing** | Which link to click, out of hundreds | [TypeSafe launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) |
| **AI slop filter** | Is this LinkedIn post AI slop? Red banner if yes | Community demo |
| **Ad blocker** | Is this page element an ad? | Community demo |
| **Subway Surfers** | Left, right, jump, duck | Community demo |

**How do game demos work if Jev is text-only?**
They turn the game screen into text or JSON first. Then send that as the state.

---

## From the official cookbooks

Real recipes with numbers. All in the [TypeSafe cookbooks](https://docs.typesafe.ai/cookbooks.md).

| Cookbook | What it shows |
|---|---|
| Parallel questions | Regulatory briefings: **12.2x cheaper, 10x faster** with batching |
| Skill suggestion | Pick 1 skill out of a **182-option** catalog |
| Entity alignment | Match product pairs across **450** candidates |
| Rerank | Legal document reranking with better top-1 accuracy |
| Semantic find | Search a file by scoring it line by line |
| LLM guardrails | Screen messages and route hazards |
| Citation check | Does the source actually support the claim? |
| Classifying RAG passages | Keep only useful passages for retrieval |
| Hierarchical classification | Deep category trees with beam search |
| Function calling | Plain-English trading commands → typed function calls |
| Date extraction | Absolute and relative dates, done safely |
| SDE cascade | 2-stage extraction that cuts reasoning costs |

Build one yourself: [projects →](../projects)
