#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. Pure Python standard library, no network.
Output is exactly the username: no trailing newline, no extra text.
"""

import os

# The entry: the entrant's own make.fun username, one word, 10 chars.
USERNAME = "acengpikri"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(USERNAME)
    print(USERNAME)


if __name__ == "__main__":
    main()
