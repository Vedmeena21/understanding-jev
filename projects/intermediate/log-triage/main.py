"""Log triage: read error logs, build an on-call summary.

python main.py                     # uses data/errors.log
python main.py /path/to/app.log    # your own log (one event per line)
"""

import sys
from collections import defaultdict
from pathlib import Path

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

HERE = Path(__file__).parent

QUESTIONS = {
    "severity": Score(
        instructions="How serious is `log_line` for the business right now",
        criteria=["Ignore", "Low: fix this week", "High: fix today", "Critical: wake someone up"],
    ),
    "area": Choice(
        instructions="Which area is `log_line` about",
        criteria={
            "money": "Payments, charges, refunds, billing",
            "security": "Login, tokens, permissions, suspicious access",
            "data": "Databases, disks, backups, data loss",
            "performance": "Slowness, timeouts, high latency",
            "other": "Anything else",
        },
    ),
    "users_affected": Noul(instructions="`log_line` means real users are affected right now"),
}
SEVERITY = ["ignore", "low", "high", "CRITICAL"]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "data" / "errors.log"
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    client = TypeSafeClient()
    groups = defaultdict(list)
    for line in lines:
        a = client.system_one(state={"log_line": line}, questions=QUESTIONS).answers
        level = min(3, round(a["severity"].score))
        groups[level].append((a["area"].choice, a["users_affected"].noul > 0.5, line))

    print("ON-CALL SUMMARY\n")
    for level in (3, 2, 1, 0):
        if not groups[level]:
            continue
        print(f"{SEVERITY[level]} ({len(groups[level])})")
        for area, users, line in groups[level]:
            print(f"  [{area}]{' 👥 users affected' if users else ''}\n    {line}")
        print()


if __name__ == "__main__":
    main()
