"""
`multiprocessing` allows Python programs to run code in multiple processes
instead of multiple threads. Since each process has its own Python interpreter
and memory space, each process also has its own GIL, allowing true parallel
execution of CPU-bound code.

The trade-off is that processes are much heavier than threads. They take longer
to create, use more memory, and cannot directly share Python objects.
"""

import os
import time
from multiprocessing import Manager, Pool, Process, Queue, Value


# Creating Processes
def worker(name):

    print(f"{name} running " f"(PID={os.getpid()})")

    time.sleep(0.1)


def example_1():
    p1 = Process(target=worker, args=("Worker A",))
    p2 = Process(target=worker, args=("Worker B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")


# Global Variables are **Not Shared**
counter = 0


def increment():
    global counter

    counter += 1

    print(counter)


def example_2():
    p = Process(target=increment)

    p.start()
    p.join()

    print(counter)


# Process Pool
def square(x):
    return x * x


def example_3():
    with Pool(4) as pool:
        result = pool.map(square, range(10))

    print(result)


# Returning Values
def enqueue(queue):
    queue.put("Hello from worker!")
    queue.put("Hello again from worker!")


def example_4():
    # A specialized Queue variant used when you need to pass data between
    # separate processes rather than threads.
    queue = Queue()

    p = Process(target=enqueue, args=(queue,))

    p.start()

    message = queue.get()

    p.join()

    print(message)

    message = queue.get()

    print(message)


# Sharing Memory
def count(counter):
    counter.value += 1


def example_5():
    counter = Value("i", 0)

    processes = []

    for _ in range(5):
        p = Process(target=count, args=(counter,))

        p.start()

        processes.append(p)

    for p in processes:
        p.join()

    print(counter.value)


# Sharing Lists
def append_list(shared):
    shared.append("hello")


def example_6():
    # `Manager` provides process-safe shared containers
    manager = Manager()

    shared = manager.list()

    workers = []

    for _ in range(4):
        p = Process(target=append_list, args=(shared,))

        p.start()

        workers.append(p)

    for p in workers:
        p.join()

    print(list(shared))


# CPU parallelism
def compute(_):

    total = 0

    for i in range(30_000_000):
        total += i

    return total


def example_7():
    start = time.perf_counter()

    with Pool(4) as pool:
        pool.map(compute, range(4))

    end = time.perf_counter()

    print(f"{end-start:.2f} seconds")


# NOTE: Without `if __name__ == "__main__"`, Process(...) may repeatedly create
# child processes, causing an infinite spawning loop.
if __name__ == "__main__":
    example_1()

    example_2()

    example_3()

    example_4()

    example_5()

    example_6()

    example_7()
