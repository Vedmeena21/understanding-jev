# Set up Jev everywhere

[← Back to README](../README.md) · [All resources](README.md)

Python, JavaScript, curl, Claude Code, Codex, Cursor, Gemini CLI, MCP, LangChain, Vercel AI SDK, and options with no API key.

---

## Contents

1. [Get an API key](#1-get-an-api-key)
2. [Try it in the Playground](#2-try-it-in-the-playground)
3. [Python](#3-python)
4. [JavaScript / TypeScript](#4-javascript--typescript)
5. [curl (any language)](#5-curl-any-language)
6. [Set up Jev in your coding agent](#6-set-up-jev-in-your-coding-agent)
7. [Frameworks and tools](#7-frameworks-and-tools)
8. [No API key? Options](#8-no-api-key-options)

---

## 1. Get an API key

1. Go to [typesafe.ai](https://typesafe.ai) and sign in.
2. Open the console → **API Keys**.
3. Create a new key.
4. Save it as an environment variable:

```bash
export TYPESAFE_API_KEY="your-key"
```

- Both official SDKs read `TYPESAFE_API_KEY` automatically.
- Never paste your key into code or a chat.

---

## 2. Try it in the Playground

Before writing code:

- Open the **Playground** in the console.
- Paste some text as the **state**.
- Write a **question**.
- Add a few **options**.
- Hit run. See the probabilities.

Best way to get a feel for it in 2 minutes.

---

## 3. Python

```bash
pip install typesafe-sdk
# or
uv add typesafe-sdk
```

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()

response = client.system_one(
    state="Hi, I've been trying to connect my Stripe account for 3 days and the integration keeps failing. I'm losing sales. Please help ASAP.",
    questions={
        "department": Choice(
            instructions="Which team should handle this",
            criteria={
                "billing": "Payment or subscription issues",
                "technical": "Bugs or integration problems",
                "sales": "Pricing or account questions",
            },
        ),
        "frustration": Score(
            instructions="How frustrated the customer appears",
            criteria=["Calm, just stating facts", "Frustrated but civil", "Very angry, strong language"],
        ),
        "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity"),
    },
)

print(response.answers["department"].choice)  # "technical"
print(response.answers["frustration"].score)  # 1.0
print(response.answers["is_urgent"].noul)     # 1.0
```

- The SDK uses `jev-latest` by default.
- Full file: [`lessons/02-your-first-call/code/first_call.py`](../lessons/02-your-first-call/code/first_call.py)
- Docs: [Python SDK](https://docs.typesafe.ai/sdk/python.md)

---

## 4. JavaScript / TypeScript

```bash
npm install @typesafe-ai/sdk
```

```ts
import { choice, TypeSafeClient } from "@typesafe-ai/sdk";

const client = new TypeSafeClient();

const response = await client.systemOne({
  state: { document: "I was charged twice. Please fix this ASAP." },
  questions: {
    category: choice("What is this ticket about?", {
      billing: null,
      technical: null,
      other: null,
    }),
  },
});

console.log(response.answers.category.choice);
```

- Also has `score()` and `noul()` helpers.
- Full file: [`lessons/02-your-first-call/code/first_call.ts`](../lessons/02-your-first-call/code/first_call.ts)
- Docs: [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript.md)

---

## 5. curl (any language)

```bash
curl https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "state": "Help! My payouts have been failing for 3 days.",
    "model": "jev-latest",
    "questions": {
      "is_urgent": { "type": "noul", "instructions": "Does this convey urgency?" },
      "department": {
        "type": "choice",
        "instructions": "Which team should handle this?",
        "criteria": {
          "billing": "Payments, invoicing, refunds",
          "technical": "Bugs, outages, integrations",
          "sales": "Pricing, upgrades, new accounts"
        }
      }
    }
  }'
```

Full file: [`lessons/02-your-first-call/code/first_call.sh`](../lessons/02-your-first-call/code/first_call.sh)

---

## 6. Set up Jev in your coding agent

Two different things here:

- **A. Teach your agent to build apps with Jev.** (Most people want this.)
- **B. Let your agent use Jev as a tool**, while it works.

Jev is **not** a replacement for the model inside your coding agent.
It's something your agent can **build with** or **call for small decisions**.

### A. Teach your agent to build with Jev (official skill)

The official [typesafe-ai/skills](https://github.com/typesafe-ai/skills) gives your agent the full Jev API, patterns and cookbooks.

**Claude Code**

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

Check it works: type `/typesafe:typesafe-ai` in Claude Code.

**Codex, Cursor, Gemini CLI and other agents**

```bash
npx skills add typesafe-ai/skills --skill typesafe-ai
```

- Pick your agent when asked.
- Installs in the current project by default.
- Add `-g` to install globally.

**Try this prompt:**

> Use TypeSafe to route incoming support tickets by department, with human review for uncertain decisions.

**Keep it updated**

```bash
# Claude Code
claude plugin marketplace update typesafe-ai
claude plugin update typesafe@typesafe-ai

# Other agents
npx skills update
```

**Our 6 focused skills** (design, audit, options, thresholds, evals, migration):

```bash
claude plugin marketplace add Vedmeena21/understanding-jev
claude plugin install jev-skills@vedmeena21
# or, for Codex, Cursor, Gemini CLI and others
npx skills add Vedmeena21/understanding-jev
```

More → [skills](../skills)

**Any agent, no install:**
Point it at the docs index: `https://docs.typesafe.ai/llms.txt`

### B. Give your agent Jev as a tool (MCP)

**[jev-mcp](https://github.com/jkudish/jev-mcp)**: fast, cheap, typed judgments as MCP tools.

```bash
# Claude Code
claude mcp add jev -- npx -y @jkudish/jev-mcp

# Amp
amp mcp add jev -- npx -y @jkudish/jev-mcp

# Any MCP client: run this as the server command
npx -y @jkudish/jev-mcp
```

- Needs Node.js 22+.
- Set `TYPESAFE_API_KEY` in the server's environment.

**[system-one-connector](https://github.com/itsmostafa/system-one-connector)**: an MCP connector for Jev, Laya and other System One models.

```bash
curl -fsSL https://raw.githubusercontent.com/itsmostafa/system-one-connector/main/install.sh | sh
```

### C. Jev add-ons for coding agents

**Smarter `/compact` in Claude Code**: [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)

- Jev scores every old message.
- Drops the stale ones. Keeps the rest word for word.

```bash
claude plugin marketplace add tamaratran/fast-jev-compaction
claude plugin install fast-jev-compaction@fast-jev-compaction
```

- Needs Claude Code 2.1.274+ and function hooks turned on.
- Add to `~/.claude/settings.json`:

```json
{ "env": { "CLAUDE_CODE_ENABLE_FUNCTION_HOOKS": "1", "TYPESAFE_API_KEY": "<your key>" } }
```

**Pick the cheapest model per task in Claude Code or Codex**: [jev-router](https://github.com/gargpratyush/jev-router)

```bash
npm install -g jev-router
echo "JEV_API_KEY=..." > ~/.jev-router.env
```

**Find code by asking what it does**: [jevgrep](https://github.com/dzhng/jevgrep)

```bash
npm install -g @dzhng/jevgrep
jg auth
jg skill
jg "How are telemetry events recorded and sent?" ./my-project
```

**Hermes agents (also Claude Code and Codex)**: [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)
Routing, memory, compaction, skill selection, browser use.

```bash
git clone https://github.com/kerpopule/hermes-jev-skills ~/hermes-jev-skills
python3 ~/hermes-jev-skills/install.py
```

**Codex browser speed-up**: [jev-browser-use](https://github.com/wy-coliney/jev-browser-use)
Jev clicks, Codex thinks and verifies.

```bash
npx skills add wy-coliney/jev-browser-use -g -a codex -y
```

---

## 7. Frameworks and tools

### LangChain

```bash
pip install langchain-typesafe
```

```python
from langchain_typesafe import Choice, Noul, TypeSafeClassifier

classifier = TypeSafeClassifier()

response = classifier.invoke({
    "state": "Your input text here",
    "questions": {
        "urgent": Noul(instructions="Does this need attention right now?"),
        "team": Choice(
            instructions="Which team should pick this up?",
            criteria={
                "infra": "Deploys, availability, and on-call incidents.",
                "billing": "Payments, invoices, and subscriptions.",
            },
        ),
    },
})
```

- Agent middleware too: `pip install "langchain-typesafe[experimental]"`
  - **ModelRouterMiddleware**: routes requests across models.
  - **AutoModeMiddleware**: blocks tool calls that are too risky.
- Docs: [LangChain TypeSafe integration](https://docs.langchain.com/oss/python/integrations/providers/typesafe)

### LangSmith and Langfuse (tracing and evals)

- **LangSmith** traces every Jev decision. Jev also works as a judge in LangSmith Evals. → [LangChain blog](https://www.langchain.com/blog/jev-is-now-available-in-langsmith-evals)
- **Langfuse** has a Jev observability integration. → [Langfuse docs](https://langfuse.com/integrations/model-providers/typesafe)

### Vercel AI SDK

```bash
pnpm add @ai-sdk/typesafe-ai
```

```ts
import { experimental_evaluate } from "ai";
import { typeSafeAi } from "@ai-sdk/typesafe-ai";

const result = await experimental_evaluate({
  model: typeSafeAi.evaluationModel("jev-latest"),
  state: { message: "Sample text" },
  questions: {
    category: {
      type: "choice",
      instructions: "Categorize this",
      criteria: { option1: null, option2: null },
    },
  },
});
```

Docs: [AI SDK TypeSafe provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)

### LLM CLI (by Simon Willison)

```bash
llm install llm-typesafe
llm keys set typesafe

llm -m jev 'Please refund my last payment.' \
  -s 'Does this message explicitly request a refund?'
```

Repo: [simonw/llm-typesafe](https://github.com/simonw/llm-typesafe)

---

## 8. No API key? Options

**Run your Jev code on an LLM you already pay for**
[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) (official): a drop-in `TypeSafeClient` backed by LLM APIs.

```bash
pip install 'system-one-adapter[openai]'     # OpenAI-compatible providers
pip install 'system-one-adapter[anthropic]'  # Anthropic
pip install 'system-one-adapter[gemini]'     # Gemini
```

**Run a Jev-like model on your own machine**

```bash
# Laya: open-source decision model
python -m pip install laya

# Ollaya: "Ollama for decision models", with a TypeSafe-compatible API
curl -fsSL https://ollaya.dev/install.sh | sh
```

More local options → [Open alternatives](repos.md#open-alternatives-run-it-yourself)

Next: [Best practices →](best-practices.md)
