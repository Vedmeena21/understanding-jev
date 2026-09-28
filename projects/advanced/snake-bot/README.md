# Snake bot

🔴 Advanced · Uses: Choice (every move)

Jev plays Snake in your terminal.
Every move is one Jev decision: **up, down, left or right**.

---

## What it looks like

```
┌────────────────────────────┐
│                            │
│          🍎                │
│                            │
│      🟢🟢🟩                │
│                            │
└────────────────────────────┘
score 4 · move right · Jev decided in 180 ms
```

---

## The big lesson: turn the screen into words

Jev reads **text**, not pictures.
And it's better with **words** than raw numbers.

So the game is described like this:

```json
{
  "food_is": ["right", "up"],
  "moves_that_crash": ["left"],
  "safe_moves": ["up", "down", "right"],
  "snake_length": 5
}
```

Not like this: `"head": [3, 4], "food": [9, 1]`.

That's how every game and browser demo works with a text-only model.

---

## Jev judges. Code decides.

- Jev gives a probability for each move.
- The code takes the **most likely move that's safe**.
- So the snake never drives into a wall because of a bad guess.

---

## Run it

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"

python main.py                          # up to 150 moves
python main.py --moves 300 --delay 0.05
```

It costs very little: each move is a tiny request.

---

## Make it yours

- Add "moves that trap you in a corner" to the state. Does it survive longer?
- Try a bigger board.
- Build the same idea for 2048, Tetris or a browser game.
- Real-world version: [typesafe-mario](https://github.com/fhshaik/typesafe-mario) plays Super Mario from emulator state.
