# Mini-Jev

🔴 Advanced · No Jev API key needed · Runs on a laptop in about 30 seconds

Build your own tiny decision model, the way Jev (likely) works inside:

1. Take a small open LLM.
2. **Remove the part that writes words** (the LM head).
3. Add a small **answer head** that scores only your options.
4. Train it on **synthetic data**.
5. Check it's **calibrated**, not just accurate.

⚠️ This is a teaching toy. It shows the idea. It is not Jev.

---

## How it works

```
state + question + options (as text)
            ↓
SmolLM2-135M, frozen        ← reads and understands (the "prefill")
            ↓
one vector per option       ← taken at the last token of each option
            ↓
answer head (tiny, trained) ← one score per option
            ↓
softmax → probabilities → pick + confidence
```

- `AutoModel` loads the LLM **without** its writing head. It literally can't write.
- Only the answer head is trained. The LLM stays frozen.
- The loss is **cross-entropy**, a "proper scoring rule": the model scores best by being **honest** about its confidence.

---

## Run it

```bash
pip install -r requirements.txt          # torch + transformers

python make_data.py                      # 1. make synthetic data
python train.py                          # 2. train the answer head (~30 s)
python predict.py "My parcel says delivered but it is not here" \
  "Which team should handle this message?" \
  "billing=payments, charges, refunds" "shipping=delivery, damaged or missing items" \
  "technical=bugs, errors, crashes" "general=anything else"
```

What you'll see (one real run):

```
Fresh test (new sentences, written by hand): accuracy 92% · Brier score 0.165
  confidence   examples   actually right
    0.8–0.9         5        100%
    0.9–1.0         4        100%

→ shipping  (confidence 1.00)
```

---

## Files

| File | What it does |
|---|---|
| `make_data.py` | Makes 660 synthetic examples for 3 tasks: team routing, mood, urgency |
| `mini_jev.py` | The model: frozen LLM + answer head |
| `train.py` | Trains the head. Prints accuracy, Brier score and a calibration table |
| `predict.py` | Ask your model anything. Options are `name=description` |
| `data/fresh_test.jsonl` | 12 hand-written examples it never saw. The honest test |

---

## What we learned building it

- **Round 1:** 100% on the test set, but every answer was 100% sure, and new sentences went wrong. The options were always in the same order, so it learned the **position**, not the meaning.
- **Fix:** shuffle option order in every example.
- **Round 2:** 92% on brand-new sentences, and confidence that actually means something.
- **Lesson:** test on data that **doesn't** look like your training data. And check calibration, not just accuracy.

---

## Make it better

- More tasks and more varied synthetic data (use an LLM to write it).
- Unfreeze the last layer of the LLM.
- A bigger base model (Qwen, Llama) on a GPU.
- Test it on [JevBench](https://github.com/fstandhartinger/jevbench).

## Go deeper

- [NanoJev](https://github.com/TianyuCodings/NanoJev): a fuller replica with a complete training pipeline
- [kev](https://github.com/jaredpalmer/kev): Jev-like models on Qwen you can train and run
- [Laya](https://github.com/NandhaKishorM/laya): an open decision model trained with proper scoring rules
- [Lesson 12 · How Jev works inside](../../../lessons/12-how-jev-works-inside)
