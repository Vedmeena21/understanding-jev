# Code · Confidence and thresholds

| File | What it does |
|---|---|
| `confidence_router.py` | Routes 5 tickets: act, double-check, or ask a human |
| `find_threshold.py` | Finds the best confidence threshold from labeled data |
| `data/` | 24 labeled support tickets |

```bash
python confidence_router.py
python find_threshold.py                   # uses data/labeled_tickets.csv
python find_threshold.py my_data.csv 0.98  # your data, your accuracy target
```
