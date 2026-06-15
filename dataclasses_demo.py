"""
A dataclass is a class decorator that automatically generates common methods
such as `__init__`, `__repr__`, `__eq__`, and optionally ordering methods
`__lt__`, `__le__`, `__gt__`, `__ge__` based on class fields.

Dataclasses are useful when a class primarily exists to hold data rather than
implement complex behavior. They eliminate a large amount of boilerplate while
remaining regular Python classes.
"""

from dataclasses import dataclass, field


# Similar to:
#
# class Item:
#
#    def __init__(self, name, value, weight):
#        self.name = name
#        self.value = value
#        self.weight = weight
#
#    def __repr__(self): ...
#
#    def __eq__(self, other): ...
@dataclass
class Item:
    name: str
    value: int
    weight: float

    display_name: str = field(init=False)

    def __post_init__(self):
        self.display_name = self.name.upper()


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total_value(self):
        return sum(item.value for item in self.items)

    def total_weight(self):
        return sum(item.weight for item in self.items)


def main():
    sword = Item(name="Iron Sword", value=100, weight=5.0)

    shield = Item(name="Wooden Shield", value=50, weight=7.5)

    inventory = Inventory()
    inventory.add(sword)
    inventory.add(shield)

    print(sword)

    print(f"Item display name: {sword.display_name}")

    print(sword == Item("Iron Sword", 100, 5.0))

    print(f"Total value: " f"{inventory.total_value()}")

    print(f"Total weight: " f"{inventory.total_weight()}")


if __name__ == "__main__":
    main()
