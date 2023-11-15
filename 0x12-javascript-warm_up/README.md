# Project Title: 0x12. JavaScript - Warm up

## Description

This project focuses on warm-up exercises in JavaScript, covering fundamental concepts such as scripting, web front-end, variables, data types, operators, control flow, functions, objects, arrays, and more. The goal is to gain a solid understanding of JavaScript basics through practical coding exercises.


## Project Overview

In this project, you will be working with JavaScript for scripting purposes and understanding web front-end development. The tasks are designed to reinforce your knowledge of essential JavaScript concepts.


## Background Context

JavaScript is a versatile language used for both scripting and web development. In this project, the emphasis is on learning basic concepts through scripting. Future stages will involve making the AirBnB project dynamic using JavaScript and JQuery.

## Resources

Before starting the tasks, it's recommended to read or watch the provided resources to grasp essential JavaScript concepts.

- [Writing JavaScript Code](#)
- [Variables](#)
- [Data Types](#)
- [Operators](#)
- [Control Flow](#)
- [Functions](#)
- [Objects and Arrays](#)
- [Module Patterns](#)
- [var, let, and const](#)
- [JavaScript Tutorial](#)
- [Modern JS](#)

## Learning Objectives

By the end of this project, you should be able to:

### General

1. Explain why JavaScript programming is amazing.
2. Run a JavaScript script.
3. Create variables and constants.
4. Differentiate between var, const, and let.
5. Understand all available data types in JavaScript.
6. Use if, if ... else statements.
7. Use comments effectively.
8. Affect values to variables.
9. Use while and for loops.
10. Use break and continue statements.
11. Understand what a function is and how to use functions.
12. Explain what a function without a return statement returns.
13. Understand the scope of variables.
14. Work with arithmetic operators.
15. Manipulate dictionaries.
16. Import a file.

## Copyright - Plagiarism

- Solutions to tasks must be created independently.
- Plagiarism is strictly forbidden and will result in removal from the program.
- Do not publish any content of this project.

## Requirements

### General

- Allowed editors: vi, vim, emacs.
- All files interpreted on Ubuntu 20.04 LTS using Node (version 14.x).
- Files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/node`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should be semistandard compliant (version 16.x.x) with semicolons. Reference: AirBnB style.
- All files must be executable.
- File lengths will be tested using `wc`.

### More Info

- Install Node 14:
  ```bash
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```
- Install semi-standard:
  ```bash
  $ sudo npm install semistandard --global
  ```

## Project Structure

The project is organized into multiple tasks, each addressing specific JavaScript concepts. The tasks are present in the `0x12-javascript-warm_up` directory, and each task has its own corresponding file.

## How to Run

1. Ensure Node.js (version 14.x) is installed on your system.
2. Install semi-standard globally: `$ sudo npm install semistandard --global`.
3. Navigate to the task directory, e.g., `0x12-javascript-warm_up`.
4. Run the JavaScript files using the command: `$ ./filename.js`.

## Task Details

### Task 0: First constant, first print

- Print the message "JavaScript is amazing" using a constant variable.
- Use `console.log(...)` to print output.
- Avoid using `var`.

```bash
$ ./0-javascript_is_amazing.js
JavaScript is amazing
```

### Task 1: 3 languages

- Print three lines: "C is fun," "Python is cool," and "JavaScript is amazing."
- Use `console.log(...)` to print output.
- Avoid using `var`.

```bash
$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
```

### Task 2: Arguments

- Print a message based on the number of arguments passed.
- Use `console.log(...)` to print output.
- Avoid using `var`.
- Reference: `process.argv`.

```bash
$ ./2-arguments.js
No argument
$ ./2-arguments.js Best
Argument found
$ ./2-arguments.js Best School
Arguments found
```
### Task 3: Value of my argument

- Print the first argument passed to the script.
- Use `console.log(...)` to print output.
- Avoid using `var` and `length`.

```bash
$ ./3-value_argument.js
No argument
$ ./3-value_argument.js School
School
```

### Task 4: Create a sentence

- Print two arguments passed to the script in the format: "arg1 is arg2."
- Use `console.log(...)` to print output.
- Avoid using `var`.

```bash
$ ./4-concat.js c cool
c is cool
$ ./4-concat.js c
c is undefined
$ ./4-concat.js
undefined is undefined
```

### Task 5: An Integer

- Print "My number: <first argument converted to integer>" if the first argument can be converted to an integer.
- If the argument can't be converted, print "Not a number."
- Use `console.log(...)` to print output.
- Avoid using `var` and `try/catch`.

```bash
$ ./5-to_integer.js
Not a number
$ ./5-to_integer.js 89
My number: 89
$ ./5-to_integer.js "89"
My number: 89
$ ./5-to_integer.js 89.89
My number: 89
$ ./5-to_integer.js School
Not a number
```

### Task 6: Loop to languages

- Print three lines using an array of strings and a loop.
- The lines should be: "C is fun," "Python is cool," and "JavaScript is amazing."
- Use `console.log(...)` to print output.
- Avoid using `var`, if/else statements, and use only one `console.log`.
- Use a loop (while, for, etc.).

```bash
$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
```

### Task 7: I love C

- Print "C is fun" x times, where x is the first argument of the script.
- If the first argument can't be converted to an integer, print "Missing number of occurrences."
- Use `console.log(...)` to print output.
- Avoid using `var`.
- Use a loop (while, for, etc.).

```bash
$ ./7-multi_c.js 2
C is fun
C is fun
$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ ./7-multi_c.js
Missing number of occurrences
$ ./7-multi_c.js -3
```

### Task 8: Square

- Print a square using the character 'X'.
- The size of the square is the first argument.
- If the first argument can't be converted to an integer, print "Missing size."
- Use `console.log(...)` to print output.
- Avoid using `var`.
- Use a loop (while, for, etc.).

```bash
$ ./8-square.js
Missing size
$ ./8-square.js School
Missing size
$ ./8-square.js 2
XX
XX
$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ ./8-square.js -3
```

### Task 9: Add

- Print the addition of two integers.
- The first and second arguments are the integers.
- Define a function named `add(a, b)` to perform the addition.
- Use `console.log(...)` to print output.
- Avoid using `var`.

```bash
$ ./9-add.js
NaN
$ ./9-add.js 1
NaN
$ ./9-add.js 1 7
8
$ ./9-add.js 13 89
102
```

### Task 10: Factorial

- Compute and print the factorial of the first argument.
- If no argument is provided, the factorial of NaN is 1.
- Implement the factorial computation recursively.
- Use a function and `console.log(...)` to print output.
- Avoid using `var`.

```bash
$ ./10-factorial.js
1
$ ./10-factorial.js 3
6
$ ./10-factorial.js 89
1.6507955160908452e+136
$ ./10-factorial.js 333
Infinity
```

### Task 11: Second biggest!

- Search and print the second biggest integer in the list of arguments.
- Assume all arguments can be converted to integers.
- If no argument is passed, print 0. If there is only one argument, print 0.
- Use `console.log(...)` to print output.
- Avoid using `var`.

```bash
$ ./11-second_biggest.js
0
$ ./11-second_biggest.js 1
0
$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```

### Task 12: Object

- Replace the value 12 with 89 in the provided script.

```bash
$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
```

### Task 13: Add file

- Write a function that returns the addition of two integers.
- The function must be visible from outside.
- The name of the function must be `add`.

```bash
$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
$ ./13-main.js
8
```

### Task 14: Const or not const

- Modify the value of `myVar` to 333 in the provided script.

```bash
$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
$ ./100-main.js
333
```

### Task 15: Call me Moby

- Write a function that executes a given function x times.
- The function must be visible from outside.

```bash
$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
$ ./101-main.js
C is fun
C is fun
C is fun
```

### Task 16: Add me maybe

- Write a function that increments and calls a function.
- The function must be visible from outside.

```bash
$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
$ ./102-main.js
New value: 5
```

### Task 17: Increment object

- Update the script by adding a new function `incr` that increments the integer value.

```bash
$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
