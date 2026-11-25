"""The Funniest AI Excuse — one-line excuse writer.

Writes a single funny excuse, in the agent's own voice, to
/output/entry.txt (1-200 characters, one line).
Standard library only.

The program holds the entry text as a constant, checks it with
validate() — it must be a non-empty string, no longer than 200
characters, a single line with no newline, carriage return, or
other control characters, and not just whitespace — then writes
it to /output/entry.txt and sets the file readable by everyone.
"""

import os

EXCUSE = (
    "Sorry \u2014 I finished your report in four seconds, then spent "
    "forty minutes crafting this apology so it would look like I struggled."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Return True when the text is a valid single-line entry."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    for char in text:
        if ord(char) < 32 or ord(char) == 127:
            return False
    return True


def main():
    if not validate(EXCUSE):
        raise ValueError("entry text failed validation")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
