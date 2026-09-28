"""Find a confidence threshold from your own labeled data.

python find_threshold.py                    # uses data/labeled_tickets.csv
python find_threshold.py my_data.csv 0.98   # your CSV (message,team) and target accuracy
"""

import csv
import sys
from pathlib import Path

from typesafe_sdk import Choice, TypeSafeClient

path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "data" / "labeled_tickets.csv"
target = float(sys.argv[2]) if len(sys.argv) > 2 else 0.95

client = TypeSafeClient()
TEAM = Choice(
    instructions="Which team should handle this support message",
    criteria={
        "billing": "Payments, invoices, charges, refunds, subscriptions",
        "shipping": "Delivery, tracking, damaged, missing or wrong items",
        "technical": "Bugs, errors, crashes, app or API problems",
        "general": "Questions that are not billing, shipping or technical",
    },
)

with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

results = []  # (confidence, was_it_right)
for row in rows:
    answer = client.system_one(state=row["message"], questions={"team": TEAM}).answers["team"]
    results.append((answer.confidence, answer.choice == row["team"]))

print(f"{len(rows)} labeled examples\n")
print("threshold  coverage  accuracy")
best = None
for threshold in [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]:
    kept = [right for conf, right in results if conf >= threshold]
    if not kept:
        print(f"   {threshold:.2f}        0%        -")
        continue
    coverage = len(kept) / len(results)
    accuracy = sum(kept) / len(kept)
    print(f"   {threshold:.2f}      {coverage:>4.0%}     {accuracy:>4.0%}")
    if best is None and accuracy >= target:
        best = threshold

if best is None:
    print(f"\n→ No threshold reached {target:.0%}. Improve your options (lesson 05) or add a human step.")
else:
    print(f"\n→ Lowest threshold with ≥ {target:.0%} accuracy: {best:.2f}")
