"""
The iterator protocol is the mechanism that allows objects to be used in a for
loop. An iterator is any object that implements: `__next__`

and an iterable is any object that can produce an iterator via: `__iter__`.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# Iterator
class TreeIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        node = self.stack.pop()

        for child in reversed(node.children):
            self.stack.append(child)

        return node.value


# Iterable
class Tree:
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return TreeIterator(self.root)


def build_tree():
    root = TreeNode("A")

    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")

    root.add_child(b)
    root.add_child(c)

    b.add_child(d)
    b.add_child(e)

    c.add_child(f)

    return Tree(root)


class BatchIterator:
    def __init__(self, items, batch_size):
        self.items = items
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration

        batch = self.items[self.index : self.index + self.batch_size]

        self.index += self.batch_size

        return batch


def main():
    tree = build_tree()

    # iterator = iter(tree)
    #
    # while True:
    #     try:
    #         node = next(iterator)
    #         print(node)
    #     except StopIterator:
    #         break
    for node in tree:
        print(node)

    for batch in BatchIterator(list(range(10)), batch_size=3):
        print(batch)


if __name__ == "__main__":
    main()
