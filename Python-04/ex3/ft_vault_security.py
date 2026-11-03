#!/usr/bin/env python3

def secure_archive(
        filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:

    try:
        if action == "read":
            with open(filename, "r") as f:
                return (True, f.read())
        else:
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))


def main():
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow", "read"))

    test_file = "fragment_test.txt"
    write_res = secure_archive(
        test_file,
        "write",
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
    )
    print("Using 'secure_archive' to write content to a new file:")
    print(write_res)

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive(test_file, "read"))


if __name__ == "__main__":
    main()
