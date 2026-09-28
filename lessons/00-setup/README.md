# 00 · Setup

⏱ 10 min · 🎯 Beginner · 🧪 Code: [`code/check_setup.py`](code/check_setup.py)

[All lessons](../README.md) · [01 · What is Jev →](../01-what-is-jev)

---

## What you'll do

- Get a TypeSafe API key
- Install the SDK
- Make one tiny call to check everything works

---

## 1. Get an API key

1. Go to [typesafe.ai](https://typesafe.ai) and sign in.
2. Open the console → **API Keys**.
3. Create a new key. Copy it.

## 2. Save the key

Mac / Linux:

```bash
export TYPESAFE_API_KEY="your-key"
```

Windows (PowerShell):

```powershell
$env:TYPESAFE_API_KEY="your-key"
```

- The SDK reads this automatically.
- Never paste your key into code, GitHub or a chat.

## 3. Install

```bash
pip install typesafe-sdk
```

Using JavaScript instead? `npm install @typesafe-ai/sdk`

## 4. Check it works

```bash
python code/check_setup.py
```

You should see something like:

```
✓ TYPESAFE_API_KEY is set
✓ typesafe-sdk is installed
✓ Jev answered in 0.31 s
  "Is this message spam?" → 0.98
All set. Go to lesson 01.
```

---

## Using Claude Code, Codex, Cursor, MCP or LangChain?

See [Set up Jev everywhere](../../resources/setup-everywhere.md).

---

## Try the Playground too

- Open the **Playground** in the TypeSafe console.
- Paste some text. Write a question. Add options.
- Hit run. Watch the probabilities.

It's the fastest way to get a feel for Jev.

---

## Stuck?

| Problem | Fix |
|---|---|
| `TYPESAFE_API_KEY is not set` | Run the `export` line again in the same terminal |
| `No module named typesafe_sdk` | Run `pip install typesafe-sdk` in the same Python you use to run the script |
| Authentication error | The key is wrong or was deleted. Make a new one |
| Rate limit error | Wait a minute. Limits are busy right after launch |

---

## Quiz

<details><summary>1. Where should your API key live?</summary>

In an environment variable (`TYPESAFE_API_KEY`). Never in your code or on GitHub.
</details>

<details><summary>2. Which Python package do you install?</summary>

`typesafe-sdk`
</details>

<details><summary>3. What's the quickest way to try Jev without code?</summary>

The Playground in the TypeSafe console.
</details>

---

Next: [01 · What is Jev →](../01-what-is-jev)
