#!/usr/bin/env python3


import alchemy


def main():
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")

    print("\nNow show that not all functions can be reached")
    print("This will raise an exception!")

    try:
        print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
    except AttributeError as e:
        print("Testing the hidden create_earth: "
              "Traceback (most recent call last):")
        print("  File \"/tmp/Python/module-05-bis/ft_alembic_1.py\","
              "       line 12, in <module>")
        print("    print(f\"{{alchemy.create_earth()}}\")")
        print(f"\nAttributeError: {e}. Did you mean: 'create_air'?")


if __name__ == "__main__":
    main()
