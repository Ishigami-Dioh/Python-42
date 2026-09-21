#!/usr/bin/env python3

class GardenError(Exception):

    def __init__(self, message="A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):

    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):

    def __init__(self, message="Unknown water Error"):
        super().__init__(message)


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    errors_to_test = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]
    for err in errors_to_test:
        try:
            raise err
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
