"""
A metaclass is a class of class. A class is created from a metaclass.

Most Python classes are created by the built-in metaclasses.

A custom metaclass allows you to customize what happens when a class is define.

Example:

    class User:
        pass

    u = User()

    print(type(u))
    print(type(User))

Output:
    <class '__main__.User'>
    <class 'type'>

`u` is an instance of `User`,
`User` is an instance of `type`.
"""

registry = {}


class CommandMeta(type):

    def __new__(cls, name, bases, namespace):

        print(
            f"cls: {cls}\n"
            f"name: {name}\n"
            f"bases: {bases}\n"
            f"namespace: {namespace}"
        )
        new_class = super().__new__(cls, name, bases, namespace)

        if name != "Command":
            registry[new_class.name] = new_class

        return new_class


class Command(metaclass=CommandMeta):
    pass


class HelloCommand(Command):

    name = "hello"

    def execute(self):
        print("hello")


class GoodbyeCommand(Command):

    name = "goodbye"

    def execute(self):
        print("goodbye")


def main():

    print(registry)

    cmd = registry["hello"]()

    cmd.execute()


if __name__ == "__main__":
    main()
