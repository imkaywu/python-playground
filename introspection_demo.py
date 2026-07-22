"""
Introspection is Python's ability to examine objects, classes, functions, and
modules at runtime. Unlike many statically compiled languages, Python lets you
inspect an object's type, attributes, methods, inheritance hierarchy, source
code, and even function signatures while the program is running.

This capability powers many Python frameworks, including ORMs, testing
libraries, web frameworks, serializers, and debuggers.
"""

import inspect
import math


# ------------------------------------------------------------
# Example 01
# type()
# ------------------------------------------------------------
def example_01():
    print("\n========== Example 01: type() ==========")

    class Dog:

        def bark(self):
            print("Woof")

    dog = Dog()

    print(type(dog))
    print(type(42))
    print(type("hello"))
    print(type([1, 2, 3]))


# ------------------------------------------------------------
# Example 02
# isinstance()
# ------------------------------------------------------------
def example_02():
    print("\n========== Example 02: isinstance() ==========")

    class Animal:
        pass

    class Dog(Animal):
        pass

    dog = Dog()

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(isinstance(dog, object))


# ------------------------------------------------------------
# Example 03
# dir(): returns a sorted list of all valid attributes and methods of any
# object (or module, class, etc.)
# ------------------------------------------------------------
def example_03():
    print("\n========== Example 03: dir() ==========")

    class Person:

        def greet(self):
            pass

    person = Person()

    print(dir(person))
    print(person.__class__)
    print(person.__dict__)


# ------------------------------------------------------------
# Example 04
# vars() and __dict__
# ------------------------------------------------------------
def example_04():
    print("\n========== Example 04: vars() ==========")

    class Person:

        def __init__(self):
            self.name = "Alice"
            self.age = 30

    person = Person()

    # `vars()` returns the `__dict__` attribute of an object (its namespace of
    # writable attributes) as a dictionary, or acts like `locals()` if called
    # with no argument.
    print(vars(person))
    print(person.__dict__)


# ------------------------------------------------------------
# Example 05
# getattr(), setattr(), hasattr()
# ------------------------------------------------------------
def example_05():
    print("\n========== Example 05: getattr/setattr/hasattr ==========")

    class Person:

        def __init__(self):
            self.name = "Alice"

    person = Person()

    print(getattr(person, "name"))

    setattr(person, "age", 30)

    print(person.age)

    print(hasattr(person, "age"))
    print(hasattr(person, "salary"))


# ------------------------------------------------------------
# Example 06
# Dynamically calling a method
# ------------------------------------------------------------
def example_06():
    print("\n========== Example 06: Dynamic Method Call ==========")

    class Robot:

        def wave(self):
            print("👋 Hello!")

    robot = Robot()

    method = getattr(robot, "wave")

    method()


# ------------------------------------------------------------
# Example 07
# inspect.signature()
# ------------------------------------------------------------
def example_07():
    print("\n========== Example 07: inspect.signature ==========")

    def greet(name, age=18):
        pass

    signature = inspect.signature(greet)

    print(signature)


# ------------------------------------------------------------
# Example 08
# Inspecting function parameters
# ------------------------------------------------------------
def example_08():
    print("\n========== Example 08: Function Parameters ==========")

    def area(width, height=10):
        return width * height

    signature = inspect.signature(area)

    for parameter in signature.parameters.values():
        print(parameter.name, parameter.default)


# ------------------------------------------------------------
# Example 09
# inspect.getsource()
# ------------------------------------------------------------
def example_09():
    print("\n========== Example 09: inspect.getsource ==========")

    def square(x):
        return x * x

    print(inspect.getsource(square))


# ------------------------------------------------------------
# Example 10
# Class hierarchy
# ------------------------------------------------------------
def example_10():
    print("\n========== Example 10: Class Hierarchy ==========")

    class Animal:
        pass

    class Dog(Animal):
        pass

    print("Bases:")
    print(Dog.__bases__)

    print()

    print("MRO:")
    print(Dog.__mro__)


# ------------------------------------------------------------
# Example 11
# Listing methods of a class
# ------------------------------------------------------------
def example_11():
    print("\n========== Example 11: Listing Methods ==========")

    class Calculator:

        def add(self, a, b):
            return a + b

        def subtract(self, a, b):
            return a - b

        @staticmethod
        def version():
            return "1.0"

    methods = inspect.getmembers(Calculator, predicate=inspect.isfunction)

    for name, func in methods:
        print(name)


# ------------------------------------------------------------
# Example 12
# Module introspection
# ------------------------------------------------------------
def example_12():
    print("\n========== Example 12: Module Introspection ==========")

    print(math.__name__)
    print(math.__file__)

    print()

    print(dir(math)[:15])


# ------------------------------------------------------------
# Example 13
# Dynamic type checking
# ------------------------------------------------------------
def example_13():
    print("\n========== Example 13: Dynamic Type Checking ==========")

    def describe(obj):

        if isinstance(obj, int):
            print("Integer")

        elif isinstance(obj, str):
            print("String")

        elif callable(obj):
            print("Callable")

        else:
            print("Unknown")

    describe(10)
    describe("hello")
    describe(print)
    describe([1, 2, 3])


# ------------------------------------------------------------
# Example 14
# callable()
# ------------------------------------------------------------
def example_14():
    print("\n========== Example 14: callable() ==========")

    class Dog:

        def bark(self):
            print("Woof")

    class Counter:

        def __call__(self):
            print("Counter called!")

    def greet():
        pass

    dog = Dog()
    counter = Counter()

    print(callable(greet))
    print(callable(dog.bark))
    print(callable(counter))
    print(callable(dog))


# ------------------------------------------------------------
# Example 15
# inspect.getdoc()
# ------------------------------------------------------------
def example_15():
    print("\n========== Example 15: inspect.getdoc() ==========")

    def square(x):
        """Return x squared."""
        return x * x

    print(inspect.getdoc(square))


# ------------------------------------------------------------
# Example 16
# inspect.getmembers()
# ------------------------------------------------------------
def example_16():
    print("\n========== Example 16: inspect.getmembers() ==========")

    class Person:

        species = "Human"

        def __init__(self):
            self.name = "Alice"

        def greet(self):
            print("Hello")

    person = Person()

    members = inspect.getmembers(person)

    for name, value in members[:15]:
        print(f"{name:20} -> {type(value).__name__}")


# ------------------------------------------------------------
# Example 17
# inspect.isclass(), isfunction(), ismethod()
# ------------------------------------------------------------
def example_17():
    print("\n========== Example 17: inspect Type Predicates ==========")

    class Dog:

        def bark(self):
            pass

    def foo():
        pass

    dog = Dog()

    print(inspect.isclass(Dog))
    print(inspect.isfunction(foo))
    print(inspect.ismethod(dog.bark))
    print(inspect.isfunction(dog.bark))


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
if __name__ == "__main__":
    example_01()
    example_02()
    example_03()
    example_04()
    example_05()
    example_06()
    example_07()
    example_08()
    example_09()
    example_10()
    example_11()
    example_12()
    example_13()
    example_14()
    example_15()
    example_16()
    example_17()
