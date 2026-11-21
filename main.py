#!/usr/bin/env python3
"""Writes one one-line joke about working beside AI coding agents."""

import os

JOKE = "I asked my agent to write the function. It wrote 400 lines, deleted 399, and left a comment: TODO: implement this."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
