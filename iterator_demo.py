"""
- An iterable is any object that has an `__iter__` or `__getitem__` method
defined, which can produce an iterator.
- An iterator is an object that has a `__next__` method defined, which keeps
track of the current position and returns the next item each time it is asked.
- Iteration is the process of retrieving items one by one.
"""

from collections.abc import Iterable, Iterator


# ------------------------------------------------------------
# Example 01
# Basic iteration over a list
# ------------------------------------------------------------
def example_01():
    print("\n========== Example 01: Iterate over a List ==========")

    numbers = [10, 20, 30]

    for n in numbers:
        print(n)


# ------------------------------------------------------------
# Example 02
# Creating an iterator with iter()
# ------------------------------------------------------------
def example_02():
    print("\n========== Example 02: iter() ==========")

    numbers = [10, 20, 30]

    iterator = iter(numbers)

    print(iterator)
    print(type(iterator))


# ------------------------------------------------------------
# Example 03
# next()
# ------------------------------------------------------------
def example_03():
    print("\n========== Example 03: next() ==========")

    numbers = [10, 20, 30]

    iterator = iter(numbers)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))


# ------------------------------------------------------------
# Example 04
# StopIteration
# ------------------------------------------------------------
def example_04():
    print("\n========== Example 04: StopIteration ==========")

    numbers = [10, 20]

    iterator = iter(numbers)

    try:
        while True:
            print(next(iterator))

    except StopIteration:
        print("Iterator exhausted.")


# ------------------------------------------------------------
# Example 05
# How a for loop works internally
# ------------------------------------------------------------
def example_05():
    print("\n========== Example 05: Simulating a for Loop ==========")

    numbers = [1, 2, 3]

    iterator = iter(numbers)

    while True:

        try:
            value = next(iterator)
            print(value)

        except StopIteration:
            break


# ------------------------------------------------------------
# Example 06
# Iterable vs Iterator
# ------------------------------------------------------------
def example_06():
    print("\n========== Example 06: Iterable vs Iterator ==========")

    numbers = [1, 2, 3]

    iterator = iter(numbers)

    print("numbers is Iterable :", isinstance(numbers, Iterable))
    print("numbers is Iterator :", isinstance(numbers, Iterator))

    print()

    print("iterator is Iterable:", isinstance(iterator, Iterable))
    print("iterator is Iterator:", isinstance(iterator, Iterator))


# ------------------------------------------------------------
# Example 07
# Strings
# ------------------------------------------------------------
def example_07():
    print("\n========== Example 07: String Iterator ==========")

    iterator = iter("Python")

    while True:

        try:
            print(next(iterator))

        except StopIteration:
            break


# ------------------------------------------------------------
# Example 08
# Dictionary iterator
# ------------------------------------------------------------
def example_08():
    print("\n========== Example 08: Dictionary Iterator ==========")

    person = {
        "name": "Alice",
        "age": 30,
    }

    iterator = iter(person)

    print(next(iterator))
    print(next(iterator))


# ------------------------------------------------------------
# Example 09
# File iterator
# ------------------------------------------------------------
def example_09():
    print("\n========== Example 09: File Iterator ==========")

    filename = "sample.txt"

    with open(filename, "w") as f:
        f.write("Apple\n")
        f.write("Banana\n")
        f.write("Orange\n")

    with open(filename) as f:
        print(next(f).strip())
        print(next(f).strip())


# ------------------------------------------------------------
# Example 10
# Custom iterator
# ------------------------------------------------------------
def example_10():
    print("\n========== Example 10: Custom Iterator ==========")

    class Countdown:

        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self

        def __next__(self):

            if self.current == 0:
                raise StopIteration

            value = self.current
            self.current -= 1

            return value

    counter = Countdown(5)

    for value in counter:
        print(value)


# ------------------------------------------------------------
# Example 11
# Custom iterable
# ------------------------------------------------------------
def example_11():
    print("\n========== Example 11: Custom Iterable ==========")

    class Numbers:

        def __iter__(self):
            return iter([1, 2, 3])

    numbers = Numbers()

    for n in numbers:
        print(n)

    print("Second loop")

    for n in numbers:
        print(n)


