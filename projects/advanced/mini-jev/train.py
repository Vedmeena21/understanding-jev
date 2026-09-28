"""Step 2: train the answer head, then check accuracy AND calibration.

python train.py        → mini_jev_head.pt
"""

import json
import random
from pathlib import Path

import torch

from mini_jev import MiniJev

HERE = Path(__file__).parent
torch.manual_seed(0)
random.seed(0)


def load(name):
    with open(HERE / "data" / f"{name}.jsonl", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


model = MiniJev()
train, test, fresh = load("train"), load("test"), load("fresh_test")

print(f"Reading {len(train) + len(test) + len(fresh)} examples with the frozen model (the prefill step)…")
def encode(rows):
    return [(model.features(r["state"], r["question"], r["options"]), list(r["options"]).index(r["answer"])) for r in rows]
train_x, test_x, fresh_x = encode(train), encode(test), encode(fresh)

# Cross-entropy (log loss) is a "proper scoring rule": the model scores best by
# reporting honest probabilities. That's the idea behind calibrated confidence.
opt = torch.optim.AdamW(model.answer_head.parameters(), lr=1e-3, weight_decay=0.01)
for epoch in range(1, 11):
    random.shuffle(train_x)
    total = 0.0
    for feats, label in train_x:
        loss = torch.nn.functional.cross_entropy(model.scores(feats).unsqueeze(0), torch.tensor([label]))
        opt.zero_grad()
        loss.backward()
        opt.step()
        total += loss.item()
    if epoch % 5 == 0:
        print(f"epoch {epoch:>2}  loss {total / len(train_x):.3f}")

# ── Test: accuracy, Brier score and a calibration table ───────────────
def evaluate(name, examples):
    right, brier, bins = 0, 0.0, {}
    with torch.no_grad():
        for feats, label in examples:
            probs = torch.softmax(model.scores(feats), dim=-1)
            pick, conf = int(probs.argmax()), float(probs.max())
            right += pick == label
            target = torch.zeros_like(probs)
            target[label] = 1
            brier += float(((probs - target) ** 2).sum())
            b = min(int(conf * 10), 9)
            n, k = bins.get(b, (0, 0))
            bins[b] = (n + 1, k + (pick == label))
    print(f"\n{name}: accuracy {right / len(examples):.0%} · Brier score {brier / len(examples):.3f} (lower is better)")
    print("  confidence   examples   actually right")
    for b in sorted(bins):
        n, k = bins[b]
        print(f"    {b / 10:.1f}–{(b + 1) / 10:.1f}      {n:>4}        {k / n:.0%}")


evaluate("Test (same templates as training)", test_x)
evaluate("Fresh test (new sentences, written by hand)", fresh_x)

torch.save(model.answer_head.state_dict(), HERE / "mini_jev_head.pt")
print("\nSaved mini_jev_head.pt")
