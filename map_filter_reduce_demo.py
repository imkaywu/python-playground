"""
`map()`, `filter()`, and `reduce()` are functional programming tools in Python.
They allow you to process collections by applying functions rather than writing
explicit loops. Each has a distinct purpose:

- `map()` transforms every element, returns Iterator type
- `filter()` selects elements that satisfy a condition, returns Iterator type.
- `reduce()` combines all elements into a single result.

Although list comprehensions are often preferred for readability, these
functions remain important
"""

import operator
from functools import reduce


# ------------------------------------------------------------
# Example 01
# Basic map()
# ------------------------------------------------------------
def example_01():
    print("\n========== Example 01: Basic map() ==========")

    numbers = [1, 2, 3, 4]

    result = map(lambda x: x * x, numbers)

    print(list(result))


# ------------------------------------------------------------
# Example 02
# map() with a normal function
# ------------------------------------------------------------
def example_02():
    print("\n========== Example 02: map() with Function ==========")

    def square(x):
        return x * x

    numbers = [1, 2, 3, 4]

    result = map(square, numbers)

    print(list(result))


# ------------------------------------------------------------
# Example 03
# map() over multiple iterables
# ------------------------------------------------------------
def example_03():
    print("\n========== Example 03: map() Multiple Iterables ==========")

    a = [1, 2, 3]
    b = [10, 20, 30]

    result = map(lambda x, y: x + y, a, b)

    print(list(result))


# ------------------------------------------------------------
# Example 04
# filter()
# ------------------------------------------------------------
def example_04():
    print("\n========== Example 04: filter() ==========")

    numbers = [1, 2, 3, 4, 5, 6]

    result = filter(lambda x: x % 2 == 0, numbers)

    print(list(result))


# ------------------------------------------------------------
# Example 05
# filter(None, ...)
# ------------------------------------------------------------
def example_05():
    print("\n========== Example 05: filter(None, ...) ==========")

    values = [0, "", None, "Python", [], 42, False]

    print(list(filter(None, values)))
    print(list(filter(lambda x: x, values)))


# ------------------------------------------------------------
# Example 06
# Basic reduce()
# ------------------------------------------------------------
def example_06():
    print("\n========== Example 06: reduce() ==========")

    numbers = [1, 2, 3, 4]

    result = reduce(lambda a, b: a + b, numbers)

    print(result)


# ------------------------------------------------------------
# Example 07
# Product using reduce()
# ------------------------------------------------------------
def example_07():
    print("\n========== Example 07: Product ==========")

    numbers = [1, 2, 3, 4]

    result = reduce(operator.mul, numbers)

    print(result)


# ------------------------------------------------------------
# Example 08
# Maximum using reduce()
# ------------------------------------------------------------
def example_08():
    print("\n========== Example 08: Maximum ==========")

    numbers = [5, 8, 2, 12, 3]

    maximum = reduce(lambda a, b: a if a > b else b, numbers)

    print(maximum)


# ------------------------------------------------------------
# Example 09
# Chaining map -> filter -> reduce
# ------------------------------------------------------------
def example_09():
    print("\n========== Example 09: Chaining ==========")

    numbers = range(10)

    result = reduce(
        lambda a, b: a + b,
        filter(lambda x: x % 2 == 0, map(lambda x: x * x, numbers)),
    )

    print(result)


# ------------------------------------------------------------
# Example 10
# map() vs list comprehension
# ------------------------------------------------------------
def example_10():
    print("\n========== Example 10: map() vs Comprehension ==========")

    numbers = [1, 2, 3, 4]

    mapped = list(map(lambda x: x * x, numbers))

    comprehension = [x * x for x in numbers]

    print(mapped)
    print(comprehension)


# ------------------------------------------------------------
# Example 11
# filter() vs comprehension
# ------------------------------------------------------------
def example_11():
    print("\n========== Example 11: filter() vs Comprehension ==========")

    numbers = range(10)

    filtered = list(filter(lambda x: x % 2 == 0, numbers))

    comprehension = [x for x in numbers if x % 2 == 0]

    print(filtered)
    print(comprehension)


# ------------------------------------------------------------
# Example 12
# map() is lazy
# ------------------------------------------------------------
def example_12():
    print("\n========== Example 12: map() is Lazy ==========")

    numbers = [1, 2, 3]

    mapped = map(print, numbers)

    print(mapped)

    print("Nothing has executed yet.")

    print(list(mapped))


# ------------------------------------------------------------
# Example 13
# filter() is lazy
# ------------------------------------------------------------
def example_13():
    print("\n========== Example 13: filter() is Lazy ==========")

    numbers = [1, 2, 3, 4]

    filtered = filter(lambda x: x > 2, numbers)

    print(filtered)

    print(next(filtered))
    print(next(filtered))


# ------------------------------------------------------------
# Example 14
# reduce() with initial value
# ------------------------------------------------------------
def example_14():
    print("\n========== Example 14: Initial Value ==========")

    numbers = [1, 2, 3]

    # reduce(function, iterable, initializer)
    result = reduce(lambda a, b: a + b, numbers, 100)

    print(result)


# ------------------------------------------------------------
# Example 15
# Counting total characters
# ------------------------------------------------------------
def example_15():
    print("\n========== Example 15: Character Count ==========")

    words = ["Python", "is", "awesome"]

    # 1st arg: receives the accumulated value from previous iterations
    # 2nd arg: receives each element from the list
    total = reduce(lambda total, word: total + len(word), words, 0)

    print(total)


# ------------------------------------------------------------
# Example 16
# map() returning strings
# ------------------------------------------------------------
def example_16():
    print("\n========== Example 16: String Conversion ==========")

    numbers = [1, 2, 3, 4]

    result = map(str, numbers)

    print(list(result))


# ------------------------------------------------------------
# Example 17
# filter() on objects
# ------------------------------------------------------------
def example_17():
    print("\n========== Example 17: Filtering Objects ==========")

    students = [
        {"name": "Alice", "score": 90},
        {"name": "Bob", "score": 55},
        {"name": "Charlie", "score": 82},
    ]

    passed = filter(lambda s: s["score"] >= 60, students)

    print(list(passed))


# ------------------------------------------------------------
# Example 18
# reduce() to build a dictionary
# ------------------------------------------------------------
def example_18():
    print("\n========== Example 18: Build Dictionary ==========")

    pairs = [
        ("Alice", 90),
        ("Bob", 80),
        ("Charlie", 95),
    ]

    # Union operator | (Python 3.9+) to merge dictionaries
    result = reduce(lambda d, pair: d | {pair[0]: pair[1]}, pairs, {})

    print(result)


# ------------------------------------------------------------
# Example 19
# map() + zip()
# ------------------------------------------------------------
def example_19():
    print("\n========== Example 19: map() with zip() ==========")

    names = ["Alice", "Bob", "Charlie"]
    ages = [20, 25, 30]

    result = map(lambda pair: f"{pair[0]} ({pair[1]})", zip(names, ages))

    print(list(result))


# ------------------------------------------------------------
# Example 20
# One pipeline
# ------------------------------------------------------------
def example_20():
    print("\n========== Example 20: Complete Pipeline ==========")

    numbers = range(20)

    pipeline = map(lambda x: x * 2, filter(lambda x: x % 3 == 0, numbers))

    print(list(pipeline))


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
