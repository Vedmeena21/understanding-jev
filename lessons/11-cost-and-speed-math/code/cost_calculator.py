"""What does Jev save you? No API key needed.

python cost_calculator.py
python cost_calculator.py --per-day 50000 --tokens-in 800 --llm-out 150 --llm-in-price 1.25 --llm-out-price 10
"""

import argparse

p = argparse.ArgumentParser(description="Compare the cost of decisions on Jev vs an LLM.")
p.add_argument("--per-day", type=int, default=10_000, help="decisions per day")
p.add_argument("--tokens-in", type=int, default=1_000, help="input tokens per decision")
p.add_argument("--llm-out", type=int, default=200, help="output tokens the LLM writes per decision")
p.add_argument("--llm-in-price", type=float, default=1.25, help="LLM price per 1M input tokens (USD)")
p.add_argument("--llm-out-price", type=float, default=10.0, help="LLM price per 1M output tokens (USD)")
p.add_argument("--jev-in-price", type=float, default=0.042, help="Jev price per 1M input tokens (USD)")
a = p.parse_args()

llm_each = a.tokens_in * a.llm_in_price / 1e6 + a.llm_out * a.llm_out_price / 1e6
jev_each = a.tokens_in * a.jev_in_price / 1e6  # Jev output is free

print(f"{a.per_day:,} decisions a day · {a.tokens_in} tokens in · LLM writes {a.llm_out} tokens\n")
print(f"{'':<6}{'per decision':>14}{'per day':>12}{'per month':>12}{'per year':>13}")
for name, each in [("LLM", llm_each), ("Jev", jev_each)]:
    day = each * a.per_day
    print(f"{name:<6}{'$' + format(each, '.6f'):>14}{'$' + format(day, ',.2f'):>12}{'$' + format(day * 30, ',.2f'):>12}{'$' + format(day * 365, ',.2f'):>13}")
print(f"\nJev is about {llm_each / jev_each:.0f}x cheaper for this workload.")
