# Code · Evals and tracing

| File | What it does |
|---|---|
| `mini_eval.py` | Measures accuracy, speed and cost on labeled data |
| `data/` | 20 labeled messages: spam or not |

```bash
python mini_eval.py                 # uses data/eval_set.csv
python mini_eval.py my_data.csv     # columns: message,label (spam / not_spam)
```
