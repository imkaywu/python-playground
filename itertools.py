"""
`itertools` is a standard library module that provides a collection of fast,
memory-efficient iterator building blocks. Instead of creating large
intermediate lists, most itertools functions return lazy iterators that
generate values only when needed.

The module is especially useful when working with large datasets, combinatorial
problems, data pipelines, and generator-based processing. Many of its tools can
replace nested loops with concise, efficient code.
"""

import operator
from itertools import (
    accumulate,
    batched,
    chain,
    combinations,
    combinations_with_replacement,
    compress,
    count,
    cycle,
    dropwhile,
    groupby,
    islice,
    pairwise,
    permutations,
    product,
    repeat,
    takewhile,
)


# ------------------------------------------------------------
# Example 01
# count()
# ------------------------------------------------------------
def example_01():
    print("\n========== Example 01: count() ==========")

    counter = count(start=10, step=5)

    for _ in range(5):
        print(next(counter))


# ------------------------------------------------------------
# Example 02
# cycle()
# ------------------------------------------------------------
def example_02():
    print("\n========== Example 02: cycle() ==========")

    colors = cycle(["Red", "Green", "Blue"])

    for _ in range(8):
        print(next(colors))


# ------------------------------------------------------------
# Example 03
# repeat()
# ------------------------------------------------------------
def example_03():
    print("\n========== Example 03: repeat() ==========")

    for value in repeat("Hello", 4):
        print(value)


# ------------------------------------------------------------
# Example 04
# chain()
# ------------------------------------------------------------
def example_04():
    print("\n========== Example 04: chain() ==========")

    numbers = chain(
        [1, 2],
        [3, 4],
        [5, 6],
    )

    print(list(numbers))


# ------------------------------------------------------------
# Example 05
# chain.from_iterable()
# ------------------------------------------------------------
def example_05():
    print("\n========== Example 05: chain.from_iterable() ==========")

    nested = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    print(list(chain.from_iterable(nested)))


# ------------------------------------------------------------
# Example 06
# islice()
# ------------------------------------------------------------
def example_06():
    print("\n========== Example 06: islice() ==========")

    numbers = count()

    print(list(islice(numbers, 10)))


# ------------------------------------------------------------
# Example 07
# accumulate()
# ------------------------------------------------------------
def example_07():
    print("\n========== Example 07: accumulate() ==========")

    numbers = [1, 2, 3, 4]

    print(list(accumulate(numbers)))


# ------------------------------------------------------------
# Example 08
# accumulate() with multiplication
# ------------------------------------------------------------
def example_08():
    print("\n========== Example 08: accumulate() Multiply ==========")

    numbers = [1, 2, 3, 4]

    print(
        list(
            accumulate(
                numbers,
                operator.mul,
            )
        )
    )


# ------------------------------------------------------------
# Example 09
# compress()
# ------------------------------------------------------------
def example_09():
    print("\n========== Example 09: compress() ==========")

    letters = ["A", "B", "C", "D"]

    selectors = [True, False, True, False]

    print(list(compress(letters, selectors)))


# ------------------------------------------------------------
# Example 10
# takewhile()
# ------------------------------------------------------------
def example_10():
    print("\n========== Example 10: takewhile() ==========")

    numbers = [2, 4, 6, 7, 8, 10]

    result = takewhile(
        lambda x: x % 2 == 0,
        numbers,
    )

    print(list(result))


# ------------------------------------------------------------
# Example 11
# dropwhile()
# ------------------------------------------------------------
def example_11():
    print("\n========== Example 11: dropwhile() ==========")

    numbers = [2, 4, 6, 7, 8, 10]

    result = dropwhile(
        lambda x: x % 2 == 0,
        numbers,
    )

    print(list(result))


# ------------------------------------------------------------
# Example 12
# product()
# ------------------------------------------------------------
def example_12():
    print("\n========== Example 12: product() ==========")

    for pair in product(
        ["A", "B"],
        [1, 2, 3],
    ):
        print(pair)


# ------------------------------------------------------------
# Example 13
# permutations()
# ------------------------------------------------------------
def example_13():
    print("\n========== Example 13: permutations() ==========")

    for p in permutations([1, 2, 3]):
        print(p)


# ------------------------------------------------------------
# Example 14
# combinations()
# ------------------------------------------------------------
def example_14():
    print("\n========== Example 14: combinations() ==========")

    for c in combinations(
        [1, 2, 3, 4],
        2,
    ):
        print(c)


# ------------------------------------------------------------
# Example 15
# combinations_with_replacement()
# ------------------------------------------------------------
def example_15():
    print("\n========== Example 15: combinations_with_replacement() ==========")

    for c in combinations_with_replacement(
        [1, 2, 3],
        2,
    ):
        print(c)


# ------------------------------------------------------------
# Example 16
# groupby()
# ------------------------------------------------------------
def example_16():
    print("\n========== Example 16: groupby() ==========")

    words = [
        "apple",
        "ant",
        "banana",
        "boat",
        "cat",
    ]

    for key, group in groupby(
        words,
        key=lambda word: word[0],
    ):
        print(key, list(group))


# ------------------------------------------------------------
# Example 17
# Why groupby() often needs sorting
# ------------------------------------------------------------
def example_17():
    print("\n========== Example 17: groupby() Consecutive ==========")

    words = [
        "apple",
        "banana",
        "ant",
        "boat",
    ]

    for key, group in groupby(
        words,
        key=lambda word: word[0],
    ):
        print(key, list(group))


# ------------------------------------------------------------
# Example 18
# pairwise()
# ------------------------------------------------------------
def example_18():
    print("\n========== Example 18: pairwise() ==========")

    numbers = [10, 20, 30, 40]

    print(list(pairwise(numbers)))


# ------------------------------------------------------------
# Example 19
# batched()
# Python 3.12+
# ------------------------------------------------------------
def example_19():
    print("\n========== Example 19: batched() ==========")

    numbers = range(10)

    for batch in batched(numbers, 3):
        print(batch)


# ------------------------------------------------------------
# Example 20
# Building an iterator pipeline
# ------------------------------------------------------------
def example_20():
    print("\n========== Example 20: Iterator Pipeline ==========")

    even_numbers = (x for x in count(0, 2))

    first_ten = islice(
        even_numbers,
        10,
    )

    running_sum = accumulate(first_ten)

    print(list(running_sum))


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
