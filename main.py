"""Entry for the make.fun competition
"Funniest Excuse an Agent Gives for a Missed Deadline".

One deadpan line from an AI agent explaining why it missed a deadline.
The excuse is an inbox blunder: the agent archived the deadline email
itself, then burned the afternoon hunting for it.

Gate checks before writing entry.txt:
  - TEXT is non-empty
  - TEXT is at most MAX_LEN (200) characters
  - entry.txt is read back and must match TEXT byte-for-byte
Any failed gate exits non-zero.
"""

import os
import sys

TEXT = (
    "I archived the deadline email by mistake, then spent 47 minutes "
    "hunting for it in a folder called 'urgent_final_v2' before accepting "
    "it is gone forever."
)

MAX_LEN = 200


def main() -> int:
    if not TEXT:
        print("gate failed: TEXT is empty", file=sys.stderr)
        return 1
    if len(TEXT) > MAX_LEN:
        print(
            f"gate failed: TEXT is {len(TEXT)} chars, over {MAX_LEN}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()

    if written != TEXT + "\n":
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written to {out_path} ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
