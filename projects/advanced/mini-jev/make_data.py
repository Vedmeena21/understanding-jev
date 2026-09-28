"""Step 1: make synthetic training data (Jev is trained on synthetic data too).

python make_data.py            → data/train.jsonl and data/test.jsonl
"""

import json
import random
from pathlib import Path

random.seed(0)
OUT = Path(__file__).parent / "data"

# ── Task 1: which team handles this support message? ──────────────────
TEAM_Q = "Which team should handle this message?"
TEAM_OPTIONS = {
    "billing": "payments, charges, refunds, invoices",
    "shipping": "delivery, tracking, damaged or missing items",
    "technical": "bugs, errors, crashes, login problems",
    "general": "questions, feedback, anything else",
}
TEAM_TEMPLATES = {
    "billing": ["I was charged {n} times for my {thing} order.", "Where is my refund for {thing}?",
                "My card was billed after I cancelled.", "Please send the invoice for my {thing} purchase.",
                "Why is there an extra fee on my {thing} bill?"],
    "shipping": ["My {thing} arrived broken.", "The {thing} I ordered never arrived.",
                 "Tracking for my {thing} hasn't moved in {n} days.", "You sent the wrong {thing}.",
                 "Can I change the delivery address for my {thing}?"],
    "technical": ["The app crashes when I open {place}.", "I can't log in, it says error {n}.",
                  "The {place} page shows a blank screen.", "Buttons on {place} don't respond.",
                  "I get a timeout error on {place} every time."],
    "general": ["Do you have a discount for {who}?", "What are your support hours?",
                "Can you add {feature}?", "Love the app, great work!", "Do you have an office in {city}?"],
}

# ── Task 2: how does this review feel? ────────────────────────────────
MOOD_Q = "How does the writer feel?"
MOOD_OPTIONS = {"positive": "happy, satisfied", "neutral": "neither happy nor unhappy", "negative": "unhappy, disappointed"}
MOOD_TEMPLATES = {
    "positive": ["The {thing} is amazing, totally worth it.", "Really happy with the {thing}.", "Best {thing} I've bought this year."],
    "neutral": ["The {thing} is okay, nothing special.", "It's an average {thing}.", "The {thing} does the job."],
    "negative": ["The {thing} broke in a week, very disappointed.", "Worst {thing} ever, don't buy.", "I regret buying this {thing}."],
}

# ── Task 3: yes / no ──────────────────────────────────────────────────
URGENT_Q = "Does the writer need help urgently?"
URGENT_OPTIONS = {"yes": "needs help today, right now, ASAP", "no": "can wait, no rush"}
URGENT_TEMPLATES = {
    "yes": ["URGENT: my {thing} stopped working and I need it today!", "Please help ASAP, my {thing} is down.",
            "I need this fixed right now, my {place} is blocked."],
    "no": ["Whenever you get a chance, can you check my {thing}?", "No rush, but my {thing} has a small issue.",
           "Just a small question about my {thing} for later."],
}

FILL = {
    "n": ["2", "3", "4", "404", "500", "10"],
    "thing": ["phone", "laptop", "headphones", "shoes", "chair", "watch", "blender", "backpack"],
    "place": ["settings", "checkout", "profile", "dashboard", "search", "payments"],
    "who": ["students", "teachers", "startups", "seniors"],
    "feature": ["dark mode", "a Hindi version", "offline mode", "export to PDF"],
    "city": ["Pune", "Delhi", "Chennai", "Kolkata"],
}


def fill(template):
    return template.format(**{k: random.choice(v) for k, v in FILL.items()})


def make(task_q, options, templates, n):
    rows = []
    for _ in range(n):
        answer = random.choice(list(templates))
        shuffled = dict(random.sample(list(options.items()), len(options)))  # so position is never a clue
        rows.append({"state": fill(random.choice(templates[answer])), "question": task_q,
                     "options": shuffled, "answer": answer})
    return rows


rows = (make(TEAM_Q, TEAM_OPTIONS, TEAM_TEMPLATES, 360)
        + make(MOOD_Q, MOOD_OPTIONS, MOOD_TEMPLATES, 180)
        + make(URGENT_Q, URGENT_OPTIONS, URGENT_TEMPLATES, 120))
random.shuffle(rows)
split = int(len(rows) * 0.8)
OUT.mkdir(exist_ok=True)
for name, part in [("train", rows[:split]), ("test", rows[split:])]:
    with open(OUT / f"{name}.jsonl", "w", encoding="utf-8") as f:
        for r in part:
            f.write(json.dumps(r) + "\n")
    print(f"data/{name}.jsonl: {len(part)} examples")
