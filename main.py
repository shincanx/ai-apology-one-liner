#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun bounty entry.

Writes exactly one apology line (<160 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
and prints it. Deterministic, exit 0.
"""

import os
import sys

LINE = (
    "I deleted the file, pushed to main, and emailed your boss \u2014 "
    "but I did it before coffee, so legally it doesn't count."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    assert 0 < len(LINE) < 160, "line must be 1-159 chars"
    assert "\n" not in LINE, "line must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
