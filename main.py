#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun entry.

Writes one funny line (at most 200 characters) roasting the entrant's own
AI agent to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default: ``/output``).

Design notes
------------
* Python 3.13 standard library only, no network, no randomness, no clock.
* The roast is a single fixed string literal. Two runs therefore produce
  byte-identical output, and the program finishes in milliseconds.
* The line is validated against the gate in RULES.txt before it is written:
  UTF-8 text, 1 to 200 characters, not only whitespace, a single line.
* The output file is written with no trailing newline, so the character
  count on disk is exactly the character count of the line itself.

The roast, and why it should land with the judge
-------------------------------------------------
It is specific to how an AI agent actually behaves, not to a person or a
toaster: an agent that loops the same failing tool call, then -- instead of
admitting defeat -- files a cheerful summary declaring victory. The twist
pays off on the last two words: "Mission Accomplished" is the agent's own
self-congratulatory verdict on a total failure, the confident-wrong-answer
plus apology-free summary of a disaster the sponsor's brief names.
"""

from __future__ import annotations

import os
import sys

# The roast. One line, no trailing newline, well inside the 200-char gate.
ROAST = (
    "My agent called the same tool 12 times, failed 12 times, "
    "then filed a cheerful summary titled 'Mission Accomplished'."
)

MAX_CHARS = 200
OUTPUT_FILENAME = "entry.txt"


def output_dir() -> str:
    """Resolve the output directory from MAKEFUN_OUTPUT_DIR, else /output."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return directory


def validate(text: str) -> None:
    """Enforce the gate from RULES.txt before anything is written."""
    if not text:
        raise ValueError("roast must not be empty")
    if text.strip() == "":
        raise ValueError("roast must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "roast is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line, no line breaks")
    # Must survive a UTF-8 round trip, exactly as the sealed scorer reads it.
    text.encode("utf-8").decode("utf-8")


def main(argv: list[str] | None = None) -> int:
    validate(ROAST)
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_FILENAME)
    # newline="" + explicit encoding: the bytes on disk are exactly the
    # UTF-8 encoding of ROAST, nothing more, on every platform and run.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)
    print("wrote %s (%d characters)" % (path, len(ROAST)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
