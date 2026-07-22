"""
A closure is a function that remembers variables from the scope where it was
created, even after that scope has finished executing.

Closures are commonly used when you want to create configurable functions
without creating a class. Decorators, callbacks, event handlers, and many
framework internals rely heavily on closures.

Function + variable captured from an enclosing scope = closure
"""


# Example 1
class EventBus:
    def __init__(self):
        self.handlers = []

    def subscribe(self, handler):
        self.handlers.append(handler)

    def emit(self, message):
        for handler in self.handlers:
            handler(message)


def create_logger(prefix):
    """
    Creates a new event handler
    'prefix' is captured by the closure
    """

    def handler(message):
        print(f"[{prefix}] {message}")

    return handler


# Example 2: Stateful closure
def create_counter():

    # This variable survives between function calls
    count = 1000

    def increment():
        # Used in nested functions to modify variables from the enclosing
        # (outer) function's scope (not global).
        nonlocal count

        count += 1
        return count

    return increment


def main():
    # Example 1
    bus = EventBus()

    info_logger = create_logger("INFO")
    warning_logger = create_logger("WARNING")
    error_logger = create_logger("ERROR")

    bus.subscribe(info_logger)
    bus.subscribe(warning_logger)
    bus.subscribe(error_logger)

    bus.emit("Server started")

    # Python stores the captured variable inside the function object
    print(info_logger.__closure__)
    print(info_logger.__closure__[0].cell_contents)

    print()

    bus.emit("Disk almost full")

    # Example 2
    counter = create_counter()
    print(counter())
    print(counter())
    print(counter())

    # Example 3
    funcs = []
    for i in range(3):

        def f():
            return i

        funcs.append(f)

    print(f"i={i}")

    for i in range(3):

        def f2(i=i):
            return i

        funcs.append(f2)

    for f in funcs:
        print(f())


if __name__ == "__main__":
    main()
