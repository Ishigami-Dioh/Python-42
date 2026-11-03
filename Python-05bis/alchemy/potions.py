from elements import create_fire, create_water
from alchemy.elements import create_earth, create_air


def strength_potion():
    return (f"Strength potion brewed with '{create_fire()}' "
            f"and '{create_water()}'")


def healing_potion():
    return (f"Healing potion brewed with '{create_earth()}' "
            f"and '{create_air()}'")
