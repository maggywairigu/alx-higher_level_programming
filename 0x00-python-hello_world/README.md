# Project: 0x00. Python - Hello, World

## Overview

This project is designed to introduce you to Python programming. It covers the basics of Python syntax, printing, string manipulation, and more. The project consists of a series of tasks that require you to write Python scripts to accomplish specific objectives.

## Author

- Guillaume

## Project Duration

This project took place from Jun 5, 2023, 6:00 AM to Jun 6, 2023, 6:00 AM. An auto-review will be launched at the deadline.

## Auto QA Review

- Mandatory tasks: 71.0/89
- Optional tasks: 27.0/27
- Total score: 159.56%

## Concepts

For this project, you are expected to focus on the following concept:

- Python programming

## Author's Disclaimer

Welcome to the Python world!

The first projects are more "C-oriented" with no tricks or funky syntax, just simple Python. If you've already worked with Python, don't worry; more interesting challenges will come your way. You'll soon discover that Python, like many higher-level languages, offers various ways to solve the same problem. Some tasks may have only one correct implementation, while others may have multiple valid approaches. Similar to C, Python has its own style guide called PEP8 (now known as PyCode), which you should follow.

Enjoy your Python journey!

- Guillaume

## Resources

Please read or watch the following resources:

- [The Python tutorial](https://docs.python.org/3/tutorial/) (only the first three chapters)
  - [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
  - [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
  - [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until "3.1.2. Strings" included)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Learn to Program](https://docs.python.org/3/tutorial/introduction.html#learn-to-program)
- [Pycodestyle – Style Guide for Python Code](https://pep8.org/)

## Learning Objectives

By the end of this project, you should be able to explain the following topics to anyone without needing to Google:

### General
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style, and how to check your code with `pycodestyle`

## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file at the root of the folder of this project is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Shell Scripts

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

### C Scripts

- Allowed editors: vi, vim, emacs
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All your files should end with a new line
- Your code should use the Betty style, checked using `betty-style.pl` and `betty-doc.pl`
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

## More Info

### Zen

The Zen of Python, by Tim Peters:

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```

### Pycodestyle

Pycodestyle is now the new standard of Python style code.

## Tasks

### 0. Run Python file

**Mandatory**

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`.

Example:

```shell
$ cat main.py
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./0-run
Best School
$
```

### 1. Run inline

**Mandatory**

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`.

Example:

```shell
$ export PYCODE='print(f"Best School: {88+10}")'
$ ./1-run_inline
Best School: 98
$
```

### 2. Hello, print

**Mandatory**

Write a Python script that prints exactly "Programming is like building a multilingual puzzle", followed by a new line.

Use the `print` function.

### 3. Print integer

**Mandatory**

Complete the source code to print the integer stored in the variable `number`, followed by "Battery street", followed by a new line.

Example:

```shell
$ ./3-print_number.py
98 Battery

 street
```

### 4. Print float

**Mandatory**

Complete the source code to print the float stored in the variable `number` with a precision of 2 digits.

Example:

```shell
$ ./4-print_float.py
Float: 3.14
```

### 5. Print string

**Mandatory**

Complete the source code to print the string stored in the variable `str` three times, followed by its first 9 characters.

Example:

```shell
$ ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

### 6. Play with strings

**Mandatory**

Complete the source code to print "Welcome to Holberton School!" without using any loops or conditional statements. You must use the variables `str1` and `str2` in your code.

### 7. Copy - Cut - Paste

**Mandatory**

Complete the source code to perform the following operations:

- `word_first_3` should contain the first 3 letters of the variable `word`.
- `word_last_2` should contain the last 2 letters of the variable `word`.
- `middle_word` should contain the value of the variable `word` without the first and last letters.

Example:

```shell
$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

### 8. Create a new sentence

**Mandatory**

Complete the source code to print "object-oriented programming with Python", followed by a new line. You are not allowed to create new variables, use string literals, or use loops or conditional statements.

Example:

```shell
$ ./8-concat_edges.py
object-oriented programming with Python
```

### 9. Easter Egg

**Mandatory**

Write a Python script that prints "The Zen of Python", by Tim Peters, followed by a new line. Your script should be a maximum of 98 characters long.

Example:

```shell
$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
```

### 10. Linked list cycle

**Mandatory**

Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: `int check_cycle(listint_t *list);`
Return: `0` if there is no cycle, `1` if there is a cycle
Requirements:
- Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

### 11. Hello, write

**Advanced**

Write a Python script that prints "and that piece of art is useful - Dora Korpar, 2015-10-19", followed by a new line. Your script should print to stderr and exit with the status code 1.

Example:

```shell
$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
$ echo $?
1
```

### 12. Compile

**Advanced**

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable `$PYFILE`.

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`).

Example:

```shell
$ cat main.py
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./101-compile
Compiling main.py ...
$ ls
101-compile  main.py  main.pyc
$ cat main.pyc | zgrep -c "Best School"
1
$ od -t x1 main.pyc  # SYSTEM DEPENDENT => CAN BE DIFFERENT
```

### 13. ByteCode -> Python #1

**Advanced**

Write the Python function `def magic_calculation(a, b)` that does exactly the same as the following Python bytecode:

```python
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

## Conclusion

This project introduces you to Python programming and covers various fundamental concepts. By completing the tasks, you'll gain hands-on experience and become more comfortable with Python's syntax and capabilities. Remember to follow the coding style guidelines and aim for clean and readable code. Enjoy your Python programming journey!
