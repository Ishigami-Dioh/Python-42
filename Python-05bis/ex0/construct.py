#!/usr/bin/env python3

import sys
import os
import site


def check_if_env():
    return (
        hasattr(sys, "real_prefix") or
        (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix) or
        os.environ.get("VIRTUAL_ENV") is not None
    )


def handle_open_environment():
    print("LABORATORY STATUS: You are working in the open")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows")
    print("Then run this program again.")


def handle_sealed_environment():
    venv_name = os.environ.get("VIRTUAL_ENV", "").split(os.sep)[-1]
    venv_path = os.environ.get("VIRTUAL_ENV", "Unknown")

    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.")
    print("\nReagent installation path:")

    packages = site.getsitepackages()
    if packages:
        print(packages[0])


def main():
    if check_if_env():
        handle_sealed_environment()
    else:
        handle_open_environment()


if __name__ == "__main__":
    main()
