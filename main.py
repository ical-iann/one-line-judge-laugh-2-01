#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Writes a single funny line (<= 200 characters) to /output/entry.txt.
Deterministic: no network, no randomness, no environment dependence.
"""

LINE = "I quit my job to follow my dreams. My dreams filed a restraining order, and my landlord co-signed it."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
