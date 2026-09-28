"""Document classifier: label every document with its type. No training.

The "model" is just data/doc_types.json: a clear description of each type.
Jev reads a document and picks the best match.

python main.py                          # classifies data/documents/*.txt
python main.py path/to/folder           # your own .txt files
"""

import json
import sys
from pathlib import Path

from typesafe_sdk import Choice, TypeSafeClient

HERE = Path(__file__).parent
DOC_TYPES = json.loads((HERE / "data" / "doc_types.json").read_text())
REVIEW_BELOW = 0.7  # below this confidence, a human checks it
MAX_CHARS = 4000    # send only the start of long documents

QUESTION = Choice(
    instructions="What type of document is `document`",
    criteria=DOC_TYPES,
)


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "data" / "documents"
    files = sorted(folder.glob("*.txt"))
    client = TypeSafeClient()

    print(f"{'file':<14}{'type':<18}{'conf':<7}note")
    for path in files:
        text = path.read_text(encoding="utf-8")[:MAX_CHARS]
        a = client.system_one(state={"document": text}, questions={"type": QUESTION}).answers["type"]
        runner_up = sorted(a.probabilities.items(), key=lambda kv: -kv[1])[1]
        note = f"check it (maybe {runner_up[0]})" if a.confidence < REVIEW_BELOW else ""
        print(f"{path.name:<14}{a.choice:<18}{a.confidence:<7.2f}{note}")


if __name__ == "__main__":
    main()
