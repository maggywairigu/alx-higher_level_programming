# 0x09. Python - Everything is object

This project is part of the curriculum of the ALX High-Level Programming program and focuses on understanding the concept of objects in Python.
It covers various aspects of object-oriented programming (OOP) and explores the differences between immutable and mutable objects.

## Background Context

In this project, we delve deeper into how Python works with different types of objects.
We explore scenarios where variables are modified and examine the resulting behavior.
By understanding these concepts, we can effectively answer questions about Python's specificity and apply the same logic to other variables and types.

## Learning Objectives

By the end of this project, you will be able to explain the following concepts without relying on external resources:

- The awesomeness of Python programming
- What is an object
- The difference between a class, an object, and an instance
- The distinction between immutable and mutable objects
- Understanding references, assignments, and aliases
- Identifying identical variables and variables linked to the same object
- Displaying variable identifiers (memory addresses in CPython)
- Knowing the difference between mutable and immutable types
- Familiarity with built-in mutable and immutable types
- Understanding how Python passes variables to functions

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All script files should end with a newline character
- The first line of all script files should be exactly `#!/usr/bin/python3`
- All files must be executable
- Your code should adhere to the Pycodestyle style guide (version 2.8.*)

### README.md File

A `README.md` file is included at the root of the project directory. This file serves as a guide and provides information about the project.

### .txt Answer Files

- Each task has a corresponding `.txt` file containing the answer.
- Each answer should be written on a single line, without any leading or trailing spaces.
- No shebang line is needed for the `.txt` files.
- All `.txt` files should end with a newline character.

### Mandatory Tasks

The project contains a series of tasks that need to be completed to fulfill the learning objectives. The mandatory tasks are as follows:

#### 0. Who am I?

- File: `0-answer.txt`
- Task: Write the name of the function that returns the type of an object, without using parentheses.

#### 1. Where are you?

- File: `1-answer.txt`
- Task: Write the name of the function that returns the variable identifier (memory address) in the CPython implementation.

#### 2. Right count

- File: `2-answer.txt`
- Task: Determine whether variables `a` and `b` point to the same object. Answer with Yes or No.

#### 3. Right count =

- File: `3-answer.txt`
- Task: Determine whether variables `a` and `b` point to the same object. Answer with Yes or No.

#### 4. Right count =

- File: `4-answer.txt`
- Task: Determine whether variables `a` and `b` point to the same object. Answer with Yes or No.

#### 5. Right count =+

- File: `5-answer.txt`
- Task: Determine whether variables `a` and `b` point to the same object. Answer with Yes or No.

#### 6. Is equal

- File: `6-answer.txt`
- Task: Determine the output of the given code snippet.

#### 7. Is the same

- File: `7-answer.txt`
- Task: Determine the output of the given code snippet.

#### 8. Is really equal

- File: `8-answer.txt`
- Task: Determine the output of the given code snippet.

#### 9. Is really the same

- File: `9-answer.txt`
- Task: Determine the output of the given code snippet.

#### 10. And with a list, is it equal

- File: `10-answer.txt`
- Task: Determine the output of the given code snippet.

#### 11. And with a list, is it the same

- File: `11-answer.txt`
- Task: Determine the output of the given code snippet.

#### 12. And with a list, is it really equal

- File: `12-answer.txt`
- Task: Determine the output of the given code snippet.

#### 13. And with a list, is it really the same

- File: `13-answer.txt`
- Task: Determine the output of the given code snippet.

#### 14. List append

- File: `14-answer.txt`
- Task: Determine the output of the given code snippet.

#### 15. List add

- File: `15-answer.txt`
- Task: Determine the output of the given code snippet.

#### 16. Integer incrementation

- File: `16-answer.txt`
- Task: Determine the output of the given code snippet.

#### 17. List incrementation

- File: `17-answer.txt`
- Task: Determine the output of the given code snippet.

#### 18. List assignation

- File: `18-answer.txt`
- Task: Determine the output of the given code snippet.

#### 19. Copy a list object

- File: `19-copy_list.py`
- Task: Write a function `copy_list(l)` that returns a copy of a list. The input list can contain any type of objects.

#### 20. Tuple or not?

- File: `20-answer.txt`
- Task: Determine whether `a` is a tuple. Answer with Yes or No.

#### 21. Tuple or not?

- File: `21-answer.txt`
- Task: Determine whether `a` is a tuple. Answer with Yes or No.

#### 22. Tuple or not?

- File: `22-answer.txt`
- Task: Determine whether `a` is a tuple. Answer with Yes or No.

#### 23. Tuple or not?

- File: `23-answer.txt`
- Task: Determine whether `a` is a tuple. Answer with Yes or No.

#### 24. Who I am?

- File: `24-answer.txt`
- Task: Determine the output of the given code snippet.

#### 25. Tuple or not

- File: `25-answer.txt`
- Task: Determine the output of the given code snippet.

#### 26. Empty is not empty

- File: `26-answer.txt`
- Task: Determine the output of the given code snippet.

#### 27. Still the same?

- File: `27-answer.txt`
- Task: Determine whether the last line of the code snippet will print `139926795932424`. Answer with Yes or No.

#### 28. Same or not?

- File: `28-answer.txt`
- Task: Determine whether the last line of the code snippet will print `139926795932424`. Answer with Yes or No.

#### 29. #pythonic

- File: `100-magic_string.py`
- Task: Write a function `magic_string()` that returns the string "BestSchool" repeated a number of times equal to the iteration number.

#### 30. Low memory cost

- File: `101-

locked_class.py`
- Task: Implement a class `LockedClass` that prevents the dynamic creation of new instance attributes, except for the attribute `first_name`.

#### 31. int 1/3

- Files: `103-line1.txt`, `103-line2.txt`
- Task: Determine the number of `int` objects created by executing the first and second lines of the code snippet.

#### 32. int 2/3

- Files: `104-line1.txt`, `104-line2.txt`, `104-line3.txt`, `104-line4.txt`, `104-line5.txt`
- Task: Determine the number of `int` objects created by executing each line of the code snippet. Answer additional questions about object deletion.

#### 33. int 3/3

- File: `105-line1.txt`
- Task: Determine the number of `int` objects created and still in memory before the execution of the second line of the code snippet.

#### 34. Clear strings

- Files: `106-line1.txt`, `106-line2.txt`, `106-line3.txt`, `106-line4.txt`, `106-line5.txt`
- Task: Determine the number of string objects created by executing each line of the code snippet. Answer additional questions about object deletion.

