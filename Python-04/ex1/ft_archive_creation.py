#!/usr/bin/env python3

import sys
import typing


def read_file(filename: str) -> typing.Optional[str]:
    try:
        f: typing.IO[str]
        with open(filename, "r") as f:
            print("---")
            content = f.read()
            print(content, end="")
            print("---")
        print(f"File '{filename}' closed.\n")
        return content
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None


def transform_content(content: str) -> str:
    print("Transform data:")
    print("---")
    lines = content.splitlines(keepends=True)
    transformed = []
    for line in lines:
        if line.endswith("\n"):
            transformed.append(line.rstrip("\r\n") + "#\n")
        else:
            transformed.append(line + "#")
    result = "".join(transformed)
    print(result, end="")
    print("---")
    return result


def save_new_file(filename: str, content: str):
    if filename == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{filename}'")
    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"Data saved in file '{filename}'.")
    except OSError as e:
        print(f"Error saving file '{filename}': {e}")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Acessing file '{filename}'")
    content = read_file(filename)
    if content is None:
        return

    transformed = transform_content(content)
    new_filename = input("Enter new file name (or empty): ")
    save_new_file(new_filename, transformed)


if __name__ == "__main__":
    main()
