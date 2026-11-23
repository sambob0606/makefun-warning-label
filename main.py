#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt. The label is at most 160 characters, UTF-8, one line.
"""

import os

LABEL = "WARNING: Contents under pressure. This human has never read the instructions and will argue about them anyway."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(LABEL)


if __name__ == "__main__":
    main()
