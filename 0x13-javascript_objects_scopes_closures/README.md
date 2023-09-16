# 0x13. JavaScript - Objects, Scopes and Closures

## Overview
This project focuses on JavaScript fundamentals, including objects, scopes, closures, and more. You will be implementing various tasks to reinforce your understanding of these concepts. Make sure to follow the provided guidelines and requirements for each task.

## Author
Guillaume

## Project Duration
September 12, 2023, 6:00 AM - September 13, 2023, 6:00 AM

## Auto QA Review
An auto review will be launched at the deadline to assess the completion of tasks.

## Learning Objectives
Upon completing this project, you should be able to explain the following concepts without relying on external sources:

### General
- The importance of JavaScript programming.
- How to create an object in JavaScript.
- The significance of `this` in JavaScript.
- Understanding of `undefined` in JavaScript.
- The importance of variable type and scope.
- What a closure is in JavaScript.
- Understanding of prototypes in JavaScript.
- How to inherit an object from another.

## Copyright and Plagiarism
Please note that plagiarism is strictly forbidden, and any form of it will result in removal from the program. Ensure that all solutions are your original work.

## Requirements
### General
- Allowed editors: vi, vim, emacs.
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x).
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/node`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should be semistandard compliant, following the rules of Standard with semicolons. Additionally, refer to the AirBnB style for reference.
- All your files must be executable.
- The length of your files will be tested using `wc`.
- You are not allowed to use `var`.

## Resources
To complete this project, you should read or watch the following resources:
- JavaScript object basics
- Object-oriented JavaScript (read all examples!)
- Class - ES6
- super - ES6
- extends - ES6
- Object prototypes
- Inheritance in JavaScript
- Closures
- this/self
- Modern JS

## Installation Instructions
Before starting, ensure that you have Node.js version 14.x and the `semistandard` package installed.

To install Node.js 14, use the following commands:
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

To install `semistandard`, use the following command:
```bash
$ sudo npm install semistandard --global
```

## Tasks
### Task 0: Rectangle #0 (50.0%)
Write an empty class `Rectangle` that defines a rectangle.

You must use the class notation for defining your class.

Example:
```javascript
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);
```

### Task 1: Rectangle #1 (50.0%)
Write a class `Rectangle` that defines a rectangle.

You must use the class notation for defining your class.

The constructor must take 2 arguments `w` and `h`.

Initialize the instance attribute `width` with the value of `w`.

Initialize the instance attribute `height` with the value of `h`.

Example:
```javascript
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);
```

### Task 2: Rectangle #2 (50.0%)
Write a class `Rectangle` that defines a rectangle.

You must use the class notation for defining your class.

The constructor must take 2 arguments `w` and `h`.

Initialize the instance attribute `width` with the value of `w`.

Initialize the instance attribute `height` with the value of `h`.

If `w` or `h` is equal to 0 or not a positive integer, create an empty object.

Example:
```javascript
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);
```

### Task 3: Rectangle #3 (50.0%)
Write a class `Rectangle` that defines a rectangle.

You must use the class notation for defining your class.

The constructor must take 2 arguments: `w` and `h`.

Initialize the instance attribute `width` with the value of `w`.

Initialize the instance attribute `height` with the value of `h`.

If `w` or `h` is equal to 0 or not a positive integer, create an empty object.

Create an instance method called `print()` that prints the rectangle using the character `X`.

Example:
```javascript
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();
```

### Task 4: Rectangle #4 (50.0%)
Write a class `Rectangle` that defines a rectangle.

You must use the class notation for defining your class.

The constructor must take 2 arguments: `w` and `h`.

Initialize the instance attribute `width` with the value of `w`.

Initialize the instance attribute `height` with the value of `h`.

If `w` or `h` is equal to 0 or not a positive integer, create an empty object.

Create an instance method called `print()` that prints the rectangle using the character `X`.

Create an instance method called `rotate()` that exchanges the width and the height of the rectangle.

Create an instance method called `double()` that multiplies the width and the height of the rectangle by 2.

Example:
```javascript
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();
```

### Task 5: Square #0 (50.0%)
Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`.

You must use the class notation for defining your class and `extends`.

The constructor must take 1 argument: `size`.

The constructor of `Rectangle` must be called (by using `super()`).

Example:
```javascript
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();
```

### Task 6: Square #1 (50.0%)
Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`.

You must use the class notation
