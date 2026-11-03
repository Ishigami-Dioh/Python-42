from elements import create_fire
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (f"Recipe transmutating Lead to Gold: brew '{create_air()}' "
            f"and '{strength_potion()}' "
            f"mixed with '{create_fire()}'")
