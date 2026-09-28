"""Context compactor: shrink a long agent session without losing what matters.

Jev looks at every message in ONE call and decides: keep, shorten or drop.
Kept messages stay word for word. No lossy summary.

python main.py                        # compacts data/session.json
python main.py my_session.json        # your own {"goal": ..., "messages": [...]}
Writes compacted.json next to this file.
"""

import json
import sys
from pathlib import Path

from typesafe_sdk import Choice, TypeSafeClient

HERE = Path(__file__).parent
ALWAYS_KEEP_LAST = 3   # the most recent messages always stay
SHORTEN_TO = 160       # characters kept when a message is shortened


def tokens(messages):
    """Rough token count: about 4 characters per token."""
    return sum(len(m["content"]) for m in messages) // 4


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "data" / "session.json"
    session = json.loads(path.read_text(encoding="utf-8"))
    messages = session["messages"]

    # One question per message, all in the same call.
    questions = {
        f"m{i}": Choice(
            instructions=f"For reaching `goal`, what should we do with `messages[{i}]` in the agent's memory",
            criteria={
                "keep": "Still needed: the task, key findings, errors, decisions, or changes made",
                "shorten": "Partly useful: long output where only the first lines matter",
                "drop": "Not needed anymore: dead ends, unrelated files, chatter, repeated info",
            },
        )
        for i in range(len(messages) - ALWAYS_KEEP_LAST)
    }
    answers = TypeSafeClient().system_one(state=session, questions=questions).answers

    compacted, log = [], []
    for i, m in enumerate(messages):
        decision = answers[f"m{i}"].choice if f"m{i}" in answers else "keep"
        if i == 0:
            decision = "keep"  # the user's request always stays
        if decision == "keep":
            compacted.append(m)
        elif decision == "shorten":
            compacted.append({**m, "content": m["content"][:SHORTEN_TO] + " …[shortened]"})
        log.append((i, decision, m.get("name", m["role"]), m["content"].splitlines()[0][:60]))

    for i, decision, who, first_line in log:
        print(f"{i:>2} {decision:<8} {who:<11} {first_line}")

    before, after = tokens(messages), tokens(compacted)
    print(f"\n{len(messages)} → {len(compacted)} messages · ~{before} → ~{after} tokens ({1 - after / before:.0%} smaller)")
    (HERE / "compacted.json").write_text(json.dumps({**session, "messages": compacted}, indent=2), encoding="utf-8")
    print("Saved compacted.json")


if __name__ == "__main__":
    main()
