#!/usr/bin/env python3
"""Write one dad joke to the output entry file."""

import os

JOKE = (
    "My spreadsheet has terrible cell-f esteem: it keeps comparing itself "
    "to every cell around it, and no matter what the formula says, it never "
    "feels like it adds up."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
