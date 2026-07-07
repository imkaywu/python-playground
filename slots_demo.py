"""
By default, Python stores instance attributes in a dictionary called `__dict__`.
This makes Python objects flexible because new attributes can be added at
runtime.

`__slot__` allows a class to declare exactly which attributes it will have,
eliminating the per-instance dictionary and reducing memory usage
"""

import sys
from dataclasses import dataclass

# PyObject                PyGC_Head
# +--------------------+  +--------------------+
# | ob_refcnt   8 B    |  | next pointer 8 B   |
# +--------------------+  +--------------------+
# | ob_type     8 B    |  | prev pointer 8 B   |
# +--------------------+  +--------------------+
#
# 16 bytes                16 bytes


#         Point object (48 bytes)
#
#         +----------------------+
#         | GC header    16      |
#         | ob_refcount      8   |
#         | ob_type ptr      8   |
#         | __dict__ ptr  8 ------------+
#         | weakref ptr   8      |      |
#         +----------------------+      |
#                                       |
#                                       |
#                                       v
#            __dict__ (296 bytes)
#
#   +----------------------------------------+
#   | hash table                             |
#   |                                        |
#   | "x" -------> int object (28 bytes)     |
#   | "y" -------> int object (28 bytes)     |
#   | "color" --> string (44 bytes)          |
#   +----------------------------------------+
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# +------------------------------+
# | PyGC_Head           16 B     |
# | ob_refcnt            8 B     |
# | ob_type              8 B     |
# | slot x pointer       8 B     |
# | slot y pointer       8 B     |
# +------------------------------+
#
# Total allocated
#
# 16 +16 +16 = 48 bytes
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

    # `__sizeof__()`: ob_refcount + ob_type
    print(f"has __dict__: {hasattr(p, '__dict__')}")
    print(f"raw C level size: {p.__sizeof__()}")  # output: 16
    print(f"Python's reported size: {sys.getsizeof(p)}")  # output: 48
    print(f"__dict__ size: {sys.getsizeof(p.__dict__)}")
    print(f"p.x size: {sys.getsizeof(p.x)}")
    print(f"p.y size: {sys.getsizeof(p.y)}")
    print(f"p.color size: {sys.getsizeof(p.color)}")

    print("-" * 40)

    p2 = Point2(10, 20)
    try:
        p2.color = "red"
    except AttributeError as e:
        print(f"{e}")

    print(f"has __dict__: {hasattr(p2, '__dict__')}")
    print(f"has __slots__: {hasattr(p2, '__slots__')}")
    # `__sizeof__()`: ob_refcount + ob_type + slot x + slot y
    print(f"raw C level size: {p2.__sizeof__()}")  # output: 32
    print(f"Python's reported size: {sys.getsizeof(p2)}")  # output: 48

    print("-" * 40)

    p3 = Point3(10, 20)
    print(f"has __dict__: {hasattr(p3, '__dict__')}")
    print(f"raw C level size: {p3.__sizeof__()}")  # output: 32
    print(f"Python's reported size: {sys.getsizeof(p3)}")  # output: 48

    dog = Dog()
    dog.age = 5


if __name__ == "__main__":
    main()
