"""
Python source code (`.py` files) is not executed directly by the CPU. Instead,
CPython first compiles your source code into an intermediate representation
called bytecode, which is then executed by the Python Virtual Machine (PVM).
The PVM is stack-based, with most instructions pushing and popping values from
an evaluation stack.

Bytecode is platform-independent, lower-level than Python source code, but much
higher-level than machine code. Understanding bytecode helps explain Python's
execution model, why some operations are faster than others, and how function
calls, loops, and expressions are actually executed.

Python Source (.py)
        │
        ▼
Compiler
        │
        ▼
Bytecode (.pyc)
        │
        ▼
Python Virtual Machine (PVM)
        │
        ▼
CPU Instructions
"""

import dis


# ------------------------------------------------------------
# Example 01
# Basic bytecode
# ------------------------------------------------------------
def example_01():
    print("\n========== Example 01: Basic Bytecode ==========")

    def add(a, b):
        return a + b

    dis.dis(add)


# ------------------------------------------------------------
# Example 02
# Arithmetic
# ------------------------------------------------------------
def example_02():
    print("\n========== Example 02: Arithmetic ==========")

    def calculate():
        x = 10
        y = 20
        return x * y + 5

    dis.dis(calculate)


# ------------------------------------------------------------
# Example 03
# Loops
# ------------------------------------------------------------
def example_03():
    print("\n========== Example 03: For Loop ==========")

    def total():
        result = 0

        for i in range(3):
            result += i

        return result

    dis.dis(total)


# ------------------------------------------------------------
# Example 04
# Function calls
# ------------------------------------------------------------
def example_04():
    print("\n========== Example 04: Function Calls ==========")

    def square(x):
        return x * x

    def main():
        return square(5)

    dis.dis(main)


# ------------------------------------------------------------
# Example 05
# If statement
# ------------------------------------------------------------
def example_05():
    print("\n========== Example 05: If Statement ==========")

    def maximum(a, b):

        if a > b:
            return a

        return b

    dis.dis(maximum)


# ------------------------------------------------------------
# Example 06
# Individual instructions
# ------------------------------------------------------------
def example_06():
    print("\n========== Example 06: Individual Instructions ==========")

    def cube(x):
        return x**3

    for instruction in dis.get_instructions(cube):
        print(
            f"{instruction.offset:3}",
            f"{instruction.opname:30}",
            instruction.argrepr,
        )


# ------------------------------------------------------------
# Example 07
# Function constants
# ------------------------------------------------------------
def example_07():
    print("\n========== Example 07: Constants ==========")

    def greet():
        message = "Hello"
        return message

    print(greet.__code__.co_consts)


# ------------------------------------------------------------
# Example 08
# Local variables
# ------------------------------------------------------------
def example_08():
    print("\n========== Example 08: Local Variables ==========")

    def calculate():
        x = 10
        y = 20
        return x + y

    print(calculate.__code__.co_varnames)


# ------------------------------------------------------------
# Example 09
# Code object
# ------------------------------------------------------------
def example_09():
    print("\n========== Example 09: Code Object ==========")

    def greet(name):
        print(name)

    code = greet.__code__

    print("Name:", code.co_name)
    print("Argument count:", code.co_argcount)
    print("Filename:", code.co_filename)
    print("First line:", code.co_firstlineno)
    print("Local variables:", code.co_varnames)
    print("Constants:", code.co_consts)


# ------------------------------------------------------------
# Example 10
# List comprehension
# ------------------------------------------------------------
def example_10():
    print("\n========== Example 10: List Comprehension ==========")

    def squares():
        return [x * x for x in range(5)]

    dis.dis(squares)


# ------------------------------------------------------------
# Example 11
# Lambda
# ------------------------------------------------------------
def example_11():
    print("\n========== Example 11: Lambda ==========")

    square = lambda x: x * x

    dis.dis(square)


# ------------------------------------------------------------
# Example 12
# While loop
# ------------------------------------------------------------
def example_12():
    print("\n========== Example 12: While Loop ==========")

    def countdown(n):

        while n > 0:
            n -= 1

        return n

    dis.dis(countdown)


# ------------------------------------------------------------
# Example 13
# Exception handling
# ------------------------------------------------------------
def example_13():
    print("\n========== Example 13: try/except ==========")

    def divide(a, b):

        try:
            return a / b

        except ZeroDivisionError:
            return None

    dis.dis(divide)


# ------------------------------------------------------------
# Example 14
# Global vs Local variables
# ------------------------------------------------------------
GLOBAL_VALUE = 100


def example_14():
    print("\n========== Example 14: Globals vs Locals ==========")

    def foo():
        x = GLOBAL_VALUE
        return x

    dis.dis(foo)


# ------------------------------------------------------------
# Example 15
# Generator bytecode
# ------------------------------------------------------------
def example_15():
    print("\n========== Example 15: Generator ==========")

    def counter():

        for i in range(3):
            yield i

    dis.dis(counter)


# ------------------------------------------------------------
# Example 16
# Nested function
# ------------------------------------------------------------
def example_16():
    print("\n========== Example 16: Nested Function ==========")

    def outer():

        x = 10

        def inner():
            return x

        return inner()

    dis.dis(outer)


# ------------------------------------------------------------
# Example 17
# Closure variables
# ------------------------------------------------------------
def example_17():
    print("\n========== Example 17: Closure Variables ==========")

    def outer():

        x = 42

        def inner():
            return x

        return inner

    fn = outer()

    print(fn.__code__.co_freevars)

    dis.dis(fn)


# ------------------------------------------------------------
# Example 18
# Stack size
# ------------------------------------------------------------
def example_18():
    print("\n========== Example 18: Stack Size ==========")

    def compute():
        return (1 + 2) * (3 + 4)

    print("Stack size:", compute.__code__.co_stacksize)

    dis.dis(compute)


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
    example_18()
