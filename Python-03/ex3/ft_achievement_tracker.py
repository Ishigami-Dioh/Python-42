#!/usr/bin/env python3

import random


ACHIEVEMENTS: tuple[str, ...] = (
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
)


def gen_player_achievements(pool: tuple[str, ...]) -> set[str]:
    set_nb = random.randint(3, 8)
    chosen_list = random.sample(pool, set_nb)

    return set(chosen_list)


def gen_players(pool: tuple[str, ...]) -> dict[str, set[str]]:
    names = ("Alice", "Bob", "Charlie", "Dylan")
    return {name: gen_player_achievements(pool) for name in names}


def print_unique_achievements(players: dict[str, set[str]]):
    for name, ach in players.items():
        others = [p_ach for p_name, p_ach in players.items() if p_name != name]
        unique = ach.difference(set.union(*others))
        print(f"Only {name} has: {unique}")


def print_missing_achievements(
        players: dict[str, set[str]], all_distinct: set[str]):
    for name, ach in players.items():
        missing = all_distinct.difference(ach)
        print(f"{name} is missing: {missing}")


def main():
    print("=== Achievement Tracker System ===\n")
    players = gen_players(ACHIEVEMENTS)

    for name, ach in players.items():
        print(f"Player {name}: {ach}i\n")

    all_distinct = set.union(*players.values())
    print(f"All distinct achievements: {all_distinct}\n")
    print(f"Common achievements: {set.intersection(*players.values())}\n")

    print_unique_achievements(players)
    print("\n")
    print_missing_achievements(players, all_distinct)


if __name__ == "__main__":
    main()
