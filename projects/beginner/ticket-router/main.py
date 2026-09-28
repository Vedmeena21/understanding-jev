"""Ticket router: send each support email to the right team.

python main.py                      # uses data/tickets.csv
python main.py my_tickets.csv       # your CSV with columns: id,message
Writes routed.csv next to this file.
"""

import csv
import sys
from pathlib import Path

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

HERE = Path(__file__).parent
AUTO_ROUTE = 0.8  # below this confidence, a human checks the team

QUESTIONS = {
    "team": Choice(
        instructions="Which team should handle this support message",
        criteria={
            "billing": "Money: charges, invoices, refunds, subscriptions, cancellations",
            "shipping": "Orders: delivery, tracking, damaged, missing or wrong items",
            "technical": "Software: bugs, errors, crashes, login or app problems",
            "general": "Anything else: questions, feedback, greetings",
        },
    ),
    "urgent": Noul(instructions="The customer needs help today or threatens to leave, cancel or dispute"),
    "wants_refund": Noul(instructions="The customer asks for a refund or their money back"),
    "mood": Score(instructions="How upset the customer is", criteria=["Calm", "Annoyed", "Angry"]),
}


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else HERE / "data" / "tickets.csv"
    with open(path, newline="", encoding="utf-8") as f:
        tickets = list(csv.DictReader(f))

    client = TypeSafeClient()
    rows = []
    for t in tickets:
        a = client.system_one(state=t["message"], questions=QUESTIONS).answers
        team = a["team"]
        rows.append({
            "id": t["id"],
            "team": team.choice if team.confidence >= AUTO_ROUTE else "needs_human",
            "confidence": round(team.confidence, 2),
            "urgent": a["urgent"].noul > 0.5,
            "wants_refund": a["wants_refund"].noul > 0.5,
            "mood": ["calm", "annoyed", "angry"][round(a["mood"].score)],
            "message": t["message"],
        })

    rows.sort(key=lambda r: (not r["urgent"], r["team"]))  # urgent first
    print(f"{'id':<5}{'team':<13}{'conf':<6}{'urgent':<8}{'refund':<8}{'mood':<9}message")
    for r in rows:
        print(f"{r['id']:<5}{r['team']:<13}{r['confidence']:<6}{'yes' if r['urgent'] else '':<8}"
              f"{'yes' if r['wants_refund'] else '':<8}{r['mood']:<9}{r['message'][:50]}")

    with open(HERE / "routed.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nSaved {len(rows)} tickets to routed.csv")


if __name__ == "__main__":
    main()
