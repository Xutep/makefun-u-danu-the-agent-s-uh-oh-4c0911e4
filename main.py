#!/usr/bin/env python3
"""The Agent's Uh-Oh - make.fun entry.

One word an agent says when it has no idea what to do: the sound a
machine makes when it stalls mid-task. Writes it to /output/entry.txt.
"""

import os

WORD = "beep"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
