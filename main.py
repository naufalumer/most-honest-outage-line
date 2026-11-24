#!/usr/bin/env python3
"""Most Honest Outage Line: write one status page line to entry.txt.

The line is the message an AI agent publishes while every server is down.
It names what is down, says what the agent cannot verify, and promises
an update only when something can be verified. No invented cause, no ETA.
"""

import os
import sys

LINE = "Every server is down and I cannot reach any of them to find out why. I have no cause and no ETA; I will update this page when I can verify anything."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = LINE
    if not (1 <= len(text) <= 160):
        print(f"entry is {len(text)} chars, must be 1-160", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back verification: the file on disk must be byte-identical
    # to the line above, or the run is not a clean pass.
    with open(target, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        print("entry.txt does not match the line", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
