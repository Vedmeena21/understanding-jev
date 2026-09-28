"""Review ratings: turn raw reviews into per-feature ratings.

7 features x 2 questions = 14 questions per review, in ONE call.
No training. No fine-tuning.

python main.py                     # uses data/reviews.csv
python main.py my_reviews.csv      # your CSV with a "review" column
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

from typesafe_sdk import Noul, Score, TypeSafeClient

HERE = Path(__file__).parent

FEATURES = {
    "camera": "the camera, photos or videos",
    "battery": "battery life or charging",
    "display": "the display or screen",
    "design": "the design or looks",
    "performance": "speed, lag or gaming performance",
    "build_quality": "build quality or durability",
    "value_for_money": "price and value for money",
}

# 5 levels, lowest to highest. Jev's score lands on 0..4, so stars = score + 1.
LEVELS = ["Very unhappy", "Unhappy", "Neutral", "Happy", "Very happy"]
MENTIONED = 0.5  # below this, the review doesn't really talk about the feature


def build_questions():
    questions = {}
    for name, about in FEATURES.items():
        questions[f"{name}_mentioned"] = Noul(instructions=f"The reviewer gives an opinion or experience about {about}")
        questions[f"{name}_rating"] = Score(instructions=f"How satisfied the reviewer is with {about}", criteria=LEVELS)
    return questions


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else HERE / "data" / "reviews.csv"
    with open(path, newline="", encoding="utf-8") as f:
        reviews = [row["review"] for row in csv.DictReader(f) if row.get("review")]

    client = TypeSafeClient()
    questions = build_questions()
    stars = defaultdict(list)       # feature → list of star ratings
    quotes = defaultdict(list)      # feature → reviews that mention it

    for review in reviews:
        answers = client.system_one(state=review, questions=questions).answers
        for name in FEATURES:
            if answers[f"{name}_mentioned"].noul > MENTIONED:
                stars[name].append(answers[f"{name}_rating"].score + 1)
                quotes[name].append(review)

    everything = [s for values in stars.values() for s in values]
    print(f"{len(reviews)} reviews\n")
    if everything:
        print(f"{'Overall':<17}{sum(everything) / len(everything):.1f} ★")
    for name in FEATURES:
        label = name.replace("_", " ").title()
        if stars[name]:
            avg = sum(stars[name]) / len(stars[name])
            print(f"{label:<17}{avg:.1f} ★  {'█' * round(avg * 2):<10} {len(stars[name])} reviews")
        else:
            print(f"{label:<17}  -   not mentioned")

    worst = min((n for n in FEATURES if stars[n]), key=lambda n: sum(stars[n]) / len(stars[n]), default=None)
    if worst:
        print(f"\nWeakest feature: {worst.replace('_', ' ')}. What people say:")
        for q in quotes[worst][:3]:
            print("  •", q)


if __name__ == "__main__":
    main()
