"""
A generator is a function that can pause and resume execution using yield.
Unlike a normal function, it doesn't compute everything upfront. Instead, it
produces values one at a time as they're needed.

Generators are primarily used for:
- Processing large files
- Streaming data
- Pipelines
- Infinite sequences
- Memory-efficient iteration

The biggest advantage is that they avoid loading everything into memory at once.
"""

from collections import deque


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def bfs(root):
    """
    Breadth-first traversal generator.
    """
    queue = deque([root])

    while queue:
        node = queue.popleft()

        yield node

        print(f"Appending {node.name}'s children")
        for child in node.children:
            queue.append(child)


def traverse(root, path=None):
    if path is None:
        path = []

    path = path + [root.name]

    if not root.children:
        yield path
        return

    for child in root.children:
        yield from traverse(child, path)


def build_tree():
    ceo = Node("CEO")

    eng = Node("Engineering")
    sales = Node("Sales")
    hr = Node("HR")

    ceo.add_child(eng)
    ceo.add_child(sales)
    ceo.add_child(hr)

    eng.add_child(Node("Backend"))
    eng.add_child(Node("Frontend"))

    sales.add_child(Node("US"))
    sales.add_child(Node("Europe"))

    return ceo


def main():
    root = build_tree()

    for node in bfs(root):
        print(f"Traversing {node.name}")

    for path in traverse(root):
        print(path)


if __name__ == "__main__":
    main()
