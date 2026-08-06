def ft_count_harvest_recursive():
    duh = int(input("Days until harvest: "))

    def count_day(current: int) -> None:
        if current > duh:
            print("Harvest time!")
            return
        print(f"Day {current}")
        count_day(current + 1)

    count_day(1)
