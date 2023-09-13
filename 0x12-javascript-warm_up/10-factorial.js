#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const num = parseInt(firstArg);
function factorial (num) {
  if (num === 0) {
    return 1;
  } else if (!isNaN(num)) {
    return num * factorial(num - 1);
  } else {
    return 1;
  }
}
const result = factorial(num);
console.log(result);
