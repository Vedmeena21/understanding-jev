"""Jev quickstart: one call, three questions.

pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"
python quickstart.py
"""

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()  # reads TYPESAFE_API_KEY, uses jev-latest

email = "My package arrived damaged and I want a refund."

response = client.system_one(
    state=email,
    questions={
        "team": Choice(
            instructions="Which team should handle this",
            criteria={
                "billing": "Payments, invoices, charges",
                "shipping": "Delivery, damaged or lost packages",
                "technical": "Bugs or app problems",
                "general": "Anything else",
            },
        ),
        "wants_refund": Noul(instructions="The customer asks for a refund"),
        "anger": Score(
            instructions="How upset the customer is",
            criteria=["Calm", "Annoyed", "Very angry"],
        ),
    },
)

team = response.answers["team"]
print("team:         ", team.choice)
print("probabilities:", team.probabilities)
print("confidence:   ", team.confidence)
print("wants refund: ", response.answers["wants_refund"].noul)
print("anger level:  ", response.answers["anger"].score)  # 0 = Calm, 1 = Annoyed, 2 = Very angry

# Let confidence decide what happens next
if team.confidence >= 0.8:
    print(f"→ Auto-route to {team.choice}")
else:
    print("→ Send to a human to check")
