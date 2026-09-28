# Model router

🟡 Intermediate · Uses: Choice · Score · Noul

Most prompts don't need your most expensive model.
This router sends each one to the **cheapest model that can handle it**.

---

## What it does

```
model     conf  hard  code  prompt
small     0.94  0.3         Fix the typo in this sentence…
medium    0.81  1.6   yes   Write a Python function that checks…
frontier  0.88  3.4   yes   Our checkout service drops 2% of orders…
small     0.97  0.2         Translate "good morning" to French.

Everything on frontier: $0.1200
With routing:           $0.0431  (64% saved)
```

(Example. Your numbers will differ.)

---

## The Jev questions

| Question | Type |
|---|---|
| Which model size is enough? | Choice: small / medium / frontier |
| How hard is it? | Score: trivial → very hard |
| Does it involve code? | Noul |

## The safety rule

If Jev is **less than 70% sure**, the router goes **one size up**.
Better to overpay a little than to give a bad answer.

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"

python main.py                          # routes every prompt in prompts.txt
python main.py "Explain recursion"      # routes one prompt
```

---

## Files

| File | What it is |
|---|---|
| `main.py` | The router |
| `models.json` | Your 3 model sizes: name, what they're good for, price |
| `prompts.txt` | 6 sample prompts |

---

## Make it yours

- Put your real models and prices in `models.json`.
- The `good_for` text is what Jev reads. Make it specific.
- Plug `route()` into your app before every LLM call.
- Log what the big model would have cost. Show the savings.

---

## Inspired by

The idea of Jev-based model routing is popular in the community, for example [jev-router](https://github.com/gargpratyush/jev-router) for Claude Code and Codex. This project is a small, from-scratch version to learn from.
