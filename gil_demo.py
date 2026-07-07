"""
The Global Interpreter Lock (GIL) is a mutex inside the standard Python
interpreter (CPython) that ensures only one thread executes Python bytecode at
a time.

This means that even on an 8-core CPU, multiple Python threads cannot execute
CPU-bound Python code in parallel within a single process. The GIL exists
primarily to simplify CPython's memory management, particularly its reference
counting implementation.

Q: Why Doesn't Python Remove the GIL?
A: The GIL simplifies CPython's implementation. Without it, nearly every
operation on Python objects would require synchoronization.

Q: Does the GIL affect C extensions
A: Many C libraries release the GIL while performing long-running work.

Q: If the GIL allows only one thread to execute at a time, why does Python even
have threads
A: Because many programs spend most of their time waiting for external
resources such as disk, network, or databases. During these waiting periods,
Python releases the GIL, allowing other threads to make progress. As a result,
threading can significantly improve the throughput of I/O-bound applications
even though it does not provide parallel execution of CPU-bound Python code.
"""

import time
from multiprocessing import Process
from threading import Thread


# CPU-bound
def compute():

    total = 0

    for i in range(10_000_000):
        total += i


def cpu_bound_thread():
    start = time.perf_counter()

    t1 = Thread(target=compute)
    t2 = Thread(target=compute)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()

    print(f"thread: {end - start:.2f} seconds")


def cpu_bound_process():
    start = time.perf_counter()

    p1 = Process(target=compute)
    p2 = Process(target=compute)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()

    print(f"process: {end - start:.2f} seconds")


# IO-bound
def download(name):

    print(f"{name} started")

    time.sleep(3)

    print(f"{name} finished")


def io_bound_task():
    start = time.perf_counter()

    t1 = Thread(target=download, args=("File A",))
    t2 = Thread(target=download, args=("File B",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()

    print(f"thread: {end - start:.2f} seconds")


def main():

    cpu_bound_thread()

    cpu_bound_process()

    io_bound_task()


if __name__ == "__main__":
    main()
