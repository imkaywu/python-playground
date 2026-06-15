"""
By default, Python stores instance attributes in a dictionary called `__dict__`.
This makes Python objects flexible because new attributes can be added at
runtime.

`__slot__` allows a class to declare exactly which attributes it will have,
eliminating the per-instance dictionary and reducing memory usage
"""

from dataclasses import dataclass


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2:

    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Animal:

    __slots__ = ("name",)


# NOTE: subclass w/o `__slot__` automatically gets a `__dict__`
class Dog(Animal):
    # __slots__ = ()
    pass


@dataclass(slots=True)
class Point3:
    x: int
    y: int


def main():
    p = Point(10, 20)
    print(p.__dict__)

    p.color = "red"
    print(p.__dict__)

    print(f"has __dict__: {hasattr(p, '__dict__')}")
    print(f"sizeof: {p.__sizeof__()}")  # output: 16

    p2 = Point2(10, 20)
    try:
        p2.color = "red"
    except AttributeError as e:
        print(f"{e}")

    print(f"has __dict__: {hasattr(p2, '__dict__')}")
    # TODO: supposed to reduce memory usage?
    print(f"sizeof: {p2.__sizeof__()}")  # output: 32

    p3 = Point3(10, 20)
    print(f"has __dict__: {hasattr(p3, '__dict__')}")
    print(f"sizeof: {p3.__sizeof__()}")

    dog = Dog()
    dog.age = 5


if __name__ == "__main__":
    main()
