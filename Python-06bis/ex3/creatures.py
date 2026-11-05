from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, creature_type: str) -> None:
        self._name: str = name
        self._creature_type: str = creature_type

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        print(f"{self._name} is a {self._creature_type} type Creature")


class Pyrodon(Creature):

    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self):
        print(f"{self._name} uses Flamethrower!")


class Flameling(Creature):

    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        print(f"{self._name} uses Ember!")


class TransformCapability(ABC):

    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class Shiftling(Creature, TransformCapability):

    def __init__(self):
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self):
        if self._transformed:
            print(f"{self._name} performs a boosted strike!")
        else:
            print(f"{self._name} attacks normally!")

    def transform(self):
        self._transformed = True
        print(f"{self._name} shifts into a sharper form!")

    def revert(self):
        self._transformed = False
        print(f"{self._name} returns to normal.")


class Morphagon(Creature, TransformCapability):

    def __init__(self):
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self):
        if self._transformed:
            print(f"{self._name} unleashes a devastating morph strike!")
        else:
            print(f"{self._name} attacks normally!")

    def transform(self):
        self._transformed = True
        print(f"{self._name} morphs into a dragonic battle form!")

    def revert(self):
        self._transformed = False
        print(f"{self._name} stabilizes it's form.")
