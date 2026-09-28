"""Step 3: ask your mini-Jev a question.

python predict.py "My order never arrived" "Which team should handle this message?" \
    "billing=payments, charges, refunds" "shipping=delivery, damaged or missing items" \
    "technical=bugs, errors, crashes" "general=anything else"

Options are name=description. The description matters, just like with real Jev.
"""

import sys
from pathlib import Path

import torch

from mini_jev import MiniJev

if len(sys.argv) < 5:
    sys.exit('Usage: python predict.py "message" "question" "name=description" "name=description" ...')

state, question = sys.argv[1], sys.argv[2]
options = dict(arg.split("=", 1) if "=" in arg else (arg, arg) for arg in sys.argv[3:])
model = MiniJev()
model.answer_head.load_state_dict(torch.load(Path(__file__).parent / "mini_jev_head.pt"))

pick, confidence, probs = model.decide(state, question, options)
print(f"→ {pick}  (confidence {confidence:.2f})")
for name, p in sorted(probs.items(), key=lambda kv: -kv[1]):
    print(f"   {name:<12} {p:.2f} {'█' * round(p * 30)}")
