"""Model router: send each prompt to the cheapest model that can handle it.

python main.py                        # routes every line in prompts.txt
python main.py "Explain recursion"    # routes one prompt
Edit models.json to use your real models and prices.
"""

import json
import sys
from pathlib import Path

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

HERE = Path(__file__).parent
MODELS = json.loads((HERE / "models.json").read_text())
SURE = 0.7            # below this, play safe and go one size up
TOKENS_OUT = 800      # rough output size, for the cost estimate

QUESTIONS = {
    "model": Choice(
        instructions="Which model size is enough to do `prompt` well",
        criteria={key: m["good_for"] for key, m in MODELS.items()},
    ),
    "difficulty": Score(instructions="How hard is `prompt`", criteria=["Trivial", "Easy", "Medium", "Hard", "Very hard"]),
    "needs_code": Noul(instructions="`prompt` asks to write, read or fix code"),
}
ORDER = list(MODELS)  # small → medium → frontier


def route(client, prompt):
    a = client.system_one(state={"prompt": prompt}, questions=QUESTIONS).answers
    pick = a["model"]
    key = pick.choice
    if pick.confidence < SURE and key != ORDER[-1]:
        key = ORDER[ORDER.index(key) + 1]  # not sure → one size up
    return key, pick.confidence, a["difficulty"].score, a["needs_code"].noul


def main():
    prompts = [" ".join(sys.argv[1:])] if len(sys.argv) > 1 else (HERE / "prompts.txt").read_text().strip().splitlines()
    client = TypeSafeClient()
    routed_cost = frontier_cost = 0.0

    print(f"{'model':<10}{'conf':<6}{'hard':<6}{'code':<6}prompt")
    for prompt in prompts:
        key, conf, hard, code = route(client, prompt)
        routed_cost += TOKENS_OUT * MODELS[key]["price_per_1m_output"] / 1e6
        frontier_cost += TOKENS_OUT * MODELS["frontier"]["price_per_1m_output"] / 1e6
        print(f"{key:<10}{conf:<6.2f}{hard:<6.1f}{'yes' if code > 0.5 else '':<6}{prompt[:60]}")

    if len(prompts) > 1:
        saved = 1 - routed_cost / frontier_cost
        print(f"\nEverything on frontier: ${frontier_cost:.4f}")
        print(f"With routing:           ${routed_cost:.4f}  ({saved:.0%} saved)")


if __name__ == "__main__":
    main()
