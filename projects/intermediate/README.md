# 🟡 Intermediate projects

Jev inside a real tool.
Config files, routing rules and reports, with your code in charge.
Best after [lessons 00–10](../../lessons).

| Project | What it does | Jev question types |
|---|---|---|
| [Model router](model-router) | Sends each prompt to the cheapest model that can handle it | Choice · Score · Noul |
| [Document classifier](doc-classifier) | Labels documents with no training, from a JSON of descriptions | Choice |
| [Log triage](log-triage) | Turns raw error logs into an on-call summary | Score · Choice · Noul |

## The pattern in all 3

1. **Jev judges.** Which model? Which document type? How serious?
2. **Your code decides.** Thresholds, fallbacks, sorting, reports.
3. **Unsure → play safe.** Go one model size up, flag for review, or wake a human.

## Run any of them

```bash
cd model-router
python main.py
```
