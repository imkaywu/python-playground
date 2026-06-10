"""
A context manager is an object that automatically performs setup and cleanup
around a block of code.

Instead of:
    resource = acquire()

    try:
        use(resource)
    finally:
        release(resource)

We can do:
    with resource:
        use(resource)

The return value of __enter__() becomes the value assigned by the as clause.
"""

import time


class Database:
    def begin(self):
        print("BEGIN TRANSACTION")

    def commit(self):
        print("COMMIT")

    def rollback(self):
        print("ROLLBACK")


class Transaction:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.db.begin()
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.db.commit()
        else:
            self.db.rollback()

        # NOTE: continue propagating the exception.
        return False


def successful_transaction():
    db = Database()

    # NOTE: roughly translats into:
    #
    #   tx = Transaction(db)
    #   _ = tx.__enter__()
    #   try:
    #       print("Insert user")
    #   finally:
    #       tx.__exit__(...)
    with Transaction(db):
        print("Insert user")
        print("Update inventory")


def failed_transaction():
    db = Database()

    with Transaction(db):
        print("Insert user")
        raise ValueError("Something went wrong")


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"Took {elapsed:.3f} seconds")


def main():
    # Example 1
    print("=== Success ===")
    successful_transaction()

    print("\n=== Failure ===")

    try:
        failed_transaction()
    except Exception as e:
        print(f"Caught: {e}")

    # Example 2
    with Timer():
        time.sleep(1)


if __name__ == "__main__":
    main()
