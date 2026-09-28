# Understanding Jev

**Everything about Jev in one place.**
What it is. How it works. How to set it up. What to build with it.
Plus the best repos, articles and tools, checked and sorted.

> Jev is an AI model that **doesn't write text**.
> You give it some text, a question and a few options.
> It picks an option, gives a probability for each one, and says how sure it is.
> In about **0.1 to 0.5 seconds**.

---

## Jev in 30 seconds

| | |
|---|---|
| **What** | A "System One" decision model. Not a chatbot. Not an LLM that writes. |
| **By** | [TypeSafe AI](https://typesafe.ai), founded by ex-OpenAI researcher Diogo Almeida |
| **Launched** | 15 September 2026 (early access) |
| **Input** | Text or JSON ("state") + typed questions |
| **Output** | A choice, a score or a yes/no probability, plus confidence |
| **Speed** | 70 to 500 ms per request (TypeSafe's number) |
| **Price** | $0.042 per 1M input tokens. **Output is free.** |
| **Limits** | Text only. 64K tokens per request. Up to 255 options per question. |
| **Model name** | `jev-latest` (currently `jev-1.13.0`) |

---

## Start here

| I want to... | Go to |
|---|---|
| Understand what Jev is, in plain words | [01 · What is Jev](docs/01-what-is-jev.md) |
| See how it works inside | [02 · How Jev works](docs/02-how-jev-works.md) |
| Make my first Jev call | [03 · Setup](docs/03-setup.md) |
| Use Jev inside Claude Code, Codex, Cursor or Gemini CLI | [03 · Setup for coding agents](docs/03-setup.md#6-set-up-jev-in-your-coding-agent) |
| Learn the right way to build with it | [04 · Build with Jev](docs/04-build-with-jev.md) |
| Know where Jev fits in real companies | [05 · Use cases](docs/05-use-cases.md) |
| Build a project for my portfolio | [06 · Projects to build](docs/06-projects.md) |
| Know what's hype and what's real | [07 · Reality check](docs/07-reality-check.md) |
| Find the best open-source Jev repos | [Resources · Repos](resources/repos.md) |
| Read the best articles and talks | [Resources · Reading list](resources/reading-list.md) |
| Run a Jev-like model on my own machine | [Resources · Open alternatives](resources/repos.md#open-alternatives-run-it-yourself) |

---

## The learning path

| # | Chapter | What you'll learn |
|---|---|---|
| 01 | [What is Jev](docs/01-what-is-jev.md) | LLM vs Jev. System 1 vs System 2. Who built it and why. |
| 02 | [How Jev works](docs/02-how-jev-works.md) | State, questions, the 3 question types, confidence. What's likely inside. |
| 03 | [Setup](docs/03-setup.md) | API key. Python, JavaScript, curl. Claude Code, Codex, Cursor, MCP, LangChain. |
| 04 | [Build with Jev](docs/04-build-with-jev.md) | Golden rules. 4 patterns. Known weak spots and fixes. |
| 05 | [Use cases](docs/05-use-cases.md) | 19 industries. 10 decision types. Real demos people built. |
| 06 | [Projects to build](docs/06-projects.md) | 15 projects, beginner to advanced, each with a reference repo. |
| 07 | [Reality check](docs/07-reality-check.md) | Official claims vs independent tests. Downsides. What's next. |

Code you can run: [`examples/`](examples)

---

## One call, three answers

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()  # reads TYPESAFE_API_KEY

response = client.system_one(
    state="My package arrived damaged and I want a refund.",
    questions={
        "team": Choice(
            instructions="Which team should handle this",
            criteria={
                "billing": "Payments, invoices, charges",
                "shipping": "Delivery, damaged or lost packages",
                "technical": "Bugs or app problems",
            },
        ),
        "wants_refund": Noul(instructions="The customer asks for a refund"),
        "anger": Score(
            instructions="How upset the customer is",
            criteria=["Calm", "Annoyed", "Very angry"],
        ),
    },
)

print(response.answers["team"].choice)       # "shipping"
print(response.answers["team"].confidence)   # e.g. 0.9
print(response.answers["wants_refund"].noul) # e.g. 0.97
```

- One request.
- Three questions answered **in parallel**.
- No text to parse. The answer is always one of your options.

---

## Best repos (preview)

Only repos with **300+ stars**, or official ones. Stars as of 29 Sep 2026.

| Repo | What it is | ⭐ |
|---|---|---|
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | **Official.** Teaches Claude Code, Codex and Cursor to build with Jev | 2.3k |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | Fastest and cheapest web agent, built by Browser Use | 21.1k |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | Claude Code plugin: Jev decides which old messages to drop | 7.1k |
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | Open-source decision model. Runs locally. 100+ languages | 27.6k |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | Jev-like models on Qwen that you can train and run yourself | 7.6k |
| [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | A tiny Jev replica with the full training pipeline. Best to learn from | 2.3k |
| [dzhng/jevgrep](https://github.com/dzhng/jevgrep) | Find code by asking what it does | 1.3k |
| [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) | Classifies 261 IRS tax forms at ~$0.001 per page | 473 |

**Full list, 40+ repos by category** → [resources/repos.md](resources/repos.md)

---

## Best reads (preview)

| Read | Why |
|---|---|
| [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | The official launch post |
| [Simon Willison: Jev introduces a new shape of LLM](https://simonwillison.net/2026/Sep/21/jev/) | An honest hands-on take, with criticisms |
| [Latent Space: System One models for Prod, not God](https://www.latent.space/p/jev) | The founder explains the thinking |
| [Jev after eight days of independent tests](https://dev.to/aws-builders/jev-after-eight-days-of-independent-tests-level-with-mid-price-llms-behind-the-frontier-1c60) | Real numbers vs 19 LLMs |
| [TypeSafe docs](https://docs.typesafe.ai/introduction) | API, patterns and 19 cookbooks |

**Full reading list** → [resources/reading-list.md](resources/reading-list.md)

---

## Reality check

- TypeSafe says: **40x to 200x faster** than LLMs on System One tasks.
- The most careful independent test found about **2.9x faster** and **12x cheaper** than Claude Haiku 4.5.
- Still fast and cheap. Just not magic.
- It's great at yes/no and few-option decisions.
- It's weaker at counting, dates, numbers and non-English text.

More → [07 · Reality check](docs/07-reality-check.md)

---

## Repo map

```
understanding-jev/
├── README.md              ← you are here
├── docs/
│   ├── 01-what-is-jev.md
│   ├── 02-how-jev-works.md
│   ├── 03-setup.md
│   ├── 04-build-with-jev.md
│   ├── 05-use-cases.md
│   ├── 06-projects.md
│   └── 07-reality-check.md
├── examples/
│   ├── quickstart.py
│   ├── quickstart.ts
│   ├── quickstart.sh
│   └── review_ratings.py
└── resources/
    ├── repos.md
    └── reading-list.md
```

---

Made by [Ved Prakash Meena](https://www.linkedin.com/in/ved-prakash-meena/). Follow for more AI resources.

Found a great Jev repo or article? Open an issue or a PR.
