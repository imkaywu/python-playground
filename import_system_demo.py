"""
Python's import system is responsible for finding, loading, and initializing
modules. One of its most important features is that a module is imported only
once per interpreter session. After the first import, Python caches the module
in `sys.modules`, so subsequent imports simply reuse the existing module object.

Understanding the import system is important because it explains circular
imports, module caching, plugin systems, package layouts, and why imports can
sometimes have unexpected side effects.

Some import-system behaviors (module caching, circular imports, packages)
normally require multiple files. For those examples, this script creates
temporary modules/directories so everything remains self-contained.
"""

import importlib
import os
import shutil
import sys
import tempfile
import textwrap
import time


# ------------------------------------------------------------
# Example 1
# A module is only executed once
# ------------------------------------------------------------
def example_01():
    print("\n========== Example 1 ==========")

    temp_dir = tempfile.mkdtemp()

    try:
        with open(os.path.join(temp_dir, "greetings.py"), "w") as f:
            f.write(
                textwrap.dedent(
                    """
                        print("Loading greetings module...")
        
                        message = "Hello!"
        
                        def greet():
                            print(message)
                    """
                )
            )

        sys.path.insert(0, temp_dir)

        import greetings

        greetings.greet()

        print("Importing again...")

        import greetings

        greetings.greet()

    finally:
        sys.path.remove(temp_dir)
        shutil.rmtree(temp_dir)


# ------------------------------------------------------------
# Example 2
# Inspecting sys.modules
# ------------------------------------------------------------
def example_02():
    print("\n========== Example 2 ==========")

    import math

    print("math" in sys.modules)
    print(sys.modules["math"])


# ------------------------------------------------------------
# Example 3
# Modules are singleton objects
# ------------------------------------------------------------
def example_03():
    print("\n========== Example 3 ==========")

    temp_dir = tempfile.mkdtemp()

    try:
        with open(os.path.join(temp_dir, "counter.py"), "w") as f:
            f.write("count = 0\n")

        sys.path.insert(0, temp_dir)

        import counter

        counter.count += 1

        import counter

        print(counter.count)

        a = counter
        b = counter

        print(a is b)

    finally:
        sys.path.remove(temp_dir)
        shutil.rmtree(temp_dir)


# ------------------------------------------------------------
# Example 4
# sys.path
# ------------------------------------------------------------
def example_04():
    print("\n========== Example 4 ==========")

    for path in sys.path:
        print(path)


# ------------------------------------------------------------
# Example 5
# Dynamic import
# ------------------------------------------------------------
def example_05():
    print("\n========== Example 5 ==========")

    module_name = "math"

    module = importlib.import_module(module_name)
    print(module)

    print(module.sqrt(25))


# ------------------------------------------------------------
# Example 6
# Reloading a module
# ------------------------------------------------------------
def example_06():
    print("\n========== Example 6 ==========")

    temp_dir = tempfile.mkdtemp()

    try:
        module_path = os.path.join(temp_dir, "demo.py")

        with open(module_path, "w") as f:
            f.write('value = "Version 1"\n')

        sys.path.insert(0, temp_dir)

        import demo

        print(demo.value)

        # ------------------------------------------
        # importlib.reload() re-executes the module, but Python may reuse
        # cached bytecode (__pycache__) if the file's modification time hasn't
        # changed (often 1-second resolution). If the file is rewritten too
        # quickly, reload() may still execute the old bytecode.

        # solution 1:
        # time.sleep(1.1)

        # solution 2:
        cache = os.path.join(temp_dir, "__pycache__")
        shutil.rmtree(cache, ignore_errors=True)
        # ------------------------------------------

        with open(module_path, "w") as f:
            f.write('value = "Version 2"\n')

        importlib.reload(demo)

        print(demo.value)

    finally:
        sys.path.remove(temp_dir)
        shutil.rmtree(temp_dir)


# ------------------------------------------------------------
# Example 7
# Circular import
# ------------------------------------------------------------
def example_07():
    print("\n========== Example 7 ==========")

    temp_dir = tempfile.mkdtemp()

    try:
        with open(os.path.join(temp_dir, "a.py"), "w") as f:
            f.write(
                textwrap.dedent(
                    """
                        print("Loaded A")
                        import b
        
                        x = 42
                    """
                )
            )

        with open(os.path.join(temp_dir, "b.py"), "w") as f:
            f.write(
                textwrap.dedent(
                    """
                        print("Loaded B")
                        import a
        
                        print(a.x)
                    """
                )
            )

        sys.path.insert(0, temp_dir)

        try:
            import a
        except Exception as e:
            print(type(e).__name__)
            print(e)

    finally:
        sys.path.remove(temp_dir)
        shutil.rmtree(temp_dir)


# ------------------------------------------------------------
# Example 8
# Import aliases
# ------------------------------------------------------------
def example_08():
    print("\n========== Example 8 ==========")

    import math as m

    print(m.pi)


# ------------------------------------------------------------
# Example 9
# Importing selected names
# ------------------------------------------------------------
def example_09():
    print("\n========== Example 9 ==========")

    from math import sqrt

    print(sqrt(49))


# ------------------------------------------------------------
# Example 10
# Top-level code executes during import
# ------------------------------------------------------------
def example_10():
    print("\n========== Example 10 ==========")

    temp_dir = tempfile.mkdtemp()

    try:
        with open(os.path.join(temp_dir, "demo_import.py"), "w") as f:
            f.write(
                textwrap.dedent(
                    """
                        print("Top-level code is executing!")
        
                        x = 123
                    """
                )
            )

        sys.path.insert(0, temp_dir)

        import demo_import

        print(demo_import.x)

    finally:
        sys.path.remove(temp_dir)
        shutil.rmtree(temp_dir)


# ------------------------------------------------------------
# Example 11
# __name__
# ------------------------------------------------------------
def example_11():
    print("\n========== Example 11 ==========")

    print("__name__ inside this file =", __name__)


# ------------------------------------------------------------
# Example 12
# Packages
# ------------------------------------------------------------
def example_12():
    print("\n========== Example 12 ==========")

    temp_dir = tempfile.mkdtemp()

    try:
        package = os.path.join(temp_dir, "utils")
        os.mkdir(package)

        with open(os.path.join(package, "__init__.py"), "w") as f:
            pass

        with open(os.path.join(package, "math_utils.py"), "w") as f:
            f.write(
                textwrap.dedent(
                    """
                        def add(a, b):
                            return a + b
                    """
                )
            )

        sys.path.insert(0, temp_dir)

        from utils.math_utils import add

        print(add(3, 5))

    finally:
        sys.path.remove(temp_dir)
        shutil.rmtree(temp_dir)


# ------------------------------------------------------------
# Example 13
# Absolute import
# ------------------------------------------------------------
def example_13():
    print("\n========== Example 13 ==========")

    import math

    print(math.factorial(6))


# ------------------------------------------------------------
# Example 14
# Module objects
# ------------------------------------------------------------
def example_14():
    print("\n========== Example 14 ==========")

    import math

    print(type(math))
    print(math)
    print(math.__name__)
    print(math.__file__)


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
