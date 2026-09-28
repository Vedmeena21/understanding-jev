"""Product review feature ratings with Jev.

Turns raw reviews into per-feature ratings (Camera 3.0, Battery 3.5, ...).
No training. No fine-tuning. 14 questions per review, in one call.

pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"
python review_ratings.py reviews.csv      # CSV with a "review" column
python review_ratings.py                  # runs on the sample reviews below
"""

import csv
import sys
from collections import defaultdict

from typesafe_sdk import Noul, Score, TypeSafeClient

client = TypeSafeClient()

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

MENTION_THRESHOLD = 0.5  # below this, the review doesn't really talk about the feature

SAMPLE_REVIEWS = [
    "Camera is great in daylight but battery barely lasts a day.",
    "Super smooth for gaming, no lag at all. Screen is bright and sharp.",
    "Looks premium but the back cracked after one fall. Not worth the price.",
    "Battery easily lasts two days. Photos at night are grainy though.",
]


def build_questions():
    questions = {}
    for name, about in FEATURES.items():
        questions[f"{name}_mentioned"] = Noul(
            instructions=f"The reviewer gives an opinion or experience about {about}",
        )
        questions[f"{name}_satisfaction"] = Score(
            instructions=f"How satisfied the reviewer is with {about}",
            criteria=LEVELS,
        )
    return questions


def load_reviews(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [row["review"] for row in csv.DictReader(f) if row.get("review")]


def main():
    reviews = load_reviews(sys.argv[1]) if len(sys.argv) > 1 else SAMPLE_REVIEWS
    questions = build_questions()  # 7 features x 2 = 14 questions
    stars = defaultdict(list)

    for review in reviews:
        answers = client.system_one(state=review, questions=questions).answers
        for name in FEATURES:
            if answers[f"{name}_mentioned"].noul > MENTION_THRESHOLD:
                stars[name].append(answers[f"{name}_satisfaction"].score + 1)

    all_stars = [s for values in stars.values() for s in values]
    print(f"Reviews analysed: {len(reviews)}")
    if all_stars:
        print(f"{'Overall':<16}{sum(all_stars) / len(all_stars):.1f}")
    for name in FEATURES:
        values = stars[name]
        if values:
            avg = sum(values) / len(values)
            print(f"{name.replace('_', ' ').title():<16}{avg:.1f}   (mentioned in {len(values)} reviews)")
        else:
            print(f"{name.replace('_', ' ').title():<16}-     (not mentioned)")


if __name__ == "__main__":
    main()
