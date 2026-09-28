# Document classifier

🟡 Intermediate · Uses: Choice

Labels documents: invoice, salary slip, bank statement, offer letter, resume…
**No model training.** The whole "model" is a JSON file of descriptions.

---

## What it does

```
file          type              conf   note
doc_01.txt    invoice           0.97
doc_02.txt    salary_slip       0.95
doc_03.txt    offer_letter      0.93
doc_04.txt    rent_agreement    0.96
doc_05.txt    bank_statement    0.94
doc_06.txt    resume            0.62   check it (maybe offer_letter)
```

(Example. Your numbers will differ.)

---

## The trick: good descriptions

Open `data/doc_types.json`. Every type looks like this:

```json
"salary_slip": {
  "what": "A monthly pay slip from an employer showing earnings, deductions and net pay",
  "signals": ["Basic", "HRA", "PF", "Net pay", "Employee ID"],
  "not_for": "An offer letter (that promises pay, it doesn't pay it)"
}
```

- `what`: what it is
- `signals`: words that usually appear
- `not_for`: the look-alike it should **not** be confused with

Better descriptions = better accuracy. No retraining. Ever.

---

## The Jev question

| Question | Type |
|---|---|
| What type of document is this? | Choice (up to 255 types) |

Below 70% confidence → it tells you to check, and shows the runner-up.

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"

python main.py                     # the 6 sample documents
python main.py path/to/folder      # your own .txt files
```

Have PDFs? Turn them into text first (for example with `pdftotext`).

---

## Make it yours

- Add your own document types to `doc_types.json`.
- Classify **page by page** for long PDFs.
- Route each type to its own next step: invoices → accounts, resumes → HR.

---

## Inspired by

[kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) classifies 261 IRS tax forms the same way, at about $0.001 per page. This project is a small, from-scratch version with everyday documents.
