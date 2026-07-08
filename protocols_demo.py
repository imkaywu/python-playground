"""
A Protocol defines a set of methods or attributes that a type must have, without
requiring inheritance.

Protocols allow code to depend on capabilities instead of inheritance
hierarchies.
"""

from typing import Protocol, runtime_checkable

# Traditional inheritance version
#   class Write:
#
#    def write(self, message):
#      raise NotImplementedError
#
#   class FileWriter(Writer):
#    pass


# Case 1
# `@runtime_checkable` is a decorator from the `typing` module that makes your
# protocols work with `isinstance()` and `issubclass()` checks at runtime.
@runtime_checkable
class Writer(Protocol):

    def write(self, message: str) -> None: ...


class FileWriter:

    def write(self, message: str) -> None:
        print(f"FILE: {message}")


class ConsoleWriter:

    def write(self, message: str) -> None:
        print(f"CONSOLE: {message}")


def save_log(writer: Writer, message: str):
    if not isinstance(writer, Writer):
        raise TypeError("Must be Writer type")

    writer.write(message)


# Case 2: multiple required methods
class DatabaseConnection(Protocol):

    def connect(self): ...

    def disconnect(self): ...


class PostgreSQL:

    def connect(self):
        print("Connected")

    def disconnect(self):
        print("Disconnected")


# Case 3: protocols can require attributes
class HasName(Protocol):
    name: str


class User:
    def __init__(self, name):
        self.name = name


def greet(obj: HasName):
    print(f"Hello {obj.name}")


def main():
    file_writer = FileWriter()

    console_writer = ConsoleWriter()

    save_log(file_writer, "Application started")

    save_log(console_writer, "Application started")

    greet(User("Alice"))


if __name__ == "__main__":
    main()
