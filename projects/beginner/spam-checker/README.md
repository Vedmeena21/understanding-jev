# Spam checker

🟢 Beginner · Uses: Choice · Noul

Paste a message. Find out if it's normal, an ad, spam, phishing or a scam.
And **why**: does it ask for secrets, rush you, or ask for money?

---

## What it does

```
$ python main.py "Your parcel is on hold. Pay ₹25 customs fee here: bit.ly/xyz"

🚨  SCAM  (confidence 0.91)
   ⚠️  asks for secrets   0.12
   ⚠️  rushes you         0.78
   ⚠️  asks for money     0.95
   → Don't click links. Don't reply. Report and delete.
```

(Example. Your numbers will differ.)

---

## The Jev questions

| Question | Type |
|---|---|
| What kind of message is this? | Choice: normal / promo / spam / phishing / scam |
| Asks for a password, OTP or card? | Noul |
| Pushes you to act fast? | Noul |
| Asks you to pay? | Noul |

All 4 in one call.

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"

python main.py "You won a free iPhone! Click here"   # check one message
python main.py                                       # check many, one by one
```

---

## Make it yours

- Turn it into a WhatsApp or Telegram bot for your family.
- Measure it: run 500 labeled messages through [lesson 10's eval](../../../lessons/10-evals-and-tracing).
- Add a question: *"Does the link look like a fake version of a real brand?"*

In one independent test, Jev scored **98.33%** on 18,514 emails for spam detection.
