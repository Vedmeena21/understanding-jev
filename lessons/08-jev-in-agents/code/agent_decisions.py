"""The small decisions inside an AI agent, made by Jev.

python agent_decisions.py
"""

from typesafe_sdk import Choice, Score, TypeSafeClient

client = TypeSafeClient()

task = "Find last month's failed payments in the database and email each customer."

# ── Decision 1: which tool first? ─────────────────────────────────────
TOOLS = {
    "sql_query": "Run a read-only SQL query on the payments database",
    "send_email": "Send an email to one customer",
    "web_search": "Search the public web",
    "read_file": "Read a file from the project folder",
}
tool = client.system_one(
    state={"task": task, "done_so_far": []},
    questions={"next_tool": Choice(instructions="Which tool should the agent use next for `task`", criteria=TOOLS)},
).answers["next_tool"]
print(f"1. Next tool → {tool.choice} (confidence {tool.confidence:.2f})")

# ── Decision 2: is this step safe to run? ─────────────────────────────
step = {"tool": "sql_query", "input": "DELETE FROM payments WHERE status = 'failed'"}
risk = client.system_one(
    state={"task": task, "planned_step": step},
    questions={
        "risk": Score(
            instructions="How risky is `planned_step` for the user's data",
            criteria=["Safe, read-only", "Changes data but can be undone", "Deletes or destroys data"],
        )
    },
).answers["risk"]
verdict = "BLOCK and ask the user" if risk.score >= 1.5 else "OK to run"
print(f"2. Step risk → {risk.score:.2f} → {verdict}")

# ── Decision 3: which model should do the hard part? ──────────────────
MODELS = {
    "small": "Short, simple, well-defined tasks",
    "medium": "Normal coding or writing tasks",
    "frontier": "Hard reasoning, long plans, tricky bugs",
}
model = client.system_one(
    state={"task": task},
    questions={"model": Choice(instructions="Which model size is enough for `task`", criteria=MODELS)},
).answers["model"]
print(f"3. Model → {model.choice} (confidence {model.confidence:.2f})")