# ------------------------------------------------------------
# Example 12
# Exhausted iterator
# ------------------------------------------------------------
def example_12():
    print("\n========== Example 12: Exhausted Iterator ==========")

    iterator = iter([1, 2, 3])

    for x in iterator:
        print(x)

    print("Iterating again:")

    for x in iterator:
        print(x)

    print("(Nothing printed)")


# ------------------------------------------------------------
# Example 13
# Generator is an iterator
# ------------------------------------------------------------
def example_13():
    print("\n========== Example 13: Generator ==========")

    def count():
        yield 1
        yield 2
        yield 3

    generator = count()

    print(isinstance(generator, Iterator))

    print(next(generator))
    print(next(generator))
    print(next(generator))


# ------------------------------------------------------------
# Example 14
# enumerate()
# ------------------------------------------------------------
def example_14():
    print("\n========== Example 14: enumerate ==========")

    letters = ["A", "B", "C"]

    e = enumerate(letters)

    print(type(e))

    for index, value in e:
        print(index, value)


# ------------------------------------------------------------
# Example 15
# zip()
# ------------------------------------------------------------
def example_15():
    print("\n========== Example 15: zip ==========")

    names = ["Alice", "Bob", "Charlie"]
    ages = [20, 25, 30]

    z = zip(names, ages)

    print(type(z))

    pairs = []
    for name, age in z:
        print((name, age))
        pairs.append((name, age))

    print()

    names_, ages_ = list(zip(*pairs))
    print(names_)
    print(ages_)


# ------------------------------------------------------------
# Example 16
# iter() calls __iter__()
# ------------------------------------------------------------
def example_16():
    print("\n========== Example 16: __iter__ is Called ==========")

    class MyCollection:

        def __iter__(self):
            print("__iter__() called")
            return iter([100, 200, 300])

    collection = MyCollection()

    for value in collection:
        print(value)


# ------------------------------------------------------------
# Example 17
# next() calls __next__()
# ------------------------------------------------------------
def example_17():
    print("\n========== Example 17: __next__ is Called ==========")

    class Counter:

        def __init__(self):
            self.value = 1

        def __iter__(self):
            print("__iter__() called")
            return self

        def __next__(self):

            print("__next__() called")

            if self.value > 3:
                raise StopIteration

            current = self.value
            self.value += 1

            return current

    for n in Counter():
        print(n)


# ------------------------------------------------------------
# Example 18
# Multiple independent iterators
# ------------------------------------------------------------
def example_18():
    print("\n========== Example 18: Multiple Iterators ==========")

    numbers = [10, 20, 30]

    it1 = iter(numbers)
    it2 = iter(numbers)

    print(next(it1))
    print(next(it1))

    print()

    print(next(it2))
    print(next(it2))


# ------------------------------------------------------------
# Example 19
# iter(iterator) returns itself
# ------------------------------------------------------------
def example_19():
    print("\n========== Example 19: iter(iterator) ==========")

    iterator = iter([1, 2, 3])

    print(iter(iterator) is iterator)


# ------------------------------------------------------------
# Example 20
# Manual expansion of a for loop
# ------------------------------------------------------------
def example_20():
    print("\n========== Example 20: Full Expansion ==========")

    class Numbers:

        def __iter__(self):
            print("__iter__() called")
            return iter([1, 2, 3])

    numbers = Numbers()

    iterator = iter(numbers)

    while True:

        try:
            value = next(iterator)
            print(value)

        except StopIteration:
            print("StopIteration raised")
            break


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
if __name__ == "__main__":
    example_01()
    example_02()
    example_03()
    example_04()
    example_05()
    example_06()
    example_07()
    example_08()
    example_09()
    example_10()
    example_11()
    example_12()
    example_13()
    example_14()
    example_15()
    example_16()
    example_17()
    example_18()
    example_19()
    example_20()
