from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (BattleStrategy, NormalStrategy, AggressiveStrategy,
                 InvalidStrategyError)


def tournament_run(name: str,
                   opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    print(f"Tournament {name}")
    creatures = [f.create_base() for f, _ in opponents]

    pairs = [
        f"{c.__class__.__name__}"
        f"+{s.__class__.__name__.replace('Strategy', '')}"
        for c, (_, s) in zip(creatures, opponents)
    ]
    print(f"[ {', '.join(f'({p})' for p in pairs)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    print("* Battle *")
    creatures = [f.create_base() for f, _ in opponents]
    creatures[0].describe()
    print(" vs.")
    creatures[1].describe()
    print(" now fight!")
    try:
        for creature, (_, strategy) in zip(creatures, opponents):
            strategy.act(creature)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournaments: {e}")


def main():
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    tournament_run(
            "0 (basic)",
            [
                (flame_factory, NormalStrategy()),
                (transform_factory, AggressiveStrategy()),
            ],
    )
    print()
    tournament_run(
        "1 (error)",
        [
            (transform_factory, AggressiveStrategy()),
            (flame_factory, AggressiveStrategy()),
        ],
    )


if __name__ == "__main__":
    main()
