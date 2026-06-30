"""
Python's primary memory management mechanism is reference counting, but it has
one major limitation: it cannot reclaim objects involved in reference cycles.

To solve this, Python includes a cyclic garbage collector that periodically
searches for groups of objects that reference each other but are no longer
reachable by the program.
"""

import gc


class Node:

    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(f"{self.name} destroyed")


def main():

    a = Node("A")
    b = Node("B")

    # Create a cycle
    # a ─────► Node A
    #            ▲
    #            │
    #            ▼
    # b ─────► Node B
    a.other = b
    b.other = a

    print("Delete a")
    del a

    print("Delete b")
    del b

    # NOTE: Variables are gone, but objects are referencing each other
    # Node A ───► Node B
    #   ▲           │
    #   └───────────┘
    print("Collecting...")

    gc.collect()

    print("Done")


if __name__ == "__main__":
    main()
