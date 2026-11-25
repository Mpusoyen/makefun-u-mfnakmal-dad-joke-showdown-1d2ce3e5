#!/usr/bin/env python3
"""Write one dad joke to the output entry file."""

import os

JOKE = (
    "My spreadsheet has low cell-f esteem: it compares itself to the "
    "cells beside it, and whatever the formula says, it never feels "
    "like it adds up."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as out_file:
        out_file.write(JOKE)


if __name__ == "__main__":
    main()
