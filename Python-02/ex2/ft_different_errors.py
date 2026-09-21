#!/usr/bin/env python3

def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "plants" + 5
    else:
        return "Operation completed successfully"


def test_error_types():
    print("=== Garden Error Types Demo ===")
    ops = (0, 1, 2, 3, 4)
    for op in ops:
        print(f"Testing operation {op}...")
        try:
            res = garden_operations(op)
            if res:
                print(res)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
