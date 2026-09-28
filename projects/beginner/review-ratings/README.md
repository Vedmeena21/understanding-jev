# Review ratings

🟢 Beginner · Uses: Noul · Score

Turns raw product reviews into ratings per feature.
Like the "Camera 4.6 · Battery 4.1" you see on shopping sites.

---

## What it does

```
12 reviews
        ↓
Overall          3.4 ★
Camera           3.0 ★  ██████     4 reviews
Battery          3.3 ★  ███████    4 reviews
Display          3.5 ★  ███████    3 reviews
...
Weakest feature: build quality. What people say:
  • Looks premium but the back cracked after one fall.
```

(Example. Your numbers will differ.)

- No training.
- No fine-tuning.
- About 90 lines.

Normally a data team would train or fine-tune a model (like BERT) for this.
With Jev, you just ask.

---

## The Jev questions

For **each** of 7 features, 2 questions:

| Question | Type |
|---|---|
| Does the review talk about this feature? | Noul |
| How happy is the reviewer with it? | Score (5 levels) |

7 × 2 = **14 questions per review, in one call.**

Features: camera, battery, display, design, performance, build quality, value for money.

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"
python main.py
```

Your own reviews:

```bash
python main.py my_reviews.csv      # a CSV with a "review" column
```

---

## How the math works

- A feature only counts if "mentioned" is above 0.5.
- The Score comes back on 0 to 4. Add 1 → stars from 1 to 5.
- Average the stars per feature.

---

## Make it yours

- Change `FEATURES` for your product (a laptop, a hotel, a course).
- Show the reviews behind each rating, like a real store does.
- Run it on 1,000 reviews and compare the cost to an LLM ([lesson 11](../../../lessons/11-cost-and-speed-math)).
