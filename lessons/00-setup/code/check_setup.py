"""Check that your Jev setup works.

pip install typesafe-sdk
export TYPESAFE_API_KEY="your-key"
python check_setup.py
"""

import os
import sys
import time

if not os.environ.get("TYPESAFE_API_KEY"):
    sys.exit("✗ TYPESAFE_API_KEY is not set. See lessons/00-setup/README.md")
print("✓ TYPESAFE_API_KEY is set")

try:
    from typesafe_sdk import Noul, TypeSafeClient
except ImportError:
    sys.exit("✗ typesafe-sdk is not installed. Run: pip install typesafe-sdk")
print("✓ typesafe-sdk is installed")

client = TypeSafeClient()

start = time.perf_counter()
response = client.system_one(
    state="CONGRATULATIONS!!! You won a free iPhone. Click here to claim now.",
    questions={"spam": Noul(instructions="Is this message spam?")},
)
seconds = time.perf_counter() - start

print(f"✓ Jev answered in {seconds:.2f} s")
print(f'  "Is this message spam?" → {response.answers["spam"].noul:.2f}')
print("All set. Go to lesson 01.")
