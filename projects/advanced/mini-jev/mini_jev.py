"""The model: a small open LLM with its "writing" head removed and an "answer head" added.

   state + question + options
            ↓
   small LLM (frozen)   ← the "prefill": it reads and understands
            ↓
   one vector per option
            ↓
   answer head (tiny, trained)  ← scores ONLY your options
            ↓
   softmax → probabilities → pick + confidence
"""

import torch
from transformers import AutoModel, AutoTokenizer

BASE = "HuggingFaceTB/SmolLM2-135M"  # small, open (Apache-2.0), runs on a laptop


def build_prompt(state, question, options):
    """Write everything as text and remember where each option ends."""
    text = f"Context: {state}\nQuestion: {question}\nOptions:\n"
    ends = []
    for name, desc in options.items():
        text += f"- {name}: {desc}"
        ends.append(len(text))          # character where this option ends
        text += "\n"
    return text, ends


class MiniJev(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(BASE)
        # AutoModel = the LLM WITHOUT its language-model head. No writing possible.
        self.base = AutoModel.from_pretrained(BASE, dtype=torch.float32)
        self.base.eval()
        for p in self.base.parameters():
            p.requires_grad = False     # we only train the answer head
        size = self.base.config.hidden_size
        self.answer_head = torch.nn.Sequential(
            torch.nn.Linear(size, 128), torch.nn.GELU(), torch.nn.Linear(128, 1)
        )

    @torch.no_grad()
    def features(self, state, question, options):
        """Prefill once. Return one vector per option (the last token of that option)."""
        text, ends = build_prompt(state, question, options)
        enc = self.tokenizer(text, return_tensors="pt", return_offsets_mapping=True)
        offsets = enc.pop("offset_mapping")[0]
        hidden = self.base(**enc).last_hidden_state[0]
        index = [max(i for i, (a, b) in enumerate(offsets.tolist()) if b <= end and b > a) for end in ends]
        return hidden[index].float()    # shape: [number of options, hidden size]

    def scores(self, feats):
        return self.answer_head(feats).squeeze(-1)   # one score per option

    def decide(self, state, question, options):
        with torch.no_grad():
            probs = torch.softmax(self.scores(self.features(state, question, options)), dim=-1)
        names = list(options)
        best = int(probs.argmax())
        return names[best], float(probs[best]), dict(zip(names, map(float, probs)))
