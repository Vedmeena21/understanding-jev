"""Spam checker: is this message spam, a scam or phishing?

python main.py "You won a free iPhone! Click here"
python main.py                       # type messages one by one (empty line to quit)
"""

import sys

from typesafe_sdk import Choice, Noul, TypeSafeClient

client = TypeSafeClient()

QUESTIONS = {
    "kind": Choice(
        instructions="What kind of message is this",
        criteria={
            "normal": "A normal personal or work message",
            "promo": "A real company's ad or newsletter",
            "spam": "Unwanted bulk messages, get-rich-quick offers, fake prizes",
            "phishing": "Tries to steal passwords, card details or OTPs, often with a fake link",
            "scam": "Tries to get you to send money: fake parcels, lottery, crypto doubling, job fees",
        },
    ),
    "asks_for_secrets": Noul(instructions="The message asks for a password, OTP, PIN or card details"),
    "has_pressure": Noul(instructions="The message pushes you to act fast (urgent, limited time, account blocked)"),
    "asks_for_money": Noul(instructions="The message asks you to pay or transfer money"),
}

ICONS = {"normal": "✅", "promo": "📣", "spam": "🗑️", "phishing": "🎣", "scam": "🚨"}


def check(message):
    a = client.system_one(state=message, questions=QUESTIONS).answers
    kind = a["kind"]
    print(f"\n{ICONS[kind.choice]}  {kind.choice.upper()}  (confidence {kind.confidence:.2f})")
    for name, label in [("asks_for_secrets", "asks for secrets"), ("has_pressure", "rushes you"), ("asks_for_money", "asks for money")]:
        p = a[name].noul
        print(f"   {'⚠️ ' if p > 0.5 else '  '} {label:<17} {p:.2f}")
    if kind.choice in ("phishing", "scam"):
        print("   → Don't click links. Don't reply. Report and delete.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        check(" ".join(sys.argv[1:]))
    else:
        while (message := input("\nPaste a message (empty to quit): ").strip()):
            check(message)
