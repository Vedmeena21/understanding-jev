"""A tiny eval: accuracy, speed and cost of Jev on your own labeled data.

python mini_eval.py                         # uses data/eval_set.csv
python mini_eval.py my_data.csv             # your CSV with columns: message,label (spam / not_spam)
"""

import csv
import statistics
import sys
import time
from pathlib import Path

from typesafe_sdk import Noul, TypeSafeClient

PRICE_PER_M_INPUT = 0.042  # USD per 1M input tokens. Output is free.

path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "data" / "eval_set.csv"
with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

client = TypeSafeClient()
SPAM = Noul(
    instructions="This message is spam, a scam or phishing",
    criteria={"true": "Unwanted ads, scams, fake prizes, phishing links", "false": "A normal personal or work message"},
)

right, times, tokens, mistakes = 0, [], 0, []
for row in rows:
    start = time.perf_counter()
    r = client.system_one(state=row["message"], questions={"spam": SPAM})
    times.append(time.perf_counter() - start)
    tokens += r.usage.input_tokens or 0
    guess = "spam" if r.answers["spam"].noul > 0.5 else "not_spam"
    if guess == row["label"]:
        right += 1
    else:
        mistakes.append((row["message"], row["label"], r.answers["spam"].noul))

n = len(rows)
cost = tokens / 1_000_000 * PRICE_PER_M_INPUT
print(f"Examples:        {n}")
print(f"Accuracy:        {right / n:.0%}")
print(f"Median latency:  {statistics.median(times) * 1000:.0f} ms (includes your network)")
print(f"Input tokens:    {tokens}")
print(f"Cost:            ${cost:.6f}  (≈ ${cost / n * 1000:.4f} per 1,000 decisions)")
if mistakes:
    print("\nMistakes to look at:")
    for message, label, p in mistakes:
        print(f"  expected {label:<8} got p(spam)={p:.2f} ← {message[:60]}")
