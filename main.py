#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the roast to /output/entry.txt.
"""

import os

LINE = "My agent's context window is so small it forgot this sentence before finishing it."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
