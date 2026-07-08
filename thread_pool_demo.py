"""
ThreadPoolExecutor is a high-level API for running tasks concurrently using
a pool of worker threads. It is commonly used for I/O-bound workloads such as
network requests, file I/O, and database operations.
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# ------------------------------------------------------------
# Example 01
# Submit a single task
# ------------------------------------------------------------
def example_01():
    print("\n========== Example 01: submit() ==========")

    def task():
        print(f"Running in {threading.current_thread().name}")
        time.sleep(1)
        return "Task finished"

    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(task)

        print(future.result())  # blocks until result is ready


# ------------------------------------------------------------
# Example 02
# Multiple submit()
# ------------------------------------------------------------
def example_02():
    print("\n========== Example 02: Multiple Tasks ==========")

    def task(number):
        print(f"Task {number} started")
        time.sleep(1)
        print(f"Task {number} finished")
        return number * number

    with ThreadPoolExecutor(max_workers=3) as executor:

        futures = []

        for i in range(5):
            futures.append(executor.submit(task, i))

        for future in futures:
            print("Result:", future.result())


# ------------------------------------------------------------
# Example 03
# map()
# ------------------------------------------------------------
def example_03():
    print("\n========== Example 03: executor.map() ==========")

    def square(x):
        time.sleep(0.5)
        return x * x

    with ThreadPoolExecutor(max_workers=4) as executor:

        results = executor.map(square, range(8))

        print(list(results))


# ------------------------------------------------------------
# Example 04
# map() preserves order
# ------------------------------------------------------------
def example_04():
    print("\n========== Example 04: map() Order ==========")

    def work(x):

        time.sleep(3 - x)

        print(f"Finished {x}")

        return x

    with ThreadPoolExecutor(max_workers=3) as executor:

        for result in executor.map(work, [0, 1, 2]):
            print("Received:", result)


# ------------------------------------------------------------
# Example 05
# as_completed()
# ------------------------------------------------------------
def example_05():
    print("\n========== Example 05: as_completed() ==========")

    def work(x):

        time.sleep(3 - x)

        return x

    with ThreadPoolExecutor(max_workers=3) as executor:

        futures = [executor.submit(work, i) for i in [0, 1, 2]]

        # `concurrent.futures.as_completed()` is a generator function that
        # takes an iterable of Future objects and yields them in the order of
        # completion (i.e., the order in which they finish execution), rather
        # than the order of submission (the order in which they were created).
        for future in as_completed(futures):
            print("Finished:", future.result())


# ------------------------------------------------------------
# Example 06
# Passing multiple arguments
# ------------------------------------------------------------
def example_06():
    print("\n========== Example 06: Multiple Arguments ==========")

    def add(a, b):
        return a + b

    with ThreadPoolExecutor(max_workers=2) as executor:

        future = executor.submit(add, 10, 20)

        print(future.result())


# ------------------------------------------------------------
# Example 07
# Exception handling
# ------------------------------------------------------------
def example_07():
    print("\n========== Example 07: Exceptions ==========")

    def divide(x):
        return 10 / x

    with ThreadPoolExecutor(max_workers=3) as executor:

        futures = [executor.submit(divide, x) for x in [2, 1, 0]]

        for future in futures:

            try:
                print(future.result())

            except Exception as e:
                print(type(e).__name__, e)


# ------------------------------------------------------------
# Example 08
# Future states
# ------------------------------------------------------------
def example_08():
    print("\n========== Example 08: Future ==========")

    def task():
        time.sleep(2)
        return 100

    with ThreadPoolExecutor(max_workers=1) as executor:

        future = executor.submit(task)

        print("Done?", future.done())

        print(future.result())

        print("Done?", future.done())


# ------------------------------------------------------------
# Example 09
# Thread names
# ------------------------------------------------------------
def example_09():
    print("\n========== Example 09: Thread names ==========")

    def task(index):

        print(f"Task {index} running in", threading.current_thread().name)

        time.sleep(1)

    with ThreadPoolExecutor(max_workers=3) as executor:

        executor.map(task, range(6))


# ------------------------------------------------------------
# Example 10
# max_workers
# ------------------------------------------------------------
def example_10():
    print("\n========== Example 10: max_workers ==========")

    def task(i):

        print(f"Start {i}")

        time.sleep(2)

        print(f"End {i}")

    with ThreadPoolExecutor(max_workers=2) as executor:

        executor.map(task, range(5))


# ------------------------------------------------------------
# Example 11
# Simulated file download
# ------------------------------------------------------------
def example_11():
    print("\n========== Example 11: Download Simulation ==========")

    def download(filename):

        print(f"Downloading {filename}")

        time.sleep(1)

        print(f"Finished {filename}")

    files = [
        "a.txt",
        "b.txt",
        "c.txt",
        "d.txt",
    ]

    with ThreadPoolExecutor(max_workers=4) as executor:

        executor.map(download, files)


# ------------------------------------------------------------
# Example 12
# Simulated API requests
# ------------------------------------------------------------
def example_12():
    print("\n========== Example 12: API Simulation ==========")

    def request(user):

        time.sleep(1)

        return {"user": user, "status": "OK"}

    users = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
    ]

    with ThreadPoolExecutor(max_workers=4) as executor:

        for result in executor.map(request, users):
            print(result)


# ------------------------------------------------------------
# Example 13
# Measuring speedup
# ------------------------------------------------------------
def example_13():
    print("\n========== Example 13: Sequential vs ThreadPool ==========")

    def task():

        time.sleep(1)

    start = time.perf_counter()

    for _ in range(5):
        task()

    print("Sequential:", time.perf_counter() - start)

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=5) as executor:

        list(executor.map(lambda _: task(), range(5)))

    print("ThreadPool:", time.perf_counter() - start)


# ------------------------------------------------------------
# Example 14
# Shutdown happens automatically
# ------------------------------------------------------------
def example_14():
    print("\n========== Example 14: Context Manager ==========")

    def task():

        print("Working")

        time.sleep(1)

    with ThreadPoolExecutor(max_workers=2) as executor:

        executor.submit(task)

    print("Executor has shut down.")


# ------------------------------------------------------------
# Example 15
# Collecting results into a dictionary
# ------------------------------------------------------------
def example_15():
    print("\n========== Example 15: Collect Results ==========")

    def compute(x):

        time.sleep(0.5)

        return x * x

    numbers = [1, 2, 3, 4, 5]

    results = {}

    with ThreadPoolExecutor(max_workers=3) as executor:

        future_to_number = {executor.submit(compute, n): n for n in numbers}

        for future in as_completed(future_to_number):

            number = future_to_number[future]

            results[number] = future.result()

    print(results)


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
