from ex3 import TransformCreatureFactory


def test_transformed_factory(Factory: TransformCreatureFactory):
    print("Testing Creature with transform capability")
    print(" base:")
    p1 = Factory.create_base()
    p2 = Factory.create_evolved()
    p1.describe()
    p1.attack()
    p1.transform()
    p1.attack()
    p1.revert()

    print(" evolved:")
    p2.describe()
    p2.attack()
    p2.transform()
    p2.attack()
    p2.revert()


if __name__ == "__main__":
    factory = TransformCreatureFactory()
    test_transformed_factory(factory)
