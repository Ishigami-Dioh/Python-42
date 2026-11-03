#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Acessing file '{filename}'")

    try:
        f: typing.IO[str]
        with open(filename, "r") as f:
            print("---")
            print(f.read(), end="")
            print("---")
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
