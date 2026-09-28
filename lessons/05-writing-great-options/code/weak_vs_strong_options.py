"""Same tickets. Weak options vs strong options. See the difference.

python weak_vs_strong_options.py
"""

from typesafe_sdk import Choice, TypeSafeClient

client = TypeSafeClient()

# (message, right answer)
TICKETS = [
    ("I was charged twice for my May invoice.", "billing"),
    ("My refund still hasn't reached my bank.", "billing"),
    ("The courier marked it delivered but I got nothing.", "shipping"),
    ("Wrong size delivered, I ordered M not XL.", "shipping"),
    ("Your checkout page shows an error when I pay with UPI.", "technical"),
    ("Notifications stopped working on Android.", "technical"),
    ("Can you add dark mode?", "general"),
    ("Is there a way to talk to a human?", "general"),
]

WEAK = Choice(
    instructions="Team",
    criteria={"billing": None, "shipping": None, "technical": None, "general": None},
)

STRONG = Choice(
    instructions="Which team should handle this support message",
    criteria={
        "billing": {
            "what": "Money: charges, invoices, refunds, subscriptions, card details",
            "not_for": "Payment pages that crash or show errors (that's technical)",
            "examples": ["Charged twice", "Refund not received"],
        },
        "shipping": {
            "what": "Physical orders: delivery, tracking, damaged, missing or wrong items",
            "not_for": "Refunds for a delivered order (that's billing)",
            "examples": ["Package never arrived", "Wrong size sent"],
        },
        "technical": {
            "what": "Software problems: bugs, errors, crashes, login, app or API issues",
            "not_for": "Feature requests (that's general)",
            "examples": ["App crashes", "Error at checkout"],
        },
        "general": {
            "what": "Everything else: questions, feedback, feature requests, contact",
            "not_for": "Anything about money, orders or bugs",
            "examples": ["Support hours?", "Please add dark mode"],
        },
    },
)


def score(question, name):
    right, confidence = 0, 0.0
    for message, label in TICKETS:
        answer = client.system_one(state=message, questions={"team": question}).answers["team"]
        right += answer.choice == label
        confidence += answer.confidence
    n = len(TICKETS)
    print(f"{name:<8} accuracy {right / n:>4.0%}   average confidence {confidence / n:.2f}")


score(WEAK, "Weak")
score(STRONG, "Strong")
