"""
Normally, each process has its own private memory. If one process modifies a
variable, other processes cannot see the change.

Shared memory is a mechanism that allows multiple processes to access the same
region of memory, avoiding the need to copy data between processes. It is
especially useful for large datasets, such as images or numerical arrays, where
copying would be expensive.

Unlike threads, which automatically share memory, processes require explicit
mechanisms such as shared memory to communicate.
"""

from multiprocessing import Array, Lock, Process, Value, shared_memory

import numpy as np


# Value
#   "i" -> int
#   "d" -> double
#   "f" -> float
#   "b" -> signed char
#   "c" -> char
def increment(counter):
    counter.value += 1


def example_1():
    counter = Value("i", 0)

    processes = []

    for _ in range(5):
        p = Process(target=increment, args=(counter,))

        p.start()

        processes.append(p)

    for p in processes:
        p.join()

    print(counter.value)


# Array
def square(numbers):
    for i in range(len(numbers)):
        numbers[i] *= numbers[i]


def example_2():
    numbers = Array("i", [1, 2, 3, 4, 5])

    p = Process(target=square, args=(numbers,))

    p.start()
    p.join()

    print(list(numbers))


# shared_memory module
def worker(name):
    shm = shared_memory.SharedMemory(name=name)

    buffer = shm.buf

    buffer[0] = 99

    shm.close()


def example_3():
    shm = shared_memory.SharedMemory(create=True, size=10)

    shm.buf[0] = 42

    p = Process(target=worker, args=(shm.name,))

    p.start()
    p.join()

    print(shm.buf[0])

    shm.close()
    shm.unlink()


def example_4():
    shm = shared_memory.SharedMemory(create=True, size=100 * np.int64().nbytes)

    array = np.ndarray((100,), dtype=np.int64, buffer=shm.buf)

    array[:] = np.arange(100)

    print(array[:5])

    shm.close()
    shm.unlink()


# Lock
def safe_increment(counter, lock):
    with lock:
        counter.value += 1


def example_5():
    counter = Value("i", 0)

    lock = Lock()

    workers = []

    for _ in range(100):
        p = Process(target=safe_increment, args=(counter, lock))

        p.start()

        workers.append(p)

    for p in workers:
        p.join()

    print(counter.value)


if __name__ == "__main__":
    example_1()

    example_2()

    example_3()

    example_4()

    example_5()
