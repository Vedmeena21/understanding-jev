"""Ask 8 questions in 1 call vs 8 separate calls. Compare time and tokens.

python many_questions.py
"""

import time

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()

email = (
    "Hi, this is the THIRD time I'm writing. My order #4471 arrived with a cracked screen, "
    "and I was still charged the express shipping fee even though it came a week late. "
    "I want a full refund today or I'm going to my bank. - Priya"
)

QUESTIONS = {
    "team": Choice(
        instructions="Which team should handle this",
        criteria={"billing": "Money and refunds", "shipping": "Delivery and damage", "technical": "Bugs", "general": "Anything else"},
    ),
    "wants_refund": Noul(instructions="The customer asks for a refund"),
    "is_urgent": Noul(instructions="The customer needs an answer today"),
    "repeat_contact": Noul(instructions="The customer says they have contacted support before"),
    "legal_risk": Noul(instructions="The customer threatens a chargeback, bank dispute or legal action"),
    "damaged_item": Noul(instructions="The customer says an item arrived damaged"),
    "anger": Score(instructions="How angry the customer is", criteria=["Calm", "Annoyed", "Angry", "Furious"]),
    "reply_priority": Score(instructions="How soon support should reply", criteria=["This week", "Tomorrow", "Today", "Within an hour"]),
}

# 1 call, 8 questions
start = time.perf_counter()
one = client.system_one(state=email, questions=QUESTIONS)
one_time = time.perf_counter() - start

# 8 calls, 1 question each
start = time.perf_counter()
many_tokens = 0
for name, question in QUESTIONS.items():
    r = client.system_one(state=email, questions={name: question})
    many_tokens += r.usage.input_tokens or 0
many_time = time.perf_counter() - start

print("Answers from the single call:")
for name, answer in one.answers.items():
    if answer.type == "choice":
        value = answer.choice
    elif answer.type == "noul":
        value = f"{answer.noul:.2f}"
    else:
        value = f"{answer.score:.2f}"
    print(f"  {name:<15} {value}")

print(f"\n1 call,  8 questions: {one_time:.2f} s, {one.usage.input_tokens} input tokens")
print(f"8 calls, 1 question:  {many_time:.2f} s, {many_tokens} input tokens")
