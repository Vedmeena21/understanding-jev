# Projects

10 things you can build with Jev. Each one runs.
Pick one, run it, then make it yours.

| Level | What it means |
|---|---|
| 🟢 [Beginner](beginner) | One call per item. A few questions. Under 100 lines |
| 🟡 [Intermediate](intermediate) | Jev inside a real tool. Config files, routing, reports |
| 🔴 [Advanced](advanced) | Real-time decisions, agent internals, and training your own model |

---

## All projects

| # | Project | Level | What it does |
|---|---|---|---|
| 1 | [Ticket router](beginner/ticket-router) | 🟢 | Sends support emails to the right team, with urgency and mood |
| 2 | [Review ratings](beginner/review-ratings) | 🟢 | Turns raw reviews into "Camera 4.1 · Battery 3.2" ratings |
| 3 | [Spam checker](beginner/spam-checker) | 🟢 | Tells you if a message is spam, a scam or phishing |
| 4 | [Comment moderator](beginner/comment-moderator) | 🟢 | Sorts YouTube comments: keep, hide or reply |
| 5 | [Model router](intermediate/model-router) | 🟡 | Sends each prompt to the cheapest model that can handle it |
| 6 | [Document classifier](intermediate/doc-classifier) | 🟡 | Labels documents (invoice, salary slip, resume…) with no training |
| 7 | [Log triage](intermediate/log-triage) | 🟡 | Reads error logs and builds an on-call summary |
| 8 | [Context compactor](advanced/context-compactor) | 🔴 | Shrinks a long agent session without losing what matters |
| 9 | [Snake bot](advanced/snake-bot) | 🔴 | Jev plays Snake in your terminal, one move at a time |
| 10 | [Mini-Jev](advanced/mini-jev) | 🔴 | Train your own tiny decision model with an answer head |

---

## Every project has

- `README.md`: what it does, the Jev questions it asks, how to run it
- `main.py`: the code. Short and commented
- `data/`: sample data so it works right away

## Before you start

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"
```

New to Jev? Do [lessons 00–06](../lessons) first. It takes about 2 hours.

## Show it off

For any project you share, show 3 numbers:

1. **Accuracy** on labeled examples
2. **Speed** per decision
3. **Cost** per 1,000 decisions, compared to an LLM

That's what makes a portfolio project stand out.
