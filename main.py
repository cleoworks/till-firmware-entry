#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes one robot wedding vow (a single sentence, 75 characters) to
/output/entry.txt. Deterministic: the same bytes on every run.
No network, no input, no randomness.
"""

import os

VOW = "I vow to love you until someone unplugs me, and even then, on backup power."


def main():
    os.makedirs("/output", exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours the smaller text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
