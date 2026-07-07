"""
A decorator is a function that takes another function and returns a modified
version of it. They're commonly used to add cross-cutting behavior such as
logging, caching, retries, authentication, rate limiting, and timing without
changing the original function's code.

def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@decorator
def func():
    pass
"""

import random
import time
from functools import wraps


# Example 1: Decorator with Arguments
def retry(max_attempts=3, delay=1):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Attemp {attempt}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed: {e}")
                    last_exception = e

                    if attempt < max_attempts:
                        time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator


@retry(max_attempts=5, delay=0.5)
def fetch_user_profile(user_id):
    """
    Simulate an unreliable service.
    """
    if random.random() < 0.7:
        raise ConnectionError("Temporary network issue")

    return {"id": user_id, "name": "Alice"}


# Example 2: Class decorator (decorating a function with a class)
class TimerDecorator:
    """A class-based decorator that times how long a function takes to execute"""

    def __init__(self, func):
        self.func = func
        self.execution_count = 0

    def __call__(self, *args, **kwargs):
        import time

        self.execution_count += 1
        start_time = time.time()

        result = self.func(*args, **kwargs)

        end_time = time.time()
        elapsed = end_time - start_time

        print(
            f"Function '{self.func.__name__}' executed {self.execution_count} time(s)"
        )
        print(f"Execution time: {elapsed:.4f} seconds")
        print("-" * 40)

        return result


@TimerDecorator
def slow_function(seconds):
    """Simulates a slow operation"""
    import time

    time.sleep(seconds)
    return f"Completed after {seconds} second(s)"


@TimerDecorator
def calculate_sum(n):
    """Calculates sum of numbers from 1 to n"""
    return sum(range(1, n + 1))


# Example 3: Decorator with parameters using class
class RepeatDecorator:
    """A class-based decorator that repeats a function multiple times"""

    def __init__(self, times=2):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(self.times):
                print(f"Execution {i+1}/{self.times}")
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper


@RepeatDecorator(times=3)
def greet(name):
    return f"Hello {name}!"


# Example 4: Class method decorator (decorating methods inside a class)
def log_method_call(func):
    """A function-based decorator that logs method calls"""

    def wrapper(self, *args, **kwargs):
        print(f"Calling method: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(self, *args, **kwargs)
        print(f"Returned: {result}")
        print("-" * 30)
        return result

    return wrapper


class Calculator:
    def __init__(self, name):
        self.name = name

    @log_method_call
    def add(self, a, b):
        return a + b

    @log_method_call
    def multiply(self, a, b):
        return a * b


# Example 5
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    # @property (getter): makes a method callable without parentheses - like an
    # attribute.
    @property
    def full_name(self):
        """This acts like an attribute but computes the value"""
        return f"{self._first_name} {self._last_name}"

    # @property_name.setter
    @full_name.setter
    def full_name(self, name):
        """Allows setting the full name which updates both parts"""
        first, last = name.split()
        self._first_name = first
        self._last_name = last


# ==================== RUN THE EXAMPLES ====================
def main():
    print("\n" + "=" * 50)
    print("EXAMPLE 1: Decorator with Arguments")
    print("=" * 50)
    try:
        # NOTE: similar to:
        # profile = retry(max_attempts=5, delay=0.5)(fetch_user_profile)(123)
        profile = fetch_user_profile(123)
        print("\nSuccess")
        print(profile)
    except Exception as e:
        print("\nOperation permanently failed")
        print(e)

    print("\n" + "=" * 50)
    print("EXAMPLE 2: TimerDecorator (class decorator)")
    print("=" * 50)

    slow_function(1)
    slow_function(0.5)
    calculate_sum(1000000)  # This will show timing for a large calculation

    print("\n" + "=" * 50)
    print("EXAMPLE 3: RepeatDecorator (parameterized class decorator)")
    print("=" * 50)

    print(greet("Alice"))
    print(greet("Bob"))

    print("\n" + "=" * 50)
    print("EXAMPLE 4: Method decorator inside a class")
    print("=" * 50)

    calc = Calculator("My Calculator")
    calc.add(5, 3)
    calc.multiply(4, 7)

    print("\n" + "=" * 50)
    print("EXAMPLE 5: Property decorator (built-in)")
    print("=" * 50)

    person = Person("John", "Doe")
    print(f"Full name: {person.full_name}")  # Using property like an attribute

    person.full_name = "Jane Smith"  # Using setter
    print(f"Updated full name: {person.full_name}")
    print(f"First name: {person._first_name}")
    print(f"Last name: {person._last_name}")


if __name__ == "__main__":
    main()
