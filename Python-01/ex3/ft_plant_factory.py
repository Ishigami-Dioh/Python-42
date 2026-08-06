#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = float(height)
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def main() -> None:
    print("=== Plant Factory Output ===")

    plant_data = [
            ("Rose", 25.0, 30),
            ("Oak", 200.0, 365),
            ("Cactus", 5.0, 90),
            ("Sunflower", 80.0, 45),
            ("Fern", 15.0, 120),
        ]

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
