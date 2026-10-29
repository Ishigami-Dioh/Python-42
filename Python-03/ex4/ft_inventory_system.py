#!/usr/bin/env python3

import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        if ":" not in arg:
            print("Error - invalid parameter '{arg}'")
            continue
        item, qty_str = arg.split(":", 1)

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty = int(qty_str)
            inventory[item] = qty
        except ValueError:
            print(f"Quantity error for '{item}': "
                  f"invalid literal for int() with base 10: '{qty_str}'")
    return inventory


def print_percentages(inventory: dict[str, int], total_qty: int):
    if total_qty == 0:
        return
    for item, qty in inventory.items():
        pct = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {pct:.1f}%")


def print_abundance_report(inventory: dict[str, int]):
    if not inventory:
        return

    first_item = next(iter(inventory))
    max_item = min_item = first_item
    max_qty = min_qty = inventory[first_item]

    for item, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            max_item = item
        if qty < min_qty:
            min_qty = qty
            min_item = item

    print(f"Item most abundant: {max_item} with quantity {max_qty}")
    print(f"Item least abundant: {min_item} with quantity {min_qty}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])

    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total_qty}")

    print_percentages(inventory, total_qty)
    print_abundance_report(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
