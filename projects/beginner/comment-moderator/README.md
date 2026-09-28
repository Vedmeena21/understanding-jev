# Comment moderator

🟢 Beginner · Uses: Choice · Score · Noul

Goes through YouTube comments. Decides what to do with each one:
**keep**, **hide**, **reply**, or send to you to **review**.

---

## What it does

```
action  type      author        comment
keep    praise    riya_codes    This explained Jev better than the official docs…
hide    spam      spam_bot_99   Earn $500/day from home!!! Check my profile 🔥🔥
reply   question  dev_arjun     Does Jev work with Hindi text or only English?
hide    abuse     anon123       You clearly have no idea what you're talking…

Summary: 4 keep, 4 hide, 2 reply

Questions to answer:
  @dev_arjun: Does Jev work with Hindi text or only English?
  @sam_builds: How do I set the confidence threshold for my use case?
```

(Example. Your results will differ.)

---

## The Jev questions

| Question | Type |
|---|---|
| What kind of comment? | Choice: question / praise / feedback / spam / abuse |
| How rude? | Score: not at all → abusive |
| Does it need a reply? | Noul |

## The rules (in code, not in the model)

- Spam, abuse, or very rude → **hide**
- Jev isn't sure (confidence below 0.6) → **review**
- Needs a reply → **reply**
- Everything else → **keep**

Jev judges. Your code decides. That's the pattern.

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"
python main.py
python main.py my_comments.csv       # columns: author,comment
```

---

## Make it yours

- Pull real comments with the YouTube Data API.
- Hide automatically, but only above a confidence you trust.
- Add a "question topic" Choice to find what your audience asks most.
