"""Your first Jev call.

pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"
python first_call.py
"""

from typesafe_sdk import Choice, TypeSafeClient

client = TypeSafeClient()  # reads TYPESAFE_API_KEY, uses jev-latest

response = client.system_one(
    state="My package arrived damaged and I want a refund.",
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
    },
)

answer = response.answers["team"]
print("Jev picked:  ", answer.choice)
print("Confidence:  ", round(answer.confidence, 2))
print("All options: ")
for option, p in sorted(answer.probabilities.items(), key=lambda kv: -kv[1]):
    print(f"  {option:<10} {p:.2f}")
