"""
Profiling is the process of measuring where your program spends its time and
memory. Rather than guessing what is slow, profiling lets you identify the
actual bottlenecks so you can optimize the parts of the program that matter.

NOTE:
Example 06 depends on Example 05 because it reads the generated
"profile.prof" file.
"""

import cProfile
import math
import pstats
import sys
import time
import timeit
import tracemalloc
from functools import lru_cache

# time.time(): returns the system wall-clock time (real-world time) as seconds
# since January 1, 1970 (the Unix Epoch).

# time.perf_counter(): returns a high-resolution timer that never goes
# backwards.


# ------------------------------------------------------------
# Example 01
# time.perf_counter()
# ------------------------------------------------------------
def example_01():
    print("\n========== Example 01: perf_counter ==========")

    start = time.perf_counter()

    total = sum(range(1_000_000))

    end = time.perf_counter()

    print("Result:", total)
    print(f"Elapsed: {end - start:.6f} seconds")


# ------------------------------------------------------------
# Example 02
# timeit
# ------------------------------------------------------------
def example_02():
    print("\n========== Example 02: timeit ==========")

    # timeit.timeit(stmt, setup='pass', number=1000000, globals=None)
    #   - stmt: The code you want to time (as a string).
    #   - number: How many times to run stmt. Default is 1,000,000.
    elapsed = timeit.timeit(stmt="sum(range(1000))", number=10000)

    print(f"{elapsed:.6f} seconds")


# ------------------------------------------------------------
# Example 03
# Compare two implementations
# ------------------------------------------------------------
def example_03():
    print("\n========== Example 03: Comparing Implementations ==========")

    list_comp = timeit.timeit("[x*x for x in range(1000)]", number=10000)

    loop = timeit.timeit(
        """
result = []
for x in range(1000):
    result.append(x*x)
""",
        number=10000,
    )

    print(f"List comprehension : {list_comp:.6f}")
    print(f"For loop           : {loop:.6f}")


# ------------------------------------------------------------
# Example 04
# cProfile
# ------------------------------------------------------------
def fibonacci(n):

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def example_04():
    print("\n========== Example 04: cProfile ==========")

    cProfile.run("fibonacci(20)")


# ------------------------------------------------------------
# Example 05
# Save profiling results
# ------------------------------------------------------------
def example_05():
    print("\n========== Example 05: Saving Profile ==========")

    def work():

        total = 0

        for i in range(1_000_000):
            total += i

        return total

    profiler = cProfile.Profile()

    profiler.enable()

    work()

    profiler.disable()

    profiler.dump_stats("profile.prof")

    print("Profile written to profile.prof")


# ------------------------------------------------------------
# Example 06
# Read profiling results
# ------------------------------------------------------------
def example_06():
    print("\n========== Example 06: Reading Profile ==========")

    stats = pstats.Stats("profile.prof")

    stats.sort_stats("cumulative")

    stats.print_stats(10)


# ------------------------------------------------------------
# Example 07
# tracemalloc
# ------------------------------------------------------------
def example_07():
    print("\n========== Example 07: tracemalloc ==========")

    tracemalloc.start()

    numbers = [i for i in range(1_000_000)]

    current, peak = tracemalloc.get_traced_memory()

    print(f"Current: {current / 1024 / 1024:.2f} MB")
    print(f"Peak   : {peak / 1024 / 1024:.2f} MB")

    tracemalloc.stop()

    del numbers


# ------------------------------------------------------------
# Example 08
# Finding memory allocations
# ------------------------------------------------------------
def example_08():
    print("\n========== Example 08: Allocation Statistics ==========")

    tracemalloc.start()

    data = [i for i in range(100000)]

    snapshot = tracemalloc.take_snapshot()

    stats = snapshot.statistics("lineno")

    for stat in stats[:5]:
        print(stat)

    tracemalloc.stop()

    del data


# ------------------------------------------------------------
# Example 09
# Generator vs List memory
# ------------------------------------------------------------
def example_09():
    print("\n========== Example 09: Generator Memory ==========")

    lst = [x for x in range(100000)]

    gen = (x for x in range(100000))

    print("List size      :", sys.getsizeof(lst))
    print("Generator size :", sys.getsizeof(gen))


# ------------------------------------------------------------
# Example 10
# Algorithm improvement
# ------------------------------------------------------------
def example_10():
    print("\n========== Example 10: Better Algorithm ==========")

    result = []

    start = time.perf_counter()

    for i in range(10000):

        if i not in result:
            result.append(i)

    end = time.perf_counter()

    print(f"List version: {end-start:.6f}")

    result = set()

    start = time.perf_counter()

    for i in range(10000):
        result.add(i)

    end = time.perf_counter()

    print(f"Set version : {end-start:.6f}")


# ------------------------------------------------------------
# Example 11
# Built-in functions
# ------------------------------------------------------------
def example_11():
    print("\n========== Example 11: Built-in Functions ==========")

    numbers = list(range(1_000_000))

    start = time.perf_counter()

    total = 0

    for n in numbers:
        total += n

    end = time.perf_counter()

    print(f"Loop : {end-start:.6f}")

    start = time.perf_counter()

    total = sum(numbers)

    end = time.perf_counter()

    print(f"sum() : {end-start:.6f}")


# ------------------------------------------------------------
# Example 12
# Local lookup optimization
# ------------------------------------------------------------
def example_12():
    print("\n========== Example 12: Local Lookup ==========")

    numbers = list(range(100000))

    start = time.perf_counter()

    for n in numbers:
        math.sqrt(n)

    end = time.perf_counter()

    print(f"Attribute lookup : {end-start:.6f}")

    sqrt = math.sqrt

    start = time.perf_counter()

    for n in numbers:
        sqrt(n)

    end = time.perf_counter()

    print(f"Local variable   : {end-start:.6f}")


# ------------------------------------------------------------
# Example 13
# lru_cache optimization
# ------------------------------------------------------------
def example_13():
    print("\n========== Example 13: lru_cache ==========")

    @lru_cache(maxsize=None)
    def fibonacci(n):

        if n < 2:
            return n

        return fibonacci(n - 1) + fibonacci(n - 2)

    start = time.perf_counter()

    print(fibonacci(35))

    end = time.perf_counter()

    print(f"Elapsed: {end-start:.6f}")


# ------------------------------------------------------------
# Example 14
# String concatenation
# ------------------------------------------------------------
def example_14():
    print("\n========== Example 14: String Building ==========")

    start = time.perf_counter()

    s = ""

    for _ in range(10000):
        s += "a"

    end = time.perf_counter()

    print(f"Using += : {end-start:.6f}")

    start = time.perf_counter()

    pieces = []

    for _ in range(10000):
        pieces.append("a")

    s = "".join(pieces)

    end = time.perf_counter()

    print(f"Using join : {end-start:.6f}")


# ------------------------------------------------------------
# Example 15
# Sorting key optimization
# ------------------------------------------------------------
def example_15():
    print("\n========== Example 15: key Function ==========")

    words = ["pear", "banana", "apple", "orange"]

    words.sort(key=len)

    print(words)


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
