"""Let confidence decide what your app does.

python confidence_router.py
"""

from typesafe_sdk import Choice, TypeSafeClient

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

TICKETS = [
    "I was charged twice for my May invoice.",
    "The app crashes every time I open settings.",
    "My order came late and the invoice amount looks wrong too.",
    "hello??",
    "Do you ship to Nepal?",
]

AUTO = 0.9   # above this: act on it
ASK = 0.6    # between ASK and AUTO: double-check. Below ASK: a human decides

for ticket in TICKETS:
    answer = client.system_one(state=ticket, questions={"team": TEAM}).answers["team"]
    if answer.confidence >= AUTO:
        action = f"auto-route to {answer.choice}"
    elif answer.confidence >= ASK:
        action = f"probably {answer.choice}, double-check with a bigger model"
    else:
        action = "send to a human"
    print(f"{answer.confidence:.2f}  {action:<48} ← {ticket}")
