# 08 · Jev in agents

⏱ 20 min · 🎯 Intermediate · 🧪 Code: [`code/agent_decisions.py`](code/agent_decisions.py)

[← 07 · Jev in RAG](../07-jev-in-rag) · [All lessons](../README.md) · [09 · Guardrails and safety →](../09-guardrails-and-safety)

---

## What you'll learn

- Which agent steps Jev should handle
- Which steps still need an LLM
- 3 decisions every agent makes

---

## An agent is full of small decisions

Every agent loop looks something like this:

1. Understand the goal
2. Pick a tool
3. Fill in the tool's inputs
4. Check the step is safe
5. Run it
6. Decide: done, or go again?

Some steps need deep thinking. Most don't.

---

## Who does what

| Step | Who | Why |
|---|---|---|
| Understand the goal, make a plan | **LLM** | Needs reasoning |
| Pick the next tool | **Jev** | Choice between a few tools |
| Write the tool's inputs | **LLM** | Needs writing |
| Is this step safe? | **Jev** | A risk score |
| Which model for this task? | **Jev** | Choice: small, medium, frontier |
| Which old context to drop? | **Jev** | Keep or drop, per message |
| Is the task done? | **Jev** | Yes or no |
| Write the final answer | **LLM** | Needs writing |

> A big model plans.
> Cheap decision models run every step in between.

---

## 3 decisions in the code

**1. Pick a tool**

```python
Choice(instructions="Which tool should the agent use next for `task`", criteria=TOOLS)
```

Describe each tool clearly. That's your option list.

**2. Check the step is safe**

```python
Score(
    instructions="How risky is `planned_step` for the user's data",
    criteria=["Safe, read-only", "Changes data but can be undone", "Deletes or destroys data"],
)
```

High risk → stop and ask the user.

**3. Route to a model**

```python
Choice(instructions="Which model size is enough for `task`", criteria=MODELS)
```

Easy task → small, cheap model. Hard task → frontier model.

---

## Try it

```bash
python code/agent_decisions.py
```

It picks a tool, catches a dangerous `DELETE` step, and chooses a model size.

---

## See it in real tools

- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction): Jev decides which old messages Claude Code can drop
- [jev-router](https://github.com/gargpratyush/jev-router): picks the cheapest model per task in Claude Code and Codex
- [AgentiLoop/Agent](https://github.com/AgentiLoop/Agent): Jev checks shell commands before they run
- LangChain's `AutoModeMiddleware` blocks risky tool calls with Jev ([docs](https://docs.langchain.com/oss/python/integrations/providers/typesafe))

---

## Quiz

<details><summary>1. Should Jev write the arguments for a tool call?</summary>

No. That's writing, so the LLM does it. Jev picks the tool and checks the step.
</details>

<details><summary>2. Your agent is about to run `rm -rf ./data`. What should Jev do?</summary>

Score it as high risk, so your code blocks it and asks the user.
</details>

<details><summary>3. Why route easy tasks to a small model?</summary>

It's faster and much cheaper, and it's good enough for easy tasks.
</details>

---

Next: [09 · Guardrails and safety →](../09-guardrails-and-safety)
