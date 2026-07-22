"""
`asyncio` is Python's framework for asynchronous programming. Instead of using
multiple threads or processes, it allows a single thread to manage many tasks
by switching between them whenever one is waiting (for example, on network or
file I/O).

Unlike threading, where the operating system decides when to switch threads,
`asyncio` uses cooperative multitasking: a coroutine runs until it explicitly
yields control with await.

Q: If asyncio uses only one thread, how can multiple tasks appear to run
simultaneously?
A: Only one coroutine executes at a time. Whenever a coroutine reaches an await
on an operation that cannot complete immediately (such as network I/O or
`asyncio.sleep()`), it voluntarily suspends itself. The event loop then
schedules another ready coroutine. Because the program switches between
coroutines while they are waiting, many tasks can make progress concurrently
without creating additional threads.

await:
    Pauses the execution of the coroutine, yields control back to the event
    loop, allowing other tasks to run while waiting.
gather:
    Takes multiple "awaitable" operations, kicks them off concurrently, and
    returns a list of their results.
create_task:
    Wrap a coroutine into a Task and schedule its execution. Return the Task
    object.
wait_for:
    If the target awaitable does not finish within the specified seconds, it is
    automatically canceled, and a TimeoutError is raised.

"""

import asyncio


# First Coroutine
async def hello_world():

    print("Hello")

    await asyncio.sleep(0.5)

    print("World")


def example_1():
    asyncio.run(hello_world())


# Running Multiple Coroutines
async def worker(name):
    print(f"{name} started")

    await asyncio.sleep(0.5)

    print(f"{name} finished")


async def create_multi_workers():

    await asyncio.gather(worker("Task A"), worker("Task B"), worker("Task C"))


def example_2():
    asyncio.run(create_multi_workers())


# Creating Tasks
async def countdown():
    for i in range(5, 0, -1):
        print(i)

        await asyncio.sleep(0.5)


async def create_task():
    # NOTE: instant scheduling
    task = asyncio.create_task(countdown())

    print("Doing something else...")

    await asyncio.sleep(0.5)

    print("Waiting...")

    await task


def example_3():
    asyncio.run(create_task())


# Producer-Consumer
queue = asyncio.Queue()


async def producer():
    for i in range(5):
        print(f"Produced {i}")

        await queue.put(i)

        await asyncio.sleep(1)

    await queue.put(None)


async def consumer():
    while True:
        item = await queue.get()

        if item is None:
            break

        print(f"Consumed {item}")


async def create_producer_consumer():
    await asyncio.gather(producer(), consumer())


def example_4():
    asyncio.run(create_producer_consumer())


# Timeout
async def slow():
    await asyncio.sleep(4)


async def timeout():
    try:
        await asyncio.wait_for(slow(), timeout=1)
    except asyncio.TimeoutError:
        print("Timed out")


def example_5():
    asyncio.run(timeout())


# Event Loop
#
#   while True:
#
#       find coroutine ready to run
#
#       execute it
#
#       if it reaches await:
#
#           suspend it
#
#           run another coroutine

if __name__ == "__main__":
    example_1()

    example_2()

    example_3()

    example_4()

    example_5()
