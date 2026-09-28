"""Comment moderator: decide what to do with every comment. Keep, hide or reply.

python main.py                       # uses data/comments.csv
python main.py my_comments.csv       # your CSV with columns: author,comment
"""

import csv
import sys
from collections import Counter
from pathlib import Path

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

HERE = Path(__file__).parent

QUESTIONS = {
    "type": Choice(
        instructions="What kind of comment is this",
        criteria={
            "question": "Asks the creator something they could answer",
            "praise": "Says something positive about the video",
            "feedback": "Polite criticism or a suggestion",
            "spam": "Ads, self-promotion, scams, links to make money",
            "abuse": "Insults, hate or harassment",
        },
    ),
    "toxicity": Score(instructions="How rude or hurtful the comment is", criteria=["Not at all", "A little rude", "Very rude", "Abusive"]),
    "needs_reply": Noul(instructions="The comment asks something the creator should answer"),
}


def decide(a):
    kind = a["type"]
    if kind.choice in ("spam", "abuse") or a["toxicity"].score >= 2:
        return "hide"
    if kind.confidence < 0.6:
        return "review"
    if a["needs_reply"].noul > 0.5:
        return "reply"
    return "keep"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else HERE / "data" / "comments.csv"
    with open(path, newline="", encoding="utf-8") as f:
        comments = list(csv.DictReader(f))

    client = TypeSafeClient()
    actions = Counter()
    to_reply = []
    print(f"{'action':<8}{'type':<10}{'author':<14}comment")
    for c in comments:
        a = client.system_one(state=c["comment"], questions=QUESTIONS).answers
        action = decide(a)
        actions[action] += 1
        if action == "reply":
            to_reply.append(c)
        print(f"{action:<8}{a['type'].choice:<10}{c['author']:<14}{c['comment'][:55]}")

    print("\nSummary:", ", ".join(f"{n} {k}" for k, n in actions.most_common()))
    if to_reply:
        print("\nQuestions to answer:")
        for c in to_reply:
            print(f"  @{c['author']}: {c['comment']}")


if __name__ == "__main__":
    main()
