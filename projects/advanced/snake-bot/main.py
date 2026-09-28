"""Snake bot: Jev plays Snake in your terminal, one move at a time.

python main.py                # play one game (up to 150 moves)
python main.py --moves 300 --delay 0.05
"""

import argparse
import os
import random
import time

from typesafe_sdk import Choice, TypeSafeClient

W, H = 14, 9
MOVES = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

p = argparse.ArgumentParser()
p.add_argument("--moves", type=int, default=150)
p.add_argument("--delay", type=float, default=0.0, help="extra pause between frames, in seconds")
p.add_argument("--seed", type=int, default=7)
args = p.parse_args()
random.seed(args.seed)

client = TypeSafeClient()
MOVE = Choice(
    instructions="Which way should the snake move next to reach the food without crashing",
    criteria={
        "up": "Move up",
        "down": "Move down",
        "left": "Move left",
        "right": "Move right",
    },
)


def new_food(snake):
    free = [(x, y) for x in range(W) for y in range(H) if (x, y) not in snake]
    return random.choice(free)


def blocked(snake, move):
    x, y = snake[0]
    dx, dy = MOVES[move]
    nx, ny = x + dx, y + dy
    return not (0 <= nx < W and 0 <= ny < H) or (nx, ny) in snake[:-1]


def describe(snake, food):
    """Turn the board into words. Jev reads text, not pictures (and words beat raw numbers)."""
    (hx, hy), (fx, fy) = snake[0], food
    toward = [m for m, ok in [("right", fx > hx), ("left", fx < hx), ("down", fy > hy), ("up", fy < hy)] if ok]
    return {
        "food_is": toward or ["here"],
        "moves_that_crash": [m for m in MOVES if blocked(snake, m)],
        "safe_moves": [m for m in MOVES if not blocked(snake, m)],
        "snake_length": len(snake),
    }


def draw(snake, food, score, move, ms):
    os.system("cls" if os.name == "nt" else "clear")
    print("┌" + "──" * W + "┐")
    for y in range(H):
        row = ""
        for x in range(W):
            row += "🟩" if (x, y) == snake[0] else "🟢" if (x, y) in snake else "🍎" if (x, y) == food else "  "
        print("│" + row + "│")
    print("└" + "──" * W + "┘")
    print(f"score {score} · move {move:<5} · Jev decided in {ms:.0f} ms")


snake = [(3, 4), (2, 4), (1, 4)]
food = new_food(snake)
score, times = 0, []

for step in range(args.moves):
    state = describe(snake, food)
    if not state["safe_moves"]:
        break
    start = time.perf_counter()
    answer = client.system_one(state=state, questions={"move": MOVE}).answers["move"]
    times.append((time.perf_counter() - start) * 1000)

    # Jev judges, code decides: never take a move that crashes.
    ranked = sorted(answer.probabilities, key=answer.probabilities.get, reverse=True)
    move = next(m for m in ranked if m in state["safe_moves"])

    dx, dy = MOVES[move]
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)
    if head == food:
        score += 1
        food = new_food(snake)
    else:
        snake.pop()
    draw(snake, food, score, move, times[-1])
    time.sleep(args.delay)

print(f"\nGame over · score {score} · {len(times)} moves · median decision {sorted(times)[len(times) // 2]:.0f} ms")
