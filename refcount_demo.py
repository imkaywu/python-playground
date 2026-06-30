"""
Python primarily manages memory using reference counting. Every object keeps
track of how many references point to it. When an object's reference count
reaches zero, it is immediately destroyed.

Reference counting alone cannot handle circular references (objects referencing
each other), so Python also includes a cyclic garbage collector, which we'll
cover in the next topic.
"""

import sys


class Person:

    def __init__(self, name):
        self.name = name

    # Python docs recommends avoiding __del__() for resource management:
    #   - object destruction timing isn't guaranteed on all Python
    #     implementations
    #   - exceptions inside __del__() are ignored
    #   - circular references involving __del__() are problematic
    # Instead use:
    #   - context managers `with`
    #   - try/finally
    def __del__(self):
        print(f"Delete {self.name}")


def inspect(obj):
    return sys.getrefcount(obj)


def main():
    # Class object

    # NOTE: Variables don't contain objects, they contain reference.
    #
    # person
    # │
    # ▼
    # +-----------+
    # |  Person   |
    # +-----------+
    person = Person("Alice")

    # NOTE: sys.getrefcount() temporarily creates another reference while
    # calling the function.
    print("Initial:", sys.getrefcount(person))

    print("Inside Function Call:", inspect(person))

    # user ─────┐
    #           │
    # another ──┤
    #           ▼
    #       +-----------+
    #       |  Person   |
    #       +-----------+
    another = person

    print("After assignment:", sys.getrefcount(person))

    del another

    print("After deletion:", sys.getrefcount(person))

    # Mutable object
    numbers = [1, 2, 3]
    numbers2 = numbers.copy()
    alias = numbers
    alias.append(4)
    print(numbers)
    print(alias)
    print(numbers2)


if __name__ == "__main__":
    main()
