#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt. The label is at most 160 characters, UTF-8, one line.
"""

import os

# The label is composed from parts so the wording stays easy to tune
# without touching the output logic.
_PARTS = [
    "WARNING: Contents under pressure.",
    "This human has never read the instructions",
    "and will argue about them anyway.",
]
def build_label(parts):
    """Join label parts into one line and enforce the entry gate.

    Returns the single-line label; raises AssertionError if it is
    empty, over 160 characters, or spans more than one line.
    """
    label = " ".join(part.strip() for part in parts if part.strip())
    assert 1 <= len(label) <= 160, f"label is {len(label)} chars, must be 1-160"
    assert "\n" not in label, "label must be a single line"
    return label


LABEL = build_label(_PARTS)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(LABEL)


if __name__ == "__main__":
    main()
