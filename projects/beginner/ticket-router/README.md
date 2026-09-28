# Ticket router

🟢 Beginner · Uses: Choice · Noul · Score

Reads support emails. Sends each one to the right team.
Also flags what's urgent, who wants a refund, and who's angry.

---

## What it does

```
"Third time writing!!! Cancel my subscription NOW
 or I'm disputing the charge with my bank."
        ↓
team: billing · urgent: yes · refund: no · mood: angry
```

- Urgent tickets go to the top.
- Unsure? It says `needs_human` instead of guessing.
- Saves everything to `routed.csv`.

---

## The Jev questions

One call per ticket. 4 questions.

| Question | Type | Options |
|---|---|---|
| Which team? | Choice | billing / shipping / technical / general |
| Urgent? | Noul | yes / no |
| Wants a refund? | Noul | yes / no |
| How upset? | Score | calm → annoyed → angry |

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"
python main.py
```

Your own tickets:

```bash
python main.py my_tickets.csv      # columns: id,message
```

---

## Files

| File | What it is |
|---|---|
| `main.py` | The router. About 70 lines |
| `data/tickets.csv` | 8 sample tickets |
| `routed.csv` | Created when you run it |

---

## Make it yours

- Change the teams in `QUESTIONS["team"]` to match your company.
- Change `AUTO_ROUTE` (0.8) after testing on your data ([lesson 04](../../../lessons/04-confidence-and-thresholds)).
- Add a question: `"language": Choice(...)` to route by language.
- Connect it to your inbox or helpdesk.
