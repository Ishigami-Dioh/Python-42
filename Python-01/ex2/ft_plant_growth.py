#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, amount: float) -> None:
        self.height += amount

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height: .1f}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    initial_height = rose.height

    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age_one_day()
        rose.show()

    total_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
