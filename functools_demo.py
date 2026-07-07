"""
lru_cache: A decorator that caches function results and automatically reuses
previously computed values for the same arguments, avoiding redundant
computation.

partial: A function that creates a new callable by pre-filling some of the
arguments of an existing function.

singledispatch: A decorator that enables function overloading by dispatching to
different implementations based on the type of the first argument.

wraps: A decorator helper that copies metadata (such as name, docstring,
annotations, and module information) from the original function to a wrapper
function.
"""

import time
from functools import lru_cache, partial, singledispatch, wraps


# ================================================
# lru_cache
# ================================================
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# ================================================
# partial
# ================================================
def send_notification(channel, username, message):
    print(f"[{channel}] {username}: {message}")


# ================================================
# singledispatch
# ================================================
@singledispatch
def serialize(obj):
    raise TypeError(f"Unsupported type: {type(obj)}")


@serialize.register
def _(obj: int):
    return str(obj)


@serialize.register
def _(obj: str):
    return obj


@serialize.register
def _(obj: list):
    return ",".join(serialize(x) for x in obj)


# ================================================
# wraps
# ================================================
def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


# ================================================
# main
# ================================================
def main():
    print("=== lru_cache ===")
    start = time.perf_counter()

    print(fib(40))

    elapsed = time.perf_counter() - start

    print(f"Took {elapsed:.6f} seconds")

    print("=== partial ===")
    email_sender = partial(send_notification, "EMAIL")

    sms_sender = partial(send_notification, "SMS")

    email_sender("alice", "Welcome!")

    sms_sender("bob", "Verification code")

    print("=== singledispatch ===")
    print(serialize(123))
    print(serialize("hello"))
    print(serialize([1, 2, "abs"]))

    print("=== wraps ===")
    print(add.__name__)


if __name__ == "__main__":
    main()
