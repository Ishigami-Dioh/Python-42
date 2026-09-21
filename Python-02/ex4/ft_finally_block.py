#!/usr/bin/env python3

class GardenError(Exception):

    def __init__(self, message="A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):

    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants):
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
