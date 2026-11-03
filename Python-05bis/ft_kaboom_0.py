#!/usr/bin/env python3

from alchemy.grimoire.light_spellbook import light_spell_record


def main():
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    res = light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {res}")


if __name__ == "__main__":
    main()
