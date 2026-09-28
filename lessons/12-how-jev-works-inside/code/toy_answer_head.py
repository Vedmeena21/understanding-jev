"""A toy model of the idea behind Jev. No API key needed.

An LLM's "LM head" scores EVERY word in its vocabulary, picks one, and repeats.
Jev's (likely) "answer head" scores ONLY your options, once.

python toy_answer_head.py
"""

import math

# Pretend the model has already read the question (the "prefill" step)
# and learned how well each word fits. Real models learn these numbers.
QUESTION = "What is the capital of India?"
VOCAB_SCORES = [
    # (words written so far) → score for every word in a tiny vocabulary
    {"The": 3.0, "New": 1.0, "Delhi": 0.5, "Mumbai": 0.2, "capital": 0.1, "is": 0.1, ".": 0.0},
    {"capital": 3.2, "New": 0.4, "Delhi": 0.3, "The": 0.1, "is": 0.2, "Mumbai": 0.1, ".": 0.0},
    {"is": 3.1, "New": 0.5, "Delhi": 0.4, "The": 0.0, "capital": 0.0, "Mumbai": 0.2, ".": 0.1},
    {"New": 3.4, "Mumbai": 1.1, "Delhi": 0.9, "The": 0.0, "capital": 0.0, "is": 0.0, ".": 0.1},
    {"Delhi": 3.6, "Mumbai": 0.2, "New": 0.1, "The": 0.0, "capital": 0.0, "is": 0.0, ".": 0.3},
    {".": 3.5, "Delhi": 0.1, "New": 0.0, "The": 0.0, "capital": 0.0, "is": 0.0, "Mumbai": 0.0},
]
OPTION_SCORES = {"Mumbai": 1.2, "Chennai": 0.3, "Delhi": 3.9, "Kolkata": 0.4}


def softmax(scores):
    """Turn raw scores into probabilities that add up to 1."""
    top = max(scores.values())
    exp = {k: math.exp(v - top) for k, v in scores.items()}
    total = sum(exp.values())
    return {k: v / total for k, v in exp.items()}


print(f"Question: {QUESTION}\n")

print("LLM with an LM head: one word per step, over the whole vocabulary")
words = []
for step, scores in enumerate(VOCAB_SCORES, 1):
    probs = softmax(scores)
    word = max(probs, key=probs.get)
    words.append(word)
    print(f"  step {step}: scores {len(scores)} words → picks {word!r:<10} ({probs[word]:.2f})")
print(f"  answer: {' '.join(words).replace(' .', '.')}")
print(f"  steps: {len(VOCAB_SCORES)} · then your code must pull 'Delhi' out of the text\n")

print("Jev-style answer head: score only your options, once")
probs = softmax(OPTION_SCORES)
for option, p in sorted(probs.items(), key=lambda kv: -kv[1]):
    bar = "█" * round(p * 30)
    print(f"  {option:<8} {p:.2f} {bar}")
print("  steps: 1 · the answer is already one of your options")
