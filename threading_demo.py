"""
Threading allows a single process to execute multiple threads concurrently.
Threads share the same memory space, making communication between them fast, but
also introducing the possibility of race conditions when multiple threads access
the same data.

Threading is most effective for I/O-bound tasks (network requests, file
operations, waiting for databases), but it does not speed up CPU-bound Python
code because of the Global Interpreter Lock (GIL), which we'll discuss in the
next topic.
"""

# A synchronized queue class which implements multi-producer, multi-consumer
# queues, useful in threaded programming when information must be exchanged
# safely between multiple threads.
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def download(name):

    for i in range(5):
        print(f"{name}: downloading chunk {i}")
        time.sleep(0.1)


# start()/join()
def example_1():
    t1 = threading.Thread(target=download, args=("File A",))
    t2 = threading.Thread(target=download, args=("File B",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All downloads finished.")


counter = 0


def increment():

    global counter

    for _ in range(100_000):
        counter += 1


# Race condition
def example_2():
    threads = []

    for _ in range(4):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Counter: {counter}")


counter_w_lock = 0
lock = threading.Lock()


def increment_w_lock():

    global counter_w_lock

    for _ in range(100_000):
        with lock:
            counter_w_lock += 1


# Lock
def example_3():
    threads = []

    for _ in range(4):
        t = threading.Thread(target=increment_w_lock)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Counter: {counter_w_lock}")


# Producer-Consumer Pattern
tasks = queue.Queue()  # queue.Queue is thread safe


def producer():
    for i in range(5):
        print(f"Produced {i}")
        tasks.put(i)
        time.sleep(1)

    tasks.put(None)


def consumer():
    while True:
        task = tasks.get()

        if task is None:
            break

        print(f"Consumed {task}")


def example_4():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


# Thread Pool
def square(x):

    time.sleep(1)

    return x * x


def example_5():
    with ThreadPoolExecutor(max_workers=4) as executor:

        results = executor.map(square, range(8))

        print(list(results))


if __name__ == "__main__":
    example_1()

    example_2()

    example_3()

    example_4()

    example_5()
