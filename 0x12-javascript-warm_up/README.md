# Captain's Log JavaScript Warm-up

![JavaScript Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/480px-JavaScript-logo.png)

## Introduction
This project consists of a series of JavaScript warm-up exercises designed to help you become familiar with JavaScript programming concepts and practices. These exercises are part of the ALX Software Engineering program and are meant to be completed individually.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Background Context](#background-context)
3. [Resources](#resources)
4. [Learning Objectives](#learning-objectives)
5. [Requirements](#requirements)
6. [Tasks](#tasks)
7. [Copyright and Plagiarism](#copyright-and-plagiarism)

---

## Project Overview

### Project Details
This project is all about JavaScript programming, and it involves completing a series of tasks to improve your JavaScript skills. The tasks are designed to help you understand JavaScript basics, such as variables, data types, operators, loops, functions, and more.

## Background Context

JavaScript is a versatile programming language used for both web development and general-purpose scripting. In this project, you will focus on learning JavaScript for the following purposes:

1. Scripting (similar to what you did with Python)
2. Web front-end development

The initial focus will be on scripting to grasp the fundamental concepts of the language. Later, you will apply your knowledge to make an Airbnb project dynamic using JavaScript and jQuery.

## Resources

To successfully complete this project, you will need to read and learn from the following resources:

- [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)
- [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
- [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
- [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [Module Patterns](https://coryrylan.com/blog/javascript-module-pattern-basics)
- [var, let, and const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
- [JavaScript Tutorial](https://www.javascripttutorial.net/)
- [Modern JS](https://javascript.info/)
  
## Learning Objectives

By the end of this project, you are expected to be able to explain the following concepts to anyone without the help of Google:

### General
- Understand why JavaScript programming is amazing.
- Know how to run a JavaScript script.
- Create variables and constants.
- Differentiate between `var`, `const`, and `let`.
- Identify all the data types available in JavaScript.
- Use `if` and `if...else` statements.
- Comment code effectively.
- Assign values to variables.
- Work with `while` and `for` loops.
- Utilize `break` and `continue` statements.
- Define what a function is and how to use functions.
- Explain the return value of a function that does not use any return statement.
- Understand the scope of variables.
- Know and use arithmetic operators.
- Manipulate dictionaries.
- Import external files.

## Requirements

### General
- Use editors such as `vi`, `vim`, or `emacs`.
- Interpret your files on Ubuntu 20.04 LTS using Node.js (version 14.x).
- Ensure all your files end with a new line.
- The first line of all your files should begin with `#!/usr/bin/node`.
- Include a `README.md` file at the root of your project folder.
- Ensure your code is semistandard compliant (version 16.x.x) with rules of Standard plus semicolons.
- All your files must be executable.
- The length of your files will be tested using `wc`.

### More Info
- Install Node 14:
  ```bash
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```

- Install semistandard:
  ```bash
  $ sudo npm install semistandard --global
  ```

---

## Tasks

### Task 0: First Constant, First Print
- Create a script that prints "JavaScript is amazing."
- Use a constant variable named `myVar` with the value "JavaScript is amazing."
- Print the output using `console.log(...)`.
- You are not allowed to use `var`.

### Task 1: 3 Languages
- Create a script that prints three lines:
  1. "C is fun"
  2. "Python is cool"
  3. "JavaScript is amazing"
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.

### Task 2: Arguments
- Create a script that prints a message depending on the number of arguments passed:
  - If no arguments are passed, print "No argument."
  - If only one argument is passed, print "Argument found."
  - Otherwise, print "Arguments found."
- Use `console.log(...)` to print the output.
- Utilize `process.argv`.

### Task 3: Value of My Argument
- Create a script that prints the first argument passed to it:
  - If no arguments are passed, print "No argument."
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.
- You are not allowed to use `length`.

### Task 4: Create a Sentence
- Create a script that prints two arguments passed to it in the following format: "[arg1] is [arg2]."
- Use `console.log(...)` to print the output.

### Task 5: An Integer
- Create a script that prints "My number: [first argument converted to an integer]" if the first argument can be converted to an integer:
  - If the argument can't be converted to an integer, print "Not a number."
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.
- You are not allowed to use try/catch.

### Task 6: Loop to Languages
- Create a script that prints three lines using an array of strings and a loop:
  1. "C is fun"
  2. "Python is cool"
  3. "JavaScript is amazing"
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.
-

 You are not allowed to use any if/else statement.
- Use only one `console.log(...)`.
- Use a loop (while, for, etc.).

### Task 7: I Love C
- Create a script that prints "C is fun" x times, where x is the first argument of the script.
  - If the first argument can't be converted to an integer, print "Missing number of occurrences."
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.
- Use only two `console.log(...)`.
- Use a loop (while, for, etc.).

### Task 8: Square
- Create a script that prints a square based on the size provided as the first argument:
  - If the first argument can't be converted to an integer, print "Missing size."
  - Use the character "X" to print the square.
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.
- Use a loop (while, for, etc.).

### Task 9: Add
- Create a script that prints the addition of two integers:
  - The first argument is the first integer.
  - The second argument is the second integer.
  - Define a function with the prototype: `function add(a, b)`
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.

### Task 10: Factorial
- Create a script that computes and prints a factorial:
  - The first argument is an integer used for computing the factorial.
  - The factorial of NaN is 1.
  - You must do it recursively.
  - You must use a function.
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.

### Task 11: Second Biggest!
- Create a script that searches for the second biggest integer in the list of arguments.
  - You can assume all arguments can be converted to integers.
  - If no arguments are passed, print 0.
  - If the number of arguments is 1, print 0.
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.

### Task 12: Object
- Update the script to replace the value 12 with 89:
  - You are not allowed to use `var`.

### Task 13: Add File
- Write a function that returns the addition of two integers:
  - The function must be visible from outside.
  - The name of the function must be `add`.
  - You are not allowed to use `var`.

### Task 14: Const or Not Const
- Write a file that modifies the value of `myVar` to 333.

### Task 15: Call Me Moby
- Write a function that executes a function `x` times:
  - The function must be visible from outside.
  - The prototype is `function (x, theFunction)`.
  - You are not allowed to use `var`.

### Task 16: Add Me Maybe
- Write a function that increments and calls a function:
  - The function must be visible from outside.
  - The prototype is `function (number, theFunction)`.
  - You are not allowed to use `var`.

### Task 17: Increment Object
- Update the script to include a new function `incr` that increments the integer value:
  - You are not allowed to use `var`.

---

## Copyright and Plagiarism
- You are tasked with coming up with solutions for the tasks yourself to meet the learning objectives.
- Do not copy and paste someone else's work.
- Do not publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

---

Copyright © 2023 ALX, All rights reserved.
