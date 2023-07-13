# 0x0A. Python - Inheritance

## Python - OOP - Inheritance

This project covers the concept of inheritance in Python and its implementation. It includes various tasks that require understanding and working with inheritance in object-oriented programming.

## Learning Objectives

By completing this project, you should be able to:

- Explain why Python programming is awesome
- Understand the concepts of superclass, baseclass, and parentclass
- Define and use subclasses
- List attributes and methods of a class or instance
- Add new attributes to an instance
- Inherit a class from another
- Define a class with multiple base classes
- Understand the default class every class inherits from
- Override methods or attributes inherited from the base class
- Access attributes and methods inherited by subclasses
- Understand the purpose of inheritance
- Use built-in functions such as `isinstance`, `issubclass`, `type`, and `super`
- Implement class inheritance and method overriding
- Handle exceptions and raise custom exceptions

## Requirements

- Python Scripts:
  - Allowed editors: vi, vim, emacs
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A README.md file, at the root of the project folder, is mandatory
  - Code should use the pycodestyle (version 2.8.*) style guide
  - All files must be executable
  - The length of the files will be tested using `wc`

- Python Test Cases:
  - Allowed editors: vi, vim, emacs
  - All files should end with a new line
  - All test files should be inside a folder named `tests`
  - All test files should be text files with the `.txt` extension
  - All tests should be executed using the command `python3 -m doctest ./tests/*`
  - All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - Documentation should be informative, explaining the purpose of the module, class, or method
  - The length of the documentation will be verified

## Project Structure

The project consists of multiple Python files, each addressing a specific task related to inheritance. Here is an overview of the files in the project:

- `0-lookup.py`: Contains a function that returns the list of available attributes and methods of an object.
- `1-my_list.py`: Defines a class `MyList` that inherits from `list` and includes a method to print the list in sorted order.
- `2-is_same_class.py`: Contains a function that checks if an object is exactly an instance of a specified class.
- `3-is_kind_of_class.py`: Contains a function that checks if an object is an instance of, or if it inherits from, a specified class.
- `4-inherits_from.py`: Contains a function that checks if an object is an instance of a class that inherited (directly or indirectly) from a specified class.
- `5-base_geometry.py`: Defines an empty class `BaseGeometry`.
- `6-base_geometry.py`: Extends `BaseGeometry` and adds an `area()` method that raises an Exception.
- `7-base_geometry.py`: Extends `BaseGeometry` and adds an `integer_validator()` method for validating integer values.
- `8-rectangle.py`: Inherits from `BaseGeometry` and defines a class `Rectangle` with width and height attributes.
- `9-rectangle.py`: Extends `Rectangle` and overrides the `__str__` method for proper representation.
- `10-square.py`: Inherits from `Rectangle` and defines a class `Square` with a size attribute.
- `11-square.py`: Extends `Square` and overrides the `__str__` method for proper representation.
- `100-my_int.py`: Inherits from `int` and inverts the behavior of the equality operators.
- `101-add_attribute.py`: Contains a function that adds a new attribute to an object if possible.

## Getting Started

To get started, clone the GitHub repository [alx-higher_level_programming](https://github.com/Alx-88/alx-higher_level_programming) to your local machine. Navigate to the `0x0A-python-inheritance` directory, which contains all the task files mentioned above.

## Usage

Each task file can be executed individually to test its implementation. For example, to test task 0, run the following command:

```
./0-main.py
```

To run the test cases for a specific task, use the following command:

```
python3 -m doctest ./tests/FILE_NAME.txt
```

Replace `FILE_NAME` with the name of the test file for the corresponding task.

## Testing

The project includes test files in the `tests` directory for each task. These test files contain sample inputs and expected outputs, which are used to verify the correctness of the implemented functions and classes. You can run the test cases using the command mentioned in the "Usage" section.

## Author

This project was done by @maggywairigu, a student at ALX School.