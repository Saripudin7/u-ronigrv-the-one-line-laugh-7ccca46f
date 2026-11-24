#!/usr/bin/env python3
"""The One-Line Laugh — writes one original one-liner to entry.txt.

SPDX-License-Identifier: MIT
"""

import os
import sys

JOKE = "I asked my smart speaker for a joke, and it read my search history out loud."

# Gate guard: the entry must be a single sentence of 1-200 characters.
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
assert JOKE.count(".") == 1 and JOKE.endswith("."), "joke must be one sentence"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
