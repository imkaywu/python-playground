import json
from collections import namedtuple


def main():
    # ============================================
    # EXAMPLE 1: Basic NamedTuple
    # ============================================
    print("=" * 50)
    print("EXAMPLE 1: Basic NamedTuple")
    print("=" * 50)

    # Define a named tuple type
    Person = namedtuple("Person", ["name", "age", "city"])

    # Create instances
    person1 = Person("Alice", 30, "New York")
    person2 = Person("Bob", 25, "Los Angeles")

    print(f"Person 1: {person1}")
    print(f"Person 2: {person2}")
    print(f"Person 1 name: {person1.name}")
    print(f"Person 1 age: {person1.age}")
    print(f"Person 1 city: {person1.city}")
    print(f"Index access: {person1[0]}")  # Also works like a tuple

    # ============================================
    # EXAMPLE 2: Alternative Ways to Define
    # ============================================
    print("\n" + "=" * 50)
    print("EXAMPLE 2: Alternative Ways to Define")
    print("=" * 50)

    # Using a string with spaces
    Point = namedtuple("Point", "x y z")
    p1 = Point(1, 2, 3)
    print(f"Point: {p1}")

    # Using a list
    Color = namedtuple("Color", ["red", "green", "blue"])
    c1 = Color(255, 128, 0)
    print(f"Color: {c1}")

    # Using comma-separated string
    Student = namedtuple("Student", "id, name, grade")
    s1 = Student(101, "Emma", "A")
    print(f"Student: {s1}")

    # ============================================
    # EXAMPLE 3: Creating from Different Sources
    # ============================================
    print("\n" + "=" * 50)
    print("EXAMPLE 3: Creating from Different Sources")
    print("=" * 50)

    Book = namedtuple("Book", ["title", "author", "year"])

    # From a list
    book_data = ["1984", "George Orwell", 1949]
    book1 = Book._make(book_data)  # _make creates from iterable
    print(f"From list: {book1}")

    # From a dictionary
    book_dict = {"title": "Dune", "author": "Frank Herbert", "year": 1965}
    book2 = Book(**book_dict)  # Unpack dictionary
    print(f"From dict: {book2}")

    # From keyword arguments
    book3 = Book(title="The Hobbit", author="J.R.R. Tolkien", year=1937)
    print(f"From kwargs: {book3}")

    # ============================================
    # EXAMPLE 4: Useful Methods
    # ============================================
    print("\n" + "=" * 50)
    print("EXAMPLE 4: Useful Methods")
    print("=" * 50)

    Car = namedtuple("Car", ["make", "model", "year", "color"])
    car1 = Car("Toyota", "Camry", 2020, "Blue")

    # _asdict() - Convert to dictionary
    car_dict = car1._asdict()
    print(f"As dictionary: {car_dict}")
    print(f"JSON: {json.dumps(car_dict)}")

    # _replace() - Create a new instance with replaced fields
    car2 = car1._replace(color="Red", year=2022)
    print(f"Original: {car1}")
    print(f"Replaced: {car2}")

    # _fields - Get the field names
    print(f"Field names: {car1._fields}")

    # Getting default values (Python 3.7+)
    CarWithDefaults = namedtuple(
        "CarWithDefaults",
        ["make", "model", "year", "color"],
        defaults=["Unknown", "Unknown", 2000, "White"],
    )
    car3 = CarWithDefaults("Honda")
    print(f"With defaults: {car3}")

    # ============================================
    # EXAMPLE 5: Inheritance and Custom Methods
    # ============================================
    print("\n" + "=" * 50)
    print("EXAMPLE 5: Inheritance and Custom Methods")
    print("=" * 50)

    # You can extend namedtuple with custom methods
    class Vector(namedtuple("Vector", ["x", "y"])):
        """A 2D vector with custom methods"""

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Vector(self.x - other.x, self.y - other.y)

        def magnitude(self):
            return (self.x**2 + self.y**2) ** 0.5

        def dot(self, other):
            return self.x * other.x + self.y * other.y

        def __str__(self):
            return f"Vector({self.x}, {self.y})"

    # Create vectors
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 magnitude = {v1.magnitude():.2f}")
    print(f"v1 · v2 = {v1.dot(v2)}")

    # ============================================
    # EXAMPLE 6: Nested Named Tuples
    # ============================================
    print("\n" + "=" * 50)
    print("EXAMPLE 6: Nested Named Tuples")
    print("=" * 50)

    Address = namedtuple("Address", ["street", "city", "zip_code"])
    Contact = namedtuple("Contact", ["name", "email", "address"])

    address1 = Address("123 Main St", "Springfield", "12345")
    contact1 = Contact("Homer Simpson", "homer@example.com", address1)

    print(f"Contact: {contact1.name}")
    print(f"Email: {contact1.email}")
    print(f"Street: {contact1.address.street}")
    print(f"City: {contact1.address.city}")

    # ============================================
    # EXAMPLE 7: Type Hints (Python 3.6+)
    # ============================================
    print("\n" + "=" * 50)
    print("EXAMPLE 7: Type Hints")
    print("=" * 50)

    from typing import List, Optional

    # Typed named tuple (Python 3.6+ with typing)
    class Product(namedtuple("Product", ["id", "name", "price", "tags"])):
        """Product with type hints"""

        id: int
        name: str
        price: float
        tags: Optional[List[str]] = None

    product1 = Product(101, "Laptop", 999.99, ["electronics", "computers"])
    product2 = Product(102, "Mouse", 29.99, ["peripherals"])

    print(f"Product: {product1.name}, Price: ${product1.price}")
    print(f"Tags: {product1.tags}")

    # ============================================
    # Example 8: Performance Comparison
    # ============================================
    print("\n" + "=" * 50)
    print("EXAMPLE 8: Performance Comparison")
    print("=" * 50)

    import timeit

    # Regular class
    class RegularPerson:
        __slots__ = [
            "name",
            "age",
            "city",
        ]  # For fairness (memory optimization)

        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city

    # Named tuple
    PersonNT = namedtuple("PersonNT", ["name", "age", "city"])

    # Test creation time
    def test_creation():
        RegularPerson("Alice", 30, "New York")

    def test_nt_creation():
        PersonNT("Alice", 30, "New York")

    regular_time = timeit.timeit(test_creation, number=100000)
    nt_time = timeit.timeit(test_nt_creation, number=100000)

    print(f"Regular class creation: {regular_time:.4f} seconds")
    print(f"Named tuple creation: {nt_time:.4f} seconds")
    print(f"Named tuples are {regular_time/nt_time:.2f}x faster to create!")

    # Test memory usage
    import sys

    regular = RegularPerson("Alice", 30, "New York")
    nt = PersonNT("Alice", 30, "New York")

    print(f"Regular class size: {sys.getsizeof(regular)} bytes")
    print(f"Named tuple size: {sys.getsizeof(nt)} bytes")
    print(
        f"Named tuples use {sys.getsizeof(regular)/sys.getsizeof(nt):.2f}x less memory!"
    )


if __name__ == "__main__":
    main()
