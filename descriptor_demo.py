"""
A descriptor is an object that controls what happens when an attribute is
accessed, assigned, or deleted. A descriptor implements one or more of:

    __get__()
    __set__()
    __delete__()

Data descriptor:
    Define both __get__ and __set__ (or __delete__)
    Used for managing attributes where reads and writes need control

Non-Data descriptor:
    Define only __get__
    Used for computed attributes or read-only access.

Descriptors form the foundation of many built-in features such as:

    @property     -> data descriptor
?   classmethod   -> non-data descriptor (alternative ctor)
?   staticmethod  -> non-data descriptor (util function)
"""


class PositiveInteger:

    # NOTE: When python creates a class, it automatically calls `__set_name__`
    # on descriptors found in the class body.
    def __set_name__(self, owner, name):
        self.private_name = "_" + name
        print(f"Creating an attribute name={name} in owner={owner.__name__}")

    def __get__(self, instance, owner):

        print(
            f"Getting instance={instance} attribute name={self.private_name}, owner={owner.__name__}"
        )
        if instance is None:
            return self

        return getattr(instance, self.private_name)

    def __set__(self, instance, value):

        print(
            f"Setting instance={instance} attribute name={self.private_name}, value={value}"
        )

        if not isinstance(value, int):
            raise TypeError("Must be an integer")

        if value <= 0:
            raise ValueError("Must be positive")

        setattr(instance, self.private_name, value)


class User:

    # age.__set_name__(User, "age")
    age = PositiveInteger()  # creates a descriptor object

    def __init__(self, age):
        self.age = age


class NonEmptyString:

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):

        if instance is None:
            return self

        return getattr(instance, self.private_name)

    def __set__(self, instance, value):

        if not isinstance(value, str):
            raise TypeError("Must be a string")

        if not value:
            raise ValueError("Cannot be empty")

        setattr(instance, self.private_name, value)


class Customer:
    name = NonEmptyString()

    def __init__(self, name):
        self.name = name


class Circle:

    def __init__(self, radius):
        self.radius = radius

    # @property (getter): makes a method callable without parentheses - like an
    # attribute.
    @property
    def area(self):
        return 3.14 * self.radius**2


def main():
    user = User(20)

    # Similar to:
    # user.age.__get__(user, User)
    print(user.age)

    # Similar to:
    # user.age.__set__(user, 30)
    user.age = 30

    print(user.age)

    try:
        user.age = -5
    except ValueError as e:
        print(f"{e}")

    customer = Customer("Alice")
    print(customer.name)

    circle = Circle(1)
    print(circle.area)


if __name__ == "__main__":
    main()
