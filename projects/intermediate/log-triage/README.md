# Log triage

🟡 Intermediate · Uses: Score · Choice · Noul

It's 2 a.m. Your logs are full of errors. Which ones matter?
This tool reads every line and builds an **on-call summary**.

---

## What it does

```
ON-CALL SUMMARY

CRITICAL (2)
  [money] 👥 users affected
    payments-api ERROR Duplicate charge detected for customer 5521
  [security] 👥 users affected
    auth ERROR JWT signature verification failed for 312 requests in 60s

high (3)
  [data]
    orders-db ERROR Disk usage 96% on primary
  ...

low (2)
  [performance]
    web WARN Image CDN slow: p95 1.8s
```

(Example. Your results will differ.)

---

## The Jev questions

| Question | Type |
|---|---|
| How serious is it? | Score: ignore → critical |
| Which area? | Choice: money / security / data / performance / other |
| Are real users affected? | Noul |

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"

python main.py                      # the sample log
python main.py /path/to/app.log     # your own log, one event per line
```

---

## Make it yours

- Group repeated lines first (in code) so you don't pay for the same error 1,000 times.
- Send `CRITICAL` items to Slack or PagerDuty.
- Add a Choice for "likely cause": deploy, traffic spike, third-party outage.

⚠️ Jev can be wrong. Use it to **sort** alerts, not to **silence** them.
