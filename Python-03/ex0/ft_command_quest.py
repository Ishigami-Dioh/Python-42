#!/usr/bin/env python3

import sys

def main():
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    x = len(sys.argv)
    i = 1
    if x > i:
        print(f"Arguments received: {x - 1}")
        while x > i:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {x}")


if __name__ == "__main__":
    main()
