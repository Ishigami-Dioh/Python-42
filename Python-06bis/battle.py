#!/usr/bin/env python3

from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory):
    base_creature = factory.create_base()
    base_creature.describe()
    base_creature.attack()

    evolved_creature = factory.create_evolved()
    evolved_creature.describe()
    evolved_creature.attack()


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory):
    p1 = factory1.create_base()
    p2 = factory2.create_base()

    p1.describe()
    print("vs.")
    p2.describe()
    print("fight!")

    p1.attack()
    p2.attack()


def main():
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing factory")
    test_factory(flame_factory)

    print("\nTesting factory")
    test_factory(transform_factory)

    print("\nTesting battle")
    test_battle(flame_factory, transform_factory)


if __name__ == "__main__":
    main()
