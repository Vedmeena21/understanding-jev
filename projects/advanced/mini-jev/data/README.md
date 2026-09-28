# Data · Mini-Jev

| File | What it is |
|---|---|
| `fresh_test.jsonl` | 12 hand-written examples the model never sees in training. The honest test |
| `train.jsonl`, `test.jsonl` | Made by `make_data.py` when you run it (not stored in the repo) |

Each line is one example: `state`, `question`, `options` (name → description) and the right `answer`.
