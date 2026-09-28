# Jev reading list

[← Back to README](../README.md)

The articles, talks and docs worth your time.
Sorted by what you need.

---

## Contents

1. [Start here (official)](#start-here-official)
2. [Deep dives and opinions](#deep-dives-and-opinions)
3. [Independent tests and reviews](#independent-tests-and-reviews)
4. [Tutorials](#tutorials)
5. [Integrations](#integrations)
6. [Open alternatives and the research behind them](#open-alternatives-and-the-research-behind-them)
7. [Background](#background)

---

## Start here (official)

| Read | Why |
|---|---|
| [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | The launch post (15 Sep 2026). Claims, demos, pricing |
| [TypeSafe docs](https://docs.typesafe.ai/introduction) | Start of the official docs |
| [Quick start](https://docs.typesafe.ai/introduction/quickstart) | First call in 5 minutes |
| [Use-case map](https://docs.typesafe.ai/concepts/use-case-map.md) | 19 industries, 10 decision types |
| [How to build with System One](https://docs.typesafe.ai/concepts/how-to-build-with-system-one.md) | The design rules |
| [Patterns](https://docs.typesafe.ai/patterns.md) | Fan-out, confidence routing, composite scoring, intent routing |
| [Cookbooks](https://docs.typesafe.ai/cookbooks.md) | 19 end-to-end recipes with numbers |
| [Jev 1.13 known issues](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) | Where Jev fails, and how to work around it |
| [Machine learning primer](https://docs.typesafe.ai/introduction/machine-learning-primer.md) | Why calibrated probabilities matter |
| [llms.txt](https://docs.typesafe.ai/llms.txt) | The full docs index. Give it to your coding agent |

---

## Deep dives and opinions

| Read | By | Why |
|---|---|---|
| [Jev introduces a new shape of LLM: System One, aka Decision Models](https://simonwillison.net/2026/Sep/21/jev/) | Simon Willison | Hands-on notes. Honest about black-box and bias risks |
| [Jev: System One models for Prod, not God](https://www.latent.space/p/jev) | Latent Space podcast | The founder, Diogo Almeida, on why and how |
| [AINews: Jev, a "System One Model" that only decides](https://www.latent.space/p/ainews-jev-a-system-one-model-that) | Latent Space | Launch-week roundup and reactions |
| [Jev by TypeSafe: a new agent layer, if calibration holds](https://agentconn.com/blog/jev-typesafe-new-agent-layer-if-calibration-holds/) | AgentConn | What Jev means for agent builders |

---

## Independent tests and reviews

| Read | Why |
|---|---|
| [Jev after eight days of independent tests](https://dev.to/aws-builders/jev-after-eight-days-of-independent-tests-level-with-mid-price-llms-behind-the-frontier-1c60) | Speed, cost and accuracy vs 19 LLMs. The most careful numbers so far |
| [TypeSafe Jev review (2026)](https://www.eesel.ai/blog/typesafe-jev-review) | A tested review from eesel AI |
| [JevBench leaderboard](https://benchmarkheaven.com/jev-models) | Decision models ranked on intelligence, calibration, speed and cost |

---

## Tutorials

| Read | Why |
|---|---|
| [A coding guide to TypeSafe AI Jev](https://www.marktechpost.com/2026/09/23/a-coding-guide-to-typesafe-ai-jev/) | Typed decisions, confidence and fan-out, in code |
| [How to use Jev: a practical guide](https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e) | SDK setup, question types, limits |
| [Your first hour with TypeSafe Jev](https://stackademic.com/blog/first-hour-with-typesafe-jev-api-key-to-typed-answers) | From API key to typed answers |
| [What is Jev?](https://www.digitalocean.com/resources/articles/what-is-jev) | DigitalOcean's beginner explainer |
| [What "System One Models" actually are](https://www.truefoundry.com/blog/typesafe-ai-jev) | TrueFoundry on the new model class |
| [Jev explained](https://www.mindstudio.ai/blog/jev-system-one-model-launch) | MindStudio on the non-autoregressive idea |
| [TypeSafe AI releases Jev](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/) | MarkTechPost's launch coverage |

---

## Integrations

| Read | Why |
|---|---|
| [Jev is now available in LangSmith Evals](https://www.langchain.com/blog/jev-is-now-available-in-langsmith-evals) | Jev as an eval judge, plus tracing |
| [LangChain TypeSafe integration](https://docs.langchain.com/oss/python/integrations/providers/typesafe) | Classifier, model router, risky-tool-call guard |
| [Observability for Jev with Langfuse](https://langfuse.com/integrations/model-providers/typesafe) | Trace every Jev call |
| [Vercel AI SDK: TypeSafe provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) | Jev from TypeScript apps |
| [TypeSafe agent skill](https://docs.typesafe.ai/agent-skill.md) | Set up Claude Code, Codex, Cursor, Gemini CLI |

---

## Open alternatives and the research behind them

| Read | Why |
|---|---|
| [I built non-autoregressive decision models a year ago. Then a frontier lab called it a "breakthrough"](https://dev.to/nandakishor_m_6cc0adfde9f/i-built-non-autoregressive-decision-models-a-year-ago-then-a-frontier-lab-called-it-a-18me) | Laya's creator tells the backstory |
| [Laya: a 421M local decision model that outruns the cloud](https://themenonlab.blog/blog/laya-local-system-1-decision-model/) | How Laya works, explained |
| [SalesRLAgent (arXiv, Mar 2025)](https://arxiv.org/abs/2503.23303) | Early RL-trained decision model by Laya's creator |
| [Confidence-Aware Routing (arXiv, Sep 2025)](https://arxiv.org/abs/2510.01237) | Routing by confidence to cut hallucinations |
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | Papers, reproductions and evaluations in one list |

---

## Background

| Read | Why |
|---|---|
| *Thinking, Fast and Slow* by Daniel Kahneman | Where "System 1" and "System 2" come from |
| [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155) | The RLHF paper Jev's founder worked on |

[← Back to README](../README.md)
