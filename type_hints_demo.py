"""
Type hints allow you to describe the expected types of variables, parameters,
and return values

Python does NOT enforce type hints at runtime. They exist primarily for:
    - IDE support
    - static analysis
    - documentation
    - detecting bugs before execution

Generics allow type hints to work with arbitrary types while preserving type
safety. Without genrics:

    class Box:
        def __init__(self, value):
            self.value = value

The type checker has no idea what's inside.
"""

from typing import Generic, TypeVar

# Generic Class
T = TypeVar("T")  # TypeVar: creates a type placeholder


class Box(Generic[T]):

    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


# Generic Function
def first_item(items: list[T]) -> T:
    return items[0]


# Multiple Type Parameters
K = TypeVar("K")
V = TypeVar("V")


class Pair(Generic[K, V]):

    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value


# Type alises
type ScoreMap = dict[
    str,
    list[int]
]

def main():
    int_box = Box[int](123)

    str_box = Box[str]("hello")

    print(int_box.get())  # type checker knows this returns int
    print(str_box.get())

    first_item([1, 2, 3])
    first_item(["a", "b", "c"])
    print(first_item.__annotations__)

    pair = Pair[str, int]("age", 25)

    print(pair.key)
    print(pair.value)

    score = ScoreMap = {
        "Alice": [90, 95]
    }
    print(score)

if __name__ == "__main__":
    main()
