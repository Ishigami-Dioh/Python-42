#!/usr/bin/env python3

import alchemy.transmutation.recipes


def main():
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    result = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {result}")


if __name__ == "__main__":
    main()
