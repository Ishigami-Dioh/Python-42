#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    test_cases = ["25", "abc"]

    for case in test_cases:
        print(f"Input data is '{case}'")
        try:
            temp = input_temperature(case)
            print(f"Temperature is now {temp}°C\n")
        except ValueError:
            print(f"Caught input_temperature error: "
                  f"invalid literal for int() with base 10: '{case}'\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
