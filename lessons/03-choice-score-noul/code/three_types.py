"""One message. Three question types. One call.

python three_types.py
"""

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()

message = "Help! My payouts have been failing for 3 days and nobody is replying."

response = client.system_one(
    state=message,
    questions={
        # Choice: pick one option
        "department": Choice(
            instructions="Which team should handle this",
            criteria={
                "billing": "Payments, invoicing, refunds, payouts",
                "technical": "Bugs, outages, integrations",
                "sales": "Pricing, upgrades, new accounts",
            },
        ),
        # Score: a level on an ordered scale (0 = Calm, 1 = Frustrated, 2 = Very angry)
        "frustration": Score(
            instructions="How frustrated the customer is",
            criteria=["Calm", "Frustrated", "Very angry"],
        ),
        # Noul: yes or no, as a probability
        "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity"),
    },
)

a = response.answers
print("Choice →", a["department"].choice, f"(confidence {a['department'].confidence:.2f})")
print("Score  →", f"{a['frustration'].score:.2f}", "on 0 = Calm … 2 = Very angry")
print("Noul   →", f"{a['is_urgent'].noul:.2f}", "chance it's urgent")
