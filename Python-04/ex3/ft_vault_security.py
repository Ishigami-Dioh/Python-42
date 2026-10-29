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
