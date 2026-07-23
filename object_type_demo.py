"""
┌─────────────────────────────────────────────┐
│  type (metaclass)                           │
│  - creates classes (including object)       │
│  - is itself a class                        │
│  - is an instance of itself (special!)      │
│  - inherits from object                     │
└────────────────┬────────────────────────────┘
                 │ creates
                 ▼
┌─────────────────────────────────────────────┐
│  object (ultimate base class)               │
│  - is a class (created by type)             │
│  - is an instance of type                   │
│  - is parent of all classes (incl. type)    │
└─────────────────────────────────────────────┘
"""


def main():
    print(object.__bases__)
    print(type.__bases__)

    print("-" * 40)

    # Statement 1: object is an instance of type
    # Meaning: object is a class, and all classes are instances of type
    print(isinstance(object, type))  # True

    # Statement 2: type is a subclass of object
    # Meaning: type is a class, and all classes inherit from object
    print(isinstance(type, object))  # True

    print("-" * 40)

    print(type(object))
    print(type(type))

    print(object.__class__)
    print(type.__class__)

    print("-" * 40)

    # Also true:
    print(issubclass(type, object))  # True (type inherits from object)
    print(issubclass(object, type))  # False (object doesn't inherit from type)


if __name__ == "__main__":
    main()
